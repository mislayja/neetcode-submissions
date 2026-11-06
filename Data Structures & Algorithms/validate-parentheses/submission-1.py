# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for char in s:
#             if char in ('(','{','['):
#                 stack.append(char)
#             else:
#                 if len(stack) ==0:
#                     return False
#                 popped = stack.pop()
#                 if not(ord(popped) == ord(char)-1 or ord(popped) == ord(char)-2): return False

#                 # it seems like there are other
        
#         return len(stack)==0

class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        pstack = []
        


        for i in s: 
            if i not in closeToOpen:
                pstack.append(i)
            elif pstack and closeToOpen[i] == pstack[-1]:
                pstack.pop()
            else:
                return False
        return len(pstack) == 0

                

        
