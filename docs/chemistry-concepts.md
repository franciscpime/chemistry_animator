# Chemistry Concepts

## 1. Overview

Chemistry Animator is designed to automatically balance chemical equations and generate step-by-step educational animations using Manim.

To ensure accurate results, the application must follow fundamental chemical principles, particularly the law of conservation of mass.

This document describes the chemical concepts relevant to the application's development.

---

## 2. Chemical Equations

A chemical equation represents a chemical reaction using chemical formulas.

A typical equation contains:

- Reactants
- Products
- A reaction arrow
- Chemical elements
- Subscripts
- Stoichiometric coefficients

### Example

```text
H2 + O2 -> H2O
```

In this equation:

**Reactants:**
- H2, Hydrogen
- O2, Oxygen

**Product:**
- H2O, Water

The arrow (`->`) separates reactants from products.

The plus sign (`+`) separates individual chemical species.

This equation is not balanced because the number of oxygen atoms differs between the two sides.

---

## 3. Chemical Elements

Chemical elements are represented by symbols consisting of one or two letters in the currently recognized periodic table.

The first letter is always uppercase.

If a second letter exists, it must be lowercase.

### Examples

| Symbol | Element |
|---|---|
| H | Hydrogen |
| O | Oxygen |
| C | Carbon |
| N | Nitrogen |
| Na | Sodium |
| Cl | Chlorine |
| Fe | Iron |
| Ca | Calcium |
| Mg | Magnesium |

### Programming Considerations

The parser must distinguish between uppercase and lowercase letters.

For example:

```text
NaCl
```

Contains two elements:

```text
Na
Cl
```

It must not be interpreted as four individual letters.

The current parser uses the following regular expression:

```python
r"([A-Z][a-z]?)(\d*)"
```

This expression identifies candidate element symbols and their optional subscripts.

However, it does not verify whether the identified symbols correspond to real chemical elements.

---

## 4. Chemical Subscripts

Subscripts indicate the number of atoms of an element within a chemical formula.

### Example

```text
H2O
```

Contains:

| Element | Number of Atoms |
|---|---:|
| H | 2 |
| O | 1 |

When no subscript is provided, the quantity is assumed to be 1.

### Additional Example

```text
CO2
```

Contains:

| Element | Number of Atoms |
|---|---:|
| C | 1 |
| O | 2 |

### Programming Considerations

The parser must:

1. Identify each element.
2. Extract its subscript.
3. Assume a quantity of 1 when the subscript is absent.
4. Support multi-digit subscripts.

For example:

```text
C12H22O11
```

Contains:

```text
C: 12
H: 22
O: 11
```

---

## 5. Stoichiometric Coefficients

Coefficients indicate the relative number of chemical entities participating in a reaction.

They are written before chemical formulas.

### Example

```text
2H2O
```

The coefficient is:

```text
2
```

The formula is:

```text
H2O
```

Each water molecule contains:

```text
H: 2
O: 1
```

The coefficient multiplies the quantities of all atoms in the formula.

Therefore:

```text
2H2O
```

Represents:

```text
H: 4
O: 2
```

### General Rule

For an element in a simple formula:

```text
Total atoms = Coefficient × Subscript
```

If the element appears multiple times in a formula, its contributions must be added.

### Important Distinction

Consider:

```text
2H2O
```

And:

```text
H2O2
```

These expressions represent different chemical compositions.

**2H2O:**

```text
H: 4
O: 2
```

**H2O2:**

```text
H: 2
O: 2
```

Changing a coefficient changes the quantity of a chemical species.

Changing a subscript changes its chemical formula and potentially its identity.

Therefore, chemical equation balancing must modify coefficients, not subscripts.

---

## 6. Law of Conservation of Mass

The law of conservation of mass states that mass is conserved during a chemical reaction in a closed system.

In ordinary chemical reactions, atoms are rearranged rather than created or destroyed.

Therefore, a correctly balanced chemical equation must contain the same number of atoms of each element on both sides.

### Example

Unbalanced equation:

```text
H2 + O2 -> H2O
```

Atom counts:

| Element | Reactants | Products |
|---|---:|---:|
| H | 2 | 2 |
| O | 2 | 1 |

Oxygen is not balanced.

Balanced equation:

```text
2H2 + O2 -> 2H2O
```

Atom counts:

| Element | Reactants | Products |
|---|---:|---:|
| H | 4 | 4 |
| O | 2 | 2 |

Both elements are now balanced.

---

## 7. Chemical Equation Balancing

