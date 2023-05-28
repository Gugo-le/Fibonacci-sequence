# 피보나치 수열(Fibonacci Sequence)

피보나치 수열이란?<br>

```
특정 위치의 숫자는 첫번째 바로 앞에 숫자와 두번째 앞의 숫자를 더한 것이 되는 수열을 의미한다.
```

<img src = "fibo.png" width="500" height="300">

## <재귀함수의 이용>

```python
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

```

위 코드는 피보나치 수열을 재귀적으로 짠 코드이다.<br>
50번째의 피보나치 수를 구하기 위해서 n에 50을 넣고 <br>
return 하는 곳에서 함수 인자가 각각 n=49, n=48이 들어가는<br>
함수를 호출합니다. ----> 엄청난 성능 저하

