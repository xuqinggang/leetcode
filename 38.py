from itertools import groupby

class Solution(object):
    # def countAndSay(self, n):
    #     """
    #     :type n: int
    #     :rtype: str
    #     """
    #     res = '1'
    #     for i in xrange(n-1):
    #         res = ''.join([str(len(list(group))) + digit for digit, group in groupby(res)])
    #     return res

    def countAndSay(self, n):
        curres = '1'
        # 1
        # 11
        # 21
        # 1211
        # 111221
        # 312211
        for i in xrange(n-1):
            newres = ''
            count = 1
            j = 0
            while j < len(curres):
                if j < len(curres) -1 and curres[j] == curres[j+1]:
                    count += 1
                else:
                    newres += (str(count) + curres[j])
                    count = 1
                j += 1
            curres = newres
        # print '\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a\a'
        return curres

            

print Solution().countAndSay(6)


