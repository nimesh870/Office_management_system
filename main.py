import hashlib
from email_validator import validate_email, EmailNotValidError
import json
import os
from datetime import datetime


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
        self.email = self.validate_employee_email(email)
        
        #checking validity of email
    def validate_employee_email(self, email) :
        try:
            #checks the syntax of email and also checks if the email exists or not
            valid = validate_email(email, check_deliverability = False)
            return valid.email #returns email if it is valid
        
        except EmailNotValidError as e:
            raise ValueError("\n⚠️ Invalid Email entered. Ex: user@gmail.com") from e
        
              
    def __str__(self):
        return f"({self.emp_id}) {self.name}  {self.gender} -> {self.post}  {self.email}\n"
    
class Task:
    def __init__(self, task_id, assigned_to, task_title, deadline, task_status = "pending"):
        self.task_id = task_id
        self.assigned_to = assigned_to
        self.task_title = task_title
        self.deadline = deadline
        self.task_status = task_status
        
    def __str__(self):
        return f"({self.task_id})  {self.assigned_to} ->{self.task_status}, task -> {self.task_title}\n"   
     
    
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
        if gender.lower() not in ["male" , "female"]:
            print("\n❌ Invalid gender entered.\n")
            return
        
        emp = Employee(emp_id, name, gender, post, email)
        self.employees.append(emp)
        print(f"\n✅ Successfully added the details of {name}.\n")
            
        
    def view_employee(self):
        if not self.employees:
            print("❌ No employees found.\n")
            return
            
        for emp in self.employees:
            print(emp)
            
    def add_task(self, task_id, task_title, assigned_to, deadline):
        employee = next((e for e in self.employees if e.emp_id == emp_id), None) #loops through employee and filters emp_id
        if not self.employees:
            print("❌ Employees not found. Add employees first.\n")
            return
            
        task = Task(task_id, assigned_to, task_title, deadline)
        self.tasks.append(task)
        print("\n✅ Tasks added successfully.\n")
        
        
    def view_task(self):
        if not self.tasks:
            print("❌ No tasks added yet.\n")
            return
            
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
            
    def delete_emp(self):
        emp_id = input("Enter employee's ID : ")
        
        employee = next((e for e in self.employees if e.emp_id == emp_id), None)
        
        if not employee :
            print("\n❌ Employees not found.\n")
            return
        
        confirm = input(f"Are you sure want to delete {employee.name} as employee (y/n) : ")
        if confirm.lower() != 'y':
            print("\n❌ Deletion canceled.\n")
            return # exits safely
        
        self.employees = [e for e in self.employees if e.emp_id != emp_id] #deleting employees using list comprehension
        self.tasks = [t for t in self.tasks if t.assigned_to != employee.name]
        
        print("\n✅ Deletion of employee and related task successful.\n")
        
            
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
        
        
    def save_data(self):
            data = {
                
                "employees" : [
                    {
                        "emp_id" : emp.emp_id,
                        "name" : emp.name,
                        "gender" : emp.gender,
                        "post" : emp.post,
                        "email" : emp.email,
                    }
                    for emp in self.employees
                ],
                
                "tasks" :
                    [
                        {
                            "task_id" : tsk.task_id,
                            "task_title" : tsk.task_title,
                            "assigned_to" : tsk.assigned_to,
                            "deadline" : tsk.deadline,
                            "task_status" : tsk.task_status
                        }
                        for tsk in self.tasks
                    ]
            }  
            
            with open("file.json" , "w") as fp:
                json.dump(data, fp, indent = 4)
                
            print("\n🗃️ Sucessfully saved data.\n")
        
        
    def load_data(self):
        try :
            
            filename = "file.json"
            if not os.path.exists(filename) or os.stat(filename).st_size == 0:
                # File does not exist or is empty
               return {"employees": [], "tasks": []}
           
            with open("file.json", "r") as fp:
                data = json.load(fp)
             
            #load employees   
            self.employees = [
                
                #creates python object of each employee
                Employee (
                    emp["emp_id"], #keys in the dictionary
                    emp["name"],
                    emp["gender"],
                    emp["post"],
                    emp["email"]
                )
                for emp in data.get("employees", []) # get employees from data
            ]
            
            #load tasks
            self.tasks = [
                
                Task(
                    tsk["task_id"],
                    tsk["assigned_to"],
                    tsk["task_title"],
                    tsk["deadline"],
                    tsk["task_status"]
                    
                )
                for tsk in data.get("tasks" , []) # get tasks from data
            ]
            
            print("\n📂 Data loaded successfully.\n")
            
        except FileNotFoundError as f:
            print("\n⚠️ No data are saved yet.\n", str(f))
            
            
def validate_date(date_str):
    try:
        #reads the datetime string
        entered_date = datetime.strptime(date_str, "%Y-%m-%d")

        #get today's date (without time)
        today = datetime.now().date()

        #reject past dates
        if entered_date.date() < today:
            return False

        return True
    
    except ValueError:
        return False
    
def validate_emp_id(emp_id):
    return emp_id.startswith("EMP") and len(emp_id) > 3

def validate_task_id(task_id):
    return task_id.startswith("TSK") and len(task_id) > 3


    
if __name__ == "__main__":
    
    systemOfEmp = Office_mgmt_sys()
    systemOfEmp.load_data()
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
        print("5. Delete employee.")
        print("6. Exit.\n")
        
        
        while True:
            choice = int(input("Enter your choice : "))
                
            if choice == 1:
                emp_id = input("\nEnter employee's id : ")
                name = input("Enter employee's name : ")
                gender = input("Enter employee's gender : ")
                post = input("Enter employee's post : ")
                email = input("Enter employee's email : ")
                
                if not validate_emp_id(emp_id):
                    print("\n❌ Invalid employee ID.\n")
                    continue
               
                systemOfEmp.add_employee(emp_id, name, gender, post, email)
                    
            elif choice == 2:
                print("\n-----Details of employee-----\n")
                systemOfEmp.view_employee()
                    
            elif choice == 3:
                task_id = input("\nEnter employee's task id : ")
                task_title = input("Enter the task : ")
                assigned_to = input("Enter the name of employee to whom task is assigned : ")
                deadline = input("Enter the deadline(YYYY-MM-DD) : ")
                
                if not validate_date(deadline):
                    print("\n❌ Invalid or past date entered.\n")
                    continue
                    
                    
                elif not validate_task_id(task_id):
                    print("\n❌ Incorrect task ID.\n")
                    continue
               
                systemOfEmp.add_task(task_id, task_title, assigned_to, deadline)
                    
            elif choice == 4:
                print("\n-----Task details-----\n")
                systemOfEmp.view_task()
                
            elif choice == 5:
                systemOfEmp.delete_emp()

                
            elif choice == 6:
                systemOfEmp.save_data()
                print("\n👋 Exited from menu.")
                break
                    
            else:
                print("\n⚠️ Invalid choice.")
                
            
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
                name = input("\nEnter your name : ")
                print("\n-----Your tasks details-----\n")
                systemOfEmp.view_tasks_of_employee(name) #shows task related to user's name
                
            elif choice == 3:
                # systemOfEmp.save_data()
                print("\n👋 Exited from menu.")
                break
            
            else:
                print("\n⚠️ Invalid choice.")