temp=0
class linkeListNode:
    point=None
    val=None


class linkedListOperation:
    

    def insertBegLinkedList(tempVal):
        global temp
        tempObjLinkedList= linkeListNode()
        if temp==0:
            temp=tempObjLinkedList
            tempObjLinkedList.val=tempVal
        else:
            tempObjLinkedList.point=temp
            temp=tempObjLinkedList
            tempObjLinkedList.val=tempVal

    def traverseLinkedList():
        if temp==0:
            print("No Node in Linked List")
        else:
            traversetemp=temp
            while traversetemp!=None:
                print(traversetemp.val) 
                traversetemp=traversetemp.point
    
    def insertEndLinked(tempVal):
        tempObjLinkedList= linkeListNode()
        tempObjLinkedList.val=tempVal
        if temp==0:
            print("No Node in Linked List")
        else:
            traversetemp=temp
            lastTemp=None
            while traversetemp!=None:
                lastTemp=traversetemp
                traversetemp=traversetemp.point
        lastTemp.point=tempObjLinkedList


ll=linkedListOperation
ll.insertBegLinkedList(200)
ll.insertBegLinkedList(300)
ll.insertBegLinkedList(400)
ll.insertBegLinkedList(500)
ll.insertBegLinkedList(600)
#ll.traverseLinkedList()
ll.insertEndLinked(600)
ll.insertEndLinked(500)
ll.insertEndLinked(400)
ll.insertEndLinked(300)
ll.insertEndLinked(200)
ll.traverseLinkedList()