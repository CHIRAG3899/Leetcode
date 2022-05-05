#Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
#
#Implement the MyStack class:
#
#void push(int x) Pushes element x to the top of the stack.
#int pop() Removes the element on the top of the stack and returns it.
#int top() Returns the element on the top of the stack.
#boolean empty() Returns true if the stack is empty, false otherwise.
#Notes:
#
#You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
#Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
# 
#
#Example 1:
#
#Input
#["MyStack", "push", "push", "top", "pop", "empty"]
#[[], [1], [2], [], [], []]
#Output
#[null, null, null, 2, 2, false]
#
#Explanation
#MyStack myStack = new MyStack();
#myStack.push(1);
#myStack.push(2);
#myStack.top(); // return 2
#myStack.pop(); // return 2
#myStack.empty(); // return False

class MyStack(object):
    '''
    Implement Stack using Queues
    '''
    def __init__(self):
        self.queue = []

    def push(self, x):
        # convert queue to stack
        self.queue.append(x)
        for _ in range(1, len(self.queue)):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        return self.queue.pop(0)

    def top(self):
        return self.queue[0]

    def empty(self):
        return not self.queue

class MyStack(object):
    def __init__(self):
        self.arr = []

    def push(self, x):
        self.arr.append(x)
        
    def pop(self):
        return self.arr.pop()

    def top(self):
        return self.arr[len(self.arr)-1]

    def empty(self):
        if self.arr:
            return False
        return True