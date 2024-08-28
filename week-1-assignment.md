# Week 1: Assignment


### 1. Add parentheses to the following expression so that it evaluates to ...
> 把下面的程式碼加上小括號 (parentheses) 使得計算得到的值為 ...
```python
8 - 3 * 2 - 1 + 1    # = 0 ?
5 - 3 // 2           # = 1 ?
``` 

### 2. What does this code do?
> 下面的程式碼在做什麼？ 什麼時候不能正確運行呢？

```python
from math import sqrt

a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))

root1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
root2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

print(root1, root2)
```

After understanding how the program works, do the following steps:

1. Set `D = b**2 - 4*a*c`, where D stands for **discriminant** (look up this word in your dictionary).
2. When will the code make mistake? Use if-else to exclude the case.
3. Solve $-24x^2+22x+12=0$ with your program

### 3. What does this code do?
> 下面的程式碼在做什麼？ 要加上那個條件比較正確呢？

```python
from math import sqrt

a = float(input("a ="))
b = float(input("b ="))

hypotenuse = sqrt(a*2 + b*2)
print(hypotenuse)
```

1. What is a **hypotenuse**? Look up this word in your dictionary.
2. Which one is a good condition for the program?
   1. `a > 0 and b > 0`
   2. `a > 0 or b > 0`

### 4. String operations
Try it yourself.

```python
text = "Say hello"
text1 = "to my little friends."

print(text[0])
print(text[1])
print(text[-1])
print(text + " " + text2)
print(text * 3)
print(text ** 3)
print(text.split())
```

### 5. Add more conditions to the code in Task 4.
```python
score = int(input("Score of math exam:"))
if score >= 90:
    print("Excellent !!")
elif score >= 60:
    print("Passed :)")
else:
    print("Failed :(")
```

### 6. Break the code!
> 來搞破壞吧！ 把裡面的符號隨興地改動，程式還能不能運作呢？

```python
numbers = ["one", "two", "three", "four", "five"]

for i in range(5):
   print(i, numbers[i])

for n in numbers:
   print(n)
```

What does `range` mean?
