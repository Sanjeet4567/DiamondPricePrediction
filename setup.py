from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' #automatically executes setup.py if requirements.py is run

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[requirement.replace("\n","") for requirement in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='SanjeetRaj',
    author_email='sanjeetraj0440@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
