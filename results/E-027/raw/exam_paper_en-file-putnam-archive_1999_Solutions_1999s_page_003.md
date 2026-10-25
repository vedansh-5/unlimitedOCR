<|det|>page_number [913, 35, 923, 46]<|/det|>3
<|det|>text [124, 66, 490, 141]<|/det|>To see that \( n \) divides \( a_{n} \), factor \( n \) as \( 2^{k}m \), with \( m \) odd. Then note that \( k \leq n \leq n(n - 1) / 2 \), and that there exists \( i \leq m - 1 \) such that \( m \) divides \( 2^{i} - 1 \), namely \( i = \phi(m) \) (Euler's totient function: the number of integers in \( \{1, \ldots, m\} \) relatively prime to \( m \)).
<|det|>text [92, 150, 490, 224]<|/det|>B-1 The answer is 1/3. Let \( G \) be the point obtained by reflecting \( C \) about the line \( AB \). Since \( \angle ADC = \frac{\pi - \theta}{2} \), we find that \( \angle BDE = \pi - \theta - \angle ADC = \frac{\pi - \theta}{2} = \angle ADC = \pi - \angle BDC = \pi - \angle BDG \), so that \( E, D, G \) are collinear. Hence
<|det|>equation [167, 234, 408, 269]<|/det|>\[
| E F | = \frac {| B E |}{| B C |} = \frac {| B E |}{| B G |} = \frac {\sin (\theta / 2)}{\sin (3 \theta / 2)},
\]
<|det|>text [124, 279, 490, 308]<|/det|>where we have used the law of sines in  \( \triangle BDG \) . But by l'Hôpital's Rule,
<|det|>equation [146, 319, 428, 354]<|/det|>\[
\lim _ {\theta \rightarrow 0} \frac {\sin (\theta / 2)}{\sin (3 \theta / 2)} = \lim _ {\theta \rightarrow 0} \frac {\cos (\theta / 2)}{3 \cos (3 \theta / 2)} = 1 / 3.
\]
<|det|>text [92, 368, 491, 456]<|/det|>B-2 First solution: Suppose that \( P \) does not have \( n \) distinct roots; then it has a root of multiplicity at least 2, which we may assume is \( x = 0 \) without loss of generality. Let \( x^k \) be the greatest power of \( x \) dividing \( P(x) \), so that \( P(x) = x^k R(x) \) with \( R(0) \neq 0 \); a simple computation yields
<|det|>equation [120, 466, 457, 485]<|/det|>\[
P ^ {\prime \prime} (x) = (k ^ {2} - k) x ^ {k - 2} R (x) + 2 k x ^ {k - 1} R ^ {\prime} (x) + x ^ {k} R ^ {\prime \prime} (x).
\]
<|det|>text [124, 495, 490, 583]<|/det|>Since \( R(0) \neq 0 \) and \( k \geq 2 \), we conclude that the greatest power of \( x \) dividing \( P''(x) \) is \( x^{k-2} \). But \( P(x) = Q(x)P''(x) \), and so \( x^2 \) divides \( Q(x) \). We deduce (since \( Q \) is quadratic) that \( Q(x) \) is a constant \( C \) times \( x^2 \); in fact, \( C = 1/(n(n-1)) \) by inspection of the leading-degree terms of \( P(x) \) and \( P''(x) \).
<|det|>text [124, 588, 490, 650]<|/det|>Now if  \( P(x) = \sum_{j=0}^{n} a_{j} x^{j} \) , then the relation  \( P(x) = C x^{2} P''(x) \)  implies that  \( a_{j} = C j(j-1) a_{j} \)  for all j; hence  \( a_{j} = 0 \)  for  \( j \leq n-1 \) , and we conclude that  \( P(x) = a_{n} x^{n} \) , which has all identical roots.
<|det|>text [124, 655, 490, 700]<|/det|>Second solution (by Greg Kuperberg): Let  \( f(x) = P''(x)/P(x) = 1/Q(x) \) . By hypothesis, f has at most two poles (counting multiplicity).
<|det|>text [124, 705, 491, 791]<|/det|>Recall that for any complex polynomial P, the roots of  \( P' \)  lie within the convex hull of P. To show this, it suffices to show that if the roots of P lie on one side of a line, say on the positive side of the imaginary axis, then  \( P' \)  has no roots on the other side. That follows because if  \( r_{1}, \ldots, r_{n} \)  are the roots of P,
<|det|>equation [227, 802, 348, 840]<|/det|>\[
\frac {P ^ {\prime} (z)}{P (z)} = \sum_ {i = 1} ^ {n} \frac {1}{z - r _ {i}}
\]
<|det|>text [124, 850, 490, 880]<|/det|>and if z has negative real part, so does  \( 1/(z-r_{i}) \)  for  \( i=1,\ldots,n \) , so the sum is nonzero.
<|det|>text [124, 885, 492, 915]<|/det|>The above argument also carries through if z lies on the imaginary axis, provided that z is not equal to a root of
<|det|>text [553, 66, 920, 96]<|/det|>P. Thus we also have that no roots of  \( P' \)  lie on the sides of the convex hull of P, unless they are also roots of P.
<|det|>text [553, 100, 920, 187]<|/det|>From this we conclude that if r is a root of P which is a vertex of the convex hull of the roots, and which is not also a root of  \( P' \) , then f has a single pole at r (as r cannot be a root of  \( P'' \) ). On the other hand, if r is a root of P which is also a root of  \( P' \) , it is a multiple root, and then f has a double pole at r.
<|det|>text [553, 191, 919, 220]<|/det|>If \( P \) has roots not all equal, the convex hull of its roots has at least two vertices.
<|det|>text [521, 229, 671, 243]<|/det|>B-3 We first note that
<|det|>equation [621, 249, 812, 281]<|/det|>\[
\sum_ {m, n > 0} x ^ {m} y ^ {n} = \frac {x y}{(1 - x) (1 - y)}.
\]
<|det|>text [554, 291, 919, 306]<|/det|>Subtracting S from this gives two sums, one of which is
<|det|>equation [563, 315, 868, 351]<|/det|>\[
\sum_ {m \geq 2 n + 1} x ^ {m} y ^ {n} = \sum_ {n} y ^ {n} \frac {x ^ {2 n + 1}}{1 - x} = \frac {x ^ {3} y}{(1 - x) (1 - x ^ {2} y)}
\]
<|det|>text [554, 360, 919, 389]<|/det|>and the other of which sums to \( xy^3 / [(1 - y)(1 - xy^2)] \). Therefore
<|det|>equation [571, 398, 860, 504]<|/det|>\[
\begin{array}{l} S (x, y) = \frac {x y}{(1 - x) (1 - y)} - \frac {x ^ {3} y}{(1 - x) (1 - x ^ {2} y)} \\ - \frac {x y ^ {3}}{(1 - y) (1 - x y ^ {2})} \\ = \frac {x y (1 + x + y + x y - x ^ {2} y ^ {2})}{(1 - x ^ {2} y) (1 - x y ^ {2})} \\ \end{array}
\]
<|det|>text [555, 513, 708, 526]<|/det|>and the desired limit is
<|det|>equation [587, 535, 846, 560]<|/det|>\[
\lim _ {(x, y) \to (1, 1)} x y (1 + x + y + x y - x ^ {2} y ^ {2}) = 3.
\]
<|det|>text [520, 573, 920, 661]<|/det|>B-4 (based on work by Daniel Stronger) We make repeated use of the following fact: if \( f \) is a differentiable function on all of \( \mathbb{R} \), \( \lim_{x\to -\infty}f(x)\geq 0 \), and \( f'(x) > 0 \) for all \( x\in \mathbb{R} \), then \( f(x) > 0 \) for all \( x\in \mathbb{R} \). (Proof: if \( f(y) < 0 \) for some \( x \), then \( f(x) < f(y) \) for all \( x < y \) since \( f' > 0 \), but then \( \lim_{x\to -\infty}f(x)\leq f(y) < 0 \).)
<|det|>text [555, 664, 850, 680]<|/det|>From the inequality \( f'''(x) \leq f(x) \) we obtain
<|det|>equation [571, 688, 862, 707]<|/det|>\[
f ^ {\prime \prime} f ^ {\prime \prime \prime} (x) \leq f ^ {\prime \prime} (x) f (x) <   f ^ {\prime \prime \prime} (x) f (x) + f ^ {\prime \prime} (x) ^ {2}
\]
<|det|>text [554, 715, 919, 745]<|/det|>since \( f'(x) \) is positive. Applying the fact to the difference between the right and left sides, we get
<|det|>equation [638, 754, 920, 784]<|/det|>\[
\frac {1}{2} (f ^ {\prime \prime} (x)) ^ {2} <   f (x) f ^ {\prime} (x). \tag {1}
\]
<|det|>text [554, 795, 919, 825]<|/det|>On the other hand, since \( f(x) \) and \( f'''(x) \) are both positive for all \( x \), we have
<|det|>equation [576, 833, 856, 852]<|/det|>\[
2 f ^ {\prime} (x) f ^ {\prime \prime} (x) <   2 f ^ {\prime} (x) f ^ {\prime \prime} (x) + 2 f (x) f ^ {\prime \prime \prime} (x).
\]
<|det|>text [554, 860, 919, 890]<|/det|>Applying the fact to the difference between the sides yields
<|det|>equation [644, 897, 920, 916]<|/det|>\[
f ^ {\prime} (x) ^ {2} \leq 2 f (x) f ^ {\prime \prime} (x). \tag {2}
\]
