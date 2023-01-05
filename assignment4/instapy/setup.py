from distutils.core import setup
import setuptools
setup(
    name='instapy',
    version='1.0',
    author='Jouval',
    author_email='jmsomer@math.uio.no',
    packages=setuptools.find_packages(),
    scripts=['bin/instapy.py']
)