# 📞 Telephone Directory Management System (TDMS)

A simple and interactive **command-line based contact manager** built using Python. It allows users to store, search, update, delete, and export contact records easily.

---

## 🚀 Features

- Add new contacts with name, phone, and email
- View all saved contacts
- Search contacts by name, phone, or email
- Update existing contact details
- Delete unwanted contacts
- Export contact list to CSV
- Stores data persistently using `pickle`

---

## 🖥️ How to Run

```bash
python TDMS.py
```

---

## 📋 Menu Options

```
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Export Contacts to CSV
7. Exit
```

---

## 🗂️ File Structure

```
TDMS/
├── TDMS.py                    # Main program file
├── telephone_directory.dat    # Stores contact data (auto-created)
└── telephone_directory.csv    # Optional CSV export file
```

---

## 🧩 Requirements

This project uses only standard Python libraries:
- `pickle`
- `csv`

> ✅ No external packages needed

---

## 📤 CSV Export Example

```csv
Name,Phone,Email
Alice,9876543210,alice@example.com
Bob,9123456789,bob@example.com
```

---

## 📚 Future Enhancements

- GUI with Tkinter or PyQt
- Input validation
- Backup/restore features
- Contact categories and tags

---

## 📄 License

This project is free to use for learning and personal use.

---