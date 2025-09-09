class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        know = deque([(1, 1)])
        share = deque([])
        knownum, sharenum =  1, 0 # start with first person knowing
        for i in range(2, n + 1):
            if know and know[0][0] == i - delay: # check if the day in know array is ready to share after delay
                knownum -= know[0][1]
                sharenum += know[0][1]
                share.append(know[0])
                know.popleft() # push know tuple to share
            if share and share[0][0] == i - forget:
                sharenum -= share[0][1]
                share.popleft() # pop share num after forget
            if share:
                knownum += sharenum
                know.append((i, sharenum))
        return (knownum + sharenum) % (10 ** 9 + 7)

            
