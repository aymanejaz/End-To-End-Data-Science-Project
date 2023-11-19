from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this fun will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]
    
    return requirements


setup(
    name='End-To-End-Data-Science-Project',
    version='0.0.1',
    author='Ayman',
    author_email='aymanijaz8@gmail.com',
    description='This is a project to demonstrate the end to end data science process using Python and Machine Learning libraries like Scikit Learn, Tensor',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
        
),