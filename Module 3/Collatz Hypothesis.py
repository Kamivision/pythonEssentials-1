# Scenario
# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:

# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.

# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1. We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.

# Hint: the most important part of the problem is how to transform Collatz's idea into a while loop - this is the key to success.

c0 = int(input("Enter a positive number greater than 0: "))
step = int(0)

while c0 != 1:
    step += 1
    if c0 % 2 == 0:
        c0 //= 2 
    else: c0 = 3 * c0 + 1
    print(c0)

print(f"steps = {step}")