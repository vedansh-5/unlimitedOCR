<|det|>header [531, 44, 800, 62]<|/det|>2.7 Public Key Cryptography
<|det|>page_number [805, 45, 864, 60]<|/det|>79
<|det|>text [139, 84, 865, 121]<|/det|>Theorem 2.19 Let \( m \) be an integer that is the product of two prime numbers. The prime divisors of \( m \) are the roots of the quadratic equation
<|det|>equation [343, 130, 660, 152]<|/det|>\[
x ^ {2} - (m + 1 - \varphi (m)) x + m = 0,
\]
<|det|>text [140, 162, 616, 181]<|/det|>and so \(\varphi(m)\) determines the prime factors of \(m\).
<|det|>text [161, 192, 396, 211]<|/det|>Proof. If \( m = pq \), then
<|det|>equation [217, 218, 787, 255]<|/det|>\[
\varphi (m) = (p - 1) (q - 1) = p q - p - q + 1 = m - p - \frac {m}{p} + 1,
\]
<|det|>text [140, 263, 212, 279]<|/det|>and so
<|det|>equation [351, 275, 651, 311]<|/det|>\[
p - (m + 1 - \varphi (m)) + \frac {m}{p} = 0.
\]
<|det|>text [139, 314, 772, 333]<|/det|>Equivalently, \( p \) and \( q \) are the solutions of the quadratic equation
<|det|>equation [343, 341, 659, 363]<|/det|>\[
x ^ {2} - (m + 1 - \varphi (m)) x + m = 0.
\]
<|det|>text [140, 373, 419, 392]<|/det|>This completes the proof. \(\square\)
<|det|>text [160, 428, 852, 448]<|/det|>For example, if \( m = 221 \) and \( \varphi(m) = 192 \), then the quadratic equation
<|det|>equation [404, 455, 602, 476]<|/det|>\[
x ^ {2} - 3 0 x + 2 2 1 = 0
\]
<|det|>text [139, 487, 643, 505]<|/det|>has solutions \( x = 13 \) and \( x = 17 \), and \( 221 = 13 \cdot 17 \).
<|det|>text [138, 507, 865, 603]<|/det|>This method, known as the RSA cryptosystem, is called a public key cryptosystem, since the encryption key is made available to everyone, and the encrypted message can be transmitted through public channels. Only the possessor of the prime factors of m can decrypt the message. RSA is simple, but useful, and is the basis of many commercially valuable cryptosystems.
<|det|>title [142, 630, 252, 649]<|/det|>Exercises
<|det|>text [167, 660, 861, 717]<|/det|>1. Consider the secret key cryptosystem constructed from the prime \( p = 947 \) and the encoding key \( e = 167 \). Encipher the plaintext \( P = 2 \). Find a decrypting key and decipher the ciphertext \( C = 3 \).
<|det|>text [166, 728, 861, 786]<|/det|>2. Consider the primes \( p = 53 \) and \( q = 61 \). Let \( m = pq \). Prove that \( e = 7 \) is relatively prime to \( \varphi(m) \). Find a positive integer \( d \) such that \( ed \equiv 1 \pmod{\varphi(m)} \).
<|det|>text [166, 796, 861, 834]<|/det|>3. The integer 6059 is the product of two distinct primes, and \(\varphi(6059) = 5904\). Use Theorem 2.19 to compute the prime divisors of 6059.
<|det|>text [166, 845, 862, 942]<|/det|>4. The probability that an integer chosen at random between 1 and \( n \) is relatively prime to \( n \) is \( \varphi(n)/n \). Let \( n = pq \), where \( p \) and \( q \) are distinct primes greater than \( x \). Prove that the probability that a randomly chosen positive integer up to \( x \) is relatively prime to \( n \) is greater than \( (1 - 1/x)^2 \). If \( x = 200 \), this probability is greater than 0.99.
