# Python: Week 1


### Task 1. Build the Environment
> 建置環境、終端機和基本語法<br>
> Learning objective: types of variable (int, float), math operations, assignment, print()

1. Install Python on your computer
2. Open `cmd`
3. Run `python` in the terminal and use it as a calculator. E.g.

```python
> from math import sqrt
> a = 6
> b = 16
> print(a + b)   
> print(a - b)    
> print(a * b)
> print(a / b)
> print((a + b) * (a - b))
> c = sqrt(b)
> print(c)
```

> 剛剛輸入的 a b 都是變數，變數可以想像為標籤的箱子，想裝什麼就裝什麼！

>「=」讀作「指定為」，所以 「a = 6」讀作「把 a 指定為 6」 或者 「把 6 指定給 a」

1. Remove `from math import sqrt` and see what happens?
2. Can `b` be 0 or -1? 

```python
> print(type(a))
> print(type(c))
```

### Task 2. Break this code!
> 來搞破壞吧！ 把裡面的符號隨興地改動，程式還能不能運作呢？

```python
PI = 3.1416
radius = 1.0                       
perimeter = 2 * PI * radius
area = PI * radius * radius
print(perimeter, area)
```
> 這段程式好像在算什麼呢 ... ?

1. What does this program do? What does radius and area mean?
2. What is `PI`?
3. Rename `perimeter` to `pineapple` and `area` to `apple`. What happened?
4. Rename `print` to `show`. What happened?

> 雖然變數的命名是自由的，但是好的程式設計師會採用有意義的命名，也會配合團隊或社群的命名規範

### Task 3. My First Program: Hello World!
> 第一隻程式: Hello World <br>
> Learning objective:  string, input

1. Open text editor, type in `print("Hello World")` and save it as `hello.py`
2. Run `python hello.py`
3. How about the following pieces of code?

```python
message = input("Type something:")
print(message)
```

```python
greeting = "Hi." + "How are you?"
print(greeting)
```


### Task 4. Get your hand dirty!
> 動手寫寫看！ <br>
> Learning objective: if-elif-else, boolean

```python
score = int(input("Score of math exam:"))
if score >= 60:
    print("Passed :)")
```
1. What does this code do?
2. Remove `int` before input? What happened?
3. let `pass_condition = score >= 60` and write `if pass_condition`. What will happen? What is the type of `pass_condition`?
4. Add `else`

```python
score = int(input("Score of math exam:"))
if score >= 60:
    print("Passed :)")
else:
    print("Failed :(")
```

5. Add `elif`

```python
score = int(input("Score of math exam:"))
if score >= 90:
    print("Excellent !!")
elif score >= 60:
    print("Passed :)")
else:
    print("Failed :(")
```