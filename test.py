import numpy as np

transmat = [[.5,.25,.25,0],[.25,.5,0,.25],[.25,0,.5,.25],[0,0,0,1]]

mat = np.array(transmat)
pol = mat
rewards = [[-1],[-1],[-1],[0]]
rewards = np.array(rewards)
q_values = np.zeros((4,1))


# new_q_values = np.matmul(mat, q_values)
# print(new_q_values)
# print()

# new_q_values = np.add(new_q_values, rewards)
# print(new_q_values)
# print()

# new_q_values = np.matmul(mat, new_q_values)
# print(new_q_values)
# print()

# new_q_values = np.matmul(pol, new_q_values)
# print(new_q_values)
# print()

ident_mat = np.identity(4)

gamma = .8

prod_mat = np.add(ident_mat, -gamma * mat)
print(prod_mat)
print()

future_r = np.linalg.inv(prod_mat)
print(future_r)
print()

v = np.matmul(future_r, rewards)
print(v)
print()


