<|det|>header [156, 51, 446, 68]<|/det|>【微信公众号：墨尘的数学笔记】
<|det|>text [148, 95, 616, 136]<|/det|>例4：已知数列 \(\{a_{n}\}\) 满足 \(a_1 = 2, a_{n + 1} = 2\left(1 + \frac{1}{n}\right)^2 a_n, n \in N_+\)
<|det|>text [155, 150, 657, 188]<|/det|>（1）求证：数列 \(\left\{\frac{a_n}{n^2}\right\}\) 是等比数列，并求出数列 \(\{a_n\}\) 的通项公式
<|det|>text [155, 206, 516, 242]<|/det|>(2) 设  \( c_{n}=\frac{n}{a_{n}} \) ，求证： \( c_{1}+c_{2}+\cdots+c_{n}<\frac{17}{24} \)
<|det|>text [148, 259, 497, 300]<|/det|>解：（1） \(a_{n + 1} = 2\left(1 + \frac{1}{n}\right)^2 a_n = 2\cdot \frac{(n + 1)^2}{n^2} a_n\)
<|det|>text [148, 315, 556, 354]<|/det|>\(\therefore \frac{a_{n + 1}}{(n + 1)^2} = 2 \cdot \frac{a_n}{n^2} \quad \therefore \left\{\frac{a_n}{n^2}\right\}\) 是公比为2的等比数列
<|det|>equation [150, 371, 331, 410]<|/det|>\[
\therefore \frac {a _ {n}}{n ^ {2}} = \left(\frac {a _ {1}}{1 ^ {2}}\right) \cdot 2 ^ {n - 1} = 2 ^ {n}
\]
<|det|>equation [150, 428, 256, 447]<|/det|>\[
\therefore a _ {n} = n ^ {2} \cdot 2 ^ {n}
\]
<|det|>text [148, 464, 848, 567]<|/det|>(2) 思路: \(c_{n} = \frac{n}{a_{n}} = \frac{1}{n \cdot 2^{n}}\), 无法直接求和, 所以考虑放缩成为可求和的通项公式 (不等号: <), 若要放缩为裂项相消的形式, 那么需要构造出 “顺序同构” 的特点。观察分母中有 \(n\), 故分子分母通乘以 \((n - 1)\), 再进行放缩调整为裂项相消形式。
<|det|>text [148, 584, 418, 622]<|/det|>解： \(c_{n} = \frac{n}{a_{n}} = \frac{1}{n\cdot 2^{n}} = \frac{n - 1}{n(n - 1)2^{n}}\)
<|det|>text [148, 640, 534, 680]<|/det|>而 \(\frac{1}{(n - 1)2^{n - 1}} -\frac{1}{n\cdot 2^n} = \frac{2n - (n - 1)}{n(n - 1)2^n} = \frac{n + 1}{n(n - 1)2^n}\)
<|det|>text [148, 696, 645, 734]<|/det|>所以 \(c_{n} = \frac{n - 1}{n(n - 1)2^{n}} < \frac{n + 1}{n(n - 1)2^{n}} = \frac{1}{(n - 1)2^{n - 1}} -\frac{1}{n\cdot 2^{n}} (n\geq 2)\)
<|det|>equation [150, 748, 828, 836]<|/det|>\[
\begin{array}{l} c _ {1} + c _ {2} + \dots + c _ {n} <   c _ {1} + c _ {2} + c _ {3} + \left(\frac {1}{3 \cdot 2 ^ {3}} - \frac {1}{4 \cdot 2 ^ {4}} + \frac {1}{4 \cdot 2 ^ {4}} - \frac {1}{5 \cdot 2 ^ {5}} + \dots + \frac {1}{(n - 1) 2 ^ {n - 1}} - \frac {1}{n \cdot 2 ^ {n}}\right) \\ = \frac {1}{2} + \frac {1}{8} + \frac {1}{2 4} + \frac {1}{2 4} - \frac {1 7}{n \cdot 2 ^ {n}} = \frac {1 7}{2 4} - \frac {1}{n \cdot 2 ^ {n}} <   \frac {1 7}{2 4} \quad (n > 3) \\ \because c _ {n} > 0 \quad \therefore c _ {1} <   c _ {1} + c _ {2} <   c _ {1} + c _ {2} + c _ {3} = \frac {1 6}{2 4} <   \frac {1 7}{2 4} \\ \end{array}
\]
<|det|>text [148, 879, 850, 895]<|/det|>小炼有话说：（1）本题先确定放缩的类型，向裂项相消放缩，从而按“依序同构”的目标进
