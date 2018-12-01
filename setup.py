from setuptools import setup

setup(
    name='ipysh',
    version='0.1.0',
    author='Vinnie Magro',
    author_email='v@vinn.ie',
    packages=['ipysh'],
    entry_points={
        'console_scripts': ['ipysh=ipysh.main:ipysh'],
    },
    license='LICENSE',
    description='IPython as system shell',
    long_description=open('README.md').read(),
    install_requires=[
        "IPython == 7.2.0",
    ],
    setup_requires=[
        "pex",
    ]
)
