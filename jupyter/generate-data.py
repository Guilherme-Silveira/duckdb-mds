import argparse
import random
import csv

def pretty_sci(x):
    tmp = str(x).split("+", 1)[0]
    if len(tmp) == 1:
        return tmp[0] + "e" + str(len(tmp) - 1)
    elif len(tmp) == 2:
        return tmp[0] + str(int(tmp[1]))

parser = argparse.ArgumentParser()
parser.add_argument("num_rows", type=int)
parser.add_argument("K", type=int)
parser.add_argument("nas", type=int)
parser.add_argument("sort", type=int)
args = parser.parse_args()

num_rows = args.num_rows
K = args.K
nas = args.nas
sort_flag = args.sort

assert nas <= 100 and nas >= 0
assert sort_flag in [0, 1]

random.seed(108)
print(f"Producing data of {pretty_sci(num_rows)} rows, {pretty_sci(K)} K groups factors, {nas} NAs ratio, {sort_flag} sort flag")

DT = {}
DT["id1"] = [f"id{num:03d}" for num in random.choices(range(1, min(K, num_rows) + 1), k=num_rows)]  # large groups (str) # large groups (str)
DT["id2"] = [f"id{num:03d}" for num in random.choices(range(1, min(K, num_rows) + 1), k=num_rows)]  # small groups (str)
DT["id3"] = [f"id{num:010d}" for num in random.choices(range(1, min(num_rows // K + 1, num_rows) + 1), k=num_rows)]  # large groups (str)
DT["id4"] = random.choices(range(1, min(K, num_rows) + 1), k=num_rows)  # large groups (int)
DT["id5"] = random.choices(range(1, min(K, num_rows) + 1), k=num_rows)  # small groups (int)
DT["id6"] = random.choices(range(1, min(num_rows // K + 1, num_rows) + 1), k=num_rows)  # small groups (int)
DT["v1"] = random.choices(range(1, 6), k=num_rows)  # int in range [1,5]
DT["v2"] = random.choices(range(1, 16), k=num_rows)  # int in range [1,15]
DT["v3"] = [round(random.uniform(0, 100), 6) for _ in range(num_rows)]  # numeric e.g. 23.574912

if nas > 0:
    print("Inputting NAs")
    for col in ["id1", "id2", "id3", "id4", "id5", "id6"]:
        ucol = list(set(DT[col]))
        nna = int(len(ucol) * (nas / 100))
        if nna > 0:
            indices = random.sample(range(len(ucol)), nna)
            for idx in indices:
                for i, val in enumerate(DT[col]):
                    if val == ucol[idx]:
                        DT[col][i] = None
            del indices
        del ucol
    nna = int(num_rows * (nas / 100))
    if nna > 0:
        for col in ["v1", "v2", "v3"]:
            indices = random.sample(range(num_rows), nna)
            for idx in indices:
                DT[col][idx] = None
        del indices

if sort_flag == 1:
    print("Sorting data")
    sorted_keys = sorted(DT.keys())
    DT = {k: v for k in sorted_keys for v in [DT[k]]}

# Write the data to a CSV file
output_file = "benchmark_data.csv"
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(DT.keys())
    writer.writerows(zip(*DT.values()))

print(f"Data written to {output_file}, quitting")
