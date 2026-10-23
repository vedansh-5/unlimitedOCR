<|det|>image [370, 94, 631, 220]<|/det|>
<|det|>image_caption [138, 233, 719, 253]<|/det|>Figure 11-4. High-side Switching with an NPN BJT Driving a PNP BJT
<|det|>text [137, 270, 862, 330]<|/det|>Low-side switching (Recipe 11.1) is the most common and simplest arrangement, and unless you have a good reason such as the need for one end of the load to be connected to ground, you should use low-side switching.
<|det|>title [138, 345, 230, 367]<|/det|>See Also
<|det|>text [138, 377, 714, 397]<|/det|>For a discussion of NPN and PNP bipolar transistors, see Recipe 5.1.
<|det|>text [138, 405, 670, 424]<|/det|>GPIO ports and their output logic are described in Recipe 10.7.
<|det|>text [138, 433, 859, 471]<|/det|>You will find an example of switching with a transistor using an Arduino in Recipe 11.6 and for a Raspberry Pi in Recipe 11.7.
<|det|>text [138, 480, 545, 500]<|/det|>For switching using a MOSFET, see Recipe 11.3.
<|det|>title [139, 518, 517, 546]<|/det|>11.3 Switch Much More Power
<|det|>title [138, 562, 233, 586]<|/det|>Problem
<|det|>text [137, 595, 860, 634]<|/det|>You want to allow a GPIO pin to control more power than it otherwise could, but a BJT isn't enough.
<|det|>title [138, 651, 231, 673]<|/det|>Solution
<|det|>text [137, 683, 860, 741]<|/det|>You can use a MOSFET as an electronic switch. Use the transistor in a common-source arrangement. Figure 11-5 shows the schematic for this circuit. Along with Recipe 11.1, you will find yourself using this circuit a lot.
<|det|>text [137, 750, 859, 788]<|/det|>This type of switching is called “low-side” switching because the transistor acts as a switch between the low voltage of GND and the load.
<|det|>text [137, 797, 860, 854]<|/det|>If the GPIO pin is high (3.3V or 5V) and exceeds the gate-threshold voltage of the MOSFET, the MOSFET will turn on, allowing current to flow from +V through the load to GND.
<|det|>footer [617, 923, 799, 939]<|/det|>11.3 Switch Much More Power
<|det|>page_number [833, 923, 858, 937]<|/det|>173
