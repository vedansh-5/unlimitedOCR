<|det|>page_number [141, 46, 167, 60]<|/det|>88
<|det|>header [210, 44, 631, 63]<|/det|>3. Primitive Roots and Quadratic Reciprocity
<|det|>text [137, 83, 865, 122]<|/det|>Proof. This follows immediately from Theorem 3.3, since \( |(\mathbf{Z} / p\mathbf{Z})^{\times}| = p - 1 \).
<|det|>text [161, 157, 819, 177]<|/det|>The following table lists the primitive roots for the first six primes.
<|det|>table [342, 186, 664, 322]<|/det|><table><tr><td>p</td><td>φ(p-1)</td><td>primitive roots</td></tr><tr><td>2</td><td>1</td><td>1</td></tr><tr><td>3</td><td>1</td><td>2</td></tr><tr><td>5</td><td>2</td><td>2,3</td></tr><tr><td>7</td><td>2</td><td>3,5</td></tr><tr><td>11</td><td>4</td><td>2,6,7,8</td></tr><tr><td>13</td><td>4</td><td>2,6,7,11</td></tr></table>
<|det|>text [139, 333, 865, 371]<|/det|>Let \( p \) be a prime, and let \( g \) be a primitive root modulo \( p \). If \( a \) is an integer not divisible by \( p \), then there exists a unique integer \( k \) such that
<|det|>equation [416, 381, 586, 403]<|/det|>\[
a \equiv g ^ {k} \pmod {p}
\]
<|det|>text [140, 414, 184, 430]<|/det|>and
<|det|>equation [398, 432, 602, 453]<|/det|>\[
k \in \{0, 1, \dots , p - 2 \}.
\]
<|det|>text [139, 458, 863, 495]<|/det|>This integer \( k \) is called the index of \( a \) with respect to the primitive root \( g \), and is denoted by
<|det|>equation [439, 496, 561, 518]<|/det|>\[
k = \operatorname{ind} _ {g} (a).
\]
<|det|>text [139, 523, 643, 542]<|/det|>If \( k_{1} \) and \( k_{2} \) are any integers such that \( k_{1} \leq k_{2} \) and
<|det|>equation [379, 551, 624, 573]<|/det|>\[
a \equiv g ^ {k _ {1}} \equiv g ^ {k _ {2}} \pmod {p},
\]
<|det|>text [140, 584, 190, 599]<|/det|>then
<|det|>equation [392, 599, 609, 622]<|/det|>\[
g ^ {k _ {2} - k _ {1}} \equiv 1 \pmod {p},
\]
<|det|>text [140, 630, 210, 645]<|/det|>and so
<|det|>equation [389, 647, 612, 667]<|/det|>\[
k _ {1} \equiv k _ {2} \pmod {p - 1}.
\]
<|det|>text [139, 670, 865, 707]<|/det|>If \( a \equiv g^{k} \pmod{p} \) and \( b \equiv g^{\ell} \pmod{p} \), then \( ab \equiv g^{k}g^{\ell} = g^{k + \ell} \pmod{p} \), and so
<|det|>equation [250, 710, 752, 732]<|/det|>\[
\operatorname{ind} _ {g} (a b) \equiv k + \ell \equiv \operatorname{ind} _ {g} (a) + \operatorname{ind} _ {g} (b) \pmod {p - 1}.
\]
<|det|>text [139, 736, 865, 775]<|/det|>The index map \(\mathrm{ind}_g\) is also called the discrete logarithm to the base \(g\) modulo \(p\).
<|det|>text [139, 775, 863, 811]<|/det|>For example, 2 is a primitive root modulo 13. Here is a table of \(\mathrm{ind}_2(a)\) for \(a = 1,\dots ,12\):
<|det|>table [364, 811, 639, 948]<|/det|><table><tr><td>a</td><td>\( \text{ind}_2(a) \)</td><td>a</td><td>\( \text{ind}_2(a) \)</td></tr><tr><td>1</td><td>0</td><td>7</td><td>11</td></tr><tr><td>2</td><td>1</td><td>8</td><td>3</td></tr><tr><td>3</td><td>4</td><td>9</td><td>8</td></tr><tr><td>4</td><td>2</td><td>10</td><td>10</td></tr><tr><td>5</td><td>9</td><td>11</td><td>7</td></tr><tr><td>6</td><td>5</td><td>12</td><td>6</td></tr></table>
