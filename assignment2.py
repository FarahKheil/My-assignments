attempts = 3
username = 'admin'
password = 1234

while attempts > 0:
   user_input1 = str(input("enter your username : "))
   user_input2 = str(input("enter your password : "))
   if user_input1 ==str ('admin') and user_input2 == str(1234):
   
        N=int(input ('enter  N: '))
        print("prime numbers from 2 to N:")
        for num in range (2, N+1):
              is_prime = True
              for d in range (2, num):
               if num % d == 0:
                 is_prime = False
                 break
              if is_prime:
                 print(num, end=' ') 
              
        print()
        break
   else:
      attempts -=1
else:
   print('account locked')