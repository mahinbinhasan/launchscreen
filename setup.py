from setuptools import setup, find_packages
import codecs

VERSION = '1.0'
DESCRIPTION = 'Launch Screen for Tkinter'
setup(
    name="mahinlaunchscreen",
    version=VERSION,
    author="Mahin Bin Hasan (mahinbinhasan)",
    author_email="<allmahin149@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'launchscreen','tkstartingwindow','transparent window'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)