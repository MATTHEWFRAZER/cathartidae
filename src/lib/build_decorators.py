from functools import wraps

from src.builder_args import BuilderArgs
from src.control_decorator import ControlDecorator
from src.control_decorator_builder import ControlDecoratorBuilder
from src.lib.echos import echo, dynamic_echo

__all__ = ["build_decorator", "build_decorator_dynamic"]


def build_decorator(abstracted_block_constructor, operand, func, default=None):
    return build_decorator_inner(abstracted_block_constructor, echo, operand, func, default)


def build_decorator_dynamic(abstracted_block_constructor, operand, func, default=None):
    return build_decorator_inner(abstracted_block_constructor, dynamic_echo, operand, func, default)


def build_decorator_inner(abstracted_block_constructor, operand_pre_operation, operand, func, default=None):
    builder_args = BuilderArgs(operand, default, func)
    control_decorator_builder = ControlDecoratorBuilder(abstracted_block_constructor, operand_pre_operation)
    return wraps(func)(ControlDecorator(builder_args, control_decorator_builder))