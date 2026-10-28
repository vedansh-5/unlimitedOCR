<|det|>page_number [912, 35, 923, 47]<|/det|>7
<|det|>text [125, 66, 198, 79]<|/det|>as desired.
<|det|>text [124, 85, 490, 145]<|/det|>Remark: The use of Cesaro's lemma above is the special case \( b_{n} = n \) of the Cesaro-Stolz theorem: if \( a_{n}, b_{n} \) are sequences such that \( b_{n} \) is positive, strictly increasing, and unbounded, and
<|det|>equation [220, 156, 355, 186]<|/det|>\[
\lim _ {n \to \infty} \frac {a _ {n + 1} - a _ {n}}{b _ {n + 1} - b _ {n}} = L,
\]
<|det|>text [125, 197, 159, 209]<|/det|>then
<|det|>equation [245, 218, 331, 248]<|/det|>\[
\lim _ {n \to \infty} \frac {a _ {n}}{b _ {n}} = L.
\]
<|det|>text [124, 262, 491, 320]<|/det|>Second solution: In this solution, rather than applying Taylor's theorem with remainder to \((1 + x)^m\) for \(1 < m < 2\) and \(x > 0\), we only apply convexity to deduce that \((1 + x)^m \geq 1 + mx\). This gives
<|det|>equation [194, 330, 381, 360]<|/det|>\[
a _ {n + 1} ^ {(k + 1) / k} - a _ {n} ^ {(k + 1) / k} \geq \frac {k + 1}{k},
\]
<|det|>text [125, 370, 172, 383]<|/det|>and so
<|det|>equation [214, 392, 361, 423]<|/det|>\[
a _ {n} ^ {(k + 1) / k} \geq \frac {k + 1}{k} n + c
\]
<|det|>text [125, 433, 321, 448]<|/det|>for some \(c\in \mathbb{R}\) . In particular,
<|det|>equation [208, 458, 367, 493]<|/det|>\[
\operatorname * {l i m i n f} _ {n \to \infty} \frac {a _ {n} ^ {(k + 1) / k}}{n} \geq \frac {k + 1}{k}
\]
<|det|>text [125, 503, 172, 516]<|/det|>and so
<|det|>equation [170, 526, 404, 565]<|/det|>\[
\operatorname * {l i m i n f} _ {n \to \infty} \frac {a _ {n}}{n ^ {k / (k + 1)}} \geq \left(\frac {k + 1}{k}\right) ^ {k / (k + 1)}.
\]
<|det|>text [125, 573, 368, 588]<|/det|>But turning this around, the fact that
<|det|>equation [150, 601, 422, 680]<|/det|>\[
\begin{array}{l} a _ {n + 1} - a _ {n} \\ = a _ {n} ^ {- 1 / k} \\ \leq \left(\frac {k + 1}{k}\right) ^ {- 1 / (k + 1)} n ^ {- 1 / (k + 1)} (1 + o (1)), \\ \end{array}
\]
<|det|>text [124, 689, 490, 719]<|/det|>where \(o(1)\) denotes a function tending to 0 as \(n \to \infty\), yields
<|det|>equation [139, 732, 435, 864]<|/det|>\[
\begin{array}{l} a _ {n} \\ \leq \left(\frac {k + 1}{k}\right) ^ {- 1 / (k + 1)} \sum_ {i = 1} ^ {n} i ^ {- 1 / (k + 1)} (1 + o (1)) \\ = \frac {k + 1}{k} \left(\frac {k + 1}{k}\right) ^ {- 1 / (k + 1)} n ^ {k / (k + 1)} (1 + o (1)) \\ = \left(\frac {k + 1}{k}\right) ^ {k / (k + 1)} n ^ {k / (k + 1)} (1 + o (1)), \\ \end{array}
\]
<|det|>text [126, 875, 145, 886]<|/det|>SO
<|det|>equation [171, 896, 402, 935]<|/det|>\[
\limsup _ {n \to \infty} \frac {a _ {n}}{n ^ {k / (k + 1)}} \leq \left(\frac {k + 1}{k}\right) ^ {k / (k + 1)}
\]
<|det|>text [555, 66, 748, 81]<|/det|>and this completes the proof.
<|det|>text [554, 85, 921, 129]<|/det|>Third solution: We argue that  \( a_{n} \rightarrow \infty \)  as in the first solution. Write  \( b_{n} = a_{n} - Ln^{k/(k+1)} \) , for a value of L to be determined later. We have
<|det|>equation [571, 143, 862, 199]<|/det|>\[
\begin{array}{l} b _ {n + 1} \\ = b _ {n} + a _ {n} ^ {- 1 / k} - L ((n + 1) ^ {k / (k + 1)} - n ^ {k / (k + 1)}) \\ = e _ {1} + e _ {2}, \\ \end{array}
\]
<|det|>text [556, 211, 600, 223]<|/det|>where
<|det|>equation [605, 233, 826, 295]<|/det|>\[
\begin{array}{l} e _ {1} = b _ {n} + a _ {n} ^ {- 1 / k} - L ^ {- 1 / k} n ^ {- 1 / (k + 1)} \\ e _ {2} = L ((n + 1) ^ {k / (k + 1)} - n ^ {k / (k + 1)}) \\ - L ^ {- 1 / k} n ^ {- 1 / (k + 1)}. \\ \end{array}
\]
<|det|>text [554, 308, 919, 337]<|/det|>We first estimate \( e_1 \). For \( -1 < m < 0 \), by the convexity of \( (1 + x)^m \) and \( (1 + x)^{1 - m} \), we have
<|det|>equation [624, 348, 810, 385]<|/det|>\[
\begin{array}{l} 1 + m x \leq (1 + x) ^ {m} \\ \leq 1 + m x (1 + x) ^ {m - 1}. \\ \end{array}
\]
<|det|>text [556, 397, 602, 410]<|/det|>Hence
<|det|>equation [590, 420, 843, 480]<|/det|>\[
\begin{array}{l} - \frac {1}{k} L ^ {- (k + 1) / k} n ^ {- 1} b _ {n} \leq e _ {1} - b _ {n} \\ \leq - \frac {1}{k} b _ {n} a _ {n} ^ {- (k + 1) / k}. \\ \end{array}
\]
<|det|>text [554, 490, 920, 548]<|/det|>Note that both bounds have sign opposite to  \( b_{n} \) ; moreover, by the bound  \( a_{n} = \Omega(n^{(k-1)/k}) \) , both bounds have absolutely value strictly less than that of  \( b_{n} \)  for n sufficiently large. Consequently, for n large,
<|det|>equation [677, 560, 754, 576]<|/det|>\[
\left| e _ {1} \right| \leq \left| b _ {n} \right|.
\]
<|det|>text [554, 587, 919, 617]<|/det|>We now work on \( e_2 \). By Taylor's theorem with remainder applied to \( (1 + x)^m \) for \( x > 0 \) and \( 0 < m < 1 \),
<|det|>equation [610, 627, 824, 678]<|/det|>\[
\begin{array}{l} 1 + m x \geq (1 + x) ^ {m} \\ \geq 1 + m x + \frac {m (m - 1)}{2} x ^ {2}. \\ \end{array}
\]
<|det|>text [554, 689, 920, 739]<|/det|>The “main term” of  \( L((n+1)^{k/(k+1)}-n^{k/(k+1)}) \)  is  \( L\frac{k}{k+1}n^{-1/(k+1)} \) . To make this coincide with  \( L^{-1/k}n^{-1/(k+1)} \) , we take
<|det|>equation [644, 750, 788, 786]<|/det|>\[
L = \left(\frac {k + 1}{k}\right) ^ {k / (k + 1)}.
\]
<|det|>text [555, 796, 672, 810]<|/det|>We then find that
<|det|>equation [666, 821, 767, 839]<|/det|>\[
| e _ {2} | = O (n ^ {- 2}),
\]
<|det|>text [554, 849, 919, 879]<|/det|>and because \( b_{n+1} = e_1 + e_2 \), we have \( |b_{n+1}| \leq |b_n| + |e_2| \). Hence
<|det|>equation [624, 890, 810, 930]<|/det|>\[
| b _ {n} | = O \left(\sum_ {i = 1} ^ {n} i ^ {- 2}\right) = O (1),
\]
