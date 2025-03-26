import time
import pandas as pd
import os
import ast
from datetime import datetime


def initialize_excel_file(excel_file_path):
    # Initialize the Excel file with the required columns if not already present
    if not os.path.exists(excel_file_path):
        df_empty = pd.DataFrame(columns=["Ports", "Parameter", "Min", "Mid", "Max","Worstcase"])
        df_empty.to_excel(excel_file_path, index=False)
        print(f"Initialized Excel file with columns: {excel_file_path}")
    else:
        print(f"Excel file already exists: {excel_file_path}")

def initialize_excel_inter_file(excel_file_path):
    # Initialize the Excel file with the required columns if not already present
    if not os.path.exists(excel_file_path):
        columns = ["Ports", "Parameter"]
        with open("text.txt", 'r') as file:
            con = file.read()
        data = ast.literal_eval(con)  # Parse data from the file
        res = [item[1] for item in data]
        for i in res:
            columns.append(i)
        df_empty = pd.DataFrame(columns)
        df_empty.to_excel(excel_file_path, index=False)
        print(f"Initialized Excel file with columns: {excel_file_path}")
    else:
        print(f"Excel file already exists: {excel_file_path}")



def extract_and_append_data(file_path, excel_file_path, column_to_update, port_name):
    # Read the content from the file
    print(file_path)
    time.sleep(10)
    with open(file_path, 'r') as file:
        content = file.readlines()

    print(f"Processing file: {file_path}")
    print("File content:")
    print(content)  # Check the content for debugging

    # Read the Excel file if it exists
    if os.path.exists(excel_file_path):
        df_existing = pd.read_excel(excel_file_path)
    else:
        df_existing = pd.DataFrame(columns=["Ports", "Parameter", "Min", "Mid", "Max","Worstcase"])

    # Process each trace in the input file
    r_values = {
        port_name: {'S11': None, 'S12': None, 'S22': None}
    }

    # Variables to track the trace and its corresponding parameter
    current_trc = None
    current_sparam = None

    # Process the file content to extract M3 values
    for line in content:
        print(f"Processing line: {line}")

        # Set the current trace (R1, R2, R3) based on the trace name (Trc1, Trc2, Trc3)
        if 'Trc1' in line:
            current_trc = port_name
            current_sparam = 'S11'  # Trc1 corresponds to S11
        elif 'Trc2' in line:
            current_trc = port_name
            current_sparam = 'S12'  # Trc2 corresponds to S12
        elif 'Trc3' in line:
            current_trc = port_name
            current_sparam = 'S22'  # Trc3 corresponds to S22

        # Extract M3 values and assign to corresponding trace
        if 'M3' in line:
            parts = line.split()  # Split the line into components
            print(f"Line split into parts: {parts}")

            m3_value = parts[-2]  # The M3 value is usually the second-to-last item
            print(f"Extracted M3 value: {m3_value}")

            # Assign the M3 value to the appropriate parameter (S11, S12, or S22)
            if current_trc == port_name:
                r_values[current_trc][current_sparam] = float(m3_value)

    # Print the r_values dictionary to check its content
    print("r_values dictionary:")
    print(r_values)

    # Update the DataFrame with new values or add new rows
    for trace, params in r_values.items():
        for param, m3_value in params.items():
            if m3_value is not None:
                # Check if the trace already exists in the DataFrame
                trace_row = df_existing[(df_existing["Ports"] == trace) & (df_existing["Parameter"] == param)]
                if not trace_row.empty:
                    # Update the existing row for the current trace and parameter
                    row_index = trace_row.index[0]
                    df_existing.at[row_index, column_to_update] = m3_value
                    print(f"Updated {trace} - {param} in the {column_to_update} column of the Excel file")
                else:
                    # Add a new row for the trace and parameter
                    new_row = {
                        "Ports": trace,
                        "Parameter": param,
                        "Min": None,
                        "Mid": None,
                        "Max": None,
                        "Worstcase": None
                    }
                    new_row[column_to_update] = m3_value
                    df_existing = pd.concat([df_existing, pd.DataFrame([new_row])], ignore_index=True)
                    print(f"Added new row for {trace} - {param} in the {column_to_update} column of the Excel file")

    # Ensure the directory for the Excel file exists
    excel_dir = os.path.dirname(excel_file_path)
    if not os.path.exists(excel_dir):
        os.makedirs(excel_dir)

    # Write the updated data back to the Excel file
    df_existing.to_excel(excel_file_path, index=False)


