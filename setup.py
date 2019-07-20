import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prettyjson",
    version="1.0.1",
    author="vimfun",
    author_email="vimfunny@gmail.com",
    description="Tool for printing pretty JSON (just for the missing options in `json.tool`)",

    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vimfunny/prettyjson",
    packages=setuptools.find_packages(),
    # packages=['example_pkg'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: MIT License',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',

        'Environment :: Console',

        "Operating System :: OS Independent",

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
