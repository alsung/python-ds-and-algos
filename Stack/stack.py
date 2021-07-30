# Stacks in Python

# stack associated functions:
#   - empty() - Returns whether stack is empty                  Time: O(1)
#   - size()  - Returns size of stack                           Time: O(1)
#   - top()   - Returns a reference to top most element (peek)  Time: O(1)
#   - push(g) - Adds element 'g' to top of stack                Time: O(1)
#   - pop()   - Return and deletes topmost element of stack     Time: O(1)

# can be implemented using:
#   - list
#   - collections.deque
#   - queue.LifoQueue

list_stack = []

# append() to push element to stack
list_stack.append('a')
list_stack.append('b')
list_stack.append('c')

print("Initial list stack: ", list_stack)

# list_stack[-1] will retrieve but not remove top element of stack 
# use this to perform the peek() stack function
print("peep() using list_stack[-1]")
print(list_stack[-1])

# pop() to pop element from stack in LIFO order
print("Elements popped from stack:")
print(list_stack.pop())
print(list_stack.pop())
print(list_stack.pop())

print("Stack after elements are popped: ", list_stack)

