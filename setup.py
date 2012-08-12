#!/usr/bin/python
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

app_name = 'django-chronograph'
package_dir = 'chronograph'

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

packages = []
data_files = []

for dirpath, dirnames, filenames in os.walk(package_dir):
    if '__init__.py' in filenames:
        packages.append('.'.join(dirpath.split(os.sep)))
    elif filenames:
        data_files.append([os.sep.join(dirpath.split(os.sep)), [os.path.join(dirpath, f) for f in filenames]])

setup(
    name=app_name,
    version='0.1.11',
    description='Django chronograph application.',
    url='https://github.com/tim-patterson/django-chronograph',
    author='Weston Nielson',
    author_email='wnielson@gmail.com',
    packages=packages,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    data_files=data_files
)
