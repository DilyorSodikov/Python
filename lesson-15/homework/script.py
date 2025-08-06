import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

# 1. Create Roster table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
''')

# 2. Populate table with initial values
cursor.execute("DELETE FROM Roster")  # Clear existing data to avoid duplication

roster_data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29),
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", roster_data)

# 3. Update Jadzia Dax to Ezri Dax
cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

# 4. Display Name and Age of Bajoran species
print("Bajoran Members (Name & Age):")
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
rows = cursor.fetchall()
for name, age in rows:
    print(f"{name} - Age {age}")

# Finalize
conn.commit()
conn.close()
