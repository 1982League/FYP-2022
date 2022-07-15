from setuptools import setup, find_packages

setup(
    name='FYP-2022',
    version='1.0.0',
    description='ACL Automation Tool',
    author='Siddharth Joshi',
    author_email='siddharth.joshi@mycit.ie',
    url='https://github.com/1982League/FYP-2022',
    packages=find_packages(exclude=('tests','testing*')),
    entry_points={
        'console_scripts':[
            'acl_tool-cli = acl_tool.main:main',
        ],
    },
)