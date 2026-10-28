7.2 Matrix Multiplication

Parallel processing of products on the computer is facilitated by a variant of (3) for computing C = AB, which is used by standard algorithms (such as in Lapack). In this method, A is used as given, B is taken in terms of its column vectors, and the product is computed columnwise; thus,

\[
(5) \mathbf {A B} = \mathbf {A} [ \mathbf {b} _ {1} \mathbf {b} _ {2} \dots \mathbf {b} _ {p} ] = [ \mathbf {A b} _ {1} \mathbf {A b} _ {2} \dots \mathbf {A b} _ {p} ].
\]

Columns of B are then assigned to different processors (individually or several to each processor), which simultaneously compute the columns of the product matrix  \( Ab_{1} \) ,  \( Ab_{2} \) , etc.

Section 7.2 p21

Advanced Engineering Mathematics, 10/e by Edwin Kreyszig

Copyright 2011 by John Wiley & Sons. All rights reserved.
