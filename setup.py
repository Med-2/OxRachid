from setuptools import find_packages, setup

setup(
    name="darkdown",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "yt-dlp>=2024.10.7",
        "requests>=2.32.3",
    ],
    entry_points={
        "console_scripts": [
            "darkdown=src.main:main",
        ],
    },
    author="0xRach",
    author_email="0xxrach@gmail.com",
    description="A powerful YouTube video and playlist and audio downloader using yt-dlp",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="git@github.com:OxRachid/darkdown.git",
    python_requires=">=3.6",
    # Make sure your package is easily installable
    zip_safe=False,
    # Add classifiers for better visibility
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Video",
        "Environment :: Console",
    ],
)
