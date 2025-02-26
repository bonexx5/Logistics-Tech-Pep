from setuptools import setup, find_packages

setup(
    name='pepsa_logistics_optimization',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.21.0',
        'pandas==1.3.0',
        'scikit-learn==0.24.2',
        'matplotlib==3.4.2',
        'geopy==2.2.0',
        'python-dotenv==0.19.0',
    ],
    entry_points={
        'console_scripts': [
            'pepsa-optimize=src.main:main',
        ],
    },
)
