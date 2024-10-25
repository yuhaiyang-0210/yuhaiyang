import unittest


def my_sum(a,b):
    return a+b


class my_test1(unittest.TestCase):
    def test1_oo1(self):
        print(my_sum(5,3))

    def test1_oo2(self):
        print(my_sum(10,4))
