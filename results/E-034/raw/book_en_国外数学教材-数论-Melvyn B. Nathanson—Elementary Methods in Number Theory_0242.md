<|det|>page_number [142, 45, 178, 60]<|/det|>234
<|det|>header [220, 44, 412, 60]<|/det|>7. Divisor Functions
<|det|>equation [242, 81, 700, 297]<|/det|>\[
\begin{array}{l} = 2 \sum_ {1 \leq u \leq \sqrt {x}} \left[ \frac {x}{u} \right] - \left[ \sqrt {x} \right] ^ {2} \\ = 2 \sum_ {1 \leq u \leq \sqrt {x}} \left(\frac {x}{u} - \left\{\frac {x}{u} \right\}\right) - \left(\sqrt {x} - \left\{\sqrt {x} \right\}\right) ^ {2} \\ = 2 x \sum_ {1 \leq u \leq \sqrt {x}} \frac {1}{u} - 2 \sum_ {1 \leq u \leq \sqrt {x}} \left\{\frac {x}{u} \right\} - x + O (\sqrt {x}) \\ = 2 x \left(\log \sqrt {x} + \gamma + O \left(\frac {1}{\sqrt {x}}\right)\right) - x + O (\sqrt {x}) \\ = x \log x + (2 \gamma - 1) x + O (\sqrt {x}). \\ \end{array}
\]
<|det|>text [140, 314, 419, 334]<|/det|>This completes the proof.
<|det|>text [140, 385, 398, 403]<|/det|>Theorem 7.4 For \(x \geq 1\),
<|det|>equation [284, 418, 715, 463]<|/det|>\[
\Delta (x) = \sum_ {n \leq x} (\log n - d (n) + 2 \gamma) = O \left(x ^ {1 / 2}\right).
\]
<|det|>text [162, 479, 484, 497]<|/det|>Proof. By Theorem 7.3 we have
<|det|>equation [290, 513, 712, 556]<|/det|>\[
\sum_ {n \leq x} d (n) = x \log x + (2 \gamma - 1) x + O \left(x ^ {1 / 2}\right).
\]
<|det|>text [140, 573, 387, 591]<|/det|>By Theorem 6.4 we have
<|det|>equation [331, 608, 667, 648]<|/det|>\[
\sum_ {n \leq x} \log n = x \log x - x + O (\log x).
\]
<|det|>text [139, 665, 704, 684]<|/det|>Subtracting the first equation from the second, we obtain
<|det|>equation [168, 700, 834, 743]<|/det|>\[
\sum_ {n \leq x} (\log n - d (n) + 2 \gamma) = O \left(x ^ {1 / 2}\right) - 2 \gamma \{x \} + O (\log x) = O \left(x ^ {1 / 2}\right).
\]
<|det|>text [138, 811, 865, 947]<|/det|>An ordered factorization of the positive integer n into exactly  \( \ell \)  factors is an  \( \ell \) -tuple  \( (d_{1},\ldots,d_{\ell}) \)  such that  \( n=d_{1}\cdots d_{\ell} \) . The divisor function  \( d(n) \)  counts the number of ordered factorizations of n into exactly two factors, since each factorization  \( n=dd' \)  is completely determined by the first factor d. For every positive integer  \( \ell \) , we define the arithmetic function  \( d_{\ell}(n) \)  as the number of factorizations of n into exactly  \( \ell \)  factors. Then  \( d_{1}(n)=1 \)  and  \( d_{2}(n)=d(n) \)  for all n.
