<!-- <style>
mark{
    background:blue;
    color:white;
}
</style> -->

#  <center> Python Essentials 1 </center>
# Modules 1, 2, & 3

## Literals
 
  - Integers (int()) = Whole numbers that can be either positive or negative
  - Floats (float()) = Numbers with decimal
  - Strings (str()) = Words/phrases contained in " "
  - Boolean (bool()) = True or False this literal is case sensitive

## Variables

### Variable Naming

- Should be lowercase and multiple words should be seperated by an underscore
  - <mark> ex. my_variable </mark>
- Function names use same conventions
- Camelcase is allowed if needed for backwards compatibility 
  - <mark> ex. myVariable </mark>

### Creating a Variable

variables are created by using the assignment operator ( = )\
<mark> ex. my_variable = "something"</mark>

## Comments

- Anything after ( # ) is ignored by Python
- Best practice is to comment and explain each piece of important code
- Can be used to turn on and off sections of code you're testing
- To quickly comment or comment blocks of code use keyboard shortcut <strong> ctrl + \ </strong>

## User Interactions

### input() funtion

- Prompts user to input some data 
- Is a string by default but can be converted
- Should contain a message to prompt user


> ex. number = input("Please enter a number: ")\
> 
> ex. number = int(input("Enter a whole number: ")) - with conversion

### print() function

- Displays data for the user
- Accepts any data type
