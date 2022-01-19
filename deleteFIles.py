#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 16:11:16 2022
@author: ashutoshverma

NOTE - remove .DS_Store file before executing this script on MAC
"""

import os

baseDirectory = "/Users/ashutoshverma/Docs/Rwth/Sem III/Optimization of Logistics Systems"
subDirectories = os.listdir(baseDirectory)

for item in subDirectories:
    subFolderPath = baseDirectory + "/" + item
    test = os.listdir(subFolderPath)
    for item in test:
        if item.endswith(".html"):
            os.remove(os.path.join(subFolderPath, item))