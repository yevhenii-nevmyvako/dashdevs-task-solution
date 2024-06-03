import setuptools

with open('./requirements.txt') as requirements_file:
    install_requires = requirements_file.readlines()


scripts = ['./equilibrium_index_finder/scripts/find_equilibrium_index.py']


setuptools.setup(
    name='task-solution',
    version='0.1.0',
    python_requires='>=3.10',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points='''
    [console_scripts]
    find_index=equilibrium_index_finder.scripts.find_equilibrium_index:find_equilibrium_index_cli
    
    ''',
    scripts=scripts
)
