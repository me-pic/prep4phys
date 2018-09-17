
__version__ = '0.0.1'

NAME = 'peakdet'
MAINTAINER = 'Ross Markello'
EMAIL = 'rossmarkello@gmail.com'
VERSION = __version__
LICENSE = 'GPLv3'
DESCRIPTION = """\
A toolbox for reproducible physiological data analysis\
"""
LONG_DESCRIPTION = 'README.md'
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'
URL = 'https://github.com/rmarkello/{name}'.format(name=NAME)
DOWNLOAD_URL = ('http://github.com/rmarkello/{name}/archive/{ver}.tar.gz'
                .format(name=NAME, ver=__version__))

INSTALL_REQUIRES = [
    'matplotlib',
    'numpy',
    'scikit-learn',
    'scipy',
]

TESTS_REQUIRES = [
    'codecov',
    'pytest',
    'pytest-cov'
]

EXTRAS_REQUIRES = {
}

PACKAGE_DATA = {
    'peakdet.tests': [
        'data/*'
    ]
}

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3.6',
]
