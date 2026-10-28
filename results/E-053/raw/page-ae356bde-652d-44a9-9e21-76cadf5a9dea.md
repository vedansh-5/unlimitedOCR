<|det|>page_number [900, 35, 920, 47]<|/det|>27
<|det|>text [84, 66, 722, 82]<|/det|>This model in [35] is equivalent to our construction when the sign is flipped. Notice that
<|det|>equation [400, 92, 604, 108]<|/det|>\[
U _ {i} = Z _ {8 i + 1} Z _ {8 i + 3} Z _ {8 i + 5} Z _ {8 i + 7}
\]
<|det|>text [83, 118, 327, 133]<|/det|>is a symmetric operator, we have
<|det|>equation [160, 142, 846, 188]<|/det|>\[
\left(- \sum_ {I} \tilde {P} _ {I, I + 1}\right) \prod_ {i = 1} ^ {[ L / 8 ]} U _ {i} = \left\{ \begin{array}{l l} \prod_ {i = 1} ^ {[ L / 8 ]} U _ {i} \left(- \sum_ {I} P _ {I, I + 1}\right) & L \equiv 0 \mod 8 \\ \prod_ {i = 1} ^ {[ L / 8 ]} U _ {i} \left(- \sum_ {I} P _ {\bar {I}, I + 1} - \bar {P} _ {L / 4 - 1, L / 4} - \bar {P} _ {L / 4, L / 4 + 1}\right) & L \equiv 4 \mod 8 \end{array} \right.
\]
<|det|>text [84, 194, 132, 206]<|/det|>where
<|det|>equation [289, 215, 717, 245]<|/det|>\[
P _ {I, I + 1} = \frac {1}{4} (1 + Z _ {4 I - 3} X _ {4 I - 1} Z _ {4 I + 1}) (1 + Z _ {4 I - 1} X _ {4 I + 1} Z _ {4 I + 3}),
\]
<|det|>equation [289, 246, 717, 275]<|/det|>\[
\bar {P} _ {L / 4 - 1, L / 4} = \frac {1}{4} (1 + Z _ {L - 7} X _ {L - 5} Z _ {L - 3}) (1 - Z _ {L - 5} X _ {L - 3} Z _ {L - 1}),
\]
<|det|>equation [325, 277, 672, 306]<|/det|>\[
\bar {P} _ {L / 4, 1} = \frac {1}{4} (1 - Z _ {L - 3} X _ {L - 1} Z _ {1}) (1 + Z _ {L - 1} X _ {1} Z _ {3}).
\]
<|det|>text [83, 313, 919, 343]<|/det|>Thus the local projector is \( P_{I,I + 1} \) with exceptions on the boundary, which correspond to local symmetric defects. Since a phase is at the thermodynamic limit, the phase realized in [35] is equivalent to
<|det|>equation [437, 352, 569, 385]<|/det|>\[
H = - \sum_ {I} P _ {I, I + 1}.
\]
<|det|>text [84, 393, 519, 409]<|/det|>The component of \( P_{I,I + 1} \) in each sector can be expanded as
<|det|>equation [219, 418, 789, 495]<|/det|>\[
P _ {e} = \frac {1}{4} \begin{array}{c c c c c} & e e & s s & r ^ {2} r ^ {2} & s r ^ {2} s r ^ {2} \\ \hline e e & 1 & 1 & - 1 & 1 \\ s s & 1 & 1 & - 1 & 1 \\ r ^ {2} r ^ {2} & - 1 & - 1 & 1 & - 1 \\ s r ^ {2} s r ^ {2} & 1 & 1 & - 1 & 1 \end{array} , \quad P _ {s} = \frac {1}{4} \begin{array}{c c c c c} e s & s e & s r ^ {2} r ^ {2} & r ^ {2} s r ^ {2} \\ \hline e s & 1 & 1 & - 1 & 1 \\ s e & 1 & 1 & - 1 & 1 \\ s r ^ {2} r ^ {2} & - 1 & - 1 & 1 & - 1 \\ r ^ {2} s r ^ {2} & 1 & 1 & - 1 & 1 \\ \hline \end{array} ,
\]
<|det|>text [84, 583, 135, 596]<|/det|>Define
<|det|>equation [269, 604, 731, 636]<|/det|>\[
m _ {e} = \frac {| e e s s r ^ {2} r ^ {2} s r ^ {2} s r ^ {2}}{| 1 1 - 1} , \quad m _ {s} = \frac {| e s s e s r ^ {2} r ^ {2} r ^ {2} s r ^ {2}}{| 1 1 - 1} ,
\]
<|det|>equation [248, 638, 756, 670]<|/det|>\[
m _ {r ^ {2}} = \frac {| e r ^ {2} r ^ {2} e s s r ^ {2} s r ^ {2} s}{r ^ {2} | 1 1 - 1 - 1}, \quad m _ {s r ^ {2}} = \frac {| e s r ^ {2} s r ^ {2} e s r ^ {2} r ^ {2} s}{s r ^ {2} | 1 1 - 1}.
\]
<|det|>text [84, 680, 127, 693]<|/det|>Then
<|det|>equation [457, 700, 548, 730]<|/det|>\[
P = \frac {1}{4} m ^ {\dagger} m.
\]
<|det|>text [84, 739, 414, 754]<|/det|>We can then extract the cocycle gauge by \(m\):
<|det|>equation [260, 762, 742, 781]<|/det|>\[
\omega (r ^ {2}, r ^ {2}) = \omega (s r ^ {2}, r ^ {2}) = \omega (s r ^ {2}, s) = \omega (s r ^ {2}, s) = - 1, \quad \omega (\mathrm{others}) = 1.
\]
<|det|>text [84, 789, 794, 805]<|/det|>Thus the Hamiltonian of [35], for either \( L = 0 \mod 8 \) or \( L = 4 \mod 8 \), matches our model locally
<|det|>equation [405, 813, 597, 849]<|/det|>\[
H = - \frac {1}{4} \sum_ {i} m _ {i, i + 1} ^ {\dagger} m _ {i, i + 1}.
\]
<|det|>text [84, 858, 517, 873]<|/det|>And the MPO \(A_{\sigma}\) acts on ground state as \(\operatorname{Tr}(A_{\sigma})|e\rangle = 2|e\rangle\).
<|det|>text [99, 873, 921, 889]<|/det|>The third model is constructed similarly. After applying the CZ gate, the ground state is stabilized by the generator
<|det|>equation [361, 898, 642, 914]<|/det|>\[
- X _ {2 n - 1} = 1, \quad - Z _ {2 n - 2} X _ {2 n} Z _ {2 n + 2} = 1.
\]
