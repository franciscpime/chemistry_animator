# Chemistry Animator

**Chemistry Animator** is a Python-based application designed to automatically balance chemical equations and generate step-by-step educational animations using Manim.

The project aims to combine chemical equation processing with mathematical animations to visually demonstrate how chemical equations are balanced.

> **Development Status:** Early Development, Chemical Equation Parser

## Project Overview

The application is being developed to perform three main operations:

1. Parse chemical equations and identify reactants, products, elements, coefficients, and subscripts.
2. Automatically determine the coefficients required to balance chemical equations.
3. Generate educational animations using Manim to demonstrate the balancing process step by step.

The long-term objective is to transform a chemical equation into an animated explanation of its balancing process.

## Features

### Currently Implemented

- Separation of reactants and products.
- Identification of individual chemical compounds.
- Recognition of chemical element symbols using regular expressions.
- Recognition of coefficients and subscripts in simple chemical formulas.
- Calculation of total atom counts on each side of an equation for supported formulas.

### In Development

- Structured representation of chemical element counts.
- Improved chemical formula parsing.
- Handling invalid chemical equations.

### Planned Features

- Support for chemical formulas containing parentheses.
- Automatic chemical equation balancing.
- Verification of balanced equations.
- Step-by-step animations using Manim.
- Visual representation of balancing operations.

## Technologies

- **Python**: Main programming language.
- **Manim**: Mathematical animation engine.
- **Regular Expressions (`re`)**: Chemical formula parsing.
- **Collections (`Counter`)**: Element counting.
- **pandas**: Planned tabular representation of chemical data.

## Project Structure

```text
chemistry_animator/
├── main.py
├── chemistry/
│   ├── parser.py
│   └── balancer.py
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   ├── chemistry-concepts.md
│   ├── development-log.md
│   └── decisions.md
├── README.md
├── CHANGELOG.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Installation

### Prerequisites

- Python 3.13
- pip
- Manim and its system dependencies

### Clone the Repository

```bash
git clone https://github.com/franciscpime/chemistry_animator.git
cd chemistry_animator
```

### Install Dependencies

```bash
python3 -m pip install -r requirements.txt
```

> Ensure that the Python interpreter used to install the dependencies is the same interpreter used to run the application.

## Usage

The application is not yet available as a complete executable program.

Currently, the chemical equation parser is being developed and tested independently.

Automatic balancing and animation generation will be introduced in future development stages.

## Documentation

Additional technical documentation is available in the `docs/` directory.

- [Architecture](docs/architecture.md)
- [Development Roadmap](docs/roadmap.md)
- [Development Log](docs/development-log.md)
- [Chemistry Concepts](docs/chemistry-concepts.md)
- [Technical Decisions](docs/decisions.md)

## Development Status

**Current Phase:** Chemical Equation Parsing

The primary focus is implementing a reliable parser capable of extracting and counting chemical elements from chemical equations.

The next major development milestone is the automatic equation balancing algorithm.

## License

See the [LICENSE](LICENSE) file for licensing information.