
class FizzBuzz:

    def fizzbuzz(self, number):
        
        answer = ""
        
        if (number % 15 == 0):
            answer = "FizzBuzz"
        
        elif number % 5 == 0:
            answer = "Buzz"
            
        elif number % 3 == 0:
            answer =  "Fizz"
        
        else:
            answer = str(number)
            
        return(answer)
        
    
    
