from setuptools import setup, find_packages

setup(
    name='django-sysmon',
    version='0.1',
    author='Hakan OZAY',
    author_email='hakanzy@gmail.com',
    url='https://github.com/hakanzy/django-sysmon',
    description=('Django application for view simple system statistics',
                 ' in django admin panel'),
    long_description=open('README.md').read(),
    packages=find_packages(exclude=[]),
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
