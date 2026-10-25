<|det|>header [293, 44, 699, 56]<|/det|>Y. Sun, P.S.P. Tse/Journal of Computational Physics 230 (2011) 2076–2094
<|det|>page_number [894, 44, 927, 55]<|/det|>2089
<|det|>image [128, 71, 486, 330]<|/det|>
<|det|>image_caption [315, 336, 341, 351]<|/det|>(a)
<|det|>image [504, 72, 862, 330]<|/det|>
<|det|>image_caption [693, 336, 720, 351]<|/det|>(b)
<|det|>image [128, 357, 486, 617]<|/det|>
<|det|>image_caption [315, 623, 340, 638]<|/det|>(c)
<|det|>image [504, 359, 861, 617]<|/det|>
<|det|>image_caption [687, 623, 714, 638]<|/det|>(d)
<|det|>image_caption [62, 648, 928, 673]<|/det|>Fig. 4. The dispersion contours with stepsizes \(\Delta t = 0.01\), \(\Delta = 0.1\) for Maxwell's equations (46) from (a) exact dispersion; (b) boxscheme; (c) symplectic method and (d) Yee's method. The constant contour values are \(\omega \in [2,4,6,\dots,24]\).
<|det|>equation [107, 688, 926, 721]<|/det|>\[
\varphi = \tan^ {- 1} \left(\frac {\left(\nu_ {g}\right) _ {y}}{\left(\nu_ {g}\right) _ {x}}\right), \quad \left| \nu_ {g} \right| = \sqrt {\left(\nu_ {g}\right) _ {x} ^ {2} + \left(\nu_ {g}\right) _ {y} ^ {2}}. \tag {48}
\]
<|det|>text [62, 727, 928, 755]<|/det|>Substituting into (48) the vectors \(\kappa\) and \(\nu_{g}\) in polar coordinates (44), and let \(a = |\kappa|\Delta\), this yields the propagation angle \(\varphi\) and the propagation speed \(|v_{g}|\) in terms of \(a\) and \(\theta\).
<|det|>text [84, 756, 414, 770]<|/det|>For example,  \( \varphi \)  for the boxscheme is given by
<|det|>equation [107, 775, 420, 813]<|/det|>\[
\varphi = \tan^ {- 1} \left(\frac {\sin \left(\frac {1}{2} \sin (\theta) a\right) \cos^ {3} \left(\frac {1}{2} \cos (\theta) a\right)}{\cos^ {3} \left(\frac {1}{2} \sin (\theta) a\right) \sin \left(\frac {1}{2} \cos (\theta) a\right)}\right).
\]
<|det|>text [63, 818, 592, 833]<|/det|>Taking the Taylor expansion of this expression with respect to \( a = 0 \) yields,
<|det|>equation [108, 839, 926, 868]<|/det|>\[
\varphi \approx \theta - \frac {1}{1 2} \sin (4 \theta) a ^ {2} + O (a ^ {3}). \tag {49}
\]
<|det|>text [63, 872, 436, 888]<|/det|>Similarly, the Taylor expansion of \( |v_g| \) at \( a = 0 \) yields,
<|det|>equation [107, 892, 926, 925]<|/det|>\[
\left| v _ {g} \right| \approx 1 + \left(\frac {1}{1 6} \cos (4 \theta) - \frac {r ^ {2}}{4} + \frac {3}{1 6}\right) a ^ {2} + O \left(a ^ {4}\right), \tag {50}
\]
