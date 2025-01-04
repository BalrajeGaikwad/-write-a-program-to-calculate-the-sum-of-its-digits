 #write a  program to calculate the sum of its digits

num=int(input("Enter the 5 digit Number :-"))   #12345

d1 = num // 10000            # First digit
print(d1)
d2 = (num // 1000) % 10      # Second digit
print(d2)
d3 = (num // 100) % 10       # Third digit
print(d3)
d4 = (num // 10) % 10        # Fourth digit
print(d4)
d5 = num % 10                # Fifth digit
print(d5)

sum=d1+d2+d3+d4+d5

print(sum)