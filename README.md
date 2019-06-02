## Chemical-Structurer
Desktop Application to display the bond-line structure of any chemical compound/molecule

# Objective
1.The main objective of the application is to ask for the data from PubChem through its Rest API.                                
2.This provides a good UI for the user to work with.       
3. Displays basic information about the given chemical compound or molecule

# Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install bs4
pip install pillow    #for PIL
```
# Visuals

![qrgenerator](https://user-images.githubusercontent.com/24393343/58764209-081ef500-8582-11e9-8e1c-a8993c9baa33.jpg)
 
# Run Locally
1. Method-1
* Clone the repo.
* Open the file and extract it.
* Edit the .py File in any editor and run it.

2. Method-2
* Go to this website : https://absanthosh01.wixsite.com/pythonist
* Download the application and run the portable .exe file!!
# Requirnments

```bash
import PIL 
import PIL.Image
import PIL.ImageTk
import base64
import os
import pyperclip
import qrcode
import tkinter

from PIL import Image
from resizeimage import resizeimage
from tkinter import *
from tkinter import PhotoImage 
from tkinter import filedialog
from tkinter import messagebox

```
    
