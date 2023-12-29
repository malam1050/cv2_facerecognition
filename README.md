# cv2

https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-windows/?ref=lbp

How to Install OpenCV for Python on Windows?

Prerequisite: Python Language Introduction   OpenCV is the huge open-source library for computer vision, machine learning, and image processing and now it plays a major role in real-time operation which is very important in today’s systems. By using it, one can process images and videos to identify objects, faces, or even the handwriting of a human. When it integrated with various libraries, such as Numpy, python is capable of processing the OpenCV array structure for analysis. To Identify image patterns and its various features we use vector space and perform mathematical operations on these features. To install OpenCV, one must have Python and PIP, preinstalled on their system. To check if your system already contains Python, go through the following instructions: Open the Command line(search for cmd in the Run dialog( + R). Now run the following command:

python --version
If Python is already installed, it will generate a message with the Python version available.

If Python is not present, go through How to install Python on Windows? and follow the instructions provided.   PIP is a package management system used to install and manage software packages/libraries written in Python. These files are stored in a large “on-line repository” termed as Python Package Index (PyPI). To check if PIP is already installed on your system, just go to the command line and execute the following command:

pip -V

If PIP is not present, go through How to install PIP on Windows? and follow the instructions provided.

Downloading and Installing OpenCV:
OpenCV can be directly downloaded and installed with the use of pip (package manager). To install OpenCV, just go to the command-line and type the following command:

pip install opencv-python

To check if OpenCV is correctly installed, just run the following commands to perform a version check:

python
>>>import cv2
>>>print(cv2.__version__)




