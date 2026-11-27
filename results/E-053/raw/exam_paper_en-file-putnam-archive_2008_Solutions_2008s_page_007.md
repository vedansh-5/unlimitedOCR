<|det|>page_number [894, 35, 905, 46]<|/det|>7
<|det|>text [124, 66, 490, 96]<|/det|>identity matrix), the bottom right block is  \( M_{n-2k-1,k} \) , and the other two blocks are zero. We conclude that
<|det|>equation [157, 108, 418, 125]<|/det|>\[
\det (M _ {n, k}) \equiv \det (M _ {n - 2 k - 1, k}) \pmod {2},
\]
<|det|>text [124, 135, 338, 150]<|/det|>proving the desired congruence.
<|det|>text [124, 155, 491, 271]<|/det|>To prove the desired result, we must now check that  \( F_{0,k}, F_{1,k} \)  are odd and  \( F_{2,k}, \ldots, F_{2k,k} \)  are even. For  \( n = 0, \ldots, k + 1 \) , the matrix  \( M_{n,k} \)  consists of all ones, so its determinant is 1 if n = 0, 1 and 0 otherwise. (Alternatively, we have  \( F_{n,k} = n! \)  for  \( n = 0, \ldots, k + 1 \) , since every permutation of  \( \{1, \ldots, n\} \)  is k-limited.) For  \( n = k + 2, \ldots, 2k \) , observe that rows k and  \( k + 1 \)  of  \( M_{n,k} \)  both consist of all ones, so  \( \det(M_{n,k}) = 0 \)  as desired.
<|det|>text [124, 275, 492, 348]<|/det|>Third solution: (by Tom Beloulovich) Define  \( M_{n,k} \)  as in the second solution. We prove  \( \det(M_{n,k}) \)  is odd for  \( n \equiv 0, 1 \pmod{2k + 1} \)  and even otherwise, by directly determining whether or not  \( M_{n,k} \)  is invertible as a matrix over the field of two elements.
<|det|>text [124, 353, 492, 426]<|/det|>Let \( r_i \) denote row \( i \) of \( M_{n,k} \). We first check that if \( n \equiv 2, \ldots, 2k \pmod{2k + 1} \), then \( M_{n,k} \) is not invertible. In this case, we can find integers \( 0 \leq a < b \leq k \) such that \( n + a + b \equiv 0 \pmod{2k + 1} \). Put \( j = (n + a + b) / (2k + 1) \). We can then write the all-ones vector both as
<|det|>equation [226, 438, 348, 477]<|/det|>\[
\sum_ {i = 0} ^ {j - 1} r _ {k + 1 - a + (2 k + 1) i}
\]
<|det|>text [125, 486, 172, 499]<|/det|>and as
<|det|>equation [225, 509, 348, 548]<|/det|>\[
\sum_ {i = 0} ^ {j - 1} r _ {k + 1 - b + (2 k + 1) i}.
\]
<|det|>text [125, 558, 314, 573]<|/det|>Hence \(M_{n,k}\) is not invertible.
<|det|>text [553, 66, 920, 153]<|/det|>We next check that if  \( n \equiv 0, 1 \pmod{2k + 1} \) , then  \( M_{n,k} \)  is invertible. Suppose that  \( a_{1}, \ldots, a_{n} \)  are scalars such that  \( a_{1}r_{1} + \cdots + a_{n}r_{n} \)  is the zero vector. The m-th coordinate of this vector equals  \( a_{m-k} + \cdots + a_{m+k} \) , where we regard  \( a_{i} \)  as zero if  \( i \notin \{1, \ldots, n\} \) . By comparing consecutive coordinates, we obtain
<|det|>equation [605, 166, 828, 182]<|/det|>\[
a _ {m - k} = a _ {m + k + 1} \quad (1 \leq m <   n).
\]
<|det|>text [554, 193, 920, 222]<|/det|>In particular, the \(a_{i}\) repeat with period \(2k + 1\). Taking \(m = 1, \ldots, k\) further yields that
<|det|>equation [636, 236, 796, 250]<|/det|>\[
a _ {k + 2} = \dots = a _ {2 k + 1} = 0
\]
<|det|>text [554, 261, 818, 276]<|/det|>while taking \( m = n - k, \ldots, n - 1 \) yields
<|det|>equation [628, 290, 805, 304]<|/det|>\[
a _ {n - 2 k} = \dots = a _ {n - 1 - k} = 0.
\]
<|det|>text [554, 315, 910, 330]<|/det|>For \( n \equiv 0 \pmod{2k + 1} \), the latter can be rewritten as
<|det|>equation [656, 343, 778, 357]<|/det|>\[
a _ {1} = \dots = a _ {k} = 0
\]
<|det|>text [554, 369, 915, 384]<|/det|>whereas for \( n \equiv 1 \pmod{2k + 1} \), it can be rewritten as
<|det|>equation [648, 397, 786, 411]<|/det|>\[
a _ {2} = \dots = a _ {k + 1} = 0.
\]
<|det|>text [554, 412, 776, 425]<|/det|>In either case, since we also have
<|det|>equation [648, 438, 785, 452]<|/det|>\[
a _ {1} + \dots + a _ {2 k + 1} = 0
\]
<|det|>text [553, 464, 920, 494]<|/det|>from the \((k + 1)\)-st coordinate, we deduce that all of the \(a_{i}\) must be zero, and so \(M_{n,k}\) must be invertible.
<|det|>text [553, 498, 922, 558]<|/det|>Remark: The matrices  \( M_{n,k} \)  are examples of banded matrices, which occur frequently in numerical applications of linear algebra. They are also examples of Toeplitz matrices.
