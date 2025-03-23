#只读
# fs = open(r"C:\Users\haiyang.yu\PycharmProjects\pythonProject4\study\函数30.txt",encoding="utf-8")
# s = fs.read()
# print(s)

#只写 覆盖
# fs = open(r"C:\Users\haiyang.yu\PycharmProjects\pythonProject4\study\函数30.txt","w",encoding="utf-8")
# s = fs.write("今天是周末 天气很好\n")
# fs.close()
# print(s)

#写  末尾
fs = open(r"C:\Users\haiyang.yu\PycharmProjects\pythonProject4\study\函数30.txt","a",encoding="utf-8")
s = fs.write("今天是周末 天气很好\n")
fs.close()
print(s)