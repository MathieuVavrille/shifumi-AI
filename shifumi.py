from random import randint

def find_all_index_max(l):
    m = max(l)
    ret = []
    for i in range(len(l)):
        if l[i] == m:
            ret.append(i)
    return ret

class Decision_Tree():
    """0 -> player have lost, 1 -> player have won, r,p,c -> 0,1,2"""
    
    
    def __init__(self, depth, full = True):
        if depth == 0:
            self.sons = []
            self.leaf = [0,0,0]
        elif full:
            self.sons = [Decison_Tree(depth, False) for i in range(0,1)]
            self.leaf = -1
        else:
            self.sons = [Decison_Tree(depth-1, True) for i in range(0,2)]
            self.leaf = -1
    
    
    def add(self, previous_moves, played, full = True):
        if self.sons != []:
            self.sons[previous_moves[-1][1]].sons[previous_moves[-1][0]].add(previous_moves[:-1], played)
        else:
            self.leaf[played] += 1
    
    
    def sum_all(self):
        if self.leaf == -1:
            return [0,0,0]
        elif self.sons == []:
            return self.leaf
        else:
            results = [subtree.sum_all() for subtree in self.sons]
            ret = [0,0,0]
            for l in results:
                for i in range(0,2)
                    ret[i] += l[i]
            return ret
    
    def find_next(self, previous_moves):
        if self.leaf != -1
        

class AI_first():
    
    def __init__(self, memory):
        self.memory = memory
        self.data = dict()
        self.previous_moves = list()
    
    def played(self, move):
        """take the object played and the result as a tuple"""
        
        if len(self.previous_moves) < memory:
            self.previous_moves.append(move)
        else:
            self.data[previous_moves] = move[0]
            self.previous_moves.pop(0)
            self.previous_moves.append(move)
    
    def find_next_move(self):
        if len(self.data) == 0:
            return randint(0,2)
        else:
            return 0











if __name__ == "__main__":
    print(find_all_index_max([0,1,5,3,5,2,0,5,4,-20,3,5]))
    """memory = int(input("How much will it learn (N is good)? "))
    bot = AI_first(memory)
    score_ai = 0
    score_player = 0
    answer = 0
    while answer != 3:
        bot.find_next_move()
        move = {"r":0, "rock":0, "p":1, "paper":1, "s":2, "scissors":2, "q":3, "quit":3}[input("What do you play (r(ock), p(aper), or s(cissors))? q(uit) to quit. ")]
        """








