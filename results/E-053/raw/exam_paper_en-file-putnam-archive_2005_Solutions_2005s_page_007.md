<|det|>page_number [913, 35, 923, 46]<|/det|>7
<|det|>text [125, 66, 490, 97]<|/det|>Third solution: (by Richard Stanley) The cycle indicator of the symmetric group  \( S_{n} \)  is defined by
<|det|>equation [166, 106, 408, 139]<|/det|>\[
Z _ {n} (x _ {1}, \ldots , x _ {n}) = \sum_ {\pi \in S _ {n}} x _ {1} ^ {c _ {1} (\pi)} \dots x _ {n} ^ {c _ {n} (\pi)},
\]
<|det|>text [125, 150, 490, 166]<|/det|>where \(c_{i}(\pi)\) is the number of cycles of \(\pi\) of length \(i\). Put
<|det|>equation [137, 176, 437, 207]<|/det|>\[
F _ {n} = \sum_ {\pi \in S _ {n}} \sigma (\pi) x ^ {\nu (\pi)} = Z _ {n} (x, - 1, 1, - 1, 1, \dots)
\]
<|det|>text [125, 218, 155, 230]<|/det|>and
<|det|>equation [163, 240, 412, 277]<|/det|>\[
f (n) = \sum_ {\pi \in S _ {n}} \frac {\sigma (\pi)}{\nu (\pi) + 1} = \int_ {0} ^ {1} F _ {n} (x) d x.
\]
<|det|>text [125, 288, 490, 318]<|/det|>A standard argument in enumerative combinatorics (the Exponential Formula) gives
<|det|>equation [168, 329, 406, 368]<|/det|>\[
\sum_ {n = 0} ^ {\infty} Z _ {n} (x _ {1}, \dots , x _ {n}) \frac {t ^ {n}}{n !} = \exp \sum_ {k = 1} ^ {\infty} x _ {k} \frac {t ^ {k}}{k},
\]
<|det|>text [125, 377, 185, 392]<|/det|>yielding
<|det|>equation [134, 400, 440, 540]<|/det|>\[
\begin{array}{l} \sum_ {n = 0} ^ {\infty} f (n) \frac {t ^ {n}}{n !} = \int_ {0} ^ {1} \exp \left(x t - \frac {t ^ {2}}{2} + \frac {t ^ {3}}{3} - \dots\right) d x \\ = \int_ {0} ^ {1} e ^ {(x - 1) t + \log (1 + t)} d x \\ = \int_ {0} ^ {1} (1 + t) e ^ {(x - 1) t} d x \\ = \frac {1}{t} (1 - e ^ {- t}) (1 + t). \\ \end{array}
\]
<|det|>text [554, 66, 920, 96]<|/det|>Expanding the right side as a Taylor series and comparing coefficients yields the desired result.
<|det|>text [554, 100, 920, 130]<|/det|>Fourth solution (sketch): (by David Savitt) We prove the identity of rational functions
<|det|>equation [587, 141, 845, 178]<|/det|>\[
\sum_ {\pi \in S _ {n}} \frac {\sigma (\pi)}{\nu (\pi) + x} = \frac {(- 1) ^ {n + 1} n ! (x + n - 1)}{x (x + 1) \cdots (x + n)}
\]
<|det|>text [553, 189, 920, 248]<|/det|>by induction on n, which for x = 1 implies the desired result. (This can also be deduced as in the other solutions, but in this argument it is necessary to formulate the strong induction hypothesis.)
<|det|>text [554, 252, 919, 282]<|/det|>Let \( R(n,x) \) be the right hand side of the above equation. It is easy to verify that
<|det|>equation [565, 293, 868, 365]<|/det|>\[
\begin{array}{l} R (x, n) = R (x + 1, n - 1) + (n - 1)! \frac {(- 1) ^ {n + 1}}{x} \\ + \sum_ {l = 2} ^ {n - 1} (- 1) ^ {l - 1} \frac {(n - 1) !}{(n - l) !} R (x, n - l), \\ \end{array}
\]
<|det|>text [553, 375, 920, 462]<|/det|>since the sum telescopes. To prove the desired equality, it suffices to show that the left hand side satisfies the same recurrence. This follows because we can classify each  \( \pi \in S_{n} \)  as either fixing n, being an n-cycle, or having n in an l-cycle for one of  \( l = 2, \ldots, n - 1 \) ; writing the sum over these classes gives the desired recurrence.
