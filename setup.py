# SPDX-License-Identifier: GPL-3.0+

from setuptools import setup, find_packages

setup(
    name='estuary_updater',
    version='0.1',
    description='A micro-service that updates the graph database in real-time for Estuary',
    author='Red Hat, Inc.',
    author_email='mprahl@redhat.com',
    license='GPLv3+',
    packages=find_packages(exclude=['tests']),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        'estuary @ https://github.com/release-engineering/estuary-api/tarball/master#egg=estuary',
        'fedmsg',
        'fedmsg[commands]',
        'fedmsg[consumers]',
        'requests',
        'requests_kerberos',
        'koji',
        'moksha.hub',
        'PyOpenSSL',
        'stomper',
        'neomodel>=4.0.3',
    ],
    entry_points="""
    [moksha.consumer]
    estuary_updater = estuary_updater.consumer:EstuaryUpdater
    """
)
