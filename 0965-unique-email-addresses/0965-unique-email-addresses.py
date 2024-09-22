class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            local = email.split("@")[0]
            domain = email.split("@")[1]
            newLocal = ""
            for char in local:
                if char == '.':
                    newLocal += ""
                elif char == "+":
                    break
                else:
                    newLocal += char
            newLocal += "@" + domain
            if not newLocal in res:
                res.add(newLocal)
        return len(res)