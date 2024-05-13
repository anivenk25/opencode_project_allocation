import pandas as pd
from collections import defaultdict

# Path to the input CSV file containing the data
input_file_path = r"D:\OPENCODE DEMO - Form responses 1.csv"
# Path to the output CSV file where allocated data will be written
output_file_path = 'output_dataf.csv'

def read_input_file(input_file_path):
    """
    Read input CSV file into pandas DataFrame.

    Args:
        input_file_path (str): Path to the input CSV file.

    Returns:
        pd.DataFrame: DataFrame containing input data.
    """
    try:
        df = pd.read_csv(input_file_path)
        return df
    except FileNotFoundError:
        print(f"Input file not found at: {input_file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"Input file is empty: {input_file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading input file: {e}")
        return None

def allocate_project_role_pair(row, vacancy_data):
    """
    Allocate project-role pair based on allocation precedence (PROJECT or ROLE).

    Args:
        row (pd.Series): Input row containing allocation preferences.
        vacancy_data (dict): Dictionary of project-wise role vacancies.

    Returns:
        str or None: Project-role pair (e.g., 'SOCIAL MEDIA APP, ML') or None if allocation failed.
    """
    try:
        if row['CHOOSE PRECEDENCE OF ALLOCATION'] == 'PROJECT':
            project_cols = [col for col in row.index if 'PROJECT PRIORITY' in col]
            role_priorities = [col for col in row.index if 'ROLE PRIORITY' in col]

            for project_col in sorted(project_cols, key=lambda x: row[x]):
                chosen_project = project_col.split('[')[1].split(']')[0]
                roles_vacancies = vacancy_data[chosen_project]

                for role in sorted(role_priorities, key=lambda x: row[x]):
                    chosen_role = role.split('[')[1].split(']')[0]
                    if roles_vacancies.get(chosen_role, 0) > 0:
                        roles_vacancies[chosen_role] -= 1
                        return f"{chosen_project}, {chosen_role}"

        elif row['CHOOSE PRECEDENCE OF ALLOCATION'] == 'ROLE':
            project_cols = [col for col in row.index if 'PROJECT PRIORITY' in col]
            role_priorities = ['ROLE PRIORITY [ML]', 'ROLE PRIORITY [FRONTEND]',
                               'ROLE PRIORITY [BACKEND / APPDEV]', 'ROLE PRIORITY [CYSEC/ALGO]']

            for role in sorted(role_priorities, key=lambda x: row[x]):
                chosen_role = role.split('[')[1].split(']')[0]

                for project_col in sorted(project_cols, key=lambda x: row[x]):
                    chosen_project = project_col.split('[')[1].split(']')[0]
                    roles_vacancies = vacancy_data[chosen_project]

                    if roles_vacancies.get(chosen_role, 0) > 0:
                        roles_vacancies[chosen_role] -= 1
                        return f"{chosen_project}, {chosen_role}"

        return None
    except Exception as e:
        print(f"Error during allocation: {e}")
        return None

def main():
    # Read input CSV file
    df = read_input_file(input_file_path)

    if df is None:
        print("Error reading input file. Please check the file path and format.")
        return

    # Define vacancy data (replace this with your actual vacancy data)
    vacancy_data = defaultdict(lambda: defaultdict(int))
    vacancy_data.update({
        'SOCIAL MEDIA APP': {'ML': 3, 'FRONTEND': 5, 'BACKEND / APPDEV': 5, 'CYSEC/ALGO': 2},
        'GEN AI FOR STORIES': {'ML': 2, 'FRONTEND': 2, 'BACKEND / APPDEV': 1, 'CYSEC/ALGO': 0},
        'CODE VULNERABILITY': {'ML': 1, 'FRONTEND': 2, 'BACKEND / APPDEV': 2, 'CYSEC/ALGO': 5},
        'CODE OPTIMIZATION': {'ML': 1, 'FRONTEND': 1, 'BACKEND / APPDEV': 1, 'CYSEC/ALGO': 2},
        'CODE REVIEW ASSISTANT': {'ML': 1, 'FRONTEND': 1, 'BACKEND / APPDEV': 1, 'CYSEC/ALGO': 2}
    })

    # Apply allocation function to each row to determine project-role pair
    df['PROJECT_ROLE_PAIR'] = df.apply(lambda row: allocate_project_role_pair(row, vacancy_data), axis=1)

    # Filter out rows where allocation was not successful (e.g., due to all vacancies being filled)
    allocated_df = df.dropna(subset=['PROJECT_ROLE_PAIR'])

    # Write the DataFrame with allocated data to a new CSV file
    allocated_df.to_csv(output_file_path, index=False)
    print(f"Allocated data has been written to {output_file_path}.")

if __name__ == "__main__":
    main()
