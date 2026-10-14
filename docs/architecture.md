# Software Architecture

## 1. Overview

Chemistry Animator is a Python application designed to automatically balance chemical equations and generate step-by-step animations using Manim.

The application is being developed with a modular architecture, separating chemical equation processing from animation generation.

**Current development phase:** Chemical Equation Parsing.

## 2. Project Architecture

The planned processing workflow is:

```text
Chemical Equation Input
          |
          v
    Equation Parser
          |
          v
   Element Counting
          |
          v
   Equation Balancer
          |
          v
  Balancing Validation
          |
          v
  Animation Generator
          |
          v
    Manim Animation
```

Only the initial parsing and element-counting components are currently implemented.

The balancing, validation, and animation stages are planned.

## 3. Project Structure

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

### main.py

**Status:** Initial structure.

Contains the initial Manim scene class, `Chemistry_Animator`.

The animation logic has not yet been implemented.

### chemistry/parser.py

**Status:** In development.

Contains the `Equation_Parser` class, responsible for processing chemical equations and extracting information about their chemical elements.

### chemistry/balancer.py

**Status:** Not implemented.

Reserved for the future chemical equation balancing algorithm.

## 4. Equation Parser

### Class: Equation_Parser

The `Equation_Parser` class currently uses instance attributes to store information extracted from chemical equations.

### 4.1 divide_equation()

**Purpose:** Separate reactants and products.

**Input:**

```python
"2H2 + O2 -> 2H2O"
```

**Internal representation:**

```python
self.reagents = "2H2+O2"
self.products = "2H2O"
```

The method removes spaces and separates the equation using `->`.

### 4.2 divide_reagents()

**Purpose:** Identify individual reactant formulas.

**Example:**

```python
"2H2+O2"
```

**Result:**

```python
self.reagents_no_plus = ["2H2", "O2"]
```

### 4.3 divide_products()

**Purpose:** Identify individual product formulas.

**Example:**

```python
"2H2O"
```

**Result:**

```python
self.products_no_plus = ["2H2O"]
```

### 4.4 count_elements()

**Purpose:** Calculate the total number of atoms of each chemical element on both sides of an equation.

The method uses:

- `re.match()` to separate leading coefficients from formulas.
- `re.findall()` to identify element symbols and subscripts.
- `Counter` to accumulate element quantities.

**Example equation:**

```text
2H2 + O2 -> 2H2O
```

**Reactant atom counts:**

```python
Counter({"H": 4, "O": 2})
```

**Product atom counts:**

```python
Counter({"H": 4, "O": 2})
```

The results are stored in:

```python
self.total_reagents
self.total_products
```

The current implementation supports simple formulas containing element symbols and optional numeric subscripts.

It does not correctly handle grouped formulas containing parentheses.

### 4.5 table()

**Status:** In development.

The intended purpose is to represent element counts in a structured pandas table.

The current implementation is incomplete.

## 5. Data Structures

The parser currently uses three main types of data structures.

### Strings

Used to represent chemical equations and individual formulas.

Example:

```python
"H2+O2->H2O"
```

### Lists

Used to store individual reactants and products.

Example:

```python
["H2", "O2"]
```

### Counter

Used to associate chemical elements with their total atom counts.

Example:

```python
Counter({"H": 4, "O": 2})
```

`Counter` is provided by Python's `collections` module.

## 6. Current Limitations

The following limitations have been identified:

1. Chemical formulas containing parentheses are not correctly interpreted.
2. Nested chemical groups are not supported.
3. Invalid chemical equations are not systematically detected.
4. The parser relies on methods being executed in the correct order.
5. The element-counting method currently receives arguments that it does not use.
6. The pandas table generation method is incomplete.
7. Chemical balancing has not yet been implemented.
8. The parser currently imports from `main.py`, creating an unnecessary dependency on the application entry point.

These limitations will be addressed during future development.

## 7. Planned Architecture

The long-term objective is to separate the application into independent components.

### Parser

Responsible for interpreting chemical equations and extracting structured chemical information.

### Balancer

Responsible for calculating the coefficients required to balance an equation.

### Validator

Responsible for verifying that the number of atoms of each element is equal on both sides.

### Animation Generator

Responsible for converting balancing operations into visual explanations using Manim.

This separation is intended to improve maintainability, testability, and code reuse.

## 8. Design Principles

The project aims to follow these principles:

**Modularity:** Each component should have a clearly defined responsibility.

**Separation of Concerns:** Chemical calculations should remain independent of animation logic.

**Testability:** Chemical processing should be verifiable without executing Manim.

**Maintainability:** Code should remain understandable and easy to extend.

**Extensibility:** New chemical formula structures and animation features should be supported without major architectural changes.

## 9. Future Improvements

Planned architectural improvements include:

- Introducing structured representations of chemical compounds.
- Supporting grouped chemical formulas.
- Implementing systematic input validation.
- Removing unnecessary dependencies between modules.
- Adding automated unit tests.
- Separating chemical balancing calculations from animation generation.

---

**Document Status:** Initial architecture documentation.

**Last Updated:** 14 October 2026.