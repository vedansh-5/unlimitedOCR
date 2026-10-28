<|det|>title [198, 64, 808, 101]<|/det|>Solutions to the 58th Willam Lowell Putnam Mathematical Competition
Saturday, December 6, 1997
<|det|>text [332, 114, 673, 131]<|/det|>Manjul Bhargava, Kiran Kedlaya, and Lenny Ng
<|det|>text [90, 165, 493, 239]<|/det|>A-1 The centroid G of the triangle is collinear with H and O (Euler line), and the centroid lies two-thirds of the way from A to M. Therefore H is also two-thirds of the way from A to F, so AF = 15. Since the triangles BFH and AFC are similar (they're right triangles and
<|det|>equation [183, 250, 393, 266]<|/det|>\[
\angle H B C = \pi / 2 - \angle C = \angle C A F),
\]
<|det|>text [125, 278, 185, 292]<|/det|>we have
<|det|>equation [222, 304, 354, 320]<|/det|>\[
B F / F H = A F / F C
\]
<|det|>text [125, 333, 145, 345]<|/det|>or
<|det|>equation [200, 357, 373, 372]<|/det|>\[
B F \cdot F C = F H \cdot A F = 7 5.
\]
<|det|>text [125, 385, 163, 398]<|/det|>Now
<|det|>equation [130, 410, 445, 428]<|/det|>\[
B C ^ {2} = (B F + F C) ^ {2} = (B F - F C) ^ {2} + 4 B F \cdot F C,
\]
<|det|>text [125, 439, 152, 452]<|/det|>but
<|det|>equation [117, 465, 459, 481]<|/det|>\[
B F - F C = B M + M F - (M C - M F) = 2 M F = 2 2,
\]
<|det|>text [125, 495, 145, 506]<|/det|>SO
<|det|>equation [170, 517, 404, 536]<|/det|>\[
B C = \sqrt {2 2 ^ {2} + 4 \cdot 7 5} = \sqrt {7 8 4} = 2 8.
\]
<|det|>text [90, 552, 491, 640]<|/det|>A–2 We show more precisely that the game terminates with one player holding all of the pennies if and only if  \( n = 2^{m} + 1 \)  or  \( n = 2^{m} + 2 \)  for some m. First suppose we are in the following situation for some  \( k \geq 2 \) . (Note: for us, a “move” consists of two turns, starting with a one-penny pass.)
<|det|>text [145, 649, 490, 680]<|/det|>- Except for the player to move, each player has \( k \) pennies;
<|det|>text [145, 684, 437, 699]<|/det|>- The player to move has at least \( k \) pennies.
<|det|>text [123, 708, 491, 884]<|/det|>We claim then that the game terminates if and only if the number of players is a power of 2. First suppose the number of players is even; then after \( m \) complete rounds, every other player, starting with the player who moved first, will have \( m \) more pennies than initially, and the others will all have 0. Thus we are reduced to the situation with half as many players; by this process, we eventually reduce to the case where the number of players is odd. However, if there is more than one player, after two complete rounds everyone has as many pennies as they did before (here we need \( m \geq 2 \)), so the game fails to terminate. This verifies the claim.
<|det|>text [123, 888, 491, 974]<|/det|>Returning to the original game, note that after one complete round,  \( \left\lfloor\frac{n-1}{2}\right\rfloor \)  players remain, each with 2 pennies except for the player to move, who has either 3 or 4 pennies. Thus by the above argument, the game terminates if and only if  \( \left\lfloor\frac{n-1}{2}\right\rfloor \)  is a power of 2, that is, if and only if  \( n=2^{m}+1 \)  or  \( n=2^{m}+2 \)  for some m.
<|det|>text [520, 165, 919, 196]<|/det|>A-3 Note that the series on the left is simply  \( x \exp(-x^{2}/2) \) . By integration by parts,
<|det|>equation [576, 204, 858, 235]<|/det|>\[
\int_ {0} ^ {\infty} x ^ {2 n + 1} e ^ {- x ^ {2} / 2} d x = 2 n \int_ {0} ^ {\infty} x ^ {2 n - 1} e ^ {- x ^ {2} / 2} d x
\]
<|det|>text [555, 244, 693, 259]<|/det|>and so by induction,
<|det|>equation [592, 269, 841, 300]<|/det|>\[
\int_ {0} ^ {\infty} x ^ {2 n + 1} e ^ {- x ^ {2} / 2} d x = 2 \times 4 \times \dots \times 2 n.
\]
<|det|>text [555, 309, 785, 325]<|/det|>Thus the desired integral is simply
<|det|>equation [664, 334, 771, 370]<|/det|>\[
\sum_ {n = 0} ^ {\infty} \frac {1}{2 ^ {n} n !} = \sqrt {e}.
\]
<|det|>text [520, 386, 920, 414]<|/det|>A-4 In order to have \(\psi(x) = a\phi(x)\) for all \(x\), we must in particular have this for \(x = e\), and so we take \(a = \phi(e)^{-1}\).
<|det|>text [556, 415, 672, 428]<|/det|>We first note that
<|det|>equation [596, 441, 838, 459]<|/det|>\[
\phi (g) \phi (e) \phi (g ^ {- 1}) = \phi (e) \phi (g) \phi (g ^ {- 1})
\]
<|det|>text [554, 469, 920, 497]<|/det|>and so \(\phi(g)\) commutes with \(\phi(e)\) for all \(g\). Next, we note that
<|det|>equation [570, 509, 863, 528]<|/det|>\[
\phi (x) \phi (y) \phi (y ^ {- 1} x ^ {- 1}) = \phi (e) \phi (x y) \phi (y ^ {- 1} x ^ {- 1})
\]
<|det|>text [555, 538, 875, 553]<|/det|>and using the commutativity of \(\phi(e)\), we deduce
<|det|>equation [585, 564, 848, 583]<|/det|>\[
\phi (e) ^ {- 1} \phi (x) \phi (e) ^ {- 1} \phi (y) = \phi (e) ^ {- 1} \phi (x y)
\]
<|det|>text [555, 594, 779, 610]<|/det|>or \(\psi(xy) = \psi(x)\psi(y)\), as desired.
<|det|>text [520, 618, 920, 678]<|/det|>A–5 We may discard any solutions for which  \( a_{1} \neq a_{2} \) , since those come in pairs; so assume  \( a_{1} = a_{2} \) . Similarly, we may assume that  \( a_{3} = a_{4} \) ,  \( a_{5} = a_{6} \) ,  \( a_{7} = a_{8} \) ,  \( a_{9} = a_{10} \) . Thus we get the equation
<|det|>equation [585, 689, 848, 706]<|/det|>\[
2 / a _ {1} + 2 / a _ {3} + 2 / a _ {5} + 2 / a _ {7} + 2 / a _ {9} = 1.
\]
<|det|>text [554, 717, 920, 775]<|/det|>Again, we may assume  \( a_{1}=a_{3} \)  and  \( a_{5}=a_{7} \) , so we get  \( 4/a_{1}+4/a_{5}+2/a_{9}=1 \) ; and  \( a_{1}=a_{5} \) , so  \( 8/a_{1}+2/a_{9}=1 \) . This implies that  \( (a_{1}-8)(a_{9}-2)=16 \) , which by counting has 5 solutions. Thus  \( N_{10} \)  is odd.
<|det|>text [520, 784, 920, 873]<|/det|>A–6 Clearly  \( x_{n+1} \)  is a polynomial in c of degree n, so it suffices to identify n values of c for which  \( x_{n+1}=0 \) . We claim these are c=n-1-2r for  \( r=0,1,\ldots,n-1 \) ; in this case,  \( x_{k} \)  is the coefficient of  \( t^{k-1} \)  in the polynomial  \( f(t)=(1-t)^{r}(1+t)^{n-1-r} \) . This can be verified by noticing that f satisfies the differential equation
<|det|>equation [631, 882, 804, 916]<|/det|>\[
\frac {f ^ {\prime} (t)}{f (t)} = \frac {n - 1 - r}{1 + t} - \frac {r}{1 - t}
\]
