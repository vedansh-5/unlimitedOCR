HOMEOMORPHISMS OF THE PSEUDOARC

23

hence \( p \sqcap_{G_m} q \), as \( \beth_m^m \) is \( \sqcap \)-preserving. Conversely, if \( p \sqcap_{G_m} q \) then we have \( r \in G_{m+1} \) with \( p, q > r \), as \( \beth_{m+1}^m \) is edge-witnessing, showing that \( \sqcap_{G_m} \subseteq \wedge_m \). Thus \( \mathbb{P} \) is a K-poset that is K-subabsorbing, by construction.

3.3. Compatibility. Throughout the rest of this section we assume that

(1) K is a fixed subcategory of the graph category G.

(2) \(\mathbb{P}\) is a K-regular K-subabsorbing K-poset.

In particular, \(\mathbb{P}\) is regular so \(\mathbb{SP}\) is Hausdorff, by [BBV23, Corollary 2.40]. As K-morphisms are co-injective, each level \(\mathbb{P}_n\) is a minimal cap, by [BBV23, Proposition 1.21], which thus yields a minimal open cover \(\{p_{\mathsf{S}}: p \in \mathbb{P}_n\}\) of \(\mathbb{SP}\), by [BBV23, Proposition 2.8]. In particular, \(p_{\mathsf{S}} \neq \emptyset\), for all \(p \in \mathbb{P}\), i.e. \(\mathbb{P}\) is also a prime \(\omega\)-poset.

We are interested in continuous maps on \(\mathbb{SP}\) that are compatible with the given subcategory \(\mathbf{K}\). First, for any finite \(\supset \subseteq \mathbb{P} \times \mathbb{P}\), let \(\supset^{\mathbf{C}}\) denote the basic open subset of \(\mathbf{C}_{\mathbb{SP}}^{\mathbb{SP}}\) corresponding to the open subset \(\supset^{\mathbf{S}}\) of strong refiners defined in (2.3), i.e.

\[
\supset^ {\mathbf {C}} = \{\phi \in \mathbf {C} _ {\mathbb {S P}} ^ {\mathbb {S P}}: \supset \subseteq \supset_ {\phi} \} = \{\phi \in \mathbf {C} _ {\mathbb {S P}} ^ {\mathbb {S P}}: \forall p, q (q \supset p \Rightarrow q _ {\mathsf {S}} \supseteq \phi [ \overline {{p _ {\mathsf {S}}}} ]) \}.
\]

Definition 3.14. The K-compatible functions on SP are given by

\[
\mathbf {C} _ {\mathbf {K}} = \bigcap_ {m \in \omega} \bigcup_ {n \geq m} \bigcup_ {\supset \in \mathbf {K} _ {n} ^ {m}} \supset^ {\mathbf {C}} = \{\phi \in \mathbf {C} _ {\mathbb {S P}} ^ {\mathbb {S P}}: \forall m \in \omega \exists \supset \in \mathbf {K} _ {n} ^ {m} (\supset \subseteq \supset_ {\phi}) \}.
\]

Corollary 2.32 tells us that \(\mathbf{C}_{\mathbf{K}}\) has another basis consisting of open sets \(\leftarrow_{\mathbf{K}}\), for relations \(\leftarrow \subseteq \mathbb{P}_n \times \mathbb{P}_n\) defined on levels of \(\mathbb{P}\), where

\[
\leftarrow_ {\mathbf {K}} = \leftarrow_ {\mathbf {C}} \cap \mathbf {C} _ {\mathbf {K}} = \{\phi \in \mathbf {C} _ {\mathbf {K}}: \phi \subseteq \leftarrow_ {\mathbf {S}} \}.
\]

However, many of these basic sets can be empty and our interest in \(\mathbf{K}\)-like relations stems from the fact that these are the only ones for which \(\leftarrow_{\mathbf{S}}\) can contain any \(\phi \in \mathbf{C}_{\mathbf{K}}\). We can even revert to a relation below \(\leftarrow\) which not just \(\mathbf{K}\)-like but widely \(\mathbf{K}\)-subfactorisable (note every widely \(\mathbf{K}\)-subfactorisable \(\leftarrow\) is \(\mathbf{K}\)-like, by Lemma 3.8, as \(\mathbb{P}\) is \(\mathbf{K}\)-subabsorbing).

