# 資料，程式的基本單位

# 數字
3456 #整數
3.5  #浮點數

# 字串
"測試中文"
"Hello World"

# 布林值
True
False

# 有順序，可動式列表List
[3,4,5]
["hello","world"]
grades=[3,4,5]
string=["hello","world"]
# print(grades)
# print(string)

# 有順序，不可動式列表Tuple
s1=(3,4,5)
s2={4,5,6,7}
# s3=s1&s2 # 交集(&)：取2個集合中，相同的資料
# s3=s1|s2 # 聯集(|)：取2個集合中的所有資料，但不重複取
# s3=s1-s2 # 差集(-)：從s1中，減去和s2重疊的部分，有順序性，s1-s2和s2-s1不一樣
# s3=s1^s2 # 反交集(^)：取2個集合中，不重疊的部分
# print(s3)
print(3 in s1)
("Hello","world")

# 集合 set 集合沒有順序概念，列表有順序概念
{3,4,5}
{"Hello","world"}
s=set("Hello") # 把字串中的字母拆解成集合: set(字串)
print(s)
print("a" in s)

# 字典 Dictionary
{"apple":"蘋果","data":"資料"}
dic={"apple":"蘋果","data":"資料"}
del dic["apple"] # 刪除字典中的鍵值對(key-value pair)
print(dic)
print("apple" in dic)
print("banana" in dic)

# 變數 用英文，開頭不可用數字
x=3
y="hello"
z={3,4,5}# 集合 set


# 數字，字串的運算
x=9/6
y=9//6
print(x)
print(y)
z="Hell\"o\nworld"+"hello"*3
print(z)
s="hello"
print(s[1:])
