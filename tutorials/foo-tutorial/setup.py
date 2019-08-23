from distutils.core import setup


setup(
    name="foo",
    version="0.1",
    packages=[
        "foo",
    ],
    install_requires=[
        "numpy",
        "tqdm",
        "matplotlib",
        "torch",
        "torchvision",
    ]
)
