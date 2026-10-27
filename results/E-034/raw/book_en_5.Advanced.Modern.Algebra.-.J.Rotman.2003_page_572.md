<|det|>page_number [203, 120, 232, 133]<|/det|>556
<|det|>header [662, 120, 796, 134]<|/det|>Algebras Ch. 8
<|det|>text [201, 149, 794, 240]<|/det|>ring, and Jacobson semisimple, by Corollary 8.35(ii)]. The factor module \( J^q / J^{q+1} \) is an \( (R / J) \)-module; hence, by Corollary 8.43, \( J^q / J^{q+1} \) is a semisimple module, and so it can be decomposed into a direct sum of (possibly infinitely many) simple \( (R / J) \)-modules. But there can be only finitely many summands, for every \( (R / J) \)-submodule of \( J^q / J^{q+1} \) is necessarily an \( R \)-submodule, and \( J^q / J^{q+1} \) has the DCC on \( R \)-submodules. Hence, there are simple \( (R / J) \)-modules \( S_i \) with
<|det|>equation [387, 248, 609, 266]<|/det|>\[
J ^ {q} / J ^ {q + 1} = S _ {1} \oplus S _ {2} \oplus \dots \oplus S _ {p}.
\]
<|det|>text [201, 275, 794, 303]<|/det|>Throwing away one simple summand at a time yields a series of \( J^q / J^{q+1} \) whose \( i \)th factor module is
<|det|>equation [335, 306, 660, 322]<|/det|>\[
(S _ {i} \oplus S _ {i + 1} \oplus \dots \oplus S _ {p}) / (S _ {i + 1} \oplus \dots \oplus S _ {p}) \cong S _ {i}.
\]
<|det|>text [201, 326, 794, 386]<|/det|>Now the simple  \( (R/J) \) -module  \( S_{i} \)  is also a simple R-module, for it is an R-module annihilated by J, so that we have constructed a composition series for  \( J^{q}/J^{q+1} \)  as a left R-module. Finally, refine the original series for R in this way, for every q, to obtain a composition series for R.
<|det|>text [220, 393, 545, 407]<|/det|>Of course, the converse of Theorem 8.46 is false.
<|det|>text [221, 408, 428, 422]<|/det|>The next result is fundamental.
<|det|>text [201, 437, 794, 468]<|/det|>Theorem 8.47 (Maschke's Theorem). If \( G \) is a finite group and \( k \) is a field whose characteristic does not divide \( |G| \), then \( kG \) is a left semisimple ring.
<|det|>text [201, 488, 664, 503]<|/det|>Remark. The hypothesis always holds if \( k \) has characteristic 0.
<|det|>text [201, 516, 794, 653]<|/det|>Proof. By Proposition 8.42, it suffices to prove that every left ideal \( I \) of \( kG \) is a direct summand. Since \( k \) is a field, \( kG \) is a vector space over \( k \) and \( I \) is a subspace. By Corollary 6.49, \( I \) is a (vector space) direct summand: There is a subspace \( V \) (which may not be a left ideal in \( kG \)) with \( kG = I \oplus V \). There is a \( k \)-linear transformation \( d: kG \to I \) with \( d(b) = b \) for all \( b \in I \) and with \( \ker d = V \) [each \( u \in kG \) has a unique expression of the form \( u = b + v \), where \( b \in I \) and \( v \in V \), and \( d(u) = b \)]. Were \( d \) a \( kG \)-map, not merely a \( k \)-map, then we would be done, by the criterion of Corollary 7.17: \( I \) is a summand of \( kG \) if and only if it is a retract; that is, there is a \( kG \)-map \( D: kG \to I \) with \( D(u) = u \) for all \( u \in I \). We now force \( d \) to be a \( kG \)-map by an “averaging” process.
<|det|>text [220, 654, 391, 668]<|/det|>Define \(D:kG\to kG\) by
<|det|>equation [405, 677, 591, 713]<|/det|>\[
D (u) = \frac {1}{| G |} \sum_ {x \in G} x d (x ^ {- 1} u)
\]
<|det|>text [200, 721, 794, 750]<|/det|>for all \( u \in kG \). Note that \( |G| \neq 0 \) in \( k \), by the hypothesis on the characteristic of \( k \), and so it is invertible. It is obvious that \( D \) is a \( k \)-map.
<|det|>text [201, 751, 294, 765]<|/det|>(i) im \(D \subseteq I\).
<|det|>text [200, 765, 794, 810]<|/det|>If \( u \in kG \) and \( x \in G \), then \( d(x^{-1}u) \in I \) (because \( \operatorname{im} d \subseteq I \)), and \( xd(x^{-1}u) \in I \) because \( I \) is a left ideal. Therefore, \( D(u) \in I \), for each term in the defining sum of \( D(u) \) lies in \( I \).
