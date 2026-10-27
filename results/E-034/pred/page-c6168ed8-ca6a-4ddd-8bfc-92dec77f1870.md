\[
\sigma_ {*} (\mathbf {E}) \leq \sup _ {\| \mathbf {w} \| = 1} \| \mathbb {E} [ \mathbf {E w w} ^ {\top} \mathbf {E} ^ {\top} ] \| ^ {\frac {1}{2}} \leq \max _ {i \in [ N ]} \sup _ {\| \mathbf {w} \| = 1} \| \mathbb {E} [ \mathbf {E} _ {i,:} \mathbf {w w} ^ {\top} \mathbf {E} _ {i,:} ^ {\top} ] \| ^ {\frac {1}{2}} \leq \widetilde {\sigma}, \tag {S.13}
\]

\[
R (\mathbf {E}) = \left\| \max _ {i \in [ N ], l \in [ L ]} \| \mathbf {E} _ {i, S _ {l}} \| \right\| _ {\infty} \leq \sqrt {M} B.
\]

Then the first inequality in Lemma S.5 follows by plugging these conditions into Proposition 1 with \( t = c\log d \) with a sufficiently large constant \( c \).

Similarly, for the second and third inequalities we use

\[
\sigma (\mathbf {E} _ {i,:}) = \max \{\| \mathbb {E} [ \mathbf {E} _ {i,:} ^ {\top} \mathbf {E} _ {i,:} ] \| ^ {\frac {1}{2}}, \| \mathbb {E} [ \mathbf {E} _ {i,:} \mathbf {E} _ {i,:} ^ {\top} ] \| ^ {\frac {1}{2}} \} \leq \max \{\sigma \sqrt {J}, \widetilde {\sigma} \} = \sigma \sqrt {J},
\]

\[
v (\mathbf {E} _ {i,:}) = \| \mathrm{Cov} (\mathbf {E} _ {i,:}) \| ^ {\frac {1}{2}} \leq \widetilde {\sigma}, \quad \sigma_ {*} (\mathbf {E} _ {i,:}) \leq \widetilde {\sigma}, \quad R (\mathbf {E} _ {i,:}) \leq \sqrt {M} B,
\]

and

\[
\sigma (\mathbf {E} _ {:, j}) = \max \{\| \mathbb {E} [ \mathbf {E} _ {:, j} ^ {\top} \mathbf {E} _ {:, j} ] \| ^ {\frac {1}{2}}, \| \mathbb {E} [ \mathbf {E} _ {:, j} \mathbf {E} _ {:, j} ^ {\top} ] \| ^ {\frac {1}{2}} \} \leq \sigma \sqrt {N},
\]

\[
v (\mathbf {E} _ {:, j}) \leq \sigma , \quad \sigma_ {*} (\mathbf {E} _ {:, j}) \leq \sigma , \quad R (\mathbf {E} _ {:, j}) \leq B.
\]

Furthermore, for the fourth and fifth inequalities,

\[
\sigma \left(\mathbf {E} \mathbf {V} ^ {*}\right) = \max \left\{\| \mathbb {E} \left[ \mathbf {E} \mathbf {V} ^ {*} \mathbf {V} ^ {* \top} \mathbf {E} ^ {\top} \right] \| ^ {\frac {1}{2}}, \| \mathbb {E} \left[ \mathbf {V} ^ {* \top} \mathbf {E} ^ {\top} \mathbf {E} \mathbf {V} ^ {*} \right] \| ^ {\frac {1}{2}} \right\} \leq \widetilde {\sigma} \sqrt {N},
\]

\[
v (\mathbf {E V} ^ {*}) \leq \widetilde {\sigma}, \quad \sigma_ {*} (\mathbf {E V} ^ {*}) \leq \sigma_ {*} (\mathbf {E}) \stackrel {(S. 1 3)} {\leq} \widetilde {\sigma},
\]

and with \(MK \lesssim ML \asymp J\) we have

\[
\| \mathbb {E} [ \mathbf {E} ^ {\top} \mathbf {U} ^ {*} \mathbf {U} ^ {* \top} \mathbf {E} ] \| = \max _ {l \in [ L ]} \| \mathbb {E} [ \mathbf {E} _ {:, S _ {l}} ^ {\top} \mathbf {U} ^ {*} \mathbf {U} ^ {* \top} \mathbf {E} _ {:, S _ {l}} ] \| \leq \max _ {l \in [ L ]} \mathbb {E} [ \| \mathbf {E} _ {:, S _ {l}} ^ {\top} \mathbf {U} ^ {*} \mathbf {U} ^ {* \ top} \mathbf {E} _ {:, S _ {l}} \|
\]

\[
= M \max _ {j \in [ J ]} \mathbb {E} [ \mathbf {E} _ {:, j} ^ {\top} \mathbf {U} ^ {*} \mathbf {U} ^ {* \top} \mathbf {E} _ {:, j} ] \leq M \sigma^ {2} \| \mathbf {U} ^ {*} \| _ {F} ^ {2} = M K \sigma^ {2},
\]

\[
\| \mathbb {E} [ \mathbf {U} ^ {* \top} \mathbf {E E} ^ {\top} \mathbf {U} ^ {*} ] \| \leq \| \mathbb {E} [ \mathbf {E E} ^ {\top} ] \| \leq \sigma^ {2} J,
\]

\[
\sigma (\mathbf {E} ^ {\top} \mathbf {U} ^ {*}) \leq \sigma \sqrt {J} + \sigma \sqrt {M K},
\]

\[
R (\mathbf {E} ^ {\top} \mathbf {U} ^ {*}) = \left\| \max _ {i \in [ N ], l \in [ L ]} \| \mathbf {E} _ {i, S _ {l}} ^ {\top} \mathbf {U} _ {i,:} ^ {*} \| \right\| _ {\infty} \leq \sqrt {M} B \| \mathbf {U} ^ {*} \| _ {2, \infty},
\]

\[
\upsilon \left(\mathbf {E} ^ {\top} \mathbf {U} ^ {*}\right) \leq \max _ {l \in [ L ]} \left\| \mathbb {E} \left[ \mathbf {E} _ {:, S _ {l}} ^ {\top} \mathbf {U} ^ {*} \mathbf {U} ^ {* \top} \mathbf {E} _ {:, S _ {l}} \right] \right\| ^ {\frac {1}{2}} \leq \sqrt {M K} \sigma ,
\]

\[
\sigma_ {*} \left(\mathbf {U} ^ {* \top} \mathbf {E}\right) ^ {2} \leq \sigma_ {*} (\mathbf {E}) ^ {2} \stackrel {\text {by (S.13)}} {\leq} \widetilde {\sigma} ^ {2} \leq M \sigma^ {2}.
\]

43
