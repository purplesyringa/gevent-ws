from setuptools import find_packages, setup


setup(
    name="gevent-ws",
    version="2.0.8",
    description="Websocket server for gevent.pywsgi",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ivanq",
    python_requires=">=3",
    url="https://github.com/imachug/gevent-ws",
    packages=find_packages(),
    license="MIT"
)
