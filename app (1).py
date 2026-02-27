import streamlit as st
from math_engine import compute_gcd, extended_euclidean, euclidean_steps
from ai_engine import generate_gcd_explanation

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

st.set_page_config(page_title="AI Number Theory Lab", layout="wide")

st.title("🏛 AI-Powered Number Theory & Cryptography Lab")

st.sidebar.title("Modules")

module = st.sidebar.selectbox(
    "Choose Module",
    [
        "Divisibility & Euclidean Lab",
        "Congruence & CRT Engine",
        "Prime & Pseudoprime Analyzer",
        "Crypto Sandbox"
    ]
)

if module == "Divisibility & Euclidean Lab":
    from math_engine import compute_gcd, extended_euclidean, euclidean_steps

    st.header("Divisibility & Euclidean Algorithm")

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input("Enter first integer (a)", step=1, value=252)

    with col2:
        b = st.number_input("Enter second integer (b)", step=1, value=198)

    if st.button("Compute GCD & Solve Diophantine Equation"):
        g = compute_gcd(a, b)
        g, x, y = extended_euclidean(a, b)
        steps = euclidean_steps(a, b)
        with st.expander("Show Euclidean Algorithm Steps", expanded=True):
            for step in steps:
                st.write(step)
        st.subheader("Results")
        st.markdown(f"### GCD({a}, {b}) = {g}")
        st.markdown(f"### Solution to {a}x + {b}y = {g}")
        st.markdown(f"**x = {x}, y = {y}**")
        st.success(f"Verification: {a}({x}) + {b}({y}) = {a*x + b*y}")
        if g == 1:
            inverse = x % b
            st.info(f"Modular Inverse of {a} mod {b} is {inverse}")
        else:
            st.warning(f"No modular inverse exists since gcd({a}, {b}) ≠ 1")
    st.markdown("---")
    st.header("Prime Factorization & Divisor Analysis")
    n_pf = st.number_input("Enter integer to factorize", step=1, value=360)
    def prime_factorization(n):
        factors = {}
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors[d] = factors.get(d, 0) + 1
                n //= d
                d += 1
        if n > 1:
            factors[n] = 1
            return factors
    if st.button("Factorize"):
        factors = prime_factorization(n_pf)
        st.subheader("Prime Factorization")
        factor_string = " × ".join([f"{p}^{e}" if e > 1 else f"{p}" for p, e in factors.items()])
        st.markdown(f"**{n_pf} = {factor_string}**")
        num_divisors = 1
        for e in factors.values():
            num_divisors *= (e + 1)
        st.info(f"Number of divisors: {num_divisors}")
        sum_divisors = 1
        for p, e in factors.items():
            sum_divisors *= (p**(e+1) - 1) // (p - 1)
        st.info(f"Sum of divisors: {sum_divisors}")
    st.markdown("---")
    st.header("LCM & GCD Relationship Explorer")
    a_lcm = st.number_input("Enter first integer", step=1, value=48, key="lcm_a")
    b_lcm = st.number_input("Enter second integer", step=1, value=180, key="lcm_b")
    if st.button("Compute LCM & Verify Identity"):
        g = compute_gcd(a_lcm, b_lcm)
        lcm = abs(a_lcm * b_lcm) // g
        st.subheader("Results")
        st.markdown(f"GCD({a_lcm}, {b_lcm}) = {g}")
        st.markdown(f"LCM({a_lcm}, {b_lcm}) = {lcm}")
        left = g * lcm
        right = a_lcm * b_lcm
        st.success(f"Verification: GCD × LCM = {left}")
        st.success(f"a × b = {right}")
    st.markdown("---")
    st.header("Divisibility & Division Algorithm Checker")
    a_div = st.number_input("Enter dividend (a)", step=1, value=100, key="div_a")
    b_div = st.number_input("Enter divisor (b)", step=1, value=7, key="div_b")
    if st.button("Check Divisibility"):
        if b_div == 0:
            st.error("Division by zero not allowed.")
    else:
        q = a_div // b_div
        r = a_div % b_div

        st.write(f"Quotient q = {q}")
        st.write(f"Remainder r = {r}")

        st.success(f"Verification: {a_div} = {b_div} × {q} + {r}")

        if r == 0:
            st.info(f"{b_div} divides {a_div}")
        else:
            st.warning(f"{b_div} does NOT divide {a_div}")
            
        
