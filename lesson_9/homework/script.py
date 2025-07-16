# # Homework:

# # # Object-Oriented Programming (OOP) Exercises

# # ## 1. Circle Class
# # Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * (self.radius ** 2)

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# # Example usage:
# circle = Circle(5)
# print("Area:", circle.area())
# print("Perimeter:", circle.perimeter())


# # ## 2. Person Class
# # Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

# from datetime import datetime

# class Person:
#     def __init__(self, name, country, birthdate):
#         self.name = name
#         self.country = country
#         self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

#     def get_age(self):
#         today = datetime.today()
#         return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

# # Test
# p = Person("Ali", "Uzbekistan", "2000-05-15")
# print(f"{p.name} is {p.get_age()} years old.")


# # ## 3. Calculator Class
# # Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         return a / b if b != 0 else "Cannot divide by zero"

# # Test
# calc = Calculator()
# print(calc.add(10, 5))
# print(calc.subtract(10, 5))
# print(calc.multiply(10, 5))
# print(calc.divide(10, 0))


# # ## 4. Shape and Subclasses
# # Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

# import math

# class Shape:
#     def area(self):
#         return 0

#     def perimeter(self):
#         return 0

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.radius

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

#     def perimeter(self):
#         return 4 * self.side

# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def perimeter(self):
#         return self.a + self.b + self.c

#     def area(self):
#         s = self.perimeter() / 2
#         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# # Test
# shapes = [Circle(3), Square(4), Triangle(3, 4, 5)]
# for shape in shapes:
#     print("Area:", shape.area())
#     print("Perimeter:", shape.perimeter())


# # ## 5. Binary Search Tree Class
# # Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, key):
#         self.root = self._insert(self.root, key)

#     def _insert(self, node, key):
#         if not node:
#             return Node(key)
#         if key < node.key:
#             node.left = self._insert(node.left, key)
#         else:
#             node.right = self._insert(node.right, key)
#         return node

#     def search(self, key):
#         return self._search(self.root, key)

#     def _search(self, node, key):
#         if not node:
#             return False
#         if key == node.key:
#             return True
#         elif key < node.key:
#             return self._search(node.left, key)
#         else:
#             return self._search(node.right, key)

# # Test
# tree = BST()
# tree.insert(10)
# tree.insert(5)
# tree.insert(15)
# print(tree.search(15))  # True
# print(tree.search(7))   # False


# # ## 6. Stack Data Structure
# # Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop() if not self.is_empty() else "Stack is empty"

#     def is_empty(self):
#         return len(self.items) == 0

# # Test
# s = Stack()
# s.push(1)
# s.push(2)
# print(s.pop())  # 2
# print(s.pop())  # 1
# print(s.pop())  # Stack is empty


# # ## 7. Linked List Data Structure
# # Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=' -> ')
#             current = current.next
#         print("None")

#     def insert(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def delete(self, key):
#         current = self.head
#         prev = None
#         while current and current.data != key:
#             prev = current
#             current = current.next
#         if not current:
#             return
#         if prev:
#             prev.next = current.next
#         else:
#             self.head = current.next

# # Test
# ll = LinkedList()
# ll.insert(10)
# ll.insert(20)
# ll.insert(30)
# ll.display()
# ll.delete(20)
# ll.display()


# # ## 8. Shopping Cart Class
# # Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

# class ShoppingCart:
#     def __init__(self):
#         self.items = {}

#     def add_item(self, name, price):
#         self.items[name] = self.items.get(name, 0) + price

#     def remove_item(self, name):
#         if name in self.items:
#             del self.items[name]

#     def total_price(self):
#         return sum(self.items.values())

# # Test
# cart = ShoppingCart()
# cart.add_item("Book", 20)
# cart.add_item("Pen", 5)
# print("Total:", cart.total_price())
# cart.remove_item("Pen")
# print("Total after removal:", cart.total_price())


# # ## 9. Stack with Display
# # Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, val):
#         self.stack.append(val)

#     def pop(self):
#         return self.stack.pop() if self.stack else "Empty Stack"

#     def display(self):
#         print("Stack:", self.stack)

# # Test
# s = Stack()
# s.push(1)
# s.push(2)
# s.display()
# s.pop()
# s.display()


# # ## 10. Queue Data Structure
# # Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, val):
#         self.queue.append(val)

#     def dequeue(self):
#         return self.queue.pop(0) if self.queue else "Empty Queue"

# # Test
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# print(q.dequeue())
# print(q.dequeue())
# print(q.dequeue())


# # ## 11. Bank Class
# # Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

# class Account:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} deposited. New balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#             print(f"{amount} withdrawn. New balance: {self.balance}")

# class Bank:
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self, name):
#         self.accounts[name] = Account(name)

#     def get_account(self, name):
#         return self.accounts.get(name)

# # Test
# bank = Bank()
# bank.create_account("Alice")
# acc = bank.get_account("Alice")
# acc.deposit(100)
# acc.withdraw(30)
# acc.withdraw(100)
