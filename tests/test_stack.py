from testing.stack import Stack
import pytest



def test_push(data) :
    actual = data.top.value
    expected = 'wrekat'
    assert expected == actual


def test_pop(data) :
    actual = data.pop()
    expected = 'wrekat'
    assert expected == actual



@pytest.fixture
def data() :
    stack = Stack()
    stack.push('mhmad')
    stack.push(25)
    stack.push('wrekat')
    return stack