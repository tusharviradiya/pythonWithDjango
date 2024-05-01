# str
# str is class
# str is iterable
# str is mutable
# str is hashtable
# str is a sequence

# how to create str
s1 = "hello"
s2 = 'tushar'
s3 = """tushar"""
s4 = '''tushar'''
s5 = str(343)
s6 = str([1, 2, 3, 4, 5])

# build in method for str
# len(), min(), max(), sum(), sorted()
# sorted always return list

# concatenation
s7 = s1 + s2
print(s7)
s8 = s1*3

# methods in str
s9 = "tushar viradya"
x = s9.index('t')
print(x)

#formate
s10 = "my name is {1} and i am {0} year old".format("tushar", 21)
print(s10)

# split
s11 = "tushar viradya"
s12 = s11.split()
print(s12)

# join
s13 = ["tushar", "viradya"]
s14 = " ".join(s13)
print(s14)

# slicing operator
s15 = "tushar"
s15[0:3:1]
print(s15)

# tuple
# tuple is class
# tuple is iterable
# tuple is immutable
# tuple element is indexed
# tuple is sequence
t1 = (1, 2, 3, 4, 5)
t2 = ()
t3 = (1,)
t4 = 10, 20, 30, 40, 50
# sorted
s1 = [1, 6, 2, 78, 9, 0]
s2 = sorted(s1, reverse=True)
print(s2)
#build in method in tuple
# index()
# count()
print(t4[1:3:1])