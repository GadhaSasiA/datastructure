from collections import deque

my_stack=deque()

my_stack.append("item 1")
my_stack.append("item 2")
my_stack.append("item 3")

item=my_stack.pop()
print("deleted item:",item)

print("is the stack empty?") 