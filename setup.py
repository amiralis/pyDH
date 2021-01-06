
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'pyDH',
  packages = ['pyDH'],
  version = '0.1.6',
  license = 'Apache',
  description = 'Pure Python Implementation of Diffie-Hellman Key Exchange',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Amirali Sanatinia',
  author_email = 'amirali@ccs.neu.edu',
  url = 'https://github.com/amiralis/pyDH',
  keywords = ['crypto', 'Diffie Hellman', 'Key Exchange'],
  classifiers = [
    	'License :: OSI Approved :: Apache Software License',
    	'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
		'Topic :: Security :: Cryptography',
		],
)
