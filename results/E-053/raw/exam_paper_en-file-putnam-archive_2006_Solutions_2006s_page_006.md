<|det|>page_number [908, 35, 921, 47]<|/det|>6
<|det|>text [124, 65, 489, 94]<|/det|>Zaslavsky, Extremal arrangements of hyperplanes, Ann. N. Y. Acad. Sci. 440 (1985), 69-87.
<|det|>text [91, 103, 490, 135]<|/det|>B-4 The maximum is \(2^{k}\), achieved for instance by the subspace
<|det|>equation [150, 146, 424, 163]<|/det|>\[
\{(x _ {1}, \dots , x _ {n}) \in \mathbb {R} ^ {n}: x _ {1} = \dots = x _ {n - k} = 0 \}.
\]
<|det|>text [124, 179, 491, 237]<|/det|>First solution: More generally, we show that any affine k-dimensional plane in  \( R^{n} \)  can contain at most  \( 2^{k} \)  points in Z. The proof is by induction on  \( k + n \) ; the case k = n = 0 is clearly true.
<|det|>text [123, 242, 491, 386]<|/det|>Suppose that \( V \) is a \( k \)-plane in \( \mathbb{R}^n \). Denote the hyperplanes \( \{x_n = 0\} \) and \( \{x_n = 1\} \) by \( V_0 \) and \( V_1 \), respectively. If \( V \cap V_0 \) and \( V \cap V_1 \) are each at most \( (k - 1) \)-dimensional, then \( V \cap V_0 \cap Z \) and \( V \cap V_1 \cap Z \) each have cardinality at most \( 2^{k-1} \) by the induction assumption, and hence \( V \cap Z \) has at most \( 2^k \) elements. Otherwise, if \( V \cap V_0 \) or \( V \cap V_1 \) is \( k \)-dimensional, then \( V \subset V_0 \) or \( V \subset V_1 \); now apply the induction hypothesis on \( V \), viewed as a subset of \( \mathbb{R}^{n-1} \) by dropping the last coordinate.
<|det|>text [123, 392, 490, 508]<|/det|>Second solution: Let \( S \) be a subset of \( Z \) contained in a \( k \)-dimensional subspace of \( V \). This is equivalent to asking that any \( t_1, \ldots, t_{k+1} \in S \) satisfy a nontrivial linear dependence \( c_1t_1 + \cdots + c_{k+1}t_{k+1} = 0 \) with \( c_1, \ldots, c_{k+1} \in \mathbb{R} \). Since \( t_1, \ldots, t_{k+1} \in \mathbb{Q}^n \), given such a dependence we can always find another one with \( c_1, \ldots, c_{k+1} \in \mathbb{Q} \); then by clearing denominators, we can find one with \( c_1, \ldots, c_{k+1} \in \mathbb{Z} \) and not all having a common factor.
<|det|>text [123, 512, 491, 629]<|/det|>Let \(\mathbb{F}_2\) denote the field of two elements, and let \(\overline{S} \subseteq \mathbb{F}_2^n\) be the reductions modulo 2 of the points of \(S\). Then any \(t_1, \ldots, t_{k+1} \in \overline{S}\) satisfy a nontrivial linear dependence, because we can take the dependence from the end of the previous paragraph and reduce modulo 2. Hence \(\overline{S}\) is contained in a \(k\)-dimensional subspace of \(\mathbb{F}_{2^n}\), and the latter has cardinality exactly \(2^k\). Thus \(\overline{S}\) has at most \(2^k\) elements, as does \(S\).
<|det|>text [123, 633, 490, 720]<|/det|>Variant (suggested by David Savitt): if  \( \overline{S} \)  contained  \( k+1 \)  linearly independent elements, the  \( (k+1)\times n \)  matrix formed by these would have a nonvanishing maximal minor. The lift of that minor back to R would also not vanish, so S would contain  \( k+1 \)  linearly independent elements.
<|det|>text [123, 726, 491, 842]<|/det|>Third solution: (by Catalan Zara) Let V be a k-dimensional subspace. Form the matrix whose rows are the elements of  \( V \cap Z \) ; by construction, it has row rank at most k. It thus also has column rank at most k; in particular, we can choose k coordinates such that each point of  \( V \cap Z \)  is determined by those k of its coordinates. Since each coordinate of a point in Z can only take two values,  \( V \cap Z \)  can have at most  \( 2^{k} \)  elements.
<|det|>text [123, 846, 492, 934]<|/det|>Remark: The proposers probably did not realize that this problem appeared online about three months before the exam, at http://www.artofproblemsolving.com/Forum/viewtopic.php?t=105991. (It may very well have also appeared even earlier.)
<|det|>text [521, 65, 752, 80]<|/det|>B-5 The answer is 1/16. We have
<|det|>equation [608, 91, 829, 192]<|/det|>\[
\begin{array}{l} \int_ {0} ^ {1} x ^ {2} f (x) d x - \int_ {0} ^ {1} x f (x) ^ {2} d x \\ = \int_ {0} ^ {1} (x ^ {3} / 4 - x (f (x) - x / 2) ^ {2}) d x \\ \leq \int_ {0} ^ {1} x ^ {3} / 4 d x = 1 / 1 6, \\ \end{array}
\]
<|det|>text [555, 201, 766, 217]<|/det|>with equality when \( f(x) = x / 2 \).
<|det|>text [521, 226, 921, 320]<|/det|>B-6 First solution: We start with some easy upper and lower bounds on \( a_{n} \). We write \( O(f(n)) \) and \( \Omega(f(n)) \) for functions \( g(n) \) such that \( f(n) / g(n) \) and \( g(n) / f(n) \), respectively, are bounded above. Since \( a_{n} \) is a nondecreasing sequence, \( a_{n+1} - a_{n} \) is bounded above, so \( a_{n} = O(n) \). That means \( a_{n}^{-1/k} = \Omega(n^{-1/k}) \), so
<|det|>equation [599, 329, 834, 371]<|/det|>\[
a _ {n} = \Omega \left(\sum_ {i = 1} ^ {n} i ^ {- 1 / k}\right) = \Omega (n ^ {(k - 1) / k}).
\]
<|det|>text [555, 380, 880, 394]<|/det|>In fact, all we will need is that \(a_{n} \to \infty\) as \(n \to \infty\).
<|det|>text [554, 399, 920, 428]<|/det|>By Taylor's theorem with remainder, for \(1 < m < 2\) and \(x > 0\),
<|det|>equation [600, 440, 834, 470]<|/det|>\[
\left| (1 + x) ^ {m} - 1 - m x \right| \leq \frac {m (m - 1)}{2} x ^ {2}.
\]
<|det|>text [555, 480, 920, 512]<|/det|>Taking \( m = (k + 1) / k \) and \( x = a_{n + 1} / a_n = 1 + a_n^{-(k + 1) / k} \), we obtain
<|det|>equation [562, 520, 871, 555]<|/det|>\[
\left| a _ {n + 1} ^ {(k + 1) / k} - a _ {n} ^ {(k + 1) / k} - \frac {k + 1}{k} \right| \leq \frac {k + 1}{2 k ^ {2}} a _ {n} ^ {- (k + 1) / k}.
\]
<|det|>text [555, 565, 643, 580]<|/det|>In particular,
<|det|>equation [609, 589, 824, 620]<|/det|>\[
\lim _ {n \rightarrow \infty} a _ {n + 1} ^ {(k + 1) / k} - a _ {n} ^ {(k + 1) / k} = \frac {k + 1}{k}.
\]
<|det|>text [554, 634, 920, 662]<|/det|>In general, if \( x_{n} \) is a sequence with \( \lim_{n\to \infty}x_n = c \), then also
<|det|>equation [663, 672, 771, 707]<|/det|>\[
\lim _ {n \rightarrow \infty} \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} = c
\]
<|det|>text [554, 718, 920, 748]<|/det|>by Cesaro's lemma. Explicitly, for any \(\varepsilon > 0\), we can find \(N\) such that \(|x_{n} - c| \leq \varepsilon / 2\) for \(n \geq N\), and then
<|det|>equation [580, 757, 857, 799]<|/det|>\[
\left| c - \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} \right| \leq \frac {n - N}{n} \frac {\varepsilon}{2} + \frac {N}{n} \left| \sum_ {i = 1} ^ {N} (c - x _ {i}) \right|;
\]
<|det|>text [555, 810, 836, 825]<|/det|>for \(n\) large, the right side is smaller than \(\varepsilon\).
<|det|>text [555, 830, 738, 844]<|/det|>In our case, we deduce that
<|det|>equation [642, 855, 780, 889]<|/det|>\[
\lim _ {n \rightarrow \infty} \frac {a _ {n} ^ {(k + 1) / k}}{n} = \frac {k + 1}{k}
\]
<|det|>text [555, 899, 602, 911]<|/det|>and so
<|det|>equation [636, 921, 797, 959]<|/det|>\[
\lim _ {n \rightarrow \infty} \frac {a _ {n} ^ {k + 1}}{n ^ {k}} = \left(\frac {k + 1}{k}\right) ^ {k},
\]
