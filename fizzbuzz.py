def fizz_buzz(x):
  
   #Step1: check for divisibility by both 3 and 5
    if x%3 == 0 and x%5 == 0:
        return("FizzBuzz")
  
  #Step2: check for divisibility by 3
    elif x%3 == 0:
        return("Fizz")
        
  #Step3: check for divisibility by 5
    elif x%5 == 0:
        return("Buzz")

    else:
        return (x)

fizz_buzz(3)
fizz_buzz(33)
fizz_buzz(5)
fizz_buzz(25)
fizz_buzz(15)
fizz_buzz(105)
fizz_buzz(101)
fizz_buzz(8)

