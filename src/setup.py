from setuptools import setup

setup(
    name="Bimeta",
    version="1.0",
    py_modules=['bimeta'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        bimeta=bimeta:cli
    ''',
)
