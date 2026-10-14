# Development Log

## 1. Overview

This document records the development progress of Chemistry Animator, including implemented functionality, technical challenges, solutions, and future tasks.

The purpose of this log is to maintain a chronological record of the project's evolution.

Unlike `CHANGELOG.md`, which focuses on software changes, this document also records development experiences, technical investigations, and lessons learned.

---

## 2. Development Timeline

### Initial Development, Project Setup and Chemical Equation Parser

**Period:** Before 14 October 2026  
**Status:** Completed and ongoing activities

#### Project Setup

The initial project structure was created to support Python development and future Manim animations.

The repository was organized into separate files for chemical processing, animation development, and documentation.

The main components include:

- `main.py`: Initial Manim application structure.
- `chemistry/parser.py`: Chemical equation parser.
- `chemistry/balancer.py`: Reserved for the balancing algorithm.
- `docs/`: Technical documentation.

The GitHub repository was also configured for version control.

#### Python Environment Configuration

The development environment was configured on macOS using Visual Studio Code.

Python 3.13 was selected as the interpreter for the project.

Manim was installed and configured for this Python installation.

**Challenges encountered:**

- Multiple Python installations were available on the system.
- The Homebrew Python interpreter did not contain the same packages as Python 3.13.
- Import errors occurred when using an interpreter without the required dependencies.
- The Python interpreter configuration needed to be checked after changes to the project directory.

**Lessons learned:**

Python packages are installed in specific Python environments.

Using the correct interpreter is essential for accessing project dependencies.

#### Chemical Equation Separation

The initial parser was implemented using a Python class named `Equation_Parser`.

The following methods were introduced:

```python
divide_equation()
divide_reagents()
divide_products()
```

These methods allow the application to:

- Separate reactants from products.
- Remove spaces from equation strings.
- Identify individual chemical formulas separated by plus signs.

**Example:**

```text
H2 + O2 -> H2O
```

The equation can be separated into:

```python
reagents = ["H2", "O2"]
products = ["H2O"]
```

#### Chemical Element Identification

The parser was extended to identify chemical elements and their quantities.

Initial approaches involved iterating through individual characters and identifying letters and digits separately.

This approach introduced difficulties when associating chemical elements with their respective subscripts.

For example:

```text
H2O
```

Contains two elements but only one explicitly written subscript.

The parser was subsequently improved using regular expressions.

#### Regular Expression Implementation

Python's `re` module was introduced to identify coefficients, chemical elements, and subscripts.

Leading coefficients are extracted using:

```python
re.match(r"(\d*)(.*)", item)
```

Element symbols and subscripts are extracted using:

```python
re.findall(r"([A-Z][a-z]?)(\d*)", formula)
```

This approach supports simple formulas containing:

- Single-letter element symbols.
- Two-letter element symbols.
- Optional numeric subscripts.
- Leading coefficients.

**Example:**

```text
2H2O
```

Can be separated into:

```text
Coefficient: 2
Formula: H2O
```

The formula can then be interpreted as:

```text
H: 2
O: 1
```

After applying the coefficient:

```text
H: 4
O: 2
```

#### Atom Counting

The `Counter` class from Python's `collections` module was introduced to accumulate atom quantities.

Two separate counters were implemented:

```python
self.total_reagents = Counter()
self.total_products = Counter()
```

This allows the parser to calculate the total number of atoms on each side of an equation.

**Example:**

```text
2H2 + O2 -> 2H2O
```

Expected results:

```text
Reactants:
H: 4
O: 2

Products:
H: 4
O: 2
```

#### Initial pandas Integration

The pandas library was introduced experimentally to represent chemical element counts in a structured table.

An initial `table()` method was created.

However, the implementation is incomplete and requires further development.

---

### 14 October 2026, Documentation and Project Organization

**Status:** In Progress

#### Work Completed

A documentation structure was established to improve the project's maintainability and long-term organization.

The following documents were prepared:

- `README.md`
- `docs/architecture.md`
- `docs/roadmap.md`
- `docs/chemistry-concepts.md`
- `docs/decisions.md`
- `docs/development-log.md`

The documentation distinguishes between implemented, incomplete, and planned functionality.

#### Technical Review

The existing parser implementation was reviewed.

The following limitations were identified:

1. Parentheses are not correctly interpreted.
2. Nested chemical groups are not supported.
3. Input validation is incomplete.
4. The `table()` method is unfinished.
5. Some method arguments are currently unused.
6. The parser contains an unnecessary import from `main.py`.
7. Automated tests have not yet been implemented.

#### Current Development Status

| Component | Status |
|---|---|
| Project setup | Completed |
| Initial Manim configuration | Completed |
| Equation separation | Implemented |
| Simple formula parsing | Implemented |
| Coefficient identification | Implemented |
| Subscript identification | Implemented |
| Atom counting | Implemented for simple formulas |
| pandas table | In progress |
| Input validation | Not implemented |
| Grouped formulas | Not implemented |
| Automatic balancing | Not implemented |
| Animation generation | Not implemented |
| Automated tests | Not implemented |

---

## 3. Current Technical Challenges

### 3.1 Chemical Formula Complexity

The current regular expressions cannot correctly interpret formulas containing parentheses.

Examples:

```text
Ca(OH)2
Fe2(SO4)3
```

A more advanced parsing strategy may be required.

### 3.2 Input Validation

The parser currently assumes that the input follows a supported structure.

Invalid or unsupported notation may produce incorrect results.

Input validation must be introduced before the parser is considered reliable.

### 3.3 Method Dependencies

The current parser stores intermediate results in instance attributes.

Some methods depend on attributes created by previously executed methods.

This requires methods to be called in a particular order.

The class design should be reviewed to improve reliability.

### 3.4 Structured Output

Atom counts are currently stored using `Counter`.

A structured representation suitable for comparison, balancing, and animation generation must be finalized.

---

## 4. Next Development Tasks

### Immediate Priorities

- [ ] Complete the atom-count comparison table.
- [ ] Review unnecessary imports.
- [ ] Improve method consistency.
- [ ] Introduce basic input validation.
- [ ] Add automated tests for simple chemical equations.

### Parser Improvements

- [ ] Support parentheses.
- [ ] Support nested chemical groups.
- [ ] Validate chemical element symbols.
- [ ] Detect unsupported notation.
- [ ] Improve error handling.

### Future Development

- [ ] Implement automatic equation balancing.
- [ ] Implement balancing validation.
- [ ] Integrate chemical processing with Manim.
- [ ] Generate step-by-step balancing animations.

---

## 5. Development Log Guidelines

Future entries should follow this structure:

### YYYY-MM-DD, Development Topic

**Status:** Completed / In Progress / Blocked

#### Objectives

Describe the intended work.

#### Work Completed

Document the functionality implemented or modified.

#### Problems Encountered

Describe technical difficulties or unexpected behavior.

#### Solutions

Explain how the problems were resolved.

#### Lessons Learned

Record relevant programming or scientific concepts learned.

#### Next Steps

Identify the next development activities.

---

## 6. Notes

This document should be updated regularly as the project evolves.

Entries should reflect actual development activities rather than planned functionality.

Significant architectural decisions should also be recorded in `docs/decisions.md`.

Software changes associated with releases should be summarized in `CHANGELOG.md`.

---

**Document Status:** Active development log.

**Last Updated:** 14 October 2026.