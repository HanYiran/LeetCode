def reverse(x):
    s = cmp(x, 0)
    print(s)
    i = int(str(x)[::-1])
    print(i)
    return i*s * (i < 2**31)
#
# print(reverse(-214748364787))
# import  operator
# def reverse(x):
# 	print(operator.lt(x, 0))
#
# 	print(int(str(x)[:0:-1]))
# 	# return i*s *(i<2**31)
#
print(reverse(-124))
# def reverse(x):
# 	s = 1 if x>=0 else -1
# 	i = int(str(x)[:0:-1])
# 	return i*s *(i<2**31)
#
# print(reverse(-124))