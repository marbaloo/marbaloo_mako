from setuptools import setup
readme = open('README.rst').read()

setup(name='marbaloo_mako',
      version='0.1.0',
      description='Mako template support for cherrypy.',
      long_description=readme,
      url='http://github.com/marbaloo/marbaloo_mako',
      author='Mahdi Ghane.g',
      license='MIT',
      keywords='mako cherrypy marbaloo marbaloo_mako',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Framework :: CherryPy',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Unix',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Software Development :: Libraries'
      ],
      install_requires=[
          'cherrypy>=8.1.2',
          'mako>=1.0.4'
      ],
      packages=['marbaloo_mako'],
      )
