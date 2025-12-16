import os, sys
from Bio import SeqIO
from Bio.Seq import Seq
from os.path import isfile
from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from Bio.SeqUtils import gc_fraction

## initalizations
console = Console()

## Functions
def ValidFile(filePath):
    valid_extensions = ['.fasta', '.fa', '.fna', '.fas']
    _, extension = os.path.splitext(filePath)

    if not os.path.isfile(filePath):
        console.print(f"[bold red]Error: [/bold red] [italic] file ({filePath}) could not be found.")
        return False
    if not extension.lower() in valid_extensions:
        console.print(f"[bold red]Error: [/bold red] [italic] file ({filePath}) does not have the correct extension (either .fasta, .fa, .fna or .fas)")
        return False
    else:
        return True

def AnalyzeFile(filePath):
    ## first row
    table = Table(title="FASTA File Contents Summary", show_header=True, header_style="bold magenta")
    table.add_column("Record ID", style="cyan", min_width=20)
    table.add_column("Type", style="yellow")
    table.add_column("Length (bp/nt)", style="green")
    table.add_column("GC Content", style="green")
    
    ## table population & output
    file_name = os.path.basename(filePath)
    record_count = 0
    
    try:
        for record in SeqIO.parse(filePath, "fasta"):
            record_count += 1
            
            seq_id = record.id             
            seq_length = len(record.seq)
            
            seq_string = str(record.seq).upper()
            if 'U' in seq_string and 'T' not in seq_string:
                seq_type = "RNA"
            elif 'A' in seq_string or 'T' in seq_string or 'G' in seq_string or 'C' in seq_string:
                seq_type = "DNA"
            else:
                seq_type = "Unknown"
            
            # second row
            table.add_row(seq_id, seq_type, f"{seq_length:,}", f"{gc_fraction(record.seq) * 100:.2f}") # Using f-string formatting for thousands comma
                
    except Exception as e:
        console.print(f"[bold red]FATAL PARSING ERROR:[/bold red] {e}")
        return

    console.print("\n")
    console.rule(f"[bold cyan]Analyzing ({file_name})[/bold cyan]")
    console.print(table)
    console.print(f"\n[bold yellow]Total Records Found:[/bold yellow] [bold white]{record_count}[/bold white]")

    ## console outputs
    ## console.rule(f"[bold cyan]Analyzing ({file_name}[/bold cyan])")

def DisplayHelpMenu():
    console.rule("[bold cyan]FASTA File Analyzer Tool[/bold cyan]")
    
    # Title
    console.print("A tool for quick genomic data summaries.", justify="center", style="italic yellow")
    console.print("\n")

    # Usage Panel
    usage_text = (f"python <sequence-analyzer> <path/to/file.fasta>")
    console.print(
        Panel(
            usage_text, 
            title="[bold green]Usage[/bold green]", 
            border_style="green", 
        ),
        justify="center"
    )
    console.print("\n")

    # args/options
    console.print("[bold magenta]Options:[/bold magenta]")
    console.print("* [cyan]<path/to/file.fasta>[/cyan]: The required path to your FASTA, FA, FNA, or FAS file.")
    console.print("* [cyan]-h / --help[/cyan]: Display this help menu.") 
    console.print("[bold blue]Note:[/bold blue]")
    console.print("* [cyan]Paths:[/cyan] Paths can be either absolute or relative.")
    console.print("\n")

    console.rule("[dim]Thank you for using the Analyzer![/dim]")

## Arguemnt Checking
if (len(sys.argv) < 2):
    error_message = Text("Error: ", style="bold red")
    error_message.append("No file path provided")
    console.print(error_message)

    console.print("[bold yellow]Usage:[/bold yellow] python sequence-analyzer.py <fasta_file_path>")
    console.print("[bold yellow]Help:[/bold yellow] for help use --h or --help")
    sys.exit(1)

if (len(sys.argv) >= 2):
    for path in range(len(sys.argv)-1):
        if ("--h" in sys.argv or "--help" in sys.argv):
            DisplayHelpMenu()
            continue
        if (ValidFile(sys.argv[path+1])):
            console.print(f"[bold green]Analyzing file:[/bold green] [italic blue] {sys.argv[path+1]} [/italic blue]")
            AnalyzeFile(sys.argv[path+1])


## Comment out to run tests in /test folder
### If running on windows change / to \ in test_file_directory
"""
test_file_directory = os.getcwd() + '/test-files'
test_files = os.listdir(test_file_directory)
for file in test_files:
    test_file_path = test_file_directory + "/" + file
    if (ValidFile(test_file_path)):
        AnalyzeFile(test_file_path)
"""
