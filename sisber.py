# Data rekening bank
data_rekening = [
    {"ID": "111111", "GROUP_CODE": "DT", "LIMIT": 0},
    {"ID": "112131", "GROUP_CODE": "NW", "LIMIT": 100},
    {"ID": "198121", "GROUP_CODE": "DT", "LIMIT": 200},
    {"ID": "201431", "GROUP_CODE": "DT", "LIMIT": 100},
    {"ID": "208432", "GROUP_CODE": "NW", "LIMIT": 0},
    {"ID": "291821", "GROUP_CODE": "NW", "LIMIT": 0},
    {"ID": "300123", "GROUP_CODE": "NE", "LIMIT": 100},
    {"ID": "310103", "GROUP_CODE": "DT", "LIMIT": 0},
    {"ID": "324196", "GROUP_CODE": "EA", "LIMIT": 0},
    {"ID": "335812", "GROUP_CODE": "DT", "LIMIT": 0},
    {"ID": "386132", "GROUP_CODE": "WE", "LIMIT": 100},
    {"ID": "387122", "GROUP_CODE": "WE", "LIMIT": 0},
    {"ID": "415631", "GROUP_CODE": "NE", "LIMIT": 100},
    {"ID": "486212", "GROUP_CODE": "DT", "LIMIT": 100},
    {"ID": "511211", "GROUP_CODE": "NW", "LIMIT": 250},
    {"ID": "534216", "GROUP_CODE": "EA", "LIMIT": 250},
    {"ID": "535218", "GROUP_CODE": "EA", "LIMIT": 250},
    {"ID": "641230", "GROUP_CODE": "DT", "LIMIT": 100},
    {"ID": "686116", "GROUP_CODE": "DT", "LIMIT": 100},
    {"ID": "696123", "GROUP_CODE": "NE", "LIMIT": 25}
]

group_index = {}

for rekening in data_rekening:
    group = rekening["GROUP_CODE"]
    id_rekening = rekening["ID"]

    if group not in group_index:
        group_index[group] = []

    group_index[group].append(id_rekening)

print("=== INVERTED INDEX GROUP-CODE ===")
for group, ids in group_index.items():
    print(f"{group} -> {', '.join(ids)}")


print("\n=== MENCARI GROUP-CODE ===")
cari = input("Masukkan GROUP-CODE: ").upper()

if cari in group_index:
    print("ID yang ditemukan:")
    for id_rekening in group_index[cari]:
        print(id_rekening)
else:
    print("GROUP-CODE tidak ditemukan")

# ==================================================
# SOAL 3 : Inverted Index berdasarkan LIMIT
# ==================================================
limit_index = {}

for rekening in data_rekening:
    limit = rekening["LIMIT"]
    id_rekening = rekening["ID"]

    if limit not in limit_index:
        limit_index[limit] = []

    limit_index[limit].append(id_rekening)

print("\n=== INVERTED INDEX LIMIT ===")
for limit, ids in limit_index.items():
    print(f"LIMIT = {limit} -> {', '.join(ids)}")


print("\nID dengan LIMIT = 100")
for id_rekening in limit_index.get(100, []):
    print(id_rekening)