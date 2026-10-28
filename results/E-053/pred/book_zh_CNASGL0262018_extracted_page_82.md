CNAS-GL026:2018

第81页共114页

-EUT与频谱分析仪之间的链路S参数0.724(m)，损耗2.8dB(d)则

\[
u _ {\mathrm{EUT-功分器}} = \frac {0 . 7 \times 0 . 0 9 9 \times 1 0 0}{\sqrt {2} \times 1 1 . 5} = 0. 4 2 6 \mathrm{dB}
\]

\[
u _ {\text {功分器 - 衰减网络}} = \frac {0 . 0 9 9 \times 0 . 3 3 3 \times 1 0 0}{\sqrt {2} \times 1 1 . 5} = 0. 2 0 3 \mathrm{dB}
\]

\[
u _ {\text {衰减网络 - 频谱仪}} = \frac {0 . 3 3 3 \times 0 . 0 9 1 \times 1 0 0}{\sqrt {2} \times 1 1 . 5} = 0. 1 8 6 \mathrm{dB}
\]

\[
u _ {\mathrm{EUT-衰减网络}} = \frac {0 . 7 \times 0 . 3 3 3 \times 0 . 9 1 2 \times 0 . 9 1 2 \times 1 0 0}{\sqrt {2} \times 1 1 . 5} = 1. 1 9 2 \mathrm{dB}
\]

\[
u _ {\text {功分器 - 频谱仪}} = \frac {0 . 0 9 9 \times 0 . 3 3 3 \times 0 . 7 9 4 \times 0 . 7 9 4 \times 1 0 0}{\sqrt {2} \times 1 1 . 5} = 0. 1 2 8 \mathrm{dB}
\]

\[
u _ {\mathrm{EIT-频谱仪}} = \frac {0 . 7 \times 0 . 0 9 1 \times 0 . 7 2 4 \times 0 . 7 2 4 \times 1 0 0}{\sqrt {2} \times 1 1 . 5} = 0. 2 0 5 \mathrm{dB}
\]

则 \(u(\delta P_M) = \sqrt{0.426^2 + 0.203^2 + 0.186^2 + 1.192^2 + 0.128^2 + 0.205^2} = 1.318\mathrm{dB}\)

5.5.3.5 被测样供电电压变化引入的不确定度分量 \(u(\delta P_{v})\)

在测试期间，实验室供电电压可控范围为 \(0.1\mathrm{V}\)，根据ETSI TR 100 028 表F.1-均值 \(10\% (\mathrm{p}) / \mathrm{V}\)

- 标准差 3%(p)/V

\[
u (\delta P _ {r}) = = \frac {0 . 1 V \times \sqrt {(10 \% / V) ^ {2} + (3 \% / V) ^ {2}}}{\sqrt {3} \times 2 3 . 0} = 0. 0 2 6 \mathrm{dB}
\]

5.5.3.6 时间周期变化引入的不确定度分量 \( u(\delta P_{D}) \)

根据 ETSI TR 100 028 表 F.1，时间周期误差为 2%(d)(p)(σ)

\[
u (\delta P _ {D}) = = \frac {2 \%}{23.0} = 0.087 \mathrm{dB}
\]

5.5.4 不确定度概算

表 5-10 传导杂散发射测量不确定度概算表

<table><tr><td>分量</td><td>概率分布</td><td>灵敏系数</td><td>不确定度分量值(dB)</td></tr></table>

2018年03月01日发布

2018年09月01日实施
