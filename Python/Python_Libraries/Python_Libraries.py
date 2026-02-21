'''------------------------- NumPy Tutorial -----------------------
NumPy, which stands for Numerical Python, is an open-source Python library consisting
of multidimensional and single-dimensional array elements. It's a standard that computes
numerical data in Python. NumPy is most widely used in almost every domain where
numerical computation is required, like science and engineering; hence, the NumPy API
functionalities are highly utilized in data science and scientific Python packages, including
Pandas, SciPy, Matplotlib, scikit-learn, scikit-image, and many more.

This NumPy tutorial explains the basics of NumPy, such as its architecture and
environment. It also discusses array functions, types of indexing, etc., and then extends
to learn Matplotlib, Pandas, SciPy, and other important Python libraries. All this is
explained with the help of examples for better understanding.'''

'''Why NumPy - Need of NumPy
NumPy is a fundamental package for numerical computation in Python. It provides
mathematical functions to compute data as well as functions to operate multi-dimensional
arrays and matrices efficiently. 
Here are some reasons why NumPy is essential:
     NumPy includes a wide range of mathematical functions for basic arithmetic, linear
        algebra, Fourier analysis, and more.
     NumPy performs numerical operations on large datasets efficiently.
     NumPy supports multi-dimensional arrays, allowing for the representation of
        complex data structures such as images, sound waves, and tensors in machine
        learning models.
     It supports the writing of concise and readable code for complex mathematical
        computations.
     NumPy integrates with other libraries to do scientific computation; these are SciPy
        (for scientific computing), Pandas (for data manipulation and analysis), and scikit-
        learn (for machine learning).
     Many scientific and numerical computing libraries and tools are built on top of
        NumPy.
     Its widespread adoption and stability make it a standard choice for numerical
        computing tasks.
Overall, NumPy plays a crucial role in the Python ecosystem for scientific computing, data
analysis, machine learning, and more. Its efficient array operations and extensive
mathematical functions make it an indispensable tool for working with numerical data in
Python.'''


''' NumPy Applications - Uses of NumPy
The following are some common application areas where NumPy is extensively used:
     Data Analysis: NumPy offers rapid and effective array operations, rendering it
        well-suited for tasks like data cleansing, filtering, and transformation. It is
        predominantly used in the analysis and scientific handling of data, particularly when
        working with extensive, large datasets.
     Machine Learning and Artificial Intelligence: Different machine learning and
        deep learning frameworks in Python, such as TensorFlow, and PyTorch, rely on
        NumPy arrays for handling input data, model parameters, and outputs.
     Scientific Computing: NumPy is widely used in scientific computing applications
        such as physics, chemistry, biology, and astronomy for data manipulation,
        numerical simulations, and analysis. NumPy is often used in numerical simulations
        and computational modelling for solving differential equations, optimisation
        problems, and other mathematical problems.
     Array manipulation: NumPy provides an assortment of methods for manipulating
        arrays, such as resizing, slicing, indexing, stacking, splitting, and concatenating
        arrays. These techniques are essential for preparing and manipulating data in
        diverse scientific computing jobs.
     Finance and Economics: The NumPy API is also widely used in financial data
        analysis and economics to do portfolio optimization, risk analysis, time series
        analysis, and statistical modelling.
     Engineering and Robotics: NumPy is used in engineering disciplines such as
        mechanical, civil, and electrical engineering for tasks like finite element analysis,
        control system design, and robotics simulations.
     Image and Signal Processing: NumPy is extensively used in processing and
        analyzing images and signals.
     Data Visualization: NumPy doesn't provide data visualization but supports
        Matplotlib and Seaborn libraries to generate plots and visualizations from numerical
        data.
Overall, NumPy's versatility and efficiency make it an essential Python package across a
wide range of application areas in scientific computing, data analysis, and beyond.'''

''' NumPy Example
The following is an example of Python NumPy:'''
# Importing NumPy Array
import numpy as np
# Creating an array using np.array() method
arr = np.array([10, 20, 30, 40, 50])
# Printing
print(arr) # Prints [10 20 30 40 50]


'''NumPy Compiler
To practice the NumPy example, we provided an online compiler. Practice your NumPy
programs here:
"https://www.tutorialspoint.com/compilers/online-numpy-compiler.htm"'''

''' NumPy Codebase
NumPy's source code can be found at this github repository:
https://github.com/numpy/numpy'''