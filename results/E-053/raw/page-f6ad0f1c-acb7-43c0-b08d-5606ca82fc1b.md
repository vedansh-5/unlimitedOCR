<|det|>header [354, 63, 644, 75]<|/det|>FOKKER-PLANCK-ALIGNMENT EQUATIONS
<|det|>page_number [935, 64, 950, 74]<|/det|>19
<|det|>text [132, 89, 570, 113]<|/det|>We now test (80) against \( G' \left( \frac{(\theta f)_{\varepsilon_1}}{\theta + \varepsilon_2} \right) \), and integrate in time:
<|det|>equation [136, 124, 907, 274]<|/det|>\[
\begin{array}{l} \int_ {\Omega \times \mathbb {R} ^ {n} \times \{t \}} G \left(\frac {(\theta f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}}\right) \varphi \mathrm{d} v \mathrm{d} x - \int_ {\Omega \times \mathbb {R} ^ {n} \times \{0 \}} G \left(\frac {(\theta f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}}\right) \varphi \mathrm{du} \mathrm{dx} - \int_ {0} ^ {t} \int_ {\Omega \times \mathbb {R} ^ {n} \times \{t \}} G \left(\frac {(\theta f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}}\right) \partial_ {t} \varphi \mathrm{du} \mathrm{dx} \mathrm{ds} \\ = - \int_ {0} ^ {t} \int_ {\Omega \times \mathbb {R} ^ {n}} \frac {(\theta v \cdot \nabla_ {x} f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}} G ^ {\prime} \left(\frac {(\theta f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}}\right) \varphi \mathrm{d} v \mathrm{d} x \mathrm{d} s + \int_ {0} ^ {t} \int_ {\Omega \times \mathbb {R} ^ {n}} \frac {(\theta s _ {\rho} \Delta_ {v} f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}} G ^ {\prime} \left(\frac {(\theta f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}}\right) \varphi \mathrm{d} v \mathrm{d} x \mathrm{d} s \\ + \int_ {0} ^ {t} \int_ {\Omega \times \mathbb {R} ^ {n}} \frac {\nabla_ {v} \cdot (\theta s _ {\rho} v f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}} G ^ {\prime} \left(\frac {(\theta f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}}\right) \varphi \mathrm{d} v \mathrm{d} x \mathrm{d} s - \int_ {0} ^ {t} \int_ {\Omega \times \mathbb {R} ^ {n}} \frac {\nabla_ {v} \cdot (\theta \mathrm{w} _ {\rho} f) _ {\varepsilon_ {1}} ^ {\prime}}{\theta + \varepsilon_ {2}} G ^ {\prime} \left(\frac {(\theta f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}}\right) \varphi \mathrm{d} v \mathrm{d} x \mathrm{d} s \\ + \int_ {0} ^ {t} \int_ {\Omega \times \mathbb {R} ^ {n}} \left[ \frac {(f \partial_ {t} \theta) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}} - \frac {(\theta f) _ {\varepsilon_ {1}} \partial_ {t} \theta}{[ \theta + \varepsilon_ {2} ] ^ {2}} \right] G ^ {\prime \prime} \left(\frac {(\theta f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}}\right) \varphi \mathrm{d} v \mathrm{d} x \mathrm{d} s := - I + I I I + I I I - I V + V. \\ \end{array}
\]
<|det|>text [132, 282, 566, 297]<|/det|>Let us note that \(\theta\) satisfies the mollified continuity equation
<|det|>equation [423, 309, 573, 326]<|/det|>\[
\partial_ {t} \theta = - (u \rho) * \nabla \chi_ {r _ {0}},
\]
<|det|>text [113, 337, 170, 351]<|/det|>and so,
<|det|>equation [116, 363, 578, 382]<|/det|>\[
\| \partial_ {t} \theta \| _ {\infty} \lesssim \| u \| _ {L _ {\rho} ^ {2}} \lesssim C. \tag {81}
\]
<|det|>text [132, 393, 706, 407]<|/det|>In what follows we will be taking consecutive limits as \(\varepsilon_{1}\rightarrow 0\) and then \(\varepsilon_{2}\rightarrow 0\).
<|det|>text [112, 408, 884, 440]<|/det|>The left hand side converges to its natural limit since \( G \) is smooth and \( \frac{(\theta f)_{\varepsilon_1}}{\theta + \varepsilon_2} \to \frac{\theta f}{\theta + \varepsilon_2} \to f \) pointwise almost everywhere. So, we obtain
<|det|>equation [197, 451, 799, 490]<|/det|>\[
\int_ {\Omega \times \mathbb {R} ^ {n} \times \{t \}} G (f) \varphi \mathrm{d} v \mathrm{d} x - \int_ {\Omega \times \mathbb {R} ^ {n} \times \{0 \}} G (f) \varphi \mathrm{d} v \mathrm{d} x - \int_ {0} ^ {t} \int_ {\Omega \times \mathbb {R} ^ {n} \times \{t \}} G (f) \partial_ {t} \varphi \mathrm{d} v \mathrm{d} x \mathrm{d} s.
\]
<|det|>text [113, 510, 569, 526]<|/det|>LIMIT OF I. Let us go back to I. Integrating by parts we have
<|det|>equation [128, 539, 868, 612]<|/det|>\[
\begin{array}{l} I = - \int_ {0} ^ {t} \int_ {\Omega \times \mathbb {R} ^ {n}} \frac {(f v \cdot \nabla \theta) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}} G ^ {\prime} \left(\frac {(\theta f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}}\right) \varphi \mathrm{d} v \mathrm{d} x \mathrm{d} s \\ + \int_ {0} ^ {t} \int_ {\Omega \times \mathbb {R} ^ {n}} \frac {(f v \theta) * \nabla_ {x} \chi_ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}} G ^ {\prime} \left(\frac {(\theta f) _ {\varepsilon_ {1}}}{\theta + \varepsilon_ {2}}\right) \varphi \mathrm{d} v \mathrm{d} x \mathrm{d} s := I _ {1} + I _ {2}. \\ \end{array}
\]
<|det|>text [112, 624, 882, 661]<|/det|>For the limit of \( I_1 \), we have \( fv \cdot \nabla \theta \in L^1 \), so, \( (fv \cdot \nabla \theta)_{\varepsilon_1} \to fv \cdot \nabla \theta \) in \( L^1 \), while \( G' \left( \frac{(\theta f)_{\varepsilon_1}}{\theta + \varepsilon_2} \right) \to G' \left( \frac{\theta f}{\theta + \varepsilon_2} \right) \) a.e. and is uniformly bounded. Consequently, by dominated convergence,
<|det|>equation [115, 671, 677, 706]<|/det|>\[
I _ {1} \rightarrow - \int_ {0} ^ {t} \int_ {\Omega \times \mathbb {R} ^ {n}} \frac {f v \cdot \nabla \theta}{\theta + \varepsilon_ {2}} G ^ {\prime} \left(\frac {\theta f}{\theta + \varepsilon_ {2}}\right) \varphi \mathrm{d} v \mathrm{d} x \mathrm{d} s. \tag {82}
\]
<|det|>text [113, 715, 526, 730]<|/det|>We will leave it at that for now, and turn to  \( I_{2} \) . Observe
<|det|>equation [196, 739, 797, 810]<|/det|>\[
\begin{array}{l} (f v \theta) * \nabla_ {x} \chi_ {\varepsilon_ {1}} = \int_ {\Omega \times \mathbb {R} ^ {n}} f (y, w) w \theta (y) \nabla_ {x} \chi_ {\varepsilon_ {1}} (x - y, v - w) d w d y \\ = \int_ {\Omega \times \mathbb {R} ^ {n}} f (y, w) (w - v) \theta (y) \nabla_ {x} \chi_ {\varepsilon_ {1}} (x - y, v - w) d w d y + v \cdot \nabla_ {x} (f \theta) _ {\varepsilon_ {1}} \\ \end{array}
\]
<|det|>text [113, 819, 536, 835]<|/det|>using that \( w\nabla_x\chi_{\varepsilon_1}(\cdot ,w) \) is odd in \( w \), we can insert \( f(y,v) \),
<|det|>equation [114, 845, 864, 916]<|/det|>\[
\begin{array}{l} (f v \theta) * \nabla_ {x} \chi_ {\varepsilon_ {1}} = \int_ {\Omega \times \mathbb {R} ^ {n}} [ f (y, w) - f (y, v) ] (w - v) \theta (y) \nabla_ {x} \chi_ {\varepsilon_ {1}} (x - y, v - w) d w d y + v \cdot \nabla_ {x} (f \theta) _ {\varepsilon_ {1}} \tag {83} \\ = \int_ {0} ^ {1} \int_ {\Omega \times \mathbb {R} ^ {n}} \theta (x - y) \nabla_ {v} f (x - y, v + \theta w) w \otimes w \nabla_ {x} \chi_ {\varepsilon_ {1}} (y, w) d w d \theta + v \cdot \nabla_ {x} (\theta f) _ {\varepsilon_ {1}}. \\ \end{array}
\]