# def get_port_name_from_filename(filename,fold):
#     # Extract port name (e.g., R1 from R1_marker_min.txt)
#     print(f"filepath from vna.py {filename}")
#     print(f"folder directory from vna.py {fold}")
#     base_name = os.path.basename(filename)  # e.g., 'marker2585__min.txt'
#     port_name = base_name.split('_')[1]  # e.g., 'R1'

# # Path to the Excel file where data will be saved
# #     excel_file_path = os.path.join(fold,f"\\output.xlsx")

# # Initialize the Excel file before the loop starts
# #     if 'worstcase' not  in base_name.lower():
#     excel_file_path = os.path.join(fold, f"\\output.xlsx")
#     if os.path.exists(excel_file_path):
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         excelname = f"output_{timestamp}"
#         newexcelpath = os.path.join(fold,excelname)
#     else:
#         newexcelpath = os.path.join(fold,f"\\output.xlsx")
#     initialize_excel_file(newexcelpath)
#     # else:
#     #     excel_file_path = os.path.join(fold, f"\\output_worstcase.xlsx")
#     #     worstcase_excel_file(excel_file_path)


# # Loop through the text files and extract & append data
#     # Determine which column to update based on the file name
#     if 'min' in base_name.lower():
#         column_to_update = 'Min'
#     elif 'mid' in base_name.lower():
#         column_to_update = 'Mid'
#     elif 'max' in base_name.lower():
#         column_to_update = 'Max'
#     elif 'worstcase' in base_name.lower():
#         column_to_update = 'Worstcase'

#     # # to choose which file to append (out-excel or worstcase-excel)
#     # if column_to_update == 'new' :
#     #     worstcase(filename)
#     # else:
#     extract_and_append_data(filename, excel_file_path, column_to_update, port_name)

def get_port_name_from_filename(filename,fold,exc):
    # Extract port name (e.g., R1 from R1_marker_min.txt)
    print(f"filepath from vna.py {filename}")
    print(f"folder directory from vna.py {fold}")
    base_name = os.path.basename(filename)  # e.g., 'marker2585__min.txt'
    port_name = base_name.split('_')[1]  # e.g., 'R1'

# Path to the Excel file where data will be saved
#     excel_file_path = os.path.join(fold,f"\\output.xlsx")

# Initialize the Excel file before the loop starts
#     if 'worstcase' not  in base_name.lower():
    excel_file_path = os.path.join(exc, f"output.xlsx")
    initialize_excel_file(excel_file_path)
#     excel_file_path = os.path.join(fold, f"\\output.xlsx")
#     if os.path.exists(excel_file_path):
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         excelname = f"output_{timestamp}"
#         newexcelpath = os.path.join(fold,excelname)
#     else:
#         newexcelpath = os.path.join(fold,f"\\output.xlsx")
#     initialize_excel_file(newexcelpath)
    # else:
    #     excel_file_path = os.path.join(fold, f"\\output_worstcase.xlsx")
    #     worstcase_excel_file(excel_file_path)


# Loop through the text files and extract & append data
    # Determine which column to update based on the file name
    if 'min' in base_name.lower():
        column_to_update = 'Min'
    elif 'mid' in base_name.lower():
        column_to_update = 'Mid'
    elif 'max' in base_name.lower():
        column_to_update = 'Max'
    elif 'worstcase' in base_name.lower():
        column_to_update = 'Worstcase'

    # # to choose which file to append (out-excel or worstcase-excel)
    # if column_to_update == 'new' :
    #     worstcase(filename)
    # else:
    extract_and_append_data(filename, excel_file_path, column_to_update, port_name)
# def get_interband(filename,fold) :
#     print(f"filepath from vna.py {filename}")
#     print(f"folder directory from vna.py {fold}")
#     base_name = os.path.basename(filename)  # e.g., 'marker2585__min.txt'
#     port_name = base_name.split('_')[1]  # e.g., 'R1'
#
#     excel_file_path = os.path.join(fold, f"\\interband.xlsx")
#     initialize_excel_inter_file(excel_file_path)