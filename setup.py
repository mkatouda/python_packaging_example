from setuptools import setup

setup(
    name="corona-propella", # Replace with your own username
    version="0.0.1",
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'corona=corona.corona:main',
        ],
    },
    author="Propella",
    author_email="propella@example.com",
    description="A covoid-19 tracker",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
