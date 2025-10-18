class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict = defaultdict(int)
        for char in s1:
            s1dict[char] += 1
        print("s1dict", s1dict)
        tempdict = s1dict.copy()
        start = 0
        end = 0
        while start <= end and end < len(s2):
            print("s2[start]", s2[start])
            print("s2[end", s2[end])
            if s2[end] in s1dict.keys():
                print("we here")
                if tempdict[s2[end]] > 0:
                    tempdict[s2[end]] -= 1
                    end += 1
                    if all(value == 0 for value in tempdict.values()):
                        print("WE GOOD")
                        return True
                else:
                    while start < end and s2[start] != s2[end]:
                        if s2[start] in s1dict:
                            tempdict[s2[start]] += 1
                        start += 1
                    start += 1
                    end += 1
            else:
                tempdict = s1dict.copy()
                print("tempdict:", tempdict)
                start = end + 1
                end = start
        return False

            
        