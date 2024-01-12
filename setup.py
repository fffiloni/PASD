from setuptools import setup, find_packages

setup(
    name='PASD',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add dependencies from the PASD repository requirements.txt file
        'diffusers==0.21.4',
        'accelerate',
        'transformers',
        'xformers',
        'basicsr',
        'ultralytics',
        'salesforce-lavis',
        'webdataset',
        # Add more dependencies as needed
    ],
)


