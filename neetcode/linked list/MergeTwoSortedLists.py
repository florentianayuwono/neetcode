# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr_1 = list1
        curr_2 = list2
        result = ListNode()
        curr_result = result

        if not (curr_1 or curr_2):
            return None

        while curr_1 or curr_2:
            if curr_1 == None:
                curr_result.val = curr_2.val
                curr_result.next = curr_2.next
                return result
            if curr_2 == None:
                curr_result.val = curr_1.val
                curr_result.next = curr_1.next
                return result
            if curr_1.val <= curr_2.val:
                curr_result.val = curr_1.val
                curr_result.next = ListNode()
                curr_result = curr_result.next
                curr_1 = curr_1.next
            else:
                curr_result.val = curr_2.val
                curr_result.next = ListNode()
                curr_result = curr_result.next
                curr_2 = curr_2.next
        
        return result
