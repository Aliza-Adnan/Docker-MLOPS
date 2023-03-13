# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:52:52 2023

@author: aliza
"""

import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'exp':1.8,})
print(r.json())