try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension
try:
    from Cython.Distutils import build_ext
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

if USE_CYTHON:
    ext = '.pyx'
    cmdclass = {'build_ext': build_ext}
else:
    ext = '.c'
    cmdclass = {}

ext_modules = [Extension(
    'skin_classifier',
    sources=['skin_classifier' + ext]
)]

setup(name='mudepy',
      version='0.5.2',
      description="mudepy is maintained nudepy. Nudity detection with Python. Port of nude.js to Python",
      long_description_content_type='text/markdown',
      long_description=open('README.md').read(),
      author='Yaroslav Polyakov',
      author_email='yaroslaff@gmail.com',
      url='https://github.com/yaroslaff/mude.py',
      license='MIT',
      platforms='Linux',
      py_modules=['nude'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3'],
      keywords="nude",
      zip_safe=False,
      install_requires=['pillow'],
      entry_points={'console_scripts': ['nudepy = nude:main']},
      ext_modules=ext_modules,
      cmdclass=cmdclass,
      )
