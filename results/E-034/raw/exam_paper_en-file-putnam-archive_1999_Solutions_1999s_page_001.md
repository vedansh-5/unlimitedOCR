<|det|>title [198, 64, 808, 101]<|/det|>Solutions to the 60th William Lowell Putnam Mathematical Competition Saturday, December 4, 1999
<|det|>text [332, 114, 673, 131]<|/det|>Manjul Bhargava, Kiran Kedlaya, and Lenny Ng
<|det|>text [90, 165, 475, 181]<|/det|>A-1 Note that if \( r(x) \) and \( s(x) \) are any two functions, then
<|det|>equation [185, 192, 388, 211]<|/det|>\[
\max (r, s) = (r + s + | r - s |) / 2.
\]
<|det|>text [125, 222, 447, 238]<|/det|>Therefore, if \( F(x) \) is the given function, we have
<|det|>equation [126, 251, 449, 337]<|/det|>\[
\begin{array}{l} F (x) = \max \{- 3 x - 3, 0 \} - \max \{5 x, 0 \} + 3 x + 2 \\ = (- 3 x - 3 + | 3 x + 3 |) / 2 \\ - (5 x + | 5 x |) / 2 + 3 x + 2 \\ = | (3 x + 3) / 2 | - | 5 x / 2 | - x + \frac {1}{2}, \\ \end{array}
\]
<|det|>text [124, 348, 490, 380]<|/det|>so we may set \( f(x) = (3x + 3) / 2 \), \( g(x) = 5x / 2 \), and \( h(x) = -x + \frac{1}{2} \).
<|det|>text [90, 389, 491, 464]<|/det|>A-2 First solution: First factor \( p(x) = q(x)r(x) \), where \( q \) has all real roots and \( r \) has all complex roots. Notice that each root of \( q \) has even multiplicity, otherwise \( p \) would have a sign change at that root. Thus \( q(x) \) has a square root \( s(x) \).
<|det|>text [124, 470, 490, 530]<|/det|>Now write  \(  r(x) = \prod_{j=1}^{k} (x - a_j)(x - \overline{a_j})  \)  (possible because r has roots in complex conjugate pairs). Write  \(  \prod_{j=1}^{k} (x - a_j) = t(x) + i u(x)  \)  with t, x having real coefficients. Then for x real,
<|det|>equation [154, 542, 418, 602]<|/det|>\[
\begin{array}{l} p (x) = q (x) r (x) \\ = s (x) ^ {2} (t (x) + i u (x)) (\overline {{t (x) + i u (x)}}) \\ = (s (x) t (x)) ^ {2} + (s (x) u (x)) ^ {2}. \\ \end{array}
\]
<|det|>text [124, 614, 491, 673]<|/det|>(Alternatively, one can factor \( r(x) \) as a product of quadratic polynomials with real coefficients, write each as a sum of squares, then multiply together to get a sum of many squares.)
<|det|>text [124, 678, 490, 810]<|/det|>Second solution: We proceed by induction on the degree of \( p \), with base case where \( p \) has degree 0. As in the first solution, we may reduce to a smaller degree in case \( p \) has any real roots, so assume it has none. Then \( p(x) > 0 \) for all real \( x \), and since \( p(x) \to \infty \) for \( x \to \pm \infty \), \( p \) has a minimum value \( c \). Now \( p(x) - c \) has real roots, so as above, we deduce that \( p(x) - c \) is a sum of squares. Now add one more square, namely \( (\sqrt{c})^2 \), to get \( p(x) \) as a sum of squares.
<|det|>text [90, 822, 490, 895]<|/det|>A-3 First solution: Computing the coefficient of \( x^{n+1} \) in the identity \( (1 - 2x - x^2)\sum_{m=0}^{\infty}a_mx^m = 1 \) yields the recurrence \( a_{n+1} = 2a_n + a_{n-1} \); the sequence \( \{a_n\} \) is then characterized by this recurrence and the initial conditions \( a_0 = 1, a_1 = 2 \).
<|det|>text [124, 899, 490, 918]<|/det|>Define the sequence \(\{b_n\}\) by \(b_{2n} = a_{n - 1}^2 +a_n^2\), \(b_{2n + 1} =\)
<|det|>text [555, 166, 708, 181]<|/det|>\(a_{n}(a_{n - 1} + a_{n + 1})\) . Then
<|det|>equation [561, 193, 871, 254]<|/det|>\[
\begin{array}{l} 2 b _ {2 n + 1} + b _ {2 n} = 2 a _ {n} a _ {n + 1} + 2 a _ {n - 1} a _ {n} + a _ {n - 1} ^ {2} + a _ {n} ^ {2} \\ = 2 a _ {n} a _ {n + 1} + a _ {n - 1} a _ {n + 1} + a _ {n} ^ {2} \\ = a _ {n + 1} ^ {2} + a _ {n} ^ {2} = b _ {2 n + 2}, \\ \end{array}
\]
<|det|>text [554, 267, 920, 342]<|/det|>and similarly \(2b_{2n} + b_{2n - 1} = b_{2n + 1}\), so that \(\{b_n\}\) satisfies the same recurrence as \(\{a_n\}\). Since further \(b_0 = 1, b_1 = 2\) (where we use the recurrence for \(\{a_n\}\) to calculate \(a_{-1} = 0\)), we deduce that \(b_n = a_n\) for all \(n\). In particular, \(a_n^2 + a_{n + 1}^2 = b_{2n + 2} = a_{2n + 2}\).
<|det|>text [555, 346, 735, 360]<|/det|>Second solution: Note that
<|det|>equation [531, 374, 901, 450]<|/det|>\[
\begin{array}{l} \frac {1}{1 - 2 x - x ^ {2}} \\ = \frac {1}{2 \sqrt {2}} \left(\frac {\sqrt {2} + 1}{1 - (1 + \sqrt {2}) x} + \frac {\sqrt {2} - 1}{1 - (1 - \sqrt {2}) x}\right) \\ \end{array}
\]
<|det|>text [555, 460, 613, 473]<|/det|>and that
<|det|>equation [605, 485, 831, 521]<|/det|>\[
\frac {1}{1 + (1 \pm \sqrt {2}) x} = \sum_ {n = 0} ^ {\infty} (1 \pm \sqrt {2}) ^ {n} x ^ {n},
\]
<|det|>text [555, 535, 604, 547]<|/det|>so that
<|det|>equation [575, 558, 857, 592]<|/det|>\[
a _ {n} = \frac {1}{2 \sqrt {2}} \left((\sqrt {2} + 1) ^ {n + 1} - (1 - \sqrt {2}) ^ {n + 1}\right).
\]
<|det|>text [554, 603, 920, 634]<|/det|>A simple computation (omitted here) now shows that \(a_{n}^{2} + a_{n + 1}^{2} = a_{2n + 2}\).
<|det|>text [555, 638, 920, 686]<|/det|>Third solution (by Richard Stanley): Let \(A\) be the matrix \(\left( \begin{array}{cc}0 & 1\\ 1 & 2 \end{array} \right)\). A simple induction argument shows that
<|det|>equation [637, 700, 795, 733]<|/det|>\[
A ^ {n + 2} = \left( \begin{array}{c c} a _ {n} & a _ {n + 1} \\ a _ {n + 1} & a _ {n + 2} \end{array} \right).
\]
<|det|>text [554, 745, 920, 775]<|/det|>The desired result now follows from comparing the top left corner entries of the equality  \( A^{n+2}A^{n+2}=A^{2n+4} \) .
<|det|>text [520, 787, 898, 803]<|/det|>A–4 Denote the series by S, and let  \( a_{n} = 3^{n}/n \) . Note that
<|det|>equation [631, 816, 801, 890]<|/det|>\[
\begin{array}{l} S = \sum_ {m = 1} ^ {\infty} \sum_ {n = 1} ^ {\infty} \frac {1}{a _ {m} (a _ {m} + a _ {n})} \\ = \sum_ {m = 1} ^ {\infty} \sum_ {n = 1} ^ {\infty} \frac {1}{a _ {\mathrm{n}} (a _ {m} + a _ {n})}, \\ \end{array}
\]
<|det|>text [555, 902, 920, 918]<|/det|>where the second equality follows by interchanging m
