<|det|>header [797, 44, 867, 65]<|/det|>Full Paper
<|det|>header [871, 35, 905, 64]<|/det|>C
C T
<|det|>equation [88, 77, 490, 106]<|/det|>\[
\Lambda_ {\mathrm{r}} (\mathrm{r}) = \lambda_ {\mathrm{bed}} (\mathrm{r}) + \mathrm{K} _ {1} \mathrm{Pe} _ {0} \frac {\mathrm{u} _ {\mathrm{c}}}{\bar {\mathrm{u}} _ {0}} \mathrm{f} (\mathrm{R} - \mathrm{r}) \lambda_ {\mathrm{f}} \tag {17}
\]
<|det|>text [88, 110, 490, 156]<|/det|>The damping function  \( f(R-r) \)  remains the same as for the mass transfer (Eq.(11)), while the slope parameter and the damping parameter are slightly modified to, respectively,
<|det|>equation [89, 162, 490, 192]<|/det|>\[
\mathrm{K} _ {1} = \frac {1}{8} \tag {18}
\]
<|det|>equation [89, 206, 490, 238]<|/det|>\[
\mathrm{K} _ {2} = 0. 4 4 + 4 \exp \left(- \frac {\mathrm{Re} _ {0}}{7 0}\right) \tag {19}
\]
<|det|>text [87, 243, 491, 405]<|/det|>The heat release by adsorption, see [19] for  \( \Delta H_{ad} \) , is derived in the last term on the right-hand side of Eq.(14) from the change of solids load with time. This very term couples the energy with the mass balance, so that both have to be solved simultaneously in order to account for thermal effects. Heat transfer resistances to or in the particles are neglected. The terms  \( \delta_{\mathrm{bed}}(\mathbf{r}) \)  and  \( \lambda_{\mathrm{bed}}(\mathbf{r}) \)  in Eqs. (8), (10), (15) and (17) describe the isotropic effective diffusivity and thermal conductivity of the bed without fluid flow. Boundary and initial conditions for Eqs. (7) and (14) are recapitulated in Tab. 1.
<|det|>text [88, 406, 490, 480]<|/det|>On the basis of the above described general model various reductions are possible by neglecting thermal effects, the radial coordinate or gas-to-particle and intraparticle mass transfer resistances. From such reduced versions the following has been considered in more detail in the present work:
<|det|>text [89, 480, 490, 509]<|/det|>1) plug-flow model (1-D) with local equilibrium between the gas and the solids,
<|det|>text [88, 510, 490, 538]<|/det|>2) plug-flow model (1-D) with mass transfer resistance to the solids,
<|det|>text [88, 539, 440, 553]<|/det|>3) 2-D maldistribution model with local equilibrium,
<|det|>text [88, 554, 490, 581]<|/det|>4) 2-D maldistribution model with mass transfer resistance to the solids.
<|det|>text [87, 583, 490, 657]<|/det|>In our terminology “plug flow” means that every influence of the radial coordinate is neglected, including the influence of the wall on porosity and flow velocity. However, axial dispersion, as expressed by the dispersion coefficient  \( D_{ax} \) , is accounted for, so that the equation
<|det|>equation [88, 664, 490, 699]<|/det|>\[
\bar {\psi} \frac {\partial \mathrm{Y}}{\partial t} = \mathrm{D} _ {\mathrm{ax}} \frac {\partial^ {2} \mathrm{Y}}{\partial z ^ {2}} - \bar {\mathrm{u}} _ {0} \frac {\partial \mathrm{Y}}{\partial z} - [ 1 - \bar {\psi} ] \frac {\partial \mathrm{X}}{\partial t} \frac {\rho_ {\mathrm{p}}}{\rho_ {\mathrm{f}}} \tag {20}
\]
<|det|>text [88, 702, 493, 763]<|/det|>applies to the isothermal plug flow models (models 1 and 2). Eq. (20) is the classical, conventional way to model packed bed adsorbers. Local equilibrium corresponds, in terms of the two-layers model from [19], to the limiting case of \(\beta_{\mathrm{f}} \to \infty\)
<|det|>text [506, 82, 911, 184]<|/det|>and  \( \beta_{p} \rightarrow \infty \) . At this limit, equilibrium is considered to be sufficient for calculating the response of the solid phase to changes of the concentration in the fluid. Model 4 is our complete, highest order model, as previously outlined and in exact correspondence to [13–18]. Mainly this model has been evaluated for both isothermal and non-isothermal conditions.
<|det|>title [508, 214, 830, 230]<|/det|>4 Numerical Solution and its Validation
<|det|>text [506, 244, 911, 436]<|/det|>The partial differential equation or equations of the various models have been solved by the method of lines. The numerical calculations were conducted for different mesh densities, and the results accepted when the change of calculated gas moisture content values was lower than 0.05% of the maximal difference of gas moisture content appearing in the packed bed. When the error was bigger, the mesh was made denser. Since the width of the concentration front is, in many cases, not much smaller than the length of the bed, equidistant meshes have been used in the axial direction. In the maldistribution models (models 3 and 4 in the previous section) meshes that were denser near the wall than in the center of the tube have been applied.
<|det|>text [506, 436, 911, 569]<|/det|>To check the numerical procedure, respective results have been compared with available analytical solutions. One of such a solution is attributed to Anzelius [1] and refers to model 2 after the classification of section 3, additionally reduced by neglecting axial dispersion ( \( D_{ax} = 0 \) ). Furthermore, it is assumed that the sorption equilibrium is throughout linear (“Henry’s law”), and that the bed is long. The mass transfer resistance is attributed to the fluid phase. Then, axial profiles can be derived to
<|det|>equation [508, 576, 910, 607]<|/det|>\[
\frac {C}{C _ {\mathrm{in}}} = \frac {1}{2} \operatorname{erfc} \left(\sqrt {\xi} - \sqrt {\tau}\right) \tag {21}
\]
<|det|>text [508, 613, 544, 625]<|/det|>with
<|det|>equation [508, 633, 910, 667]<|/det|>\[
\xi = 6 \frac {\beta_ {\mathrm{f}}}{\mathrm{d} _ {\mathrm{p}} \mathrm{u}} \frac {\mathrm{z} 1 - \psi}{\psi} \tag {22}
\]
<|det|>text [509, 673, 537, 686]<|/det|>and
<|det|>equation [508, 694, 910, 726]<|/det|>\[
\tau = 6 \frac {\beta_ {\mathrm{f}}}{\mathrm{d} _ {\mathrm{p}} \mathrm{K}} \left(\mathrm{t} - \frac {\mathrm{z}}{\mathrm{u}}\right) \tag {23}
\]
<|det|>text [507, 731, 910, 761]<|/det|>In Eq. (21) the concentration of adsorbate in the gas phase, C, is used instead of the content, Y, assuming an ini-
<|det|>text [89, 780, 357, 792]<|/det|>Table 1. Boundary and initial conditions for models.
<|det|>table [90, 796, 911, 908]<|/det|><table><tr><td>t&gt;0</td><td>0≤ r≤ R</td><td>z=0</td><td>Y = Yin or u0(Yin - Y) = -Daxdy/Z</td><td>T = Tin</td></tr><tr><td></td><td></td><td>z = L</td><td>dy/Z= 0</td><td>dy/Z= 0</td></tr><tr><td>t&gt;0</td><td>0≤ z≤ L</td><td>r=0</td><td>dy/Z= 0</td><td>dy/Z= 0</td></tr><tr><td></td><td></td><td>r = R</td><td>dy/Z= 0</td><td>T = Tw</td></tr><tr><td>t=0</td><td>0≤ r≤ R</td><td>0≤ z≤ L</td><td>X(r,z) = X0</td><td>Y(r,z) = Y0</td></tr></table>
<|det|>footer [90, 932, 288, 945]<|/det|>Chem. Eng. Technol. 2004, 27, No. 11
<|det|>footer [316, 932, 450, 945]<|/det|>http://www.cet-journal.de
<|det|>footer [485, 932, 813, 945]<|/det|>© 2004 WILEY-VCH Verlag GmbH & Co. KGaA, Weinheim
<|det|>page_number [875, 931, 908, 944]<|/det|>1181
