from setuptools import setup, find_packages

setup_args = dict(
    name='pyflix',
    version='1.0.2',
    description='Netflix SDK',
    license='MIT',
    install_requires=[
        'PyJWT',
        'requests'
        'bcrypt; python_version == "4.0.1"',
    ],
    author='John Doe',
    author_email='example@example.com'
)


if __name__ == '__main__':
    setup(**setup_args)
