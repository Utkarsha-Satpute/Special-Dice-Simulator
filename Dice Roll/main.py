import random
while True:
     user_input = input("do you want to roll the dice?")
     a = random.randint(1, 9)
     if user_input == 'yes':
         if a > 6:
             print(6)
         else:
             print(a)
     elif user_input == 'no':
         break
print("thanks for using\ncode by utkarsha")