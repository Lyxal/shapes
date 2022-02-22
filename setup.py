from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='shaapes',
    version='0.0.0.dev0',
    description='A graphical shape based esolang',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/photon-niko/shapes',
    author='Calico Niko',
    license='GPL-3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Interpreters',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='shapes graphical esoteric esolang programming language graph image',
    packages=find_packages(),
    python_requires='>=3.6, <4',
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/photon-niko/shapes/issues',
        'Source': 'https://github.com/photon-niko/shapes',
    },
)