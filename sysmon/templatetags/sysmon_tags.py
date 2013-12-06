from collections import namedtuple

from django import template

from psutil import AccessDenied


cpuTuple = namedtuple('cpuTuple',
                      'core, used')

memTuple = namedtuple('memTuple',
                      'total, used')

diskPartTuple = namedtuple('diskPartTuple',
                           'device, mountpoint, fstype, total, percent')

networkTuple = namedtuple('networkTuple',
                          'device, sent, recv, pkg_sent, pkg_recv')

processTuple = namedtuple('processTuple',
                          'pid, name, status, user, memory')


def bytes2human(num):
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, x)
        num /= 1024.0
    return "%3.1f%s" % (num, 'TB')


register = template.Library()


class SysMon(template.Node):
    def render(self, context):
        try:
            import psutil as pu
        except:
            context['error_psutil'] = 'not_found'
            return ''

        # cpu
        cpu_info = cpuTuple(
            core=pu.NUM_CPUS,
            used=pu.cpu_percent())

        # memory
        mem_info = memTuple(
            total=bytes2human(pu.TOTAL_PHYMEM),
            used=pu.virtual_memory().percent)

        # disk
        partitions = list()
        for part in pu.disk_partitions():
            partitions.append(
                diskPartTuple(
                    device=part.device,
                    mountpoint=part.mountpoint,
                    fstype=part.fstype,
                    total=bytes2human(
                        pu.disk_usage(part.mountpoint).total),
                    percent=pu.disk_usage(part.mountpoint).percent))

        # network
        networks = list()
        for k, v in pu.network_io_counters(pernic=True).items():
            # Skip loopback interface
            if k == 'lo':
                continue

            networks.append(
                networkTuple(
                    device=k,
                    sent=bytes2human(v.bytes_sent),
                    recv=bytes2human(v.bytes_recv),
                    pkg_sent=v.packets_sent,
                    pkg_recv=v.packets_recv))

        # processes
        processes = list()
        for process in pu.process_iter():

            try:
                percent = process.get_memory_percent()
            except AccessDenied:
                percent = "Access Denied"
            else:
                percent = int(percent)

            processes.append(processTuple(
                pid=process.pid,
                name=process.name,
                status=process.status,
                user=process.username,
                memory=percent))

        processes_sorted = sorted(
            processes, key=lambda p: p.memory, reverse=True)

        all_stats = {
            'cpu_info': cpu_info,
            'mem_info': mem_info,
            'partitions': partitions,
            'networks': networks,
            'processes': processes_sorted[:10],
        }

        context.update(all_stats)

        return ''


@register.tag
def get_system_stats(parser, token):
    return SysMon()
