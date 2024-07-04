====================================================================================================
Project Overview
====================================================================================================

This project consists of independent scripts designed to validate JSON data from a CSV file and generate a detailed report on the validation results.

----------------------------------------------------------------------------------------------------
Components
----------------------------------------------------------------------------------------------------

1. `gen_raport.py`: This script reads JSON data from a CSV file, validates each JSON string, and generates a report (`return_json_valid_info.txt`) summarizing the validation status for each line.

2. `utils.py`: Contains utility functions used in `gen_raport.py`, including progress bar rendering (`printProgressBar`), JSON validation (`validateJSON`), and subprocess validation (`validate_line`).

----------------------------------------------------------------------------------------------------
Usage
----------------------------------------------------------------------------------------------------

To use the project:
- Ensure Python 3.x is installed on your system.
- Clone the repository from GitHub.

----------------------------------------------------------------------------------------------------
Instructions
----------------------------------------------------------------------------------------------------

1. Place your CSV file containing JSON data (`json-err.json`) in the project directory.
2. Modify `csv_file_path` and `delimiter` in `gen_raport.py` if necessary.
3. Run `python gen_raport.py`.
4. Monitor the progress bar indicating the validation process.
5. Once completed, view the generated report (`return_json_valid_info.txt`) for detailed validation results.

----------------------------------------------------------------------------------------------------
Dependencies
----------------------------------------------------------------------------------------------------

- This project uses standard Python libraries (`json`, `csv`, `subprocess`, `os`, `time`).

----------------------------------------------------------------------------------------------------
Author
----------------------------------------------------------------------------------------------------

- Created by [Your Name]

----------------------------------------------------------------------------------------------------
License
----------------------------------------------------------------------------------------------------

This project is licensed under the [License Name] License - see the LICENSE.md file for details.

====================================================================================================
