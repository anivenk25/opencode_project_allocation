# Project Role Allocation Script

## Algorithm Overview

- **Reading Input Data:** The script reads the input CSV file containing respondent preferences into a pandas DataFrame.
  
- **Define Vacancy Data:** A predefined vacancy dataset (`vacancy_data`) is used to represent available roles per project.
  
- **Allocation Function (`allocate_project_role_pair`):**
  - For each respondent row, the function allocates a project-role pair based on the chosen allocation precedence (`PROJECT` or `ROLE`).
  - If allocation by `PROJECT` precedence is chosen:
    - It iterates over project columns to determine the most preferred project with available role vacancies.
    - Then, it looks for the most preferred role within that project where vacancies exist.
  - If allocation by `ROLE` precedence is chosen:
    - It iterates over role priorities to determine the most preferred role.
    - Within each role, it checks for available vacancies across all projects to allocate the role.
  
- **Main Execution (`main`):**
  - Reads the input CSV file.
  - Applies the allocation function to each row using `apply` method.
  - Filters out rows where allocation failed (e.g., due to all vacancies being filled).
  - Writes the allocated data to a new CSV file (`output_data.csv`).

## Usage

### Input Data Format

Prepare your input data in a CSV format with the following columns:

- `CHOOSE PRECEDENCE OF ALLOCATION`: Specify allocation precedence as 'PROJECT' or 'ROLE'.
- Columns for project priorities (e.g., `PROJECT PRIORITY [ProjectName]`) and role priorities (e.g., `ROLE PRIORITY [RoleName]`) based on participant preferences.

### Vacancy Data Setup

Modify the `vacancy_data` dictionary within the script to reflect available vacancies for each project-role combination. Update the number of vacancies (integer values) for different projects and roles accordingly.

## Customization

- Customize the `vacancy_data` dictionary to reflect your project-specific vacancy data for different projects and roles.
- Adjust the allocation logic within the `allocate_project_role_pair` function based on your specific allocation requirements.

## Error Handling

The script includes comprehensive error handling to manage potential issues during file reading, allocation processing, and other unexpected exceptions encountered during execution.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- pandas library (install via `pip install pandas`)

## Contributors

- Anirudh Venkateswaran
