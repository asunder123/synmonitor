import setuptools
with open("README.md", "r") as fh:

        long_description = fh.read()


setuptools.setup(

            name="asunder",
            author="anand",
            author_email="anandsunder@capgemini.com",
            description="<Template Setup.py package>",
            long_description="",
            long_description_content_type="text/markdown",
            url="https://github.com/asunder123/synmonitor",
            packages=setuptools.find_packages(),
            classifiers=[

                         "Programming Language :: Python :: 3",

                                 "License :: OSI Approved :: MIT License",

                                         "Operating System :: OS Independent",

                                             ],
           python_requires='>=3.6',

           )
