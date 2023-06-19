# Information
This is a very simple example on how to evaluate a mathematical expression from a string.  
Currently only + - * / ^ are possible. I will add more in the future.  
If there are any issues, please let me know. I did not have a lot of time for testing.  

# Examples:
"what's 53+7*6/2 ?"  ->  74  
"what is 9 * 67+90?" ->  693  
"2^7"                ->  128  

# How to use
1. you can just read the code, if it interests you.  
2. you can use it as a library by downloading it, importing it in other files, and running the "evaluate" function.  
3. you can download the file and modify it.  
   - add this code to the bottom of the file to make it run when you start it:  
     ```
     while True:
         print(evaluate(input("You: ")))
     ```
