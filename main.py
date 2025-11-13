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
    
    def task(self, task_id, assigned_to, task_title, deadline, task_status = "pending"):
        self.task_id = task_id
        self.assigned_to = assigned_to
        self.task_title = task_title
        self.deadline = deadline
        self.task_status = task_status
        
    def __str__(self):
        return f"({self.task_id})  {self.assigned_to} -> {self.task_status}"    
    
class Office_mgmt_sys:
    def __init__(self):
        self.employees = []
        self.tasks= []
         
    def add_employee(self , name , gender , post , email):
        emp_id = len(self.employees) + 1 # increaments by 1 when new employee is added
        emp = Employee(emp_id, name, gender, post, email)
        self.employees.append(emp)
        print(f"✅ Successfully added the details of {self.name}.")
        
    def view_employee(self):
        if not self.employee:
            print("❌ No employees found.")
            
        for emp in self.employees:
            print(emp)
            
    def add_task(self, task_id, task_title, assigned_to, deadline, emp_id):
        employee = next((e for e in self.employees if e.emp_id == emp_id), None)
        if not self.employees:
            print("❌ Employees not found.")
            
            return 
        task_id = len(self.tasks) + 1
        
        task = Task(task_id, task_title, deadline, employee)
        self.tasks.append(task)
        print("✅ Tasks added successfully.")
        
    def view_task(self):
        if not self.tasks:
            print("❌ NO tasks added yet.")
            
        for task in self.tasks:
            print(task)