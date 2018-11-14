def getScore(s):
    # calculate Longest Palindromic Subsequence Array
    memoized_result = [[0 for i in range(len(s))] for i in range(len(s))]

    def LPS(s):
        for i in range(len(s)):
            memoized_result[i][i] = 1

        # sl = substring length
        for sl in range(2, len(s)+1):
            for i in range(0, len(s)-sl+1):
                j = i+sl-1
                if s[i] == s[j] and sl==2:
                    memoized_result[i][j]=2
                elif s[i] == s[j]:
                    memoized_result[i][j]=memoized_result[i+1][j-1]+2
                else:
                    memoized_result[i][j]=max(memoized_result[i+1][j], memoized_result[i][j-1])

        return memoized_result[0][len(s)-1]

    LPS(s)
    maximum_product = 0

    for i in range(len(memoized_result)-1):
        value = memoized_result[0][i] * memoized_result[i+1][len(memoized_result)-1]
        maximum_product = max(maximum_product, value)
    
    return maximum_product


def LPS(s):
    def longestPalindromicSubsequenceRecurisive(s, start, end):
        if end - start <= 1:
            return 1
        if end - start == 1 and s[start] == s[end]:
            return 2
        if s[start] == s[end]:
            return longestPalindromicSubsequenceRecurisive(s, start+1, end-1)+2
        else:
            return max(longestPalindromicSubsequenceRecurisive(s, start+1, end), longestPalindromicSubsequenceRecurisive(s, start, end-1))

    return longestPalindromicSubsequenceRecurisive(s, 0, len(s)-1)


def LPSTabulation(s):
    memoized_result = [[0 for i in range(len(s))] for i in range(len(s))]

    for i in range(len(s)):
        memoized_result[i][i] = 1

    # sl = substring length
    for sl in range(2, len(s)+1):
        for i in range(0, len(s)-sl+1):
            j = i+sl-1
            if s[i] == s[j] and sl==2:
                memoized_result[i][j]=2
            elif s[i] == s[j]:
                memoized_result[i][j]=memoized_result[i+1][j-1]+2
            else:
                memoized_result[i][j]=max(memoized_result[i+1][j], memoized_result[i][j-1])

    return memoized_result[0][len(s)-1]
    


def LPSMemoization(s):
    memoized_result = [[None for i in range(len(s))] for i in range(len(s))]

    def longestPalindromicSubsequenceRecurisiveMemoization(s, start, end):
        if memoized_result[start][end] == None:
            result = longestPalindromicSubsequenceRecurisive(s, start, end)
            memoized_result[start][end] = result
            return result
        else:
            return memoized_result[start][end]

    def longestPalindromicSubsequenceRecurisive(s, start, end):
        if end - start <= 1:
            return 1
        if end - start == 1 and s[start] == s[end]:
            return 2
        if s[start] == s[end]:
            return longestPalindromicSubsequenceRecurisiveMemoization(s, start+1, end-1)+2
        else:
            return max(longestPalindromicSubsequenceRecurisiveMemoization(s, start+1, end), longestPalindromicSubsequenceRecurisiveMemoization(s, start, end-1)) 
    
    result = longestPalindromicSubsequenceRecurisiveMemoization(s, 0, len(s)-1)
    return result



#s = "acdapmpompsfdlkljdlfjsoweuroeiuossioazoidaosidoidfuosdifuosifusodfiusodfiusoifuosdisdocuyoxucolsafskdfkasljaekrlskjflkdsjflklwejrlskfdjlskjalkfjalfjelwjlfksjflkaflakjlkwjelrjlkjlcljlalkdfladjlckjlykvcljcvyczvrxczvzrzyzxcvecxvwtvcxwvtyxcwvxctvxcrevytvsdfuszdufisauzewrfbsmnbwmenbqmwemwqernbmwnrbmsnsdbxiuyiuxczitustduadztaisudqwemnwemqwnebmqwenbyxicututassudzsdtaiqwejhqvwejwqhefqwemnwvenqwbvenqwve"
s = "acdapmpomp"
print(getScore(s))
#print(LPSTabulation(s))
#print(LPSMemoization(s))
#print(LPS(s))



