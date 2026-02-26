import sqlite3

def fetch_data():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM research_data")
    data = cursor.fetchall()
    conn.close()
    return data

# Example usage
entries = fetch_data()
for entry in entries:
    print(entry)