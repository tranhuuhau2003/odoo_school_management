# 🎓 School Management

## 🧾 Overview

The **School Management** module is a comprehensive system designed to streamline all aspects of managing an educational institution within the Odoo framework. It provides tools for administrators, teachers, parents, and accountants to collaboratively manage students, classes, attendance, exams, fees, and more.

---

## 🚀 Features

- **Classroom Management**: Create and manage school classrooms with assigned teachers.
- **Student Management**: Maintain student records with personal information and unique IDs.
- **Parent Management**: Link parents/guardians with students and track contact details.
- **Subject Management**: Define and manage academic subjects.
- **Timetable Scheduling**: Generate and view class schedules by week and period.
- **Attendance Tracking**: Record daily attendance with status and reporting.
- **Exam Results**: Enter, view, and calculate student grades.
- **Fee Management**: Track school fee payments and statuses.

---

## 🏗️ Main Models

| Model                 | Description                                |
|----------------------|--------------------------------------------|
| `school.class`       | Stores classroom info, assigned teacher    |
| `student.student`    | Manages student data                       |
| `student.parent`     | Manages parent/guardian information        |
| `school.subject`     | List of academic subjects                  |
| `school.timetable`   | Weekly class schedules                     |
| `school.attendance`  | Daily attendance for students              |
| `school.exam.result` | Student exam results per subject           |
| `school.fee`         | Fee assignments and payment tracking       |

---

## 🧑‍💻 User Roles

- **Administrator**: Full access to configure and manage the entire system.
- **Teacher**: Can manage their classes, take attendance, and input exam results.
- **Parent**: Can view their child’s academic performance and fee information.
- **Accountant**: Handles fee structures and payment tracking.

---

## 📐 Functional Requirements

### 1. Student Management (`student.student`)
- CRUD operations for students.
- Auto-generate unique student ID.
- Fields: name, gender, DOB, status, admission date, photo, etc.
- Link each student to one class and one parent.
- Searchable by name, class, and status.

### 2. Parent Management (`student.parent`)
- CRUD for parent profiles.
- Fields: name, phone, email, occupation, address.
- View all children linked to one parent.

### 3. Classroom Management (`school.class`)
- CRUD for class info.
- Assign one homeroom teacher per class.
- View list of students per class.

### 4. Subject Management (`school.subject`)
- CRUD for school subjects.
- Fields: subject name, subject code.

### 5. Timetable (`school.timetable`)
- Weekly schedule view by class.
- Show subject, teacher, time slot per day.

### 6. Attendance (`school.attendance`)
- Teachers mark daily attendance.
- Record student, date, status (present/absent/late).
- Parents can view attendance history.
- Exportable reports by class/student/date range.

### 7. Exam Results (`school.exam.result`)
- Input exam scores per subject per student.
- Track test type (quiz, midterm, final).
- Calculate average score.
- Parents view report cards.

### 8. Fee Management (`school.fee`)
- Create and assign fees per student.
- Track status (paid/unpaid).
- Parents view detailed fee history.

---

## 🔗 Data Relationships

- One parent → many students (`One2many`)
- One class → many students (`One2many`)
- One student → one class (`Many2one`)
- One student → one parent (`Many2one`)
- One class → one homeroom teacher (`Many2one → res.users`)

---

## 🔐 Non-Functional Requirements

- **Security**: Role-based access (e.g., parents see only their child’s data).
- **Usability**: Intuitive interface, localized to Vietnamese.
- **Performance**: Smooth with large datasets (students, results, records).

---

## 🛠️ Installation
2. Activate virtual environment and run Odoo:
   ```bash
psql -U odoo -d postgres
   cd /opt/odoo/odoo
   ./odoo-bin -c /opt/odoo/odoo/odoo.conf
   ```

3. Update module and restart Odoo with specific DB:
   ```bash
   ./odoo-bin -c /opt/odoo/odoo/odoo.conf -d odoo_db -u school_management
   ```

4. Check if Odoo is running:
   ```bash
   ps aux | grep odoo
   ```


1. Clone this repository:
   ```bash
   git clone https://github.com/tranhuuhau2003/odoo_school_management.git


## Author

- **Tran Huu Hau**
