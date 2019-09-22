from setuptools import setup, find_packages

setup(
    name='s_click',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    # please note the entry_points
    # The magic is in the entry_points parameter. Below console_scripts, each line identifies one console script.
    # The first part before the equals sign (=) is the name of the script that should be generated,
    # the second part is the import path followed by a colon (:) with the Click command.
    entry_points={
        "console_scripts": [
            'sclick=s_click.main:run',
        ],
    },

)