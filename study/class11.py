# for index in range(1,10):
#     for sub in range(1,index+1):
#         print(sub,end = "  ")#end表示不换行
#     print("")
# def get_user_name(name,password,key):
#         """
#
#         :param name:
#         :param password:
#         :param key:
#         :return:
#         """
#         if name == 10:
#             print('不对')
#         if not password:
#             print('你还没输入密码')
#         if len(key) <= 10:
#             print('太短了')
#
# get_user_name('10','10',"11212")

# def get_monet_much(money,keyword,*args,**kwargs):
#     if len(money)<=6:
#         print('你还是太穷了')
#     else:print('你有钱啦')
#     if not keyword:
#         print('请输入密码')
#     print(args)
#     print(kwargs)
# get_monet_much('10000000000','123456')
# get_monet_much('10000000000','123456','10000',name = '余海洋')
def add(*args):
    sum_num = 0
    for item in args:
        sum_num += item
    return sum_num
res = add(1,2,3,4,5)
print(res)


