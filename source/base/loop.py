import os
import re

# 输出
print("有效输出")

# 运算
a,b = 1,2
print(a + b)

# 删除a的引用
del a
print(b)

# 列表 & 循环
b = ['1','2','3']
for value in b:
    print(value)

# 引入
from count import sayHello

# 字典
a = {"name": "张三", "code": "zs", 2: "num"}
print(a[2])

# 判断
key = "code"
if a["code"] == a[key] :
    print("key是有效的")
elif a["name"] == "李四":
    print("key可能无效")
else:
    print("key无效")

# 函数
print(sayHello(a["name"]))

# 读写
f = open("../io/test.txt", 'r', encoding='utf-8')
print(f.readlines())
f.close()

f = open("../io/test.txt", 'w', encoding='utf-8')
f.write("this is test /n")

# 异常
try:
    b = a / 0
except Exception:
    print("error")

# 类
class MyShill:
    status = "java"
    def saySkill(self):
        return self.status

x = MyShill()
print(x.saySkill())

# 引入库
print("当前目录：" + os.getcwd())

print(re.match("www","www.baidu.com"))