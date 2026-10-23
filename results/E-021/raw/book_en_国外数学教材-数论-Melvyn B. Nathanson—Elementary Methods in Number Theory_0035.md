<|det|>header [307, 43, 800, 60]<|/det|>1.3 The Euclidean Algorithm and Continued Fractions
<|det|>page_number [805, 45, 826, 58]<|/det|>21
<|det|>text [140, 85, 186, 100]<|/det|>and
<|det|>equation [258, 99, 745, 141]<|/det|>\[
\frac {a}{b} = \frac {r _ {0}}{r _ {1}} = q _ {0} + \frac {r _ {2}}{r _ {1}} = q _ {0} + \frac {1}{\frac {r _ {1}}{r _ {2}}} = q _ {0} + \frac {1}{q _ {1}} = \langle q _ {0}, q _ {1} \rangle .
\]
<|det|>text [138, 149, 865, 227]<|/det|>Let \( n \geq 2 \), and assume that the theorem is true for integers \( a \) and \( b \geq 1 \) whose Euclidean algorithm has length \( n \). Let \( a \) and \( b \geq 1 \) be integers whose Euclidean algorithm has length \( n + 1 \) and whose sequence of partial quotients is \( \langle q_0, q_1, \ldots, q_n \rangle \). Let
<|det|>equation [400, 244, 576, 262]<|/det|>\[
r _ {0} = r _ {1} q _ {0} + r _ {2}
\]
<|det|>equation [402, 269, 574, 285]<|/det|>\[
r _ {1} = r _ {2} q _ {1} + r _ {3}
\]
<|det|>text [448, 298, 460, 314]<|/det|>:
<|det|>equation [377, 326, 624, 342]<|/det|>\[
r _ {n - 1} = r _ {n} q _ {n - 1} + r _ {n + 1}
\]
<|det|>equation [400, 350, 560, 366]<|/det|>\[
r _ {n} = r _ {n + 1} q _ {n}.
\]
<|det|>text [138, 384, 865, 459]<|/det|>be the  \( n + 1 \)  equations in the Euclidean algorithm for  \( a = r_{0} \)  and  \( b = r_{1} \) . The Euclidean algorithm for the positive integers  \( r_{1} \)  and  \( r_{2} \)  has length n with sequence of partial quotients  \( q_{1}, \ldots, q_{n} \) . It follows from the induction hypothesis that
<|det|>equation [418, 459, 586, 495]<|/det|>\[
\frac {r _ {1}}{r _ {2}} = \langle q _ {1}, \dots , q _ {n} \rangle
\]
<|det|>text [140, 502, 210, 518]<|/det|>and so
<|det|>equation [230, 530, 775, 575]<|/det|>\[
\frac {a}{b} = \frac {r _ {0}}{r _ {1}} = q _ {0} + \frac {1}{\frac {r _ {1}}{r _ {2}}} = q _ {0} + \frac {1}{\langle q _ {1} , \dots , q _ {n} \rangle} = \langle q _ {0}, q _ {1}, \dots , q _ {n} \rangle .
\]
<|det|>text [141, 588, 418, 608]<|/det|>This completes the proof.
<|det|>text [139, 643, 863, 681]<|/det|>It is also true that the representation of a rational number as a finite simple continued fraction is essentially unique (Exercise 8).
<|det|>title [143, 714, 252, 733]<|/det|>Exercises
<|det|>text [167, 744, 865, 802]<|/det|>1. Use the Euclidean algorithm to compute the greatest common divisor of 35 and 91, and to express (35, 91) as a linear combination of 35 and 91. Compute the simple continued fraction for 91/35.
<|det|>text [166, 816, 865, 874]<|/det|>2. Use the Euclidean algorithm to write the greatest common divisor of 4534 and 1876 as a linear combination of 4534 and 1876. Compute the simple continued fraction for 4534/1876.
<|det|>text [166, 888, 865, 944]<|/det|>3. Use the Euclidean algorithm to compute the greatest common divisor of 1197 and 14280, and to express (1197, 14280) as a linear combination of 1197 and 14280.
