import setuptools
from dsfcli import __version__

setuptools.setup(
    name='dsf-cli',
    version=__version__,
    packages=setuptools.find_namespace_packages(),
    entry_points={
        "console_scripts": [
            "dsf=dsfcli.__main__:main"
        ]
    },
    install_requires=['urllib3'],
    python_requires='>=3.6',
    url='https://github.com/imperva/dsf-cli',
    license='Imperva-Community Developer License',
    author='Joe Moore',
    author_email='joe.moore@imperva.com',
    description="CLI for gateway, asset CRUD on DSF via API.",
    long_description='The package provides a simple to use CLI that reflects industry standards (such as the AWS cli), '
                     'and enables customers to manage DSF configurations and processes via the [DSF Open API]'
                     '(https://docs.imperva.com/bundle/v4.13-sonar-user-guide/page/84552.htm) easily integrating into '
                     'configurations management, orchestration or automation frameworks to support the DevOps model.',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
