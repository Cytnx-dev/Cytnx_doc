T = cytnx.UniTensor(cytnx.ones([5,5,5,5,5]), rowrank = 3)
Q, R = cytnx.linalg.Qr(T)
Q.set_name("Q")
R.set_name("R")

Q.print_diagram()
R.print_diagram()

# Verify the recomposition
print((Contract(Q,R)-T).Norm())