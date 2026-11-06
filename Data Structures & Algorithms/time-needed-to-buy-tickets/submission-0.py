class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # this looks like we need to access kth person then sum up numbers <=k before and k, after
        total = tickets[k]

        kth = tickets[k]
        for idx, val in enumerate(tickets):
            if idx<k:
                total += min(val,kth)
            elif idx>k:
                total += min(val,kth-1)
        return total