__author__ = 'ratnesh.mishra'

""" Sample example demonstrating use of noob rules """

from nrules.decorators import *
from nrules.executor import Executor, Evaluator

lest = ['dert', 'purr', 'heamm', 'shitt']


class evaluate(Evaluator):

    @condition([{"ruleset.a": ('==', 3), "ruleset.b": ('in', lest)}, {"ruleset.c": ('>', 4), "ruleset.d": ('<', 4)}])
    def print_hello(self, data):
        print('hello')

    @condition([{"ruleset.a": ('==', 5), "ruleset.b": ('in', lest)}, {"ruleset.c": ('>', 4), "ruleset.d": ('<', 4)}])
    def print_world(self, data):
        print('world')

    @condition([{"ruleset.a": ('==', 4), "ruleset.b": ('in', lest)}, {"ruleset.c": ('>', 4), "ruleset.d": ('<', 4)}])
    def print_mister(self, data):
        print('mister')

if __name__ == '__main__':
    data = ('data', {'a': 5, 'b': 'shitt', 'c': 3, 'd': 5})
    e = evaluate()
    Executor.ruleset = e
    Executor.execute(data)

