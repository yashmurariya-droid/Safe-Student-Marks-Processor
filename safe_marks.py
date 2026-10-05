
import csv

filename = "students.csv"

try:
    with open(filename, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or not {"name", "marks"}.issubset(
            {field.strip().lower() for field in reader.fieldnames}
        ):
            raise ValueError("CSV must contain 'name' and 'marks' columns.")

        students = []

        for row in reader:
            try:
                name = row["name"].strip()
                marks = float(row["marks"])

                if not name:
                    raise ValueError("Student name is empty.")

                if not 0 <= marks <= 100:
                    raise ValueError("Marks must be between 0 and 100.")

                students.append({"name": name, "marks": marks})

            except (ValueError, TypeError, KeyError) as error:
                print(f"Skipping invalid row: {row} ({error})")

    if not students:
        print("No valid student records found.")
    else:
        average = sum(s["marks"] for s in students) / len(students)
        top = max(students, key=lambda s: s["marks"])

        print(f"Valid students: {len(students)}")
        print(f"Average marks: {average:.2f}")
        print(f"Top student: {top['name']} ({top['marks']:g})")

except FileNotFoundError:
    print(f"Error: {filename} was not found.")
except PermissionError:
    print("Error: Permission denied while reading the file.")
except (OSError, ValueError) as error:
    print(f"Could not process the CSV: {error}")