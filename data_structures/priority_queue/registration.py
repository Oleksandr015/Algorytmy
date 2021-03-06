"""
CLINIC REGISTRATION

W tym zadaniu zasymulujemy klinikę/oddział SOR do którego zgłaszają się kolejni pacjenci. Wykorzystamy tutaj kolejkę
priorytetową (PriorityQueue). Pacjenci zgłaszają się do przychodni, nadawany jest priorytet ich przypadkowi na podstawie
trzech list priorytetów: LOW_PRIORITY, MEDIUM_PRIORITY oraz HIGH_PRIORITY. Naszym zadaniem w tym pliku jest napisanie
logiki rejestracji.

SPECYFIKACJA:
*   w konstruktorze TWORZONA jest pusta kolejka priorytetowa priority_queue (powinna być publiczna lub powinna
    wystawiać getter @property)
*   metoda register(patient: Patient):
    *   dodaje pacjenta do kolejki priorytetowej nadając mu priorytet na podstawie trzec list priorytetów.
    *   jeżeli pacjent przyjdzie z dolegliwościami, które nie są zawarte w listach priorytetów, program rzuca wyjątek
        NotImplementedError('Unknown case').
    *   do kolejki priorytetowej dodajemy elementy za pomocą metody put(<tuple>)
**  metoda get_estimated_waiting_time(waiting_patient: Patient):
    *   zwraca oszacowany czas oczekiwania pacjenta na wizytę lekarska, gdzie każdy z priorytetów ma określony czas
        wizyty. Powiązanie priorytet - czas przedstawia słownik _PRIORITY_TIME_MAPPER (należy z niego skorzsytać).
    *   aby dostać się do kolejności z jaką będą wykonywane wizyty należy użyć atrybutu kolejki priorytetowej 'queue'
        zwracającego kolejkę pacjentów o type Deque. Wtedy można iterować po pacjentach wraz z priorytetami np. w pętli
        for, co jest zalecane do tego rozwiązania

WSKAZÓWKI:
*   klasa pacjenta Patient jest juz zaimplementowana


NASTĘPNY KROK -> Implementacja klasy Doctor
"""

from queue import PriorityQueue

from data_structures.priority_queue.patient import Patient

HIGH_PRIORITY = [
    'heart attack',
    'stabbed',
    'fall from height'
]

MEDIUM_PRIORITY = [
    'fracture',
    'serious headache',
    'dehydration'
]

LOW_PRIORITY = [
    'dizziness',
    'flu',
    'high blood pressure'
]


class Registration:
    _PRIORITY_TIME_MAPPER = {
        1: 30,
        2: 15,
        3: 5
    }
