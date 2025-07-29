# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binaryStr = ""
        res = 0
        curr = head
        while curr != None:
            binaryStr += str(curr.val)
            curr = curr.next
        for i in range(len(binaryStr)):
            if binaryStr[i] == '1':
                res += 2 ** (len(binaryStr) - 1 - i)
        return res
        