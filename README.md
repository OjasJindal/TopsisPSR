# Topsis-Ojas-102317056

A Python package for performing TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) analysis on multi-criteria decision-making problems.

**Author:** Ojas Jindal  
**Roll Number:** 102317056

## What is TOPSIS?

TOPSIS is a multi-criteria decision analysis method that helps in selecting the best alternative from a set of alternatives based on multiple criteria. It works by finding the alternative that is closest to the ideal solution and farthest from the negative-ideal solution.

## Installation

```bash
pip install Topsis-Ojas-102317056
Usage
Command Line Interface
After installation, you can use the topsis command directly from the command line:

topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
Example
topsis data.csv "1,1,1,2" "+,+,-,+" output-result.csv
If the topsis command is not recognized, run:

python -m Topsis.topsis data.csv "1,1,1,2" "+,+,-,+" output-result.csv
Parameters
InputDataFile: CSV file containing the decision matrix

First column: alternatives

Remaining columns: numeric criteria values

Weights: comma-separated weights

Example: "1,1,1,2"

Impacts: comma-separated impacts

+ = benefit criterion

- = cost criterion

Example: "+,+,-,+"

OutputResultFileName: output file path

Input File Format
Alternative	C1	C2	C3	C4	C5
A1	0.67	0.45	6.5	42.6	12.56
A2	0.60	0.36	3.6	53.3	14.47
A3	0.79	0.61	6.4	63.1	17.84
Output File Format
The output file will include:

Topsis Score

Rank (1 = best)

Validation
The package checks for:

correct number of parameters

file existence

minimum 3 columns

numeric criteria values

matching weights & impacts count

valid impacts (+ or -)

Error Handling
Clear error messages are provided for:

missing parameters

file not found

non-numeric values

mismatch in weights/impacts

invalid impacts

Algorithm Steps
Normalize decision matrix

Apply weights

Determine ideal best & worst

Calculate distances

Compute TOPSIS score

Rank alternatives

License
MIT License

Author
Ojas Jindal
102317056
ojindal_be23@thapar.edu

PyPI
https://pypi.org/project/Topsis-Ojas-102317056/
