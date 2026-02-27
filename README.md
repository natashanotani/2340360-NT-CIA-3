# 🧮 AI-Powered Number Theory & Cryptography Lab

An interactive Streamlit-based mathematical laboratory for exploring core concepts in Number Theory and Cryptography.

This project combines theoretical foundations with computational experimentation, allowing users to explore divisibility, congruences, primality testing, and RSA-style encryption in a structured modular environment.

---

## 🚀 Project Structure

The application is divided into four main modules:

---

# 🔎 1. Prime & Pseudoprime Analyzer

This module focuses on primality testing and understanding weaknesses in naive prime tests.

### Features

- **Prime Checker**
  - Deterministic trial division method
  - Checks primality up to √n

- **Fermat Pseudoprime Test**
  - Tests whether a number satisfies Fermat’s Little Theorem:
  
    \[
    a^{n-1} \equiv 1 \pmod{n}
    \]

  - Demonstrates how composite numbers can pass primality tests
  - Helps explore pseudoprimes

---

# 🔢 2. Divisibility & Euclidean Algorithm Lab

This module explores foundational tools of number theory related to divisibility and linear combinations.

### Features

- **Compute GCD & Solve Diophantine Equation**
  - Euclidean Algorithm
  - Extended Euclidean Algorithm
  - Finds integers x, y such that:
    
    \[
    ax + by = \gcd(a,b)
    \]

- **Prime Factorization & Divisor Analysis**
  - Displays prime decomposition
  - Computes number of divisors
  - Computes sum of divisors

- **LCM & GCD Relationship Explorer**
  - Verifies the identity:
    
    \[
    \gcd(a,b) \cdot \text{lcm}(a,b) = a \cdot b
    \]

- **Divisibility & Division Algorithm Checker**
  - Computes quotient and remainder
  - Verifies:
    
    \[
    a = bq + r
    \]

---

# 🔁 3. Congruence & CRT Engine

This module handles modular arithmetic and systems of congruences.

### Features

- **Linear Congruence Solver**
  - Solves:
    
    \[
    ax \equiv c \pmod{m}
    \]

  - Uses GCD conditions for existence of solutions

- **Chinese Remainder Theorem (CRT) Solver**
  - Solves systems of congruences:
    
    \[
    x \equiv a_1 \pmod{m_1}
    \]
    \[
    x \equiv a_2 \pmod{m_2}
    \]

  - Requires moduli to be coprime
  - Computes solution modulo \( m_1 m_2 \)

---

# 🔐 4. Crypto Sandbox

This module demonstrates how number theory powers modern cryptography.

### Features

- **Modular Exponentiation Playground**
  - Computes:
    
    \[
    a^b \mod m
    \]

  - Core operation in cryptographic systems

- **Mini RSA Lab**
  - Generates RSA keys using primes p and q
  - Computes:
    
    \[
    n = pq
    \]
    \[
    \varphi(n) = (p-1)(q-1)
    \]
  
  - Demonstrates encryption and decryption:
    
    \[
    c = m^e \mod n
    \]
    \[
    m = c^d \mod n
    \]

- **Fast Exponentiation (Square & Multiply)**
  - Step-by-step modular exponentiation
  - Demonstrates efficient computation used in cryptography

---

## 🧠 Educational Goals

This lab is designed to:

- Bridge theoretical number theory with computational experimentation
- Demonstrate how abstract mathematics powers cryptography
- Provide intuitive understanding of:
  - Divisibility
  - Modular arithmetic
  - Diophantine equations
  - RSA encryption

---

## 🛠 Tech Stack

- Python
- Streamlit
- Custom number theory engines (`math_engine`, etc.)

---

## ▶️ How to Run

```bash
streamlit run app.py
