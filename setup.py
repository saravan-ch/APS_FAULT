from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME = 'requirements.txt'
HYPEN_DOT_E = '-e .'
def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file_names:
        requirement_file_list = requirement_file_names.readlines()
    requirement_file_list = [requirement_name.replace('/n','') for requirement_name in requirement_file_list]

    if HYPEN_DOT_E == requirement_file_list:
        requirement_file_list.remove(HYPEN_DOT_E)
    return requirement_file_list


setup(
    name="sensor_fault_detection",
    version="0.0.2",
    author="Saravanan Chokkalingam",
    author_email="saravananc@systechusa.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)