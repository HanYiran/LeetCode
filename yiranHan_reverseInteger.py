# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

#
# import sys
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#
#         if (x).bit_length() <= 32:
#             整数字节长度问题 详见
#             xlis = list(str(x))
#             if xlis[0] == '-':
#                 newXList = ['-',]
#                 newXList1 = xlis[:0:-1]
#                 for i in range(0,len(newXList1)):
#                     newXList.append(newXList1[i])
#                 newX = int(''.join(newXList))
#                 return newX
#             else:
#                 newXList = xlis[::-1]
#                 newX = int(''.join(newXList))
#
#                 return newX
#         else:
#             return 0
#
# num = Solution()
# print(num.reverse(1534236469))


# def reverse(x):
#     s = cmp(int(x), 0)
#     r = int(s*x[::-1])
#     return s*r * (r < 2**31)
#
# print(reverse('123'))
import operator

def reverse(x):
	s = operator.ge(x, 0)
	i = int(str(x)[:0:-1])
	return i*s *(i<2**31)

print(reverse(-124))