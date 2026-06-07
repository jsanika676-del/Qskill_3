import numpy as np

# Function to input a matrix
def input_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))

    print(f"Enter elements of Matrix {name} row-wise:")

    matrix = []
    for i in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)

    return np.array(matrix)

# Input matrices
A = input_matrix("A")
B = input_matrix("B")

while True:
    print("\n===== Matrix Operations Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if A.shape == B.shape:
            print("\nAddition Result:")
            print(A + B)
        else:
            print("Matrices must have same dimensions.")

    elif choice == 2:
        if A.shape == B.shape:
            print("\nSubtraction Result:")
            print(A - B)
        else:
            print("Matrices must have same dimensions.")

    elif choice == 3:
        if A.shape[1] == B.shape[0]:
            print("\nMultiplication Result:")
            print(np.dot(A, B))
        else:
            print("Columns of A must equal rows of B.")

    elif choice == 4:
        matrix_choice = input("Transpose Matrix A or B? (A/B): ").upper()

        if matrix_choice == "A":
            print("\nTranspose of Matrix A:")
            print(A.T)
        elif matrix_choice == "B":
            print("\nTranspose of Matrix B:")
            print(B.T)
        else:
            print("Invalid choice.")

    elif choice == 5:
        matrix_choice = input("Determinant of Matrix A or B? (A/B): ").upper()

        if matrix_choice == "A":
            if A.shape[0] == A.shape[1]:
                print("\nDeterminant of A:")
                print(np.linalg.det(A))
            else:
                print("Matrix A must be square.")
        elif matrix_choice == "B":
            if B.shape[0] == B.shape[1]:
                print("\nDeterminant of B:")
                print(np.linalg.det(B))
            else:
                print("Matrix B must be square.")
        else:
            print("Invalid choice.")

    elif choice == 6:
        print("Program Ended.")
        break

    else:
        print("Invalid choice! Try again.")