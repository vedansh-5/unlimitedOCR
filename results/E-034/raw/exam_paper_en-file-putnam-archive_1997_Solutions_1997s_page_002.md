<|det|>page_number [913, 35, 923, 46]<|/det|>2
<|det|>text [125, 66, 438, 82]<|/det|>(by logarithmic differentiation) or equivalently,
<|det|>equation [126, 90, 449, 128]<|/det|>\[
\begin{array}{l} (1 - t ^ {2}) f ^ {\prime} (t) = f (t) [ (n - 1 - r) (1 - t) - r (1 + t) ] \\ = f (t) \left[ (n - 1 - 2 r) - (n - 1) t \right] \\ \end{array}
\]
<|det|>text [125, 140, 454, 155]<|/det|>and then taking the coefficient of \( t^k \) on both sides:
<|det|>equation [200, 168, 384, 202]<|/det|>\[
\begin{array}{l} (k + 1) x _ {k + 2} - (k - 1) x _ {k} = \\ (n - 1 - 2 r) x _ {k + 1} - (n - 1) x _ {k}. \\ \end{array}
\]
<|det|>text [124, 215, 489, 246]<|/det|>In particular, the largest such c is n-1, and  \( x_{k} = \binom{n-1}{k-1} \)  for  \( k = 1, 2, \ldots, n \) .
<|det|>text [124, 250, 490, 309]<|/det|>Greg Kuperberg has suggested an alternate approach to show directly that c = n - 1 is the largest root, without computing the others. Note that the condition  \( x_{n+1} = 0 \)  states that  \( (x_{1}, \ldots, x_{n}) \)  is an eigenvector of the matrix
<|det|>equation [197, 320, 372, 368]<|/det|>\[
A _ {i j} = \left\{ \begin{array}{c c c} i & j & i = i + 1 \\ n - j & j & i = i - 1 \\ 0 & \text {otherwise} \end{array} \right.
\]
<|det|>text [124, 379, 491, 438]<|/det|>with eigenvalue c. By the Perron-Frobenius theorem, A has a unique eigenvector with positive entries, whose eigenvalue has modulus greater than or equal to that of any other eigenvalue, which proves the claim.
<|det|>text [92, 446, 490, 517]<|/det|>B-1 It is trivial to check that \(\frac{m}{6n} = \{\frac{m}{6n}\} \leq \{\frac{m}{3n}\}\) for \(1 \leq m \leq 2n\), that \(1 - \frac{m}{3n} = \{\frac{m}{3n}\} \leq \{\frac{m}{6n}\}\) for \(2n \leq m \leq 3n\), that \(\frac{m}{3n} - 1 = \{\frac{m}{3n}\} \leq \{\frac{m}{6n}\}\) for \(3n \leq m \leq 4n\), and that \(1 - \frac{m}{6n} = \{\frac{m}{6n}\} \leq \{\frac{m}{6n}\}\) for \(4n \leq m \leq 6n\). Therefore the desired sum is
<|det|>equation [154, 527, 418, 610]<|/det|>\[
\begin{array}{l} \sum_ {m = 1} ^ {2 n - 1} \frac {m}{6 n} + \sum_ {m = 2 n} ^ {3 n - 1} \left(1 - \frac {m}{3 n}\right) \\ + \sum_ {m = 3 n} ^ {4 n - 1} \left(\frac {m}{3 n} - 1\right) + \sum_ {m = 4 n} ^ {6 n - 1} \left(1 - \frac {m}{6 n}\right) = n. \\ \end{array}
\]
<|det|>text [92, 622, 490, 652]<|/det|>B-2 It suffices to show that \( |f(x)| \) is bounded for \( x \geq 0 \), since \( f(-x) \) satisfies the same equation as \( f(x) \). But then
<|det|>equation [126, 661, 445, 714]<|/det|>\[
\begin{array}{l} \frac {d}{d x} \left((f (x)) ^ {2} + (f ^ {\prime} (x)) ^ {2}\right) = 2 f ^ {\prime} (x) (f (x) + f ^ {\prime \prime} (x)) \\ = - 2 x g (x) \left(f ^ {\prime} (x)\right) ^ {2} \leq 0, \\ \end{array}
\]
<|det|>text [125, 724, 432, 742]<|/det|>so that \((f(x))^2 \leq (f(0))^2 + (f'(0))^2\) for \(x \geq 0\).
<|det|>text [92, 750, 490, 779]<|/det|>B-3 The only such \( n \) are the numbers 1-4, 20-24, 100-104, and 120-124. For the proof let
<|det|>equation [244, 790, 329, 826]<|/det|>\[
H _ {n} = \sum_ {m = 1} ^ {n} \frac {1}{m}
\]
<|det|>text [125, 836, 364, 851]<|/det|>and introduce the auxiliary function
<|det|>equation [214, 861, 360, 898]<|/det|>\[
I _ {n} = \sum_ {1 \leq m \leq n, (m, 5) = 1} \frac {1}{m}.
\]
<|det|>text [554, 66, 920, 111]<|/det|>It is immediate (e.g., by induction) that  \( I_{n} \equiv 1, -1, 1, 0, 0 \pmod{5} \)  for  \( n \equiv 1, 2, 3, 4, 5 \pmod{5} \)  respectively, and moreover, we have the equality
<|det|>equation [647, 123, 787, 160]<|/det|>\[
H _ {n} = \sum_ {m = 0} ^ {k} \frac {1}{5 ^ {m}} I _ {\lfloor n / 5 ^ {m} \rfloor},
\]
<|det|>text [554, 171, 920, 244]<|/det|>where  \( k = k(n) \)  denotes the largest integer such that  \( 5^{k} \leq n \) . We wish to determine those n such that the above sum has nonnegative 5-valuation. (By the 5-valuation of a number a we mean the largest integer v such that  \( a/5^{v} \)  is an integer.)
<|det|>text [554, 247, 920, 350]<|/det|>If \(\lfloor n / 5^k\rfloor \leq 3\), then the last term in the above sum has 5-valuation \(-k\), since \(I_1, I_2, I_3\) each have valuation 0; on the other hand, all other terms must have 5-valuation strictly larger than \(-k\). It follows that \(H_n\) has 5-valuation exactly \(-k\); in particular, \(H_n\) has nonnegative 5-valuation in this case if and only if \(k = 0\), i.e., \(n = 1, 2\), or 3.
<|det|>text [554, 354, 920, 413]<|/det|>Suppose now that \(\lfloor n / 5^k\rfloor = 4\). Then we must also have \(20\leq \lfloor n / 5^{k - 1}\rfloor \leq 24\). The former condition implies that the last term of the above sum is \(I_4 / 5^k = 1 / (12\cdot 5^{k - 2})\), which has 5-valuation \(-(k - 2)\).
<|det|>text [554, 416, 920, 650]<|/det|>It is clear that \( I_{20} \equiv I_{24} \equiv 0 \pmod{25} \); hence if \( \lfloor n / 5^{k-1} \rfloor \) equals 20 or 24, then the second-to-last term of the above sum (if it exists) has valuation at least \( -(k-3) \). The third-to-last term (if it exists) is of the form \( I_r / 5^{k-2} \), so that the sum of the last term and the third to last term takes the form \( (I_r + 1/12) / 5^{k-2} \). Since \( I_r \) can be congruent only to 0,1, or -1 (mod 5), and \( 1/12 \equiv 3 \) (mod 5), we conclude that the sum of the last term and third-to-last term has valuation \( -(k-2) \), while all other terms have valuation strictly higher. Hence \( H_n \) has nonnegative 5-valuation in this case only when \( k \leq 2 \), leading to the values \( n = 4 \) (arising from \( k = 0 \)), 20,24 (arising from \( k = 1 \) and \( \lfloor n/5^{k-1} \rfloor = 20 \) and 24 resp.), 101, 102, 103, and 104 (arising from \( k = 2 \), \( \lfloor n/5^{k-1} \rfloor = 20 \)) and 120, 121, 122, 123, and 124 (arising from \( k = 2 \), \( \lfloor n/5^{k-1} \rfloor = 24 \)).
<|det|>text [553, 653, 920, 813]<|/det|>Finally, suppose \(\lfloor n / 5^k\rfloor = 4\) and \(\lfloor n / 5^{k - 1}\rfloor = 21\), 22, or 23. Then as before, the first condition implies that the last term of the sum in (*) has valuation \(-(k - 2)\), while the second condition implies that the second-to-last term in the same sum has valuation \(-(k - 1)\). Hence all terms in the sum (*) have 5-valuation strictly higher than \(-(k - 1)\), except for the second-to-last term, and therefore \(H_{n}\) has 5-valuation \(-(k - 1)\) in this case. In particular, \(H_{n}\) is integral (mod 5) in this case if and only if \(k\leq 1\), which gives the additional values \(n = 21\), 22, and 23.
<|det|>text [521, 823, 919, 856]<|/det|>B-4 Let \( s_k = \sum_i (-1)^i a_{k-1,i} \) be the given sum (note that \( a_{k-1,i} \) is nonzero precisely for \( i = 0, \ldots, \lfloor \frac{2k}{3} \rfloor \)). Since
<|det|>equation [607, 868, 826, 882]<|/det|>\[
a _ {m + 1, n} = a _ {m, n} + a _ {m, n - 1} + a _ {m, n - 2},
\]
