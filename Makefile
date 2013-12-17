# Makefile
venv/bin/activate:
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -r requirements/testing.txt
	touch venv/bin/activate

venv: venv/bin/activate

test: venv
	. venv/bin/activate; py.test sysmon/

pep8: venv
	. venv/bin/activate; py.test --pep8 --flakes sysmon/

cov: venv
	. venv/bin/activate; py.test --cov=sysmon/ --cov-report=term-missing --cov-report=html sysmon/

all: venv
	. venv/bin/activate; py.test --pep8 --flakes --cov=sysmon/ --cov-report=term-missing --cov-report=html sysmon/

