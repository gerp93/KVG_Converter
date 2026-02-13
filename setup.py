"""
Setup script for creating Windows executable using PyInstaller
"""

from setuptools import setup

APP_NAME = 'RTF_to_PDF_Converter'
VERSION = '1.0.0'

setup(
    name=APP_NAME,
    version=VERSION,
    description='RTF to PDF Converter - Windows Desktop Application',
    author='KVG Converter',
    py_modules=['rtf_to_pdf_converter'],
    install_requires=[
        'reportlab==4.1.0',
        'striprtf==0.0.26',
        'Pillow==10.3.0',
    ],
    entry_points={
        'console_scripts': [
            'rtf-to-pdf=rtf_to_pdf_converter:main',
        ],
    },
)
