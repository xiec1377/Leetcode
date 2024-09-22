class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        locals = set()

        for email in emails:
            local = email.split("@")[0]
            domain = email.split("@")[1]
            print("local:", local)
            newLocal = ""
            for char in local:
                if char == '.':
                    newLocal += ""
                elif char == "+":
                    break
                else:
                    newLocal += char
        
                    
            newLocal += "@" + domain
            if not newLocal in locals:
                locals.add(newLocal)

        return len(locals)