<|det|>page_number [116, 65, 134, 75]<|/det|>36
<|det|>header [425, 64, 575, 75]<|/det|>CHOI, JUNG, AND LEE
<|det|>title [360, 92, 638, 106]<|/det|>APPENDIX C. PROOF OF LEMMA 3.3
<|det|>text [112, 115, 884, 145]<|/det|>Here, we provide detailed proof for Lemma 3.3. We only establish (3.17) since the other estimate can be derived through a similar argument. We write \( B = B_{\mathfrak{M}} \) for simplicity.
<|det|>text [132, 146, 481, 161]<|/det|>By using the Littlewood–Paley theorem, we get
<|det|>equation [232, 166, 884, 201]<|/det|>\[
\left\| \langle \nabla \rangle^ {\alpha_ {1}} D ^ {\alpha_ {2}} B [ f, g ] \right\| _ {L ^ {\prime_ {1}} ^ {\prime}} ^ {2} \lesssim \left\| P _ {\leq 1} B [ f, g ] \right\| _ {L ^ {\prime_ {1}} ^ {\prime}} ^ {2} + \sum_ {N > 1} N ^ {2 (\alpha_ {1} + \alpha_ {2})} \left\| P _ {N} B [ f, g ] \right\| _ {L ^ {\prime_ {1}} ^ {\prime}} ^ {2}, \tag {C.1}
\]
<|det|>text [113, 206, 700, 222]<|/det|>where \(D^{\alpha_2} = \langle |\nabla |^{\alpha_2}\rangle\) or \(D^{\alpha_2} = |\nabla |^{\alpha_2}\). The first term can be estimated as follows:
<|det|>equation [382, 229, 615, 249]<|/det|>\[
\| P _ {\leq 1} B [ f, g ] \| _ {L ^ {1} _ {1}} \lesssim \| f \| _ {L ^ {1 _ {2}}} \| g \| _ {L ^ {2}}.
\]
<|det|>text [113, 254, 347, 267]<|/det|>For the second term, we observe
<|det|>equation [263, 275, 734, 311]<|/det|>\[
\| P _ {N} B [ f, g ] \| _ {L ^ {1 _ {1} ^ {\prime}}} \lesssim \| P _ {N} B [ P _ {\leq \frac {N}{8}} f, g ] \| _ {L ^ {1 _ {1} ^ {\prime}}} + \sum_ {M > \frac {N}{8}} \| P _ {N} B [ P _ {M} f, g ] \| _ {L ^ {1 _ {1} ^ {\prime}}}.
\]
<|det|>text [113, 319, 314, 335]<|/det|>By using (3.16), we deduce
<|det|>equation [126, 342, 871, 375]<|/det|>\[
\| P _ {N} B [ P _ {\leq \frac {N}{8}} f, g ] \| _ {L ^ {1 _ {1} ^ {\prime}}} \lesssim \| B [ P _ {\leq \frac {N}{8}} f, P _ {\frac {N}{8} <  . <   8 N} g ] \| _ {L ^ {1 _ {1} ^ {\prime}}} \lesssim \| P _ {\leq \frac {N}{8}} f \| _ {L ^ {1 _ {2}}} \| P _ {\frac {N}{8} <  . <   8 N} g \| _ {L ^ {2}} \lesssim \| f \| _ {L ^ {1 _ {2}}} \sum_ {M \sim N} \| P _ {M} g \| _ {L ^ {2}}.
\]
<|det|>text [113, 381, 308, 396]<|/det|>Consequently, we arrive at
<|det|>equation [226, 402, 772, 507]<|/det|>\[
\begin{array}{l} \sum_ {N > 1} N ^ {2 (\alpha_ {1} + \alpha_ {2})} \| P _ {N} B [ P _ {\leq \frac {N}{8}} f, g ] \| _ {L ^ {1 _ {1} ^ {\prime}}} ^ {2} \lesssim \| f \| _ {L ^ {1 _ {2}}} ^ {2} \sum_ {N > 1} \left(\sum_ {M \sim N} N ^ {\alpha_ {1} + \alpha_ {2}} \| P _ {M} g \| _ {L ^ {2}}\right) ^ {2} \\ \lesssim \| f \| _ {L ^ {1 _ {2}}} ^ {2} \sum_ {M \gtrsim 1} M ^ {2 (\alpha_ {1} + \alpha_ {2})} \| P _ {M} g \| _ {L ^ {2}} ^ {2} \\ \lesssim \| f \| _ {L ^ {1 2}} ^ {2} \| g \| _ {H ^ {\alpha_ {1} + \alpha_ {2}}} ^ {2}. \\ \end{array}
\]
<|det|>text [113, 511, 257, 525]<|/det|>Meanwhile, we find
<|det|>equation [180, 534, 800, 573]<|/det|>\[
\sum_ {M > \frac {N}{8}} \| P _ {N} B [ P _ {M} f, g ] \| _ {L ^ {l _ {1} ^ {\prime}}} \lesssim \sum_ {M > \frac {N}{8}} \| P _ {M} f \| _ {L ^ {2}} \| g \| _ {L ^ {l _ {2}}} \lesssim \sum_ {M > \frac {N}{8}} \frac {1}{M ^ {\alpha_ {1} + \alpha_ {2}}} \| P _ {M} f \| _ {\dot {H} ^ {\alpha_ {1} + \alpha_ {2}}} \| g \| _ {L ^ {l _ {2}}}
\]
<|det|>text [113, 581, 371, 596]<|/det|>due to (3.16). Then, it follows that
<|det|>equation [249, 602, 750, 848]<|/det|>\[
\begin{array}{l} \sum_ {N > 1} N ^ {2 (\alpha_ {1} + \alpha_ {2})} \left(\sum_ {M > \frac {N}{8}} \| P _ {N} B [ P _ {M} f, g ] \| _ {L ^ {l _ {1} ^ {\prime}}}\right) ^ {2} \\ \lesssim \sum_ {N > 1} \left(\sum_ {M > \frac {N}{8}} \left(\frac {N}{M}\right) ^ {\alpha_ {1} + \alpha_ {2}} \| P _ {M} f \| _ {\dot {H} ^ {\alpha_ {1} + \alpha_ {2}}} \| g \| _ {L ^ {l _ {2}}}\right) ^ {2} \\ \lesssim \| g \| _ {L ^ {l _ {2}}} ^ {2} \sum_ {N > 1} \left(\sum_ {M > \frac {N}{8}} \left(\frac {N}{M}\right) ^ {\alpha_ {1} + \alpha_ {2}} \sum_ {M > \frac {N}{8}} \left(\frac {N}{M}\right) ^ {\alpha_ {1} + \alpha_ _ {2}} \| P _ {M} f \| _ {\dot {H} ^ {\alpha_ {1} + \alpha_ {2}}} ^ {2}\right) \\ \lesssim \| g \| _ {L ^ {l _ {2}}} ^ {2} \sum_ {M > \frac {1}{8}} \sum_ {1 <   N <   8 M} \left(\frac {N}{M}\right) ^ {\alpha_ {1} + \alpha_ {2}} \| P _ {M} f \| _ {\dot {H} ^ {\alpha_ {1} + \alpha_ {2}}} ^ {2} \\ \lesssim \| g \| _ {L ^ {l _ {2}}} ^ {2} \sum_ {M > \frac {1}{8}} \| P _ {M} f \| _ {\dot {H} ^ {\alpha_ {1} + \alpha_ {2}}} ^ {2.} \\ \end{array}
\]
<|det|>text [113, 853, 498, 868]<|/det|>by the Cauchy–Schwartz inequality and the fact that
<|det|>equation [414, 875, 584, 915]<|/det|>\[
\sum_ {N <   8 M} \left(\frac {N}{M}\right) ^ {\alpha_ {1} + \alpha_ {2}} \lesssim 1.
\]
