# NotionExportRenamer: Rename Files and Folders by Removing Trailing IDs

This Python script renames files and folders within a specified directory by removing trailing IDs. It works recursively through all subdirectories. The ID is identified as a 32-character hexadecimal string at the end of the file or folder name.

## Features

- **Recursive Renaming**: Processes files and folders at all levels of the specified directory.
- **ID Removal**: Removes trailing IDs from filenames and folder names, where IDs are 32-character hexadecimal strings.
- **Command-Line Interface**: Easily specify the target directory as a command-line argument.

## Requirements

- Python 3.x

## Installation

**Clone the Repository**:

```bash
git clone https://github.com/JudexMars/NotionExportRenamer.git
cd NotionExportRenamer
```

## Usage

1. **Save the Script**: Save the script as `NotionExportRenamer.py` in your desired directory.

2. **Run the Script**:

    ```bash
    python rename_files.py /path/to/your/directory
    ```

    Replace `/path/to/your/directory` with the path to the directory you want to process.

3. **Example**:

    ```bash
    python rename_files.py /Users/yourusername/Documents
    ```

    This command will process all files and folders in the `Documents` directory and its subdirectories, removing any trailing IDs from their names.

## How It Works

- **ID Validation**: The script identifies IDs as 32-character hexadecimal strings (e.g., `7ec72751d2ab45ffb7c99909163dda9f`).
- **Filename Processing**: For each file and folder, the script splits the name to isolate the ID and removes it if valid.
- **Extension Handling**: The script correctly handles filenames with extensions, ensuring the extension remains intact after renaming.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

1. **Fork the Repository**.
2. **Create a Feature Branch**: `git checkout -b feature/YourFeature`
3. **Commit Your Changes**: `git commit -am 'Add new feature'`
4. **Push to the Branch**: `git push origin feature/YourFeature`
5. **Create a New Pull Request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


