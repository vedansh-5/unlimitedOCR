7.6 For Reference:

Second- and Third-Order Determinants

Cramer's Rule for Linear Systems of Three Equations

\[
\begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + a _ {1 3} x _ {3} = b _ {1} \tag {5} \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + a _ {2 3} x _ {3} = b _ {2} \\ a _ {3 1} x _ {1} + a _ {3 2} x _ {2} + a _ {3 3} x _ {3} = b _ {3} \\ \end{array}
\]

is

\[
x _ {1} = \frac {D _ {1}}{D}, \quad x _ {2} = \frac {D _ {2}}{D}, \quad x _ {3} = \frac {D _ {3}}{D} \quad (D \neq 0) \tag {6}
\]

with the determinant \(D\) of the system given by (4) and

\[
D _ {1} = \left| \begin{array}{c c c} b _ {1} & a _ {1 2} & a _ {1 3} \\ b _ {2} & a _ {2 2} & a _ {2 3} \\ b _ {3} & a _ {3 2} & a _ {3 3} \end{array} \right|, \quad D _ {2} = \left| \begin{array}{c c c} a _ {1 1} & b _ {1} & a _ {1 3} \\ a _ {2 1} & b _ {2} & a _ {2 3} \\ a _ {3 1} & b _ {3} & a _ {3 3} \end{array} \right|, \quad D _ {3} = \left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & b _ {1} \\ a _ {2 1} & a _ {2 2} & b _ {2} \\ a _ {3 1} & a _ {3 2} & b _ {3} \end{array} \right|.
\]

Note that  \( D_{1}, D_{2}, D_{3} \)  are obtained by replacing Columns 1, 2, 3, respectively, by the column of the right sides of (5).

Section 7.6 p90

Advanced Engineering Mathematics, 10/e by Edwin Kreyszig

Copyright 2011 by John Wiley & Sons. All rights reserved.
