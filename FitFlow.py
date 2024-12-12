members_list = []
memberships_list = []
trainers_list = []

generate_membership_id = 101
generate_trainer_id = 1

class Members:
    def __init__(self, name, membership_id, age, contact, password):
        self.name = name
        self.membership_id = membership_id
        self.age = age
        self.contact = contact
        self.password = password

    def __str__(self):
        return f"===========================Member Details==========================\nName: {self.name} | ID: {self.membership_id}) | Age: {self.age} | Contact: {self.contact} | Password: {self.password}"

class Membership:
    def __init__(self, membership_id, type_name, duration, fee, trainer=None):
        self.membership_id = membership_id
        self.type_name = type_name
        self.duration = duration
        self.fee = fee
        self.paid = False 
        self.trainer = trainer

    def details(self):
        trainer_info = f"Trainer: {self.trainer.name}" if self.trainer else ""
        payment_status = "Paid" if self.paid else "Not Paid"
        return f"=======Details=======\nType: {self.type_name}, \nDuration: {self.duration} months, \nFee: ${self.fee}, \nPayment Status: {payment_status}\n{trainer_info}"

class Trainer:
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact
        self.assigned_member = None

    def __str__(self):
        assigned_info = f"Assigned to: {self.assigned_member.name}" if self.assigned_member else "Not assigned"
        return f"{self.name} ({self.age}), Contact: {self.contact}, {assigned_info}"

trainers_list = [
    Trainer("John Doe", 35, "0912-345-6789"),
    Trainer("Jane Smith", 29, "0998-765-4321"),
    Trainer("Alex Brown", 40, "0913-579-2468")
]

def get_input(prompt, input_type=str):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def add_member():
    global generate_membership_id
    name = input("Enter your username: ")
    membership_id = generate_membership_id
    generate_membership_id += 1
    age = get_input("Enter your age: ", int)
    contact = input("Enter your contact number: ")
    password = input("Enter your password: ")

    member = Members(name, membership_id, age, contact, password)
    members_list.append(member)
    print(f"Member registered.\nYour Membership ID is: {membership_id}")
    login()

def add_membership(member):
    print("======Gym Membership Subscription======")
    type_name = input("Enter Membership Type (Basic/Premium): ").lower()
    duration = get_input("Enter Membership Duration (in months): ", int)
    fee = 50 * duration if type_name == "basic" else 100 * duration
    trainer = None

    if type_name == "premium":
        trainer = select_trainer()

    membership = Membership(member.membership_id, type_name.capitalize(), duration, fee, trainer)
    memberships_list.append(membership)
    print(f"Membership added for {member.name}.\n{membership.details()}")

def add_trainer():
    global generate_trainer_id
    name = input("Enter trainer's name: ")
    age = get_input("Enter trainer's age: ", int)
    contact = input("Enter trainer's contact number: ")

    trainer = Trainer(name, age, contact)
    trainers_list.append(trainer)
    generate_trainer_id += 1
    print(f"Trainer {name} added successfully!")

def select_trainer():
    if not trainers_list:
        print("No trainers available.")
        return None

    print("\nAvailable Trainers:")
    for i, trainer in enumerate(trainers_list, 1):
        print(f"{i}. {trainer}")

    choice = get_input("Select a trainer by number: ", int) - 1
    return trainers_list[choice] if 0 <= choice < len(trainers_list) else None

def process_payment(membership):
    if membership.paid:
        print(f"Membership {membership.membership_id} is already paid.")
        return

    print(f"Payment required: ${membership.fee}")
    payment = get_input("Enter payment amount: $", float)

    if payment >= membership.fee:
        membership.paid = True
        print(f"Payment of ₱{payment} accepted. Membership is now paid.")
    else:
        print("Insufficient payment. Please try again.")

def cancel_membership(member):
    membership = next((m for m in memberships_list if m.membership_id == member.membership_id), None)
    
    if membership:
        memberships_list.remove(membership)
        print(f"Membership for {member.name} (ID: {member.membership_id}) has been canceled.")
        if membership.trainer:
            membership.trainer.assigned_member = None
            print(f"Trainer {membership.trainer.name} has been unassigned from the member.")
    else:
        print("No active membership found to cancel.")

def admin_menu():
    while True:
        print("\n============Admin Menu==============")
        print("\t1. View Members")
        print("\t2. View Memberships")
        print("\t3. Add Trainer")
        print("\t4. View Trainers")
        print("\t5. Terminate Membership")
        print("\t6. Process Payment")
        print("\t7. Log out")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            for member in members_list:
                print(member)
        elif choice == "2":
            for membership in memberships_list:
                print(membership.details())
        elif choice == "3":
            add_trainer()
        elif choice == "4":
            for trainer in trainers_list:
                print(trainer)
        elif choice == "5":
            membership_id = get_input("Enter Membership ID to terminate: ", int)
            membership = next((m for m in memberships_list if m.membership_id == membership_id), None)
            if membership and not membership.paid:
                memberships_list.remove(membership)
                print(f"Membership {membership_id} terminated due to non-payment.")
        elif choice == "6":
            membership_id = get_input("Enter Membership ID to process payment: ", int)
            membership = next((m for m in memberships_list if m.membership_id == membership_id), None)
            if membership:
                process_payment(membership)
            else:
                print("Membership not found.")
        elif choice == "7":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def user_menu(member):
    if not member: 
        print("Invalid member! Please try again.")
        return

    while True:
        print(f"\n============User Menu for {member.name}============")
        print("\t1. View Membership Details")
        print("\t2. Gym Membership Subscription")
        print("\t3. Process Payment")
        print("\t4. Cancel Membership")  
        print("\t5. Log Out")
        print("============================================")

        choice = input("Enter your choice: ")

        membership = next((m for m in memberships_list if m.membership_id == member.membership_id), None)
        if choice == "1" and membership:
            print(membership.details())
        elif choice == "2":
            add_membership(member)
        elif choice == "3":
            process_payment(membership)
        elif choice == "4" and membership:
            cancel_membership(member) 
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def login():
    print("================FitFlow==================\n==========Gym Management System==========\n\tLogin as:\n\t1. Admin\n\t2. User\n\t3. Register New Member")
    print("=========================================")
    choice = input("Enter your choice: ")

    if choice == "1":
        return "admin"
    elif choice == "2":
        membership_id = get_input("Enter Membership ID: ", int)
        member = next((m for m in members_list if m.membership_id == membership_id), None)

        if member:
            password = input("Enter your password: ")
            if password == member.password:
                return "user", member
            else:
                print("Incorrect password.")
                return None
        else:
            print("Member not found.")
            return None
    elif choice == "3":
        add_member()
        return "", members_list[-1]
    else:
        print("Invalid choice.")
        return None

while True:
    user_role = login()
    if user_role == "admin":
        admin_menu()
    elif user_role and user_role[1]:  
        user_menu(user_role[1])  
    else:
        print("Access denied.")
        break
