''' Pandas is an open-source, BSD-licensed Python library providing high-performance, easy-
to-use data structures and data analysis tools for the Python programming language. This
Pandas tutorial has been prepared for those who want to learn about the foundations and
advanced features of the Pandas Python package. Python with Pandas is used in a wide
range of fields including academic and commercial domains including finance, economics,
Statistics, analytics, etc. In this tutorial, we will learn the various features of Python Pandas
and how to use them in practice'''

''' What is Pandas?
Pandas is a powerful Python library that is specifically designed to work on data frames
that have "relational" or "labeled" data. Its aim aligns with doing real-world data analysis
using Python. Its flexibility and functionality make it indispensable for various data-related
tasks. Hence, this Python package works well for data manipulation, operating a dataset,
exploring a data frame, data analysis, and machine learning-related tasks. To work on it
we should first install it using a pip command like "pip install pandas" and then import it
like "import pandas as pd". After successfully installing and importing, we can enjoy the
innovative functions of pandas to work on datasets or data frames. Pandas versatility and
ease of use make it a go-to tool for working with structured data in Python.

Generally, Pandas operates a data frame using Series and DataFrame; where Series works
on a one-dimensional labeled array holding data of any type like integers, strings, and
objects, while a DataFrame is a two-dimensional data structure that manages and operates
data in tabular form (using rows and columns).'''

''' Why Pandas?
The beauty of Pandas is that it simplifies the task related to data frames and makes it
simple to do many of the time-consuming, repetitive tasks involved in working with data
frames, such as:
     Import datasets - available in the form of spreadsheets, comma-separated values
        (CSV) files, and more.
     Data cleansing - dealing with missing values and representing them as NaN, NA,
        or NaT.
     Size mutability - columns can be added and removed from DataFrame and higher-
        dimensional objects.
     Data normalization – normalize the data into a suitable format for analysis.
     Data alignment - objects can be explicitly aligned to a set of labels.
     Intuitive merging and joining data sets – we can merge and join datasets.
     Reshaping and pivoting of datasets – datasets can be reshaped and pivoted as
        per the need.
     Efficient manipulation and extraction - manipulation and extraction of specific
        parts of extensive datasets using intelligent label-based slicing, indexing, and
        subsetting techniques.
     Statistical analysis - to perform statistical operations on datasets.
     Data visualization - Visualize datasets and uncover insights.'''

'''Applications of Pandas
The most common applications of Pandas are as follows:
     Data Cleaning: Pandas provides functionalities to clean messy data, deal with
        incomplete or inconsistent data, handle missing values, remove duplicates, and
        standardize formats to do effective data analysis.
     Data Exploration: Pandas easily summarize statistics, find trends, and visualize
        data using built-in plotting functions, Matplotlib, or Seaborn integration.
     Data Preparation: Pandas may pivot, melt, convert variables, and merge datasets
        based on common columns to prepare data for analysis.
     Data Analysis: Pandas supports descriptive statistics, time series analysis, group-
        by operations, and custom functions.
     Data Visualization: Pandas itself has basic plotting capabilities; it integrates and
        supports data visualization libraries like Matplotlib, Seaborn, and Plotly to create
        innovative visualizations.
     Time Series Analysis: Pandas supports date/time indexing, resampling,
        frequency conversion, and rolling statistics for time series data.
     Data Aggregation and Grouping: Pandas groupby() function lets you aggregate
        data and compute group-wise summary statistics or apply functions to groups.
     Data Input/Output: Pandas makes data input and export easy by reading and
        writing CSV, Excel, JSON, SQL databases, and more.
     Machine Learning: Pandas works well with Scikit-learn for data preparation,
        feature engineering, and model input data.
     Web Scraping: Pandas may be used with BeautifulSoup or Scrapy to parse and
        analyze structured web data for web scraping and data extraction.
     Financial Analysis: Pandas is commonly used in finance for stock market data
        analysis, financial indicator calculation, and portfolio optimization.
     Text Data Analysis: Pandas' string manipulation, regular expressions, and text
        mining functions help analyze textual data.
     Experimental Data Analysis: Pandas makes manipulating and analyzing large
        datasets, performing statistical tests, and visualizing results easy.'''

''' Audience: Who Should Learn Pandas
This Pandas tutorial has been prepared for those who want to learn about the foundations
and advanced features of the Pandas Python package. It is most widely used in the domain
of data science, engineering, research, agriculture science, management, statistics, and
other related fields where computation on a data set requires or explores the data frames
to find out the data insights that are required to make fruitful decisions.

After completing this tutorial, you will find yourself skilled in pandas Python package from
where you can take yourself to the next levels of expertise on other Python packages like
Matplotlib, SciPy, scikit-learn, scikit-image, and many more to keep mastering Python
language.

Pandas library uses most of the functionalities of NumPy. It is suggested to you to go
through our tutorial on NumPy.'''


''' Prerequisites to Learn Pandas
You should have a basic understanding of computer programming. A basic understanding
of Python and any of the programming languages is a plus. Basic knowledge of statistics
and mathematics is helpful for data analysis and interpretation. Pandas provide functions
for descriptive statistics, aggregation, and computation of summary metrics. By having a
strong foundation of above mentioned, you'll be well-equipped to leverage the power of
Pandas for data manipulation and analysis tasks.'''


''' Pandas Codebase
You can find the source for the Pandas at https://github.com/jvns/pandas-cookbook'''


''' List Key Features of Pandas.
The key features of Pandas as follows −
     Fast and Efficient DataFrame Object.
     Pandas supports various data loading tools for in-memory data objects.
     Data alignment and handling of missing data.
     Pandas allows you to reshaping and pivoting of datasets.
     Label-based slicing, indexing and subsetting of large data sets.
     Insert or delete columns from a data structure.
     Group by data for aggregation and transformations.
     High performance merging and joining.
     Time Series functionality.'''

''' Define Series in Pandas.
A Series in Pandas is a one-dimensional labeled array capable of holding data of any type
(integer, string, float, Python objects, etc.).'''


'''What are the two main data types in pandas?
The two primary data structures of pandas are −
     Series (1-dimensional)
     DataFrame (2-dimensional)'''