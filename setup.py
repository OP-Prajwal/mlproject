from setuptools import setup, find_packages
from typing import List

HYPEN_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements
   




setup(
    name='mlproject',
    version='0.1',
    packages=find_packages(),
    author='prajwal',
    author_email="prajwalgaonkar24@gmail.com",
    description='A small example package',
    install_requires=get_requirements('requirements.txt')
)