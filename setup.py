from setuptools import setup

__VERSION__ = '0.0.1'

setup(
    name='othello-runner',
    version=__VERSION__,
    author='yassu',
    author_email='mathyassu@gmail.com',
    description='othello program including GUI',
    entry_points="""
    [console_scripts]
    othello = othello.main:main
    """
)
