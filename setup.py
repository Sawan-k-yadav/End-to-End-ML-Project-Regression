# If I want to make the project to package then this file is needed

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()   # reading all the library of requiremensts file
        requirements=[req.replace("\n","") for req in requirements] # Replacing all the \n or line change character with blank
    
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



setup(
    name='RegressorProject',
    version='0.0.1',
    author='Sawan',
    author_email='sawan.gomia@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)