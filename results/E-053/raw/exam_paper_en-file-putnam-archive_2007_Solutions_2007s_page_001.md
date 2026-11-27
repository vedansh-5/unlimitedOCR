<|det|>title [198, 64, 808, 101]<|/det|>Solutions to the 68th William Lowell Putnam Mathematical Competition
Saturday, December 1, 2007
<|det|>text [332, 114, 672, 131]<|/det|>Manjul Bhargava, Kiran Kedlaya, and Lenny Ng
<|det|>text [90, 164, 440, 181]<|/det|>A-1 The only such \(\alpha\) are \(2/3, 3/2\), \((13 \pm \sqrt{601})/12\).
<|det|>text [124, 184, 491, 228]<|/det|>First solution: Let  \( C_{1} \)  and  \( C_{2} \)  be the curves  \( y = \alpha x^{2} + \alpha x + \frac{1}{24} \)  and  \( x = \alpha y^{2} + \alpha y + \frac{1}{24} \) , respectively, and let L be the line y = x. We consider three cases.
<|det|>text [124, 233, 490, 261]<|/det|>If \( C_1 \) is tangent to \( L \), then the point of tangency \( (x, x) \) satisfies
<|det|>equation [157, 272, 418, 300]<|/det|>\[
2 \alpha x + \alpha = 1, \quad x = \alpha x ^ {2} + \alpha x + \frac {1}{2 4};
\]
<|det|>text [124, 309, 491, 354]<|/det|>by symmetry,  \( C_{2} \)  is tangent to L there, so  \( C_{1} \)  and  \( C_{2} \)  are tangent. Writing  \( \alpha = 1/(2x + 1) \)  in the first equation and substituting into the second, we must have
<|det|>equation [227, 364, 348, 397]<|/det|>\[
x = \frac {x ^ {2} + x}{2 x + 1} + \frac {1}{2 4},
\]
<|det|>text [125, 408, 490, 454]<|/det|>which simplifies to  \( 0 = 24x^{2} - 2x - 1 = (6x + 1)(4x - 1) \) , or  \( x \in \{1/4, -1/6\} \) . This yields  \( \alpha = 1/(2x + 1) \in \{2/3, 3/2\} \) .
<|det|>text [124, 457, 490, 487]<|/det|>If  \( C_{1} \)  does not intersect L, then  \( C_{1} \)  and  \( C_{2} \)  are separated by L and so cannot be tangent.
<|det|>text [124, 490, 491, 580]<|/det|>If  \( C_{1} \)  intersects L in two distinct points  \( P_{1}, P_{2} \) , then it is not tangent to L at either point. Suppose at one of these points, say  \( P_{1} \) , the tangent to  \( C_{1} \)  is perpendicular to L; then by symmetry, the same will be true of  \( C_{2} \) , so  \( C_{1} \)  and  \( C_{2} \)  will be tangent at  \( P_{1} \) . In this case, the point  \( P_{1} = (x, x) \)  satisfies
<|det|>equation [150, 590, 421, 620]<|/det|>\[
2 \alpha x + \alpha = - 1, \quad x = \alpha x ^ {2} + \alpha x + \frac {1}{2 4};
\]
<|det|>text [124, 629, 490, 658]<|/det|>writing \(\alpha = -1 / (2x + 1)\) in the first equation and substituting into the second, we have
<|det|>equation [220, 668, 355, 702]<|/det|>\[
x = - \frac {x ^ {2} + x}{2 x + 1} + \frac {1}{2 4},
\]
<|det|>text [124, 713, 490, 745]<|/det|>or \( x = (-23 \pm \sqrt{601}) / 72 \). This yields \( \alpha = -1 / (2x + 1) = (13 \pm \sqrt{601}) / 12 \).
<|det|>text [124, 750, 491, 909]<|/det|>If instead the tangents to  \( C_{1} \)  at  \( P_{1}, P_{2} \)  are not perpendicular to L, then we claim there cannot be any point where  \( C_{1} \)  and  \( C_{2} \)  are tangent. Indeed, if we count intersections of  \( C_{1} \)  and  \( C_{2} \)  (by using  \( C_{1} \)  to substitute for y in  \( C_{2} \), then solving for y), we get at most four solutions counting multiplicity. Two of these are  \( P_{1} \)  and  \( P_{2} \), and any point of tangency counts for two more. However, off of L, any point of tangency would have a mirror image which is also a point of tangency, and there cannot be six solutions. Hence we have now found all possible  \( \alpha \).
<|det|>text [553, 165, 921, 237]<|/det|>Second solution: For any nonzero value of  \( \alpha \) , the two conics will intersect in four points in the complex projective plane  \( \mathbb{P}^{2}(\mathbb{C}) \) . To determine the y-coordinates of these intersection points, subtract the two equations to obtain
<|det|>equation [593, 250, 840, 266]<|/det|>\[
(y - x) = \alpha (x - y) (x + y) + \alpha (x - y).
\]
<|det|>text [553, 277, 921, 366]<|/det|>Therefore, at a point of intersection we have either x = y, or  \( x = -1/\alpha - (y + 1) \) . Substituting these two possible linear conditions into the second equation shows that the y-coordinate of a point of intersection is a root of either  \( Q_{1}(y) = \alpha y^{2} + (\alpha - 1)y + 1/24 \)  or  \( Q_{2}(y) = \alpha y^{2} + (\alpha + 1)y + 25/24 + 1/\alpha \) .
<|det|>text [553, 370, 921, 546]<|/det|>If two curves are tangent, then the y-coordinates of at least two of the intersection points will coincide; the converse is also true because one of the curves is the graph of a function in x. The coincidence occurs precisely when either the discriminant of at least one of  \( Q_{1} \)  or  \( Q_{2} \)  is zero, or there is a common root of  \( Q_{1} \)  and  \( Q_{2} \) . Computing the discriminants of  \( Q_{1} \)  and  \( Q_{2} \)  yields (up to constant factors)  \( f_{1}(\alpha)=6\alpha^{2}-13\alpha+6 \)  and  \( f_{2}(\alpha)=6\alpha^{2}-13\alpha-18 \) , respectively. If on the other hand  \( Q_{1} \)  and  \( Q_{2} \)  have a common root, it must be also a root of  \( Q_{2}(y)-Q_{1}(y)=2y+1+1/\alpha \) , yielding  \( y=-(1+\alpha)/(2\alpha) \)  and  \( 0=Q_{1}(y)=-f_{2}(\alpha)/(24\alpha) \) .
<|det|>text [553, 548, 920, 593]<|/det|>Thus the values of  \( \alpha \)  for which the two curves are tangent must be contained in the set of zeros of  \( f_{1} \)  and  \( f_{2} \) , namely 2/3, 3/2, and  \( (13 \pm \sqrt{601})/12 \) .
<|det|>text [553, 595, 920, 670]<|/det|>Remark: The fact that the two conics in  \( \mathbb{P}^{2}(\mathbb{C}) \)  meet in four points, counted with multiplicities, is a special case of Bézout's theorem: two curves in  \( \mathbb{P}^{2}(\mathbb{C}) \)  of degrees m, n and not sharing any common component meet in exactly mn points when counted with multiplicity.
<|det|>text [553, 673, 920, 819]<|/det|>Many solvers were surprised that the proposers chose the parameter 1/24 to give two rational roots and two nonrational roots. In fact, they had no choice in the matter: attempting to make all four roots rational by replacing 1/24 by  \( \beta \)  amounts to asking for  \( \beta^{2} + \beta \)  and  \( \beta^{2} + \beta + 1 \)  to be perfect squares. This cannot happen outside of trivial cases ( \( \beta = 0, -1 \) ) ultimately because the elliptic curve 24A1 (in Cremona's notation) over Q has rank 0. (Thanks to Noam Elkies for providing this computation.)
<|det|>text [553, 822, 919, 881]<|/det|>However, there are choices that make the radical milder, e.g., \(\beta = 1/3\) gives \(\beta^2 + \beta = 4/9\) and \(\beta^2 + \beta + 1 = 13/9\), while \(\beta = 3/5\) gives \(\beta^2 + \beta = 24/25\) and \(\beta^2 + \beta + 1 = 49/25\).
<|det|>text [520, 890, 919, 920]<|/det|>A-2 The minimum is 4, achieved by the square with vertices \((\pm 1, \pm 1)\).
