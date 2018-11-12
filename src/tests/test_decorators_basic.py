import pytest

from src.tests.basic_decorated_test_methods import BasicDecoratedTestMethods


class TestDecoratorsBasic(object):
    def test_if_decorator(self):
        try:
            BasicDecoratedTestMethods.if_test_true()
        except:
            pass
        else:
            pytest.fail("did not pass through if logic")

        try:
            BasicDecoratedTestMethods.if_test_false()
        except:
            pytest.xfail("still called if decorated")

    def test_with_decorator(self):
        BasicDecoratedTestMethods.with_test()

    def test_dynamic_while_decorator(self):
        BasicDecoratedTestMethods.dynamic_while_test()

    def test_for_decorator(self):
        BasicDecoratedTestMethods.for_test()
