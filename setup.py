from setuptools import setup, find_packages
import os

setup(
    name='django-system-monitor',
    version='0.2',
    author='Hakan OZAY',
    author_email='hakanzy@gmail.com',
    url='https://github.com/hakanzy/django-sysmon',
    description='View simple system statistics in django admin panel',
    long_description=os.path.join(os.path.dirname(__file__), 'README.md'),
    packages=find_packages(exclude=[]),
    install_requires=[
        'psutil==0.7.1',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
