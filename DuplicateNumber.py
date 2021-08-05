class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
        try:
            currentNode = head
            nextNode = head.next
        except:
            return head
        while nextNode != None:
            if currentNode.val == nextNode.val:
                nextNode = nextNode.next
                currentNode.next = nextNode
            else:
                currentNode = nextNode
                nextNode = nextNode.next

        return head