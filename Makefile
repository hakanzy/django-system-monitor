all: test

test:
	@python demo/manage.py test --with-progressive

run_demo:
	@python demo/manage.py runserver
