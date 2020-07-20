# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='conffey',
    version='v3.100.100',
    description=(
        'A library that encapsulates various functions of Python.'
    ),
    long_description=open('README.rst').read(),
    author='C.Z.F.',
    author_email='3023639843@qq.com',
    maintainer='C.Z.F.',
    maintainer_email='3023639843@qq.com',
    license='BSD License',
    packages=[
        'conffey'
    ],
    install_requires=[
        'xpinyin>=0.5.6',
        'Pillow>=7.0.0'
    ],
    platforms=["all"],
    url='https://github.com/super-took/Conffey',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ],
)
