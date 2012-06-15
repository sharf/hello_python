try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(name='pipeline',
      version='1.0',
      license='BSD',
      description='Pipeline library',
      author='sharf',
      author_email='shak.ceg@gmail.com',
      url='http://github.com/sharf/hello_python',
      platforms = ['Any'],
      packages = ['pipes','pipes.lib','pipes.steps'],
      classifiers = [ 'Development Status :: 1 - Beta',
                      'License :: OSI Approved :: BSD License',
                      'Operating System :: OS Independent',
                      'Programming Language :: Python']
)
