# Week 3: Assignment

#### Question 1

某商店在大特價，根據購買的商品總金額決定打折的
折扣，總金額越高折扣越多，折扣表如下：
1. 未滿 1000 元 = 無折扣
2. 1000~4999 元  = 9 折
3. 5000~9999 元 = 8 折
4. 高於 10000 元  = 7 折

小數點四捨五入，印出折扣後的金額。

#### Question 2
1. 寫一程式，輸入 x 和 y ，如果 x≥y ，則列印 x ，否則
列印 y
2. 寫一 程式，輸入 x 和 y 如果 x 和 y 都是正數，令 z=1
如兩者均為 負數，令 z= 1 否則 令 z=0
3. 寫一程式，輸入 x 、 y 、 u 、 v ，如果 x+y>u+v
則 令 z=x-y ，否則令 z=u-v


### Question 3
1. 寫一支程式，計算 1 + ... + 100 = ? (不要用等差級數偷算^^)
2. 寫一支程式，向使用者要求一個數字，得到數字後計算它的階層，也就是 n! = 1 * 2 * 3 * ... * n (n 有什麼限制呢？用 if 篩掉不適合的輸入)

#### Question 4
假設有一組二元一次方程式如下：
$$\mathrm{a_1x+b_1y=c_1~,~a_1x+b_2y=c_2}$$
寫一程式，輸入此方程式變數之係數。計算此組解。

#### Question 5
輸入 a 和 b,求
1. $c=\frac{a^1+b^2}{a^2-b^2}$
2. $c=\sqrt{a^2+b^2}$
3. $c=a-(b+c)(3a-c)$


#### Question 6
考慮下列程式，
```python
for i in range(7):
    print(i)
```
要怎麼用 while 改寫？

### Question 7 
```python
nba_teams = ["Boston Celtics", "Brooklyn Nets", "Golden State Warriors", "Phoenix Suns"]
```
向使用者要一個數字和隊名，將隊伍放到指定的list位置上。例如："1 Los Angeles Lakers"，那就變成`["Boston Celtics", Los Angeles Lakers", "Brooklyn Nets", "Golden State Warriors", "Phoenix Suns"]`