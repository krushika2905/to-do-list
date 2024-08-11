class Task:
    def _init_(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def _str_(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"
class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def _str_(self):
        if not self.tasks:
            return "No tasks in the list."
        task_list = [f"{i + 1}. {task}" for i, task in enumerate(self.tasks)]
        return "\n".join(task_list)
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Complete Task")
    print("4. View Tasks")
    print("5. Exit")

def get_user_choice():
    return input("Enter your choice: ")
def add_task(to_do_list):
    description = input("Enter task description: ")
    task = Task(description)
    to_do_list.add_task(task)

def remove_task(to_do_list):
    index = int(input("Enter task number to remove: ")) - 1
    to_do_list.remove_task(index)

def complete_task(to_do_list):
    index = int(input("Enter task number to complete: ")) - 1
    to_do_list.complete_task(index)

def view_tasks(to_do_list):
    print("\nTo-Do List:")
    print(to_do_list)
def main():
    to_do_list = ToDoList()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            add_task(to_do_list)
        elif choice == '2':
            remove_task(to_do_list)
        elif choice == '3':
            complete_task(to_do_list)
        elif choice == '4':
            view_tasks(to_do_list)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()