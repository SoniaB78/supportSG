#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      Administrateur
#
# Created:     06/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib.request
import pandas as pd
from random import *
import numpy as np
data=pd.read_csv("fruit.txt",sep=",",header=None)
from PIL import Image
import os
for i in range(data.shape[0]):
    a=data.iloc[i,0]
    urllib.request.urlretrieve(data.iloc[i,1], "{}.jpg".format(a))


    im = Image.open("{}.jpg".format(a))
    im.save("{}.png".format(a))



