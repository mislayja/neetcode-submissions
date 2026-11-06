# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # ok so generic merge case
        # this mentions divide and conquer? Am I really supposed to merge smaller lists into larger one
        # rather than simply do all at once?
        # no, that would be extraneous iterations at each step. 
        temp = ListNode(next=None)
        curr = temp

        exit = False
        while not exit:
            exit = True
            # find a min here, and if our item is last in list we will remove. 
            # do clean up
            m = None
            idx = None
            for i, l in enumerate(lists):
                if l:
                    exit = False
                    if m:
                        if l.val < m.val:
                            m = l
                            idx = i
                    else:
                        m=l
                        idx = i
            
            if not exit:
                lists[idx] = lists[idx].next
                curr.next = m
                curr = m

        return temp.next