import sqlite3

DB_NAME = "requirements_data.db"
OUTPUT_FILE = "requirements_longtable.tex"

def escape_latex(text):
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
        "\\": r"\textbackslash{}",
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

def fetch_requirements():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT requirement, priority, use_case_id FROM requirements")
    rows = cursor.fetchall()
    conn.close()
    return rows

def generate_longtable(rows):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(r"\begin{longtable}{|p{6cm}|p{2cm}|p{2cm}|}" + "\n")
        f.write(r"\hline" + "\n")
        f.write(r"\textbf{Requirement} & \textbf{Priority} & \textbf{UseCase ID} \\" + "\n")
        f.write(r"\hline" + "\n")
        f.write(r"\endfirsthead" + "\n")

        f.write(r"\hline" + "\n")
        f.write(r"\textbf{Requirement} & \textbf{Priority} & \textbf{UseCase ID} \\" + "\n")
        f.write(r"\hline" + "\n")
        f.write(r"\endhead" + "\n")

        for requirement, priority, use_case_id in rows:
            req = escape_latex(requirement)
            pr = escape_latex(priority)
            uc = escape_latex(use_case_id)

            f.write(f"{req} & {pr} & {uc} \\\\\n")
            f.write(r"\hline" + "\n")

        f.write(r"\end{longtable}" + "\n")

if __name__ == "__main__":
    rows = fetch_requirements()
    generate_longtable(rows)
    print(f"LaTeX file generated: {OUTPUT_FILE}")