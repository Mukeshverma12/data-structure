class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Linklist:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("List is Empty")
            return
        listr=''
        itr=self.head
        while itr:
            listr+=str(itr.data)+'-->'
            itr=itr.next
        print(listr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_value(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        while self.head:
            count+=1
            self.head=self.head.next
        return count

    def remove_index(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

if __name__=='__main__':
    li=Linklist()
    li.insert_value(['mukesh','rahul','dravid'])
    li.remove_index(2)
    li.print()
    print("length of linked list",li.get_length())
    
