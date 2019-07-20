import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

version = __import__('prettyjson').__version__

setuptools.setup(
    name='prettyjson',
    version=version,
    author='vimfun',
    author_email='vimfunny@gmail.com',
    description='Command-line tool to validate and pretty-print JSON(just for the missing options in `json.tool`)',

    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/vimfunny/prettyjson',
    packages=setuptools.find_packages(),
    license='PSF license',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: MIT License',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',

        'Environment :: Console',

        'Operating System :: OS Independent',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',

        'Topic :: System :: Shells',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
    ],
)
