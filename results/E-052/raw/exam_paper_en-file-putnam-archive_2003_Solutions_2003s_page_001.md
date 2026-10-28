<|det|>title [198, 64, 808, 101]<|/det|>Solutions to the 64th William Lowell Putnam Mathematical Competition
Saturday, December 6, 2003
<|det|>text [332, 114, 673, 131]<|/det|>Manjul Bhargava, Kiran Kedlaya, and Lenny Ng
<|det|>text [99, 165, 491, 224]<|/det|>A1 There are n such sums. More precisely, there is exactly one such sum with k terms for each of  \( k = 1, \ldots, n \)  (and clearly no others). To see this, note that if  \( n = a_{1} + a_{2} + \cdots + a_{k} \)  with  \( a_{1} \leq a_{2} \leq \cdots \leq a_{k} \leq a_{1} + 1 \) , then
<|det|>equation [154, 236, 420, 287]<|/det|>\[
\begin{array}{l} k a _ {1} = a _ {1} + a _ {1} + \dots + a _ {1} \\ \leq n \leq a _ {1} + (a _ {1} + 1) + \dots + (a _ {1} + 1) \\ = k a _ {1} + k - 1. \\ \end{array}
\]
<|det|>text [123, 300, 491, 401]<|/det|>However, there is a unique integer  \( a_{1} \)  satisfying these inequalities, namely  \( a_{1} = \lfloor n/k \rfloor \) . Moreover, once  \( a_{1} \)  is fixed, there are k different possibilities for the sum  \( a_{1} + a_{2} + \cdots + a_{k} \) : if i is the last integer such that  \( a_{i} = a_{1} \) , then the sum equals  \( ka_{1} + (i - 1) \) . The possible values of i are  \( 1, \ldots, k \) , and exactly one of these sums comes out equal to n, proving our claim.
<|det|>text [124, 405, 490, 480]<|/det|>Note: In summary, there is a unique partition of n with k terms that is “as equally spaced as possible”. One can also obtain essentially the same construction inductively: except for the all-ones sum, each partition of n is obtained by “augmenting” a unique partition of n - 1.
<|det|>text [99, 487, 491, 532]<|/det|>A2 First solution: Assume without loss of generality that  \( a_{i} + b_{i} > 0 \)  for each i (otherwise both sides of the desired inequality are zero). Then the AM-GM inequality gives
<|det|>equation [104, 546, 473, 620]<|/det|>\[
\begin{array}{l} \left(\frac {a _ {1} \cdots a _ {n}}{(a _ {1} + b _ {1}) \cdots (a _ {n} + b _ {n})}\right) ^ {1 / n} \\ \leq \frac {1}{n} \left(\frac {a _ {1}}{a _ {1} + b _ {1}} + \dots + \frac {a _ {n}}{a _ {n} + b _ {n}}\right), \\ \end{array}
\]
<|det|>text [124, 629, 490, 671]<|/det|>and likewise with the roles of a and b reversed. Adding these two inequalities and clearing denominators yields the desired result.
<|det|>text [124, 677, 490, 706]<|/det|>Second solution: Write the desired inequality in the form
<|det|>equation [104, 715, 471, 736]<|/det|>\[
(a _ {1} + b _ {1}) \dots (a _ {n} + b _ {n}) \geq [ (a _ {1} \dots a _ {n}) ^ {1 / n} + (b _ {1} \dots b _ {n}) ^ {1 / n} ] ^ {n},
\]
<|det|>text [124, 746, 491, 805]<|/det|>expand both sides, and compare the terms on both sides in which k of the terms are among the  \( a_{i} \) . On the left, one has the product of each k-element subset of  \( \{1,\ldots,n\} \) ; on the right, one has
<|det|>equation [163, 814, 414, 849]<|/det|>\[
\binom {n} {k} (a _ {1} \dots a _ {n}) ^ {k / n} \dots (b _ {1} \dots b _ {n}) ^ {(n - k) / n},
\]
<|det|>text [124, 859, 492, 933]<|/det|>which is precisely  \( \binom{n}{k} \)  times the geometric mean of the terms on the left. Thus AM-GM shows that the terms under consideration on the left exceed those on the right; adding these inequalities over all k yields the desired result.
<|det|>text [553, 165, 921, 238]<|/det|>Third solution: Since both sides are continuous in each  \( a_{i} \) , it is sufficient to prove the claim with  \( a_{1},\ldots,a_{n} \)  all positive (the general case follows by taking limits as some of the  \( a_{i} \)  tend to zero). Put  \( r_{i}=b_{i}/a_{i} \) ; then the given inequality is equivalent to
<|det|>equation [570, 248, 864, 268]<|/det|>\[
(1 + r _ {1}) ^ {1 / n} \dots (1 + r _ {n}) ^ {1 / n} \geq 1 + (r _ {1} \dots r _ {n}) ^ {1 / n}.
\]
<|det|>text [555, 279, 714, 293]<|/det|>In terms of the function
<|det|>equation [653, 305, 780, 323]<|/det|>\[
f (x) = \log (1 + e ^ {x})
\]
<|det|>text [554, 333, 920, 363]<|/det|>and the quantities \( s_i = \log r_i \), we can rewrite the desired inequality as
<|det|>equation [570, 373, 864, 408]<|/det|>\[
\frac {1}{n} (f (s _ {1}) + \dots + f (s _ {n})) \geq f \left(\frac {s _ {1} + \cdots + s _ {n}}{n}\right).
\]
<|det|>text [554, 416, 920, 461]<|/det|>This will follow from Jensen's inequality if we can verify that \( f \) is a convex function; it is enough to check that \( f''(x) > 0 \) for all \( x \). In fact,
<|det|>equation [621, 471, 811, 502]<|/det|>\[
f ^ {\prime} (x) = \frac {e ^ {x}}{1 + e ^ {x}} = 1 - \frac {1}{1 + e ^ {x}}
\]
<|det|>text [553, 512, 920, 600]<|/det|>is an increasing function of \( x \), so \( f''(x) > 0 \) and Jensen's inequality thus yields the desired result. (As long as the \( a_i \) are all positive, equality holds when \( s_1 = \cdots = s_n \), i.e., when the vectors \( (a_1, \ldots, a_n) \) and \( (b_1, \ldots, b_n) \). Of course other equality cases crop up if some of the \( a_i \) vanish, i.e., if \( a_1 = b_1 = 0 \).)
<|det|>text [555, 605, 920, 636]<|/det|>Fourth solution: We apply induction on n, the case n = 1 being evident. First we verify the auxiliary inequality
<|det|>equation [577, 644, 857, 663]<|/det|>\[
(a ^ {n} + b ^ {n}) (c ^ {n} + d ^ {n}) ^ {n - 1} \geq (a c ^ {n - 1} + b d ^ {n - 1}) ^ {n}
\]
<|det|>text [554, 673, 868, 688]<|/det|>for \(a, b, c, d \geq 0\). The left side can be written as
<|det|>equation [582, 698, 852, 799]<|/det|>\[
\begin{array}{l} a ^ {n} c ^ {n (n - 1)} + b ^ {n} d ^ {n (n - 1)} \\ + \sum_ {i = 1} ^ {n - 1} \binom {n - 1} {i} b ^ {n} c ^ {n i} d ^ {n (n - 1 - i)} \\ + \sum_ {i = 1} ^ {n - 1} \binom {n - 1} {i - 1} a ^ {n} c ^ {n (i - 1)} d ^ {n (n - i)}. \\ \end{array}
\]
<|det|>text [554, 809, 920, 839]<|/det|>Applying the weighted AM-GM inequality between matching terms in the two sums yields
<|det|>equation [531, 852, 905, 913]<|/det|>\[
\begin{array}{l} (a ^ {n} + b ^ {n}) (c ^ {n} + d ^ {n}) ^ {n - 1} \geq a ^ {n} c ^ {n (n - 1)} + b ^ {n} d ^ {n (n - 1)} \\ + \sum_ {i = 1} ^ {n - 1} \binom {n} {i} a ^ {i} b ^ {n - i} c ^ {(n - 1) i} d ^ {(n - 1) (n - i)}, \\ \end{array}
\]
