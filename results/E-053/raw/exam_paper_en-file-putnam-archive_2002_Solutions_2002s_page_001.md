<|det|>title [197, 63, 812, 101]<|/det|>Solutions to the 63rd William Lowell Putnam Mathematical Competition
Saturday, December 7, 2002
<|det|>text [398, 114, 608, 131]<|/det|>Kiran Kedlaya and Lenny Ng
<|det|>text [90, 163, 491, 239]<|/det|>A-1 By differentiating \( P_{n}(x) / (x^{k} - 1)^{n + 1} \), we find that \( P_{n + 1}(x) = (x^{k} - 1)P_{n}^{\prime}(x) - (n + 1)kx^{k - 1}P_{n}(x) \); substituting \( x = 1 \) yields \( P_{n + 1}(1) = -(n + 1)kPa(1) \). Since \( P_0(1) = 1 \), an easy induction gives \( P_{n}(1) = (-k)^{n}n! \) for all \( n\geq 0 \).
<|det|>text [124, 242, 490, 271]<|/det|>Note: one can also argue by expanding in Taylor series around 1. Namely, we have
<|det|>equation [140, 281, 436, 315]<|/det|>\[
\frac {1}{x ^ {k} - 1} = \frac {1}{k (x - 1) + \cdots} = \frac {1}{k} (x - 1) ^ {- 1} + \dots ,
\]
<|det|>text [125, 324, 147, 335]<|/det|>SO
<|det|>equation [197, 345, 378, 379]<|/det|>\[
\frac {d ^ {n}}{d x ^ {n}} \frac {1}{x ^ {k} - 1} = \frac {(- 1) ^ {n} n !}{k (x - 1) ^ {- n - 1}}
\]
<|det|>text [125, 389, 155, 402]<|/det|>and
<|det|>equation [97, 412, 475, 495]<|/det|>\[
\begin{array}{l} P _ {n} (x) = \left(x ^ {k} - 1\right) ^ {n + 1} \frac {d ^ {n}}{d x ^ {n}} \frac {1}{x ^ {k} - 1} \\ = (k (x - 1) + \dots) ^ {n + 1} \left(\frac {(- 1) ^ {n} n !}{k} (x - 1) ^ {- n - 1} + \dots\right) \\ = (- k) ^ {n} n! + \dots . \\ \end{array}
\]
<|det|>text [90, 512, 491, 600]<|/det|>A-2 Draw a great circle through two of the points. There are two closed hemispheres with this great circle as boundary, and each of the other three points lies in one of them. By the pigeonhole principle, two of those three points lie in the same hemisphere, and that hemisphere thus contains four of the five given points.
<|det|>text [123, 603, 490, 719]<|/det|>Note: by a similar argument, one can prove that among any  \( n+3 \)  points on an n-dimensional sphere, some  \( n+2 \)  of them lie on a closed hemisphere. (One cannot get by with only  \( n+2 \)  points: put them at the vertices of a regular simplex.) Namely, any n of the points lie on a great sphere, which forms the boundary of two hemispheres; of the remaining three points, some two lie in the same hemisphere.
<|det|>text [90, 728, 491, 845]<|/det|>A–3 Note that each of the sets  \( \{1\},\{2\},\ldots,\{n\} \)  has the desired property. Moreover, for each set S with integer average m that does not contain m,  \( S \cup \{m\} \)  also has average m, while for each set T of more than one element with integer average m that contains m,  \( T \setminus \{m\} \)  also has average m. Thus the subsets other than  \( \{1\},\{2\},\ldots,\{n\} \)  can be grouped in pairs, so  \( T_{n}-n \)  is even.
<|det|>text [90, 856, 492, 929]<|/det|>A-4 (partly due to David Savitt) Player 0 wins with optimal play. In fact, we prove that Player 1 cannot prevent Player 0 from creating a row of all zeroes, a column of all zeroes, or a \(2 \times 2\) submatrix of all zeroes. Each of these forces the determinant of the matrix to be zero.
<|det|>text [553, 165, 920, 224]<|/det|>For \(i, j = 1, 2, 3\), let \(A_{ij}\) denote the position in row \(i\) and column \(j\). Without loss of generality, we may assume that Player 1's first move is at \(A_{11}\). Player 0 then plays at \(A_{22}\):
<|det|>equation [682, 235, 754, 283]<|/det|>\[
\left( \begin{array}{c c c} 1 & * & * \\ * & 0 & * \\ * & * & * \end{array} \right)
\]
<|det|>text [553, 292, 920, 337]<|/det|>After Player 1's second move, at least one of \( A_{23} \) and \( A_{32} \) remains vacant. Without loss of generality, assume \( A_{23} \) remains vacant; Player 0 then plays there.
<|det|>text [553, 340, 920, 428]<|/det|>After Player 1's third move, Player 0 wins by playing at \( A_{21} \) if that position is unoccupied. So assume instead that Player 1 has played there. Thus of Player 1's three moves so far, two are at \( A_{11} \) and \( A_{21} \). Hence for \( i \) equal to one of 1 or 3, and for \( j \) equal to one of 2 or 3, the following are both true:
<|det|>text [565, 437, 920, 482]<|/det|>(a) The \(2 \times 2\) submatrix formed by rows 2 and \(i\) and by columns 2 and 3 contains two zeroes and two empty positions.
<|det|>text [565, 486, 919, 514]<|/det|>(b) Column \( j \) contains one zero and two empty positions.
<|det|>text [553, 525, 920, 569]<|/det|>Player 0 next plays at \( A_{ij} \). To prevent a zero column, Player 1 must play in column \( j \), upon which Player 0 completes the \( 2 \times 2 \) submatrix in (a) for the win.
<|det|>text [553, 573, 920, 689]<|/det|>Note: one can also solve this problem directly by making a tree of possible play sequences. This tree can be considerably collapsed using symmetries: the symmetry between rows and columns, the invariance of the outcome under reordering of rows or columns, and the fact that the scenario after a sequence of moves does not depend on the order of the moves (sometimes called “transposition invariance”).
<|det|>text [553, 693, 919, 738]<|/det|>Note (due to Paul Cheng): one can reduce Determinant Tic-Tac-Toe to a variant of ordinary tic-tac-toe. Namely, consider a tic-tac-toe grid labeled as follows:
<|det|>equation [667, 748, 768, 802]<|/det|>\[
\begin{array}{c c c} A _ {1 1} & A _ {2 2} & A _ {3 3} \\ \hline A _ {2 3} & A _ {3 1} & A _ {1 2} \\ \hline A _ {3 2} & A _ {1 3} & A _ {2 1} \end{array}
\]
<|det|>text [553, 813, 920, 915]<|/det|>Then each term in the expansion of the determinant occurs in a row or column of the grid. Suppose Player 1 first plays in the top left. Player 0 wins by playing first in the top row, and second in the left column. Then there are only one row and column left for Player 1 to threaten, and Player 1 cannot already threaten both on the third move, so Player 0 has time to block both.
