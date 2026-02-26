import sqlite3

# Create a database connection
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create a sample table
cursor.execute("""
CREATE TABLE IF NOT EXISTS research_data (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    content TEXT
)
""")

# Insert sample data
cursor.execute("INSERT INTO research_data (title, author, content) VALUES (?, ?, ?)",
               ("AI in Medicine", "John Doe", "This study explores AI applications in medicine..."))
conn.commit()
conn.close()