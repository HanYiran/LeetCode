# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.

# roman numeral 罗马数字
# 相同的数字连写、所表示的数等于这些数字相加得到的数、如：Ⅲ=3；
# 小的数字在大的数字的右边、所表示的数等于这些数字相加得到的数、 如：Ⅷ=8、Ⅻ=12；
# 小的数字（限于 I、X 和 C）在大的数字的左边、所表示的数等于大数减小数得到的数、如：Ⅳ=4、Ⅸ=9；
# 正常使用时、连写的数字重复不得超过三次；
# 在一个数的上面画一条横线、表示这个数扩大 1000 倍
# 基本数字 Ⅰ、X 、C 中的任何一个、自身连用构成数目、或者放在大数的右边连用构成数目
# 、都不能超过三个；放在大数的左边只能用一个；
# 不能把基本数字 V 、L 、D 中的任何一个作为小数放在大数的左边采用相减的方法构成数目；
# 放在大数的右边采用相加的方式构成数目、只能使用一个；


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
