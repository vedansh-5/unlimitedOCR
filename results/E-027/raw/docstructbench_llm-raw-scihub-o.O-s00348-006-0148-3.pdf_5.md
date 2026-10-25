<|det|>page_number [895, 32, 920, 44]<|/det|>283
<|det|>image_caption [76, 57, 278, 152]<|/det|>Fig. 2 Test images superimposed: in red the first, in green the second frame (left). The white square indicates the Interrogation Window. On the right the same image with a rectangular artificially saturated area on the first frame
<|det|>image [393, 58, 920, 259]<|/det|>
<|det|>image [188, 285, 382, 445]<|/det|>
<|det|>image [403, 286, 597, 444]<|/det|>
<|det|>image [618, 286, 812, 445]<|/det|>
<|det|>image_caption [75, 453, 493, 503]<|/det|>Fig. 3 Maps of dissimilarity with Lorentzian, sum of squared differences and fast correlation. Dissimilarity are subtracted of the minimum value and normalized by the maximum value. Contours are drawn from 0 to 1 with a step of 0.05. For reference, the levels
<|det|>image_caption [504, 453, 922, 503]<|/det|>0.7, 0.6 and 0.5 are drawn in red, green, and blue, respectively. The lowest the dissimilarity the darker the background. Abscissa and ordinate represent guessed displacement in the x and y direction, respectively
<|det|>image_caption [76, 526, 262, 576]<|/det|>Fig. 4 Dissimilarity maps on the modified image. Same contour lines and axes as in Fig. 3
<|det|>image [297, 526, 493, 688]<|/det|>
<|det|>image [511, 526, 707, 688]<|/det|>
<|det|>image [725, 526, 922, 688]<|/det|>
<|det|>text [75, 720, 490, 749]<|/det|>conservation by spurious pixels (outliers) between (e.g. the white square artificially added in the first frame).
<|det|>text [75, 749, 492, 879]<|/det|>The SSD and cross-correlation are functions defined univocally. Conversely, the Lorentzian depends on a parameter,  \( \sigma_{e} \) , which tunes how robust the estimator has to be. As a matter of fact, it should equal the amplitude of the expected differences between pixels fulfilling the BCC. The above maps have been computed with a value equal to 26, that is about one half of the standard deviation of the image gray levels ( \( \sigma = 43 \pm 0.1 \)  for both images).
<|det|>text [76, 880, 492, 910]<|/det|>In order to test the sensitivity of the solution on the parameter  \( \sigma_{e} \) , the dissimilarity map given by the
<|det|>text [503, 720, 922, 910]<|/det|>Lorentzian estimator was computed for six different values of  \( \sigma_{e} \) , ranging from 2 to 128; results are plotted in Fig. 5. If one assumes the level of the second peak as an indication of the signal to noise ratio, one should conclude that the values of 26 is not optimal, since the values from 3 up to 13 behaves slightly better, but the results are more or less similar to those obtained with 26. Further increases of the value deteriorate the S/N ratio, but also for  \( \sigma_{e} = 128 \) , the Lorentzian estimator works noticeably better than SSD or cross-correlation. These results indicate that the Lorentzian estimator performs well for a wide range of values of the parameter, even though the optimal seems to be at about 1/3 of the
