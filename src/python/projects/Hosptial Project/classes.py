class Person:
    """Base class for all people in the hospital."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_info(self):
        """View basic information about the person."""
        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    """Class for hospital patients, inheriting from Person."""
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self):
        """View patient record."""
        return f"Patient Record: {self.medical_record}"


class Staff(Person):
    """Class for hospital staff, inheriting from Person."""
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        """View staff information."""
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"


class Hospital:
    """Class for managing hospital operations."""
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []  # List to hold departments

    def add_department(self, department):
        """Add a department to the hospital."""
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")


class Department:
    """Class representing a department in the hospital."""
    def __init__(self, name):
        self.name = name
        self.patients = []  # List to hold patients
        self.staff = []     # List to hold staff

    def add_patient(self, patient):
        """Add a patient to the department."""
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member):
        """Add staff member to the department."""
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")


# Example Usage
if __name__ == "__main__":
    # Create a hospital
    hospital = Hospital("City Hospital", "123 Main St")

    # Create a department
    cardiology = Department("Cardiology")
    hospital.add_department(cardiology)

    # Create a patient
    patient1 = Patient("Alice", 30, "No known allergies")
    cardiology.add_patient(patient1)

    # Create a staff member
    doctor1 = Staff("Dr. Smith", 45, "Cardiologist")
    cardiology.add_staff(doctor1)

    # View patient and staff records
    print(patient1.view_record())
    print(doctor1.view_info())
