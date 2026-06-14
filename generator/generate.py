import csv
import random
import os
import sys

NUM_ROWS = 50


COLUMNS = ["ВЕС_КГ", "РОСТ_М", "ВОЗРАСТ_ЛЕТ", "КАТЕГОРИЯ"]

def generate_row():

    return {
        "ВЕС_КГ": random.randint(0, 100),
        "РОСТ_М": round(random.uniform(1.5, 9.9), 2),
        "ВОЗРАСТ_ЛЕТ": random.randint(0, 100),
        "КАТЕГОРИЯ": random.choice(["ТРАВОЯДНОЕ", "ВСЕЯДНОЕ", "ХИЩНИК"]),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)