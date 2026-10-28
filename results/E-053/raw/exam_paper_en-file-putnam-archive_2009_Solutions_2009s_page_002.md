<|det|>page_number [908, 35, 920, 46]<|/det|>2
<|det|>text [124, 66, 490, 96]<|/det|>product of the orders of all of its elements cannot be a power of 2.
<|det|>text [124, 100, 491, 188]<|/det|>We may thus consider only abelian 2-groups hereafter. For such a group G, the product of the orders of all of its elements has the form  \( 2^{k(G)} \)  for some nonnegative integer G, and we must show that it is impossible to achieve  \( k(G)=2009 \) . Again by the structure theorem, we may write
<|det|>equation [227, 200, 348, 235]<|/det|>\[
G \cong \prod_ {i = 1} ^ {\infty} (\mathbb {Z} / 2 ^ {i} \mathbb {Z}) ^ {e _ {i}}
\]
<|det|>text [124, 245, 489, 273]<|/det|>for some nonnegative integers  \( e_{1}, e_{2}, \ldots \) , all but finitely many of which are 0.
<|det|>text [124, 278, 492, 308]<|/det|>For any nonnegative integer m, the elements of G of order at most  \( 2^{m} \)  form a subgroup isomorphic to
<|det|>equation [217, 319, 355, 355]<|/det|>\[
\prod_ {i = 1} ^ {\infty} (\mathbb {Z} / 2 ^ {\min \{i, m \}} \mathbb {Z}) ^ {e _ {i}},
\]
<|det|>text [124, 365, 489, 394]<|/det|>which has \(2^{s_m}\) elements for \(s_m = \sum_{i=1}^{\infty} \min\{i, m\} e_i\). Hence
<|det|>equation [204, 404, 369, 438]<|/det|>\[
k (G) = \sum_ {i = 1} ^ {\infty} i (2 ^ {s _ {i}} - 2 ^ {s _ {i - 1}}).
\]
<|det|>text [124, 449, 489, 480]<|/det|>Since  \( s_{1} \leq s_{2} \leq \cdots, k(G) + 1 \)  is always divisible by  \( 2^{s_{1}} \) . In particular,  \( k(G) = 2009 \)  forces  \( s_{1} \leq 1 \) .
<|det|>text [124, 483, 491, 571]<|/det|>However, the only cases where  \( s_{1} \leq 1 \)  are where all of the  \( e_{i} \)  are 0, in which case  \( k(G) = 0 \) , or where  \( e_{i} = 1 \)  for some i and  \( e_{j} = 0 \)  for  \( j \neq i \) , in which case  \( k(G) = (i - 1)2^{i} + 1 \) . The right side is a strictly increasing function of i which equals 1793 for i = 8 and 4097 for i = 9, so it can never equal 2009. This proves the claim.
<|det|>text [124, 576, 490, 751]<|/det|>Remark. One can also arrive at the key congruence by dividing G into equivalence classes, by declaring two elements to be equivalent if they generate the same cyclic subgroup of G. For h > 0, an element of order  \( 2^{h} \)  belongs to an equivalence class of size  \( 2^{h-1} \) , so the products of the orders of the elements of this equivalence class is  \( 2^{j} \)  for  \( j = h2^{h-1} \) . This quantity is divisible by 4 as long as h > 1; thus to have  \( k(G) \equiv 1 \pmod{4} \) , the number of elements of G of order 2 must be congruent to 1 modulo 4. However, there are exactly  \( 2^{e} - 1 \)  such elements, for e the number of cyclic factors of G. Hence e = 1, and one concludes as in the given solution.
<|det|>text [90, 760, 420, 775]<|/det|>A–6 We disprove the assertion using the example
<|det|>equation [182, 785, 393, 804]<|/det|>\[
f (x, y) = 3 (1 + y) (2 x - 1) ^ {2} - y.
\]
<|det|>text [124, 813, 490, 843]<|/det|>We have \( b - a = d - c = 0 \) because the identity \( f(x,y) = f(1 - x,y) \) forces \( a = b \), and because
<|det|>equation [180, 852, 359, 886]<|/det|>\[
c = \int_ {0} ^ {1} 3 (2 x - 1) ^ {2} d x = 1,
\]
<|det|>equation [182, 888, 393, 920]<|/det|>\[
d = \int_ {0} ^ {1} (6 (2 x - 1) ^ {2} - 1) d x = 1.
\]
<|det|>text [555, 67, 771, 81]<|/det|>Moreover, the partial derivatives
<|det|>equation [609, 92, 824, 122]<|/det|>\[
\frac {\partial f}{\partial x} (x _ {0}, y _ {0}) = 3 (1 + y _ {0}) (8 x _ {0} - 4)
\]
<|det|>equation [612, 124, 808, 157]<|/det|>\[
\frac {\partial f}{\partial y} (x _ {0}, y _ {0}) = 3 (2 x _ {0} - 1) ^ {2} - 1.
\]
<|det|>text [553, 168, 920, 225]<|/det|>have no common zero in  \( (0,1)^{2} \) . Namely, for the first partial to vanish, we must have  \( x_{0}=1/2 \)  since  \( 1+y_{0} \)  is nowhere zero, but for  \( x_{0}=1/2 \)  the second partial cannot vanish.
<|det|>text [553, 231, 920, 336]<|/det|>Remark. This problem amounts to refuting a potential generalization of the Mean Value Theorem to bivariate functions. Many counterexamples are possible. Kent Merryfield suggests  \( y \sin(2\pi x) \) , for which all four of the boundary integrals vanish; here the partial derivatives are  \( 2\pi y \cos(2\pi x) \)  and  \( \sin(2\pi x) \) . Catalin Zara suggests  \( x^{1/3}y^{2/3} \) . Qingchun Ren suggests  \( xy(1-y) \) .
<|det|>text [521, 345, 920, 569]<|/det|>B-1 Every positive rational number can be uniquely written in lowest terms as \(a / b\) for \(a, b\) positive integers. We prove the statement in the problem by induction on the largest prime dividing either \(a\) or \(b\) (where this is considered to be 1 if \(a = b = 1\)). For the base case, we can write \(1/1 = 2! / 2!\). For a general \(a / b\), let \(p\) be the largest prime dividing either \(a\) or \(b\); then \(a / b = p^k a' / b'\) for some \(k \neq 0\) and positive integers \(a', b'\) whose largest prime factors are strictly less than \(p\). We now have \(a / b = (p!)^k \frac{a'}{(p-1)!k b'}\), and all prime factors of \(a'\) and \((p-1)!^{k} b'\) are strictly less than \(p\). By the induction assumption, \(\frac{a'}{(p-1)!^{k} b'}\) can be written as a quotient of products of prime factorials, and so \(a / b = (p!)^k \frac{a'}{(p-1)!^{k} b'}\) can as well. This completes the induction.
<|det|>text [553, 573, 919, 616]<|/det|>Remark. Noam Elkies points out that the representations are unique up to rearranging and canceling common factors.
<|det|>text [521, 626, 920, 687]<|/det|>B-2 The desired real numbers \( c \) are precisely those for which \( 1/3 < c \leq 1 \). For any positive integer \( m \) and any sequence \( 0 = x_0 < x_1 < \cdots < x_m = 1 \), the cost of jumping along this sequence is \( \sum_{i=1}^{m}(x_i - x_{i-1})x_i^2 \). Since
<|det|>equation [597, 696, 837, 805]<|/det|>\[
\begin{array}{l} 1 = \sum_ {i = 1} ^ {m} (x _ {i} - x _ {i - 1}) \geq \sum_ {i = 1} ^ {m} (x _ {i} - x _ {i - 1}) x _ {i} ^ {2} \\ > \sum_ {i = 1} ^ {m} \int_ {x _ {i}} ^ {x _ {i - 1}} t ^ {2} d t \\ = \int_ {0} ^ {1} t ^ {2} d t = \frac {1}{3}, \\ \end{array}
\]
<|det|>text [554, 815, 893, 830]<|/det|>we can only achieve costs c for which  \( 1/3 < c \leq 1 \) .
<|det|>text [553, 833, 921, 907]<|/det|>It remains to check that any such c can be achieved. Suppose  \( 0 = x_{0} < \cdots < x_{m} = 1 \)  is a sequence with  \( m \geq 1 \) . For  \( i = 1, \ldots, m \) , let  \( c_{i} \)  be the cost of the sequence  \( 0, x_{i}, x_{i+1}, \ldots, x_{m} \) . For i > 1 and  \( 0 < y \leq x_{i-1} \) , the cost of the sequence  \( 0, y, x_{i}, \ldots, x_{m} \)  is
<|det|>equation [577, 915, 855, 935]<|/det|>\[
c _ {i} + y ^ {3} + (x _ {i} - y) x _ {i} ^ {2} - x _ {i} ^ {3} = c _ {i} - y (x _ {i} ^ {2} - y ^ {2}),
\]
