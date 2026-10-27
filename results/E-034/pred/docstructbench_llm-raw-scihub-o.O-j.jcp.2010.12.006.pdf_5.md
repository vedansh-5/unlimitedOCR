2080

Y. Sun, P.S.P. Tse/Journal of Computational Physics 230 (2011) 2076–2094

\[
\partial_ {t} z _ {i, j, k} ^ {l} = \frac {z _ {i , j , k} ^ {l + 1} - z _ {i , j , k} ^ {l}}{\Delta t}, \quad \overline {{\partial}} _ {t} z _ {i, j, k} ^ {l} = \frac {z _ {i , j , k} ^ {l + 2} - z _ {i , j , k} ^ {l - 1}}{2 \Delta t}, \quad \partial_ {x _ {1}} z _ {i, j, k} ^ {l} = \frac {z _ {i + 1 , j , k} ^ {l} - z _ {i , j , k} ^ {l}}{\Delta x _ {1}}, \quad \overline {{\partial}} _ {x _ {1}} z _ {i, j, k} ^ {l} = \frac {z _ {i + 1 , j , k l} ^ {l} - z _ {i - 1 , j , k} ^ {l}}{2 \Delta x _ {1}}, \tag {6}
\]

where the difference operators \(\partial_t\), \(\overline{\partial}_t\) are the discretization of \(\frac{\partial}{\partial t}\), and the difference operators \(\partial_{x_1}\), \(\overline{\partial}_{x_1}\) are the discretization of \(\frac{\partial}{\partial x_1}\). Via these notations and the properties of the difference operators,\(^6\) we present the statement of the local/global conservation laws for the different numerical methods.

3.1. Symplectic method for Maxwell's equations

The following method is constructed based on the method of lines, i.e. discretizing the Hamiltonian PDEs in space, then applying the symplectic method to the resulting Hamiltonian ODEs (see for example  \( [6,22] \) ). Later, we will show the method is also multisymplectic in the corresponding statement of multisymplecticity.

For Maxwell's equations in Hamiltonian form, we use the central finite difference in space (which is leapfrog discretization) and implicit midpoint rule (which is symplectic) in time, it is easy to show that the Hamiltonian formulations in (5) and (7) for Maxwell's equations reduce to the same discretized system,

\[
\partial_ {t} z _ {i, j, k} ^ {l} + M ^ {- 1} K _ {1} \overline {{\partial}} _ {x _ {1}} z _ {i, j, k} ^ {l + 1} + M ^ {- 1} K _ {2} \overline {{\partial}} _ {x _ {2}} z _ {i, j, k} ^ {l + 1} + M ^ {- 1} K _ {3} \overline {{\partial}} _ {x _ {3}} z _ {i, j, k} ^ {l + 1} = 0, \tag {18}
\]

where indices \(i,j,k\) denote spatial increments and index \(I\) denotes time increment, and matrices \(M,K_1,\ldots\) as in (10). We refer to this particular discretization as the symplectic method, though it is also multisymplectic.

The symplectic method (18) is second-order in space and time, and is unconditionally stable. Furthermore, this discrete system preserves two discretized global conservation laws: the first one is the discrete quadratic global conservation law based on (8),

\[
\frac {1}{2} \partial_ {t} \left[ \mu \mathbf {H} _ {i, j, k} ^ {l} \cdot \mathbf {H} _ {i, j, k} ^ {l} + \varepsilon \mathbf {E} _ {i, j, k} ^ {l} \cdot \mathbf {E} _ {i, j, k} ^ {l} \right] = 0. \tag {19}
\]

The second discretized global conservation law for symplectic method is based on the helicity Hamiltonian functional (6)

\[
\partial_ {t} \left[ \frac {1}{2 \varepsilon} \mathbf {H} _ {i j, k} ^ {l} \cdot \widehat {\nabla} \times \mathbf {H} _ {i j, k} ^ {l} + \frac {1}{2 \mu} \mathbf {E} _ {i j, k} ^ {l} \cdot \widehat {\nabla} \times \mathbf {E} _ {i j, k} ^ {l} \right] = 0, \tag {20}
\]

where \(\widehat{\nabla} \times = R_1 \partial_{x_1} + R_2 \partial_{x_2} + R_3 \partial_{x_3}\). Furthermore, the scheme (18) is proved to be multisymplectic, since it preserves the following multisymplectic conservation law

