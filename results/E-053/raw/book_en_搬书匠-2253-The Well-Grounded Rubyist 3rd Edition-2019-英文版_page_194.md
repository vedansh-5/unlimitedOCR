<|det|>header [416, 37, 601, 51]<|/det|>Conditional code execution
<|det|>page_number [864, 37, 893, 50]<|/det|>165
<|det|>equation [186, 75, 524, 109]<|/det|>\[
\begin{array}{l} \text { >>   end } \\ = > \text { nil } \end{array} \quad \begin{array}{l} \text { Entire   if   statement   evaluates } \\ = > \text { nil } \end{array}
\]
<|det|>text [185, 119, 895, 196]<|/det|>Conditional statements interact with other aspects of Ruby syntax in a couple of ways that you need to be aware of—in particular, with assignment syntax. It’s worth looking in some detail at how conditionals behave in assignments, because it involves some interesting points about how Ruby parses code.
<|det|>title [119, 211, 616, 229]<|/det|>6.1.2 Assignment syntax in condition bodies and tests
<|det|>text [185, 237, 895, 292]<|/det|>Assignment syntax and conditional expressions cross paths at two points: in the bodies of conditional expressions, where the assignments may or may not happen at all, and in the conditional tests themselves:
<|det|>equation [186, 303, 548, 349]<|/det|>\[
\begin{array}{l} \text {if} x = 1 \quad \triangleleft \text {Assignment in conditional} \\ \mathrm{y} = 2 \quad \triangleleft \text {Assignment in conditional} \\ \text {end} \end{array}
\]
<|det|>text [185, 359, 895, 416]<|/det|>What happens (or doesn't) when you use these idioms? We'll look at both, starting with variable assignment in the body of the conditional—specifically, local-variable assignment, which displays some perhaps unexpected behavior in this context.
<|det|>title [186, 426, 571, 440]<|/det|>LOCAL-VARIABLE ASSIGNMENT IN A CONDITIONAL BODY
<|det|>text [185, 443, 895, 517]<|/det|>Ruby doesn't draw as clear a line as compiled languages do between "compile time" and "runtime," but the interpreter does parse your code before running it, and certain decisions are made during that process. An important one is the recognition and allocation of local variables.
<|det|>text [186, 521, 894, 557]<|/det|>When the Ruby parser sees the sequence identifier, equal-sign, and value, as in this expression,
<|det|>equation [186, 573, 238, 586]<|/det|>\[
x = 1
\]
<|det|>text [185, 599, 894, 656]<|/det|>it allocates space for a local variable called x. The creation of the variable—not the assignment of a value to it, but the internal creation of a variable—always takes place as a result of this kind of expression, even if the code isn't executed!
<|det|>text [215, 658, 409, 675]<|/det|>Consider this example:
<|det|>text [186, 686, 562, 761]<|/det|>if false
    x = 1    Output: nil
end
p x    NameError: undefined local
p y    variable or method 'y'
<|det|>text [185, 773, 895, 849]<|/det|>The assignment to x isn't executed, because it's wrapped in a failing conditional test. But the Ruby parser sees the sequence x = 1, from which it deduces that the program involves a local variable x. The parser doesn't care whether x is ever assigned a value. Its job is just to scour the code for local variables for which space needs to be allocated.
<|det|>text [185, 851, 895, 909]<|/det|>The result is that x inhabits a strange kind of variable limbo. It has been brought into being and initialized to nil. In that respect, it differs from a variable that has no existence at all; as you can see in the example, examining x gives you the value nil,
