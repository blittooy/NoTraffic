from setuptools import setup, find_packages
import versioneer


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(name="NoTraffic",
      version="0.0.0",
      description="Traffic Analytics",
      author="Bradford Littooy",
      author_email="bradlittooy@gmail.com",
      url="https://github.com/blittooy/NoTraffic",
      license="MIT",
      packages=find_packages(),
      classifiers=[
          "Development Status :: 0 - Beta",
          "Programming Language :: Python :: 3 :: Only"
          "Programming Language :: Python :: 3.6",
          "License :: MIT",
          "Natural Language :: English",
          "Topic :: Software Development",
          "Topic :: Scientific/Engineering :: Visualization",
      ],
      install_requires=get_requirements(),
      zip_safe=False
      )