\[
\begin{array}{l} \partial_ {t} \left[ d \mathbf {E} _ {i j, k} ^ {l} \wedge d \mathbf {H} _ {i j, k} ^ {l} \right] + \partial_ {x _ {1}} \left[ \frac {1}{\varepsilon} d \mathbf {H} _ {i j, k} ^ {l + \frac {1}{2}} \wedge \mu d \mathbf {E} _ {i - 1 j, k} ^ {l + \frac {1}{2}} \wedge R _ {1} d \mathbf {E} _ {i j, k} ^ {l + \frac {1}{2}} \right] + \partial_ {x _ {2}} \left[ \frac {1}{\varepsilon} d \mathbf {H} _ {i j - 1 k} ^ {l + \frac {1}{2}} \wedge R _ {2} d \mathbf {H} _ {i j - 1 k} ^ {l + \frac {1}{2}} + \frac {1}{\mu} d \mathbf {E} _ {i j - 1 k} ^ {l + \frac {1}{2}} \wedge R _ {2} d \mathbf {E} _ {i j, k} ^ {l + \frac {1}{2}} \right] \\ + \partial_ {x _ {3}} \left[ \frac {1}{\varepsilon} d \mathbf {H} _ {i j, k - 1} ^ {l + \frac {1}{2}} \wedge R _ {3} d \mathbf {H} _ {i j, k + 1} ^ {l + \frac {1}{2}} + R _ {3} d \mathbf {E} _ {i j, k} ^ {l + \frac {1}{2}} \right] = 0. \tag {21} \\ \end{array}
\]

Besides the global conservation laws, for the scheme (18) applied to Maxwell's equations, we also have the following local conservation laws based on (13)-(15):

The discrete quadratic conservation law is

\[
\begin{array}{l} \frac {1}{2} \partial_ {t} \left[ \mu \mathbf {H} _ {i j, k} ^ {l} \cdot \mathbf {H} _ {i j, k} ^ {l} + \varepsilon \mathbf {E} _ {i j, k} ^ {l} \cdot \mathbf {E} _ {i j, k} ^ {l} \right] + \frac {1}{2} \partial_ {x _ {1}} \left[ \mathbf {H} _ {i j, k} ^ {l + \frac {1}{2}} \cdot R _ {1} \mathbf {E} _ {i - 1 j, k} ^ {l + \frac {1}{2}} + \mathbf {H} _ {i - 1 j, k} ^ {l + \frac {1}{2}} \cdot R _ {1} \mathbf {E} _ {i j, k} ^ {l + \frac {1}{2}} \right] + \frac {1}{2} \partial_ {x _ {2}} \left[ \mathbf {H} _ {i j, k} ^ {l + \frac {1}{2}} \cdot R _ {2} \mathbf {E} _ {i j - 1, k} ^ {l + \frac {1}{2}} + \mathbf {H} _ {i j - 1, k} ^ {l + \frac {1}{2}} \cdot R _ {2} \mathbf {E} _ {i j, k} ^ {l + \frac {1}{2}} \right] \\ + \frac {1}{2} \partial_ {x _ {3}} \left[ \mathbf {H} _ {i j, k} ^ {l + \frac {1}{2}} \cdot R _ {3} \mathbf {E} _ {i j, k - 1} ^ {l + \frac {1}{2}} + \mathbf {H} _ {i j, k - 1} ^ {l + \frac {1}{2}} \cdot R _ {3} \mathbf {E} _ {i j, k} ^ {l + \frac {1}{2}} \right] = 0. \tag {22} \\ \end{array}
\]

The discrete energy conservation law is

