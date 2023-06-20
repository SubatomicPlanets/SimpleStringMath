# StrToMath
This is a very simple example on how to evaluate a mathematical expression from a string.  
Currently only + - * / ^ % are possible. I will add more in the future.  
If there are any issues, please let me know. I did not have a lot of time for testing.  

# Examples:
- "what's fifty three+7*6/2?" ->  74  
- "what is 9 * 67+90?"         ->  693  
- "2^7"                        ->  128  
- "tell me what pi - 23 * (((((-6) + (2 / (65.4 - one hundred and fourteen))) + 20) - ((5 * 3) * two)) - (0.5 / 0.9)) is."  ->  384.865871835391  
- "-pi+pi"                     ->  0  
- "-pi*two"                    ->  -6.283184
- "(twenty two*2)+one"         ->  45

# How to use
1. you can just read the code, if it interests you.  
2. you can use it as a library by downloading it, importing it in other files, and running the "evaluate" function.  
3. you can download the file and modify it.  
   - add this code to the bottom of the file to make it run when you start it:  
     ```
     while True:
         print(evaluate(input("You: ")))
     ```
