

# Idea: A better way of saying what I mean in my solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resultlist = curr = ListNode \
            (0)  # we need two varibles because if only one variable is used we might loose reference to the head
        carry = 0
        while l1 or l2 or carry: # not none
            if l1  is not None:
                carry += l1.val
                l1 = l1.next  # increase value of l1
            if l2 is not None:
                carry+= l2.val
                l2 = l2.next
            curr.next = ListNode(carry %10)  # retur remainder of division
            curr = curr.next
            carry = carry//10  # returns floor value of division

        return resultlist.next









# Idea: different cases (my solution)




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        return self.add(l1, l2, 0)

    def add(self, l1, l2, carry):
        if l1 is None and l2 is not None:
            l2.val += carry
            if l2.val >= 10:
                l2.val -= 10
                carry = 1
            else:
                carry = 0
            l2.next = self.add(l1, l2.next, carry)
            return l2
        elif l2 is None and l1 is not None:
            l1.val += carry
            if l1.val >= 10:
                l1.val -= 10
                carry = 1
            else:
                carry = 0
            l1.next = self.add(l1.next, None, carry)
            return l1
        elif l1 is None and l2 is None:
            if carry == 1:
                return ListNode(1, None)
            else:
                return None

        val1 = l1.val
        val2 = l2.val
        summ = val1 + val2 + carry
        if summ >= 10:
            carry = 1
            summ -= 10
        else:
            carry = 0

        l1.val = summ
        l1.next = self.add(l1.next, l2.next, carry)
        return l1


