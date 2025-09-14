from datetime import date, timedelta
from src.address_book import AddressBook, Record, Phone, Name

def test_phone_validation_ok():
    Phone("0123456789")  # should not raise

def test_phone_validation_fail():
    import pytest
    with pytest.raises(ValueError): Phone("12345")
    with pytest.raises(ValueError): Phone("12345678901")
    with pytest.raises(ValueError): Phone("12a4567890")

def test_name_validation():
    import pytest
    with pytest.raises(ValueError): Name("   ")

def test_record_crud_phones():
    r = Record("Alice")
    r.add_phone("1111111111")
    r.add_phone("2222222222")
    assert r.find_phone("1111111111")
    r.edit_phone("1111111111", "3333333333")
    assert r.find_phone("3333333333")
    assert r.remove_phone("2222222222") is True
    assert r.remove_phone("0000000000") is False

def test_address_book_basic_and_str():
    book = AddressBook()
    john = Record("John"); john.add_phone("1234567890")
    book.add_record(john)
    assert book.find("John") is john
    assert "Contact name: John" in str(book)
    assert book.delete("John") is True
    assert book.find("John") is None

def test_birthday_add_and_upcoming_window():
    book = AddressBook()
    r = Record("Bob")
    book.add_record(r)

    # pick a date within the next 7 days (including today)
    today = date.today()
    for offset in range(0, 7):
        candidate = today + timedelta(days=offset)
        bday_str = candidate.strftime("%d.%m.") + "1990"  # arbitrary year
        r.add_birthday(bday_str)
        upcoming = book.get_upcoming_birthdays(days=7)
        if upcoming:
            # expect there is an entry for Bob
            item = next((x for x in upcoming if x["name"] == "Bob"), None)
            if item:
                # greeting date is either the same day or shifted to Monday
                greet = candidate
                if greet.weekday() == 5:       # Saturday -> Monday
                    greet = greet + timedelta(days=2)
                elif greet.weekday() == 6:     # Sunday -> Monday
                    greet = greet + timedelta(days=1)
                assert item["birthday"] == greet.strftime("%d.%m.%Y")
                break
    else:
        # if nothing found (shouldn't happen)
        assert False, "No upcoming birthday detected within 7 days"

