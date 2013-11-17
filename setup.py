from setuptools import setup, find_packages

version = '0.0'

setup(
    name='tank',
    version=0.1,
    description="battlefield where Tanks can fight.",
    long_description="""This module generates a battlefield where Players
can fight between each other with Tanks or others stuff...
""",
    classifiers=[],
    keywords='Tank',
    author='Alexandre Brun',
    author_email='alexandre.brun@xcg-consulting.fr',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    entry_points=dict(
        console_scripts=[
          'tanks = tank.main:main',
        ],
    ),
    # to run the tests just run the command like this:
    # nosetests -v --with-coverage --cover-html --cover-package=pki
    # after installing nose and coverage
    tests_require = ['nose', 'coverage'],
)
