<|det|>page_number [912, 35, 920, 46]<|/det|>2
<|det|>text [100, 65, 491, 125]<|/det|>A5 (by Abhinav Kumar) Define  \( G : R \to R \)  by  \( G(x) = \int_{0}^{x} g(t) dt \) . By assumption, G is a strictly increasing, thrice continuously differentiable function. It is also bounded: for x > 1, we have
<|det|>equation [131, 135, 441, 166]<|/det|>\[
0 <   G (x) - G (1) = \int_ {1} ^ {x} g (t) d t \leq \int_ {1} ^ {x} d t / t ^ {2} = 1,
\]
<|det|>text [124, 175, 490, 232]<|/det|>and similarly, for x < -1, we have  \( 0 > G(x) - G(-1) \geq -1 \) . It follows that the image of G is some open interval  \( (A, B) \)  and that  \( G^{-1} : (A, B) \to \mathbb{R} \)  is also thrice continuously differentiable.
<|det|>text [124, 237, 491, 295]<|/det|>Define \( H : (A, B) \times (A, B) \to \mathbb{R} \) by \( H(x, y) = F(G^{-1}(x), G^{-1}(y)) \); it is twice continuously differentiable since \( F \) and \( G^{-1} \) are. By our assumptions about \( F \),
<|det|>equation [100, 307, 474, 380]<|/det|>\[
\begin{array}{l} \frac {\partial H}{\partial x} + \frac {\partial H}{\partial y} = \frac {\partial F}{\partial x} (G ^ {- 1} (x), G ^ {- 1} (y)) \cdot \frac {1}{g (G ^ {- 1} (x))} \\ + \frac {\partial F}{\partial y} (G ^ {- 1} (x), G ^ {- 1} (y)) \cdot \frac {1}{g (G ^ {- 1}(y))} = 0. \\ \end{array}
\]
<|det|>text [124, 387, 491, 521]<|/det|>Therefore \(H\) is constant along any line parallel to the vector \((1,1)\), or equivalently, \(H(x,y)\) depends only on \(x - y\). We may thus write \(H(x,y) = h(x - y)\) for some function \(h\) on \((- (B - A), B - A)\), and we then have \(F(x,y) = h(G(x) - G(y))\). Since \(F(u,u) = 0\), we have \(h(0) = 0\). Also, \(h\) is twice continuously differentiable (since it can be written as \(h(x) = H((A + B + x) / 2, (A + B - x) / 2)\)), so \(|h'|\) is bounded on the closed interval \([- (B - A) / 2, (B - A) / 2]\), say by \(M\).
<|det|>text [124, 523, 490, 582]<|/det|>Given \(x_{1},\ldots ,x_{n + 1}\in \mathbb{R}\) for some \(n\geq 2\) , the numbers \(G(x_{1}),\ldots ,G(x_{n + 1})\) all belong to \((A,B)\) , so we can choose indices \(i\) and \(j\) so that \(|G(x_i) - G(x_j)|\leq (B - A) / n\leq (B - A) / 2\) . By the mean value theorem,
<|det|>equation [142, 609, 432, 640]<|/det|>\[
| F (x _ {i}, x _ {j}) | = | h (G (x _ {i}) - G (x _ {j})) | \leq M \frac {B - A}{n},
\]
<|det|>text [124, 648, 384, 663]<|/det|>so the claim holds with \( C = M(B - A) \).
<|det|>text [100, 673, 491, 775]<|/det|>A6 Choose some ordering \( h_1, \ldots, h_n \) of the elements of \( G \) with \( h_1 = e \). Define an \( n \times n \) matrix \( M \) by setting \( M_{ij} = 1 / k \) if \( h_j = h_i g \) for some \( g \in \{g_1, \ldots, g_k\} \) and \( M_{ij} = 0 \) otherwise. Let \( v \) denote the column vector \( (1, 0, \ldots, 0) \). The probability that the product of \( m \) random elements of \( \{g_1, \ldots, g_k\} \) equals \( h_i \) can then be interpreted as the \( i \)-th component of the vector \( M^m v \).
<|det|>text [124, 779, 490, 868]<|/det|>Let \(\hat{G}\) denote the dual group of \(G\), i.e., the group of complex-valued characters of \(G\). Let \(\hat{e} \in \hat{G}\) denote the trivial character. For each \(\chi \in \hat{G}\), the vector \(\nu_{\chi} = (\chi(h_i))_{i=1}^n\) is an eigenvector of \(M\) with eigenvalue \(\lambda_{\chi} = (\chi(g_1) + \cdots + \chi(g_k)) / k\). In particular, \(\nu_{\hat{e}}\) is the all-ones vector and \(\lambda_{\hat{e}} = 1\). Put
<|det|>equation [185, 877, 388, 896]<|/det|>\[
b = \max \left\{\left| \lambda_ {\chi} \right|: \chi \in \hat {G} - \{\hat {e} \} \right\};
\]
<|det|>text [553, 65, 920, 93]<|/det|>we show that \( b \in (0,1) \) as follows. First suppose \( b = 0 \); then
<|det|>equation [604, 105, 830, 147]<|/det|>\[
1 = \sum_ {\chi \in \hat {G}} \lambda_ {\chi} = \frac {1}{k} \sum_ {i = 1} ^ {k} \sum_ {\chi \in \hat {G}} \chi (g _ {i}) = \frac {n}{k}
\]
<|det|>text [553, 157, 921, 306]<|/det|>because \(\sum_{\chi \in (\hat{G})}\chi (g_i)\) equals \(n\) for \(i = 1\) and 0 otherwise. However, this contradicts the hypothesis that \(\{g_1,\dots ,g_k\}\) is not all of \(G\). Hence \(b > 0\). Next suppose \(b = 1\), and choose \(\chi \in \hat{G} -\{\hat{e}\}\) with \(|\lambda_{\chi}| = 1\). Since each of \(\chi (g_1),\ldots ,\chi (g_k)\) is a complex number of norm 1, the triangle inequality forces them all to be equal. Since \(\chi (g_1) = \chi (e) = 1\), \(\chi\) must map each of \(g_{1},\ldots ,g_{k}\) to 1, but this is impossible because \(\chi\) is a nontrivial character and \(g_{1},\ldots ,g_{k}\) form a set of generators of \(G\). This contradiction yields \(b < 1\).
<|det|>text [554, 308, 871, 329]<|/det|>Since  \( v = \frac{1}{n} \sum_{\chi \in \hat{G}} v_{\chi} \)  and  \( M v_{\chi} = \lambda_{\chi} v_{\chi} \) , we have
<|det|>equation [614, 338, 820, 378]<|/det|>\[
M ^ {m} v - \frac {1}{n} v _ {\hat {c}} = \frac {1}{n} \sum_ {\chi \in \hat {G} - \{\hat {c} \}} \lambda_ {\chi} ^ {m} v _ {\chi}.
\]
<|det|>text [553, 388, 920, 417]<|/det|>Since the vectors  \( v_{\chi} \)  are pairwise orthogonal, the limit we are interested in can be written as
<|det|>equation [591, 426, 842, 456]<|/det|>\[
\lim _ {m \to \infty} \frac {1}{b ^ {2 m}} (M ^ {m} v - \frac {1}{n} v _ {\hat {c}}) \cdot (M ^ {m} v - \frac {1}{n} v _ {\hat {c}}).
\]
<|det|>text [554, 465, 696, 478]<|/det|>and then rewritten as
<|det|>equation [557, 487, 875, 526]<|/det|>\[
\lim _ {m \to \infty} \frac {1}{b ^ {2 m}} \sum_ {\chi \in \hat {G} - \{\hat {c} \}} | \lambda_ {\chi} | ^ {2 m} = \# \{\chi \in \hat {G}: | \lambda_ {\chi} | = b \}.
\]
<|det|>text [554, 536, 919, 551]<|/det|>By construction, this last quantity is nonzero and finite.
<|det|>text [553, 555, 920, 585]<|/det|>Remark. It is easy to see that the result fails if we do not assume  \( g_{1}=e \) : take  \( G=\mathbb{Z}/2\mathbb{Z}, n=1 \) , and  \( g_{1}=1 \) .
<|det|>text [553, 589, 920, 709]<|/det|>Remark. Harm Derksen points out that a similar argument applies even if G is not assumed to be abelian, provided that the operator  \( g_{1} + \cdots + g_{k} \)  in the group algebra  \( Z[G] \)  is normal, i.e., it commutes with the operator  \( g_{1}^{-1} + \cdots + g_{k}^{-1} \) . This includes the cases where the set  \( \{g_{1}, \ldots, g_{k}\} \)  is closed under taking inverses and where it is a union of conjugacy classes (which in turn includes the case of G abelian).
<|det|>text [553, 712, 920, 815]<|/det|>Remark. The matrix M used above has nonnegative entries with row sums equal to 1 (i.e., it corresponds to a Markov chain), and there exists a positive integer m such that  \( M^{m} \)  has positive entries. For any such matrix, the Perron-Frobenius theorem implies that the sequence of vectors  \( M^{m}v \)  converges to a limit w, and there exists  \( b \in [0,1) \)  such that
<|det|>equation [618, 826, 816, 861]<|/det|>\[
\limsup _ {m \to \infty} \frac {1}{b ^ {2 m}} \sum_ {i = 1} ^ {n} ((M ^ {m} v - w) _ {i}) ^ {2}
\]
<|det|>text [553, 871, 920, 915]<|/det|>is nonzero and finite. (The intended interpretation in case b = 0 is that  \( M^{m}v = w \)  for all large m.) However, the limit need not exist in general.
