import sure

from sysmon.templatetags.sysmon_tags import bytes2human


def kbyte(quantity):
  return 1024. * quantity

def mega(quantity):
  return (1024. * 1024.) * quantity

def giga(quantity):
  return mega(1024) * quantity

def tera(quantity):
  return giga(1024) * quantity


def test_bytes():
  bytes2human(0.).should.be.equal('0.0bytes')
  bytes2human(0.1).should.be.equal('0.1bytes')
  bytes2human(1.).should.be.equal('1.0bytes')
  bytes2human(100.).should.be.equal('100.0bytes')
  bytes2human(1023.9).should.be.equal('1023.9bytes')

def test_kb():
  bytes2human(kbyte(1)).should.be.equal('1.0KB')
  bytes2human(kbyte(2)).should.be.equal('2.0KB')
  bytes2human(kbyte(1023.9)).should.be.equal('1023.9KB')

def test_mb():
  bytes2human(mega(1.)).should.be.equal('1.0MB')
  bytes2human(mega(123.)).should.be.equal('123.0MB')
  bytes2human(mega(1023.9)).should.be.equal('1023.9MB')

def test_giga():
  bytes2human(giga(1.)).should.be.equal('1.0GB')
  bytes2human(giga(999.2)).should.be.equal('999.2GB')
  bytes2human(giga(1023.9)).should.be.equal('1023.9GB')

def test_tera():
  bytes2human(tera(1.)).should.be.equal('1.0TB')
  bytes2human(tera(999.)).should.be.equal('999.0TB')
