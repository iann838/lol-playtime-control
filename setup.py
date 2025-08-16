from setuptools import setup

setup(
    name="lol_playtime_control",
    version="0.1.0",
    py_modules=["main"],
    data_files=[("", ["icon.webp"])],
    include_package_data=True,
    install_requires=["psutil", "pystray", "pillow"],
    entry_points={
        "gui_scripts": [
            "lol-playtime-control = main:main",
        ]
    },
)