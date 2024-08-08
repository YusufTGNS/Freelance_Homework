# Information about gamers
Hi. We are building a platform for online gaming and we need help to store, process, use information about our gamers. This year, we'll give you a few tasks to implement; this here is the first of them.  Don't forget to look at the README.md file every time - in it, you will find detailed requirements and tips!

## TASK 1. Refinement of the Gamer class and implementation of the tool for adding user data
We have already created the Gamer class. It will allow us to process the following information about users: their name, age and favourite games. This information will be displayed as a neat little presentation, allowing the gamer to make new friends! However, there is a problem - we forgot to add fields for the user's gamer tag  and email... Can you help our team with this task? If so, here are the task checklist and some hints!


### Checklist TASK 1
 - [ ] Improve the Gamer class - add the **nickname** and **email** fields
 - [ ] Adjust the message of the mini-presentation to include the new data
 - [ ] Test the code with the **Pytest test** we prepared to make sure that the code meets our request!

## About tests

### Pytest testing
We wrote tests that automatically checks code for compliance:
-   `test_Task_1_name_and_age_check`: We check that the "Gamer" class still has the "name" and "age" attributes.
-   `test_Task_2_add_nickname`: Check that the "nickname" attribute was added to the "Gamer" class.
-   `test_Task_3_add_email`: ПCheck that the "email" attribute was added to the "Gamer" class.
-   `test_Task_4_change_message`: Tests the output of information for the gamer's mini-presentation.

## Tips

### Python classes

#### 1. Defining a class:
```python
class ClassName:
    def __init__(self, paramters):
        # Конструктор класса
        self.field1 = value1
        self.field2 = value2
        # ...

    def method(self, parameters):
        # Defining the method
        # ...

# Example:
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.имя} and I am {self.возраст} years old.")
```
#### 2. Creating instances of classes:
```python
# Сlass instance creation
object = ClassName(arguments)

# Example:
cat = Animal("Melvin", 3)
```
#### 3. Adding fields to a class:
```python
# Adding new fields to a class
yourObject.newField = value

# Example:
cat.colour = "orange"
```
#### 4. Using a class in a project:
```python
# Using methods and fields of a class
yourObject.method(arguments) 
value = yourObject.field

# Example:
cat.introduce()
print(cat.colour)
```