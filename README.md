# DNA-RNA-Sequence-Processor
A comand line tool built using Bio-Python for analysis of DNA and RNA sequences.

## How It Works
This tool processes sequences from a FASTA file input and provides entry information such as:
 - **Record ID:** The record ID of each entry in the FASTA file.
 - **Record Type:** Identifies wheter the entry is DNA or RNA.
 - **Length:** Returns the length of each entries sequence.
 - **GC Content:** Calculates the GC-Content (the percentage of Guanine and Cytosine bases) for each input sequence.

## Usage
Make sure to install all of the packages required to run this program listed in requirements.txt

**Running:**
To run the program just run the script from the terminal along with the path to your FASTA file.
```
python sequence_processor.py <input_file1.fasta> <input_file2.fasta> <...>
```
Additionally you can run `--h` or `--help` instead of a .fasta file path for help

**Output:**
The script will print the results in a table to the terminal.
