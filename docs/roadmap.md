# Development Roadmap

## 1. Project Vision

Chemistry Animator is a Python-based application designed to automatically balance chemical equations and generate step-by-step educational animations using Manim.

The development process is divided into milestones, allowing each component to be implemented, tested, and documented before progressing to the next stage.

## 2. Development Status

**Current Phase:** Version 0.1.0, Chemical Equation Parser

**Overall Status:** Early Development

The project currently focuses on interpreting chemical equations and calculating the number of atoms of each element.

The automatic balancing algorithm and animation system have not yet been implemented.

---

## 3. Version 0.1.0, Chemical Equation Parser

**Status:** In Progress

### Objective

Develop a reliable parser capable of interpreting chemical equations and extracting the information required for automatic balancing.

### Tasks

#### Equation Structure

- [x] Separate reactants and products using `->`.
- [x] Separate individual reactants using `+`.
- [x] Separate individual products using `+`.
- [x] Remove unnecessary spaces.

#### Chemical Formula Parsing

- [x] Identify chemical element symbols in simple formulas.
- [x] Recognize two-letter chemical symbols.
- [x] Identify numerical subscripts.
- [x] Identify leading coefficients.
- [x] Assume a coefficient of 1 when omitted.
- [x] Assume a subscript of 1 when omitted.
- [ ] Support formulas containing parentheses.
- [ ] Support nested chemical groups.
- [ ] Support multi-digit group multipliers.
- [ ] Validate chemical element symbols against the periodic table.

#### Atom Counting

- [x] Calculate atom quantities for simple chemical formulas.
- [x] Multiply atom quantities by molecular coefficients.
- [x] Accumulate atom counts using `Counter`.
- [x] Calculate reactant and product atom counts separately.
- [ ] Generate a structured table comparing both sides.
- [ ] Handle unsupported chemical notation explicitly.

#### Code Quality

- [ ] Remove unnecessary dependencies.
- [ ] Improve method organization.
- [ ] Implement systematic input validation.
- [ ] Add automated unit tests.
- [ ] Document public methods and expected inputs.

### Completion Criteria

Version 0.1.0 will be considered complete when:

1. The parser correctly interprets all supported chemical formulas.
2. Coefficients and subscripts are handled correctly.
3. Grouped chemical formulas are supported.
4. Invalid or unsupported input produces clear errors.
5. Atom counts are returned in a structured format.
6. Automated tests cover the main parsing scenarios.

---

## 4. Version 0.2.0, Chemical Equation Balancer

**Status:** Planned

### Objective

Implement an algorithm capable of determining the coefficients required to balance chemical equations.

### Tasks

- [ ] Compare atom counts between reactants and products.
- [ ] Identify unbalanced elements.
- [ ] Represent balancing constraints mathematically.
- [ ] Implement an automatic balancing algorithm.
- [ ] Calculate integer coefficients.
- [ ] Reduce coefficients to their smallest valid integer ratio.
- [ ] Handle equations with multiple reactants and products.
- [ ] Detect equations that cannot be balanced under the supported model.
- [ ] Add automated balancing tests.

### Completion Criteria

Version 0.2.0 will be considered complete when the application can automatically balance supported chemical equations and verify the resulting coefficients.

---

## 5. Version 0.3.0, Balancing Validation

**Status:** Planned

### Objective

Implement an independent validation component to verify chemical equation balancing results.

### Tasks

- [ ] Recalculate atom counts after balancing.
- [ ] Compare reactant and product totals.
- [ ] Verify conservation of each chemical element.
- [ ] Detect invalid balancing results.
- [ ] Return structured validation results.
- [ ] Add automated validation tests.

### Completion Criteria

The validator must independently confirm that each supported balanced equation contains the same number of atoms of every element on both sides.

---

## 6. Version 0.4.0, Basic Manim Animations

**Status:** Planned

### Objective

Develop the first animations capable of displaying chemical equations and their balancing results.

### Tasks

- [ ] Display chemical equations using Manim.
- [ ] Visually distinguish reactants and products.
- [ ] Highlight chemical elements.
- [ ] Display coefficients and subscripts.
- [ ] Animate coefficient changes.
- [ ] Display atom counts.
- [ ] Render the final balanced equation.

### Completion Criteria

The application must generate a Manim animation displaying a supported chemical equation and its balanced form.

---

## 7. Version 0.5.0, Step-by-Step Educational Animations

**Status:** Planned

### Objective

Generate animations that explain the balancing process rather than displaying only the final result.

### Tasks

- [ ] Represent the balancing process as individual steps.
- [ ] Highlight elements being balanced.
- [ ] Show atom counts before and after each operation.
- [ ] Animate coefficient adjustments.
- [ ] Explain how each adjustment affects the equation.
- [ ] Display the final verification.
- [ ] Improve animation timing and readability.

### Completion Criteria

The application must generate an animation demonstrating a coherent sequence of balancing operations for supported equations.

---

## 8. Version 1.0.0, First Complete Release

**Status:** Planned

### Objective

Deliver a functional application that integrates chemical equation parsing, automatic balancing, validation, and animation generation.

### Requirements

- [ ] Accept chemical equations as input.
- [ ] Parse supported chemical formulas.
- [ ] Automatically balance equations.
- [ ] Validate balancing results.
- [ ] Generate step-by-step Manim animations.
- [ ] Handle invalid input gracefully.
- [ ] Provide installation and usage instructions.
- [ ] Include automated tests.
- [ ] Provide complete technical documentation.

### Completion Criteria

Version 1.0.0 will be considered complete when a user can provide a supported chemical equation and receive a rendered animation explaining its balancing process.

---

## 9. Future Development

Potential improvements beyond version 1.0.0 include:

- Support for more advanced chemical notation.
- Ionic equations and charge conservation.
- Additional balancing methods.
- Customizable animation styles.
- Export options for educational content.
- A graphical user interface.
- Interactive equation input.

These features are exploratory and are not part of the initial release requirements.

---

## 10. Development Principles

The project follows an incremental development approach.

Each milestone should prioritize:

1. Correctness of chemical calculations.
2. Clear separation between application components.
3. Automated testing.
4. Maintainable Python code.
5. Accurate documentation.
6. Reliable animation generation.

Features should be considered complete only after implementation and appropriate testing.

---

**Document Status:** Initial development roadmap.

**Last Updated:** 14 October 2026.