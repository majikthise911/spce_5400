import openpyxl
import sys

# Load the Excel template
wb = openpyxl.load_workbook('satellite-crosslink-analysis/templates/Laser Link Calculations template.xlsx')
ws = wb['Sheet1']

print("="*80)
print("LASER LINK CALCULATIONS TEMPLATE STRUCTURE")
print("="*80)
print()

# Read all non-empty rows
for row_idx, row in enumerate(ws.iter_rows(min_row=1, max_row=50, values_only=True), start=1):
    # Check if row has any non-None values
    if any(cell is not None for cell in row):
        # Format the row nicely
        row_str = f"Row {row_idx:2d}: "
        for col_idx, cell in enumerate(row[:10], start=1):  # First 10 columns
            if cell is not None:
                row_str += f"[{col_idx}:{cell}] "
        print(row_str)

print()
print("="*80)
print("KEY PARAMETERS TO MODIFY:")
print("="*80)
print("Looking for range (currently 1000 km) and data rate (currently 10 Gbps)...")
