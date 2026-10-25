<|det|>page_number [142, 50, 155, 62]<|/det|>8
<|det|>header [368, 49, 681, 64]<|/det|>Chapter 1 Matrices and Gaussian Elimination
<|det|>text [138, 84, 912, 204]<|/det|>Our true goal is to look beyond two or three dimensions into \( n \) dimensions. With \( n \) equations in \( n \) unknowns, there are \( n \) planes in the row picture. There are \( n \) vectors in the column picture, plus a vector \( b \) on the right side. The equations ask for a linear combination of the \( n \) columns that equals \( b \). For certain equations that will be impossible. Paradoxically, the way to understand the good case is to study the bad one. Therefore we look at the geometry exactly when it breaks down, in the singular case.
<|det|>text [157, 230, 473, 250]<|/det|>Row picture: Intersection of planes
<|det|>text [516, 230, 892, 250]<|/det|>Column picture: Combination of columns
<|det|>title [140, 288, 338, 308]<|/det|>The Singular Case
<|det|>text [138, 326, 911, 445]<|/det|>Suppose we are again in three dimensions, and the three planes in the row picture do not intersect. What can go wrong? One possibility is that two planes may be parallel. The equations \( 2u + v + w = 5 \) and \( 4u + 2v + 2w = 11 \) are inconsistent—and parallel planes give no solution (Figure 1.5a shows an end view). In two dimensions, parallel lines are the only possibility for breakdown. But three planes in three dimensions can be in trouble without being parallel.
<|det|>image [177, 454, 365, 594]<|/det|>
<|det|>image_caption [255, 590, 280, 605]<|/det|>(a)
<|det|>image [355, 454, 501, 580]<|/det|>
<|det|>image_caption [385, 586, 501, 599]<|/det|>no intersection
<|det|>image_caption [431, 601, 456, 616]<|/det|>(b)
<|det|>image [539, 454, 685, 580]<|/det|>
<|det|>image_caption [545, 586, 691, 599]<|/det|>line of intersection
<|det|>image_caption [607, 601, 631, 616]<|/det|>(c)
<|det|>image [704, 454, 848, 580]<|/det|>
<|det|>image_caption [724, 584, 864, 599]<|/det|>all planes parallel
<|det|>image_caption [782, 601, 807, 616]<|/det|>(d)
<|det|>image_caption [223, 633, 825, 649]<|/det|>Figure 1.5: Singular cases: no solution for (a), (b), or (d), an infinity of solutions for (c).
<|det|>text [138, 679, 911, 757]<|/det|>The most common difficulty is shown in Figure 1.5b. From the end view the planes form a triangle. Every pair of planes intersects in a line, and those lines are parallel. The third plane is not parallel to the other planes, but it is parallel to their line of intersection. This corresponds to a singular system with \( b = (2,5,6) \):
<|det|>text_block [241, 772, 620, 790]<|/det|>No solution, as in Figure 1.5b
<|det|>equation_isolated [620, 772, 909, 812]<|/det|>\[
\begin{array}{c c c c c c} u & + & v & + & w & = & 2 \\ 2 u & & + & 3 w & = & 5 \\ 3 u & + & v & + & 4 w & = & 6. \end{array} \tag {3}
\]
<|det|>text [139, 845, 911, 903]<|/det|>The first two left sides add up to the third. On the right side that fails: \(2 + 5 \neq 6\). Equation 1 plus equation 2 minus equation 3 is the impossible statement \(0 = 1\). Thus the equations are inconsistent, as Gaussian elimination will systematically discover.
