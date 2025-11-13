class Employee:
    def __init__(self , emp_id, name, post, gender , email):
        
        self.emp_id = emp_id
        self.name = name
        self.post = post
        self.gender = gender
        self.email = email
        
    def __str__(self):
        return f"({self.emp_id}) {self.name}  {self.gender} -> {self.post}  {self.email}"
    
    def task(self, task_id, assigned_to, deadline, task_status = "pending"):
        self.task_id = task_id
        self.assigned_to = assigned_to
        self.deadline = deadline
        self.task_status = task_status
        
    def __str__(self):
        return f"({self.task_id})  {self.assigned_to} -> {self.task_status}"    
    
class Office_mgmt_sys:
    def __init__(self):
        self.employees = []
        self.task = []
         
    def add_employee(self):
        emp_id = len(self.employees) + 1 # increaments by 1 when new employee is added
        emp = Employee(emp_id, self.name, self.gender, self.post, self.email)
        self.employees.append(emp)
        print(f"✅ Successfully added the details of {self.name}.")
        
    def view_employee(self):
        if not self.employee:
            print("❌ No employees found.")
            
        for emp in self.employees:
            print(emp)
            
            
    def add_task(self):
        pass