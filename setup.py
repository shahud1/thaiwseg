
from setuptools import setup

REQUIRED_PACKAGES = ['virtualenv','cutkum','deepcut','docker','mtranslate','fuzzywuzzy']

def readme():
    with open('README.md') as f:
        return f.read()
setup(
    name = 'thaiwseg',
    packages=['thaiwseg'],
    include_package_data=True,
    version = '0.9',
    install_requires=REQUIRED_PACKAGES,
    description = 'Advance Thai Word Segmentation',
    long_description = readme(),
    url = 'https://github.com/shahud1/thaiwseg.git',
    author = 'Shahud',
    author_email = 'patiphan_pinkeaw@hotmail.com',
    download_url = 'https://github.com/shahud1/thaiwseg.git/archive/0.1.tar.gz',
    keywords = ['thai', 'word degment', 'NLP', 'Advance Thai Word Segmentation'],
    classifiers = [ 'Development Status :: Beta'],
)
