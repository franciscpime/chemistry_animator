# Technical Decisions

## 1. Overview

This document records the technical and architectural decisions made during the development of Chemistry Animator.

Its purpose is to preserve the reasoning behind important implementation choices and provide a reference for future development.

Each decision includes:

- Context
- Decision
- Rationale
- Consequences
- Status

Decisions may be revised as the project evolves.

---

## ADR-001, Python as the Main Programming Language

**Status:** Accepted

### Context

Chemistry Animator requires a programming language capable of processing chemical equations, performing mathematical calculations, and generating animations.

### Decision

Python is the primary programming language.

### Rationale

Python provides:

- Support for object-oriented programming.
- Built-in libraries for text processing.
- Scientific and mathematical computing libraries.
- Compatibility with Manim.
- A large ecosystem of testing and development tools.

### Consequences

The application can integrate chemical processing and animation generation within the same programming language.

External dependencies must be managed to ensure reproducibility.

---

## ADR-002, Manim as the Animation Framework

**Status:** Accepted

### Context

The application must generate animations explaining how chemical equations are balanced.

### Decision

Use Manim as the animation framework.

### Rationale

Manim supports:

- Mathematical expressions.
- Text and formula animations.
- Transformations between visual objects.
- Programmatic control of animation sequences.
- Video rendering.

### Consequences

Animations can be generated directly from Python code.

The project requires a correctly configured Manim environment.

---

## ADR-003, Object-Oriented Equation Parser

**Status:** Implemented, Subject to Refinement

### Context

Chemical equation processing involves several related operations:

- Separating reactants and products.
- Identifying individual chemical formulas.
- Extracting elements and quantities.
- Calculating total atom counts.

### Decision

Organize these operations within a Python class named `Equation_Parser`.

### Current Implementation

The class contains the following methods:

```python
divide_equation()
divide_reagents()
divide_products()
count_elements()
table()
```

The parser stores intermediate results using instance attributes.

Examples:

```python
self.reagents
self.products
self.reagents_no_plus
self.products_no_plus
self.total_reagents
self.total_products
```

### Rationale

Using a class allows related operations and their intermediate data to be grouped together.

### Consequences

The parser can preserve information between method calls.

However, the current implementation depends on certain methods being executed in the correct order.

This dependency should be reviewed as the parser becomes more complex.

---

## ADR-004, Regular Expressions for Initial Formula Parsing

**Status:** Implemented, Limited Scope

### Context

Chemical formulas contain recognizable patterns involving element symbols, coefficients, and subscripts.

### Decision

Use Python's built-in `re` module for initial chemical formula parsing.

### Current Implementation

Leading coefficients are extracted using:

```python
re.match(r"(\d*)(.*)", item)
```

Element symbols and subscripts are identified using:

```python
re.findall(r"([A-Z][a-z]?)(\d*)", formula)
```

### Rationale

Regular expressions provide a concise way to identify patterns in simple chemical formulas.

### Consequences

The current implementation can process formulas such as:

```text
H2O
CO2
NaCl
C6H12O6
```

However, the approach does not correctly handle grouped formulas such as:

```text
Ca(OH)2
Fe2(SO4)3
```

A more advanced parsing strategy may be required.

The current expressions also do not provide complete input validation.

---

## ADR-005, Counter for Atom Counting

**Status:** Accepted

### Context

The application must calculate the total number of atoms of each element on both sides of a chemical equation.

An element may appear multiple times across different chemical formulas.

### Decision

Use `Counter` from Python's `collections` module.

### Current Implementation

```python
self.total_reagents = Counter()
self.total_products = Counter()
```

Atom quantities are accumulated using:

```python
self.total_reagents[element] += coefficient * quantity
```

And:

```python
self.total_products[element] += coefficient * quantity
```

### Rationale

`Counter` provides a convenient structure for associating elements with numerical quantities.

It also supports incremental accumulation.

### Consequences

Atom counts can be stored in a structured format.

Example:

```python
Counter({"H": 4, "O": 2})
```

These results can later be used by the balancing and validation components.

---

## ADR-006, pandas for Tabular Representation

**Status:** Experimental

### Context

The application may benefit from presenting reactant and product atom counts in a structured table.

### Current Approach

The parser imports pandas and contains an initial `table()` method.

### Intended Use

Represent chemical element counts in a format suitable for inspection and comparison.

For example:

| Element | Reactants | Products |
|---|---:|---:|
| H | 4 | 4 |
| O | 2 | 2 |

### Considerations

pandas provides convenient tools for manipulating tabular data.

However, the application may not require pandas for basic atom counting.

The necessity of this dependency should be evaluated before the table implementation is finalized.

### Consequences

The project currently includes pandas as a dependency.

The table-generation functionality remains incomplete.

---

## ADR-007, Separation of Chemical Logic and Animation Logic

**Status:** Proposed

### Context

Chemical calculations and animation generation have different responsibilities.

The parser should be capable of processing equations independently of the animation framework.

### Proposed Decision

Keep chemical processing inside the `chemistry/` package.

Keep animation generation separate from chemical calculations.

### Intended Architecture

```text
Chemical Equation
       |
       v
Chemical Parser
       |
       v
Equation Balancer
       |
       v
Validation
       |
       v
Manim Animation
```

### Expected Benefits

- Easier unit testing.
- Reduced coupling between components.
- Improved maintainability.
- Possibility of reusing chemical processing independently of Manim.

### Current Limitation

The parser currently contains:

```python
from main import *
```

This creates an unnecessary dependency on the application's entry point.

The dependency should be removed when the module structure is refined.

---

## ADR-008, Incremental Development

**Status:** Adopted

### Context

Chemistry Animator combines multiple technical areas:

- Chemical formula parsing.
- Mathematical equation balancing.
- Input validation.
- Animation generation.

Developing all components simultaneously would make debugging and testing more difficult.

### Approach

Develop the application incrementally.

The planned sequence is:

1. Chemical equation parsing.
2. Automatic balancing.
3. Balancing validation.
4. Basic Manim animations.
5. Step-by-step educational animations.
6. Integration and release preparation.

### Rationale

Incremental development allows individual components to be tested before integration.

### Consequences

The application will remain partially functional during early development stages.

Documentation must distinguish implemented features from planned features.

---

## 2. Pending Technical Decisions

The following decisions have not yet been finalized:

| ID | Topic | Status |
|---|---|---|
| TBD-001 | Parsing nested chemical formulas | Pending |
| TBD-002 | Automatic balancing algorithm | Pending |
| TBD-003 | Representation of chemical compounds | Pending |
| TBD-004 | Error handling strategy | Pending |
| TBD-005 | Automated testing framework | Pending |
| TBD-006 | Animation step representation | Pending |
| TBD-007 | User input interface | Pending |

These decisions should be documented when their respective components are designed or implemented.

---

## 3. Decision Management

When a significant technical decision is made:

1. Create a new ADR entry.
2. Describe the problem or context.
3. Record the selected approach.
4. Explain the reasoning.
5. Identify relevant limitations and consequences.
6. Update the status if the decision changes.

Previous decisions should remain documented to preserve the project's technical history.

---

**Document Status:** Initial technical decision register.

**Last Updated:** 14 October 2026.