blocks = int(input("Enter the number of blocks: "))
height = 0

while blocks:
   height += 1
   blocks -= height
   if blocks <= height:
      break 

print("The height of the pyramid:", height)