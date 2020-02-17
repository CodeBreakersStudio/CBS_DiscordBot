from setuptools import setup, find_namespace_packages

setup(
    name = "cbsDiscordBot",
    version = "0.0.1",
    description = "Bot for discord made by Code Breakers Studio",
    author= "Code Breakers Studio, Kacper Kotlewski",
    packages=find_namespace_packages(include=['cbs_db.*']),
)