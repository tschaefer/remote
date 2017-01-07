# -*- coding: utf-8 -*-

from setuptools import setup

setup(
        name='remote',
        version='0.0.1',
        packages=['remote'],
        install_requires=['Flask >= 0.10.1', 'requests >= 2.12.1',
                          'SQLAlchemy >= 1.1.4', 'Flask-SQLAlchemy >= 2.1',
                          'TinyUrl >= 0.1.0', 'feedparser >= 5.2.1'],
        entry_points={'console_scripts': ['remote=remote:main']},
        author='Tobias Schäfer',
        author_email='remote@blackoxorg',
        url='https://github.com/tschaefer/remot',
        description="remote. Remote control for your TV.",
        license='BSD',
        include_package_data=True,
        zip_safe=False
)
