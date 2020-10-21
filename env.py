import numpy as np

class env:

    def __init__(self):

        self.reward_loc = [7,7]
        self.blockers = [[1,4], [2,4], [3,4], [4,4], [5,4], [6,4], [7,4]]

        self.state_e = []

        self.board_size = [8,8]

        for i in range(self.board_size[0]):
            row = []
            for j in range(self.board_size[1]):
                if [j,i] in self.blockers:
                    row.append(-1)
                elif [j,i] == self.reward_loc:
                    row.append(1)
                else:
                   row.append(0) 
            self.state_e.append(row)
        
    
    def start(self, agent_loc = [0,0]):
        self.agent_loc = agent_loc
    
    
    def move(self,move):
        y = self.agent_loc[0] + move[0]
        x = self.agent_loc[1] + move[1]

        if x >7 or x<0 or y>7 or y<0:
            self.agent_loc = [0,0]
            return -1
        elif [x,y] in self.blockers:
            self.agent_loc = [0,0]
            return -1
        elif [x,y] == self.reward_loc:
            self.agent_loc = [0,0]
            return 1
        else:
            self.agent_loc[0] += move[0]
            self.agent_loc[1] += move[1]
            return 0
    
    @property
    def actions(self):
        trans_mat = self.trans_matd
        actions = trans_mat/trans_mat
        return actions

    @property
    def state_o(self):

        y = self.agent_loc[0]
        x = self.agent_loc[1]
        board = np.copy(self.state_e)
        board[y][x] = 3
        return board


    @property
    def env_mdc_trans_mat(self):
        return np.identity(self.board_size[1]**2)


    @property
    def trans_mat(self):
        
        def nieghbor(src_pos,dst_pos):
            y_dif = dst_pos[0] - src_pos[0]
            x_dif = dst_pos[1] - src_pos[1]
            s = abs(y_dif)+abs(x_dif)

            if s== 1:
                return True
            else:
                return False
        
        def side(dst_pos):
            y = dst_pos[0]
            x = dst_pos[1]
            if x >7 or x<0 or y>7 or y<0:
                return True
            else:
                return False
        
        def block(dst_pos):
            if dst_pos in self.blockers:
                return True
            else:
                return False
             

        all_pos = []
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                all_pos.append([i,j])

        trans_mat = []
        reward_mat = []
        for src_pos in all_pos:
            posible_pos = np.array([])
            reward_pos = np.array([])
            moves = 0.0
            for dst_pos in all_pos:
                if block(dst_pos):
                    pp = 0.0
                    r = -5
                    
                if dst_pos == self.reward_loc and nieghbor(src_pos,dst_pos):
                    pp = 1.0
                    moves +=1.0
                    r = 1        
                
                if src_pos == self.reward_loc:
                    if  dst_pos ==  src_pos:
                        pp= 1.0
                        r = 1  
                        moves += 1.0
                    else:
                        pp = 0.0
                        r = 0 

                elif nieghbor(src_pos,dst_pos) and not side(dst_pos):
                    pp = 1.0
                    moves +=1.0
                    r = 1

                else:
                    pp = 0.0
                    r = 0
                
                reward_pos = np.append(reward_pos,r)
                posible_pos = np.append(posible_pos,pp)

            
            move_probs = posible_pos/np.sum(posible_pos)
            
            trans_mat.append(move_probs)
            
        
            reward_mat.append(reward_pos)
        
        
        return np.array(trans_mat)

        # return np.identity(self.board_size[1]**2)

    @property
    def rewards(self):
        
        
        all_pos = []
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                all_pos.append([i,j])
        
        
        reward = []
        
        for pos in all_pos:
            y = pos[0]
            x = pos[1]

            if x >7 or x<0 or y>7 or y<0:
                r = -5
            elif [x,y] in self.blockers:
                r = -5
            elif [x,y] == self.reward_loc:
                r = 1
            else:
                r = -1
            reward.append(r)
                # if r == 1:
                #     print(pos,action, r)

            
            
            

        
        return np.array(reward)



# env  = env()
# # actions = env.actions
# # trans_mat,rewards = env.env_mdc_trans_mat
# # print(trans_mat)
# print(env.rewards)

