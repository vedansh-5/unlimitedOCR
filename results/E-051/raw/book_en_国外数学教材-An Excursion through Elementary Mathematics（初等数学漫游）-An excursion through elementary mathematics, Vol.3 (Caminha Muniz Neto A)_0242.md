<|det|>page_number [120, 52, 153, 65]<|/det|>236
<|det|>header [616, 52, 879, 68]<|/det|>9 Calculus and Number Theory
<|det|>text [117, 90, 427, 108]<|/det|>Proof Firstly, from (9.14) we get
<|det|>equation [235, 123, 877, 230]<|/det|>\[
\begin{array}{l} \left| P _ {n} - \sum_ {k = 1} ^ {n} \frac {\mu (k)}{k ^ {2}} \right| = \left| \sum_ {k = 1} ^ {n} \mu (k) \left(\frac {1}{n ^ {2}} \left\lfloor \frac {n}{k} \right\rfloor^ {2} - \frac {1}{k ^ {2}}\right) \right| \tag {9.15} \\ \leq \sum_ {k = 1} ^ {n} \left| \frac {1}{k ^ {2}} - \frac {1}{n ^ {2}} \left\lfloor \frac {n}{k} \right\rfloor^ {2} \right|. \\ \end{array}
\]
<|det|>text [117, 246, 879, 281]<|/det|>In order to estimate the last sum above, we claim that, given natural numbers \( n \) and \( k \) such that \( 1 \leq k \leq n \), we have
<|det|>equation [357, 296, 639, 336]<|/det|>\[
\left| \frac {1}{k ^ {2}} - \frac {1}{n ^ {2}} \left\lfloor \frac {n}{k} \right\rfloor^ {2} \right| <   \frac {2}{n k} - \frac {1}{n ^ {2}}.
\]
<|det|>text [117, 351, 192, 367]<|/det|>Indeed,
<|det|>equation [233, 382, 768, 510]<|/det|>\[
\begin{array}{l} \frac {n}{k} - 1 <   \left\lfloor \frac {n}{k} \right\rfloor \leq \frac {n}{k} \Rightarrow \frac {n ^ {2}}{k ^ {2}} - \frac {2 n}{k} + 1 <   \left\lfloor \frac {n}{k} \right\rfloor^ {2} \leq \frac {n ^ {2}}{k ^ {2}} \\ \Rightarrow \frac {1}{k ^ {2}} - \frac {2}{k n} + \frac {1}{n ^ {2}} <   \frac {1}{n ^ {2}} \left\lfloor \frac {n}{k} \right\rfloor^ {2} \leq \frac {1}{k ^ {2}} \\ \Rightarrow 0 \leq \frac {1}{k ^ {2}} - \frac {1}{n ^ {2}} \left\lfloor \frac {n}{k} \right\rfloor^ {2} <   \frac {2}{k n} - \frac {1}{n ^ {2}}, \\ \end{array}
\]
<|det|>text [117, 521, 218, 536]<|/det|>as wished.
<|det|>text [145, 539, 655, 555]<|/det|>Back to (9.15), we obtain from the above estimates that
<|det|>equation [251, 571, 748, 621]<|/det|>\[
\left| P _ {n} - \sum_ {k = 1} ^ {n} \frac {\mu (k)}{k ^ {2}} \right| <   \sum_ {k = 1} ^ {n} \left(\frac {2}{n k} - \frac {1}{n ^ {2}}\right) = \frac {2}{n} \sum_ {k = 1} ^ {n} \frac {1}{k} - \frac {1}{n}.
\]
<|det|>text [117, 637, 438, 655]<|/det|>Now, from L'Hôpital's rule we get
<|det|>equation [263, 671, 738, 719]<|/det|>\[
\frac {2}{n} \sum_ {k = 1} ^ {n} \frac {1}{k} <   \frac {2}{n} \left(1 + \int_ {1} ^ {n} \frac {1}{t} d t\right) = \frac {2}{n} (\log n + 1) \rightarrow 0
\]
<|det|>text [117, 736, 316, 752]<|/det|>as \(n\to +\infty\) . Hence,
<|det|>equation [363, 768, 634, 819]<|/det|>\[
\lim _ {n \rightarrow + \infty} \left(\frac {2}{n} \sum_ {k = 1} ^ {n} \frac {1}{k} - \frac {1}{n}\right) = 0,
\]
<|det|>text [117, 833, 471, 850]<|/det|>and our previous estimates assure that
