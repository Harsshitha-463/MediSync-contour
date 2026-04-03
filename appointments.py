class Appointment:
    def __init__(self, patient_name, doctor_name, date, time, location):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.time = time
        self.location = location


# Sample usage  
if __name__ == "__main__":  
    appointment1 = Appointment("John Doe", "Smith", "2024-07-15", "10:30 AM", "New York", "NY")  
    print(appointment1.schedule())
