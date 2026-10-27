<|det|>page_number [912, 35, 923, 47]<|/det|>2
<|det|>text [125, 66, 208, 79]<|/det|>and \(n\). Thus
<|det|>equation [140, 83, 430, 201]<|/det|>\[
\begin{array}{l} 2 S = \sum_ {m} \sum_ {n} \left(\frac {1}{a _ {m} (a _ {m} + a _ {n})} + \frac {1}{a _ {n} (a _ {m} + a _ {n})}\right) \\ = \sum_ {m} \sum_ {n} \frac {1}{a _ {m} a _ {n}} \\ = \left(\sum_ {n = 1} ^ {\infty} \frac {n}{3 ^ {n}}\right) ^ {2}. \\ \end{array}
\]
<|det|>text [125, 206, 154, 218]<|/det|>But
<|det|>equation [248, 224, 326, 258]<|/det|>\[
\sum_ {n = 1} ^ {\infty} \frac {n}{3 ^ {n}} = \frac {3}{4}
\]
<|det|>text [125, 266, 310, 281]<|/det|>since, e.g., it's \( f'(1) \), where
<|det|>equation [208, 287, 366, 322]<|/det|>\[
f (x) = \sum_ {n = 0} ^ {\infty} \frac {x ^ {n}}{3 ^ {n}} = \frac {3}{3 - x},
\]
<|det|>text [125, 329, 336, 344]<|/det|>and we conclude that \( S = 9 / 32 \).
<|det|>text [91, 351, 491, 483]<|/det|>A-5 First solution: (by Reid Barton) Let \( r_1, \ldots, r_{1999} \) be the roots of \( P \). Draw a disc of radius \( \varepsilon \) around each \( r_i \), where \( \varepsilon < 1/3998 \); this disc covers a subinterval of \([-1/2, 1/2]\) of length at most \( 2\varepsilon \), and so of the 2000 (or fewer) uncovered intervals in \([-1/2, 1/2]\), one, which we call \( I \), has length at least \( \delta = (1 - 3998\varepsilon)/2000 > 0 \). We will exhibit an explicit lower bound for the integral of \( |P(x)|/P(0) \) over this interval, which will yield such a bound for the entire integral.
<|det|>text [125, 486, 192, 499]<|/det|>Note that
<|det|>equation [215, 505, 361, 542]<|/det|>\[
\frac {| P (x) |}{| P (0) |} = \prod_ {i = 1} ^ {1 9 9 9} \frac {| x - r _ {i} |}{| r _ {i} |}.
\]
<|det|>text [125, 548, 490, 586]<|/det|>Also note that by construction, \( |x - r_i| \geq \varepsilon \) for each \( x \in I \). If \( |r_i| \leq 1 \), then we have \( \frac{|x - r_i|}{|r_i|} \geq \varepsilon \). If \( |r_i| > 1 \), then
<|det|>equation [136, 592, 438, 625]<|/det|>\[
\frac {| x - r _ {i} |}{| r _ {i} |} = | 1 - x / r _ {i} | \geq 1 - | x / r _ {i} | \geq = 1 / 2 > \varepsilon .
\]
<|det|>text [124, 630, 490, 659]<|/det|>We conclude that \(\int_{I}|P(x) / P(0)|dx\geq \delta \varepsilon\) , independent of \(P\)
<|det|>text [124, 663, 490, 740]<|/det|>Second solution: It will be a bit more convenient to assume \( P(0) = 1 \) (which we may achieve by rescaling unless \( P(0) = 0 \), in which case there is nothing to prove) and to prove that there exists \( D > 0 \) such that \( \int_{-1}^{1}|P(x)|dx \geq D \), or even such that \( \int_0^1 |P(x)|dx \geq D \).
<|det|>text [124, 741, 490, 842]<|/det|>We first reduce to the case where \( P \) has all of its roots in [0, 1]. If this is not the case, we can factor \( P(x) \) as \( Q(x)R(x) \), where \( Q \) has all roots in the interval and \( R \) has none. Then \( R \) is either always positive or always negative on [0, 1]; assume the former. Let \( k \) be the largest positive real number such that \( R(x) - kx \geq 0 \) on [0, 1]; then
<|det|>equation [150, 846, 424, 912]<|/det|>\[
\begin{array}{l} \int_ {- 1} ^ {1} | P (x) | d x = \int_ {- 1} ^ {1} | Q (x) R (x) | d x \\ > \int_ {- 1} ^ {1} | Q (x) (R (x) - k x) | d x, \\ \end{array}
\]
<|det|>text [554, 66, 920, 141]<|/det|>and \( Q(x)(R(x) - kx) \) has more roots in [0, 1] than does \( P \) (and has the same value at 0). Repeating this argument shows that \( \int_0^1 |P(x)| dx \) is greater than the corresponding integral for some polynomial with all of its roots in [0, 1].
<|det|>text [555, 145, 768, 160]<|/det|>Under this assumption, we have
<|det|>equation [649, 171, 784, 209]<|/det|>\[
P (x) = c \prod_ {i = 1} ^ {1 9 9 9} (x - r _ {i})
\]
<|det|>text [555, 220, 729, 235]<|/det|>for some \(r_i \in (0,1]\). Since
<|det|>equation [646, 244, 787, 265]<|/det|>\[
P (0) = - c \prod r _ {i} = 1,
\]
<|det|>text [555, 275, 613, 287]<|/det|>we have
<|det|>equation [655, 299, 776, 320]<|/det|>\[
| c | \geq \prod | r _ {i} ^ {- 1} | \geq 1.
\]
<|det|>text [554, 333, 920, 438]<|/det|>Thus it suffices to prove that if \( Q(x) \) is a monic polynomial of degree 1999 with all of its roots in [0, 1], then \( \int_0^1 |Q(x)| dx \geq D \) for some constant \( D > 0 \). But the integral of \( \int_0^1 \prod_{i=1}^{1999} |x - r_i| dx \) is a continuous function for \( r_i \in [0, 1] \). The product of all of these intervals is compact, so the integral achieves a minimum value for some \( r_i \). This minimum is the desired \( D \).
<|det|>text [554, 443, 919, 473]<|/det|>Third solution (by Abe Kunin): It suffices to prove the stronger inequality
<|det|>equation [613, 484, 822, 520]<|/det|>\[
\sup _ {x \in [ - 1, 1 ]} | P (x) | \leq C \int_ {- 1} ^ {1} | P (x) | d x
\]
<|det|>text [553, 530, 920, 648]<|/det|>holds for some C. But this follows immediately from the following standard fact: any two norms on a finite-dimensional vector space (here the polynomials of degree at most 1999) are equivalent. (The proof of this statement is also a compactness argument: C can be taken to be the maximum of the L1-norm divided by the sup norm over the set of polynomials with L1-norm 1.)
<|det|>text [553, 652, 920, 737]<|/det|>Note: combining the first two approaches gives a constructive solution with a constant that is better than that given by the first solution, but is still far from optimal. I don't know offhand whether it is even known what the optimal constant and/or the polynomials achieving that constant are.
<|det|>text [520, 748, 919, 777]<|/det|>A–6 Rearranging the given equation yields the much more tractable equation
<|det|>equation [632, 787, 801, 817]<|/det|>\[
\frac {a _ {n}}{a _ {n - 1}} = 6 \frac {a _ {n - 1}}{a _ {n - 2}} - 8 \frac {a _ {n - 2}}{a _ {n - 3}}.
\]
<|det|>text [554, 826, 920, 869]<|/det|>Let \( b_{n} = a_{n} / a_{n - 1} \); with the initial conditions \( b_{2} = 2, b_{3} = 12 \), one easily obtains \( b_{n} = 2^{n - 1}(2^{n - 2} - 1) \), and so
<|det|>equation [629, 880, 804, 916]<|/det|>\[
a _ {n} = 2 ^ {n (n - 1) / 2} \prod_ {i = 1} ^ {n - 1} (2 ^ {i} - 1).
\]
