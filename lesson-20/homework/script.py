import pandas as pd
import sqlite3

# -------------------------
# Create a sample Chinook-like database from scratch
# -------------------------
conn = sqlite3.connect(":memory:")  # In-memory database

# Create tables
conn.execute("""
CREATE TABLE Customer (
    CustomerId INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT
)
""")
conn.execute("""
CREATE TABLE Invoice (
    InvoiceId INTEGER PRIMARY KEY,
    CustomerId INTEGER,
    Total REAL,
    FOREIGN KEY (CustomerId) REFERENCES Customer(CustomerId)
)
""")
conn.execute("""
CREATE TABLE Album (
    AlbumId INTEGER PRIMARY KEY
)
""")
conn.execute("""
CREATE TABLE Track (
    TrackId INTEGER PRIMARY KEY,
    AlbumId INTEGER,
    FOREIGN KEY (AlbumId) REFERENCES Album(AlbumId)
)
""")
conn.execute("""
CREATE TABLE InvoiceLine (
    InvoiceLineId INTEGER PRIMARY KEY,
    InvoiceId INTEGER,
    TrackId INTEGER,
    FOREIGN KEY (InvoiceId) REFERENCES Invoice(InvoiceId),
    FOREIGN KEY (TrackId) REFERENCES Track(TrackId)
)
""")

# Insert customers
customers_data = [
    (1, "John", "Smith"),
    (2, "Alice", "Brown"),
    (3, "Bob", "Taylor"),
    (4, "Emily", "Davis"),
    (5, "Michael", "Johnson"),
    (6, "Sophia", "Williams"),
]
conn.executemany("INSERT INTO Customer VALUES (?, ?, ?)", customers_data)

# Insert albums & tracks
albums_data = [(1,), (2,), (3,)]
tracks_data = [
    (1, 1), (2, 1), (3, 1),   # Album 1
    (4, 2), (5, 2),           # Album 2
    (6, 3),                   # Album 3
]
conn.executemany("INSERT INTO Album VALUES (?)", albums_data)
conn.executemany("INSERT INTO Track VALUES (?, ?)", tracks_data)

# Insert invoices
invoices_data = [
    (1, 1, 15.0),
    (2, 1, 20.0),
    (3, 2, 9.0),
    (4, 3, 12.0),
    (5, 4, 25.0),
    (6, 5, 40.0),
    (7, 6, 30.0),
]
conn.executemany("INSERT INTO Invoice VALUES (?, ?, ?)", invoices_data)

# Insert invoice lines (some full albums, some partial)
invoice_lines_data = [
    (1, 1, 1), (2, 1, 2), (3, 1, 3),  # Full Album 1 for customer 1
    (4, 2, 4),                         # Partial Album 2 for customer 1
    (5, 3, 4), (6, 3, 5),              # Full Album 2 for customer 2
    (7, 4, 1),                         # Partial Album 1 for customer 3
    (8, 5, 6),                         # Album 3 for customer 4 (full)
    (9, 6, 1),                         # Partial Album 1 for customer 5
    (10, 7, 4), (11, 7, 5),            # Full Album 2 for customer 6
]
conn.executemany("INSERT INTO InvoiceLine VALUES (?, ?, ?)", invoice_lines_data)

# -------------------------
# 1️⃣ Customer Purchases Analysis
# -------------------------
customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM Customer", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId, Total FROM Invoice", conn)

customer_totals = invoices.groupby("CustomerId")["Total"].sum().reset_index(name="TotalSpent")
customer_totals = customer_totals.merge(customers, on="CustomerId")
top5_customers = customer_totals.sort_values("TotalSpent", ascending=False).head(5)

print("🏆 Top 5 Customers by Total Purchases:\n", top5_customers)

# -------------------------
# 2️⃣ Album vs Individual Track Purchases
# -------------------------
invoice_lines = pd.read_sql("SELECT InvoiceLineId, InvoiceId, TrackId FROM InvoiceLine", conn)
tracks = pd.read_sql("SELECT TrackId, AlbumId FROM Track", conn)

invoice_tracks = invoice_lines.merge(tracks, on="TrackId").merge(invoices[["InvoiceId", "CustomerId"]], on="InvoiceId")
album_track_counts = tracks.groupby("AlbumId").size().reset_index(name="TotalTracksInAlbum")
customer_album_purchases = invoice_tracks.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index(name="TracksBought")
purchase_comparison = customer_album_purchases.merge(album_track_counts, on="AlbumId")
purchase_comparison["FullAlbumBought"] = purchase_comparison["TracksBought"] == purchase_comparison["TotalTracksInAlbum"]

customer_pref = purchase_comparison.groupby("CustomerId")["FullAlbumBought"].apply(lambda x: not all(x)).reset_index(name="PrefersIndividual")
pref_summary = customer_pref["PrefersIndividual"].value_counts(normalize=True) * 100
pref_summary = pref_summary.rename(index={True: "Individual Tracks", False: "Full Albums"}).reset_index()
pref_summary.columns = ["Preference", "Percentage"]

print("\n📊 Customer Purchase Preference Summary:\n", pref_summary)

# Close connection
conn.close()
