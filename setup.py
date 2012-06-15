try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

install = []

try:
   import importlib
except ImportError:
   install.append("importlib")

setup(name='hello_python',
      version='1.0',
      license='BSD',
      description='Pipeline library',
      long_description='Pipeline library with steps: uppercase, date , duplicate'
      author='sharf',
      author_email='shak.ceg@gmail.com',
      url='http://github.com/sharf/hello_python',
      platforms = ['Any'],
      packages = ['pipes','pipes.lib','pipes.steps'],
      install_requires = install,
      tests_require = ['nose'],
      test_suite = 'nose.collector',
      classifiers = [ 'Development Status :: 1 - Beta',
                      'License :: OSI Approved :: BSD License',
                      'Operating System :: OS Independent',
                      'Programming Language :: Python']
)