Balancing a chemical equation consists of finding coefficients that make the number of atoms of each element equal on both sides.

### Example

Initial equation:

```text
Fe + O2 -> Fe2O3
```

Balanced equation:

```text
4Fe + 3O2 -> 2Fe2O3
```

Verification:

| Element | Reactants | Products |
|---|---:|---:|
| Fe | 4 | 4 |
| O | 6 | 6 |

The coefficients are:

```text
4, 3, 2
```

These coefficients represent the smallest positive integer ratio satisfying the atom-conservation constraints.

### Balancing Rules

1. Chemical formulas must remain unchanged.
2. Only stoichiometric coefficients may be adjusted.
3. Every element must have equal atom counts on both sides.
4. The final coefficients should be expressed as the smallest positive integers satisfying the balancing constraints.

---

## 8. Polyatomic Groups

Some chemical formulas contain groups of atoms enclosed in parentheses.

A subscript following a group multiplies the number of atoms of every element inside that group.

### Example

```text
Ca(OH)2
```

Contains:

```text
Ca: 1
O: 2
H: 2
```

The subscript `2` applies to both oxygen and hydrogen.

### Additional Example

```text
Fe2(SO4)3
```

Contains:

```text
Fe: 2
S: 3
O: 12
```

Explanation:

- Fe has a subscript of 2.
- The SO4 group is repeated 3 times.
- S: 1 × 3 = 3.
- O: 4 × 3 = 12.

### Programming Considerations

The parser must eventually support:

- Parentheses.
- Group multipliers.
- Nested groups.
- Multiple occurrences of the same element.

The current parser does not correctly interpret grouped formulas.

---

## 9. Multiple Occurrences of an Element

An element may appear more than once within the same chemical formula.

### Example

```text
CH3COOH
```

The formula contains:

```text
C: 2
H: 4
O: 2
```

The parser must accumulate all occurrences of the same element.

Python's `Counter` can be used to store these totals.

Example:

```python
Counter({"C": 2, "H": 4, "O": 2})
```

---

## 10. Mathematical Representation of Balancing

Chemical equation balancing can be represented as a system of linear equations.

Consider:

```text
aH2 + bO2 -> cH2O
```

Where:

- a represents the coefficient of H2.
- b represents the coefficient of O2.
- c represents the coefficient of H2O.

### Hydrogen Conservation

```text
2a = 2c
```

### Oxygen Conservation

```text
2b = c
```

A smallest positive integer solution is:

```text
a = 2
b = 1
c = 2
```

Therefore:

```text
2H2 + O2 -> 2H2O
```

This mathematical approach can be generalized to more complex equations.

### Programming Considerations

A future balancing algorithm may:

1. Identify all unique elements.
2. Construct a matrix representing atom counts.
3. Form a homogeneous linear system.
4. Calculate a valid solution.
5. Convert the solution into positive integer coefficients.
6. Reduce the coefficients to their smallest valid ratio.
7. Verify the final equation.

The exact balancing algorithm has not yet been selected or implemented.

---

## 11. Chemical Equation Validation

Before processing an equation, the application should verify that its notation is supported and structurally valid.

Potential validation checks include:

- Presence of a reaction arrow.
- Presence of reactants and products.
- Valid chemical element symbols.
- Valid coefficient and subscript values.
- Correctly matched parentheses.
- Absence of empty chemical formulas.
- Supported chemical notation.

### Example of Invalid Input

```text
H2++O2->H2O
```

The equation contains an empty chemical species between two plus signs.

Another example:

```text
Xx2+O2->XxO2
```

`Xx` is not a recognized chemical element symbol.

The parser should eventually detect these problems and return meaningful error messages.

---

## 12. Scope and Future Chemistry Support

The initial development focuses on conventional chemical equations involving neutral chemical species.

Advanced features may include:

- Ionic equations.
- Conservation of electrical charge.
- Hydrates.
- Reaction states.
- Reversible reactions.
- More complex chemical notation.

These features are outside the initial parser implementation.

---

## 13. Scientific Accuracy

Chemistry Animator must preserve the following principles:

1. Chemical element symbols must be interpreted correctly.
2. Subscripts must not be modified during balancing.
3. Coefficients must apply to complete chemical formulas.
4. Atom counts must be conserved.
5. Final balancing results must be mathematically verified.
6. Unsupported notation must not silently produce incorrect results.

These principles should guide the development of the parser, balancing algorithm, and validation system.

---

**Document Status:** Initial chemistry reference.

**Last Updated:** 14 October 2026.