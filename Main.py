def push(self,data):
    node = Node(data,self.head)
    self.head=node

def pop(self):
    if self.head is None:
        print("Stack is Empty")
        return
    print("&quot";\n Poppped item :", self.head.data)
    self.head = self.head.next



#QUEUE
def enqueue(self,data):
    node = Node(data,None)
    if self.front is None:
        self.front = node
        self.rear = node
    else:
        self.rear.next = node
        self.rear = node

def dequeue(self):
    if self.front is None:
        print(&quot;Queue is empty!&quot;)
        return
    else:
        print(&quot;\nPopped item:&quot;,self.front.data)
        self.front = self.front.next
    if self.front is None:
        self.rear = None
