import numpy as np
import time

# testing speed
def test_sp():
    start = time.time()
    x = range(10000000)
    y = range(10000000)
    z = []
    for i in range(len(x)):
        z.append(x[i] + y[i])
    return time.time() - start

def test_np_sp():
    start = time.time()
    x = np.arange(10000000)
    y = np.arange(10000000)
    z = x + y
    return time.time() - start

print("test speed : ",test_sp(),"    test np speed : ",test_np_sp())


