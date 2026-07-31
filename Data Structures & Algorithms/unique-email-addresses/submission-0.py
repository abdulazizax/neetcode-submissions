class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for email in emails:
            validEmail = ""
            i = 0

            while email[i] != '@':
                if email[i] == '+':
                    break
                if email[i] != '.':
                    validEmail += email[i]
                i += 1

            while email[i] != '@':
                i += 1

            validEmail += email[i + 1:]
            res.add(validEmail)

        return len(res)