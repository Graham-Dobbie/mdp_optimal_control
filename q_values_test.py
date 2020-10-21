import numpy as np

pol_mat = np.array([[.5,.25,.25,0],[.25,.5,0,.25],[.25,0,.5,.25],[0,0,0,1]])
pol = np.array([pol_mat,pol_mat,pol_mat,pol_mat])

transmat = np.identity(4)
mat = np.array([transmat,transmat,transmat,transmat])

rewards = np.array([[[-1],[-1],[-1],[0]],[[-1],[-1],[0],[-1]],[[-1],[0],[-1],[-1]],[[0],[0],[0],[0]]])

q_val = np.zeros((4,4,1))


q_val = np.add(rewards,q_val)
print(q_val)
print()
print(pol_mat)
print()

q_val = np.matmul(pol_mat,q_val)
print(q_val)
print()