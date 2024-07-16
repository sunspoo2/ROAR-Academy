import numpy as np
v = np.array([2., 2., 4.])
e0=[1,0,0]
e1=[0,1,0]
e2=[0,0,1]
projection_e0 = np.dot(v, e0)
projection_e1 = np.dot(v, e1)
projection_e2 = np.dot(v, e2)
print (f'projection of v on e0: {projection_e0}')
print (f'projection of v on e1: {projection_e1}')
print (f'projection of v on e2: {projection_e2}')