#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 09:43:28 2022

@author: praveenys
"""

echo "streamlit_heroku" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/yspraveen87/streamlit_heroku.git
git push -u origin master

print("HELLO STREAMLIT AND HEROKU")