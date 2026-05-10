import numpy as np
import streamlit as st

st.title("🚦 Traffic Flow Analyzer (Numerical Methods)")

st.write("Enter traffic equations in matrix form (Ax = b):")

n = st.number_input("Number of roads (variables):", min_value=2, max_value=10, step=1)

A = []
b = []

for i in range(n):
    row = st.text_input(f"Equation {i+1} coefficients (space-separated):")
    if row:
        A.append(list(map(float, row.split())))
    val = st.number_input(f"Constant term b[{i+1}]:", value=0.0)
    b.append(val)

method = st.selectbox("Choose method:", ["Gauss Elimination", "Jacobi", "Gauss-Seidel"])

if st.button("Solve"):
    A = np.array(A)
    b = np.array(b)

    if method == "Gauss Elimination":
        x = np.linalg.solve(A, b)
        st.success(f"Solution (flows): {x}")

    elif method == "Jacobi":
        x = np.zeros_like(b)
        for _ in range(50):  # 50 iterations
            x_new = np.copy(x)
            for i in range(n):
                s = sum(A[i][j] * x[j] for j in range(n) if j != i)
                x_new[i] = (b[i] - s) / A[i][i]
            x = x_new
        st.success(f"Jacobi Approximation: {x}")

    elif method == "Gauss-Seidel":
        x = np.zeros_like(b)
        for _ in range(50):
            for i in range(n):
                s = sum(A[i][j] * x[j] for j in range(n) if j != i)
                x[i] = (b[i] - s) / A[i][i]
        st.success(f"Gauss-Seidel Approximation: {x}")
