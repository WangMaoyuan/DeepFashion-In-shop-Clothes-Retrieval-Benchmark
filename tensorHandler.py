# import tensorflow as tf
import pandas as pd
import numpy as np
import random
import math
_DATA_DIR = "./tensorData.txt"
def genData():
    return [random.random() for i in range(23)]
def store(raw):
    b = np.loadtxt(_DATA_DIR).reshape(-1,23)
    print(b)
    a = np.array(raw, 'float')
    a = a[None,:]
    c = np.concatenate((b,a),axis=0)
    print("database:")
    print(c)
    np.savetxt(_DATA_DIR,c)
# def compare(a, b):
#     dot = 0.
#     len1 = 0.
#     len2 = 0.
#     for i in range(len(a)):
#         dot = dot + a[i]*b[i]
#         len1 = len1 + a[i] ** 2
#         len2 = len2 + b[i] ** 2
#     len1 = math.sqrt(len1)
#     len2 = math.sqrt(len2)
#     cos = dot/(len1 * len2)
#     return cos
def cos(vector1, vector2):
    cosV12 = np.dot(vector1,vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2))
    return cosV12

def swap(n, a, b):
    tmp = np.copy(n[a])
    n[a] = n[b]
    n[b] = tmp

# default length of database is greater than 5
def top5(raw):
    out = []
    n=np.loadtxt(_DATA_DIR)
    for i in range(len(n)-1):
        for j in range(len(n)-1):
                v1 = cos(raw, n[j])
                v2 = cos(raw, n[j+1])
                if (v1 > v2):
                    swap(n,j,j+1)
    for i in range(5):
        out.append(n[i])
    return np.array(out)
# print(top5(genData()))
