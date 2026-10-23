<|det|>page_number [910, 35, 921, 46]<|/det|>2
<|det|>text [100, 66, 490, 96]<|/det|>B4 For any continuous real-valued function \( f \) defined on the interval [0, 1], let
<|det|>equation [114, 106, 462, 164]<|/det|>\[
\begin{array}{l} \mu (f) = \int_ {0} ^ {1} f (x) d x, \operatorname{Var} (f) = \int_ {0} ^ {1} (f (x) - \mu (f)) ^ {2} d x, \\ M (f) = \max _ {0 \leq x \leq 1} | f (x) |. \\ \end{array}
\]
<|det|>text [124, 175, 490, 204]<|/det|>Show that if \( f \) and \( g \) are continuous real-valued functions defined on the interval [0, 1], then
<|det|>equation [145, 215, 432, 234]<|/det|>\[
\operatorname{Var} (f g) \leq 2 \operatorname{Var} (f) M (g) ^ {2} + 2 \operatorname{Var} (g) M (f) ^ {2}.
\]
<|det|>text [100, 250, 491, 327]<|/det|>B5 Let \( X = \{1,2,\ldots,n\} \), and let \( k \in X \). Show that there are exactly \( k \cdot n^{n-1} \) functions \( f: X \to X \) such that for every \( x \in X \) there is a \( j \geq 0 \) such that \( f^{(j)}(x) \leq k \). [Here \( f^{(j)} \) denotes the \( j^{\text{th}} \) iterate of \( f \), so that \( f^{(0)}(x) = x \) and \( f^{(j+1)}(x) = f(f^{(j)}(x)). \)]
<|det|>text [100, 335, 490, 366]<|/det|>B6 Let \( n \geq 1 \) be an odd integer. Alice and Bob play the following game, taking alternating turns, with Alice play-
<|det|>text [553, 66, 920, 111]<|/det|>ing first. The playing area consists of \( n \) spaces, arranged in a line. Initially all spaces are empty. At each turn, a player either
<|det|>text [576, 121, 830, 137]<|/det|>- places a stone in an empty space, or
<|det|>text [576, 141, 920, 212]<|/det|>- removes a stone from a nonempty space \( s \), places a stone in the nearest empty space to the left of \( s \) (if such a space exists), and places a stone in the nearest empty space to the right of \( s \) (if such a space exists).
<|det|>text [553, 222, 920, 296]<|/det|>Furthermore, a move is permitted only if the resulting position has not occurred previously in the game. A player loses if he or she is unable to move. Assuming that both players play optimally throughout the game, what moves may Alice make on her first turn?
