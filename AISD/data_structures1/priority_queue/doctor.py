"""
CLINIC REGISTRATION

Doktor przyjmuje kolejnych pacjentów, informuje o tym, że właśnie kogoś leczy. Korzysta z tej samej kolejki
priorytetowej co klasa Registration.

SPECYFIKACJA:
*   konstruktor przyjmuje kolejkę priorytetową (tą samą z które korzysta obiekt klasy Registration), która jest
    zapisywana do prywatnego atrubytu _patient_queue
*   metoda admit_patient():
    *   metoda symuluje przeprowadzenie wizyty lekarskiej
    *   w celu pobrania następnego pacjenta należy skorzystać z metody get_nowait(), która pobiera z listy
        priorytetowej bez oczekiwania
    *   w przypadku leczenia należy wyświetlić komunikat 'Treating {patient.name } of {patient.ailment}'
    *   jeżeli kolejka jest pusta wyświetlamy 'Nobody to treat', warto użyć metody empty()

NASTĘPNY KROK -> Połączenie rozwiązań w pliku clinic.py
"""

from queue import PriorityQueue

from AISD.data_structures1.priority_queue.patient import Patient


class Doctor:
    def __init__(self, priority_queue: PriorityQueue):
        self._priority_queue = PriorityQueue()


    def admit_patient(self):

        if self._priority_queue.empty():
            print('Nobody to treat')
        else:
            _, patient = self._priority_queue.get_nowait()
            print(f'Treating {patient.name} of {patient.ailment}')

if __name__ == '__main__':
    patient_queue = PriorityQueue()
    patient_queue.put((1, Patient('Jack', 'heard attack')))

    doctor = Doctor(patient_queue)
    doctor.admit_patient()
    doctor.admit_patient()
