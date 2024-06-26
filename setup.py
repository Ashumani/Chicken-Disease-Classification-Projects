import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    log_descriptions = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification-Projects"
AUTHOR_USER_NAME = "Manish"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "manishkirnapure9@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for cnn app",
    long_description=log_descriptions,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)