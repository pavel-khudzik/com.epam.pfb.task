import setuptools

setuptools.setup(
    name='tagcounter',
    version = '1.0',
    author = 'Pavel Khudzik',
    author_email = 'pavel_khudzik@epam.com',
    description = 'Tag Counter app as a final task of course',
    packages=setuptools.find_packages(),
    package_data={'': ['*.yaml']},
    entry_points={'console_scripts': ['tagcounter = tagcounter:main']},
)
