#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Print the first 5 positive integers in ascending order with one number in each line
                                                                        


# In[2]:


for i in range(0,6):
    print(i)


# In[3]:


#Print the following pattern
"""
*
**
***
****
*****"""
#There are no spaces between consecutive stars. There are no spaces at the end of each line.


# In[4]:


#solution
for i in range(6):
    for j in range(i+1):
        print("*",end="")
    print("\n")    


# In[5]:


#Accept an integer as input and print its square as output.


# In[7]:


n = int(input("Enter the number you want to print square:"))
print(n**2)


# In[ ]:


#Accept two integers as input and print their sum as output.


# In[10]:


a = int(input("enter the first number"))
b = int(input("Enter the second number"))
sum = a + b
print("Two number Sum is",sum)


# In[ ]:


#Accept two words as input and print the two words after adding a space between them


# In[18]:


word_one = input("Enter the First Word:") 
word_Two = input("Enter the second word:")
word = word_one + " "  + word_Two
print(word)


#or
print(input(),input())


# In[ ]:


#Accept the registration number of a vehicle as input and print its state-code as output.


# In[19]:


s = input()
print(s[0:2])


# In[ ]:


#Accept a five-digit number as input and print the sum of its digits as output.


# In[21]:


d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
d5 = int(input())
sum = d1+d2+d3+d4+d5
print(sum)


# In[ ]:


#Accept five words as input and print the sentence formed by these words after adding a space between consecutive words and a full stop at the end.


# In[22]:


word = input()
word2 = input()
word3 = input()
word4 = input()
word5 = input()
sentence = word+" "+word2+" "+word3+" "+word4+" "+word5+". "
print(sentence)


# In[ ]:


#Accept the date in DD-MM-YYYY format as input and print the year as output.


# In[25]:


date = input()
year = date[-4:]
print(year)


# In[ ]:




