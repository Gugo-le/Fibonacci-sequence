import time

def iter_fibonacci(n):
    a, b = 1, 1
    if n < 2:
        return 1
    else:
        for i in range(n-2):
            c = a + b
            a, b = b, c
        return c   
  
start_time = time.time()

print(iter_fibonacci(50))

elapsed_time = time.time() - start_time

print("총 소요시간: {}초".format(elapsed_time))
