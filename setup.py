import setuptools

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setuptools.setup(
    name="PFX",
    version="1.0.1",
    author="Prashanth Umapathy",
    author_email="ujprashant@gmail.com",
    description="PFX or Python-Effects is a PyPI package for adding effects onto Image Processing",
    long_description= readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/prashanth-up/PFX",
    packages= ["pfx"],
    install_requires = ['pillow'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        "console_scripts":[
            "PFX=pfx.main:main",
        ]
    },
    python_requires='>=3.6',
)