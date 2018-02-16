
from setuptools import setup

REQUIRED_PACKAGES = ['virtualenv','cutkum','deepcut','docker','mtranslate','fuzzywuzzy']

setup(
    name = 'thaiwseg',
    packages=['thaiwseg'],
    include_package_data=True,
    version = '0.9',
    install_requires=REQUIRED_PACKAGES,
    license='MIT',
    description = 'Advance Thai Word Segmentation',
    url = 'https://github.com/shahud1/thaiwseg.git',
    author = 'Shahud',
    author_email = 'patiphan_pinkeaw@outlook.com',
    download_url = 'https://github.com/shahud1/thaiwseg.git/archive/0.1.tar.gz',
    keywords = ['thai', 'word degment', 'NLP', 'Advance Thai Word Segmentation'],
    classifiers = [ 'Development Status :: Beta'],
)
