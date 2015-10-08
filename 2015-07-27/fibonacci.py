#!/usr/bin/env python


import unittest


cache = {}
count = 0

class TestDojo(unittest.TestCase):

    def setUp(self):
        clean_cache()

    def test_clean_cache(self):
        cache[1] = 1
        clean_cache()
        assert len(cache) == 0

    def test_fib1(self):
        assert fib(1) == 1

    def test_fib2(self):
        assert fib(2) == 1

    def test_fib3(self):
        assert fib(3) == 2

    def test_fib8(self):
        assert fib(8) == 21

    def test_cache(self):
        assert cache == {}

    def test_cache_fib2(self):
        fib(2)
        assert cache[2] == 1

    def test_using_cache(self):
        fib(3)
        assert count == 4

def clean_cache():
    cache.clear()
    global count
    count = 0

def cachee(f):
    def fibb(n):
        if n in cache:
            return cache[n]

        res = f(n)
        cache[n] = res

        return res

    return fibb


@cachee
def fib(n):
    global count
    count += 1

    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    unittest.main()
