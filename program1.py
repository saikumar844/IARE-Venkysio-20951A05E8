#string reversal of large text
s = "Virat Kohli is an Indian international cricketer and former captain of the Indian national team who plays as a right-handed batsman for Royal Challengers Bangalore in the IPL and for Delhi in Indian domestic cricket"
reverse_s = s[::-1]
print(reverse_s)

#string reversal
s = "sai kumar"
reverse_s = s[::-1]
print(reverse_s)

#time complexity
import time
start=time.time()
n=input()
print(n[::-1])
end=time.time()
print(end-start)
