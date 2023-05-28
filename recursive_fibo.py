import time

def recursive_fibonacci(n):
    if n < 2:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

start_time = time.time()

print(recursive_fibonacci(50))

elapsed_time = time.time() - start_time

print("총 소요시간: {}초".format(elapsed_time))