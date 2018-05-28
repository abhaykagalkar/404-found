# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 03:40:23 2018

@author: Abhay
"""

#Python3 MySQL Library
import pymysql.cursors 

def Connect():
    try:
        connect = pymysql.connect(host='127.0.0.1',
                                 user='ipcvg',
                                 password='ipcvg',                             
                                 db='ipcvg',
                                 charset='utf8mb4',
                                 autocommit=True, 
                                 cursorclass=pymysql.cursors.DictCursor)
        return (connect)
    except:
        return False    
            
