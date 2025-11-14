import hashlib

def hashed_password(password):
    # Convert the password to bytes, hash it using SHA-256, and return the hash as a readable hexadecimal string
    return hashlib.sha256(password.encode()).hexdigest()

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
        
        #admin login
        self.admin_username = "admin"
        self.admin_password = hashed_password("admin123") #value passes to method hashed_password for encyption
        
        #employee login
        self.employee_username = "employee"
        self.employee_password = hashed_password("employee123")
        
         
    def add_employee(self, emp_id , name , gender , post , email):
        emp = Employee(emp_id, name, gender, post, email)
        self.employees.append(emp)
        print(f"\n✅ Successfully added the details of {name}.\n")
        
    def view_employee(self):
        if not self.employees:
            print("❌ No employees found.\n")
            
        for emp in self.employees:
            print(emp)
            
    def add_task(self, task_id, task_title, assigned_to, deadline, emp_id):
        employee = next((e for e in self.employees if e.emp_id == emp_id), None) #loops through employee and filters emp_id
        if not self.employees:
            print("❌ Employees not found.\n")
            
        task = Task(task_id, assigned_to, task_title, deadline)
        self.tasks.append(task)
        print("\n✅ Tasks added successfully.\n")
        
        
    def view_task(self, task_id, task_title, assigned_to, deadline, emp_id):
        if not self.tasks:
            print("❌ No tasks added yet.\n")
            
        for task in self.tasks:
            print(task)
            
            
    def view_tasks_of_employee(self, name):
        found = False
        for task in self.tasks:
            if task.assigned_to == name:
               print(task)
               found = True
    
        if not found:
            print("❌ No tasks assigned to you.\n")
            
    def login(self):
        print("\n-----Login required-----\n")
        username = input("Enter username : ")
        password = input("Enter password : ")
        hashed = hashed_password(password)
        
        if username == self.admin_username and hashed == self.admin_password:
            print("✅ Admin login successful.\n")
            return "admin"
        
        elif username == self.employee_username and hashed == self.employee_password:
            print("✅ Employee login successful.\n")
            return "employee"
        else :
            print("❌ Invalid username and password.\n")
            return None
    
    
                 
if __name__ == "__main__":
    
    systemOfEmp = Office_mgmt_sys()
    role = systemOfEmp.login() 
    
    if role is None:
        exit()
        
        #full access to admin
    if role == "admin":
        print("\n-----Admin choices-----\n")
        print("1. Add employee details.")
        print("2. View employee details.")
        print("3. Add employee tasks.")
        print("4. View employee tasks.")
        print("5. Exit.\n")
        
        
        while True:
            choice = int(input("Enter your choice : "))
                
            if choice == 1:
                emp_id = input("Enter employee's id : ")
                name = input("Enter employee's name : ")
                gender = input("Enter employee's gender : ")
                post = input("Enter employee's post : ")
                email = input("Enter employee's email : ")
               
                systemOfEmp.add_employee(emp_id, name, gender, post, email)
                    
            elif choice == 2:
                print("\n-----Details of employee-----")
                systemOfEmp.view_employee()
                    
            elif choice == 3:
                task_id = input("Enter employee's task id : ")
                task_title = input("Enter the task : ")
                assigned_to = input("Enter the name of employee to whom task is assigned : ")
                deadline = input("Enter the deadline(YYYY-MM-DD) : ")
               
                systemOfEmp.add_task(task_id, task_title, assigned_to, deadline, assigned_to)
                    
            elif choice == 4:
                print("\n-----Task details-----")
                systemOfEmp.view_task(task_id, task_title, assigned_to, deadline, emp_id)
                    
            elif choice == 5:
                print("\n👋 Exited from menu.")
                break
                    
            else:
                print("\n⚠️Invalid choice.")
                
            
    
    elif role == "employee":
        print("\n ------Employee choices------\n")
        print("1. View employee details.")
        print("2. View employee tasks.")
        print("3. Exit.\n")
        
        while True:
            choice = int(input("Enter your choice : "))
            
            if choice == 1:
                print("\n-----Your details-----\n")
                systemOfEmp.view_employee()
                
            elif choice == 2:
                print("\n-----Your tasks details-----")
                systemOfEmp.view_tasks_of_employee(systemOfEmp.employee_username) #shows task related to username
                
            elif choice == 3:
                print("\n👋 Exited from menu.")
                break
            
            else:
                print("\n⚠️Invalid choice.")