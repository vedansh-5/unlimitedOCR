<|det|>page_number [914, 36, 925, 47]<|/det|>4
<|det|>text [158, 67, 245, 80]<|/det|>or in other words
<|det|>equation [166, 90, 410, 130]<|/det|>\[
\left(1 - \frac {1}{m + n}\right) ^ {m + n - 1} <   \left(1 - \frac {1}{n}\right) ^ {n - 1}.
\]
<|det|>text [123, 137, 491, 284]<|/det|>To show this, we check that the function  \( f(x) = (1 - 1/x)^{x-1} \)  is strictly decreasing for x > 1; while this can be achieved using the weighted arithmetic-geometric mean inequality, we give a simple calculus proof instead. The derivative of  \( \log f(x) \)  is  \( \log(1 - 1/x) + 1/x \) , so it is enough to check that this is negative for x > 1. An equivalent statement is that  \( \log(1 - x) + x < 0 \)  for 0 < x < 1; this in turn holds because the function  \( g(x) = \log(1 - x) + x \)  tends to 0 as  \( x \to 0^{+} \)  and has derivative  \( 1 - \frac{1}{1-x} < 0 \)  for 0 < x < 1.
<|det|>text [92, 291, 492, 524]<|/det|>B–3 The answer is  \( \{a \mid a > 2\} \) . If a > 2, then the function  \( f(x) = 2a/(a - 2) \)  has the desired property; both perimeter and area of R in this case are  \( 2a^{2}/(a - 2) \) . Now suppose that  \( a \leq 2 \) , and let  \( f(x) \)  be a nonnegative continuous function on  \( [0, a] \) . Let  \( P = (x_{0}, y_{0}) \)  be a point on the graph of  \( f(x) \)  with maximal y-coordinate; then the area of R is at most  \( ay_{0} \)  since it lies below the line  \( y = y_{0} \) . On the other hand, the points  \( (0, 0) \) ,  \( (a, 0) \) , and P divide the boundary of R into three sections. The length of the section between  \( (0, 0) \)  and P is at least the distance between  \( (0, 0) \)  and P, which is at least  \( y_{0} \) ; the length of the section between P and  \( (a, 0) \)  is similarly at least  \( y_{0} \) ; and the length of the section between  \( (0, 0) \)  and  \( (a, 0) \)  is a. Since  \( a \leq 2 \) , we have  \( 2y_{0} + a > ay_{0} \)  and hence the perimeter of R is strictly greater than the area of R.
<|det|>text [92, 533, 491, 650]<|/det|>B–4 First solution: Identify the xy-plane with the complex plane C, so that  \( P_{k} \)  is the real number k. If z is sent to  \( z' \)  by a counterclockwise rotation by  \( \theta \)  about  \( P_{k} \), then  \( z' - k = e^{i\theta}(z - k) \); hence the rotation  \( R_{k} \)  sends z to  \( \zeta z + k(1 - \zeta) \), where  \( \zeta = e^{2\pi i/n} \). It follows that  \( R_{1} \)  followed by  \( R_{2} \)  sends z to  \( \zeta(\zeta z + (1 - \zeta)) + 2(1 - \zeta) = \zeta^{2}z + (1 - \zeta)(\zeta + 2) \), and so forth; an easy induction shows that R sends z to
<|det|>equation [120, 660, 454, 680]<|/det|>\[
\zeta^ {n} z + (1 - \zeta) (\zeta^ {n - 1} + 2 \zeta^ {n - 2} + \dots + (n - 1) \zeta + n).
\]
<|det|>text [124, 688, 490, 750]<|/det|>Expanding the product  \( (1-\zeta)(\zeta^{n-1}+2\zeta^{n-2}+\cdots+(n-1)\zeta+n) \)  yields  \( -\zeta^{n}-\zeta^{n-1}-\cdots-\zeta+n=n \) . Thus R sends z to  \( z+n \) ; in cartesian coordinates,  \( R(x,y)=(x+n,y) \) .
<|det|>text [123, 753, 491, 870]<|/det|>Second solution: (by Andy Lutomirski, via Ravi Vakil) Imagine a regular n-gon of side length 1 placed with its top edge on the x-axis and the left endpoint of that edge at the origin. Then the rotations correspond to rolling this n-gon along the x-axis; after the n rotations, it clearly ends up in its original rotation and translated n units to the right. Hence the whole plane must do so as well.
<|det|>text [124, 875, 492, 919]<|/det|>Third solution: (attribution unknown) Viewing each  \( R_{k} \)  as a function of a complex number z as in the first solution, the function  \( R_{n} \circ R_{n-1} \circ \cdots \circ R_{1}(z) \)  is linear in
<|det|>text [554, 65, 920, 110]<|/det|>\(z\) with slope \(\zeta^n = 1\). It thus equals \(z + T\) for some \(T \in \mathbb{C}\). Since \(f_1(1) = 1\), we can write \(1 + T = R_n \circ \cdots \circ R_2(1)\). However, we also have
<|det|>equation [601, 122, 831, 138]<|/det|>\[
R _ {n} \circ \dots \circ R _ {2} (1) = R _ {n - 1} \circ R _ {1} (0) + 1
\]
<|det|>text [554, 149, 887, 165]<|/det|>by the symmetry in how the  \( R_{i} \)  are defined. Hence
<|det|>equation [567, 175, 868, 193]<|/det|>\[
R _ {n} (1 + T) = R _ {n} \circ R _ {1} (0) + R _ {n} (1) = T + R _ {n} (1);
\]
<|det|>text [554, 203, 850, 218]<|/det|>that is, \( R_{n}(T) = T \). Hence \( T = n \), as desired.
<|det|>text [521, 228, 920, 285]<|/det|>B-5 First solution: By taking logarithms, we see that the desired limit is  \( \exp(L) \) , where  \( L = \lim_{x \to 1^{-}} \sum_{n=0}^{\infty} x^{n} \left( \ln(1 + x^{n+1}) - \ln(1 + x^{n}) \right) \) . Now
<|det|>equation [541, 295, 895, 414]<|/det|>\[
\begin{array}{l} \sum_ {n = 0} ^ {N} x ^ {n} \left(\ln (1 + x ^ {n + 1}) - \ln (1 + x ^ {n})\right) \\ = 1 / x \sum_ {n = 0} ^ {N} x ^ {n + 1} \ln (1 + x ^ {n + 1}) - \sum_ {n = 0} ^ {N} x ^ {n} \ln (1 + x ^ {n}) \\ = x ^ {N} \ln (1 + x ^ {N + 1}) - \ln 2 + (1 / x - 1) \sum_ {n = 1} ^ {N} x ^ {n} \ln (1 + x ^ {n}); \\ \end{array}
\]
<|det|>text [554, 424, 920, 456]<|/det|>since \(\lim_{N\to \infty}(x^{N}\ln (1 + x^{N + 1})) = 0\) for \(0 < x < 1\), we conclude that \(L = -\ln 2 + \lim_{x\to 1 - }f(x)\), where
<|det|>equation [574, 467, 860, 541]<|/det|>\[
\begin{array}{l} f (x) = (1 / x - 1) \sum_ {n = 1} ^ {\infty} x ^ {n} \ln (1 + x ^ {n}) \\ = (1 / x - 1) \sum_ {n = 1} ^ {\infty} \sum_ {m = 1} ^ {\infty} (- 1) ^ {m + 1} x ^ {n + m n} / m. \\ \end{array}
\]
<|det|>text [554, 551, 920, 580]<|/det|>This final double sum converges absolutely when 0 < x < 1, since
<|det|>equation [586, 590, 845, 666]<|/det|>\[
\begin{array}{l} \sum_ {n = 1} ^ {\infty} \sum_ {m = 1} ^ {\infty} x ^ {n + m n} / m = \sum_ {n = 1} ^ {\infty} x ^ {n} (- \ln (1 - x ^ {n})) \\ <   \sum_ {n = 1} ^ {\infty} x ^ {n} (- \ln (1 - x)), \\ \end{array}
\]
<|det|>text [554, 675, 920, 719]<|/det|>which converges. (Note that  \( -\ln(1-x) \)  and  \( -\ln(1-x^{n}) \)  are positive.) Hence we may interchange the summations in  \( f(x) \)  to obtain
<|det|>equation [565, 730, 868, 807]<|/det|>\[
\begin{array}{l} f (x) = (1 / x - 1) \sum_ {m = 1} ^ {\infty} \sum_ {n = 1} ^ {\infty} \frac {(- 1) ^ {m + 1} x ^ {(m + 1) n}}{m} \\ = (1 / x - 1) \sum_ {m = 1} ^ {\infty} \frac {(- 1) ^ {m + 1}}{m} \left(\frac {x ^ {m} (1 - x)}{1 - x ^ {m + 1}}\right). \\ \end{array}
\]
<|det|>text [554, 817, 920, 847]<|/det|>This last sum converges absolutely uniformly in \( x \), so it is legitimate to take limits term by term. Since
