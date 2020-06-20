import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = ["feedparser"]

setuptools.setup(
     name='histoday',  
     version='0.1.3',
     scripts=['histoday'] ,
     author="Mert Acikportali",
     author_email="mertacikportali@gmail.com",
     description="A Python curses library based utility to read today in history",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/hmerac/histoday",
     packages=setuptools.find_packages(),
     classifiers=[
         # How mature is this project? Common values are
         #   3 - Alpha
         #   4 - Beta
         #   5 - Production/Stable
         "Development Status :: 4 - Beta",
         "Environment :: Console :: Curses",
         "Intended Audience :: End Users/Desktop",
         "Intended Audience :: Other Audience",
         "Programming Language :: Python",
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3 :: Only",
         "License :: OSI Approved :: MIT License",
     ],
     python_requires='>=3.6',
     platforms=["Any"],
     keywords="curses history interactive",
     install_requires=install_requires,
 )

