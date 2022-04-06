#Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

#As the answer can be very large, return it modulo 109 + 7.

#Example 1:

#Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
#Output: 20
#Explanation: 
#Enumerating by the values (arr[i], arr[j], arr[k]):
#(1, 2, 5) occurs 8 times;
#(1, 3, 4) occurs 8 times;
#(2, 2, 4) occurs 2 times;
#(2, 3, 3) occurs 2 times.
#Example 2:

#Input: arr = [1,1,2,2,2,2], target = 5
#Output: 12
#Explanation: 
#arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
#We choose one 1 from [1,1] in 2 ways,
#and two 2s from [2,2,2,2] in 6 ways.

class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        ans = 0
        A.sort()

        for i, x in enumerate(A):
            # We'll try to find the number of i < j < k
            # with A[j] + A[k] == T, where T = target - A[i].

            # The below is a "two sum with multiplicity".
            T = target - A[i]
            j, k = i+1, len(A) - 1

            while j < k:
                # These steps proceed as in a typical two-sum.
                if A[j] + A[k] < T:
                    j += 1
                elif A[j] + A[k] > T:
                    k -= 1
                # These steps differ:
                elif A[j] != A[k]: # We have A[j] + A[k] == T.
                    # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
                    # And similarly for "right".
                    left = right = 1
                    while j + 1 < k and A[j] == A[j+1]:
                        left += 1
                        j += 1
                    while k - 1 > j and A[k] == A[k-1]:
                        right += 1
                        k -= 1

                    # We contributed left * right many pairs.
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1

                else:
                    # M = k - j + 1
                    # We contributed M * (M-1) / 2 pairs.
                    ans += (k-j+1) * (k-j) / 2
                    ans %= MOD
                    break

        return ans

class Solution:
    def threeSumMulti(self, arr, target):
        c = Counter(arr)
        ans, M = 0, 10**9 + 7
        for i, j in permutations(c, 2):
            if i < j < target - i - j:
                ans += c[i]*c[j]*c[target - i - j]

        for i in c:
            if 3*i != target:
                ans += c[i]*(c[i]-1)*c[target - 2*i]//2
            else:
                ans += c[i]*(c[i]-1)*(c[i]-2)//6
                
        return ans % M

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        cnt = Counter(arr)  # obtain the number of instances of each number
        res, i, l = 0, 0, len(arr)
        while i < l:  # in replacement of the for-loop, so that we can increment i by more than 1
            j, k = i, l-1  # j should be the leftmost index, hence j=i instead of j=i+1
            while j < k:  # i <= j < k; arr[i] <= arr[j] <= arr[k]
                if arr[i]+arr[j]+arr[k] < target:
                    j += cnt[arr[j]]
                elif arr[i]+arr[j]+arr[k] > target:
                    k -= cnt[arr[k]]
                else:  # arr[i]+arr[j]+arr[k] == target
                    if arr[i] != arr[j] != arr[k]:  # Case 1: All the numbers are different
                        res += cnt[arr[i]]*cnt[arr[j]]*cnt[arr[k]]
                    elif arr[i] == arr[j] != arr[k]:  # Case 2: The smaller two numbers are the same
                        res += cnt[arr[i]]*(cnt[arr[i]]-1)*cnt[arr[k]]//2  # math.comb(cnt[arr[i]], 2)*cnt[arr[k]]
                    elif arr[i] != arr[j] == arr[k]:  # Case 3: The larger two numbers are the same
                        res += cnt[arr[i]]*cnt[arr[j]]*(cnt[arr[j]]-1)//2  # math.comb(cnt[arr[j]], 2)*cnt[arr[i]]
                    else:  # Case 4: All the numbers are the same
                        res += cnt[arr[i]]*(cnt[arr[i]]-1)*(cnt[arr[i]]-2)//6  # math.comb(cnt[arr[i]], 3)
					# Shift pointers by the number of instances of the number
                    j += cnt[arr[j]]
                    k -= cnt[arr[k]]
            i += cnt[arr[i]]  # Shift pointer by the number of instances of the number
        return res%1000000007