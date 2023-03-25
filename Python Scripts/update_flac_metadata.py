import os
import csv
from tkinter import filedialog, simpledialog, messagebox
from tkinter import Tk
from mutagen.flac import FLAC

def update_flac_metadata(file_path, metadata_field, filename_section, remove_section, overwrite_all=None):
    try:
        file_name = os.path.basename(file_path)
        sections = file_name.split('_')

        metadata_value = sections[filename_section - 1]
        audio = FLAC(file_path)
        audio[metadata_field.lower()] = metadata_value
        audio.save()

        if remove_section:
            sections.pop(filename_section - 1)
            new_file_name = '_'.join(sections)
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

            if os.path.exists(new_file_path):
                if overwrite_all is None:
                    overwrite_all = messagebox.askyesno(
                        "Overwrite or Increment",
                        "There is a conflict with the filenames. "
                        "Do you want to:\n\n"
                        "YES - Overwrite All\n"
                        "NO - Increment Filenames"
                    )

                if overwrite_all:
                    os.remove(new_file_path)
                else:
                    count = 1
                    name, ext = os.path.splitext(new_file_name)
                    while os.path.exists(new_file_path):
                        new_file_name = f"{name}_{count:03}{ext}"
                        new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
                        count += 1

            os.rename(file_path, new_file_path)
            file_path = new_file_path
        return file_path, overwrite_all
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return file_path, overwrite_all

import re

def export_filenames_to_csv(file_paths, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        for file_path in file_paths:
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            file_name = re.sub(r'-\d{3}$', '', file_name)
            writer.writerow([file_name])


def main():
    root = Tk()
    root.withdraw()

    file_paths = filedialog.askopenfilenames(
        title="Select FLAC files",
        filetypes=(("FLAC files", "*.flac"),)
    )
    root.update()

    if not file_paths:
        return

    while True:
        sample_file_name = os.path.basename(file_paths[0])

        metadata_field = simpledialog.askstring(
            "Metadata Field",
            "Enter the metadata field you want to edit (e.g., title, artist, album, genre, comment, description, custom tags, key):"
        )

        filename_section = simpledialog.askinteger(
            "Filename Section",
            f"Enter the section number from the filename to use (1-based index; e.g., 1 for the first section):\n\n{sample_file_name}"
        )

        remove_section = messagebox.askyesno(
            "Remove Section",
            "Do you want to remove the selected section from the filename?"
        )

        overwrite_all = None
        updated_file_paths = []
        for file_path in file_paths:
            updated_file_path, overwrite_all = update_flac_metadata(file_path, metadata_field, filename_section, remove_section, overwrite_all)
            updated_file_paths.append(updated_file_path)

        file_paths = updated_file_paths

        if not messagebox.askyesno("Edit More Metadata", "Do you want to edit more metadata for these files?"):
            output_file = filedialog.asksaveasfilename(
                title="Save CSV",
                defaultextension=".csv",
                filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
            )
            if output_file:
                export_filenames_to_csv(file_paths, output_file)
            break

if __name__ == "__main__":
    main()
