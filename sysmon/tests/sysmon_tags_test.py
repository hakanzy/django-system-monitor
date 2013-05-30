import sure

from sysmon.templatetags.sysmon_tags import SysMon


def test_cpu_info_in_context():
    context = {}
    SysMon().render(context)

    context.should.have.key('cpu_info')

    cpu_info = context['cpu_info']
    cpu_info.should.have.property('core')
    cpu_info.should.have.property('used')

def test_mem_info_in_context():
    context = {}
    SysMon().render(context)

    context.should.have.key('mem_info')

    mem_info = context['mem_info']
    mem_info.should.have.property('total')
    mem_info.should.have.property('used')

def test_disk_partitions_in_context():
    context = {}
    SysMon().render(context)

    context.should.have.key('partitions')

    partitions = context['partitions']

    partitions.should.be.a(list)

    first_partition = partitions[0]
    first_partition.should.have.property('device')
    first_partition.should.have.property('mountpoint')
    first_partition.should.have.property('fstype')
    first_partition.should.have.property('total')
    first_partition.should.have.property('percent')

def test_networks_in_context():
    context = {}
    SysMon().render(context)

    context.should.have.key('networks')

    networks = context['networks']

    networks.should.be.a(list)

    first_network = networks[0]
    first_network.should.have.property('device')
    first_network.should.have.property('sent')
    first_network.should.have.property('recv')
    first_network.should.have.property('pkg_sent')
    first_network.should.have.property('pkg_recv')

def test_processes_in_context():
    context = {}
    SysMon().render(context)

    context.should.have.key('processes')

    processes = context['processes']

    processes.should.be.a(list)

    first_process = processes[0]
    first_process.should.have.property('pid')
    first_process.should.have.property('name')
    first_process.should.have.property('status')
    first_process.should.have.property('user')
    first_process.should.have.property('memory')
