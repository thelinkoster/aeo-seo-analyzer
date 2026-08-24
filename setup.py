from setuptools import setup, find_packages

setup(
    name="aeo_analyzer",
    version="1.0.0",
    author="Rajesh Nitharwal",
    author_email="contact@linkoster.com",
    description="A Python tool for Technical SEO audits and AEO readiness verification.",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "lxml>=5.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
