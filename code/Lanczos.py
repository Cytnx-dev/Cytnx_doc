import sys
sys.path.append("../../Cytnx")

import cytnx


class MyOp(cytnx.LinOp):
    def __init__(self):
        cytnx.LinOp.__init__(self,"mv",4)

    def matvec(self,v):
        A = cytnx.arange(16).reshape(4,4)
        A += A.permute(1,0)
        return cytnx.linalg.Dot(A,v)


op = MyOp()

v0 = cytnx.arange(4) # trial state
ev = cytnx.linalg.Lanczos_ER(op,k=1,Tin=v0)

print(ev[0]) #eigen val
print(ev[1]) #eigen vec
