def SubsetSum(set, n, sum) :
   # Base Cases
   if (sum == 0) :
      return True
   if (n == 0 and sum != 0) :
      return False
   # ignore if last element is > sum
   if (set[n - 1] > sum) :
      return SubsetSum(set, n - 1, sum);
   # else,we check the sum
   # (1) including the last element
   # (2) excluding the last element
   return SubsetSum(set, n-1, sum) or SubsetSum(set, n-1, sumset[n-1])






for i in range(int(input())):
    items, m = list(map(int, input().split()))
    vals = list(map(int, input().split()))
    
    if (SubsetSum(vals, len(vals), m) == True) :
        print(f"Case #{i+1}:{2}")
    else :
        print(f"Case #{i+1}:{0}")
