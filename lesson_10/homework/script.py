# # Homework Projects:

# # Homework 1. ToDo List Application

# # Define Task Class:
# # Create a Task class with attributes such as task title, description, due date, and status.
# # Define ToDoList Class:
# # Create a ToDoList class that manages a list of tasks.
# # Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
# # Create Main Program:
# # Develop a simple CLI to interact with the ToDoList.
# # Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
# # Test the Application:
# # Create instances of tasks and test the functionality of your ToDoList.


# from datetime import datetime

# class Task:
#     def __init__(self, title, description, due_date):
#         self.title = title
#         self.description = description
#         self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
#         self.completed = False

#     def mark_complete(self):
#         self.completed = True

#     def __str__(self):
#         status = "✓ Done" if self.completed else "✗ Pending"
#         return f"{self.title} ({status}) - Due: {self.due_date.date()}"


# # Homework 2. Simple Blog System

# # Define Post Class:
# # Create a Post class with attributes like title, content, and author.
# # Define Blog Class:
# # Create a Blog class that manages a list of posts.
# # Include methods to add a post, list all posts, and display posts by a specific author.
# # Create Main Program:
# # Develop a CLI to interact with the Blog system.
# # Include options to add posts, list all posts, and display posts by a specific author.
# # Enhance Blog System:
# # Add functionality to delete a post, edit a post, and display the latest posts.
# # Test the Application:
# # Create instances of posts and test the functionality of your Blog system.


# class ToDoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def mark_task_complete(self, title):
#         for task in self.tasks:
#             if task.title.lower() == title.lower():
#                 task.mark_complete()
#                 print(f"Task '{title}' marked as complete.")
#                 return
#         print(f"Task '{title}' not found.")

#     def list_all_tasks(self):
#         if not self.tasks:
#             print("No tasks found.")
#             return
#         for task in self.tasks:
#             print(task)

#     def list_incomplete_tasks(self):
#         found = False
#         for task in self.tasks:
#             if not task.completed:
#                 print(task)
#                 found = True
#         if not found:
#             print("No incomplete tasks.")


# # Homework 3. Simple Banking System

# # Define Account Class:
# # Create an Account class with attributes like account number, account holder name, and balance.
# # Define Bank Class:
# # Create a Bank class that manages a list of accounts.
# # Include methods to add an account, check balance, deposit money, and withdraw money.
# # Create Main Program:
# # Develop a CLI to interact with the Banking system.
# # Include options to add accounts, check balance, deposit money, and withdraw money.
# # Enhance Banking System:
# # Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
# # Test the Application:
# # Create instances of accounts and test the functionality of your Banking system.

# def main():
#     todo = ToDoList()

#     while True:
#         print("\n--- ToDo List Menu ---")
#         print("1. Add Task")
#         print("2. Mark Task Complete")
#         print("3. List All Tasks")
#         print("4. List Incomplete Tasks")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             title = input("Task Title: ")
#             desc = input("Description: ")
#             due = input("Due Date (YYYY-MM-DD): ")
#             task = Task(title, desc, due)
#             todo.add_task(task)
#             print("Task added.")

#         elif choice == "2":
#             title = input("Enter task title to mark complete: ")
#             todo.mark_task_complete(title)

#         elif choice == "3":
#             print("\n--- All Tasks ---")
#             todo.list_all_tasks()

#         elif choice == "4":
#             print("\n--- Incomplete Tasks ---")
#             todo.list_incomplete_tasks()

#         elif choice == "5":
#             print("Exiting...")
#             break

#         else:
#             print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     main()
