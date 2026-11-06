# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        curr = None

        while list1 or list2:
            # print(f"list1={list1}, list2={list2}")
            if list1 and list2:
                if list1.val > list2.val:
                    if not curr:
                        curr = list2
                        merged = curr
                        list2= list2.next
                    else:
                        curr.next = list2
                        curr = list2
                        list2 = list2.next
                else:
                    if not curr:
                        curr = list1
                        merged = curr
                        list1= list1.next
                    else:
                        curr.next = list1
                        curr = list1
                        list1 = list1.next


            elif list2:
                if not curr:
                    curr = list2
                    merged = curr
                    list2= list2.next
                else:
                    curr.next = list2
                    curr = list2
                    list2 = list2.next
                    
                    
            else:
                if not curr:
                    curr = list1
                    merged = curr
                    list1= list1.next
                else:
                    curr.next = list1
                    curr = list1
                    list1 = list1.next

        return merged
            
        