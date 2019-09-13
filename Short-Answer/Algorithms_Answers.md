#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)O(n)  The runtime will be a linear runtime which gets longer as n gets larger.


b)O(n/2) since j is being doubled each time the runtime will be half of n.


c)

## Exercise II

binary search would be most applicable for this problem.
The goal would be to keep splitting the search in 2.  So split n in half and drop egg.  If egg breaks then you know its the bottom half and if the egg doesn't break its the top half.  With the  half that is remaining you will again split it in half.  you keep doing this until you find the highest floor at which the egg doesn't break.
  function find_floor(n):
    

O(nlogn) - As n grows the runtime does not increase much.

