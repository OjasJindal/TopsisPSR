from setuptools import setup, find_packages

setup(
    name="Topsis-Ojas-102317056",
    version="1.0.0",
    author="Ojas Jindal",
    author_email="ojindal_be23@thapar.edu",
    description="TOPSIS command line tool",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main",
        ],
    },
    python_requires=">=3.6",
)
