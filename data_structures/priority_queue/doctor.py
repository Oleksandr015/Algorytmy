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


class Doctor:
    pass
