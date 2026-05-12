from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT = '-e .'
def get_requirements(requirements_path) ->List[str]:
    """
    This function reads the requirements.txt file and returns a list of requirements.
    Args:
        requirements_path: The path to the requirements.txt file.
    Returns:
        A list of requirements.
    """
    requirements = []
    with open(requirements_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '').strip()
                        for req in requirements 
                        if req.strip() and not req.startswith('#')]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

setup(
    name='student_exam_score_prediction',
    version='0.1',
    author='John Luc',
    author_email='john.luc@mail.utoronto.ca',
    packages=find_packages(),
    install_requires=get_requirements(requirements_path='requirements.txt')
)