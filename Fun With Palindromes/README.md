# Fun with Palindromes

Company| Ascend.io
---|---
Date|11/12/2018
Platform|HackerRank

We define the following:
* A _palindrome_ is a sequence of characters which reads the same forward and backwards. For example: _madam_ and _dad_ are palindromes, but _eva_ and _sam_ are not.
* A _subsequence_ is a group of characters chosen from a list while maintaining their order. For instance, the subsequences of _abc_ are _[a,b,c,ab,ac,bc,abc]_
* The score of string s is the maximum product of two non-overlapping palindromic subsequences of _s_ that we_ll refer to as _a_ and _b_. In other words, _score(s) = max(length(a) x length(b))_.

There may be multiple ways to choose _a_ and _b_, but there can't be any overlap between the two subsequences. For example:
```
Index 0123456
    s attract
```
Palindromic subsequences are _[a,t,r,c,t,aa,tt,ata,ara,ttt,trt,tat,tct,atta]_. Many of these subsequences overlap, however (e.g. _atta_ and _tct_) The maximum score is obtained using the subsequence _atta_, |_atta_| = 4 and |c| or |t| = 1, 4 x 1 = 4.

### Function Description
Complete the function _getScore_ in the editor below. The function must return an integer denoting the maximum possible _score_ of _s_.

getScore has the following parameter(s):
    s: a string to process

### Constraints
* 1 < |s| <= 3000
* s[i] is of ascii[a-z]

### Sample Case 0
#### Sample Input 0
```
acdapmpomp
```
#### Sample Output 0
```
15
```
#### Explanation 0
Given s = "acdapmpomp", we can choose a = "aca" and b= "pmpmp" to get a maximal product of score = 3 x 5 = 15.

Java solution from http://qa.geeksforgeeks.org/8994/qa.geeksforgeeks.org/8994/product-lengths-longest-overlapping-palindromic-subsequence.html

```
class Longest{

static int[][] longestPalindromicSubsequence(String seq)
{
       int n = seq.length();
       int i, j, cl;
       int L[][] = new int[n][n];  
      
       
       for (i = 0; i < n; i++)
           L[i][i] = 1;           
        
        for (cl=2; cl<=n; cl++)
        {
            for (i=0; i<n-cl+1; i++)
            {
                j = i+cl-1;
                if (seq.charAt(i) == seq.charAt(j) && cl == 2)
                   L[i][j] = 2;
                else if (seq.charAt(i) == seq.charAt(j))
                   L[i][j] = L[i+1][j-1] + 2;
                else
                   L[i][j] = Math.max(L[i][j-1], L[i+1][j]);
            }
        }
        //System.out.println(L[0][n-1]);
        return L;
}
    static int funPal(String s) 
    {
    int prodMax = -1;
    int resArr[][] = longestPalindromicSubsequence(s);
    for(int i=0; i<s.length()-1;i++)
    {
        int tempProd = resArr[0][i] * resArr[i+1][s.length()-1];
        if(prodMax <= tempProd)
            prodMax = tempProd;
    }
    return prodMax;
}⁠⁠⁠⁠
public static void main(String[] args) {
        Longest l = new Longest(); 
        System.out.println(l.longestProd("axbawbaseksqke"));
        
    }

}
```