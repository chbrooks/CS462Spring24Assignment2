from unittest import TestCase
from mars_planner import *


class TestRoverState(TestCase):
    pass


class Test(TestCase):
    def test_move_to_sample(self):
        s = RoverState(loc="battery")
        move_to_sample(s)
        self.assertEqual(s.loc, "sample")


class TestRoverState(TestCase):
    def test_successors(self):
        s=RoverState()
        slist = s.successors(action_list)
        print(slist)
