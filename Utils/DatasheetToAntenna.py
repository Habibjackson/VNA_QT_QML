from PyPDF2 import PdfReader
import re
import json
import os

def parseDataSheet(path):
    print("/home/habib/Downloads/ds_ant_4pages.pdf" == path, path)
    reader = PdfReader("/home/habib/Downloads/ds_ant_4pages.pdf")
    extracted_data = {}
    current_port = None
    frequency_values = []
    downtilt_values = []
    antenna_name = ""
    allPorts = []

    # Extract antenna name from the first page
    first_page_text = reader.pages[0].extract_text()
    if first_page_text:
        for line in first_page_text.split("\n"):
            if line.startswith("KRE"):
                antenna_name = line.strip().replace("/", "-")
                break

    # Process each page
    for page in reader.pages:
        text = page.extract_text()
        if text:
            lines = text.split("\n")
            for i, line in enumerate(lines):
                # Detect lowband or midband and extract the next word as port name
                match = re.search(r"(lowband|midband)\s+(\S+)", line, re.IGNORECASE)
                if match:
                    # Save previous port data if available
                    if current_port and frequency_values and downtilt_values:
                        allPorts.append(current_port.replace(",", ""))
                        extracted_data[current_port.replace(",", "")] = {
                            "fR": {"min": min(frequency_values), "max": max(frequency_values)},
                            "tR": {"min": downtilt_values[0], "max": downtilt_values[-1]}
                        }

                    # Reset for the new port
                    current_port = match.group(2)
                    frequency_values = []
                    downtilt_values = []

                # Extract Frequency Range values (only min and max needed)
                if line.startswith("Frequency Range"):
                    numbers = [int(num) for num in re.findall(r"\d{3,4}", line)]  # Extract numeric values as integers
                    if numbers:
                        frequency_values.extend(numbers)

                # Extract Electrical Downtilt values
                elif line.startswith("Electrical Downtilt"):
                    if i + 1 < len(lines):
                        numbers = re.findall(r"\d+\.\d+", lines[i + 1])  # Extract decimal values
                        downtilt_values.extend(numbers)

    # Save the last port data
    if current_port and frequency_values and downtilt_values:
        allPorts.append(current_port)
        extracted_data[current_port] = {
            "fR": {"min": min(frequency_values), "max": max(frequency_values)},
            "tR": {"min": downtilt_values[0], "max": downtilt_values[-1]}
        }

    # Add antenna name at the beginning of JSON output
    final_output = {"name": antenna_name,"allPorts": allPorts, "ports": extracted_data}
    return final_output
