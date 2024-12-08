FitFlow: Gym Management System

This project is a simple gym management system.

Table of Contents

[Project Overview 1](#_Toc184514179)

[Python Implementation 1](#_Toc184514180)

[SDG Integration 2](#_Toc184514181)

[How to Use 2](#_Toc184514182)

[Example Usage 2](#_Toc184514183)

### Project Overview

FitFlow is a **Gym Management System** is designed to streamline and automate the administrative tasks of a gym. It enables gym owners to efficiently manage memberships, process payments, and track member information, while offering users easy access to their membership details and trainer interactions. With a user-friendly interface, FitFlow ensures smooth operations for both admins and members, making gym management hassle-free.

Features:

- Member Management
- Membership Management
- Trainer Management
- Payment Management
- Admin Functionality
- User Functionality
- Login System
- Trainer Selection(Premium Members)
- Data Storage and Tracking

### Python Implementation

The system is implemented using **Python**, leveraging core programming concepts and libraries to handle gym management tasks effectively.

- **Data Structures:** The system uses lists to store essential data, such as members, memberships, and trainers. The members_list stores all gym members along with their personal details like name, membership ID, age, and contact information. The memberships_list holds data about each member's membership, including the membership type, duration, fee, and payment status. The trainers_list contains all the available trainers, storing their details such as name, age, contact, and assigned members.
- **Functions:** The program is divided into functions, each handling a specific task to improve modularity and code reusability. There are functions to register new members, assign memberships, and calculate membership fees. Functions also handle the payment processing by verifying and updating the payment status. Additionally, there are functions for managing trainers, including adding new trainers and assigning them to members for premium memberships.
- **Control Flow:** Conditional statements and loops control the flow of the program based on user input. Conditional statements are used to guide the program's behavior, such as determining whether the user is an admin or a member, or what actions are available based on membership status. Loops ensure that the program continues running, presenting menus to the user until they choose to log out, which maintains an interactive and continuous experience.

### SDG Integration

- **Promoting Health and Well-being (SDG 3)**: FitFlow encourages physical activity and fitness by enabling members to track their progress, stay motivated, and achieve their health goals. It supports gyms in promoting healthier lifestyles through memberships, personalized trainer assignments, and performance tracking.
- **Reducing Inequalities (SDG 10)**: FitFlow's user-friendly platform can make fitness services more accessible to a wider range of people by simplifying the registration process, offering diverse membership options (such as basic and premium), and helping gyms serve communities with different needs.
- **Decent Work and Economic Growth (SDG 8)**: By streamlining gym operations, FitFlow can help gym owners reduce administrative costs and focus on expanding their business, potentially leading to job creation for trainers and staff, contributing to local economies.

### How to Use

### Save the Python code in a file (e.g., FitFlow.py) and run it from your terminal using python FitFlow.py

### Example Usage

### For Members

### Register as a Member

### Register as a Member by choosing Option 3

### Logging in as a User

### After the Registration Process. Your Membership ID will appear. Choose Option 2 to start Login In

- **User Menu Window:**

Logging in as a user will take you to the User Menu. In this window you can view your Membership Details, Trainer, and the Duration of your Membership, Gym Membership Subscription, Process Payment, Cancel Membership, and Log Out.

- **Buying Membership:**

Choosing Option 2 will take you to the Gym Subscription Window, in this window you can choose the type of Subscription, Duration of the Subscription, and depends on the Subscription, the Available Trainers.

- **Membership Details:**

After the Subscription, you can now view your Membership Details by choosing Option 1.

- **Process Payment:**

Choosing Option 3 will take you to the payment window.

- **Cancelling Subscription:**

You can also cancel your Subscription.

**For Admins:**

- **Logging in as an Admin:**

Choice Option 1 in the Login as Window.

- **Admin Menu Window:**

Logging in as an Admin will take you to the Admin Window. In the Admin Menu you can view Members, Memberships, add Trainer, View Trainers, Terminate Membership, and Process Payment for Members that couldn’t do it online.

- **View Member/Membership Details:**

Choosing Option 1 will show the Member Details, and 2 will show the Membership Subscription.

- **Adding Trainer:**

Option 3 will take you to the Adding Trainer Window. You will need to put the name, age, contact number of the Trainer you will like to add.

- **View Trainer Details:**

Option 4 will let you view the Trainer’s Information.

- **Termination Membership:**

If the Option is needed you can remove a Members Membership ID.

- **Payment Process:**

For Members that couldn’t pay their Membership Online, there is a separate payment process in the Admin Menu.
