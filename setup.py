from setuptools import setup, find_namespace_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="tasksu", 
    version="1.0.3",
    packages=find_namespace_packages(),
    author="Cory",
    author_email="tacocat8345@gmail.com",
    description="A Task Management CLI Application.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    url="https://github.com/zephyr834/tasksu",
    py_modules=[
        "app",
        "test"
    ],
    install_requires=required,
    tests_require=[
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "tasksu=app:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
)
