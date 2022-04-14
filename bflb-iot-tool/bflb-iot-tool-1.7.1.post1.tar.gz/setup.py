#!/usr/bin/env python

from setuptools import setup, find_packages

packages = [
    'bflb_iot_tool',
    'bflb_iot_tool.core',
    'bflb_iot_tool.libs',
    'bflb_iot_tool.libs.bl60x',
    'bflb_iot_tool.libs.bl602',
    'bflb_iot_tool.libs.bl702',
    'bflb_iot_tool.libs.bl808',
]

entry_points = {'console_scripts': ['bflb-iot-tool = bflb_iot_tool.__main__:run_main']}

setup(
    name="bflb-iot-tool",
    version="1.7.1 post1",
    author="bouffalolab",
    author_email="jxtan@bouffalolab.com",
    description="Bouffalolab Iot Tool",
    license="MIT",
    url="https://pypi.org/project/bflb-iot-tool/",
    packages=packages,  # 包的代码主目录
    #package_data=package_data,
    include_package_data=True,
    entry_points=entry_points,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Unix',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'ecdsa>=0.15',
        'pycryptodome==3.9.8',
        'bflb-crypto-plus==1.0',
        'pycklink>=0.0.7',
        'pyserial==3.5',
        'pylink-square==0.5.0',
        'portalocker==2.0.0'
    ],
    python_requires='>3.0,<4.0',
    zip_safe=False,
)
