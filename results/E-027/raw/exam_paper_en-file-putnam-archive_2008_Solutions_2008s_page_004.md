<|det|>page_number [912, 36, 921, 46]<|/det|>4
<|det|>text [124, 66, 490, 96]<|/det|>(by elementary algebra, or Cramer's rule), so the center of the circle is rational. This proves the desired result.
<|det|>text [124, 100, 491, 203]<|/det|>Remark: The above solution is deliberately more verbose than is really necessary. A shorter way to say this is that any two distinct rational points determine a rational line (a line of the form  \( ax + by + c = 0 \)  with a, b, c rational), while any two nonparallel rational lines intersect at a rational point. A similar statement holds with the rational numbers replaced by any field.
<|det|>text [125, 207, 492, 252]<|/det|>Remark: A more explicit argument is to show that the equation of the circle through the rational points  \( (x_{1}, y_{1}), (x_{2}, y_{2}), (x_{3}, y_{3}) \)  is
<|det|>equation [189, 260, 382, 329]<|/det|>\[
0 = \det \left( \begin{array}{c c c c} x _ {1} ^ {2} + y _ {1} ^ {2} & x _ {1} & y _ {1} & 1 \\ x _ {2} ^ {2} + y _ {2} ^ {2} & x _ {2} & y _ {2} & 1 \\ x _ {3} ^ {2} + y _ {3} ^ {2} & x _ {3} & y _ {3} & 1 \\ x ^ {2} + y ^ {2} & x & y & 1 \end{array} \right)
\]
<|det|>text [124, 338, 491, 384]<|/det|>which has the form  \( a(x^{2} + y^{2}) + dx + ey + f = 0 \)  for a, d, e, f rational. The center of this circle is  \( (-d/(2a), -e/(2a)) \) , which is again a rational point.
<|det|>text [92, 391, 492, 478]<|/det|>B-2 We claim that \( F_{n}(x) = (\ln x - a_{n})x^{n} / n! \), where \( a_{n} = \sum_{k=1}^{n} 1 / k \). Indeed, temporarily write \( G_{n}(x) = (\ln x - a_{n})x^{n} / n! \) for \( x > 0 \) and \( n \geq 1 \); then \( \lim_{x \to 0} G_{n}(x) = 0 \) and \( G_{n}'(x) = (\ln x - a_{n} + 1 / n)x^{n-1} / (n - 1)! = G_{n-1}(x) \), and the claim follows by the Fundamental Theorem of Calculus and induction on \( n \).
<|det|>text [124, 483, 491, 571]<|/det|>Given the claim, we have  \( F_{n}(1) = -a_{n}/n! \)  and so we need to evaluate  \( -\lim_{n \to \infty} \frac{a_{n}}{\ln n} \) . But since the function 1/x is strictly decreasing for x positive,  \( \sum_{k=2}^{n} 1/k = a_{n} - 1 \)  is bounded below by  \( \int_{2}^{n} dx/x = \ln n - \ln 2 \)  and above by  \( \int_{1}^{n} dx/x = \ln n \) . It follows that  \( \lim_{n \to \infty} \frac{a_{n}}{\ln n} = 1 \) , and the desired limit is -1.
<|det|>text [91, 580, 490, 641]<|/det|>B-3 The largest possible radius is  \( \frac{\sqrt{2}}{2} \) . It will be convenient to solve the problem for a hypercube of side length 2 instead, in which case we are trying to show that the largest radius is  \( \sqrt{2} \) .
<|det|>text [124, 645, 491, 761]<|/det|>Choose coordinates so that the interior of the hypercube is the set  \( H = [-1, 1]^{4} \)  in  \( R^{4} \) . Let C be a circle centered at the point P. Then C is contained both in H and its reflection across P; these intersect in a rectangular parallelepiped each of whose pairs of opposite faces are at most 2 unit apart. Consequently, if we translate C so that its center moves to the point  \( O = (0, 0, 0, 0) \)  at the center of H, then it remains entirely inside H.
<|det|>text [124, 766, 492, 868]<|/det|>This means that the answer we seek equals the largest possible radius of a circle C contained in H and centered at O. Let  \( v_{1} = (v_{11}, \ldots, v_{14}) \)  and  \( v_{2} = (v_{21}, \ldots, v_{24}) \)  be two points on C lying on radii perpendicular to each other. Then the points of the circle can be expressed as  \( v_{1} \cos \theta + v_{2} \sin \theta \)  for  \( 0 \leq \theta < 2\pi \) . Then C lies in H if and only if for each i, we have
<|det|>equation [142, 878, 432, 896]<|/det|>\[
\left| v _ {1 i} \cos \theta + v _ {2 i} \sin \theta \right| \leq 1 \quad (0 \leq \theta <   2 \pi).
\]
<|det|>text [124, 905, 492, 936]<|/det|>In geometric terms, the vector  \( (v_{1i}, v_{2i}) \)  in  \( R^{2} \)  has dot product at most 1 with every unit vector. Since
<|det|>text [555, 66, 920, 97]<|/det|>this holds for the unit vector in the same direction as  \( (v_{1i}, v_{2i}) \) , we must have
<|det|>equation [613, 106, 820, 126]<|/det|>\[
v _ {1 i} ^ {2} + v _ {2 i} ^ {2} \leq 1 \quad (i = 1, \dots , 4).
\]
<|det|>text [554, 136, 920, 166]<|/det|>Conversely, if this holds, then the Cauchy-Schwarz inequality and the above analysis imply that \( C \) lies in \( H \).
<|det|>text [555, 170, 734, 185]<|/det|>If \( r \) is the radius of \( C \), then
<|det|>equation [646, 195, 788, 295]<|/det|>\[
\begin{array}{l} 2 r ^ {2} = \sum_ {i = 1} ^ {4} v _ {1 i} ^ {2} + \sum_ {i = 1} ^ {4} v _ {2 i} ^ {2} \\ = \sum_ {i = 1} ^ {4} (v _ {1 i} ^ {2} + v _ {2 i} ^ {2}) \\ \leq 4, \\ \end{array}
\]
<|det|>text [555, 306, 920, 337]<|/det|>so \( r \leq \sqrt{2} \). Since this is achieved by the circle through \( (1, 1, 0, 0) \) and \( (0, 0, 1, 1) \), it is the desired maximum.
<|det|>text [554, 340, 921, 430]<|/det|>Remark: One may similarly ask for the radius of the largest k-dimensional ball inside an n-dimensional unit hypercube; the given problem is the case  \( (n,k)=(4,2) \) . Daniel Kane gives the following argument to show that the maximum radius in this case is  \( \frac{1}{2}\sqrt{\frac{n}{k}} \) . (Thanks for Noam Elkies for passing this along.)
<|det|>text [554, 433, 920, 590]<|/det|>We again scale up by a factor of 2, so that we are trying to show that the maximum radius \( r \) of a \( k \)-dimensional ball contained in the hypercube \( [-1,1]^n \) is \( \sqrt{\frac{n}{k}} \). Again, there is no loss of generality in centering the ball at the origin. Let \( T: \mathbb{R}^k \to \mathbb{R}^n \) be a similitude carrying the unit ball to this embedded \( k \)-ball. Then there exists a vector \( v_i \in \mathbb{R}^k \) such that for \( e_1, \ldots, e_n \) the standard basis of \( \mathbb{R}^n \), \( x \cdot v_i = T(x) \cdot e_i \) for all \( x \in \mathbb{R}^k \). The condition of the problem is equivalent to requiring \( |v_i| \leq 1 \) for all \( i \), while the radius \( r \) of the embedded ball is determined by the fact that for all \( x \in \mathbb{R}^k \),
<|det|>equation [607, 602, 826, 639]<|/det|>\[
r ^ {2} (x \cdot x) = T (x) \cdot T (x) = \sum_ {i = 1} ^ {n} x \cdot v _ {i}.
\]
<|det|>text [554, 649, 920, 692]<|/det|>Let \(M\) be the matrix with columns \(v_{1},\ldots ,v_{k}\); then \(MM^{T} = r^{2}I_{k}\), for \(I_{k}\) the \(k\times k\) identity matrix. We then have
<|det|>equation [602, 702, 831, 778]<|/det|>\[
\begin{array}{l} k r ^ {2} = \operatorname{Trace} \left(r ^ {2} I _ {k}\right) = \operatorname{Trace} \left(M M ^ {T}\right) \\ = \operatorname{Trace} \left(M ^ {T} M\right) = \sum_ {i = 1} ^ {n} \left| v _ {i} \right| ^ {2} \\ \leq n, \\ \end{array}
\]
<|det|>text [554, 791, 783, 809]<|/det|>yielding the upper bound \(r \leq \sqrt{\frac{n}{k}}\).
<|det|>text [553, 811, 920, 898]<|/det|>To show that this bound is optimal, it is enough to show that one can find an orthogonal projection of \(\mathbb{R}^n\) onto \(\mathbb{R}^k\) so that the projections of the \(e_i\) all have the same norm (one can then rescale to get the desired configuration of \(v_1,\ldots ,v_n\)). We construct such a configuration by a "smoothing" argument. Startw with any projection. Let
