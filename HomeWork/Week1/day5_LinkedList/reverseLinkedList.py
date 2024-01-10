class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)

class Solution():
    def reverseList(self, head):
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev

l1 = LinkedList()
for num in [1,2,3,4,5]:
    l1.append(num)

solution = Solution()
answer = solution.reverseList(l1.head)
answerList = []
while answer:
    answerList.append(answer.val)
    answer = answer.next
print(answerList)






