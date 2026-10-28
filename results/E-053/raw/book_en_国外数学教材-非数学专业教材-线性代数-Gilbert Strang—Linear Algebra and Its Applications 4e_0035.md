<|det|>page_number [142, 50, 163, 62]<|/det|>26
<|det|>header [367, 49, 681, 64]<|/det|>Chapter 1 Matrices and Gaussian Elimination
<|det|>text [139, 84, 704, 103]<|/det|>columns \( b_{1}, b_{2}, b_{3} \), the columns of \( AB \) should be \( Ab_{1}, Ab_{2}, Ab_{3}! \)
<|det|>equation [270, 110, 778, 181]<|/det|>\[
\text { Multiplication   by   columns } \quad A B = A \left[ \begin{array}{c} b _ {1} \\ b _ {2} \\ b _ {3} \end{array} \right] = \left[ \begin{array}{c} A b _ {1} \\ A b _ {2} \\ A b _ {3} \end{array} \right].
\]
<|det|>text [138, 189, 911, 326]<|/det|>Our first requirement had to do with rows, and this one is concerned with columns. A third approach is to describe each individual entry in \( AB \) and hope for the best. In fact, there is only one possible rule, and I am not sure who discovered it. It makes everything work. It does not allow us to multiply every pair of matrices. If they are square, they must have the same size. If they are rectangular, they must not have the same shape; the number of columns in \( A \) has to equal the number of rows in \( B \). Then \( A \) can be multiplied into each column of \( B \).
<|det|>text [138, 329, 910, 368]<|/det|>If \( A \) is \( m \) by \( n \), and \( B \) is \( n \) by \( p \), then multiplication is possible. The product \( AB \) will be \( m \) by \( p \). We now find the entry in row \( i \) and column \( j \) of \( AB \).
<|det|>text [180, 380, 871, 437]<|/det|>1C The \(i, j\) entry of \(AB\) is the inner product of the \(i\)th row of \(A\) and the \(j\)th column of \(B\). In Figure 1.7, the 3, 2 entry of \(AB\) comes from row 3 and column 2:
<|det|>equation [329, 441, 868, 462]<|/det|>\[
(A B) _ {3 2} = a _ {3 1} b _ {1 2} + a _ {3 2} b _ {2 2} + a _ {3 3} b _ {3 2} + a _ {3 4} b _ {4 2}. \tag {6}
\]
<|det|>image [210, 482, 852, 577]<|/det|>
<|det|>image_caption [264, 592, 785, 607]<|/det|>Figure 1.7: A 3 by 4 matrix A times a 4 by 2 matrix B is a 3 by 2 matrix AB.
<|det|>text [138, 640, 910, 700]<|/det|>Note. We write AB when the matrices have nothing special to do with elimination. Our earlier example was EA, because of the elementary matrix E. Later we have PA, or LU, or even LDU. The rule for matrix multiplication stays the same.
<|det|>title [141, 710, 260, 728]<|/det|>Example 1.
<|det|>equation [337, 726, 712, 779]<|/det|>\[
A B = \left[ \begin{array}{c c} 2 & 3 \\ 4 & 0 \end{array} \right] \left[ \begin{array}{c c c} 1 & 2 & 0 \\ 5 & - 1 & 0 \end{array} \right] = \left[ \begin{array}{c c c} 1 7 & 1 & 0 \\ 4 & 8 & 0 \end{array} \right].
\]
<|det|>text [138, 782, 910, 821]<|/det|>The entry 17 is \((2)(1) + (3)(5)\), the inner product of the first row of \(A\) and first column of \(B\). The entry 8 is \((4)(2) + (0)(-1)\), from the second row and second column.
<|det|>text [138, 822, 912, 900]<|/det|>The third column is zero in B, so it is zero in AB. B consists of three columns side by side, and A multiplies each column separately. Every column of AB is a combination of the columns of A. Just as in a matrix-vector multiplication, the columns of A are multiplied by the entries in B.
