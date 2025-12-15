# DNA-RNA-Sequence-Processor
A comand line tool built using Bio-Python for analysis of DNA and RNA sequences.

## How It Works
This tool processes sequences from a FASTA file input and provides biological calculations such as:
 - **Sequence Conversion:** Converts DNA sequences to RNA (and vice versa).
 - **Reverse Complement:** Generates the reverse complementary sequence for both DNA and RNA.
 - **Translation:** Translates both DNA and RNA sequences into their corresponding protein sequences.
 - **Composition Analysis:** Calculates the GC-Content (the percentage of Guanine and Cytosine bases) for each input sequence.

## Usage
This project requires both `Python3` and `BioPython`.

**Running**
To run the program just run the script from the terminal along with the path to your FASTA file.
```
python sequence_processor.py <input_file.fasta>
```

**Output**
The script will print the results directly to the terminal.
