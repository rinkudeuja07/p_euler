# 1 multiple of 3 and 5
sum = 0
for i in range (1, 1000):
    if i % 3 ==0 or i % 5 ==0:
        sum += i
print(sum)

# 2 Fibonacci series
a = 1
e = 1
fibo = 0
sum_even_fibo = 0
while True:
    fibo = a+e
    a = e
    e = fibo
    if fibo % 2 == 0:
        sum_even_fibo += fibo

    # print(fibo)
    if sum_even_fibo > 4000000:
        break
print(sum_even_fibo)

# 3 Largest prime factor
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    if n > 1:
        return n


largest_factor = largest_prime_factor(600851475143)

print("The largest prime factor of 600851475143 is", largest_factor)

# 4 Largest palindrome number

def is_palindrome(n):
      return str(n) == str(n)[::-1]

largest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product) and product > largest_palindrome:
            largest_palindrome = product

print("The largest palindrome numbers is:", largest_palindrome)


#5 Smallest positive number

def prime(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // prime(a, b)

result = 1
for i in range(1, 21):
    result = lcm(result, i)

print("The smallest positive number is:", result)
