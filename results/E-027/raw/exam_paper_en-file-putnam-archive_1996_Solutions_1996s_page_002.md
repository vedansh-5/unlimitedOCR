<|det|>page_number [913, 35, 923, 46]<|/det|>2
<|det|>text [125, 66, 194, 79]<|/det|>Therefore
<|det|>equation [140, 93, 437, 110]<|/det|>\[
(a _ {i}, z, a _ {i + 1}), (a _ {i + 1}, a _ {j}, a _ {i}) \in S \Rightarrow (a _ {j}, a _ {i}, z) \in S
\]
<|det|>equation [155, 112, 430, 129]<|/det|>\[
(a _ {i}, z, a _ {j}), (a _ {j}, a _ {j + 1}, a _ {i}) \in S \Rightarrow (z, a _ {j}, a _ {j + 1}),
\]
<|det|>text [140, 138, 476, 155]<|/det|>so \((a_{j},z,a_{j + 1})\notin S\) . The case \(j = i + 1\) is ruled out by
<|det|>equation [135, 165, 457, 182]<|/det|>\[
(a _ {i}, z, a _ {i + 1}), (a _ {i + 1}, a _ {i + 2}, a _ {i}) \in S \Rightarrow (z, a _ {i + 1}, a _ {i + 2}) \in S
\]
<|det|>text [140, 192, 338, 206]<|/det|>and the case \( j = i - 1 \) is similar.
<|det|>text [140, 211, 490, 220]<|/det|>Finally, we put \( g(z) \) in \( (g(a_n), +\infty) \) if \( i = n \), and
<|det|>text [140, 222, 489, 236]<|/det|>\( (g(a_{i}), g(a_{i+1})) \) otherwise; an analysis similar to that
<|det|>text [140, 237, 383, 251]<|/det|>above shows that \( g \) has the desired property.
<|det|>text [90, 264, 490, 281]<|/det|>A-5 (due to Lenny Ng) For \(1 \leq n \leq p - 1\), \(p\) divides \(\binom{p}{n}\) and
<|det|>equation [166, 293, 408, 358]<|/det|>\[
\begin{array}{l} \frac {1}{p} \binom {p} {n} = \frac {1}{n} \frac {p - 1}{1} \frac {p - 2}{2} \dots \frac {p - n + 1}{n - 1} \\ \equiv \frac {(- 1) ^ {n - 1}}{n} (\mathrm{mod} p), \\ \end{array}
\]
<|det|>text [124, 371, 490, 415]<|/det|>where the congruence \( x \equiv y \pmod{p} \) means that \( x - y \) is a rational number whose numerator, in reduced form, is divisible by \( p \). Hence it suffices to show that
<|det|>equation [198, 426, 374, 464]<|/det|>\[
\sum_ {n = 1} ^ {k} \frac {(- 1) ^ {n - 1}}{n} \equiv 0 (\mathrm{mod} p).
\]
<|det|>text [124, 476, 489, 506]<|/det|>We distinguish two cases based on \( p \) (mod6). First suppose \( p = 6r + 1 \), so that \( k = 4r \). Then
<|det|>equation [97, 515, 475, 636]<|/det|>\[
\begin{array}{l} \sum_ {n = 1} ^ {4 r} \frac {(- 1) ^ {n - 1}}{n} = \sum_ {n = 1} ^ {4 r} \frac {1}{n} - 2 \sum_ {n = 1} ^ {2 r} \frac {1}{2 n} \\ = \sum_ {n = 1} ^ {2 r} \left(\frac {1}{n} - \frac {1}{n}\right) + \sum_ {n = 2 r + 1} ^ {3 r} \left(\frac {1}{n} + \frac {1}{6 r + 1 - n}\right) \\ = \sum_ {n = 2 r + 1} ^ {3 r} \frac {p}{n (p - n)} \equiv 0 (\mathrm{mod} p), \\ \end{array}
\]
<|det|>text [125, 646, 241, 661]<|/det|>since \( p = 6r + 1 \).
<|det|>text [124, 665, 490, 695]<|/det|>Now suppose \( p = 6r + 5 \), so that \( k = 4r + 3 \). A similar argument gives
<|det|>equation [95, 705, 482, 826]<|/det|>\[
\begin{array}{l} \sum_ {n = 1} ^ {4 r + 3} \frac {(- 1) ^ {n - 1}}{n} = \sum_ {n = 1} ^ {4 r + 3} \frac {1}{n} + 2 \sum_ {n = 1} ^ {2 r + 1} \frac {1}{2 n} \\ = \sum_ {n = 1} ^ {2 r + 1} \left(\frac {1}{n} - \frac {1}{n}\right) + \sum_ {n = 2 r + 2} ^ {3 r + 2} \left(\frac {1}{n} + \frac {1}{6 r + 5 - n}\right) \\ = \sum_ {n = 2 r + 2} ^ {3 r + 2} \frac {p}{n (p - n)} \equiv 0 (\mathrm{mod} p). \\ \end{array}
\]
<|det|>text [91, 842, 490, 871]<|/det|>A-6 We first consider the case \( c \leq 1/4 \); we shall show in this case \( f \) must be constant. The relation
<|det|>equation [145, 881, 428, 899]<|/det|>\[
f (x) = f \left(x ^ {2} + c\right) = f \left((- x) ^ {2} + c\right) = f (- x)
\]
<|det|>text [124, 911, 490, 940]<|/det|>proves that \( f \) is an even function. Let \( r_1 \leq r_2 \) be the roots of \( x^2 + c - x \), both of which are real. If \( x > r_2 \),
<|det|>text [553, 65, 920, 156]<|/det|>define  \( x_{0}=x \)  and  \( x_{n+1}=\sqrt{x_{n}-c} \)  for each positive integer x. By induction on n,  \( r_{2}<x_{n+1}<x_{n} \)  for all n, so the sequence  \( \{x_{n}\} \)  tends to a limit L which is a root of  \( x^{2}+c=x \)  not less than  \( r_{2} \) . Of course this means  \( L=r_{2} \) . Since  \( f(x)=f(x_{n}) \)  for all n and  \( x_{n}\to r_{2} \) , we conclude  \( f(x)=f(r_{2}) \) , so f is constant on  \( x\geq r_{2} \) .
<|det|>text [553, 159, 920, 260]<|/det|>If  \( r_{1} < x < r_{2} \)  and  \( x_{n} \)  is defined as before, then by induction,  \( x_{n} < x_{n+1} < r_{2} \) . Note that the sequence can be defined because  \( r_{1} > c \) ; the latter follows by noting that the polynomial  \( x^{2} - x + c \)  is positive at x = c and has its minimum at 1/2 > c, so both roots are greater than c. In any case, we deduce that  \( f(x) \)  is also constant on  \( r_{1} \leq x \leq r_{2} \) .
<|det|>text [553, 264, 920, 395]<|/det|>Finally, suppose \( x < r_1 \). Now define \( x_0 = x, x_{n+1} = x_n^2 + c \). Given that \( x_n < r_1 \), we have \( x_{n+1} > x_n \). Thus if we had \( x_n < r_1 \) for all \( n \), by the same argument as in the first case we deduce \( x_n \to r_1 \) and so \( f(x) = f(r_1) \). Actually, this doesn't happen; eventually we have \( x_n > r_1 \), in which case \( f(x) = f(x_n) = f(r_1) \) by what we have already shown. We conclude that \( f \) is a constant function. (Thanks to Marshall Buck for catching an inaccuracy in a previous version of this solution.)
<|det|>text [553, 400, 920, 531]<|/det|>Now suppose c > 1/4. Then the sequence  \( x_{n} \)  defined by  \( x_{0} = 0 \)  and  \( x_{n+1} = x_{n}^{2} + c \)  is strictly increasing and has no limit point. Thus if we define f on  \( [x_{0}, x_{1}] \)  as any continuous function with equal values on the endpoints, and extend the definition from  \( [x_{n}, x_{n+1}] \)  to  \( [x_{n+1}, x_{n+2}] \)  by the relation  \( f(x) = f(x^{2} + c) \) , and extend the definition further to x < 0 by the relation  \( f(x) = f(-x) \) , the resulting function has the desired property. Moreover, any function with that property clearly has this form.
<|det|>text [521, 540, 920, 759]<|/det|>B-1 Let \([n]\) denote the set \(\{1,2,\ldots,n\}\), and let \(f_n\) denote the number of minimal selfish subsets of \([n]\). Then the number of minimal selfish subsets of \([n]\) not containing \(n\) is equal to \(f_{n-1}\). On the other hand, for any minimal selfish subset of \([n]\) containing \(n\), by subtracting 1 from each element, and then taking away the element \(n-1\) from the set, we obtain a minimal selfish subset of \([n-2]\) (since 1 and \(n\) cannot both occur in a selfish set). Conversely, any minimal selfish subset of \([n-2]\) gives rise to a minimal selfish subset of \([n]\) containing \(n\) by the inverse procedure. Hence the number of minimal selfish subsets of \([n]\) containing \(n\) is \(f_{n-2}\). Thus we obtain \(f_n = f_{n-1} + f_{n-2}\). Since \(f_1 = f_2 = 1\), we have \(f_n = F_n\), where \(F_n\) denotes the \(n\)th term of the Fibonacci sequence.
<|det|>text [521, 768, 919, 798]<|/det|>B-2 By estimating the area under the graph of \(\ln x\) using upper and lower rectangles of width 2, we get
<|det|>equation [576, 807, 857, 871]<|/det|>\[
\begin{array}{l} \int_ {1} ^ {2 n - 1} \ln x d x \leq 2 (\ln (3) + \dots + \ln (2 n - 1)) \\ \leq \int_ {3} ^ {2 n + 1} \ln x d x. \\ \end{array}
\]
<|det|>text [555, 882, 919, 898]<|/det|>Since \(\int \ln x dx = x\ln x - x + C\), we have, upon exponen-