\[
\begin{array}{l} \partial_ {t} \left[ \frac {1}{2 \varepsilon} \mathbf {H} _ {i j, k} ^ {l} \cdot \widehat {\nabla} \times \mathbf {H} _ {i j, k} ^ {l} + \frac {1}{2 \mu} \mathbf {E} _ {i j, k} ^ {l} \cdot \widehat {\nabla} \times \mathbf {E} _ {i j, k} ^ {l} \right] + \partial_ {x _ {1}} \left[ \frac {1}{2 \varepsilon} \partial_ {t} \mathbf {H} _ {i j, k} ^ {l} \cdot R _ {1} \mathbf {H} _ {i - 1 j, k} ^ {l + \frac {1}{2}} + \frac {1}{2 \mu} \partial_ {t} \mathbf {E} _ {i j, k} ^ {l} \cdot R _ {1} \mathbf {E} _ {i - 1 j, k} ^ {l + \frac {1}{2}} \right] \\ + \partial_ {x _ {2}} \left[ \frac {1}{2 \varepsilon} \partial_ {t} \mathbf {H} _ {i j, k} ^ {l} \cdot R _ {2} \mathbf {H} _ {i j - 1, k} ^ {l + \frac {1}{2}} + \frac {1}{2 \mu} \partial_ {t} \mathbf {E} _ {i j, k} ^ {l} \cdot R _ {2} \mathbf {E} _ {i j, k} ^ {l + \frac {1}{2}} \right] + \partial_ {x _ {3}} \left[ \frac {1}{2 \varepsilon} \partial_ {t} \mathbf {H} _ {i j, k} ^ {l} \cdot R _ {3} \mathbf {H} _ {i j, k - 1} ^ {l + \frac {1}{2}} + \frac {1}{2 \mu} \partial_ {t} \mathbf {E} _ {i j, k} ^ {l} \cdot R _ {3} \mathbf {E} _ {i j, k - 1} ^ {l + \frac {1}{2}} \right] = 0. \tag {23} \\ \end{array}
\]

The discrete momentum conservation law is

\( ^{6} \)  Let  \( p_{i} \)  and  \( q_{i} \)  are the functions at grid i,  \( \partial \) ,  \( \bar{\partial} \)  are the difference operators, then

\(\partial [q_i p_i] = q_{i + 1}\partial p_i + \partial q_i p_i = \partial q_i p_{i + 1} + q_i\partial p_i,\)

\(\partial [q_{i + 1}p_i] = \partial q_{i + 1}p_{i + 1} + q_{i + 1}\partial p_i,\)

\(\overline{\partial}[q_i p_i] = \overline{\partial} q_i p_{i+1} + q_{i-1} \overline{\partial} p_i = \overline{\partial} p_i q_{i+1} + p_{i-1} \overline{\partial} q_i,\)

\(\overline{\partial}[q_i p_{i+1}] = q_{i+1}\overline{\partial} p_{i+1} + \overline{\partial} q_i p_i.\)

2080

Y. Sun, P.S.P. Tse/Journal of Computational Physics 230 (2011) 2076–2094

\[
\partial_ {t} z _ {i, j, k} ^ {l} = \frac {z _ {i , j , k} ^ {l + 1} - z _ {i , j , k} ^ {l}}{2 \Delta t}, \quad \overline {{\partial}} _ {t} z _ {i, j, k} ^ {l} = \frac {z _ {i + 1 , j , k} ^ {l} - z _ {i , j , k} ^ {l}}{2 \Delta t}, \quad \partial_ {x _ {1}} z _ {i, j, k} ^ {l} = \frac {z _ {i + 1 , j , k} ^ {l} - \overline {{z}} _ {i - 1 , j , k} ^ {l}}{2 \Delta x _ {1}},
\]

where the difference operators \(\partial_t\), \(\overline{\partial}_t\) are the discretization of \(\frac{\partial}{\partial t}\), and the difference operators \(\partial_{x_1}\), \(\overline{\partial}_{x_1}\) are the discretization of \(\frac{\partial}{\partial x_1}\). Via these notations and the properties of the difference operators,\(^6\) we present the statement of the local/global conservation laws for the different numerical methods.

3.1. Symplectic method for Maxwell's equations

The following method is constructed based on the method of lines, i.e. discretizing the Hamiltonian PDEs in space, then applying the symplectic method to the resulting Hamiltonian ODEs (see for example  \( [6,22] \) ). Later, we will show the method is also multisymplectic in the corresponding statement of multisymplecticity.

For Maxwell's equations in Hamiltonian form, we use the central finite difference in space (which is leapfrog discretization) and implicit midpoint rule (which is symplectic) in time, it is easy to show that the Hamiltonian formulations in (5) and (7) for Maxwell's equations reduce to the same discretized system,

