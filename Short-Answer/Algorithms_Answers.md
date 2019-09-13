#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)  The runtime will be a linear runtime which gets longer as n gets larger.


b) O(n/2) since j is being doubled each time the runtime will be half of n.


c) O(n)  Since the recursion will keep repeating and subtracting one at a time the runtime will be linear, dependent on the size of n.

## Exercise II

binary search would be most applicable for this problem.

The goal would be to keep splitting the search in 2.  So split n in half and drop egg.  If egg breaks then you know its the bottom half and if the egg doesn't break its the top half.  With the  half that is remaining you will again split it in half.  you keep doing this until you find the highest floor at which the egg doesn't break.
  function find_floor(n, range):
    top_half = range(n, n - n/2)
    bottom_half = range(0, n - n /2)
    n = n - n/2

    if range == 1:
        return n
    else:
        if egg breaks at n:
            return find_floor(n, bottom_half)
        else if egg doesn't break:
            return find_floor(n, top_half)


O(nlogn) - As n grows the runtime does not increase much.

