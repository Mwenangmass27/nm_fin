#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 2019

@author: 11317832
"""

import numpy as np

def tridiag(a, b, c, M):
	# Initialise la matrice tridiagonale
	# mat[: ,0]=a surdiagonale , mat[: ,1]=b diagonale , mat[: ,2]=c sousdiagonale
	mat = np.zeros((M,3)) 
	mat[: ,0] = a
	mat[: ,1] = b 
	mat[:,2] = c
	# ligne 0, condition de Dirichlet 
	mat[0,2] = 0
	# ligne M-1, condition de Neumann 
	mat[M-1,0] = 0
	mat[M-1,1] = b+a
	return mat;

def mult(A,x): 
	M= len(x)
	vect = np.zeros(M) 
	vect[0]=x[0]*A[0,1]+x[1]*A[0 ,0] 
	for i in range(1,M-1):
		vect[i]=x[i]*A[i,1]+x[i-1]*A[i,2]+x[i+1]*A[i ,0] 
	vect[M-1]=x[M-1]*A[M-1,1]+x [M-2]*A[M-1 ,2]
	return vect	

def inverse(B,x):
	M= len(x)
	vect = np.zeros(M)
	B[0,0]=B[0,0]/B[0 ,1] 
	x[0]=x[0]/B[0 ,1]
	for i in range(1,M-1):
		temp=B[i,1] 
		B[i,2]*B[i-1,0] 
		B[i,0] =B[i,0]/temp
		x[i] = (x[i]-B[i,2]*x[i-1])/temp
		x[M-1] = (x[M-1]-B[M-1,2]*x[M-2])/(B[M-1,1]-B[M-1,2]*B[M-2,0]) 
		vect[M-1] = x[M-1]
	for i in range(M-2, -1, -1):
		vect[i] = x[i]-B[i,0]*vect[i+1] 
	return vect