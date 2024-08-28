# Week 2: Assignment


### 1. What's the value of `a`?
> `a` 最後的數值是多少呢？ 
```python
a = 0
for i in "123456":
    if a = 0:
        a = i
    else:
        a = i + a
``` 
```python
counter = 0
a = 0
while counter < 5:
    if a % 2 == 1:
        a += 1
    else:
        a = a*2 + 1
``` 


### 2. Draw pyramids
> 用 for 迴圈畫出金字塔
```
1       2        3
*          *        *
**        **       ***
***      ***      *****
****    ****     *******
```

### 3. 9 * 9
> 用二層 for 迴圈寫出九九乘法表
```
1*1=1  1*2=2 ... 1*9=9
2*1=2  ...   ... 2*9=18
.      .     .   .
.      .     .   .
.      .     .   .
9*1=9  ...  ...  9*9=81

```
### 4. while True
> 寫一個打招呼機器人，向使用者詢問名字。
> 直到當對方說 Bye bye 時，才結束程式。

Example:
```
[START]

>>> Kevin
Hi, Kevin!

>>> Andy
Hi, Andy!

>>> Bye bye
See you! 

[END]
```
這個可以透過無窮 while 迴圈完成。
```python
while True:
    # write your code here
```

### 5. Guess a Number (?A?B)
> 猜一個每位數字不重複的 4 位數字，如果數字和位置都對了就提示A，只對了數字就提示B，最多可以猜10次

Example:
```
[START]

(Ans: 3456)

Guess the Number:
>>> 1234
0A2B

Guess the Number:
>>> 3012
1A0B

Guess the Number:
>>> 0789
0A0B

[END]
```
 
1. 先寫判斷數字的程式
2. 把剛剛的程式放在迴圈裡

這題最難的地方是 (1)，但是有很多方法可以做。
提示：
1. 過程中我們需要提取位數，也就是將一個 1234 拆成 1, 2, 3, 4 四個數字。可行的方法有：取餘數(1234取多少的餘數是1呢?)，或者直接把 1234 當成 "1234" 處理，所以第1個數字就是"1"( `"1234"[0] == 1`)。
2. 比較的時候也許可以用雙層迴圈做，位置數字都對的話 a 的值就 +1，只對數字的話 b 就 +1.

```python
guess = input("Guess a Number:") # 看你需要文字或數字，自己轉型
answer = 3456
a = 0
b = 0 

# for ...
#    for ...


print(str(a) + "A" + str(b) + "B") # 印出結果 ?A?B
```