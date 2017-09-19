import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# 使 setup.py 能在任何地方运行
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='colinws-todo',
    version='0.3',
    # packages=find_packages(),
	packages=['todo'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django Todo List application',
    long_description=README,
    url='https://blog.colinspace.com/',
    author='Colin.Liu',
    author_email='colinservice@126.com',
	platforms = 'Linux,Unix',
	keywords = 'Colin,colinws,todo, todo list, django',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
