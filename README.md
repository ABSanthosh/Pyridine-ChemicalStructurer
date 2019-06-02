## Chemical-Structurer
Desktop Application to display the bond-line structure of any chemical compound/molecule

# Objective
1.The main objective of the application is to ask for the data from PubChem through its Rest API.                                
2.This provides a good UI for the user to work with.       
3. Displays basic information about the given chemical compound or molecule                                                             
4. Saves the image of the structure to the local machine

# Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

```bash
pip install bs4
pip install pillow    #for PIL
```
# Visuals

![pyridine](https://user-images.githubusercontent.com/24393343/58765331-b2e9e000-858f-11e9-90b0-51eb00ec1444.jpg)
 
# Run Locally
1. Method-1
* Clone the repo.
* Open the file and extract it.
* Edit the .py File in any editor and run it.


# Requirnments

```bashimport base64
import os
import socket
import threading
import tkinter
import requests
import urllib.request

from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
from PIL import Image, ImageTk

```
    
