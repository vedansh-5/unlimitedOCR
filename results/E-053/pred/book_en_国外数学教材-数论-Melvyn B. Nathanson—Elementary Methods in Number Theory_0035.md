1.3 The Euclidean Algorithm and Continued Fractions

21

and

\[
\frac {a}{b} = \frac {r _ {0}}{r _ {1}} = q _ {0} + \frac {r _ {2}}{r _ {1}} = q _ {0} + \frac {1}{\frac {r _ {1}}{r _ {2}}} = q _ {0} + \frac {1}{q _ {1}} = \langle q _ {0}, q _ {1} \rangle .
\]

Let \( n \geq 2 \), and assume that the theorem is true for integers \( a \) and \( b \geq 1 \) whose Euclidean algorithm has length \( n \). Let \( a \) and \( b \geq 1 \) be integers whose Euclidean algorithm has length \( n + 1 \) and whose sequence of partial quotients is \( \langle q_0, q_1, \ldots, q_n \rangle \). Let

\[
r _ {0} = r _ {1} q _ {0} + r _ {2}
\]

\[
r _ {1} = r _ {2} q _ {1} + r _ {3}
\]

:

\[
r _ {n - 1} = r _ {n} q _ {n - 1} + r _ {n + 1}
\]

\[
r _ {n} = r _ {n + 1} q _ {n}.
\]

be the  \( n + 1 \)  equations in the Euclidean algorithm for  \( a = r_{0} \)  and  \( b = r_{1} \) . The Euclidean algorithm for the positive integers  \( r_{1} \)  and  \( r_{2} \)  has length n with sequence of partial quotients  \( q_{1}, \ldots, q_{n} \) . It follows from the induction hypothesis that

\[
\frac {r _ {1}}{r _ {2}} = \langle q _ {1}, \dots , q _ {n} \rangle
\]

and so

\[
\frac {a}{b} = \frac {r _ {0}}{r _ {1}} = q _ {0} + \frac {1}{\frac {r _ {1}}{r _ {2}}} = q _ {0} + \frac {1}{\langle q _ {1} , \dots , q _ {n} \rangle} = \langle q _ {0}, q _ {1}, \dots , q _ {n} \rangle .
\]

This completes the proof.

It is also true that the representation of a rational number as a finite simple continued fraction is essentially unique (Exercise 8).

Exercises

1. Use the Euclidean algorithm to compute the greatest common divisor of 35 and 91, and to express (35, 91) as a linear combination of 35 and 91. Compute the simple continued fraction for 91/35.

2. Use the Euclidean algorithm to write the greatest common divisor of 4534 and 1876 as a linear combination of 4534 and 1876. Compute the simple continued fraction for 4534/1876.

3. Use the Euclidean algorithm to compute the greatest common divisor of 1197 and 14280, and to express (1197, 14280) as a linear combination of 1197 and 14280.
