from src.tests.mocking_utils import Mock
from src.control_decorators import *

__all__ = ["BasicDecoratedTestMethods"]

def _verify_for(func):
    def nested(*args):
        func(*args)
        assert BasicDecoratedTestMethods.FOR_COUNT == BasicDecoratedTestMethods.EXPECTED_FOR_COUNT
    return nested

def _while_condition():
    return BasicDecoratedTestMethods.DYNAMIC_WHILE_COUNT < 5

def _verify_while(func):
    def nested(*args):
        func(*args)
        assert BasicDecoratedTestMethods.DYNAMIC_WHILE_COUNT == BasicDecoratedTestMethods.EXPECTED_DYNAMIC_WHILE_COUNT
    return nested

def _verify_with(func):
    def nested(*args):
        assert func(*args)
        assert BasicDecoratedTestMethods.MOCK_OBJ.__enter__.called
        assert BasicDecoratedTestMethods.MOCK_OBJ.__exit__.called
    return nested

class BasicDecoratedTestMethods(object):
    EXPECTED_CONTEXT_COUNT = 3
    EXPECTED_DYNAMIC_WHILE_COUNT = 5
    EXPECTED_FOR_COUNT = 5
    EXPECTED_WHILE_COUNT = 5
    DYNAMIC_WHILE_COUNT = 0

    FOR_COUNT = 0

    CONTEXT_COUNT = 0

    MOCK_OBJ = Mock()
    MOCK_OBJ.__enter__ = Mock(return_value=Mock())
    MOCK_OBJ.__exit__ = Mock(return_value=Mock())


    @if_(True)
    @staticmethod
    def if_test_true():
        raise Exception("passed through")

    @if_(False)
    @staticmethod
    def if_test_false():
        raise Exception("did not pass through")

    @_verify_with
    @with_(MOCK_OBJ)
    @staticmethod
    def with_test():
        return True

    @_verify_while
    @dynamic_while(_while_condition)
    @staticmethod
    def dynamic_while_test():
        BasicDecoratedTestMethods.DYNAMIC_WHILE_COUNT += 1

    @_verify_for
    @for_x_times(5)
    @staticmethod
    def for_test():
        BasicDecoratedTestMethods.FOR_COUNT += 1
