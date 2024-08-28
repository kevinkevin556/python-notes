# Python: Week 4
> 複習一下上次的內容！

##### 定義函式
在 Python 中，函式使用 def 關鍵字來定義。下面是一個簡單的函式範例：

```python
def greet(name):
    """
    這個函式用來問候一個人
    參數:
        name (str): 要問候的人的名字
    """
    print(f"Hello, {name}!")
```

##### 調用函式
定義函式之後，可以通過函式名稱和參數來調用它：
```python
greet("Alice")
```


##### 帶有返回值的函式
函式可以返回一個值，使用 return 關鍵字：
```python
def add(a, b):
    """
    這個函式返回兩個數的和
    參數:
        a (int/float): 第一個數
        b (int/float): 第二個數
    返回:
        int/float: 兩個數的和
    """
    return a + b
```
```python
result = add(5, 3)
print(result)
```

##### 帶有預設參數值的函式
函式參數可以有預設值，如果調用時未提供相應的參數，則使用預設值：
```python
def greet(name, message="Hello"):
    """
    這個函式用來問候一個人，使用預設或自定義的問候語
    參數:
        name (str): 要問候的人的名字
        message (str): 問候語，預設為 "Hello"
    """
    print(f"{message}, {name}!")
```

```python
greet("Bob")
greet("Bob", "Good morning")
```

## import
用別人寫好的函數，超方便！

import 陳述式最簡單的用法就是「import 模組名稱」，模組名稱是不包含 .py 的名稱，舉例來說，下方的程式碼匯入 datetime 模組，就能使用裡面 datetime 和 date 的方法，顯示目前的時間與日期 ( 其他頁面有更多標準函式庫的介紹 )。

```python
import datetime
print(datetime.datetime.now())   # 2021-10-18 06:39:48.998396
print(datetime.date.today())     # 2021-10-18
```

#### as 替模組新增別名 
如果匯入的模組名稱和原本程式碼裡使用的相同，就必須修改其中一個的名稱 ( 修改模組或自己的程式 )，這時可以將模組使用「別名」的方式匯入，就不會更動到自己的程式，使用的方法為「import 模組 as 別名」，舉例來說，下方的程式碼將匯入 datetime 模組使用「as」賦予 datetime 一個別名 dd，使用時只要呼叫 dd，就等同呼叫 datetime。

```python
import datetime as dd
print(dd.datetime.now())   # 2021-10-18 06:39:48.998396
print(dd.date.today())     # 2021-10-18
```

## 應用

#### matplotlib
畫圖。
```python
import matplotlib.pyplot as plt
xs = [1, 2, 3, 4, 5]
ys = [2, 3, 5, 7, 11]

plt.scatter(xs, ys, c='blue', marker='o')
plt.show()
```
我們在 x y座標上畫了 `(1, 2), (2, 3), (3, 5), (4, 7), (5, 11)` 這 5 個點。

#### random
製造隨機數。
```python
import random 
random.random()
``` 
這會在 (0, 1) 區間裡面任意抽取一個數。

Q: 想一想，怎麼在 (0, 2) 之間任意抽一個數？ (1, 3) 之間呢？ (-1, 1) 之間呢？


##### 蒙特卡羅方法 (Monte Carlo method)

1. 怎麼在 (-1, 1) x (-1, 1) 上隨機產生點呢？
```python
n = 100
xs = []
ys = []

for i in range(n):
    x = random.random() * 2 - 1 
    y = _____________
    x._______(_______)
    y._______(_______)
```

2. 這個點有沒有在半徑為1的圓裡面?
```python
def in_circle(x, y):
    if _______:
        return True
    else:
        return False
```


3. 把圓裡面的點跟圓外面的點分開
```python
xs_inside_circle = []
ys_inside_circle = []

xs_outside_circle = []
ys_outside_circle = []


for i in range(n):
    if in_circle(_______):
        xs_inside_circle.append(xs[i])
        ys_inside_circle.append(ys[i])
    else:  
        _______
        _______
```

4. 把點畫成 2 個顏色
```python
plt.scatter(xs_inside_circle, ys_inside_circle, c=_____, marker='o')
plt.scatter(xs_outside_circle, ys_outside_circle, c=_____, marker='o')
plot.show()
```
有沒有看出圓形呢？


5. 下面這個數應該要接近多少呢？
```python
print(len(xs_inside_circle) / n * 4)
```
當 n = 10, 100, 1000, 10000, 100000, 100000000? 把上面的程式碼包裝成function，然後把數字帶進去看看


## Assignment
這周練習看看 zerojudge 中的 a244, b836, a020, d562 吧！