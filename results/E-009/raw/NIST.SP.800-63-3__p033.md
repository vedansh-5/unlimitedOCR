<|det|>header [114, 60, 252, 75]<|/det|>NIST SP 800-63-3
<|det|>header [677, 60, 884, 76]<|/det|>DIGITAL IDENTITY GUIDELINES
<|det|>text [112, 105, 842, 143]<|/det|>Authentication, proofing, and federation errors with potentially worse consequences require higher levels of assurance. Business process, policy, and technology may help reduce risk.
<|det|>text [113, 155, 431, 174]<|/det|>Categories of harm and impact include:
<|det|>text [143, 190, 655, 208]<|/det|>1. Inconvenience, distress, or damage to standing or reputation;
<|det|>text [143, 209, 440, 225]<|/det|>2. Financial loss or agency liability;
<|det|>text [143, 226, 533, 242]<|/det|>3. Harm to agency programs or public interests;
<|det|>text [143, 243, 541, 259]<|/det|>4. Unauthorized release of sensitive information;
<|det|>text [143, 261, 337, 277]<|/det|>5. Personal safety; and
<|det|>text [143, 278, 395, 294]<|/det|>6. Civil or criminal violations.
<|det|>text [112, 312, 851, 368]<|/det|>Required assurance levels for digital transactions are determined by assessing the potential impact of each of the above categories using the potential impact values described in Federal Information Processing Standard (FIPS) 199 [FIPS 199].
<|det|>text [113, 380, 415, 399]<|/det|>The three potential impact values are:
<|det|>text [143, 415, 277, 432]<|/det|>1. Low impact,
<|det|>text [143, 433, 350, 450]<|/det|>2. Moderate impact, and
<|det|>text [143, 451, 280, 468]<|/det|>3. High impact.
<|det|>title [113, 484, 531, 501]<|/det|>5.3.1 Business Process vs. Online Transaction
<|det|>text [111, 516, 875, 744]<|/det|>The assurance level determination is only based on transactions that are part of a digital system. An online transaction may not be equivalent to a complete business process that requires offline processing, or online processing in a completely segmented system. In selecting the appropriate assurance levels, the agency should assess the risk associated with online transactions they are offering via the digital service, not the entire business process associated with the provided benefit or service. For example, in an online survey, personal information may be collected, but it is never made available online to the submitter after the information is saved. In this instance, it is important for the information to be carefully protected in backend systems, but there is no reason to identity proof or even authenticate the user providing the information for the purposes of their own access to the system or its associated benefits. The online transaction is solely a submission of the data. The entire business process may require a significant amount of data validation, without ever needing to know if the correct person submitted the information. In this scenario, there is no need for any identity proofing nor authentication.
<|det|>text [111, 758, 885, 900]<|/det|>Another example where the assessed risk could differ if the agency evaluated the entire business process rather than the online transaction requirements is a digital service that accepts résumés to apply for open job postings. In this use case, the digital service allows an individual to submit – or at least does not restrict an individual from submitting – a résumé on behalf of anyone else, and in subsequent visits to the site, access the résumé for various purposes. Since the résumé information is available to the user in later sessions, and is likely to contain personal information, the agency must select an AAL that requires MFA, even though the user self-asserted the personal information. In this case, the requirements of [EO 13681] apply and the application
<|det|>page_number [488, 924, 511, 937]<|/det|>20
