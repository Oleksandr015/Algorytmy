"""
CLINIC REGISTRATION

Testujemy obie klasy!

"""

if __name__ == '__main__':
    registration = Registration()
    doctor = Doctor(registration.priority_queue)

    obi_wan = Patient('Obi Wan', 'flu')  # 3
    anakin = Patient('Anakin Skywalker', 'heart attack')  # 1
    yoda = Patient('Yoda', 'fracture')  # 2
    general_grievous = Patient('General Grievous', 'stabbed')  # 1

    registration.register(obi_wan)
    registration.register(anakin)
    registration.register(yoda)
    registration.register(general_grievous)

    print(registration.get_estimated_waiting_time(obi_wan))
    print(registration.get_estimated_waiting_time(anakin))
    print(registration.get_estimated_waiting_time(yoda))
    print(registration.get_estimated_waiting_time(general_grievous))

    doctor.admit_patient()
    doctor.admit_patient()
    doctor.admit_patient()
    doctor.admit_patient()
    doctor.admit_patient()
