<|det|>title [238, 33, 717, 95]<|/det|>What is a digital image?
<|det|>title [25, 144, 417, 185]<|/det|>■ Mathematical definition:
<|det|>text [71, 197, 948, 280]<|/det|>■ A 2D (grayscale) digital image is a 2D function defined on a 2D domain (usually rectangular domain):
<|det|>equation [380, 298, 551, 351]<|/det|>\[
f: \Omega \to \mathbb {R}
\]
<|det|>text [72, 380, 727, 422]<|/det|>■  \( f(x,y) \)  is called the brightness/intensity/grey level;
<|det|>text [72, 432, 629, 470]<|/det|>■ (x,y) is the spatial coordinates of the image.
<|det|>text [72, 479, 578, 517]<|/det|>Thus, a 2D digital image looks like this:
<|det|>equation [230, 532, 731, 729]<|/det|>\[
f (x, y) = \left[ \begin{array}{c c c c} f (1, 1) & f (1, 2) & \ldots & f (1, N) \\ f (2, 1) & f (2, 2) & \ldots & f (2, N) \\ \vdots & \vdots & & \vdots \\ f (N, 1) & f (N, 2) & \ldots & f (N, N) \end{array} \right]
\]
<|det|>text [72, 767, 813, 806]<|/det|>■ Each element in the matrix is called pixel (picture element);
<|det|>text [72, 812, 705, 854]<|/det|>■ Usually,  \( 0 \leq f(x, y) \leq G - 1 \)  and  \( (N = 2^{n}, G = 2^{m}) \)
<|det|>text [110, 900, 893, 938]<|/det|>IMAGE PROCESSING IS RELATED TO LINEAR ALGEBRA!!
