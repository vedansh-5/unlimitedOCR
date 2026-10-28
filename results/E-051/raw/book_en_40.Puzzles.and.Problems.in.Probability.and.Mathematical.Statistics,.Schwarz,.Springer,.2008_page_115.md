<|det|>header [719, 49, 809, 63]<|/det|>Solutions
<|det|>page_number [846, 49, 881, 63]<|/det|>105
<|det|>text [113, 81, 882, 135]<|/det|>The last two expectations in this expression are known from the basic result about  \( E[U] \)  so that the only really new part concerns the expectation of the product UV. Now, by the definition of U, V
<|det|>equation [297, 148, 700, 169]<|/det|>\[
\mathbf {U V} = \exp (\mathbf {X}) \cdot \exp (\mathbf {Y}) = \exp (\mathbf {X} + \mathbf {Y})
\]
<|det|>text [113, 181, 882, 235]<|/det|>Let the rv \(\mathbf{S} = \mathbf{X} + \mathbf{Y}\). Clearly, \(\mathbf{S}\) is normally distributed, with mean \(\mu_s = \mu_x + \mu_y\) and variance \(\sigma_s^2 = \sigma_x^2 + \sigma_y^2 + 2\rho \sigma_x \sigma_y\). It then follows from the basic result about \(\mathsf{E}[\mathbf{U}]\) that
<|det|>equation [364, 248, 630, 312]<|/det|>\[
\begin{array}{l} \mathsf {E} [ \mathbf {U V} ] = \mathsf {E} [ \exp (\mathbf {S}) ] \\ = \exp \left(\mu_ {s} + \frac {1}{2} \sigma_ {s} ^ {2}\right) \\ \end{array}
\]
<|det|>text [113, 323, 882, 395]<|/det|>Putting together this result — with  \( \mu_{s}, \sigma_{s} \)  expressed in terms of the original parameters as earlier — and the previously known facts about the means and variances of U, V, the correlation coefficient is, after slight simplification, found to be
<|det|>equation [277, 405, 719, 456]<|/det|>\[
\operatorname{corr} (\mathbf {U}, \mathbf {V}) = \frac {\exp (\varrho \sigma_ {x} \sigma_ {y}) - 1}{\sqrt {\left[ \exp (\sigma_ {x} ^ {2}) - 1 \right] \left[ \exp (\sigma_ {y} ^ {2}) - 1 \right]}}
\]
<|det|>text [113, 467, 883, 592]<|/det|>Note that the correlation between \(\mathbf{U}\) and \(\mathbf{V}\) is completely independent of the means of \(\mathbf{X}\) and \(\mathbf{Y}\). As explained earlier, the exponentiation turns the location parameters \(\mu_x, \mu_y\) of \(\mathbf{X}\) and \(\mathbf{Y}\) into scaling factors of \(\mathbf{U}\) and \(\mathbf{V}\). Because variations of the scaling factors generally do not change linear correlations, the result was to be expected. On the other hand, the standard deviations \(\sigma_x, \sigma_y\) of \(\mathbf{X}\) and \(\mathbf{Y}\) turn into powers for \(\mathbf{U}\) and \(\mathbf{V}\), which generally do influence the linear correlation coefficient.
<|det|>text [113, 594, 882, 648]<|/det|>The result about the correlation of \(\mathbf{U}\) and \(\mathbf{V}\) may also be used to verify the properties we already discussed in part c. Note, in particular, that in the equal-variance case \(\sigma_x = \sigma_y = \sigma\) we get
<|det|>equation [360, 662, 637, 702]<|/det|>\[
\operatorname{corr} (\mathbf {U}, \mathbf {V}) = \frac {\exp (\varrho \sigma^ {2}) - 1}{\exp (\sigma^ {2}) - 1}
\]
<|det|>text [113, 712, 882, 784]<|/det|>The correlation of \(\mathbf{U}\) and \(\mathbf{V}\) is shown in Figure 3.25 as a function of the correlation \(\varrho\) of the original rvs \(\mathbf{X}\) and \(\mathbf{Y}\), for three values of \(\sigma\). For \(\varrho = +1\), the two correlations are identical, but for any other value the correlation between \(\mathbf{U}\) and \(\mathbf{V}\) is weaker than that between \(\mathbf{X}\) and \(\mathbf{Y}\).
