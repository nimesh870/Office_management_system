class Employee:
    def __init__(self , emp_id, name, post, gender , email):
        self.emp_id = emp_id
        self.name = name
        self.post = post
        self.gender = gender
        self.email = email
        
    def __str__(self):
        return f"({self.emp_id}) {self.name}  {self.gender} -> {self.post}  {self.email}"
    
class Task:
    def __init__(self, task_id, assigned_to, task_title, deadline, task_status = "pending"):
        self.task_id = task_id
        self.assigned_to = assigned_to
        self.task_title = task_title
        self.deadline = deadline
        self.task_status = task_status
        
    def __str__(self):
        return f"({self.task_id})  {self.assigned_to} ->{self.task_status} task -> {self.task_title}"    
    
class Office_mgmt_sys:
    def __init__(self):
        self.employees = []
        self.tasks= []
         
    def add_employee(self, emp_id , name , gender , post , email):
        emp = Employee(emp_id, name, gender, post, email)
        self.employees.append(emp)
        print(f"✅ Successfully added the details of {name}.")
        
    def view_employee(self):
        if not self.employees:
            print("❌ No employees found.")
            
        for emp in self.employees:
            print(emp)
            
    def add_task(self, task_id, task_title, assigned_to, deadline, emp_id):
        employee = next((e for e in self.employees if e.emp_id == emp_id), None) #loops through employee and filters emp_id
        if not self.employees:
            print("❌ Employees not found.")
            
        task = Task(task_id, assigned_to, task_title, deadline)
        self.tasks.append(task)
        print("✅ Tasks added successfully.")
        
        
    def view_task(self, task_id, task_title, assigned_to, deadline, emp_id):
        if not self.tasks:
            print("❌ No tasks added yet.")
            
        for task in self.tasks:
            print(task)
            
            
if __name__ == "__main__":
    
    systemOfEmp = Office_mgmt_sys()
    
    print("\n ------Your choices------")
    print("1. Add employee details.")
    print("2. View employee details.")
    print("3. Add employee tasks.")
    print("4. View employee tasks.")
    print("5. Exit.")
    
    while True:
    
        choice = int(input("Enter your choice : "))
        
        if choice == 1:
            emp_id = input("Enter employee's ID : ") # remaining for validation
            name = input("Enter employee's name : ")
            gender = input("Enter employee's gender : ")
            post = input("Enter employee's position : ")
            email = input("Enter employee's email : ") # remaining validation of email, will do this later
            
            systemOfEmp.add_employee(emp_id, name, gender, post, email)
            
            
        elif choice == 2:
            systemOfEmp.view_employee()
            
        elif choice == 3:
            task_id = input("Enter the task ID : ")
            task_title = input("Enter the title of task : ")
            assigned_to = input("Enter the name of employee to whom task is assigned : ")
            deadline = input("Enter the deadline of task(YYYY-MM--DD) : ") # remaining to validate, will do this later
            
            
            systemOfEmp.add_task(task_id, task_title, assigned_to, deadline, emp_id)    
            
        elif choice == 4:
            systemOfEmp.view_task(task_id, task_title, assigned_to, deadline, emp_id)
            
        elif choice == 5:
            print("👋 Exited successfully.")
            break
            
        else:
            print("⚠️ Enter valid choice.")
        
    # will continue later    