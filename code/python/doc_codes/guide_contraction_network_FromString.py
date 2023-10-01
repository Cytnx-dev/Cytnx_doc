net = cytnx.Network()
net.FromString(["c0: t0-c0, t3-c0",\
                "c1: t1-c1, t0-c1",\
                "c2: t2-c2, t1-c2",\
                "c3: t3-c3, t2-c3",\
                "t0: t0-c1, w-t0, t0-c0",\
                "t1: t1-c2, w-t1, t1-c1",\
                "t2: t2-c3, w-t2, t2-c2",\
                "t3: t3-c0, w-t3, t3-c3",\
                "w: w-t0, w-t1, w-t2, w-t3",\
                "TOUT:",\
                "ORDER: ((((((((c0,t0),c1),t3),w),t1),c3),t2),c2)"])
