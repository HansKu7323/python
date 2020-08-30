# 定義函式
def multiply(n1,n2):
  # print(n1*n2)
  return n1*n2
# 呼叫函式
value=multiply(3,4)+multiply(5,10)
print(value)

#函式可用來程式的包裝，同樣的邏輯可以重覆利用
def calculate(n1,n2):
  sum=0
  for n in range(n1,n2+1):
    sum=sum+n
  print(sum)

calculate(1,10)
calculate(1,20)


# 使用參數名稱對應
def divide(n1,n2):
  print(n1/n2)
divide(2,4)

# 無限/不定 參數資料
def avg(*ns):
  sum=0
  for n in ns:
    sum=sum+n
  print(sum/len(ns))

avg(3,5,10)
