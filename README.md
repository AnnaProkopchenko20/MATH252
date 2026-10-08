### LAB 1

#### AI usage
- for ai usage in code view: https://claude.ai/share/75410975-b3cc-4b1d-928d-6c5a9f7e33af

#### Theory questions:

1. What are linear transformations?

A linear transformation is a function T: V → W between vector spaces that preserves the two basic vector operations: Additivity Homogeneity.

2. The transformation matrix and its interpretation

For a linear map T: ℝⁿ → ℝᵐ, there is a unique m×n matrix A such that T(x) = Ax. Its construction is the key:

**The columns of A are the images of the basis vectors:** the j-th column is T(eⱼ).

Interpretation:
- Each column tells you where a basis vector lands. Because of linearity, knowing where the basis goes determines where *every* vector goes: x = x₁e₁ + … + xₙeₙ ⇒ T(x) = x₁T(e₁) + … + xₙT(eₙ). So Ax is a linear combination of the columns.
- Geometrically, the matrix describes how the whole coordinate grid is deformed (stretched, rotated, sheared, flattened).
- Matrix multiplication corresponds to composition: applying B then A is AB (order matters).
- The matrix depends on the chosen basis; a different basis gives a different matrix for the same transformation (A' = P⁻¹AP).

3. Rotation matrix: features and properties

In 2D, rotation by angle θ counterclockwise:

R(θ) = [[cos θ, −sin θ], [sin θ, cos θ]]

Properties:
- **Orthogonal:** RᵀR = RRᵀ = I, so R⁻¹ = Rᵀ. Columns (and rows) are orthonormal.
- **Determinant = +1** (a proper rotation; no reflection). Together these make R an element of SO(n).
- **Preserves lengths, angles, and dot products:** ‖Rx‖ = ‖x‖. Areas/volumes and orientation are preserved.
- **Inverse is rotation by −θ:** R(θ)⁻¹ = R(−θ) = R(θ)ᵀ.
- **Composition adds angles:** R(α)R(β) = R(α+β). In 2D, rotations commute; in 3D and higher they generally do not.
- **Eigenvalues:** in 2D they are e^{±iθ}, which are complex unless θ = 0 or π, so there are no real eigenvectors (no direction is preserved) for general θ. In 3D, a rotation has eigenvalue 1, whose eigenvector is the rotation axis.
- Trace = 2cos θ in 2D.
- Fixes the origin; distances between any two points are preserved (it is an isometry).

4. Undoing a transformation: the inverse

If y = Ax, the matrix that returns y to x is the **inverse matrix A⁻¹**, satisfying A⁻¹A = AA⁻¹ = I. Then x = A⁻¹y.

How to find it:
- Gauss-Jordan elimination: row-reduce [A | I] to [I | A⁻¹].
- Formula: A⁻¹ = adj(A)/det(A). For 2×2 [[a, b], [c, d]]: A⁻¹ = (1/(ad − bc)) [[d, −b], [−c, a]].
- Special cases: for rotations A⁻¹ = Aᵀ; for diagonal matrices invert each diagonal entry; for a composition, (AB)⁻¹ = B⁻¹A⁻¹ (reverse order).

The inverse exists only if A is square and det(A) ≠ 0
5. Meaning of |det A|

The determinant is the **signed factor by which volumes (areas in 2D) are scaled** by the transformation. The unit square/cube is mapped to a parallelogram/parallelepiped with volume |det A|.

- **|det A| < 1:** space is contracted; areas/volumes shrink by that factor. The map is still invertible (if det ≠ 0), and the inverse expands space by 1/|det A|.
- **|det A| > 1:** space is expanded; areas/volumes grow by that factor.
- **|det A| = 1:** volume is preserved. Shapes may be rotated, reflected, or sheared (shear changes shape but not area), but their size is unchanged. Rotations, reflections, and shears all fall here.
- **det A = 0:** space is collapsed into a lower dimension (a plane flattens to a line or point; 3D to a plane, line, or point). Volume becomes zero, the columns are linearly dependent, the matrix is singular, and the transformation is not invertible.

**The sign** of det A carries extra information: positive means orientation is preserved; negative means orientation is flipped (a reflection is involved)