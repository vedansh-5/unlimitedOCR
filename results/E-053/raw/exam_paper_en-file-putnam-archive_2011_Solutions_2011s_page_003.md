<|det|>page_number [913, 35, 923, 46]<|/det|>3
<|det|>text [100, 65, 490, 96]<|/det|>B1 Since the rational numbers are dense in the reals, we can find positive integers \(a, b\) such that
<|det|>equation [236, 106, 338, 137]<|/det|>\[
\frac {3 \varepsilon}{h k} <   \frac {b}{a} <   \frac {4 \varepsilon}{h k}.
\]
<|det|>text [124, 145, 489, 175]<|/det|>By multiplying \( a \) and \( b \) by a suitably large positive integer, we can also ensure that \( 3a^2 > b \). We then have
<|det|>equation [153, 185, 424, 220]<|/det|>\[
\frac {\varepsilon}{h k} <   \frac {b}{3 a} <   \frac {b}{\sqrt {a ^ {2} + b} + a} = \sqrt {a ^ {2} + b} - a
\]
<|det|>text [125, 230, 157, 243]<|/det|>and
<|det|>equation [148, 252, 429, 285]<|/det|>\[
\sqrt {a ^ {2} + b} - a = \frac {b}{\sqrt {a ^ {2} + b} + a} \leq \frac {b}{2 a} <   2 \frac {\varepsilon}{h k}.
\]
<|det|>text [125, 295, 417, 312]<|/det|>We may then take \( m = k^2 (a^2 + b) \), \( n = h^2 a^2 \).
<|det|>text [100, 320, 490, 364]<|/det|>B2 Only the primes 2 and 5 appear seven or more times. The fact that these primes appear is demonstrated by the examples
<|det|>equation [172, 375, 402, 392]<|/det|>\[
(2, 5, 2), (2, 5, 3), (2, 7, 5), (2, 1 1, 5)
\]
<|det|>text [125, 403, 252, 417]<|/det|>and their reversals.
<|det|>text [124, 422, 491, 626]<|/det|>It remains to show that if either \(\ell = 3\) or \(\ell\) is a prime greater than 5, then \(\ell\) occurs at most six times as an element of a triple in \(S\). Note that \((p,q,r) \in S\) if and only if \(q^2 - 4pr = a^2\) for some integer \(a\); in particular, since \(4pr \geq 16\), this forces \(q \geq 5\). In particular, \(q\) is odd, as then is \(a\), and so \(q^2 \equiv a^2 \equiv 1 \pmod{8}\); consequently, one of \(p, r\) must equal 2. If \(r = 2\), then \(8p = q^2 - a^2 = (q + a)(q - a)\); since both factors are of the same sign and their sum is the positive number \(2q\), both factors are positive. Since they are also both even, we have \(q + a \in \{2, 4, 2p, 4p\}\) and so \(q \in \{2p + 1, p + 2\}\). Similarly, if \(p = 2\), then \(q \in \{2r + 1, r + 2\}\). Consequently, \(\ell\) occurs at most twice as many times as there are prime numbers in the list
<|det|>equation [202, 636, 372, 666]<|/det|>\[
2 \ell + 1, \ell + 2, \frac {\ell - 1}{2}, \ell - 2.
\]
<|det|>text [124, 674, 490, 718]<|/det|>For \(\ell = 3, \ell - 2 = 1\) is not prime. For \(\ell \geq 7\), the numbers \(\ell - 2, \ell, \ell + 2\) cannot all be prime, since one of them is always a nontrivial multiple of 3.
<|det|>text [124, 722, 491, 809]<|/det|>Remark. The above argument shows that the cases listed for 5 are the only ones that can occur. By contrast, there are infinitely many cases where 2 occurs if either the twin prime conjecture holds or there are infinitely many Sophie Germain primes (both of which are expected to be true).
<|det|>text [100, 818, 376, 833]<|/det|>B3 Yes, it follows that \( f \) is differentiable.
<|det|>text [124, 837, 491, 911]<|/det|>First solution. Note first that at 0, \( f / g \) and \( g \) are both continuous, as then is their product \( f \). If \( f(0) \neq 0 \), then in some neighborhood of 0, \( f \) is either always positive or always negative. We can thus choose \( \varepsilon \in \{\pm 1\} \) so that \( \varepsilon f \) is the composition of the differentiable function
<|det|>text [555, 66, 920, 96]<|/det|>\( (fg) \cdot (f/g) \)  with the square root function. By the chain rule, f is differentiable at 0.
<|det|>text [555, 100, 842, 117]<|/det|>If \( f(0) = 0 \), then \( (f / g)(0) = 0 \), so we have
<|det|>equation [638, 128, 796, 160]<|/det|>\[
(f / g) ^ {\prime} (0) = \lim _ {x \to 0} \frac {f (x)}{x g (x)}.
\]
<|det|>text [554, 169, 920, 200]<|/det|>Since \( g \) is continuous at 0, we may multiply limits to deduce that \( \lim_{x\to 0}f(x) / x \) exists.
<|det|>text [554, 204, 921, 300]<|/det|>Second solution. Choose a neighborhood \(N\) of 0 on which \(g(x) \neq 0\). Define the following functions on \(N \setminus \{0\}\): \(h_1(x) = \frac{f(x)g(x) - f(0)g(0)}{x}\); \(h_2(x) = \frac{f(x)g(0) - f(0)g(x)}{xg(0)g(x)}\); \(h_3(x) = g(0)g(x)\); \(h_4(x) = \frac{1}{g(x) + g(0)}\). Then by assumption, \(h_1, h_2, h_3, h_4\) all have limits as \(x \to 0\). On the other hand,
<|det|>equation [578, 310, 857, 340]<|/det|>\[
\frac {f (x) - f (0)}{x} = \left(h _ {1} (x) + h _ {2} (x) h _ {3} (x)\right) h _ {4} (x),
\]
<|det|>text [555, 353, 903, 373]<|/det|>and it follows that \(\lim_{x\to 0}\frac{f(x) - f(0)}{x}\) exists, as desired.
<|det|>text [530, 380, 920, 470]<|/det|>B4 Number the games 1, ..., 2011, and let \( A = (a_{jk}) \) be the \( 2011 \times 2011 \) matrix whose \( jk \) entry is 1 if player \( k \) wins game \( j \) and \( i = \sqrt{-1} \) if player \( k \) loses game \( j \). Then \( \overline{a_{hj}} a_{jk} \) is 1 if players \( h \) and \( k \) tie in game \( j \); \( i \) if player \( h \) wins and player \( k \) loses in game \( j \); and \( -i \) if \( h \) loses and \( k \) wins. It follows that \( T + iW = \overline{A}^T A \).
<|det|>text [554, 475, 920, 582]<|/det|>Now the determinant of \( A \) is unchanged if we subtract the first row of \( A \) from each of the other rows, producing a matrix whose rows, besides the first one, are \( (1 - i) \) times a row of integers. Thus we can write \( \det A = (1 - i)^{2010}(a + bi) \) for some integers \( a, b \). But then \( \det(T + iW) = \det(\overline{A}^T A) = 2^{2010}(a^2 + b^2) \) is a nonnegative integer multiple of \( 2^{2010} \), as desired.
<|det|>text [530, 590, 686, 604]<|/det|>B5 Define the function
<|det|>equation [600, 612, 834, 645]<|/det|>\[
f (y) = \int_ {- \infty} ^ {\infty} \frac {d x}{(1 + x ^ {2}) (1 + (x + y) ^ {2})}.
\]
<|det|>text [554, 654, 848, 670]<|/det|>For \( y \geq 0 \), in the range \( -1 \leq x \leq 0 \), we have
<|det|>equation [517, 679, 918, 719]<|/det|>\[
\begin{array}{l} (1 + x ^ {2}) (1 + (x + y) ^ {2}) \leq (1 + 1) (1 + (1 + y) ^ {2}) = 2 y ^ {2} + 4 y + 4 \\ \leq 2 y ^ {2} + 4 + 2 (y ^ {2} + 1) \leq 6 + 6 y ^ {2}. \\ \end{array}
\]
<|det|>text [555, 730, 756, 744]<|/det|>We thus have the lower bound
<|det|>equation [655, 753, 780, 786]<|/det|>\[
f (y) \geq \frac {1}{6 (1 + y ^ {2})};
\]
<|det|>text [554, 796, 918, 812]<|/det|>the same bound is valid for \( y \leq 0 \) because \( f(y) = f(-y) \).
<|det|>text [555, 816, 828, 831]<|/det|>The original hypothesis can be written as
<|det|>equation [649, 842, 787, 881]<|/det|>\[
\sum_ {i, j = 1} ^ {n} f (a _ {i} - a _ {j}) \leq A n
\]
<|det|>text [555, 890, 697, 905]<|/det|>and thus implies that
<|det|>equation [627, 916, 806, 953]<|/det|>\[
\sum_ {i, j = 1} ^ {n} \frac {1}{1 + (a _ {i} - a _ {j}) ^ {2}} \leq 6 A n.
\]
