from sysmon.templatetags.sysmon_tags import bytes2human


def kbyte(quantity):
    return 1024. * quantity


def mega(quantity):
    return kbyte(1024.) * quantity


def giga(quantity):
    return mega(1024) * quantity


def tera(quantity):
    return giga(1024) * quantity


def test_bytes():
    assert bytes2human(0.) == '0.0bytes'
    assert bytes2human(0.1) == '0.1bytes'
    assert bytes2human(1.) == '1.0bytes'
    assert bytes2human(100.) == '100.0bytes'
    assert bytes2human(1023.9) == '1023.9bytes'


def test_kb():
    assert bytes2human(kbyte(1)) == '1.0KB'
    assert bytes2human(kbyte(2)) == '2.0KB'
    assert bytes2human(kbyte(1023.9)) == '1023.9KB'


def test_mb():
    assert bytes2human(mega(1.)) == '1.0MB'
    assert bytes2human(mega(123.)) == '123.0MB'
    assert bytes2human(mega(1023.9)) == '1023.9MB'


def test_giga():
    assert bytes2human(giga(1.)) == '1.0GB'
    assert bytes2human(giga(999.2)) == '999.2GB'
    assert bytes2human(giga(1023.9)) == '1023.9GB'


def test_tera():
    assert bytes2human(tera(1.)) == '1.0TB'
    assert bytes2human(tera(999.)) == '999.0TB'
