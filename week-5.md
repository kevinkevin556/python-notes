# Python: Week 5
> 複習一下之前的內容！

### 讓 a 遞增 1
```python
a = 1
# ???
print(a)
```

### 把 a 指定為 a-b-c 的值
```python
a = 10
b = 3
c = 2
# ???
print(a)
```

### 取餘數
```python
a = 11
print(a % 3) # 結果是什麼呢?
```

### 比大小
```python
a = 3 > 2
b = 3 <= 2
c = True
print(a == b, a == c) # 結果是什麼呢?
```

### 取小數點
```python
number_float = 1.234
number_int = int(number_float)
if (number_float - number_int) < 0.5:
    # ???
else:
    # ???
print(number)
```

### 一直加
```python
a = 0
for i in range(12):
    a = a + i   # or ???
print(a) # 結果是什麼呢?
```
跳著加：只加奇數位怎麼做呢？

### 排列
```python
for i in :
    for j in a:
        for k in a:
            print(f"{i}{j}{k}")
# 總共有幾列 ?
```

### 組合
```python
a = [1, 2, 3]
for i in range(1, 4):
    for j in range(1, i):
        for k in range(1, j):
            print(f"{i}{j}{k}")
# 總共有幾列?
```

### 九九乘法
```python
for i in range(1, 10):
    for j in range(1, 10):
        # ans = ???
        print(i, "x", j, "=", ans)
```


### 依序印出
```python
my_list = ["a", 1, "b", 2, ["abc", "def"]]
for x in my_list:
    print(x)

for i in range(len(my_list)):
    print(my_list[i])
```
倒序印出怎麼做？(Hint: 可以用`range`)

### 去頭去尾
```python
word = "Example"
my_list = [1, 2, "a", "b"]

# print(word[ : ]) ??? => "xampl"
# print(my_list[ : ]) ??? => [2, "a"]
```

### 無窮迴圈
設計一個終極密碼遊戲！填入`###`完成它。
```python
min_number = 1
max_number = 20
answer = 11

while True
    guess = int(input(f"請輸入{min_number}到{max_number}之間的數字"))
    if guess < answer:
        ###
    elif guess > answer:
        ###
    else:
        print("猜對了")
        ###
```
`while` 跟 `break` 的組合可以拿來設計遊戲控制。 

### 函式
```python
def greet(name):
    return "Hi " + name 

# 預設值 = Jack ???
```
