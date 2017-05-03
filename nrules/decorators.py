__author__ = 'ratnesh.mishra'

from functools import wraps

_WHERE_AND = '{} {} {}'
from collections import namedtuple


def _get_evaluate_expression(where_keys):
    def make_and_query(ele: dict):
        and_query = ' and '.join([_WHERE_AND.format(e[0], e[1][0], e[1][1]) for e in ele.items()])
        return '(' + and_query + ')'
    expr = ' or '.join(map(make_and_query, where_keys))
    return expr


def condition(conditions: list):
        def decor(func):
            @wraps(func)
            def wrapper(self, data):
                ruleset = namedtuple(data[0], data[1].keys())(**data[1])
                expr = _get_evaluate_expression(conditions)
                s = eval(expr)
                if s:
                    res = func(self, data)
                    return res or True
                else:
                    return False

            return wrapper
        return decor


