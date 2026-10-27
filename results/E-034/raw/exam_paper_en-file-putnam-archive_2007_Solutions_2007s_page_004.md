<|det|>page_number [914, 36, 925, 47]<|/det|>4
<|det|>text [91, 64, 491, 125]<|/det|>B-2 Put \( B = \max_{0 \leq x \leq 1} |f'(x)| \) and \( g(x) = \int_0^x f(y) dy \). Since \( g(0) = g(1) = 0 \), the maximum value of \( |g(x)| \) must occur at a critical point \( y \in (0,1) \) satisfying \( g'(y) = f(y) = 0 \). We may thus take \( \alpha = y \) hereafter.
<|det|>text [123, 129, 492, 205]<|/det|>Since \(\int_0^\alpha f(x)dx = -\int_0^{1 - \alpha}f(1 - x)dx\), we may assume that \(\alpha \leq 1 / 2\). By then substituting \(-f(x)\) for \(f(x)\) if needed, we may assume that \(\int_0^\alpha f(x)dx\geq 0\). From the inequality \(f'(x)\geq -B\), we deduce \(f(x)\leq B(\alpha -x)\) for \(0\leq x\leq \alpha\), so
<|det|>equation [174, 212, 401, 318]<|/det|>\[
\begin{array}{l} \int_ {0} ^ {\alpha} f (x) d x \leq \int_ {0} ^ {\alpha} B (\alpha - x) d x \\ = - \frac {1}{2} B (\alpha - x) ^ {2} \Bigg | _ {0} ^ {\alpha} \\ = \frac {\alpha^ {2}}{2} B \leq \frac {1}{8} B \\ \end{array}
\]
<|det|>text [125, 324, 198, 337]<|/det|>as desired.
<|det|>text [91, 348, 491, 435]<|/det|>B-3 First solution: Observing that  \( x_{2}/2 = 13 \) ,  \( x_{3}/4 = 34 \) ,  \( x_{4}/8 = 89 \) , we guess that  \( x_{n} = 2^{n-1}F_{2n+3} \) , where  \( F_{k} \)  is the k-th Fibonacci number. Thus we claim that  \( x_{n} = \frac{2^{n-1}}{\sqrt{5}}(\alpha^{2n+3} - \alpha^{-(2n+3)}) \) , where  \( \alpha = \frac{1+\sqrt{5}}{2} \) , to make the answer  \( x_{2007} = \frac{2^{2006}}{\sqrt{5}}(\alpha^{3997} - \alpha^{-3997}) \) .
<|det|>text [124, 439, 491, 504]<|/det|>We prove the claim by induction; the base case  \( x_{0}=1 \)  is true, and so it suffices to show that the recursion  \( x_{n+1}=3x_{n}+\lfloor x_{n}\sqrt{5}\rfloor \)  is satisfied for our formula for  \( x_{n} \) . Indeed, since  \( \alpha^{2}=\frac{3+\sqrt{5}}{2} \) , we have
<|det|>equation [109, 513, 463, 590]<|/det|>\[
\begin{array}{l} x _ {n + 1} - (3 + \sqrt {5}) x _ {n} = \frac {2 ^ {n - 1}}{\sqrt {5}} (2 (\alpha^ {2 n + 5} - \alpha^ {- (2 n + 5)}) \\ - (3 + \sqrt {5}) (\alpha^ {2 n + 3} - \alpha^ {- (2 n + 3)})) \\ = 2 ^ {n} \alpha^ {- (2 n + 3)}. \\ \end{array}
\]
<|det|>text [124, 602, 490, 636]<|/det|>Now \( 2^{n}\alpha^{-(2n+3)} = (\frac{1-\sqrt{5}}{2})^{3}(3-\sqrt{5})^{n} \) is between -1 and 0; the recursion follows since \( x_{n}, x_{n+1} \) are integers.
<|det|>text [124, 639, 490, 684]<|/det|>Second solution: (by Catalin Zara) Since  \( x_{n} \)  is rational, we have  \( 0 < x_{n}\sqrt{5} - \lfloor x_{n}\sqrt{5} \rfloor < 1 \) . We now have the inequalities
<|det|>equation [164, 696, 408, 714]<|/det|>\[
x _ {n + 1} - 3 x _ {n} <   x _ {n} \sqrt {5} <   x _ {n + 1} - 3 x _ {n} + 1
\]
<|det|>equation [166, 716, 410, 734]<|/det|>\[
(3 + \sqrt {5}) x _ {n} - 1 <   x _ {n + 1} <   (3 + \sqrt {5}) x _ {n}
\]
<|det|>equation [160, 738, 414, 755]<|/det|>\[
4 x _ {n} - (3 - \sqrt {5}) <   (3 - \sqrt {5}) x _ {n + 1} <   4 x _ {n}
\]
<|det|>equation [124, 759, 452, 777]<|/det|>\[
3 x _ {n + 1} - 4 x _ {n} <   x _ {n + 1} \sqrt {5} <   3 x _ {n + 1} - 4 x _ {n} + (3 - \sqrt {5}).
\]
<|det|>text [124, 789, 490, 848]<|/det|>Since  \( 0 < 3 - \sqrt{5} < 1 \) , this yields  \( \lfloor x_{n+1}\sqrt{5} \rfloor = 3x_{n+1} - 4x_{n} \) , so we can rewrite the recursion as  \( x_{n+1} = 6x_{n} - 4x_{n-1} \)  for  \( n \geq 2 \) . It is routine to solve this recursion to obtain the same solution as above.
<|det|>text [124, 853, 490, 914]<|/det|>Remark: With an initial 1 prepended, this becomes sequence A018903 in Sloane's On-Line Encyclopedia of Integer Sequences: (http://www.research.att.com/~njas/
<|det|>text [553, 66, 920, 169]<|/det|>sequences/). Therein, the sequence is described as the case \( S(1,5) \) of the sequence \( S(a_0,a_1) \) in which \( a_{n + 2} \) is the least integer for which \( a_{n + 2} / a_{n + 1} > a_{n + 1} / a_n \). Sloane cites D. W. Boyd, Linear recurrence relations for some generalized Pisot sequences, Advances in Number Theory (Kingston, ON, 1991), Oxford Univ. Press, New York, 1993, p. 333-340.
<|det|>text [521, 177, 920, 237]<|/det|>B-4 The number of pairs is \( 2^{n+1} \). The degree condition forces \( P \) to have degree \( n \) and leading coefficient \( \pm 1 \); we may count pairs in which \( P \) has leading coefficient 1 as long as we multiply by 2 afterward.
<|det|>text [555, 241, 673, 254]<|/det|>Factor both sides:
<|det|>equation [594, 267, 840, 368]<|/det|>\[
\begin{array}{l} (P (X) + Q (X) i) (P (X) - Q (X) i) \\ = \prod_ {j = 0} ^ {n - 1} (X - \exp (2 \pi i (2 j + 1) / (4 n))) \\ \cdot \prod_ {j = 0} ^ {n - 1} (X + \exp (2 \pi i (2 j + 1) / (4 n))). \\ \end{array}
\]
<|det|>text [553, 379, 920, 539]<|/det|>Then each choice of P, Q corresponds to equating  \( P(X) + Q(X)i \)  with the product of some n factors on the right, in which we choose exactly of the two factors for each  \( j = 0, \ldots, n - 1 \) . (We must take exactly n factors because as a polynomial in X with complex coefficients,  \( P(X) + Q(X)i \)  has degree exactly n. We must choose one for each j to ensure that  \( P(X) + Q(X)i \)  and  \( P(X) - Q(X)i \)  are complex conjugates, so that P, Q have real coefficients.) Thus there are  \( 2^{n} \)  such pairs; multiplying by 2 to allow P to have leading coefficient -1 yields the desired result.
<|det|>text [553, 544, 920, 606]<|/det|>Remark: If we allow P and Q to have complex coefficients but still require  \( \deg(P) > \deg(Q) \) , then the number of pairs increases to  \( 2\binom{2n}{n} \) , as we may choose any n of the 2n factors of  \( X^{2n} + 1 \)  to use to form  \( P(X) + Q(X)i \) .
<|det|>text [521, 616, 920, 647]<|/det|>B-5 For \( n \) an integer, we have \( \left\lfloor \frac{n}{k} \right\rfloor = \frac{n - j}{k} \) for \( j \) the unique integer in \( \{0, \ldots, k - 1\} \) congruent to \( n \) modulo \( k \); hence
<|det|>equation [632, 657, 800, 697]<|/det|>\[
\prod_ {j = 0} ^ {k - 1} \left(\left\lfloor \frac {n}{k} \right\rfloor - \frac {n - j}{k}\right) = 0.
\]
<|det|>text [553, 708, 919, 738]<|/det|>By expanding this out, we obtain the desired polynomials  \( P_{0}(n), \ldots, P_{k-1}(n) \) .
<|det|>text [553, 741, 919, 784]<|/det|>Remark: Variants of this solution are possible that construct the  \( P_{i} \)  less explicitly, using Lagrange interpolation or Vandermonde determinants.
<|det|>text [521, 794, 920, 868]<|/det|>B-6 (Suggested by Oleg Golberg) Assume \( n \geq 2 \), or else the problem is trivially false. Throughout this proof, any \( C_i \) will be a positive constant whose exact value is immaterial. As in the proof of Stirling's approximation, we estimate for any fixed \( c \in \mathbb{R} \),
<|det|>equation [565, 878, 866, 915]<|/det|>\[
\sum_ {i = 1} ^ {n} (i + c) \log i = \frac {1}{2} n ^ {2} \log n - \frac {1}{4} n ^ {2} + O (n \log n)
\]
