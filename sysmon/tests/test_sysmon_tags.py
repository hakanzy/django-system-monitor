from sysmon.templatetags.sysmon_tags import SysMon


def test_cpu_info_in_context():
    context = {}
    SysMon().render(context)
    assert context.get('cpu_info', None)
    cpu_info = context['cpu_info']
    assert hasattr(cpu_info, 'core')
    assert hasattr(cpu_info, 'used')


def test_cpu_info_in_context_with_fr_language_code(settings):
    context = {}
    SysMon().render(context)
    assert context.get('cpu_info', None)
    cpu_info = context['cpu_info']
    assert ',' not in str(cpu_info.used)


def test_mem_info_in_context():
    context = {}
    SysMon().render(context)
    assert context.get('mem_info', None)
    mem_info = context['mem_info']
    assert hasattr(mem_info, 'total')
    assert hasattr(mem_info, 'used')


def test_mem_info_in_context_with_fr_language_code(settings):
    settings.LANGUAGE_CODE = 'fr-FR'
    context = {}
    SysMon().render(context)
    assert context.get('mem_info', None)
    mem_info = context['mem_info']
    assert ',' not in str(mem_info.total)
    assert ',' not in str(mem_info.used)


def test_disk_partitions_in_context():
    context = {}
    SysMon().render(context)
    assert context.get('partitions', None)
    partitions = context['partitions']
    assert type(partitions) == list
    first_partition = partitions[0]
    assert hasattr(first_partition, 'device')
    assert hasattr(first_partition, 'mountpoint')
    assert hasattr(first_partition, 'fstype')
    assert hasattr(first_partition, 'total')
    assert hasattr(first_partition, 'percent')


def test_disk_partitions_in_context_with_fr_language_code(settings):
    settings.LANGUAGE_CODE = 'fr-FR'
    context = {}
    SysMon().render(context)
    assert context.get('partitions', None)
    partitions = context['partitions']
    assert type(partitions) == list
    first_partition = partitions[0]
    assert ',' not in str(first_partition.total)
    assert ',' not in str(first_partition.percent)


def test_networks_in_context():
    context = {}
    SysMon().render(context)
    assert context.get('networks', None)
    networks = context['networks']
    assert type(networks) == list
    first_network = networks[0]
    assert hasattr(first_network, 'device')
    assert hasattr(first_network, 'sent')
    assert hasattr(first_network, 'recv')
    assert hasattr(first_network, 'pkg_sent')
    assert hasattr(first_network, 'pkg_recv')


def test_processes_in_context():
    context = {}
    SysMon().render(context)
    assert context.get('processes', None)
    processes = context['processes']
    assert type(processes) == list
    first_process = processes[0]
    assert hasattr(first_process, 'pid')
    assert hasattr(first_process, 'name')
    assert hasattr(first_process, 'status')
    assert hasattr(first_process, 'user')
    assert hasattr(first_process, 'memory')
