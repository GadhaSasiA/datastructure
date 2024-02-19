from queue import Queue

#create a new queue
my_queue=Queue()

# add elements in the queue
my_queue.put("item 1")
my_queue.put("item 2")
my_queue.put("item 3")

item=my_queue.get()# remove elements from the queue
print("deleted item:",item)

# check if the queue is empty
is_empty=my_queue.empty()
print("is the queue empty?",is_empty) 