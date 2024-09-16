import os
import re
import argparse


def is_valid_id(word):
    return bool(re.match(r'^[a-f0-9]{32}$', word))


def remove_id_from_name(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            rename_file_or_folder(root, filename)

        for dirname in dirs:
            rename_file_or_folder(root, dirname)


def rename_file_or_folder(root, name):
    if name.startswith('.'):
        return

    name = name.strip()

    base_name, extension = os.path.splitext(name)

    name_parts = base_name.rsplit(' ', 1)

    if len(name_parts) == 2 and is_valid_id(name_parts[1].strip()):
        new_base_name = name_parts[0]
        new_name = new_base_name + extension

        old_full_path = os.path.join(root, name)
        new_full_path = os.path.join(root, new_name)

        os.rename(old_full_path, new_full_path)
        print(f"Renamed: '{old_full_path}' -> '{new_full_path}'")


def main():
    parser = argparse.ArgumentParser(description='Rename files and folders by removing trailing IDs.')
    parser.add_argument('directory', type=str, help='Path to the directory to process')

    args = parser.parse_args()
    directory = args.directory

    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    remove_id_from_name(directory)


if __name__ == "__main__":
    main()
