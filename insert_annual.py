import sqlite3
from tqdm import tqdm
from functions import count_rows


# File to read
file = "cotações_b3/COTAHIST.A1986"
# Database connection
conn = sqlite3.connect("stocks.db")

def main():

    # Open file and insert rows to database
    # File must be sorted by date
    insert()

# Insert to database first day of year for each code
def insert():
    c = conn.cursor()
    before = c.execute("SELECT count(*) FROM preço_anual").fetchall()[0][0]
    index = 1
    n = count_rows(file)
    added = set()
    with open(file, "r", newline="") as f:
        for i in tqdm(range(n)):
            row = f.readline().strip()
            get_id = c.execute("SELECT id FROM ativos WHERE codneg = ?", (row[12:24].strip(), )).fetchall()
            if get_id and row[12:24].strip() not in added:
                year = row[2:10][0:4]
                day = row[2:10][6:8]
                month = row[2:10][4:6]
                c.execute("INSERT INTO preço_anual (id, id_ativo, dia, mes, ano, modref, preult) VALUES (?, ?, ?, ?, ?, ?, ?)", (before + index, get_id[0][0], day, month, year, row[52:56].strip(), row[108:121]))
                index += 1
                added.add(row[12:24].strip())

    after = c.execute("SELECT count(*) FROM preço_anual").fetchall()[0][0]
    conn.commit()
    conn.close()

    return print(f"Added rows: {after - before}")


if __name__ == "__main__":
    main()