elif module == "Congruence & CRT Engine":
    st.header("Linear Congruence Solver")
    a_l = st.number_input("Enter coefficient a", step=1, value=7, key="lc_a")
    c_l = st.number_input("Enter RHS value c", step=1, value=1, key="lc_c")
    m_l = st.number_input("Enter modulus m", step=1, value=26, key="lc_m")
    if st.button("Solve ax ≡ c (mod m)"):
        g = compute_gcd(a_l, m_l)
        if c_l % g != 0:
            st.error("No solution exists because gcd(a, m) does not divide c.")
        else:
            a1 = a_l // g
            c1 = c_l // g
            m1 = m_l // g
            g_temp, x_temp, y_temp = extended_euclidean(a1, m1)
            solution = (x_temp * c1) % m1
            st.success(f"Solution: x ≡ {solution} (mod {m1})")
            st.markdown("---")
    st.header("Chinese Remainder Theorem Solver")
    a1 = st.number_input("Enter a₁", step=1, value=2, key="crt_a1")
    m1 = st.number_input("Enter modulus m₁", step=1, value=3, key="crt_m1")
    a2 = st.number_input("Enter a₂", step=1, value=3, key="crt_a2")
    m2 = st.number_input("Enter modulus m₂", step=1, value=5, key="crt_m2")
    if st.button("Solve CRT"):
        if compute_gcd(m1, m2) != 1:
            st.error("Moduli must be coprime for this simple CRT solver.")
        else:
            M = m1 * m2
            M1 = M // m1
            M2 = M // m2
            g1, y1, _ = extended_euclidean(M1, m1)
            g2, y2, _ = extended_euclidean(M2, m2)
            y1 = y1 % m1
            y2 = y2 % m2
            x = (a1 * M1 * y1 + a2 * M2 * y2) % M
            st.success(f"Solution: x ≡ {x} (mod {M})")
    st.markdown("---")
    st.header("Modular Inverse Engine")
    a_inv = st.number_input("Enter a", step=1, value=7, key="inv_a")
    m_inv = st.number_input("Enter modulus m", step=1, value=26, key="inv_m")
    if st.button("Compute Modular Inverse"):
        g, x, y = extended_euclidean(a_inv, m_inv)
        if g != 1:
            st.error(f"No inverse exists since gcd({a_inv}, {m_inv}) ≠ 1")
        else:
            inverse = x % m_inv
            st.success(f"Inverse of {a_inv} mod {m_inv} is {inverse}")
            st.info(f"Verification: ({a_inv} × {inverse}) mod {m_inv} = {(a_inv * inverse) % m_inv}")

elif module == "Prime & Pseudoprime Analyzer":
    st.header("Prime & Pseudoprime Analyzer")
    st.markdown("---")
    st.subheader("Prime Checker")
    n = st.number_input("Enter number to test", step=1, value=17)
    if st.button("Check Prime"):
        if is_prime(n):
            st.success(f"{n} is Prime")
        else:
            st.error(f"{n} is Composite")
    st.markdown("---")
    st.subheader("Fermat Pseudoprime Test")
    n_fermat = st.number_input("Enter number n", step=1, value=561, key="fermat_n")
    a = st.number_input("Enter base a", step=1, value=2, key="fermat_a")
    if st.button("Run Fermat Test"):
        if pow(a, n_fermat, n_fermat) == a:
            st.info(f"{n_fermat} passes Fermat test for base {a}")
        else:
            st.warning(f"{n_fermat} fails Fermat test for base {a}")
    
elif module == "Crypto Sandbox":
    st.header("RSA-style Encryption Lab")
    st.write("This module demonstrates RSA-style encryption.")
    st.markdown("---")
    st.header("Modular Exponentiation Playground")
    base = st.number_input("Enter base (a)", step=1, value=7, key="modexp_a")
    exp = st.number_input("Enter exponent (b)", step=1, value=128, key="modexp_b")
    mod = st.number_input("Enter modulus (m)", step=1, value=13, key="modexp_m")
    if st.button("Compute a^b mod m"):
        result = pow(base, exp, mod)
        st.success(f"{base}^{exp} ≡ {result} (mod {mod})")
    st.markdown("---")
    st.header("Mini RSA Lab")
    p = st.number_input("Enter prime p", step=1, value=11, key="rsa_p")
    q = st.number_input("Enter prime q", step=1, value=13, key="rsa_q")
    if st.button("Generate RSA Keys"):
        n = p * q
        phi = (p - 1) * (q - 1)
        st.write(f"n = {n}")
        st.write(f"φ(n) = {phi}")
        e = 7  # simple fixed public exponent
        if compute_gcd(e, phi) != 1:
            st.error("e is not coprime with φ(n). Choose different primes.")
        else:
            g, x, y = extended_euclidean(e, phi)
            d = x % phi
            st.success(f"Public Key: (e={e}, n={n})")
            st.success(f"Private Key: (d={d}, n={n})")
            message = st.number_input("Enter numeric message", step=1, value=9, key="rsa_msg")
            cipher = pow(message, e, n)
            st.write(f"Encrypted: {cipher}")
            decrypted = pow(cipher, d, n)
            st.write(f"Decrypted: {decrypted}")
    st.markdown("---")
    st.header("Fast Exponentiation (Square & Multiply)")
    a_f = st.number_input("Base", step=1, value=5, key="fast_a")
    b_f = st.number_input("Exponent", step=1, value=117, key="fast_b")
    m_f = st.number_input("Modulus", step=1, value=19, key="fast_m")
    if st.button("Show Steps"):
        result = 1
        base = a_f % m_f
        exponent = b_f
        st.write(f"Binary of exponent: {bin(exponent)}")
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % m_f
                st.write(f"Multiply → result = {result}")
            base = (base * base) % m_f
            exponent //= 2
            st.write(f"Square → base = {base}")
        st.success(f"Final Result: {result}")