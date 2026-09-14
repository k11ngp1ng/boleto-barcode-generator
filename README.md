# Brazilian Boleto Barcode Generator

A Python utility that converts Brazilian boleto payment lines (`linha digitável`) into **ITF (Interleaved 2 of 5) barcodes** and generates a print-ready PDF document.

The project demonstrates data parsing and transformation, barcode generation, input normalization, and automated PDF creation using Python.

## Features

- Reads boleto payment lines from a text file
- Removes punctuation and normalizes input data
- Converts 47-digit boleto payment lines into 44-digit barcode representations
- Preserves valid 44-digit barcode inputs after normalization
- Generates barcodes using the ITF (Interleaved 2 of 5) standard
- Organizes multiple generated barcodes into a single PDF document
- Provides a simple file-based input and output workflow

## Tech Stack

- Python
- python-barcode
- ReportLab

## How It Works

The application follows a simple processing pipeline:

```text
boletos.txt
     │
     ▼
Read payment lines
     │
     ▼
Normalize input
     │
     ▼
Convert 47-digit payment line
to 44-digit barcode format
     │
     ▼
Generate ITF barcode
     │
     ▼
Generate PDF
     │
     ▼
codigos_de_barras.pdf
```

For standard 47-digit boleto payment lines, the script rearranges the required fields to produce the corresponding 44-digit barcode representation.

Inputs that already contain 44 digits are preserved after normalization.

## Getting Started

### Prerequisites

Make sure Python is installed on your system.

Check your installation with:

```bash
python --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/k11ngp1ng/boleto-barcode-generator.git
cd boleto-barcode-generator
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install "python-barcode[images]" reportlab
```

### 4. Add Input Data

Add one boleto payment line per line to:

```text
boletos.txt
```

Example structure:

```text
<boleto-payment-line>
<boleto-payment-line>
<boleto-payment-line>
```

Use test data or information that you are authorized to process.

### 5. Run the Generator

```bash
python gerar_codigos.py
```

After execution, the generated PDF will be available at:

```text
codigos_de_barras.pdf
```

## Project Structure

```text
boleto-barcode-generator/
├── gerar_codigos.py
├── boletos.txt
├── codigos_de_barras.pdf
└── README.md
```

| File | Responsibility |
|---|---|
| `gerar_codigos.py` | Handles input processing, barcode conversion, image generation, and PDF creation |
| `boletos.txt` | Input file containing one boleto payment line per line |
| `codigos_de_barras.pdf` | Example generated PDF output |
| `README.md` | Project documentation |

## Boleto Conversion

Brazilian boletos commonly represent payment information using a human-readable payment line known as a `linha digitável`.

For supported 47-digit inputs, the script:

1. Removes formatting characters
2. Validates and normalizes the input
3. Rearranges the required fields
4. Produces the corresponding 44-digit barcode representation
5. Generates an ITF barcode from the resulting value

The generated barcode uses the **Interleaved 2 of 5 (ITF)** format commonly associated with numeric barcode representations.

## Input and Output

The application uses a straightforward file-based workflow:

```text
Input
└── boletos.txt

Processing
└── gerar_codigos.py

Output
└── codigos_de_barras.pdf
```

This makes the utility suitable for batch processing multiple boleto payment lines in a single execution.

## Limitations and Security

This project is intended primarily for **educational and demonstration purposes**.

- It does not replace official validation performed by banks or payment systems
- Generated barcodes should be validated before any operational use
- Only process test data or information you are authorized to use
- The project should not be considered a financial validation system
- Users are responsible for verifying generated output before use

## What I Learned

This project provided practical experience with:

- Python scripting
- String parsing and normalization
- Structured data transformation
- Barcode generation
- ITF barcode representation
- PDF generation with ReportLab
- File-based batch processing
- Input validation
- Building small automation utilities

## License

This project currently does not include a license.

Unless a license is added, the source code should not be assumed to be available for unrestricted reuse or redistribution.
