# JSON Validation Report Generator

This Python script validates JSON data from a CSV file and generates a detailed report on validation results.

## Features

- Validates each JSON data entry in the CSV file.
- Generates a report indicating validation status and error messages (if any).
- Utilizes progress bars to indicate processing status.

## Usage

1. **Setup**: Ensure Python 3.x is installed on your system.
2. **Clone the Repository**: Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
   ```
3. **Install Dependencies**: There are no external dependencies beyond Python's standard library.
4. **Run the Script**:
   Modify the `csv_file_path` and `delimiter` variables in main.py to match your CSV file and delimiter respectively. Then execute the script:

   ```bash
   python main.py
   ```
5. View the Report: Once completed, a report file (return_json_valid_info.txt) will be generated in the project directory.

## Structure

- main.py: Main script to read CSV data, validate JSON entries, and generate the report.
- return_json_valid_info.txt: Generated report file detailing validation results.
