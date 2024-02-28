config_requires = []
dev_requires = []
install_requires = [
    "scikit-learn",
    # "sklearn",
    "pandas",
    "numpy",
    "matplotlib",
]
build_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires = []
requires = config_requires + install_requires + build_requires + test_requires
