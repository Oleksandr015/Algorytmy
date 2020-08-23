"""
USER AUTHENTICATION SERVICE

Naszym zadaniem jest napisanie serwisu przeprowadzającego autentykację logujących sie użytkowników. Serwis posiada bufor
kolejkujący użytkowników w kolejności logowania. Bufor implementowany jest przy uzyciu stworzonej przez nas kolejki.
Serwis pobiera kolejnych użytkowników z kolejki, sprawdza czy znajdują sie w zamokowanej bazie danych (MOCKED_DATABASE)
oraz przeprowadza autentykację.

SPECYFIKACJA:
*   parametrem konstruktora jest stworzona już kolejka 'queues' zawierająca użytkowników chcących się zalogować.
    Kolejka przechowuje dane w postaci krotki loginu oraz hasła. Np. ('Majster', '123qweASD')
*   serwis posiada metoda authenticate, która przeprowadza calą autentykację
*   metoda pobiera kolejnych użytkowników z kolejki. W przyapdku wystąpienia wyjątku EmptyQueueException metoda
    zwraca wiadomość 'No user to authenticate!'.
*   metoda sprawdza czy w bazie danych (naszym mocku) istnieje użytkownik z danym loginem. Warto posłużyć się metodą
    słownika get(), która zwraca None w przypadku gdy nie znaleziono elementu o podanych kluczu. Gdy użytkownik nie
    istnieje metoda zwraca wiadomość 'No user with nick: {request_nick}'
*   metoda sprawdza czy podane hasło jest poprawne. Jeżeli hasło złe zwraca 'Wrong password', w przeciwnym wypadku
    '{request_nick} logged in'

Zaimplementowany serwis przetestować (nie trzeba assert, wystarczy po prostu wyświetlać wyniki)
"""
from typing import Dict

MOCKED_DATABASE: Dict[str, str] = {
    'Majster': '123qweASD',
    'Cziter': 'admin1',
    'powaznyUzytkownik': 'mojepowaznehaslo123',
}


class UserAuthenticationService:
    pass


if __name__ == '__main__':
    queue = CustomQueue()
    service = UserAuthenticationService(queue)
