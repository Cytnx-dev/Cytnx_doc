T = cytnx.UniTensor(cytnx.ones([5, 5, 5, 5, 5]), rowrank=3)
S1, _, _ = cytnx.linalg.Svd(Tin=T)
print(S1)
S2, _, _, err = cytnx.linalg.Svd_truncate(
    Tin=T, keepdim=10, err=1e-12, is_UvT=True, return_err=1
)
print(S2)
print(err)
