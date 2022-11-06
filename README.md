# img_processing
A repository for converting and processing the images via Python
You can download the code here and run it by following the instructions below

## Introduction
This document is illustring how we can browse for an image, convert it to <b>B&w</b> or <b>Grayscale</b>
First we need to learn about the important img processing modules including:
  <ul>
    <li>OpenCV</li>
    <li>Scikit-Image.</li>
    <li>Mahotas</li>
    <li>SciPy</li>
    <li>Pillow/PIL</li>
    <li>Matplotlib</li>
    <li>Numpy</li>
    <li>Tkinter</li>
  </ul>  
In this document we use <b>Tkinter</b>, <b>Numpy</b>, <b>PIL</b>. Therefore, by importing these modules such the ones below, we can use the main points of these libraries.
However we need to install them first:

```
pip install numpy
pip install tk
pip install pillow
```

By installing the libraries we can import them in our file:
```python
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np

```
We have declared a function and linked it to a Button in order to browse the most picture files including <b>Jpeg</b>,
<b>Jpg</b>, <b>Png</b>, <b>bmp</b>, <b>gif</b> to show the file and convert it to B&W and Grayscale. the <b>PIL</b> module helps us to convert them to the filters we want.

```python
img = Image.open(filename)

#to convert to grayscale filter we need set the ``convert()`` argument to L
grayscale = Image.open(filename)
grayscale = grayscale.convert("L")

#to convert to B&W filter we need set the ``convert()`` argument to 1
bw = Image.open(filename)
bw = bw.convert("1")
```



## Run 
```
python the_real.py
```
<img src="https://hounaar.com/github/img_processing/1.jpg">

Now by running the code, the windows will open


<img src="https://hounaar.com/github/img_processing/2.jpg">

You can see the full video here below

![](https://hounaar.com/github/img_processing/main.gif) 



I hope you have enjoyed reading this document

