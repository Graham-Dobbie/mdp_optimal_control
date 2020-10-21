import numpy as np
from env import env

class agent:

    def __init__(self, env_trans_mat, actions, rewards, init_polocy = None, init_value_func = None):

        self.env_size = list(env_trans_mat.shape)
        self.action_size = len(actions)
        self.rewards = rewards
        self.actions = actions
        self.trans_mat = env_trans_mat

        if type(init_polocy) != type(np.array(1)):
            self.polocy = np.identity(env_trans_mat.shape[0])
        else:
            self.polocy = init_polocy
        
        if type(init_value_func) != type(np.array(1)):
            self.value_func = np.zeros( (self.env_size[0]))
        else:
            self.value_func = init_value_func
    

    def eval_value_func(self):

        gamma = .8
        ident_mat = np.identity(self.trans_mat.shape[0])


        trans_pol_mat = np.matmul(self.trans_mat, self.polocy)
        prod_mat = np.add(ident_mat, -gamma * trans_pol_mat)

        future_r = np.linalg.inv(prod_mat)

        self.value_func = np.matmul(future_r, rewards)

    def greedy(self):

        for i in range(len(self.actions)):
            prod = np.multiply(self.actions[i],self.value_func)
            
            where = np.nanargmax(prod)
            g_polocy = np.zeros((self.actions[i].shape))
            g_polocy[where] = 1
            self.polocy[i] = g_polocy
    
    def itterate_polocy(self, n = 10):

        for i in range(n):
            self.eval_value_func()
            self.greedy()


        



    
e = env()
actions = e.actions
trans_mat = e.env_mdc_trans_mat
rewards = e.rewards


a = agent(trans_mat,actions,rewards)



def view_polocy(polocy):
    moves = []
    for i in range(len(polocy)):
        row = polocy[i]
        move = np.argmax(row)
        diff = move - i
        if diff == -8:
            moves.append('U')
        elif diff == -1:
            moves.append('L')
        elif diff == 1:
            moves.append('R')
        elif diff == 8:
            moves.append('D')
        else:
            moves.append('N')
    moves = np.array(moves).reshape((8,8))
    print(moves)


a.itterate_polocy(5)
view_polocy(a.polocy)
print()
a.itterate_polocy(5)
view_polocy(a.polocy)
print()
a.itterate_polocy(5)
view_polocy(a.polocy)
print()
a.itterate_polocy(5)
view_polocy(a.polocy)
print()
a.itterate_polocy(5)
view_polocy(a.polocy)
print()
a.itterate_polocy(5)
view_polocy(a.polocy)
print()
# v = np.reshape(a.value_func, (8,8)).round(3)
# print(v)
# print()




# polocy = stuff

# value_func = np.zeros(rewards.shape)
# print(rewards)
# print(trans_mat)
# print(polocy)
# print(value_func)

# 

# 

# 

# 


# 


# .round(3)
# v = v.reshape((8,8))
# print(v)
# print()








        
        

