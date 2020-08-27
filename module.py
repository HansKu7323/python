# 載入內建的 sys 模組並取得資訊
# import sys
# print(sys.platform)
# print(sys.maxsize)
# import sys as system # 使用別名
# print(system.platform)
# print(system.maxsize)

# 建立 geometry 模組，載入使用
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)
# res=geometry.slope(1,2,5,6)
# print(res)

# 調整搜尋模組的路徑
# import sys
# print(sys.path) # 印出模組的搜尋路徑列表

import sys
sys.path.append("modules")
print(sys.path) # 印出模組的搜尋路徑列表
import geometry
result=geometry.distance(1,1,5,5)
print(result)
res=geometry.slope(1,2,5,6)
print(res)