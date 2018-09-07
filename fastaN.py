import itertools 
import fasta_reader as far 


class Key(object):
    def __init__(self):
        self.is_nt,self.flag,self.prev = ['A','T','C','G'],[0,1],None
    def __call__(self,e):
        ebool = any(x in self.is_nt for x in e)
        if self.prev:
            prevbool = any(x in self.is_nt for x in self.prev)
        else:
            prevbool = None
        if prevbool != ebool:
            self.flag = self.flag[::-1]
        self.prev = e
        return self.flag[0]
            
    
def fastaN(fa):
    return [''.join(list(g)) for k,g in itertools.groupby(fa,key=Key())]