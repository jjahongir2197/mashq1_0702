class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.records = []

    def add_record(self, record):
        self.records.append(record)


class Doctor:
    def __init__(self, name, specialty, price):
        self.name = name
        self.specialty = specialty
        self.price = price


class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date


class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.cash = 0

    def add_patient(self, p):
        self.patients.append(p)

    def add_doctor(self, d):
        self.doctors.append(d)

    def book(self, p_idx, d_idx, date):
        ap = Appointment(self.patients[p_idx], self.doctors[d_idx], date)
        self.appointments.append(ap)
        self.cash += self.doctors[d_idx].price
        print("Qabul yozildi")

    def report(self):
        print("Daromad:", self.cash)
        for a in self.appointments:
            print(a.patient.name, "→", a.doctor.name, "|", a.date)


hospital = Hospital()
hospital.add_patient(Patient("Ali", 25))
hospital.add_doctor(Doctor("Dr. Karimov", "Terapevt", 80000))
hospital.book(0, 0, "12-02-2026")
hospital.report()
