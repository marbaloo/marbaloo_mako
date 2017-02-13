from setuptools import setup

setup(name='marbaloo_mako',
      version='0.1',
      description='Mako template support for cherrypy.',
      author='meytighg',
      install_requires=[
          'cherrypy>=8.1.2',
          'mako>=1.0.4'
      ],
      )
