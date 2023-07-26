from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.01',
      description='Clean Folder',
      author='Roman Kuspys',
      author_email='r@gmail.com',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder=clean_folder.main:start']}
)