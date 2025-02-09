# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # print(l1)
        # print(l2)
        
        carry, mod_result = divmod(l1.val + l2.val, 10)
        print(carry, mod_result)
        result = ListNode(mod_result)
    
        print(result)
        addition = 0
        result_copy = result

        cur1, cur2 = l1.next, l2.next
        while cur1 or cur2:
            if not cur1:
                addition = cur2.val + carry
            elif not cur2:
                addition = cur1.val + carry
            else:
                addition = cur1.val + cur2.val + carry

            carry, mod_result = divmod(addition, 10)
            print(f"{carry=}, {mod_result=}")
            result.next = ListNode(mod_result)

            if cur1:
                print(f"{cur1.val=}")   
                cur1 = cur1.next
            if cur2:
                print(f"{cur2.val=}")   
                cur2 = cur2.next
            print()     
            result = result.next
            print(f"{result=}")
            print(f"{result_copy=}")
        if carry != 0:
            result.next = ListNode(carry)
        
        return result_copy