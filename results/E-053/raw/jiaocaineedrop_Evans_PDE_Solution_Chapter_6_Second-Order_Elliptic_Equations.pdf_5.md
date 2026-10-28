<|det|>text [70, 68, 920, 112]<|/det|>10. Proof. We omit (a) since is standard. For (b), if \( u \) attains an interior maximum, then the conclusion follows from strong maximum principle.
<|det|>text [102, 118, 920, 162]<|/det|>If not, then for some \( x^0 \in \partial U, u(x^0) > u(x) \forall x \in U \). Then Hopf's lemma implies \( \frac{\partial u}{\partial \nu}(x^0) > 0 \), which is a contradiction.
<|det|>text [104, 176, 920, 220]<|/det|>Remark 2. A generalization of this problem to mixed boundary conditions is recorded in Gilbarg-Trudinger, Elliptic PDEs of second order, Problem 3.1.
<|det|>text [70, 238, 228, 255]<|/det|>11. Proof. Define
<|det|>equation [277, 255, 752, 297]<|/det|>\[
B [ u, v ] = \int_ {U} \sum_ {i, j} a ^ {i j} u _ {x _ {i}} v _ {x _ {j}} d x \text {for} u \in H ^ {1} (U), v \in H _ {0} ^ {1} (U).
\]
<|det|>text [103, 302, 673, 321]<|/det|>By Exercise 5.17, \(\phi(u) \in H^{1}(U)\). Then, for all \(v \in C_{c}^{\infty}(U)\), \(v \geq 0\),
<|det|>equation [189, 330, 841, 500]<|/det|>\[
\begin{array}{l} B [ \phi (u), v ] = \int_ {U} \sum_ {i, j} a ^ {i j} (\phi (u)) _ {x _ {i}} v _ {x _ {j}} d x \\ = \int_ {U} \sum_ {i, j} a ^ {i j} \phi^ {\prime} (u) u _ {x _ {i}} v _ {x _ {j}} d x, (\phi^ {\prime} (u) \text {   is   bounded   since   } u \text {   is   bounded }) \\ = \int_ {U} \sum_ {i, j} a ^ {i j} u _ {x _ {i}} (\phi^ {\prime} (u) v) _ {x _ {j}} - \sum_ {i, j} a _ {i j} \phi^ {\prime \prime} (u) u _ {x _ {i}} u _ {x _ {j}} v d x \\ \leq 0 - \int_ {U} \phi^ {\prime \prime} (u) v | D u | ^ {2} d x \leq 0, \text { by   convexity   of } \phi . \\ \end{array}
\]
<|det|>text [103, 508, 920, 553]<|/det|>(We don't know whether the product of two \( H^1 \) functions is weakly differentiable. This is why we do not take \( v \in H_0^1 \).) Now we complete the proof with the standard density argument.
<|det|>text [70, 570, 920, 616]<|/det|>12. Proof. Given \( u \in C^2(U) \cap C(\bar{U}) \) with \( Lu \leq 0 \) in \( U \) and \( u \leq 0 \) on \( \partial U \). Since \( \bar{U} \) is compact and \( v \in C(\bar{U}) \), \( v \geq c > 0 \). So \( w := \frac{u}{v} \in C^2(U) \cap C(\bar{U}) \). Brutal computation gives us
<|det|>equation [130, 624, 891, 734]<|/det|>\[
\begin{array}{l} - a ^ {i j} w _ {x _ {i} x _ {j}} = \frac {- a ^ {i j} u _ {x _ {i} x _ {j}} v + a ^ {i j} v _ {x _ {i} x _ {j}} u}{v ^ {2}} + \frac {a ^ {i j} v _ {x _ {i}} u _ {x _ {i}} v _ {x _ {j}} - a ^ {i j} v _ {x _ {i}} v _ {x _ {j}}}{v ^ {2}} - a ^ {i j} \frac {2}{v} v _ {x _ {i}} u - v u _ {x _ {i}} \\ = \frac {(L u - b ^ {i} u _ {x _ {i}} - c u) v + (- L v + b ^ {i} v _ {x _ {i}} + c v) u}{v ^ {2}} + 0 + a ^ {i j} \frac {2}{v} v _ {x _ {j}} w _ {x _ {i}}, \text {since} a ^ {i j} = a ^ {j i}. \\ = \frac {L u}{v} - \frac {u L v}{v ^ {2}} - b ^ {i} w _ {x _ {i}} + a ^ {i j} \frac {2}{v} v _ {x _ {j}} w _ {x _ {i}} \\ \end{array}
\]
<|det|>text [104, 744, 197, 760]<|/det|>Therefore,
<|det|>equation [170, 772, 858, 807]<|/det|>\[
M w := - a ^ {i j} w _ {x _ {i} x _ {j}} + w _ {x _ {i}} \left[ b ^ {i} - a ^ {i j} \frac {2}{v} v _ {x _ {j}} \right] = \frac {L u}{v} - \frac {u L v}{v ^ {2}} \leq 0 \text {on} \{x \in \bar {U}: u > 0 \} \subseteq U
\]
<|det|>text [102, 818, 918, 861]<|/det|>If \(\{x\in \bar{U}:u > 0\}\) is not empty, Weak maximum principle to the operator \(M\) with bounded coefficients (since \(v\in C^{1}(\bar{U})\)) will lead a contradiction that
<|det|>equation [377, 874, 648, 909]<|/det|>\[
0 <   \max _ {\{u > 0 \}} w = \max _ {\partial \{u > 0 \}} w = \frac {0}{v} = 0
\]
<|det|>text [104, 919, 266, 935]<|/det|>Hence \( u \leq 0 \) in \( U \).
<|det|>page_number [493, 957, 506, 969]<|/det|>6
