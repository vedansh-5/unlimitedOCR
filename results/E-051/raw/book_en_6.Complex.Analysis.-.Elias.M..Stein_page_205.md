<|det|>page_number [246, 64, 275, 77]<|/det|>186
<|det|>header [302, 64, 788, 78]<|/det|>Chapter 7. THE ZETA FUNCTION AND PRIME NUMBER THEOREM
<|det|>text [243, 94, 545, 110]<|/det|>which holds for \(0 \leq x < 1\), we find that
<|det|>equation [286, 121, 744, 164]<|/det|>\[
\log \zeta (s) = \log \prod_ {p} \frac {1}{1 - p ^ {- s}} = \sum_ {p} \log \left(\frac {1}{1 - p ^ {- s}}\right) = \sum_ {p, m} \frac {p ^ {- m s}}{m}.
\]
<|det|>text [242, 176, 789, 273]<|/det|>Since the double sum converges absolutely, we need not specify the order of summation. See the Note at the end of this chapter. The formula then holds for all  \( \operatorname{Re}(s) > 1 \)  by analytic continuation. Note that, by Theorem 6.2 in Chapter 3,  \( \log \zeta(s) \)  is well defined in the simply connected half-plane  \( \operatorname{Re}(s) > 1 \) , since  \( \zeta \)  has no zeros there. Finally, it is clear that we have
<|det|>equation [424, 282, 606, 325]<|/det|>\[
\sum_ {p, m} \frac {p ^ {- m s}}{m} = \sum_ {n = 1} ^ {\infty} c _ {n} n ^ {- s},
\]
<|det|>text [243, 338, 614, 355]<|/det|>where \( c_{n} = 1 / m \) if \( n = p^{m} \) and \( c_{n} = 0 \) otherwise.
<|det|>text [242, 363, 787, 396]<|/det|>The proof of the theorem we shall give depends on a simple trick that is based on the following inequality.
<|det|>text [243, 405, 635, 421]<|/det|>Lemma 1.4 If \(\theta \in \mathbb{R}\), then \(3 + 4\cos \theta + \cos 2\theta \geq 0\).
<|det|>text [260, 431, 631, 447]<|/det|>This follows at once from the simple observation
<|det|>equation [382, 460, 647, 479]<|/det|>\[
3 + 4 \cos \theta + \cos 2 \theta = 2 (1 + \cos \theta) ^ {2}.
\]
<|det|>text [243, 493, 572, 509]<|/det|>Corollary 1.5 If \(\sigma > 1\) and \(t\) is real, then
<|det|>equation [382, 522, 647, 542]<|/det|>\[
\log | \zeta^ {3} (\sigma) \zeta^ {4} (\sigma + i t) \zeta (\sigma + 2 i t) | \geq 0.
\]
<|det|>text [261, 555, 540, 571]<|/det|>Proof. Let \( s = \sigma + it \) and note that
<|det|>equation [255, 583, 775, 603]<|/det|>\[
\operatorname{Re} \left(n ^ {- s}\right) = \operatorname{Re} \left(e ^ {- (\sigma + i t) \log n}\right) = e ^ {- \sigma \log n} \cos (t \log n) = n ^ {- \sigma} \cos (t \log n).
\]
<|det|>text [244, 617, 326, 632]<|/det|>Therefore,
<|det|>equation [308, 640, 731, 737]<|/det|>\[
\begin{array}{l} \log | \zeta^ {3} (\sigma) \zeta^ {4} (\sigma + i t) \zeta (\sigma + 2 i t) | \\ = 3 \log | \zeta (\sigma) | + 4 \log | \zeta (\sigma + i t) | + \log | \zeta (\sigma + 2 i t) | \\ = 3 \operatorname{Re} [ \log \zeta (\sigma) ] + 4 \operatorname{Re} [ \log \zeta (\sigma + i t) ] + \operatorname{Re} [ \log \zeta (\sigma + 2 i t) ] \\ = \sum c _ {n} n ^ {- \sigma} (3 + 4 \cos \theta_ {n} + \cos 2 \theta_ {n}), \\ \end{array}
\]
<|det|>text [243, 748, 787, 780]<|/det|>where \(\theta_{n} = t\log n\). The positivity now follows from Lemma 1.4, and the fact that \(c_{n}\geq 0\).
