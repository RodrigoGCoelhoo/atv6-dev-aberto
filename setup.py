from setuptools import setup

setup(name='Rod',
      version='0.1',
      packages=['dev_aberto'],
      install_requires=[
        'requests'
      ],
      author='Rodrigo Coelho',
      scripts=['scripts/hello.py'],
      )