from random import randint, choice

def find_all_index_max(l):
    m = max(l)
    ret = []
    for i in range(len(l)):
        if l[i] == m:
            ret.append(i)
    return ret

def random_from_distrib(l):
    total_sum = sum(l)
    current_sum = 0
    aleat = randint(0, total_sum-1)
    for i in range(len(l)):
        current_sum += l[i]
        if aleat < current_sum:
            return i
    raise ValueError("Shouldn't happen")

class Decision_Tree():
    """0 -> player have lost, 1 -> player have won, r,p,c -> 0,1,2"""
    
    
    def __init__(self, depth, full = True):
        if depth == 0:
            self.sons = []
        elif full:
            self.sons = [Decison_Tree(depth, False) for i in range(0,1)]
        else:
            self.sons = [Decison_Tree(depth-1, True) for i in range(0,2)]
        self.leaf = [0,0,0]
    
    
    def add(self, previous_moves, played):
        if self.sons != []:
            self.sons[previous_moves[-1][1]].leaf[played] += 1
            self.sons[previous_moves[-1][1]].sons[previous_moves[-1][0]].add(previous_moves[:-1], played)
        self.leaf[played] += 1
    
    
    def find_next(self, previous_moves):
        if self.leaf == [0,0,0]:
            return randint(0,2) #should only happen on the first tries (first #depth tries)
        elif self.sons == []:
            return random_from_distrib(self.leaf)
        else:
            if len(self.sons) == 2:
                if self.sons[previous_modes[-1][1]].leaf != [0,0,0]:
                    return self.sons[previous_modes[-1][1]].find_next(previous_modes)
            else:
                if self.sons[previous_modes[-1][0]].leaf != [0,0,0]:
                    return self.sons[previous_modes[-1][0]].find_next(previous_modes[:-1])
            return random_from_distrib(self.leaf) # The son has no value
    
    
    
    
    
    
    

class AI_first():
    
    def __init__(self, memory):
        self.memory = memory
        self.tree = Decision_Tree(memory)
        self.previous_moves = list()
    
    def played(self, move):
        """take the object played and the result as a tuple"""
        
        if len(self.previous_moves) < memory:
            self.previous_moves.append(move)
        else:
            self.tree.add(self.previous_moves, move[0])
            self.previous_moves.pop(0)
            self.previous_moves.append(move)
    
    def find_next_move(self):
        probable_opponent = self.tree.find_next(self.previous_moves)











if __name__ == "__main__":
    memory = int(input("How much will it learn (N is good)? "))
    bot = AI_first(memory)
    score_ai = 0
    score_player = 0
    answer = 0
    while answer != 3:
        bot.find_next_move()
        move = {"r":0, "rock":0, "p":1, "paper":1, "s":2, "scissors":2, "q":3, "quit":3}[input("What do you play (r(ock), p(aper), or s(cissors))? q(uit) to quit. ")]
        








