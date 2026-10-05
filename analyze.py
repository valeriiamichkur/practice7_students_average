INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

math_summ = 0
python_summ = 0
english_summ = 0
count = 0
name_best = ""
name_best_average = 0

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)

    for line in f:
        line = line.strip()
        name, math, python, english = line.split(",")
        math, python, english = int(math), int(python), int(english)
        math_summ += math
        python_summ += python
        english_summ += english
        count += 1
        average = (math + python + english) / 3
        if average > name_best_average:
            name_best_average = average
            name_best = name

math_average = math_summ / count
python_average = python_summ / count
english_average = english_summ / count

result = (
    "Середній бал по класу:\n"
    f"math: {math_average:.1f}\n"
    f"python: {python_average:.1f}\n"
    f"english: {english_average:.1f}\n"
    "\n"
    f"Найкращий студент: {name_best} ({name_best_average:.1f})\n")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(result)

print(result)

