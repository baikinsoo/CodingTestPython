'''
1. 연결 리스트 두개 만들어
2. 헤드 넣어
3. 값 비교하면서 새로운 연결 리스트에 넣어
'''

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

class Solution:
    def mergeTwoList(self, node1, node2):
        if (not node1) or (node2 and node1.val > node2.val):
            node1, node2 = node2, node1
        if node1:
            node1.next = self.mergeTwoList(node1.next, node2)
        return node1

    def mergeTwoList2(self, node1, node2):
        dummy_head = ListNode()
        node = dummy_head

        while node1 != None and node2 != None:
            if node1.val <= node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next

        if node1 != None:
            node.next = node1
        elif node2 != None:
            node.next = node2

        return dummy_head.next

l1 = LinkedList()
l2 = LinkedList()
for num in [1,2,4]:
    l1.append(num)
for num in [1,3,4]:
    l2.append(num)
solution = Solution()
answer2 = solution.mergeTwoList2(l1.head, l2.head)
answerList2 = []
while answer2:
    answerList2.append(answer2.val)
    answer2 = answer2.next
print(answerList2)

