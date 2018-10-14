#!/usr/uday/anaconda/bin/python3

"""*********************************************
 Write a Class called KNN that implements the KNN Regression algorithm using 
 the Scipy KDTree. This class should be able to do the following given training
 and test data: 

 1) Calculate K-nearest neighbouts of given point
 2) Predict value using K-nearest points (taking average)




*********************************************"""

import pandas as pd 
import numpy as np 
from scipy.spatial import KDTree
import random 
import numpy.random as npr
from sklearn.preprocessing import StandardScaler 
import sys

sys.setrecursionlimit(1000)

class KNN_Regression:
    def __init__(self,data,target):
        self.tree=KDTree(data)
        self.target=target
        
    def calculate_KNeigbours(self,point,k):
        return self.tree.query(point,k=k)[1]
    
    def predict(self,point,k):
        return np.array([self.target[i] for i in self.calculate_KNeigbours(point,k)]).mean()