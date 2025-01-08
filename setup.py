from setuptools import setup, find_namespace_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="tasksu", 
    version="1.0.3",
    # packages=find_namespace_packages(),
    package_dir={ '' : 'tasksu' },
    author="Cory",
    author_email="tacocat8345@gmail.com",
    description="A Task Management CLI Application.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    url="https://github.com/zephyr834/tasksu",
    install_requires=required,
    entry_points={
        "console_scripts": [
            "tasksu=cli:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
)
