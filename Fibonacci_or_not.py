def fibs():
    a,b = 0,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b

n = int(input())
for fib in fibs():
    if n == fib:
        print("True")
        break
    if fib > n:
        print("False")
        break