<|det|>header [679, 34, 891, 46]<|/det|>CHAPTER 29 MAGNETIC FIELDS
<|det|>page_number [903, 35, 930, 46]<|/det|>819
<|det|>aside_text [76, 72, 91, 160]<|/det|>Example 29.1 cont.
<|det|>text [104, 77, 701, 140]<|/det|>Model We are asked to find the magnetic field due to a simple current distribution, so this example is a typical problem for which the Biot–Savart law is appropriate. We must find the field contribution from a small element of current and then integrate over the current distribution from  \( \theta_{1} \)  to  \( \theta_{2} \) , as shown in Figure 29.3b.
<|det|>text [104, 148, 717, 255]<|/det|>Analyse Let's start by considering a length element \(d\vec{s}\) located a distance \(r\) from \(P\). The direction of the magnetic field at point \(P\) due to the current in this element is out of the page because \(d\vec{s} \times \hat{\mathbf{r}}\) is out of the page. In fact, because all the current elements \(Id\vec{s}\) lie in the plane of the page, they all produce a magnetic field directed out of the page at point \(P\). Therefore, the direction of the magnetic field at point \(P\) is out of the page and we need only find the magnitude of the field. We place the origin at \(O\) and let point \(P\) be along the positive \(y\) axis, with \(\hat{\mathbf{k}}\) being a unit vector pointing out of the page.
<|det|>text [104, 262, 715, 313]<|/det|>From the geometry in Figure 29.3a, we can see that the angle between the vectors \(d\vec{s}\) and \(\vec{r}\) is \(\left(\frac{\pi}{2} -\theta\right)\) radians.
<|det|>text [105, 314, 439, 328]<|/det|>Evaluate the cross product in the Biot-Savart law:
<|det|>equation [249, 340, 624, 376]<|/det|>\[
d \vec {\mathbf {s}} \times \hat {\mathbf {r}} = \left| d \vec {\mathbf {s}} \times \hat {\mathbf {r}} \right| \hat {\mathbf {k}} = \left[ d x \sin \left(\frac {\pi}{2} - \theta\right) \right] \hat {\mathbf {k}} = (d x \cos \theta) \hat {\mathbf {k}}
\]
<|det|>text [105, 387, 306, 401]<|/det|>Substitute into Equation 29.1:
<|det|>equation [341, 413, 710, 442]<|/det|>\[
d \vec {\mathbf {B}} = (d B) \hat {\mathbf {k}} = \frac {\mu_ {o} I}{4 \pi} \frac {d x \cos \theta}{r ^ {2}} \hat {\mathbf {k}} \tag {1}
\]
<|det|>text [105, 453, 501, 468]<|/det|>From the geometry in Figure 29.3a, express \( r \) in terms of \( \theta \):
<|det|>equation [407, 479, 710, 507]<|/det|>\[
r = \frac {a}{\cos \theta} \tag {2}
\]
<|det|>image [735, 85, 914, 230]<|/det|>
<|det|>image [735, 245, 915, 368]<|/det|>
<|det|>image_caption [735, 395, 911, 474]<|/det|>Figure 29.3
(Example 29.1) (a) A thin, straight wire carrying a current I (b) The angles  \( \theta_{1} \)  and  \( \theta_{2} \)  are used for determining the net field.
<|det|>text [104, 520, 911, 550]<|/det|>Notice that  \( \tan\theta = -x/a \)  from the right triangle in Figure 29.3a (the negative sign is necessary because  \( d\vec{s} \)  is located at a negative value of x) and solve for x:
<|det|>equation [468, 559, 559, 572]<|/det|>\[
x = - a \tan \theta
\]
<|det|>text [105, 582, 267, 596]<|/det|>Find the differential \(dx\):
<|det|>equation [422, 605, 916, 636]<|/det|>\[
d x = - a \sec^ {2} \theta d \theta = - \frac {a d \theta}{\cos^ {2} \theta} \tag {3}
\]
<|det|>text [105, 651, 644, 667]<|/det|>Substitute Equations (2) and (3) into the magnitude of the field from Equation (1):
<|det|>equation [342, 676, 916, 713]<|/det|>\[
d B = - \frac {\mu_ {o} I}{4 \pi} \left(\frac {a d \theta}{\cos^ {2} \theta}\right) \left(\frac {\cos^ {2} \theta}{a ^ {2}}\right) \cos \theta = - \frac {\mu_ {o} I}{4 \pi a} \cos \theta d \theta \tag {4}
\]
<|det|>text [104, 726, 905, 756]<|/det|>Integrate Equation (4) over all length elements on the wire, where the subtending angles range from \(\theta_{1}\) to \(\theta_{2}\) as defined in Figure 29.3b:
<|det|>equation [360, 764, 916, 797]<|/det|>\[
B = - \frac {\mu_ {o} I}{4 \pi a} \int_ {\theta_ {1}} ^ {\theta_ {2}} \cos \theta d \theta = \frac {\mu_ {o} I}{4 \pi a} (\sin \theta_ {1} - \sin \theta_ {2}) \tag {29.4}
\]
<|det|>text [105, 807, 617, 823]<|/det|>Check the dimensions, noting that the quantity in brackets is dimensionless:
<|det|>equation [350, 829, 677, 848]<|/det|>\[
[ \mathrm{MQ} ^ {- 1} \mathrm{T} ^ {- 1} ] = [ \mathrm{MLQ} ^ {- 2} ] [ \mathrm{QT} ^ {- 1} ] / [ \mathrm{L} ] = [ \mathrm{MQ} ^ {- 1} \mathrm{T} ^ {- 1} ] Ⓞ
\]
<|det|>text [105, 853, 664, 870]<|/det|>(B) Find an expression for the field at a point near a very long current-carrying wire.
<|det|>title [105, 887, 185, 901]<|/det|>Solution
<|det|>text [104, 903, 895, 936]<|/det|>We can use Equation 29.4 to find the magnetic field of any straight current-carrying wire if we know the geometry and hence the angles \(\theta_{1}\) and \(\theta_{2}\). If the wire in Figure 29.3b becomes infinitely long, we see that \(\theta_{1} = \pi / 2\) and \(\theta_{2} = -\pi / 2\) for
<|det|>footer [180, 964, 818, 977]<|/det|>Copyright 2017 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. WCN 02-300
