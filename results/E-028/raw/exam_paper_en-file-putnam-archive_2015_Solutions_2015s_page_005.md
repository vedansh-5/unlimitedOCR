<|det|>page_number [912, 35, 923, 47]<|/det|>5
<|det|>text [145, 67, 277, 82]<|/det|>- \((a)_n\) implies \((b)_n\);
<|det|>text [145, 87, 457, 102]<|/det|>- \((a)_n\) and \((b)_1, \ldots, (b)_n\) together imply \((a)_{n+1}\).
<|det|>text [124, 111, 491, 213]<|/det|>To produce a value of \( n \) for which \( s_n \equiv 2015 \pmod{10000} \), we take \( n = 3m + 1 \) for some nonnegative integer \( m \) for which \( s_{3m+1} = 30m + 15 \). We must also have \( 30m \equiv 2000 \pmod{10000} \), or equivalently \( m \equiv 400 \pmod{1000} \). By taking \( m = 1400 \), we ensure that \( m \equiv 2 \pmod{3} \), so \( s_m = 10m + 7 \); this ensures that \( s_n \) does indeed equal \( 30m + 15 = 42015 \), as desired.
<|det|>text [124, 217, 492, 275]<|/det|>Remark: With a bit more work, we can give a complete description of  \( s_{n} \) , and in particular find the first term in the sequence whose decimal expansion ends in 2015. Define the function on nonnegative integers
<|det|>equation [198, 287, 376, 304]<|/det|>\[
f (n) = s _ {3 n + 1} - (3 0 n + 1 6)
\]
<|det|>text [125, 315, 434, 331]<|/det|>which takes values in \(\{-1,0,1\}\); we then have
<|det|>equation [138, 342, 434, 400]<|/det|>\[
f (n) = \left\{ \begin{array}{l l} 0 & n \equiv 0 \pmod {3} \\ - f ((n - 1) / 3) & n \equiv 1 \pmod {3} \\ - 1 & n \equiv 2 \pmod {3}. \end{array} \right.
\]
<|det|>text [124, 410, 491, 456]<|/det|>Consequently, if we write n in base 3, then  \( f(n) = 0 \)  unless the expansion ends with 2 followed by a string of 1s of length  \( k \geq 0 \) , in which case  \( f(n) = (-1)^{k+1} \) .
<|det|>text [124, 459, 492, 533]<|/det|>In this notation, we have  \( s_{n} \equiv 2015 \pmod{10000} \)  if and only if  \( n = 3m + 1 \)  for some nonnegative integer m for which  \( m \equiv 400 \pmod{1000} \)  and  \( f(m) = -1 \) . Since  \( 400 = 112211_{(3)} \) , the first such term in the sequence is in fact  \( s_{1201} = 12015 \) .
<|det|>text [100, 541, 491, 617]<|/det|>B3 First solution: Any element of S can be written as  \( M = \alpha A + \beta B \) , where  \( A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \) ,  \( B = \begin{pmatrix} -3 & -1 \\ 1 & 3 \end{pmatrix} \) , and  \( \alpha, \beta \in R \) . Note that  \( A^{2} = \begin{pmatrix} 4 & 4 \\ 4 & 4 \end{pmatrix} \)  and  \( B^{3} = \begin{pmatrix} -24 & -8 \\ 8 & 24 \end{pmatrix} \)  are both in S, and so any matrix of the form  \( \alpha A \)  or  \( \beta B \) ,  \( \alpha, \beta \in R \) , satisfies the given condition.
<|det|>text [124, 620, 492, 867]<|/det|>We claim that these are also the only matrices in \(S\) satisfying the given condition. Indeed, suppose \(M = \alpha A + \beta B\) where \(\alpha, \beta \neq 0\). Let \(C = \begin{pmatrix} 1 & 1/\sqrt{2} \\ 1/\sqrt{2} & 1/\sqrt{2} \end{pmatrix}\) with inverse \(C^{-1} = \begin{pmatrix} 1/2 & -1/2 \\ 1/\sqrt{2} & 1/\sqrt{2} \end{pmatrix}\). If we define \(D = C^{-1}MC\), then \(D = 2\alpha \begin{pmatrix} 0 & \gamma \\ \gamma & 1 \end{pmatrix}\) where \(\gamma = -\frac{\beta\sqrt{2}}{\alpha}\). Now suppose that \(M^k\) is in \(S\) with \(k \geq 2\). Since \((1-1)A \begin{pmatrix} 1 \\ -1 \end{pmatrix} = (1-1)B \begin{pmatrix} 1 \\ -1 \end{pmatrix} = 0\), we have \((1-1)M^k \begin{pmatrix} 1 \\ -1 \end{pmatrix} = 0\), and so the upper left entry of \(C^{-1}M^kC = D^k\) is 0. On the other hand, from the expression for \(D\), an easy induction on \(k\) shows that \(D^k = (2\alpha)^k \begin{pmatrix} \gamma^2 p_{k-1} & \gamma p_k \\ \gamma p_k & p_{k+1} \end{pmatrix}\), where \(p_k\) is defined inductively by \(p_0 = 0\), \(p_1 = 1\), \(p_{k+2} = \gamma^2 p_k + p_{k+1}\). In particular, it follows from the inductive definition that \(p_k > 0\) when \(k \geq 1\), whence the upper left entry of \(D^k\) is nonzero when \(k \geq 2\), a contradiction.
<|det|>text [124, 871, 490, 901]<|/det|>Remark: A variant of this solution can be obtained by diagonalizing the matrix M.
<|det|>text [554, 67, 920, 96]<|/det|>Second solution: If \(a, b, c, d\) are in arithmetic progression, then we may write
<|det|>equation [580, 109, 855, 124]<|/det|>\[
a = r - 3 s, b = r - s, c = r + s, d = r + 3 s
\]
<|det|>text [553, 135, 920, 178]<|/det|>for some \( r, s \). If \( s = 0 \), then clearly all powers of \( M \) are in \( xS \). Also, if \( r = 0 \), then one easily checks that \( M^3 \) is in \( S \).
<|det|>text [553, 183, 921, 329]<|/det|>We now assume  \( rs \neq 0 \) , and show that in that case M cannot be in S. First, note that the characteristic polynomial of M is  \( x^{2} - 2rx - 8s^{2} \) , and since M is nonsingular (as  \( s \neq 0 \) ), this is also the minimal polynomial of M by the Cayley-Hamilton theorem. By repeatedly using the relation  \( M^{2} = 2rM + 8s^{2}I \) , we see that for each positive integer, we have  \( M^{k} = t_{k}M + u_{k}I \)  for unique real constants  \( t_{k}, u_{k} \)  (uniqueness follows from the independence of M and I). Since M is in S, we see that  \( M^{k} \)  lies in S only if  \( u_{k} = 0 \) .
<|det|>text [553, 333, 920, 421]<|/det|>On the other hand, we claim that if k > 1, then  \( rt_{k} > 0 \)  and  \( u_{k} > 0 \)  if k is even, and  \( t_{k} > 0 \)  and  \( ru_{k} > 0 \)  if k is odd (in particular,  \( u_{k} \)  can never be zero). The claim is true for k = 2 by the relation  \( M^{2} = 2rM + 8s^{2}I \) . Assuming the claim for k, and multiplying both sides of the relation  \( M^{k} = t_{k}M + u_{k}I \)  by M, yields
<|det|>equation [533, 431, 900, 449]<|/det|>\[
M ^ {k + 1} = t _ {k} (2 r M + 8 s ^ {2} I) + u _ {k} M = (2 r t _ {k} + u _ {k}) M + 8 s ^ {2} t _ {k} I,
\]
<|det|>text [554, 460, 747, 475]<|/det|>implying the claim for  \( k + 1 \) .
<|det|>text [553, 479, 920, 523]<|/det|>Remark: (from artofproblemsolving.com, user hoeij) Once one has  \( u_{k}=0 \) , one can also finish using the relation  \( M\cdot M^{k}=M^{k}\cdot M \) .
<|det|>text [530, 533, 920, 577]<|/det|>B4 First solution: The answer is 17/21. For fixed b, c, there is a triangle of side lengths a, b, c if and only if  \( |b - c| < a < b + c \) . It follows that the desired sum is
<|det|>equation [550, 587, 882, 631]<|/det|>\[
S = \sum_ {b, c} \frac {1}{3 ^ {b} 5 ^ {c}} \left(\sum_ {a = b - c | + 1} ^ {b + c - 1} 2 ^ {a}\right) = \sum_ {b, c} \frac {2 ^ {b + c} - 2 ^ {| b - c | + 1}}{3 ^ {b} 5 ^ {c}}.
\]
<|det|>text [554, 640, 919, 670]<|/det|>We write this as \( S = S_{1} + S_{2} \) where \( S_{1} \) sums over positive integers \( b, c \) with \( b \leq c \) and \( S_{2} \) sums over \( b > c \). Then
<|det|>equation [586, 680, 845, 877]<|/det|>\[
\begin{array}{l} S _ {1} = \sum_ {b = 1} ^ {\infty} \sum_ {c = b} ^ {\infty} \frac {2 ^ {b + c} - 2 ^ {c - b + 1}}{3 ^ {b} 5 ^ {c}} \\ = \sum_ {b = 1} ^ {\infty} \left(\left(\left(\frac {2}{3}\right) ^ {b} - \frac {2}{6 ^ {b}}\right) \sum_ {c = b} ^ {\infty} \left(\frac {2}{5}\right) ^ {c}\right) \\ = \sum_ {b = 1} ^ {\infty} \left(\left(\frac {2}{3}\right) ^ {b} - \frac {2}{6 ^ {b}}\right) \frac {5}{3} \left(\frac {2}{5}\right) ^ {b} \\ = \sum_ {b = 1} ^ {\infty} \left(\frac {5}{3} \left(\frac {4}{1 5}\right) ^ {b} - \frac {1 0}{3} \left(\frac {1}{1 5}\right) ^ {b}\right) \\ = \frac {8 5}{2 3 1}. \\ \end{array}
\]
