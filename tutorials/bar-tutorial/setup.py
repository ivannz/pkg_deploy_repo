from distutils.core import setup


setup(
    name="bar",
    version="0.1",
    packages=[
        "bar",
        "bar.sub",
    ],
    install_requires=[
        "numpy",
        "tqdm",
        "matplotlib",
        "torch",
        "torchvision",
    ],
    package_data={
        "bar": [
            "data/dataset.txt",
        ],
        "bar.sub": [
            "data/data.zip",
        ]
    }
)
