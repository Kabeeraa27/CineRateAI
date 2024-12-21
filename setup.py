import setuptools

# Read the content of README.md to use it as long_description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Project version
__version__ = "0.0.0"

# Project details
REPO_NAME = "CineRateAI"
AUTHOR_USER_NAME = "Kabeeraa27"
SRC_REPO = "Predictor"
AUTHOR_EMAIL = "kabeeer27@gmail.com"

# Setup configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Movie Rating Prediction from Rotten Tomatoes Data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[  # Specify your dependencies here
        "flask",  # Example dependency, replace with actual ones
        "joblib",
        "scikit-learn",
        "pandas",
        "numpy",
    ],
    classifiers=[  # Add classifiers to categorize your project
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version requirement
)
