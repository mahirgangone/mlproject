from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    retquirements = []
    with open(file_path) as file_obj:
        retquirements = file_obj.readlines()
        retquirements = [req.replace('\n', '') for req in retquirements]

        if HYPHEN_E_DOT in retquirements:
            retquirements.remove(HYPHEN_E_DOT)
    return retquirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Mahir Gangone',
    author_email='mahirgangone@gmail.com',
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt') 
)