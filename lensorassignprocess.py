import csv
import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def process_file(input_file):
    rows = []

    with open(input_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    i = 0
    while i < len(lines):
        if lines[i] == "To do":
            try:
                time_of_inspection = lines[i + 1]
                license_plate = lines[i + 2]
                rows.append([time_of_inspection, license_plate])
                i += 3
            except IndexError:
                break
        else:
            i += 1

    output_file = os.path.splitext(input_file)[0] + ".csv"

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Time of inspection", "License plate"])
        writer.writerows(rows)

    return output_file


def pick_file():
    root = tk.Tk()
    root.withdraw()  # Hide main window

    file_path = filedialog.askopenfilename(
        title="Select TXT file",
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_path:
        return

    try:
        output = process_file(file_path)
        messagebox.showinfo("Success", f"CSV created:\n{output}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    # Case 1: Drag & drop (file passed as argument)
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        try:
            output = process_file(input_file)
            print(f"CSV created: {output}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        # Case 2: Open file picker
        pick_file()