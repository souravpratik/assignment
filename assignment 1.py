#!/usr/bin/env python
# coding: utf-8

# # assignment 1 
# (solutions)
# 
# 
QUESTION 1:

VALUES: hello, -87.8 , 6
expression: * , - , / , +QUESTION 2:

          STRING:   It is a value that represents text. Basically, it is a data type for sequence of characters that includes
                    numbers, spaces, punctuation, and even line breaks.
                    Strings can't be used for calculation.
                    It is just a type of variable.
          
          VARIABLE: It is a name that refers to any value,
                    its value can be altered as per our requirement.
                    Variables can be of several types as-
                    integer, floating point, string, boolean.
                     
QUESTION 3:
            Three different data types in python-
            [1] NUMERIC  type
            [2] SEQUENCE type
            [3] BOOLEAN type
            
            [1] NUMERIC TYPE:
                              In Python, numeric data type represent the data which has numeric value. Numeric value can be                                   integer, floating number or even complex numbers. These values are defined as int, float and                                   complex class in Python.

(i) Integers –        This value is represented by int class. It contains positive or negative whole numbers (without fraction                        or decimal). In Python there is no limit to how long an integer value can be.

(ii) Float –           This value is represented by float class. It is a real number with floating point representation. It is                         specified by a decimal point. Optionally, the character e or E followed by a positive or negative                              integer may be appended to specify scientific notation.

(iii)Complex Numbers – Complex number is represented by complex class. It is specified as (real part) + (imaginary part)j.                            For example – 2+3j
               
               
               [2] SEQUENCE TYPE:
                                  In Python, sequence is the ordered collection of similar or different data types. Sequences                     allows to store multiple values in an organized and efficient fashion. There are several sequence types in                     Python – 
 
 (i) STRING:      In Python, Strings are arrays of bytes representing Unicode characters. A string is a collection of one or                     more characters put in a single quote, double-quote or triple quote. In python there is no character data                       type, a character is a string of length one. It is represented by str class.
                  Strings in Python can be created using single quotes or double quotes or even triple quotes.
 
 (ii) LIST:       Lists are just like the arrays, declared in other languages which is a ordered collection of data. It is very                   flexible as the items in a list do not need to be of the same type.
                  Lists in Python can be created by just placing the sequence inside the square brackets[].
 
 (iii) TUPLE:     Just like list, tuple is also an ordered collection of Python objects. The only difference between tuple and                   list is that tuples are immutable i.e. tuples cannot be modified after it is created. It is represented by                     tuple class.
                  
                  In Python, tuples are created by placing a sequence of values separated by ‘comma’ with or without the use of                   parentheses for grouping of the data sequence. Tuples can contain any number of elements and of any datatype                   (like strings, integers, list, etc.).

Note: Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple.


                [3] BOOLEAN TYPE:
                                  Data type with one of the two built-in values, True or False. Boolean objects that are equal                     to True are truthy (true), and those equal to False are falsy (false). But non-Boolean objects can be                           evaluated in Boolean context as well and determined to be true or false. It is denoted by the class bool.

                    Note – True and False with capital ‘T’ and ‘F’ are valid booleans otherwise python will throw an error.
                                 
            QUESTION 4:
           
           In python, an expression is any legal combination of symbols (like a variable, constants, and operators) representing a value. An expression must have at least one operand (variable or constant) and have one or more operators. After evaluating an expression, we get a value.
           
           Expressions are used to evaluate the values or represent the result on the screen.QUESTION 5:
           Expression is made up of variables,constants & operators
           Statement is a set of text as command to print by interpreter.
           
           
# In[1]:


##Question 6:

bacon=22
bacon+1


# In[2]:


##Question 7:

'spam'+'spamspam'


# In[3]:


'spam'*3

QUESTION 8:
              As we can't assingn a variable name initiating with an integer although we can assign a variable name with integer but intiating with a letter of alphabet is mandatory, post letter we can assign integer as per our requirement.
              for example: s100 or egg100QUESTION 9:
                for integer               : int()
                for string                : str()
                for floating point number : float()
# In[4]:


##QUESTION 10:

'I have eaten'+ 99 +'burritos'


# In[5]:


'I have eaten'+str('99')+'burritos' 
## we will covert integer into string data type sing string can't be added with numerical type.


# In[ ]:




