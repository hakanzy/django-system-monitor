django-system-monitor
=========================

Simple System Monitoring in Django Admin Panel

Features
=========================

- CPU Usage
- Memory Usage
- Disk Usage (with partitions)
- Network Usage
- TOP 10 memory used processes
- Viewing only with django superuser
- It currently supports Linux, Windows, OSX and FreeBSD (psutil supported)

Requirements
=========================
- psutil (https://pypi.python.org/pypi/psutil)

Screenshots
=========================
![Screenshot](https://raw.github.com/hakanzy/django-sysmon/master/docs/screen.png)


Installation/Usage
=========================

 - pip install django-system-monitor

 - After setup, add 'sysmon' to your INSTALLED_APPS, that's all.
