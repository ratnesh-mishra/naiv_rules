__author__ = 'ratnesh.mishra'

from noob_rules.nrules.ordered_members import OrderedClassMembers


class Executor:
    ruleset = None

    @classmethod
    def set_client(cls, ruleset):
        cls.ruleset = ruleset

    @classmethod
    def execute(cls, data):
        for each in cls.ruleset.__ordered__:
            if callable(getattr(cls.ruleset, each)):
                func = getattr(cls.ruleset, each)
                res = func(data)
                if res:
                    return True
        else:
            return False


class Evaluator(metaclass=OrderedClassMembers):
    pass





