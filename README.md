# Udacity_Machine_Learning_Capstone
Github repo containing all the documentation and code required for the Udacity Machine Learning Capstone Project

**README file**

**Introduction:**

This file details the documentation required to reproduce the work done for the Udacity Machine Learning Engineer Capstone Project. This project was concerned with creating
a machine learning model to predict the number if yards to be gained/lost on given rushing plays using NFL data provided by Kaggle. The models contained in the accompanying documents were built and tested in Amazon Sagemaker using their built-in algorithms.

**What's included in this folder?**

 - Capstone Proposal V2 PDF document: This document details the proposal written before commencing with the final project
 - Capstone Report PDF document: This is the final PDF report that will take the reader through the whole process, from start to finish
 - Capstone Project Notebook: This is the Jupyter Notebook where the code is located. It contains all the steps, from importing the data to creating, fitting and evaluating the models
 - helpers.py: This Python script contains additional helper functions that are called from the above Jupyter Notebook
 - main.csv: This file is too large to host on Github, but can be found on the Kaggle competition's website at https://www.kaggle.com/c/nfl-big-data-bowl-2020/data

**Dependencies:**

The Jupyter Notebook makes use of the below libraries. The can be imported by running the code set out below:
`import io
import os
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import seaborn as sns
# Importing the helper file in which helper functions are defined
import helpers
import boto3
import sagemaker
from sagemaker import get_execution_role
%matplotlib inline`

The helpers.py file makes use of the following libraries:
`import fuzzywuzzy
from fuzzywuzzy import process
import chardet
import numpy as np
import math`

**Installations:**

The following packages will need to be installed inside a terminal instance in the Amazon Sagemaker environment you are working in:
 - missingno
 - fuzzywuzzy
 - chardet

These packages are utilised by the helpers.py file. The command used to do so is:
conda install -n mxnet_p36 -c conda-forge "insert_package_name_here"

More details on this can be found here: https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-add-external.html
