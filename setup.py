from setuptools import setup, find_packages
from shutil import copytree
import os


# Install dependencies
setup(
    name='autoXRD',
    version='0.0.1',
    description='A package designed to automate the process of phase identification from XRD spectra using a probabilistic deep learning trained with physics-informed data augmentation.',
    author='Nathan J. Szymanski',
    author_email='nathan_szymanski@berkeley.edu',
    python_requires='>=3.6.0',
    url='https://github.com/njszym/XRD-AutoAnalyzer',
    license='MIT',
    packages=find_packages(),
    install_requires=['numpy', 'pymatgen', 'dtw-python', 'scipy', 'opencv-python', 'opencv-rolling-ball', 'keras', 'tensorflow']
)

# Copy autoXRD to python path
pythonpath = os.__file__.split('/')[:-1]
pythonpath = '/'.join(pythonpath)
copytree('autoXRD', '%s/autoXRD' % pythonpath)
