<|det|>page_number [143, 50, 172, 62]<|/det|>110
<|det|>header [439, 50, 611, 64]<|/det|>Chapter 2 Vector Spaces
<|det|>text [138, 84, 909, 183]<|/det|>You must notice that the word “dimensional” is used in two different ways. We speak about a four-dimensional vector, meaning a vector in  \( R^{4} \) . Now we have defined a four-dimensional subspace; an example is the set of vectors in  \( R^{6} \)  whose first and last components are zero. The members of this four-dimensional subspace are six-dimensional vectors like  \( (0,5,1,3,4,0) \) .
<|det|>text [138, 185, 909, 263]<|/det|>One final note about the language of linear algebra. We never use the terms “basis of a matrix” or “rank of a space” or “dimension of a basis.” These phrases have no meaning. It is the dimension of the column space that equals the rank of the matrix, as we prove in the coming section.
<|det|>title [140, 309, 310, 327]<|/det|>Problem Set 2.3
<|det|>title [139, 346, 789, 365]<|/det|>Problems 1–10 are about linear independence and linear dependence.
<|det|>text [140, 376, 770, 394]<|/det|>1. Show that \( v_{1}, v_{2}, v_{3} \) are independent but \( v_{1}, v_{2}, v_{3}, v_{4} \) are dependent:
<|det|>equation [293, 402, 784, 472]<|/det|>\[
v _ {1} = \left[ \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right] \quad v _ {2} = \left[ \begin{array}{c} 1 \\ 1 \\ 0 \end{array} \right] \quad v _ {3} = \left[ \begin{array}{c} 1 \\ 1 \\ 1 \end{array} \right] \quad v _ {4} = \left[ \begin{array}{c} 2 \\ 3 \\ 4 \end{array} \right].
\]
<|det|>text [171, 481, 785, 500]<|/det|>Solve  \( c_{1}v_{1} + \cdots + c_{4}v_{4} = 0 \)  or Ac = 0. The v's go in the columns of A.
<|det|>text [139, 511, 730, 530]<|/det|>2. Find the largest possible number of independent vectors among
<|det|>equation [170, 539, 909, 628]<|/det|>\[
v _ {1} = \left[ \begin{array}{c} 1 \\ - 1 \\ 0 \\ 0 \end{array} \right] \quad v _ {2} = \left[ \begin{array}{c} 1 \\ 0 \\ - 1 \\ 0 \end{array} \right] \quad v _ {3} = \left[ \begin{array}{c} 1 \\ 0 \\ 0 \\ - 1 \end{array} \right] \quad v _ {4} = \left[ \begin{array}{c} 0 \\ 1 \\ - 1 \\ 0 \end{array} \right] \quad v _ {5} = \left[ \begin{array}{c} 0 \\ 1 \\ 0 \\ - 1 \end{array} \right] \quad v _ {6} = \left[ \begin{array}{c} 0 \\ 0 \\ 1 \\ - 1 \end{array} \right].
\]
<|det|>text [171, 636, 670, 656]<|/det|>This number is the ____ of the space spanned by the v's.
<|det|>text [139, 665, 860, 684]<|/det|>3. Prove that if \( a = 0 \), \( d = 0 \), or \( f = 0 \) (3 cases), the columns of \( U \) are dependent:
<|det|>equation [462, 693, 619, 766]<|/det|>\[
U = \left[ \begin{array}{c c c} a & b & c \\ 0 & d & e \\ 0 & 0 & f \end{array} \right].
\]
<|det|>text [139, 776, 908, 814]<|/det|>4. If \( a, d, f \) in Problem 3 are all nonzero, show that the only solution to \( Ux = 0 \) is \( x = 0 \). Then \( U \) has independent columns.
<|det|>text [140, 826, 555, 845]<|/det|>5. Decide the dependence or independence of
<|det|>text [172, 855, 571, 874]<|/det|>(a) the vectors  \( (1,3,2) \) ,  \( (2,1,3) \) , and  \( (3.2,1) \) .
<|det|>text [172, 880, 625, 900]<|/det|>(b) the vectors  \( (1,-3,2) \) ,  \( (2,1,-3) \) , and  \( (-3,2,1) \) .
