# Changelog

All notable changes to Chemistry Animator will be documented in this file.

This project follows the principles of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and intends to use [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Initial project structure.
- Initial Manim scene structure in `main.py`.
- `Equation_Parser` class for chemical equation processing.
- Separation of reactants and products.
- Separation of individual chemical formulas.
- Recognition of chemical element symbols using regular expressions.
- Recognition of leading stoichiometric coefficients.
- Recognition of numerical subscripts.
- Atom counting for simple chemical formulas using `Counter`.
- Separate atom counters for reactants and products.
- Initial experimental pandas integration.
- Initial project documentation:
  - `README.md`
  - `docs/architecture.md`
  - `docs/roadmap.md`
  - `docs/chemistry-concepts.md`
  - `docs/decisions.md`
  - `docs/development-log.md`

### Known Limitations

- Chemical formulas containing parentheses are not correctly supported.
- Nested chemical groups are not supported.
- Chemical element symbols are not validated against the periodic table.
- Input validation is incomplete.
- The pandas table-generation method is incomplete.
- Automatic chemical equation balancing is not implemented.
- Manim animation generation is not implemented.
- Automated tests have not yet been implemented.

---

## Version History

No official versions have been released yet.

The first planned milestone is version `0.1.0`, focused on chemical equation parsing.