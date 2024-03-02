config_requires = []
dev_requires = []
install_requires = [
    "scikit-learn",
    "scikit-image",
    # "sklearn",
    "pandas",
    "numpy",
    "matplotlib",
    "pycmdtools",
    "pylint",
]
build_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires = []
requires = config_requires + install_requires + build_requires + test_requires
