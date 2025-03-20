from PyPDF2 import PdfReader
import re
import json

pdf_path = "./ds_ant_4pages.pdf"  # Ensure the PDF is in the same folder

def parseDataSheet(path):
    reader = PdfReader(path)
    extracted_data = {}
    current_port = None
    frequency_values = []
    downtilt_values = []
    ports = []
    antenna_name = ''

    # Extract antenna name from the first page
    first_page_text = reader.pages[0].extract_text()
    if first_page_text:
        for line in first_page_text.split("\n"):
            if line.startswith("KRE"):
                antenna_name = line.strip()
                break

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
                        port = current_port.replace(",", "")
                        extracted_data[port] = {
                            "fR": {"min":min(frequency_values), "max": max(frequency_values)},
                            "tR": {"min": float(downtilt_values[0]), "max": float(downtilt_values[-1])}
                        }
                        ports.append(extracted_data)
                    
                    # Reset for the new port
                    current_port = match.group(2)
                    frequency_values = []
                    downtilt_values = []
                    extracted_data = {}

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
        current_port.replace(",", "")
        extracted_data[current_port] = {
                                    "fR": {"min":min(frequency_values), "max": max(frequency_values)},
                            "tR": {"min": float(downtilt_values[0]), "max": float(downtilt_values[-1])}
        }
        ports.append(extracted_data)
        extracted_data = {}

    # ports.sort()

    # return extracted data as a JSON file
    return {"name": "24242", "ports": ports}