\[
\partial_ {t} z _ {i, j, k} ^ {l} + M ^ {- 1} K _ {1} \overline {{\partial}} _ {x _ {1}} z _ {i, j, k} ^ {l + 1} + M ^ {- 1} K _ {2} \overline {{\partial}} _ {x _ {2}} z _ {i, j, k} ^ {l + 1} + M ^ {- 1} K _ {3} \overline {{\partial}} _ {x _ {3}} z _ {i, j, k} ^ {l + 1} = 0, \tag {18}
\]

where indices \(i,j,k\) denote spatial increments and index \(I\) denotes time increment, and matrices \(M,K_1,\ldots\) as in (10). We refer to this particular discretization as the symplectic method, though it is also multisymplectic.

The symplectic method (18) is second-order in space and time, and is unconditionally stable. Furthermore, this discrete system preserves two discretized global conservation laws: the first one is the discrete quadratic global conservation law based on (8),

\[
\frac {1}{2} \partial_ {t} \left[ \mu \mathbf {H} _ {i, j, k} ^ {l} \cdot \mathbf {H} _ {i, j, k} ^ {l} + \varepsilon \mathbf {E} _ {i, j, k} ^ {l} \cdot \mathbf {E} _ {i, j, k} ^ {l} \right] = 0. \tag {19}
\]

The second discretized global conservation law for symplectic method is based on the helicity Hamiltonian functional (6)

\[
\partial_ {t} \left[ \frac {1}{2 \varepsilon} \mathbf {H} _ {i, j, k} ^ {l} \cdot \widehat {\nabla} \times \mathbf {H} _ {i, j, k} ^ {l} + \frac {1}{2 \mu} \mathbf {E} _ {i, j, k} ^ {l} \cdot \widehat {\nabla} \times \mathbf {E} _ {i, j, k} ^ {l} \right] = 0, \tag {20}
\]

where \(\widehat{\nabla} \times = R_1\partial_{x_1} + R_2\partial_{x_2} + R_3\partial_{x_3}\). Furthermore, the scheme (18) is proved to be multisymplectic, since it preserves the following multisymplectic conservation law

\[
\begin{array}{l} \partial_ {t} \left[ d \mathbf {E} _ {i j, k} ^ {l} \wedge d \mathbf {H} _ {i j, k} ^ {l} \right] + \partial_ {x _ {1}} \left[ d \mathbf {H} _ {i j, k} ^ {l + \frac {1}{2}} \wedge \mu_ {l} d \mathbf {E} _ {i - 1 j, k} ^ {l + \frac {1}{2}} \wedge R _ {1} d \mathbf {E} _ {i j, k} ^ {l + \frac {1}{2}} \right] + \partial_ {x _ {2}} \left[ d \mathbf {H} _ {i j, k} ^ {l + \frac {1}{2}} \wedge R _ {2} d \mathbf {H} _ {i j, k} ^ {l + \frac {1}{2}} + \frac {1}{\mu} d \mathbf {E} _ {i j, k} ^ {l + \frac {1}{2}} \wedge R _ {2} d \mathbf {E} _ {i j, k} ^ {l + \frac {1}{2}} \right] \\ + \partial_ {x _ {3}} \left[ \frac {1}{\varepsilon} d \mathbf {H} _ {i j, k} ^ {l + \frac {1}{2}} - R _ {3} d \mathbf {H} _ {i j, k} ^ {l + \frac {1}{2}} - R _ {3} d \mathbf {\dot {E}} _ {i j, k} ^ {l + \frac {1}{2}} \right] = 0. \tag {22} \\ \end{array}
\]

The discrete energy conservation law is

