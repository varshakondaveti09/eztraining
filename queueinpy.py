queue=[]

def enqueque():
    if len(queue)==n:
        print("stack is full")
    else:
        element=input("enter element ")
        queue.append(element)
        print(queue)
        
def dequeue():
    if not queue:
        print("stack is empty")
    else:
        e=queue.pop(0)
        print(e,"removed")
        print(queue)
        
n=int(input("enter the size"))
while True:
    print("select option 1.enqueue 2.dequeue 3.quit")
    choice=int(input())
    if choice==1:
        enqueque()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("enter correct option")
