# email domain address typo, need to figure out and return correct domain name.
# e.g. yhaoo--> yahoo, giaml --> gmail, hmailot--> hotmail.
class Solution(object):
    def emailDomainCorrect(self, email, domainList):
        originDomain = email[email.find('@')+1:email.find('.')]
        dic = {}
        for domain in domainList:
            key = str(sorted(domain))
            dic[key] = domain

        correctDomain = dic[str(sorted(originDomain))]
        return email[:email.find('@')+1] + correctDomain + email[email.find('.'):]


solution = Solution()
domainList = ['yahoo', 'gmail', 'hotmail']
email = 'zhuoli@haoyo.com'
email = 'zhuoli@mailg.com'
print solution.emailDomainCorrect(email, domainList)
