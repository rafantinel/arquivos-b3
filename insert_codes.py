import sqlite3
from tqdm import tqdm
from functions import count_rows


# File to read
file = "cotações_b3/COTAHIST_A2022.TXT"
# Database connection
conn = sqlite3.connect("stocks.db")

def main():

    # Add unique codes to database
    insert()

# Add unique stock codes to database
def insert():
    c = conn.cursor()
    before = c.execute("SELECT count(*) FROM ativos").fetchall()[0][0]
    index = 1
    n = count_rows(file)
    added = set()
    with open(file, "r", newline="") as f:
        for i in tqdm(range(n)):
            row = f.readline().strip()
            if row[2:10].isnumeric():
                get_id = c.execute("SELECT id FROM ativos WHERE codneg = ?", (row[12:24].strip(), )).fetchall()
                if not get_id and row[12:24].strip() not in added:
                    c.execute("INSERT INTO ativos (id, codneg) VALUES (?, ?)", (before + index, row[12:24].strip()))
                    index += 1
                    added.add(row[12:24].strip())

    # print(list(added))
    after = c.execute("SELECT count(*) FROM ativos").fetchall()[0][0]
    conn.commit()
    conn.close()            

    return print(f"Added rows: {after - before}")


if __name__ == "__main__":
    main()
