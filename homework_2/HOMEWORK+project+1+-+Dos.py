
# coding: utf-8

# <img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">
# 
# # Project 1: Python Coding Exercises
# 
# _Authors: Joseph Nelson (DC) _
# 
# ---

# The following code challenges are drawn from common exercises used in technical interviews.
# 
# Note that there may be several ways to approach each challenge!

# ### Challenge 1: Largest Palindrome
# A palindromic number reads the same both ways. For example, 1234321 is a palindrome. The largest palindrome made from the product of two two-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two three-digit numbers.

# In[14]:


def drange(yo):
    
    for x in range(999, 0, -1): 
        for y in range (999,0,-1): 
            pal = str(x*y)
            pal_rev = reverse_string(pal)

            if test(pal, pal_rev) == True:
                pal_list.append(pal)
#PAL_LIST = X*Y APPENDS TO LIST
    return pal_list

def reverse_string(hi): 
    reversed = ""
    for a in range(len(hi)-1, -1, -1): 
        reversed += hi[a]
    return reversed

#Takes last letter and appending to reverse
# += Concatinate for string
# a = index number - last letter of string for the first time

def test(string1, string2):
    if string1 == string2: 
        return True
    else: 
        return False
    
def palindrome_max(glist):
    pal_max = 0
    for g in range(len(glist)):
        if int(glist[g]) > pal_max: 
            pal_max = int(pal_list[g])
    return(pal_max)

pal_list = []
drange(pal_list)

# print(pal_list)
print(palindrome_max(pal_list))
# a = item in list
# for g in range len glist = list of all palindromes


# 
# ### Challenge 2: Summation of Primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below 2,000.

# In[ ]:


def prime(n):
    if n < 2: 
        return False
    elif n <=3: 
        return True
    elif n % 2 == 0: 
        return False
    
for x in range(3, n//2, 2): 
    if n%x == 0: 
        return Flase
    return True

def primes(x):
    return sum(n for n in l if )

##PRACTICE DO NOT USE


# In[46]:


max = 2000

def prime(x):
    for y in range(2,x//2):
        if x%y == 0: 
            return False
#         print(x,y)
           
        return True

equal = 0 
count = 0 
num = 2 

while count != max:
    count += 1
    if prime(num):
        equal += num
    num += 1
    
print(equal)
## TEST - DO NOT USE


# In[1]:


def is_prime(n):
    if n < 2:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    
    
    length = n//2
    
    
    for i in range(3, length, 2):
        if n % i == 0:
            return False
    return True


def sum_primes(l):
    return sum(n for n in l if is_prime(n))



sum_primes(range(2000))


# ### Challenge 3: Multiples of 3 and 5
# If we list all of the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 and 5 below 1,000.

# In[4]:


sum([x for x in range (1000) if x %3 == 0 and x %5 ==0])


# In[ ]:


# 2 ways to do the formula


# In[3]:


max = 1000
result = 0 

for x in range(0,max):
    if x %3 ==0 and x % 5 == 0:
        result += x 
print (result)


# ### Challenge 4: String Compressor
# Implement a method to perform basic string compression using the counts of repeated characters. (This is called run-length encoding.) For example, the string "aabcccccaaa" would become a2b1c5a3. If the “compressed” string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a–z). Specify whether your solution is case sensitive or case insensitive and what you would need to change to make it the other.

# In[35]:


from itertools import groupby


# In[44]:





# # Bonus Challenge: FizzBuzz Extreme
# Find or develop three different solutions to the following problem, in Python, that are as different from one another as possible. Which one do you prefer? Why? In what ways are the alternative solutions better?
# 
# Write a program that prints all of the numbers from 1 to 100. For multiples of 3, instead of the number, print "Fizz;" for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz."

# In[5]:


for num in range(1,101):
    if num %3 == 0 and num %5 == 0:
        print("i love fizzbuzz")
    elif num %3 == 0:
        print ("fizz")
    elif num %5 == 0: 
        print ("buzz")
    else: 
        print (num)

