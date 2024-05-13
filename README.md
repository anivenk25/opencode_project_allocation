## Project Role Allocation Script

This Python script automates the allocation of participants to project roles based on their preferences and predefined vacancy data.

## Overview

The script reads participant preferences from a CSV file, determines project-role allocations based on specified precedence ('PROJECT' or 'ROLE'), and outputs the allocated data to a new CSV file. It includes error handling for various scenarios.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- pandas library (install via `pip install pandas`)

## Usage

**1. Input Data Format**

Prepare your input data in a CSV format with the following columns:

  - `CHOOSE PRECEDENCE OF ALLOCATION`: Specify allocation precedence as 'PROJECT' or 'ROLE'.
  - Columns for project priorities (e.g., `PROJECT PRIORITY [ProjectName]`) and role priorities (e.g., `ROLE PRIORITY [RoleName]`) based on participant preferences.

**2. Vacancy Data Setup**

Modify the `vacancy_data` dictionary within the script (`allocate_roles.py`) to reflect available vacancies for each project-role combination. Update the number of vacancies (integer values) for different projects and roles accordingly.

**3. Run the Script**

Execute the script from the command line:

```bash
python allocate_roles.py'''
Use code with caution.
content_copy

**4. Output**

  - The script generates an output CSV file (output_dataf.csv) containing the allocated project-role pairs based on the allocation logic and vacancy data.

**Script Functionality**
The script includes the following functions:

read_input_file(input_file_path): Reads the input CSV file into a pandas DataFrame and handles potential errors like file not found, empty data, and other exceptions.
allocate_project_role_pair(row, vacancy_data): Allocates a project-role pair based on the specified allocation precedence for each participant in the input data. It iterates over project and role priorities to select and allocate available roles based on vacancy data.
main(): Orchestrates the script execution: reads input data, defines vacancy data, allocates project-role pairs using the provided function, and writes the allocated data to a new CSV file.


**Customization**
  - Modify the vacancy_data dictionary in the script (allocate_roles.py) to reflect your project-specific vacancy data for different projects and roles.
  - Adjust the allocation logic (e.g., priority order of projects and roles) within the allocate_project_role_pair function based on your specific allocation requirements.

**Error Handling**
  - The script includes comprehensive error handling to manage potential issues during file reading, allocation processing, and other unexpected exceptions encountered during execution.

**Contributors**
  -Anirudh Venkateswaran
