from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='EIO-CMS',
      version=version,
      description="Contest Management System (CMS) adaptations for use in Estonian Informatics Olympiad (EIO)",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='cms olympiad ioi estonia',
      author='Konstantin Tretyakov',
      author_email='kt@ut.ee',
      url='http://eio.ut.ee/',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
