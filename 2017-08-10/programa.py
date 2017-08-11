#!/usr/bin/env python

import unittest
import math
import random


class Friend:
    def __init__(self, id, location):
        self.id = id
        self.location = location

    def __str__(self):
        return 'id={} location={}'.format(self.id, self.location)

    def get_closest_friends(self, friends):
        result = [{'id': friend,
                   'distance': calc_distance(self.location, friend.location)}
                    for friend in friends if friend is not self]
        result.sort(key=lambda x: x['distance'])

        return set([e['id'] for e in result[:3]])


def calc_distance(a, b):
    delta_x = a[0] - b[0]
    delta_y = a[1] - b[1]

    return math.sqrt(pow(delta_x, 2) + pow(delta_y, 2))


class ProgramaTestCase(unittest.TestCase):
    def setUp(self):
        self.friends = []
        for i in range(random.randint(0, 20)):
            self.friends.append(Friend(id=i+2, location=[i*2, i*3]))

    def test_distance_from_two_points(self):
        self.assertEqual(calc_distance([0, 0], [3, 4]), 5)
        self.assertAlmostEqual(calc_distance([0, 0], [4, 5]), 6.4, 1)
        self.assertNotAlmostEqual(calc_distance([0, 0], [4, 5]), 6.5, 1)

    def test_closest_three_friends_hard_mode(self):
        currentFriend = Friend(id=1, location=[3000, 9518570])

        self.assertEqual(currentFriend.get_closest_friends(self.friends), set(self.friends[-3:]))

    def test_closest_three_friends(self):
        currentFriend = Friend(id=1, location=[0, 0])

        self.assertEqual(currentFriend.get_closest_friends(self.friends), set(self.friends[:3]))

    def test_closest_three_friends_with_current_friend(self):
        currentFriend = Friend(id=1, location=[0, 0])
        self.friends.append(currentFriend)

        self.assertEqual(currentFriend.get_closest_friends(self.friends), set(self.friends[:3]))

if __name__ == '__main__':
    unittest.main()
