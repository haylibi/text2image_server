from distutils.core import setup

setup(
    name='prompt_images',
    version='1.0',
    description='A python package which, when executed, deploys a server with a Plotly dashboard which allows to visualize images',
    author='Duarte Pinto',
    author_email='duarte.pinto7337@gmail.com',
    url='',
    python_requires='>=3.10, <4',
    packages=find_packages(include=['exampleproject', 'exampleproject.*']),
    install_requires=[
        'torch',
        'torchvision',
        'torchaudio',
        'diffusers',
        'pillow',
        'dash',
        'plotly',
        'gunicorn',
        'transformers'
    ],
    package_data={
        'sample': ['sample_data.csv'],
    },
    entry_points={
        'runners': [
            'sample=sample:main',
        ]
    }
)