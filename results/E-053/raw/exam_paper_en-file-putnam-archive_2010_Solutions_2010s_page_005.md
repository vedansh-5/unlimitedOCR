<|det|>page_number [914, 35, 925, 47]<|/det|>5
<|det|>text [91, 66, 490, 153]<|/det|>B-5 First solution. The answer is no. Suppose otherwise. For the condition to make sense, \( f \) must be differentiable. Since \( f \) is strictly increasing, we must have \( f'(x) \geq 0 \) for all \( x \). Also, the function \( f'(x) \) is strictly increasing: if \( y > x \) then \( f'(y) = f(f(y)) > f(f(x)) = f'(x) \). In particular, \( f'(y) > 0 \) for all \( y \in \mathbb{R} \).
<|det|>text [123, 157, 490, 246]<|/det|>For any \( x_0 \geq -1 \), if \( f(x_0) = b \) and \( f'(x_0) = a > 0 \), then \( f'(x) > a \) for \( x > x_0 \) and thus \( f(x) \geq a(x - x_0) + b \) for \( x \geq x_0 \). Then either \( b < x_0 \) or \( a = f'(x_0) = f(f(x_0)) = f(b) \geq a(b - x_0) + b \). In the latter case, \( b \leq a(x_0 + 1)/(a + 1) \leq x_0 + 1 \). We conclude in either case that \( f(x_0) \leq x_0 + 1 \) for all \( x_0 \geq -1 \).
<|det|>text [123, 250, 491, 352]<|/det|>It must then be the case that  \( f'(f(x)) = f'(x) \leq 1 \)  for all x, since otherwise  \( f(x) > x + 1 \)  for large x. Now by the above reasoning, if  \( f(0) = b_{0} \)  and  \( f'(0) = a_{0} > 0 \) , then  \( f(x) > a_{0}x + b_{0} \)  for x > 0. Thus for  \( x > \max\{0, -b_{0}/a_{0}\} \) , we have  \( f(x) > 0 \)  and  \( f(f(x)) > a_{0}x + b_{0} \) . But then  \( f(f(x)) > 1 \)  for sufficiently large x, a contradiction.
<|det|>text [123, 357, 490, 488]<|/det|>Second solution. (Communicated by Catalan Zara.) Suppose such a function exists. Since \( f \) is strictly increasing and differentiable, so is \( f \circ f = f' \). In particular, \( f \) is twice differentiable; also, \( f''(x) = f'(f(x))f'(x) \) is the product of two strictly increasing nonnegative functions, so it is also strictly increasing and nonnegative. In particular, we can choose \( \alpha > 0 \) and \( M \in \mathbb{R} \) such that \( f'''(x) > 4\alpha \) for all \( x \geq M \). Then for all \( x \geq M \),
<|det|>equation [137, 499, 435, 517]<|/det|>\[
f (x) \geq f (M) + f ^ {\prime} (M) (x - M) + 2 \alpha (x - M) ^ {2}.
\]
<|det|>text [124, 526, 490, 555]<|/det|>In particular, for some \( M' > M \), we have \( f(x) \geq \alpha x^2 \) for all \( x \geq M' \).
<|det|>text [124, 559, 489, 591]<|/det|>Pick \( T > 0 \) so that \( \alpha T^2 > M' \). Then for \( x \geq T \), \( f(x) > M' \) and so \( f'(x) = f(f(x)) \geq \alpha f(x)^2 \). Now
<|det|>equation [141, 601, 435, 636]<|/det|>\[
\frac {1}{f (T)} - \frac {1}{f (2 T)} = \int_ {T} ^ {2 T} \frac {f ^ {\prime} (t)}{f (t) ^ {2}} d t \geq \int_ {T} ^ {2 T} \alpha d t;
\]
<|det|>text [124, 645, 490, 674]<|/det|>however, as  \( T \rightarrow \infty \) , the left side of this inequality tends to 0 while the right side tends to  \( +\infty \) , a contradiction.
<|det|>text [124, 679, 490, 724]<|/det|>Third solution. (Communicated by Noam Elkies.) Since \( f \) is strictly increasing, for some \( y_0 \), we can define the inverse function \( g(y) \) of \( f \) for \( y \geq y_0 \). Then
<|det|>text [553, 66, 920, 213]<|/det|>\( x = g(f(x)) \), and we may differentiate to find that \( 1 = g'(f(x))f'(x) = g'(f(x))f(f(x)) \). It follows that \( g'(y) = 1/f(y) \) for \( y \geq y_0 \); since \( g \) takes arbitrarily large values, the integral \( \int_{y_0}^{x} dy/f(y) \) must diverge. One then gets a contradiction from any reasonable lower bound on \( f(y) \) for \( y \) large, e.g., the bound \( f(x) \geq \alpha x^2 \) from the second solution. (One can also start with a linear lower bound \( f(x) \geq \beta x \), then use the integral expression for \( g \) to deduce that \( g(x) \leq \gamma \log x \), which in turn forces \( f(x) \) to grow exponentially.)
<|det|>text [521, 221, 920, 297]<|/det|>B-6 For any polynomial \( p(x) \), let \( [p(x)]A \) denote the \( n \times n \) matrix obtained by replacing each entry \( A_{ij} \) of \( A \) by \( p(A_{ij}) \); thus \( A^{[k]} = [x^k]A \). Let \( P(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_0 \) denote the characteristic polynomial of \( A \). By the Cayley-Hamilton theorem,
<|det|>equation [597, 307, 834, 386]<|/det|>\[
\begin{array}{l} 0 = A \cdot P (A) \\ = A ^ {n + 1} + a _ {n - 1} A ^ {n} + \dots + a _ {0} A \\ = A ^ {[ n + 1 ]} + a _ {n - 1} A ^ {[ n ]} + \dots + a _ {0} A ^ {[ 1 ]} \\ = [ x p (x) ] A. \\ \end{array}
\]
<|det|>text [555, 396, 915, 412]<|/det|>Thus each entry of \(A\) is a root of the polynomial \(xp(x)\).
<|det|>text [555, 416, 760, 431]<|/det|>Now suppose \(m \geq n + 1\). Then
<|det|>equation [580, 440, 852, 480]<|/det|>\[
\begin{array}{l} 0 = [ x ^ {m + 1 - n} P (x) ] A \\ = A ^ {[ m + 1 ]} + a _ {n - 1} A ^ {[ m ]} + \dots + a _ {0} A ^ {[ m + 1 - n ]} \\ \end{array}
\]
<|det|>text [554, 493, 919, 522]<|/det|>since each entry of \( A \) is a root of \( x^{m + 1 - n}P(x) \). On the other hand,
<|det|>equation [587, 533, 843, 571]<|/det|>\[
\begin{array}{l} 0 = A ^ {m + 1 - n} \cdot P (A) \\ = A ^ {m + 1} + a _ {n - 1} A ^ {m} + \dots + a _ {0} A ^ {m + 1 - n}. \\ \end{array}
\]
<|det|>text [554, 585, 919, 629]<|/det|>Therefore if \( A^k = A^{[k]} \) for \( m + 1 - n \leq k \leq m \), then \( A^{m+1} = A^{[m+1]} \). The desired result follows by induction on \( m \).
<|det|>text [554, 634, 920, 692]<|/det|>Remark. David Feldman points out that the result is best possible in the following sense: there exist examples of  \( n \times n \)  matrices A for which  \( A^{k} = A^{[k]} \)  for  \( k = 1, \ldots, n \)  but  \( A^{n+1} \neq A^{[n+1]} \) .
