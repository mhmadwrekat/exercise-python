from testing.queue import Queue

# Test Is Empty
# Test Enqueue
# Test Dequeue
# Test Front 
# Test Rear
# Test Peek


def test_isEmpty() :
    que = Queue()
    expected = True
    actual = que.isEmpty()
    assert expected == actual


def test_enqueue() :
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue('Python')
    expected = 'Python'
    actual = queue.rear.value

