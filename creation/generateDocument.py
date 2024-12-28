import pandas as pd

# Load the CSV file
data = pd.read_csv("data.csv")

# Initialize the Quarto .qmd content
qmd_content = r"""---
title: ""
format: pdf
output-file: NativityCatalog.pdf
author: "Denise Daniel"
fontsize: 14pt
line-spacing: 2
---

\thispagestyle{empty}

\begin{center}
\vspace*{\fill}
{\Huge \bfseries Nativities}
\vspace{2cm}

{\large A Catalog of Nativities}

\vspace*{\fill}
\end{center}
\newpage
\setcounter{page}{1}
"""


# Group columns by repeating headers (e.g., Q1.2_x, Q2.2_x)
nativity_count = len(data.columns) // 6  # Assuming 6 columns per nativity (adjust if needed)

# Initialize a list to track missing data
missing_data_summary = []

# Loop through each nativity
for i in range(nativity_count):
    base_col = i * 6  # Determine starting column for the current nativity
    name = data.iloc[1, base_col] if pd.notna(data.iloc[1, base_col]) else "Unknown Name"
    origin = data.iloc[1, base_col + 1] if pd.notna(data.iloc[1, base_col + 1]) else "Unknown Origin"
    year = data.iloc[1, base_col + 2] if pd.notna(data.iloc[1, base_col + 2]) else "Unknown Year"
    purchaser = data.iloc[1, base_col + 3] if pd.notna(data.iloc[1, base_col + 3]) else "Unknown Purchaser"
    notes = data.iloc[1, base_col + 4] if pd.notna(data.iloc[1, base_col + 4]) else ""
    materials = data.iloc[1, base_col + 5] if pd.notna(data.iloc[1, base_col + 5]) else "Unknown Materials"

    # Add details for the nativity
    qmd_content += f"""
# {name}

![](photos/Natvity_ - {i + 1}.jpeg)

\\

**Origin:** {origin}

**Year:** {year}

**Purchaser:** {purchaser}

**Material(s):** {materials}

{notes}
"""

 # Track missing data
    if name == "*****Unknown Name*****":
        missing_data_summary.append(f"Nativity {i + 1}: Missing Name")
    if origin == "******Unknown Origin*****":
        missing_data_summary.append(f"Nativity {i + 1}: Missing Origin")
    if year == "Unknown Year":
        missing_data_summary.append(f"Nativity {i + 1}: Missing Year")
    if purchaser == "Unknown Purchaser":
        missing_data_summary.append(f"Nativity {i + 1}: Missing Purchaser")
    if materials == "Unknown Materials":
        missing_data_summary.append(f"Nativity {i + 1}: Missing Materials")

# Append missing data summary to the Quarto content
if missing_data_summary:
    qmd_content += "\n# Missing Data Summary\n\n"
    qmd_content += "\n".join(f"- {item}" for item in missing_data_summary)
else:
    qmd_content += "\n# Missing Data Summary\n\n- No missing data found."


# Save the Quarto .qmd file
output_file = "nativities.qmd"
with open(output_file, "w") as file:
    file.write(qmd_content)

print(f"Quarto .qmd file created successfully: {output_file}")
