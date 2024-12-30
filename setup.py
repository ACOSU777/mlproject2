from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) ->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
# ->List means return a list
# readlines function will create /n when the text in the file has multi-lines

setup(
    name='mlproject2',
    version='0.0.1',
    author='Arthur C.',
    author_email='blackparade0518@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)
# create get_requirements function