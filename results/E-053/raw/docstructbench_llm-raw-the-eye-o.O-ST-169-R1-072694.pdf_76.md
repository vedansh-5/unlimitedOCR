<|det|>title [85, 66, 321, 83]<|/det|>Result Parameter Details
<|det|>title [84, 90, 287, 105]<|/det|>Peripheral Control Status
<|det|>text [82, 106, 812, 196]<|/det|>The SMPC outputs the peripheral control status to the status register (SR) when the SMPC control mode is used. The status register (SR) is a register that can be read without regard for the INTBACK command. However, when the register is read when the INTBACK command is not in use, all bits except the RESB bit will be undefined.
<|det|>table [86, 238, 830, 639]<|/det|><table><tr><td rowspan="2">SR</td><td colspan="8">bit7</td><td>bit0</td></tr><tr><td>1</td><td>PDL</td><td>NPE</td><td>RESB</td><td>P2MD1</td><td>P2MD0</td><td>P1MD1</td><td>P1MD0</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>P1MD:</td><td>Port 1 Mode00: 15-byte mode (Returns peripheral data up to a maximum of 15 bytes.)01: 255-byte mode (Returns peripheral data up to a maximum of 255 bytes.)10: Unused11: 0-byte mode (Port is not accessed.)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>
<|det|>text [151, 384, 310, 397]<|/det|>P2MD: Port 2 Mode
<|det|>text [241, 404, 780, 418]<|/det|>00: 15-byte mode (Returns peripheral data up to a maximum of 15 bytes.)
<|det|>text [241, 419, 797, 433]<|/det|>01: 255-byte mode (Returns peripheral data up to a maximum of 255 bytes.)
<|det|>text [242, 433, 326, 445]<|/det|>10: Unused
<|det|>text [242, 446, 530, 460]<|/det|>11: 0-byte mode (Port is not accessed.)
<|det|>text [152, 460, 384, 473]<|/det|>RESB: Reset Button Status Bit
<|det|>text [241, 474, 402, 487]<|/det|>0: Reset Button OFF
<|det|>text [241, 488, 397, 500]<|/det|>1: Reset Button ON
<|det|>text [291, 502, 784, 528]<|/det|>Reading without regard for INTBACK command is possible. (Shows status for each V-BLANK-IN.)
<|det|>text [152, 530, 479, 544]<|/det|>NPE: Remaining Peripheral Existence Bit
<|det|>text [241, 544, 405, 558]<|/det|>0: No remaining data
<|det|>text [242, 558, 386, 572]<|/det|>1: Remaining data
<|det|>text [152, 572, 426, 585]<|/det|>PDL: Peripheral Data Location Bit
<|det|>text [241, 586, 481, 600]<|/det|>0: 2nd or above peripheral data
<|det|>text [241, 600, 407, 614]<|/det|>1: 1st peripheral data
<|det|>text [152, 614, 286, 628]<|/det|>bit7: Always 1
<|det|>image_caption [320, 675, 618, 692]<|/det|>Figure 3.13 Peripheral Control Status
<|det|>page_number [100, 933, 119, 945]<|/det|>66
