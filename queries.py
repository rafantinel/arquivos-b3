import sqlite3
# from tqdm import tqdm

CONN = sqlite3.connect("stocks.db")
c = CONN.cursor()

query = c.execute(""" SELECT ativos.codneg, dia, mes, ano, modref, preult FROM preço_anual 
    JOIN ativos ON ativos.id = preço_anual.id_ativo ORDER BY ativos.codneg, ano
""").fetchall()
h = ",".join(list(map(lambda x: x[0], c.description)))
if query:
    with open("query.txt", "w") as q:
        q.write(h)
        for i, row in enumerate(query):
            r = ",".join(str(j) for j in list(row))
            q.write(f"\n{r}")

CONN.commit()
CONN.close()