\[
\begin{array}{l} \partial_ {t} \left[ \frac {1}{2 \varepsilon} \mathbf {H} _ {i j, k} ^ {l} \cdot \widehat {\nabla} \times \mathbf {H} _ {i j, k} ^ {l} + \frac {1}{2 \mu} \mathbf {E} _ {i j, k} ^ {l} \cdot \widehat {\nabla} \times \mathbf {E} _ {i j, k} ^ {l} \right] + \partial_ {x _ {1}} \left[ \frac {1}{2 \varepsilon} \partial_ {t} \mathbf {H} _ {i j, k} ^ {l} \cdot R _ {1} \mathbf {H} _ {i - 1 j, k} ^ {l + \frac {1}{2}} + \frac {1}{2 \mu} \partial_ {t} \mathbf {E} _ {i j, k} ^ {l} \cdot R _ {1} \mathbf {E} _ {i - 1 j, k} ^ {l + \frac {1}{2}} \right] \\ + \partial_ {x _ {2}} \left[ \frac {1}{2 \mathcal {E}} \partial_ {t} \mathbf {H} _ {i j, k} ^ {l} \cdot R _ {2} \mathbf {H} _ {i j, k} ^ {l + \frac {1}{2}} + \frac {1}{2 \mathcal {U}} \partial_ {t} \mathbf {E} _ {i j, k} ^ {l + \frac {1}{2}} \right] + \partial_ {x _ {3}} \left[ \frac {1}{2 \mathcal {E}} \partial_ {t} \mathbf {H} _ {i j, k} ^ {l} \cdot R _ {3} \mathbf {H} _ {i j, k - 1} ^ {l + \frac {1}{2}} + \frac {1}{2 \mathcal {U}} \partial_ {t} \mathbf {E} _ {i j, k - 1} ^ {l + \frac {1}{2}} \right] = 0. \tag {23} \\ \end{array}
\]

The discrete momentum conservation law is

\( ^{6} \)  Let  \( p_{i} \)  and  \( q_{i} \)  are the functions at grid i,  \( \partial_{i} \)  are the difference operators, then

\(\partial [q_i p_i] = q_{i + 1}\partial p_i + \partial q_i p_i = \partial q_i p_{i + 1} + q_i\partial p_i,\)

\(\partial [q_{i + 1}p_i] = \partial q_{i + 1}p_{i + 1} + q_{i + 1}\partial p_i,\)

\(\overline{\partial}[q_i p_i] = \overline{\partial} q_i p_{i+1} + q_{i-1} \overline{\partial} p_i = \overline{\partial} p_i q_{i+1} + p_{i-1} \overline{\partial} q_i,\)

\(\overline{\partial}[q_i p_{i+1}] = q_{i+1}\overline{\partial} p_{i+1} + \overline{\partial} q_i p_i.\)

6 Let \( p_i \) and \( q_i \) are the functions at grid \( i \), \( \partial_i \overline{\partial} \) are the difference operators, then

\[
\partial [ q _ {i} p _ {i} ] = q _ {i + 1} \partial p _ {i} + \partial q _ {i} p _ {i} = \partial q _ {i} p _ {i + 1} + q _ {i} \partial p _ {i},
\]

\[
\partial [ q _ {i + 1} p _ {i} ] = \partial q _ {i + 1} p _ {i + 1} + q _ {i + 1} \partial p _ {i},
\]

\[
\overline {{\partial}} [ q _ {i} p _ {i} ] = \overline {{\partial}} q _ {i} p _ {i + 1} + q _ {i - 1} \overline {{\partial}} p _ {i} = \overline {{\partial}} p _ {i} q _ {i + 1} + q _ {i} \overline {{\partial}} p _ {i + 1} = \overline {{\partial}} p _ {i + 1} q _ {i + 1} + q _ {i} \overline {{\partial}} p _ {i + 1} = \overline {{\partial}} q _ {i + 1} q _ {i + 1} + q _ {i} \overline {{\partial}} p _ {i + 1} + q _ {i} \overline {{\partial}} p _ {i + 1} + q _ {i} \overline {{p}} _ {i + 1} + q _ {i} \overline {{p}} _ {i + 1} + q _ {i} \overline {{q}} _ {i + 1} + q _ {i} \overline {{p}} _ {i + 1} + q _ {i} \overline {{\partial}} p _ {i + 1} + q _ {i} \overline {{\partial}} p _ {i + 1} + q _ {i} \overline {{p}} _ {i + 1} + q _ {i} \overline {{p}} _ {i + 1} + q _ {i} \overline {{q}} _ {i + 1} + q _ {i} \overline {{p}} _ {i + 1} + q _ {i} \overline {{\partial}} p _ {i + 1} + q _ {i} \overline {{\partial}} p _ {i + 1} + q _ {i} \overline {{p}} _ {i + 1} + q _ {i} \overline {{p}} _ {i + 1} + q _ {i} \overline {{q}} _ {i + 1} + q _ {i} \overline {{p}} _ {i + 1} + q _ {i} \overline {{\partial}} p _ {i + 1} + q _ {i} \overline {{\partial}} p _ {i + 1} + q _ {i} \overline {{p}} _ {i + 1} + q _ {i} \overline {{p}}
