# STARGAZING

## Overview

This tool allows you to get the number of stargazers of the following list of repos:

* freeCodeCamp/freeCodeCamp
* 996icu/996.ICU
* EbookFoundation/free-programming-books

The output of this program should be something like this:

    996icu/996.ICU: 261666
    EbookFoundation/free-programming-books: 230006
    freeCodeCamp/freeCodeCamp: 343651

## Building the Docker Image

Follow the steps below:

1. Use a command line to login to your Docker Hub account:
    
    ```docker login```

2. Go to de directory where the Dockerfile is and execute:

    ```docker build .```
  

## Run the Docker Image

To run the Docker Image execute:
    ```docker run```

## Run Unit tests

Follow the steps

1. Go to the mainSpec.py directory

2. Install python requirements (you need to have python 3 installed)
    
    ```python -m pip install -r requirements.txt```
    
3. Execute the following 
 
    ```pytest -q mainSpec.py```
    
    You should see an output similar to the following:
    
           1 passed in 0.11s