Let us denote the widely K-subfactorisable relations on any  \( G \in K \)  by

\[
G ^ {\mathbf {K}} = \{\leftarrow \subseteq G \times G: \forall > \in \mathbf {K} _ {H} ^ {G} (\Leftarrow \circ \rightarrow \text {subfactors into some} \sqsupset , \exists \in \mathbf {K} _ {I} ^ {H}) \}.
\]

Lemma 3.15. For any \(m, m' \in \omega\), \(\leftarrow \subseteq \mathbb{P}_m \times \mathbb{P}_m\), \(\leftarrow' \subseteq \mathbb{P}_{m'} \times \mathbb{P}_{m'}\) and \(\phi \in \leftarrow_{\mathbf{K}} \cap \leftarrow_{\mathbf{K}}'\), we have some \(n > \max(m, m')\) and \(\leftarrow \subseteq \mathbb{P}_n^{\mathbf{K}}\) with \(\phi \in \leftarrow_{\mathbf{K}}\), \(\leftarrow \leq \leftarrow\) and \(\leftarrow \leq \leftarrow'\)

Proof. By Proposition 2.31, we have \( k > m \) with \( \leftarrow_k^\phi \triangleleft_k \leftarrow \) and \( \leftarrow_k^\phi \triangleleft_k \leftarrow' \). By Proposition 3.11, we have \( \mathbb{P} \)-subamalgable \( \geqslant \in \mathbf{K}_l^k \). As \( \phi \in \mathbf{C}_{\mathbf{K}} \), we have \( \supseteq \in \mathbf{K}_n^l \) with \( \supseteq \subseteq \supset_\phi \). By Propositions 2.19 and 2.36, \( \phi \subseteq (\supset \circ \leq_n^l)_\mathsf{S} \) and \( \supset \circ \leq_n^l \subseteq \leftarrow_l^\phi \). Now set

\[
\leftarrow^ {\prime} = <   \circ > \circ \supset \subseteq_ {n} ^ {l} \circ <   \circ > \quad \text { and } \quad \leftarrow = \leq_ {l} ^ {k} \circ > \circ \supset \supset \circ \leq_ {n} ^ {l} \circ <   \circ \geq_ {l} ^ {k}.
\]

As \(\supset \circ \leq_{n}^{l} \subseteq \leftarrow'\), it follows that \(\leftarrow'\) is also a \(\mathbf{K}\)-like relation satisfying \(\phi \subseteq \leftarrow_{\mathfrak{S}}'\). The same then applies to the even larger relation \(\leftarrow\), which is also widely \(\mathbf{K}\)-subfactorisable, by Lemma 3.3. As \(\supset \circ \leq_{n}^{l} \subseteq \leftarrow_{l}^{\phi} \subseteq \leq_{l}^{k} \circ \leftarrow_{k}^{\phi} \circ \geq_{l}^{k}\) and \(\leftarrow_{k}^{\phi} \triangleleft_{k} \leftarrow\),

\[
\leftarrow \subseteq \leq_ {l} ^ {k} \circ \geq_ {l} ^ {k} \circ \leq_ {l} ^ {k} \circ \leftarrow_ {k} ^ {\phi} \circ \geq_ {l} ^ {k} \circ \leq_ {l} ^ {k} \circ \geq_ {l} ^ {k} \subseteq \leq_ {l} ^ {k} \circ \wedge_ {k} \circ \leftarrow_ {k} ^ {\phi} \circ \wedge_ {k} \circ \geq_ {l} ^ {k} \subseteq \leq_ {l} ^ {m} \circ \leftarrow \circ \geq_ {l} ^ {m}.
\]

This shows that \(\leftarrow \leq \leftarrow\) and, likewise, \(\leftarrow \leq \leftarrow'\) as well.

Corollary 3.16. The open sets \(\{\leftarrow_{\mathbf{K}}:n\in \omega\) and \(\leftarrow \in \mathbb{P}_n^{\mathbf{K}}\}\) form a basis for \(\mathbf{C}_{\mathbf{K}}\)

Proof. This is immediate from Lemma 3.15 once we note \(\leftarrow \leq \leftarrow\) implies \(\leftarrow_{\mathbf{K}} \subseteq \leftarrow_{\mathbf{K}}\).
