'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''
'''
python
re \D split
operator
'''
class Solution(object):
    def diffWaysToCompute(self, input):
       tokens = re.split('(\D)', input)
       nums = map(int, tokens[::2])
       ops = map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2])
       def build(lo, hi):
           if lo == hi:
               return [nums[lo]]
           return [ops[i](a, b)
                   for i in xrange(lo, hi)
                   for a in build(lo, i)
                   for b in build(i + 1, hi)]
       return build(0, len(nums) - 1)
