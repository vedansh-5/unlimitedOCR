<|det|>equation [214, 96, 882, 131]<|/det|>\[
\sigma_ {*} (\mathbf {E}) \leq \sup _ {\| \mathbf {w} \| = 1} \| \mathbb {E} [ \mathbf {E w w} ^ {\top} \mathbf {E} ^ {\top} ] \| ^ {\frac {1}{2}} \leq \max _ {i \in [ N ]} \sup _ {\| \mathbf {w} \| = 1} \| \mathbb {E} [ \mathbf {E} _ {i,:} \mathbf {w w} ^ {\top} \mathbf {E} _ {i,:} ^ {\top} ] \| ^ {\frac {1}{2}} \leq \widetilde {\sigma}, \tag {S.13}
\]
<|det|>equation [216, 133, 535, 174]<|/det|>\[
R (\mathbf {E}) = \left\| \max _ {i \in [ N ], l \in [ L ]} \| \mathbf {E} _ {i, S _ {l}} \| \right\| _ {\infty} \leq \sqrt {M} B.
\]
<|det|>text [112, 186, 884, 236]<|/det|>Then the first inequality in Lemma S.5 follows by plugging these conditions into Proposition 1 with \( t = c\log d \) with a sufficiently large constant \( c \).
<|det|>text [142, 248, 599, 265]<|/det|>Similarly, for the second and third inequalities we use
<|det|>equation [212, 288, 789, 311]<|/det|>\[
\sigma (\mathbf {E} _ {i,:}) = \max \{\| \mathbb {E} [ \mathbf {E} _ {i,:} ^ {\top} \mathbf {E} _ {i,:} ] \| ^ {\frac {1}{2}}, \| \mathbb {E} [ \mathbf {E} _ {i,:} \mathbf {E} _ {i,:} ^ {\top} ] \| ^ {\frac {1}{2}} \} \leq \max \{\sigma \sqrt {J}, \widetilde {\sigma} \} = \sigma \sqrt {J},
\]
<|det|>equation [232, 323, 789, 346]<|/det|>\[
v (\mathbf {E} _ {i,:}) = \| \mathrm{Cov} (\mathbf {E} _ {i,:}) \| ^ {\frac {1}{2}} \leq \widetilde {\sigma}, \quad \sigma_ {*} (\mathbf {E} _ {i,:}) \leq \widetilde {\sigma}, \quad R (\mathbf {E} _ {i,:}) \leq \sqrt {M} B,
\]
<|det|>text [113, 370, 151, 385]<|/det|>and
<|det|>equation [275, 409, 724, 433]<|/det|>\[
\sigma (\mathbf {E} _ {:, j}) = \max \{\| \mathbb {E} [ \mathbf {E} _ {:, j} ^ {\top} \mathbf {E} _ {:, j} ] \| ^ {\frac {1}{2}}, \| \mathbb {E} [ \mathbf {E} _ {:, j} \mathbf {E} _ {:, j} ^ {\top} ] \| ^ {\frac {1}{2}} \} \leq \sigma \sqrt {N},
\]
<|det|>equation [332, 446, 724, 466]<|/det|>\[
v (\mathbf {E} _ {:, j}) \leq \sigma , \quad \sigma_ {*} (\mathbf {E} _ {:, j}) \leq \sigma , \quad R (\mathbf {E} _ {:, j}) \leq B.
\]
<|det|>text [142, 490, 562, 508]<|/det|>Furthermore, for the fourth and fifth inequalities,
<|det|>equation [223, 527, 776, 559]<|/det|>\[
\sigma \left(\mathbf {E} \mathbf {V} ^ {*}\right) = \max \left\{\| \mathbb {E} \left[ \mathbf {E} \mathbf {V} ^ {*} \mathbf {V} ^ {* \top} \mathbf {E} ^ {\top} \right] \| ^ {\frac {1}{2}}, \| \mathbb {E} \left[ \mathbf {V} ^ {* \top} \mathbf {E} ^ {\top} \mathbf {E} \mathbf {V} ^ {*} \right] \| ^ {\frac {1}{2}} \right\} \leq \widetilde {\sigma} \sqrt {N},
\]
<|det|>equation [336, 562, 700, 589]<|/det|>\[
v (\mathbf {E V} ^ {*}) \leq \widetilde {\sigma}, \quad \sigma_ {*} (\mathbf {E V} ^ {*}) \leq \sigma_ {*} (\mathbf {E}) \stackrel {(S. 1 3)} {\leq} \widetilde {\sigma},
\]
<|det|>text [113, 613, 411, 631]<|/det|>and with \(MK \lesssim ML \asymp J\) we have
<|det|>equation [193, 655, 807, 688]<|/det|>\[
\| \mathbb {E} [ \mathbf {E} ^ {\top} \mathbf {U} ^ {*} \mathbf {U} ^ {* \top} \mathbf {E} ] \| = \max _ {l \in [ L ]} \| \mathbb {E} [ \mathbf {E} _ {:, S _ {l}} ^ {\top} \mathbf {U} ^ {*} \mathbf {U} ^ {* \top} \mathbf {E} _ {:, S _ {l}} ] \| \leq \max _ {l \in [ L ]} \mathbb {E} [ \| \mathbf {E} _ {:, S _ {l}} ^ {\top} \mathbf {U} ^ {*} \mathbf {U} ^ {* \ top} \mathbf {E} _ {:, S _ {l}} \|
\]
<|det|>equation [350, 696, 787, 725]<|/det|>\[
= M \max _ {j \in [ J ]} \mathbb {E} [ \mathbf {E} _ {:, j} ^ {\top} \mathbf {U} ^ {*} \mathbf {U} ^ {* \top} \mathbf {E} _ {:, j} ] \leq M \sigma^ {2} \| \mathbf {U} ^ {*} \| _ {F} ^ {2} = M K \sigma^ {2},
\]
<|det|>equation [325, 738, 638, 758]<|/det|>\[
\| \mathbb {E} [ \mathbf {U} ^ {* \top} \mathbf {E E} ^ {\top} \mathbf {U} ^ {*} ] \| \leq \| \mathbb {E} [ \mathbf {E E} ^ {\top} ] \| \leq \sigma^ {2} J,
\]
<|det|>equation [342, 772, 582, 791]<|/det|>\[
\sigma (\mathbf {E} ^ {\top} \mathbf {U} ^ {*}) \leq \sigma \sqrt {J} + \sigma \sqrt {M K},
\]
<|det|>equation [277, 801, 730, 840]<|/det|>\[
R (\mathbf {E} ^ {\top} \mathbf {U} ^ {*}) = \left\| \max _ {i \in [ N ], l \in [ L ]} \| \mathbf {E} _ {i, S _ {l}} ^ {\top} \mathbf {U} _ {i,:} ^ {*} \| \right\| _ {\infty} \leq \sqrt {M} B \| \mathbf {U} ^ {*} \| _ {2, \infty},
\]
<|det|>equation [248, 846, 673, 877]<|/det|>\[
\upsilon \left(\mathbf {E} ^ {\top} \mathbf {U} ^ {*}\right) \leq \max _ {l \in [ L ]} \left\| \mathbb {E} \left[ \mathbf {E} _ {:, S _ {l}} ^ {\top} \mathbf {U} ^ {*} \mathbf {U} ^ {* \top} \mathbf {E} _ {:, S _ {l}} \right] \right\| ^ {\frac {1}{2}} \leq \sqrt {M K} \sigma ,
\]
<|det|>equation [247, 884, 577, 911]<|/det|>\[
\sigma_ {*} \left(\mathbf {U} ^ {* \top} \mathbf {E}\right) ^ {2} \leq \sigma_ {*} (\mathbf {E}) ^ {2} \stackrel {\text {by (S.13)}} {\leq} \widetilde {\sigma} ^ {2} \leq M \sigma^ {2}.
\]
<|det|>page_number [489, 935, 510, 948]<|/det|>43
