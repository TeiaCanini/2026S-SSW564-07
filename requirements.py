import sqlite3

# Create a database connection
conn = sqlite3.connect("requirements_data.db")
cursor = conn.cursor()

# Create a sample table
cursor.execute("""
CREATE TABLE IF NOT EXISTS requirements (
    id PK,
    requirement TEXT NOT NULL, 
    priority TEXT NOT NULL, 
    use_case_id TEXT NOT NULL
)
""")

# Insert sample data
cursor.execute("INSERT INTO requirements (requirement, priority, use_case_id) VALUES (?, ?, ?)",
               ("The system shall be FDA approved.", "must", "N/A"))
cursor.execute("INSERT INTO requirements (requirement, priority, use_case_id) VALUES (?, ?, ?)",
               ("The system shall offer meals at prices which are competitive with pre-existing local food delivery services.", "should", "N/A"))
cursor.execute("INSERT INTO requirements (requirement, priority, use_case_id) VALUES (?, ?, ?)",
               ("The system shall maximize food utilization and minimize waste.", "could", "N/A"))
conn.commit()
conn.close()

def fetch_data():
    conn = sqlite3.connect("requirements_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM requirements")
    data = cursor.fetchall()
    conn.close()
    return data

# Example usage
entries = fetch_data()
for entry in entries:
    print(entry)