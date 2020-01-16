#!/usr/bin/env python
# coding: utf-8

# In[1]:


from turtle import *

def snowflake(side, level):
    if level == 0: 
        forward(side) 
        return
    side /= 3.0
    snowflake(side, level-1) 
    left(60) 
    snowflake(side, level-1) 
    right(120) 
    snowflake(side, level-1) 
    left(60) 
    snowflake(side, level-1) 
  
if __name__ == "__main__": 
    
    speed(10)                    
    length = 300.0   
         
    penup()                      
  
    backward(length/2.0) 
         
    pendown()            
    for i in range(3):     
        snowflake(length, 4) 
        right(120) 
  

    mainloop()   


# In[ ]:




