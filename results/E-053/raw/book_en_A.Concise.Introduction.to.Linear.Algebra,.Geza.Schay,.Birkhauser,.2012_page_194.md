<|det|>header [422, 54, 804, 70]<|/det|>4.2 Properties of Linear Transformations
<|det|>page_number [843, 55, 876, 69]<|/det|>181
<|det|>equation [160, 82, 878, 122]<|/det|>\[
S (\mathbf {x}) = \left[ \begin{array}{c} x _ {2} + x _ {3} \\ x _ {3} \end{array} \right] \tag {4.62}
\]
<|det|>text [117, 134, 163, 150]<|/det|>and
<|det|>equation [158, 161, 878, 201]<|/det|>\[
T (\mathbf {x}) = \left[ \begin{array}{l} x _ {1} - x _ {2} \\ x _ {1} + x _ {3} \end{array} \right]. \tag {4.63}
\]
<|det|>text [117, 213, 812, 232]<|/det|>Then \( Q = S + T \) and \( R = cT \) are the linear transformations given by
<|det|>equation [158, 243, 878, 283]<|/det|>\[
Q (\mathbf {x}) = \left[ \begin{array}{l} x _ {1} + x _ {3} \\ x _ {1} + 2 x _ {3} \end{array} \right] \tag {4.64}
\]
<|det|>text [117, 296, 163, 311]<|/det|>and
<|det|>equation [158, 322, 878, 363]<|/det|>\[
R (\mathbf {x}) = \left[ \begin{array}{l} c (x _ {1} - x _ {2}) \\ c (x _ {1} + x _ {3}) \end{array} \right]. \tag {4.65}
\]
<|det|>text [116, 405, 880, 440]<|/det|>With Definition 4.2.4 Theorems 4.2.8 and 4.2.9 lead to the following theorem.
<|det|>text [117, 454, 881, 561]<|/det|>Theorem 4.2.10. (The Linear Transformations from U to V Form a Vector Space, Which Is Isomorphic to \(\mathcal{M}_{m,n}\)). Let \(L(U,V)\) denote the set of all linear transformations from an \(n\)-dimensional vector space \(U\) to an \(m\)-dimensional vector space \(V\), and let \(A = (\mathbf{a}_1,\mathbf{a}_2,\dots,\mathbf{a}_n)\) be an ordered basis for \(U\), \(B = (\mathbf{b}_1,\mathbf{b}_2,\dots,\mathbf{b}_m)\) an ordered basis for \(V\), and \(T_{A,B}\) the \(m\times n\) matrix that represents any \(T\in L(U,V)\) relative to these bases. Then
<|det|>text [117, 563, 880, 598]<|/det|>1. \( L(U, V) \), together with addition and scalar multiple of transformations as in Definition 4.2.4, is a vector space.
<|det|>text [117, 599, 878, 651]<|/det|>2. The mapping \( M \) from \( L(U,V) \) to the vector space \( \mathcal{M}_{m,n} \) of all \( m\times n \) matrices\(^6\) given by \( M(T) = T_{A,B} \) is linear and an isomorphism. Hence \( L(U,V) \) is mn-dimensional.
<|det|>text [116, 665, 880, 755]<|/det|>Proof. 1. \( L(U,V) \) is clearly nonempty: the zero mapping \( O \) is in it. Theorem 4.2.9 shows that \( L(U,V) \) is closed under addition and multiplication by scalars. The vector space axioms for \( L(U,V) \) follow from the corresponding ones in \( V \) for every \( \mathbf{x} \) in \( \mathbf{y} = T(\mathbf{x}) \). In particular, the zero element is the zero mapping \( O \), and the element \( -T \) is the mapping \( (-1)T \).
<|det|>text [116, 756, 878, 809]<|/det|>2. Let \( S, T \in L(U, V) \) and \( a, b \) any scalars. Then, by Theorem 4.1.3, for all \( \mathbf{x} \in U \), \( \mathbf{y} = T(\mathbf{x}) \) becomes in terms of coordinates \( \mathbf{y}_B = T_{A,B}\mathbf{x}_A = M(T)\mathbf{x}_A \). Similarly \( \mathbf{y} = (aS + bT)(\mathbf{x}) \) becomes
<|det|>equation [163, 825, 875, 843]<|/det|>\[
\mathbf {y} _ {B} = (a S + b T) _ {A, B} \mathbf {x} _ {A} = M (a S + b T) \mathbf {x} _ {A}. \tag {4.66}
\]
<|det|>page_footnote [126, 871, 320, 888]<|/det|>\( ^{6} \)  See Example 3.1.2.
