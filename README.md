# Unit Converter

## Overview

**Unit Converter** is a simple and efficient tool for converting various units. Built with Python and Streamlit, it provides an easy-to-use interface for quick and accurate conversions.

## Features

- Convert between different units seamlessly
- User-friendly Streamlit web interface
- Lightweight and fast execution

## Requirements

Ensure you have Python **>=3.11** installed on your system.

### Dependencies

The project requires the following dependencies:

- `ruff>=0.9.10` (for linting)
- `streamlit>=1.43.1` (for building the web interface)

## Installation

Clone the repository and navigate into the project folder:

```sh
git clone https://github.com/Roohia-Bashir/unit_converter.git
cd unit-converter
```

Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

Install the dependencies:

```sh
pip install -r requirements.txt
```

Alternatively, install using `pyproject.toml`:

```sh
pip install .
```

## Usage

Run the unit converter application with:

```sh
unit-converter
```

This will launch the Streamlit application in your default web browser.

## Build & Development

To build the project:

```sh
pip install hatch
hatch build
```

## License

This project is licensed under the MIT License. Feel free to modify and distribute it.

## Contributing

Pull requests are welcome! Feel free to improve functionality, UI, or documentation.







