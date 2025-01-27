from app import ContactsApp

def test_add_contact():
    app = ContactsApp()
    app.add_contact("John Doe", "1234567890")
    app.add_contact("Jane Smith", "0987654321")
    contacts = app.get_contacts()
    assert len(contacts) == 2
    assert "John Doe" in contacts
    assert "Jane Smith" in contacts

def test_delete_contact():
    app = ContactsApp()
    app.add_contact("John Doe", "1234567890")
    app.add_contact("Jane Smith", "0987654321")
    app.delete_contact("John Doe")
    contacts = app.get_contacts()
    assert len(contacts) == 1
    assert "John Doe" not in contacts
    assert "Jane Smith" in contacts

def test_search_contact():
    app = ContactsApp()
    app.add_contact("John Doe", "1234567890")
    app.add_contact("Jane Smith", "0987654321")
    contact = app.search_contact("John Doe")
    assert contact is not None
    assert contact['name'] == "John Doe"
    assert contact['phone'] == "1234567890"

def test_show_contacts():
    app = ContactsApp()
    app.add_contact("John Doe", "1234567890")
    app.add_contact("Jane Smith", "0987654321")
    contacts = app.get_contacts()
    assert len(contacts) == 2
    assert "John Doe" in contacts
    assert "Jane Smith" in contacts

if __name__ == "__main__":
    test_add_contact()
    test_show_contacts()
    test_delete_contact()
    test_show_contacts()
    test_search_contact()
    print("All tests passed!")