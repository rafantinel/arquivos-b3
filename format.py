from functions import format_file
from tqdm import tqdm

HEADER = [
    "DATA", # 3-10
    "CODNEG", # 13-24
    "MODREF", # 53-56
    "PREULT" # 109-121
]

file = "cotações_b3/COTAHIST_A2013.TXT"

rows = format_file(HEADER, file)
n = len(rows)

with open("out.txt", "w") as out:
    for i in tqdm(range(n)):
        if i > 0:
            out.write("\n")
        out.write(rows[i])