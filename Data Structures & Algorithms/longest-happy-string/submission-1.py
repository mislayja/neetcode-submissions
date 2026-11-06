import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        s = ""
        chars = []
        heapq.heappush_max(chars, (a,"a"))
        heapq.heappush_max(chars, (b,"b"))
        heapq.heappush_max(chars, (c,"c"))

        canAdd=True
        while chars:
            # print(f"chars={chars}, s={s}")
            num, char = heapq.heappop_max(chars)
            # print(f"chars={chars}, s={s},char={char}, last2={s[-2:]}, check={char}{char}")
            
            if num == 0: continue

            # it's >0, lets check it now
            if len(s)>=2:
                if s[-2:]== f"{char}{char}":
                    
                    # check others now
                    try_next_prio,try_next_char = heapq.heappop_max(chars)
                    # print(f"enxtchar={try_next_char}")
                    if try_next_prio==0: return s
                    
                    s+=try_next_char
                    # ok lets add the next prio now
                    heapq.heappush_max(chars, ((try_next_prio-1), try_next_char))
                    heapq.heappush_max(chars, (num,char))
                else:
                    s+=char
                    heapq.heappush_max(chars,((num-1), char))
                
            else:
                # not long enough for repeats, just add 
                s+=char
                heapq.heappush_max(chars, ((num-1), char))



        return s