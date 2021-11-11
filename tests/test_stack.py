"""
from testing.stack import Stack
import pytest
from testing.node import Node

def test_node_value() :
    num = Node
    assert str(num(5)) == '5'

def test_stack_push() :
    stack = Stack()
    stack.push('401')
    actual = stack.top.value
    expected = '401'
    assert expected == actual

def test_stack_push_multiple(data) :
    actual = data.top.value
    expected = 'wrekat'
    assert expected == actual

def test_stack_pop(data) :
    actual = data.pop()
    expected = 'wrekat'
    assert expected == actual

def test_stack_empty_after_pop() :
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.top == None

def test_peek(data) :
    assert 'wrekat' == data.peek().value

def test_stack_empty() :
    stack = Stack()
    expected = True
    actual = stack.isEmpty()
    assert expected == actual

def test_stack_raise_exception():
  stack = Stack()
  with pytest.raises(Exception, match ="Its Empty" ):
      stack.peek()

@pytest.fixture
def data() :
    stack = Stack()
    stack.push('mhmad')
    stack.push(25)
    stack.push('wrekat')
    return stack
"""