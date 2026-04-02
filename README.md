# TP53 GC Content Analyzer

## Project Overview

This project analyzes the GC content of the TP53 gene across different species (Human, Mouse, Rat) using Python.

## Data Source

Sequences were obtained from the NCBI database in FASTA format.

## Features

* Reads FASTA files
* Extracts sequence names and DNA sequences
* Calculates GC content
* Compares GC content across species
* Displays ranked results

## Tools Used

* Python
* NCBI database
* Clustal Omega (for sequence alignment)

## Results

Human TP53 showed the highest GC content (~62%), followed by mouse (~55%) and rat (~50%), indicating conserved but slightly varying genomic composition.

## How to Run

1. Place the FASTA file in the project folder
2. Run the script:

   ```
   python gc_analyzer.py
   ```

## Author

Vanshika Jain
