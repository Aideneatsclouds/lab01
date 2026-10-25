# SECB3203 Lab 1 - Python fundamentals and a reproducible project

Student: Yaaswiny Abbiramavally Thinaharan , A24CS0213

## Setup

**Windows (PowerShell):**
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt 
```

## Run
```# Run the test suite (visible and custom tests)
python -m pytest

# Run the code style check
ruff check src

# Generate the environment report
python src/env_check.py > results/environment_report.txt
```

## What is in this repository
src/: Contains the core Python implementation modules (env_check.py and basics.py).

tests/: Contains the unit test suite, including both provided visible tests and custom tests.

data/: Contains input data files used for records and analysis.

results/: Stores generated output files like the environment report text file.

src/env_check.py: Module that inspects and reports Python version, operating system, and installed package versions.

src/basics.py: Module containing core bioinformatics calculations and string parsing functions (gc_percent, format_report, parse_counts).

tests/test_visible.py: Provided test suite validating core lab specifications.

tests/test_lab01_own.py: Custom student-created tests covering boundary cases, zero totals, and invalid inputs.

README.md: Project documentation, setup instructions, and repository structure.

AI_USE_LOG.md: Log detailing AI tool interactions and usage across project tasks.

requirements.txt / requirements-frozen.txt: Project dependency lists and locked package versions.

## What is not committed, and why
The .venv/ and results/ folders are ignored because they contain machine-specific files and generated outputs. These files should be created locally on each computer rather than being shared through Git.
'@
Set-Content -Path "README.md" -Value $content -Encoding UTF8
