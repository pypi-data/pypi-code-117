import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="Kivy4",
    version="1.2.0",
    author="Eshqol Development",
    author_email="support@eshqol.com",
    packages=["kivy4"],
    description="This package allows you to create Kivy projects faster with a pre-made kivy template.",
    long_description=description,
    long_description_content_type="text/markdown",
    license='MIT',
    python_requires='>=3.7',
    install_requires=['kivy', 'kivymd', 'darkdetect', 'screeninfo']
)

#Eshqol_Development