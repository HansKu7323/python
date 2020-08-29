# while loop
# sum=0
# n=0
# while n<=10:
#   sum=sum+n
#   n+=1
# print(sum)
# break
# n=0
# while n<5:
#   if n==3:
#     break
#   print(n)
#   n+=1
# print("最後的n:",n)


# for loop
# s=0
# for x in range(1,11): # rnage(11)
#   s=s+x
# print(s)
# continue
# m=0
# for x in [0,1,2,3,4,5,6]:
#   if x%2==0:
#     continue
#   print(x)
#   m+=1
# print("最後的m:",m)


# else
# sum=0
# for n in range(11):
#   sum+=n
# else:
#   print(sum)


  # 綜合範例：找出整數平方根
n=int(input("請輸入一個正整數"))
for i in range(n):
  if i*i==n:
    print("整數平方根",i)
    break # 用break強制結束迴圈時，不會執行else區塊
else:
  print("沒有整數平方根")