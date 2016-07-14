#coding=utf-8



# print ['asap', 3]
# print list("word"), 
# print [['list'], ['of', 'lists']]
# print list(('a', 1)) 
#  
# a = ['heterogeneous', 3]
# print a[1] + 5 

# a = [1,2,3,5,'a']
# print a[0]
# print a[4]
# s ="1235a"
# print s[0]
# print a[:3]
# print a[:-1]
# print a[::2]
# print a[::-1]
# print a[::-3]
# print a[0:4:2]
# print len(a)
# print max(a),min(a)

# sort
# a = [1,7,3,8,5]
# a.pop()
# print a
# a.append(6)
# print a
# a.sort()
# print a
# a.reverse()
# print a
# a.sort(reverse=True)
# print a


# 
# hello =  list('hello world')
# print hello
# 'h' in hello
# 'u' in hello
# if 'h' in hello:
#     print 'hello'
#      
# a = [1,2,3,4,5]
# b = a
# print 'a: ',a
# print 'b: ',b
# a.append(6)
# print 'a: ',a
# print 'b: ',b

# 
# 
# a = [1,2,3,4,5]
# import copy
# b = copy.deepcopy(a)
# a.append(7)
# print 'a: ',a
# print 'b: ',b
 
# 
# 
nums = [1,2,3,4]
squares = []
# 方法一(語法較好理解)
for n in nums:
    square = n*n
    squares.append(square)
print squares
# 方法二
squares = [n*3*n+5 for n in nums]
print squares

# 
# 
# nums = [2, 8, 1, 6]
# small = [ n for n in nums if n <= 2 ]  ## [2, 1]
# print small
# 
# small = []
# for n in nums:
#     if n <=2:
#         small.append(n)
# print small
# 
# 
# 
# fruits = ['apple', 'cherry', 'bannana', 'lemon']
# afruits = [ s.upper() for s in fruits if 'a' in s ]
# print afruits
# 
# afruits = []
# for s in fruits:
#     if 'a' in s:
#         afruits.append(s.upper())
# print afruits
# 


