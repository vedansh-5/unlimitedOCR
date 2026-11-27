<|det|>title [118, 52, 267, 67]<|/det|>3.2 Power Series
<|det|>page_number [856, 53, 880, 66]<|/det|>75
<|det|>text [117, 90, 879, 126]<|/det|>For future use, we notice that changing \( x \) by \( ax \) in the equality of the previous example, we get
<|det|>equation [421, 142, 880, 188]<|/det|>\[
e ^ {a x} = \sum_ {n \geq 0} \frac {a ^ {n}}{n !} x ^ {n} \tag {3.8}
\]
<|det|>text [117, 204, 272, 220]<|/det|>for every \(x \in \mathbb{R}\).
<|det|>text [117, 222, 880, 257]<|/det|>A variation of the argument used in Example 3.8 allows us to expand \( f(x) = (1 + x)^{\alpha} \) in power series when \( |x| < 1 \) (and for a fixed real number \( \alpha \neq 0 \)).
<|det|>text [117, 258, 880, 295]<|/det|>To this end, given \(\alpha \in \mathbb{R}\) and \(n\in \mathbb{Z}\setminus \{0\}\), we begin by defining the generalized binomial number \(\binom{\alpha}{n}\) by letting \(\binom{\alpha}{0} = 1\) and, for \(n\geq 1\),
<|det|>equation [303, 312, 880, 351]<|/det|>\[
\binom {\alpha} {n} = \frac {\alpha (\alpha - 1) (\alpha - 2) \dots (\alpha - n + 1)}{n !}. \tag {3.9}
\]
<|det|>text [117, 366, 557, 383]<|/det|>Lemma 3.9 Given \(\alpha \in \mathbb{R}\) and \(n\in \mathbb{N}\), we have:
<|det|>text [117, 390, 356, 413]<|/det|>(a) \(\binom{\alpha}{n} = \binom{\alpha - 1}{n} + \binom{\alpha - 1}{n - 1}\).
<|det|>text [117, 414, 446, 436]<|/det|>(b) \(\frac{n}{\alpha}\binom{\alpha}{n} = \binom{\alpha - 1}{n - 1}\), for every \(\alpha \neq 0\).
<|det|>text [119, 436, 417, 455]<|/det|>(c) \(\left|\binom{\alpha}{n}\right| \leq 1\) whenever \(|\alpha| \leq 1\).
<|det|>text [117, 463, 179, 480]<|/det|>Proof
<|det|>text [117, 490, 377, 508]<|/det|>(a) Is an easy computation:
<|det|>equation [202, 520, 837, 740]<|/det|>\[
\begin{array}{l} \binom {\alpha} {n} - \binom {\alpha - 1} {n} = \frac {1}{n !} \alpha (\alpha - 1) (\alpha - 2) \dots (\alpha - n + 1) \\ - \frac {1}{n !} (\alpha - 1) (\alpha - 2) \dots (\alpha - n) \\ = \frac {1}{n !} (\alpha - 1) (\alpha - 2) \dots (\alpha - n + 1) (\alpha - (\alpha - n)) \\ = \frac {1}{(n - 1) !} (\alpha - 1) (\alpha - 2) \dots (\alpha - n + 1) \\ = \binom {\alpha - 1} {n - 1}. \\ \end{array}
\]
<|det|>text [117, 752, 457, 770]<|/det|>(b) Follows immediately from (3.9).
<|det|>text [117, 788, 731, 807]<|/det|>(c) If \( |\alpha| \leq 1 \), it follows from (3.9) and the triangle inequality that
<|det|>equation [195, 821, 838, 862]<|/det|>\[
\left| \binom {\alpha} {n} \right| \leq \frac {| \alpha | (| \alpha | + 1) (| \alpha | + 2) \dots (| \alpha | + n - 1)}{n !} \leq \frac {1 \cdot 2 \cdot \dots \cdot n}{n !} = 1.
\]
