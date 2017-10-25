from distutils.core import setup, Extension

sfc_module = Extension('ExampleCLibrary', sources=['module.cpp'])

setup(
    name='ExampleCLibrary',
    version='1.0',
    description='Python Package with superfastcode C++ Extension',
    ext_modules=[sfc_module]
)
