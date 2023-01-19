from setuptools import setup, find_packages
def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="launchscreen",
    version="1.0.5",
    description="Launch Screen for Tkinter",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/mahinbinhasan/launchscreen",
    author="Mahin Bin Hasan (mahinbinhasan)",
    author_email="<allmahin149@gmail.com>",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'launchscreen','tkstartingwindow','transparent window'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)