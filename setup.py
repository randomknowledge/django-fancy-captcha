# coding=utf-8
from setuptools import setup
import finddata


exclude_directories = finddata.standard_exclude_directories + ('./example',)

setup(
    name="django_fancy_captcha",
    author="Florian Finke",
    author_email="flo@randomknowledge.org",
    version='0.0.1',
    packages=['django_fancy_captcha'],
    package_data=finddata.find_package_data(exclude_directories=exclude_directories),
    url='https://github.com/randomknowledge/django_fancy_captcha',
    include_package_data=True,
    license='MIT',
    description='',
    long_description=open('Readme.md').read(),
    zip_safe=False,
    install_requires=['Django>=1.4.1,<=1.5.1'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
