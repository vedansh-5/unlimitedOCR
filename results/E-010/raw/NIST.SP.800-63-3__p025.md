<|det|>aside_text [23, 311, 38, 768]<|/det|>This publication is available free of charge from theutterer
<|det|>header [114, 60, 251, 74]<|/det|>NIST SP 800-63-3
<|det|>header [677, 60, 884, 75]<|/det|>DIGITAL IDENTITY GUIDELINES
<|det|>title [112, 104, 445, 123]<|/det|>4.2 Enrollment and Identity Proofing
<|det|>text [112, 136, 816, 155]<|/det|>Normative requirements can be found in SP 800-63A, Enrollment and Identity Proofing.
<|det|>text [111, 168, 882, 222]<|/det|>The previous section introduced the participants in the conceptual digital identity model. This section provides additional details regarding the participants' relationships and responsibilities in enrollment and identity proofing.
<|det|>text [111, 236, 862, 272]<|/det|>An individual, referred to as an applicant at this stage, opts to be identity proofed by a CSP. If the applicant is successfully proofed, the individual is then termed a subscriber of that CSP.
<|det|>text [111, 286, 880, 410]<|/det|>The CSP establishes a mechanism to uniquely identify each subscriber, register the subscriber's credentials, and track the authenticators issued to that subscriber. The subscriber may be given authenticators at the time of enrollment, the CSP may bind authenticators the subscriber already has, or they may be generated later as needed. Subscribers have a duty to maintain control of their authenticators and comply with CSP policies in order to maintain active authenticators. The CSP maintains enrollment records for each subscriber to allow recovery of authenticators, for example, when they are lost or stolen.
<|det|>title [112, 423, 527, 440]<|/det|>4.3 Authentication and Lifecycle Management
<|det|>text [111, 454, 772, 489]<|/det|>Normative requirements can be found in SP 800-63B, Authentication and Lifecycle Management.
<|det|>title [112, 503, 304, 519]<|/det|>4.3.1 Authenticators
<|det|>text [111, 535, 855, 569]<|/det|>The classic paradigm for authentication systems identifies three factors as the cornerstones of authentication:
<|det|>text [142, 588, 494, 605]<|/det|>• Something you know (e.g., a password).
<|det|>text [142, 606, 675, 623]<|/det|>• Something you have (e.g., an ID badge or a cryptographic key).
<|det|>text [142, 624, 668, 641]<|/det|>• Something you are (e.g., a fingerprint or other biometric data).
<|det|>text [111, 658, 878, 780]<|/det|>MFA refers to the use of more than one of the above factors. The strength of authentication systems is largely determined by the number of factors incorporated by the system — the more factors employed, the more robust the authentication system. For the purposes of these guidelines, using two factors is adequate to meet the highest security requirements. As discussed in Section 5.1, other types of information, such as location data or device identity, may be used by an RP or verifier to evaluate the risk in a claimed identity, but they are not considered authentication factors.
<|det|>text [111, 795, 882, 883]<|/det|>In digital authentication the claimant possesses and controls one or more authenticators that have been registered with the CSP and are used to prove the claimant's identity. The authenticator(s) contains secrets the claimant can use to prove that he or she is a valid subscriber, the claimant authenticates to a system or application over a network by proving that he or she has possession and control of one or more authenticators.
<|det|>aside_text [31, 311, 48, 768]<|/det|>This publication is available free of charge from https://doi.org/10.6028/NIST.SP 800-23-0033
<|det|>page_number [490, 924, 510, 937]<|/det|>12
