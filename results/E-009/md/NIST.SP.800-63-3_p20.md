Withdrawn NIST Technical Series Publication

<table><tr><td colspan="2">Warning NoticeThe attached publication has been withdrawn (archived), and is provided solely for historical purposes. It may have been superseded by another publication (indicated below).</td></tr><tr><td colspan="2">Withdrawn Publication</td></tr><tr><td>Series/Number</td><td>NIST Special Publication 800-63-3</td></tr><tr><td>Title</td><td>Digital Identity Guidelines</td></tr><tr><td>Publication Date(s)</td><td>June 2017 (includes updates as of 03-02-2020)</td></tr><tr><td>Withdrawal Date</td><td>August 1, 2025</td></tr><tr><td>Withdrawal Note</td><td>NIST SP 800-63-3 is withdrawn and superseded in its entirety by NIST SP 800-63-4.</td></tr><tr><td colspan="2">Superseding Publication(s) (if applicable)</td></tr><tr><td colspan="2">The attached publication has been superseded by the following publication(s):</td></tr><tr><td>Series/Number</td><td>NIST SP 800-63-4</td></tr><tr><td>Title</td><td>Digital Identity Guidelines</td></tr><tr><td>Author(s)</td><td>David Temoshok, et al.</td></tr><tr><td>Publication Date(s)</td><td>July 2025</td></tr><tr><td>URL/DOI</td><td>https://doi.org/10.6028/NIST.SP.800-63-4</td></tr><tr><td colspan="2">Additional Information (if applicable)</td></tr><tr><td>Contact</td><td>Applied Cybersecurity Division (Information Technology Laboratory)</td></tr><tr><td>Latest revision of the attached publication</td><td></td></tr><tr><td>Related Information</td><td>https://csrc.nist.gov/pubs/sp/800/63/4/finalhttps://www.nist.gov/identity-access-management/nist-special-publication-800-63-digital-identity-guidelines</td></tr><tr><td>WithdrawalAnnouncement Link</td><td></td></tr></table>

Date updated: July 24, 2025

NIST

NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY U.S. DEPARTMENT OF COMMERCE

NIST Special Publication 800-63-3

Digital Identity Guidelines

Paul A. Grassi

Michael E. Garcia

James L. Fenton

This publication is available free of charge from:

https://doi.org/10.6028/NIST.SP.800-63-3

NIST

National Institute of

Standards and Technology

U.S. Department of Commerce

NIST Special Publication 800-63-3

Digital Identity Guidelines

Paul A. Grassi

Michael E. Garcia

Applied Cybersecurity Division

Information Technology Laboratory

James L. Fenton

Altmode Networks

Los Altos, Calif.

This publication is available free of charge from:

https://doi.org/10.6028/NIST.SP.800-63-3

June 2017

INCLUDES UPDATES AS OF 03-02-2020; PAGE X

U.S. Department of Commerce

Wilbur L. Ross, Jr., Secretary

National Institute of Standards and Technology

Kent Rochford, Acting NIST Director and Under Secretary of Commerce for Standards and Technology

Authority

This publication has been developed by NIST in accordance with its statutory responsibilities under the Federal Information Security Modernization Act (FISMA) of 2014, 44 U.S.C. § 3551 et seq., Public Law (P.L.) 113-283. NIST is responsible for developing information security standards and guidelines, including minimum requirements for federal information systems, but such standards and guidelines shall not apply to national security systems without the express approval of appropriate federal officials exercising policy authority over such systems. This guideline is consistent with the requirements of the Office of Management and Budget (OMB) Circular A-130.

Nothing in this publication should be taken to contradict the standards and guidelines made mandatory and binding on federal agencies by the Secretary of Commerce under statutory authority. Nor should these guidelines be interpreted as altering or superseding the existing authorities of the Secretary of Commerce, Director of the OMB, or any other federal official. This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST.

National Institute of Standards and Technology Special Publication 800-63-3
Natl. Inst. Stand. Technol. Spec. Publ. 800-63-3, 75 pages (June 2017)
CODEN: NSPUE2

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63-3

Certain commercial entities, equipment, or materials may be identified in this document in order to describe an experimental procedure or concept adequately. Such identification is not intended to imply recommendation or endorsement by NIST, nor is it intended to imply that the entities, materials, or equipment are necessarily the best available for the purpose.

There may be references in this publication to other publications currently under development by NIST in accordance with its assigned statutory responsibilities. The information in this publication, including concepts and methodologies, may be used by federal agencies even before the completion of such companion publications. Thus, until each publication is completed, current requirements, guidelines, and procedures, where they exist, remain operative. For planning and transition purposes, federal agencies may wish to closely follow the development of these new publications by NIST.

Organizations are encouraged to review all draft publications during public comment periods and provide feedback to NIST. Many NIST cybersecurity publications, other than the ones noted above, are available at http://csrc.nist.gov/publications.

Comments on this publication may be submitted to:

National Institute of Standards and Technology
Attn: Applied Cybersecurity Division, Information Technology Laboratory
100 Bureau Drive (Mail Stop 2000) Gaithersburg, MD 20899-2000
Email: dig-comments@nist.gov

All comments are subject to release under the Freedom of Information Act (FOIA).

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

Reports on Computer Systems Technology

The Information Technology Laboratory (ITL) at the National Institute of Standards and Technology (NIST) promotes the U.S. economy and public welfare by providing technical leadership for the Nation's measurement and standards infrastructure. ITL develops tests, test methods, reference data, proof of concept implementations, and technical analyses to advance the development and productive use of information technology. ITL's responsibilities include the development of management, administrative, technical, and physical standards and guidelines for the cost-effective security and privacy of other than national security-related information in federal information systems. The Special Publication 800-series reports on ITL's research, guidelines, and outreach efforts in information system security, and its collaborative activities with industry, government, and academic organizations.

ii

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63-3

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

Abstract

These guidelines provide technical requirements for federal agencies implementing digital identity services and are not intended to constrain the development or use of standards outside of this purpose. The guidelines cover identity proofing and authentication of users (such as employees, contractors, or private individuals) interacting with government IT systems over open networks. They define technical requirements in each of the areas of identity proofing, registration, authenticators, management processes, authentication protocols, federation, and related assertions. This publication supersedes NIST Special Publication 800-63-2.

Keywords

authentication; authentication assurance; authenticator; assertions; credential service provider; digital authentication; digital credentials; identity proofing; federation; passwords; PKI.

Acknowledgments

The authors gratefully acknowledge Kaitlin Boeckl for her artistic graphics contributions to all volumes in the SP 800-63 suite and the contributions of our many reviewers, including Joni Brennan from the Digital ID & Authentication Council of Canada (DIACC), Ellen Nadeau and Ben Piccarreta from NIST, and Danna Gabel O'Rourke from Deloitte & Touche LLP.

In addition, the authors would like to acknowledge the thought leadership and innovation of the original authors: Donna F. Dodson, Elaine M. Newton, Ray A. Perlner, W. Timothy Polk, Sarbari Gupta, and Emad A. Nabbus. Without their tireless efforts, we would not have had the incredible baseline from which to evolve SP 800-63 to the document it is today.

Requirements Notation and Conventions

The terms “SHALL” and “SHALL NOT” indicate requirements to be followed strictly in order to conform to the publication and from which no deviation is permitted.

The terms “SHOULD” and “SHOULD NOT” indicate that among several possibilities one is recommended as particularly suitable, without mentioning or excluding others, or that a certain course of action is preferred but not necessarily required, or that (in the negative form) a certain possibility or course of action is discouraged but not prohibited.

The terms “MAY” and “NEED NOT” indicate a course of action permissible within the limits of the publication.

The terms “CAN” and “CANNOT” indicate a possibility and capability, whether material, physical or causal or, in the negative, the absence of that possibility or capability.

iii

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

Executive Summary

This section is informative.

Digital identity is the online persona of a subject, and a single definition is widely debated internationally. The term persona is apropos as a subject can represent themselves online in many ways. An individual may have a digital identity for email, and another for personal finances. A personal laptop can be someone's streaming music server yet also be a worker-bot in a distributed network of computers performing complex genome calculations. Without context, it is difficult to land on a single definition that satisfies all.

Digital identity as a legal identity further complicates the definition and ability to use digital identities across a range of social and economic use cases. Digital identity is hard. Proving someone is who they say they are — especially remotely, via a digital service — is fraught with opportunities for an attacker to successfully impersonate someone. As correctly captured by Peter Steiner in The New Yorker, “On the internet, nobody knows you’re a dog.” These guidelines provide mitigations to the vulnerabilities inherent online, while recognizing and encouraging that when accessing some low-risk digital services, “being a dog” is just fine; while other, high-risk services need a level of confidence that the digital identity accessing the service is the legitimate proxy to the real-life subject.

For these guidelines, digital identity is the unique representation of a subject engaged in an online transaction. A digital identity is always unique in the context of a digital service, but does not necessarily need to uniquely identify the subject in all contexts. In other words, accessing a digital service may not mean that the subject's real-life identity is known.

Identity proofing establishes that a subject is who they claim to be. Digital authentication establishes that a subject attempting to access a digital service is in control of one or more valid authenticators associated with that subject's digital identity. For services in which return visits are applicable, successfully authenticating provides reasonable risk-based assurances that the subject accessing the service today is the same as that which accessed the service previously. Digital identity presents a technical challenge because this process often involves proofing individuals over an open network, and always involves the authentication of individual subjects over an open network to access digital government services. The processes and technologies to establish and use digital identities offer multiple opportunities for impersonation and other attacks.

These technical guidelines supersede NIST Special Publication SP 800-63-2. Agencies use these guidelines as part of the risk assessment and implementation of their digital service(s). These guidelines provide mitigations of an authentication error's negative impacts by separating the individual elements of identity assurance into discrete, component parts. For non-federated systems, agencies will select two components, referred to as Identity Assurance Level (IAL) and Authenticator Assurance Level (AAL). For federated systems, agencies will select a third component, Federation Assurance Level (FAL).

iv

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

These guidelines retire the concept of a level of assurance (LOA) as a single ordinal that drives implementation-specific requirements. Rather, by combining appropriate business and privacy risk management side-by-side with mission need, agencies will select IAL, AAL, and FAL as distinct options. While many systems will have the same numerical level for each of IAL, AAL, and FAL, this is not a requirement and agencies should not assume they will be the same in any given system.

The components of identity assurance detailed in these guidelines are as follows:

• IAL refers to the identity proofing process.

• AAL refers to the authentication process.

- FAL refers to the strength of an assertion in a federated environment, used to communicate authentication and attribute information (if applicable) to a relying party (RP).

The separation of these categories provides agencies flexibility in choosing identity solutions and increases the ability to include privacy-enhancing techniques as fundamental elements of identity systems at any assurance level. For example, these guidelines support scenarios that will allow pseudonymous interactions even when strong, multi-factor authenticators are used. In addition, these guidelines encourage minimizing the dissemination of identifying information by requiring federated identity providers (IdPs) to support a range of options for querying data, such as asserting whether an individual is older than a certain age rather than querying the entire date of birth. While many agency use cases will require individuals to be fully identified, these guidelines encourage pseudonymous access to government digital services wherever possible and, even where full identification is necessary, limiting the amount of personal information collected as much as possible.

In today's environment, an organization's identity solution need not be a monolith, where one system or vendor provides all functionality. The market for identity services is componentized, allowing organizations and agencies to employ standards-based, pluggable identity solutions based on mission need. As such, SP 800-63 has been split into a suite of documents. The suite as a whole is referred to as “the guidelines,” with the individual documents referred to as “volumes.” RPs are required to use SP 800-63; the remaining volumes may be used independently or in an integrated fashion, depending on the component service(s) an agency requires.

Each volume has adopted verbs that are internationally recognized in standards organizations as normative and requirements-based. When used in a normative statement in these guidelines, they are CAPITALIZED for ease of identification. For example, SHALL is used to denote a mandatory requirement, while SHOULD refers to a technique, technology, or process that is recommended but not mandatory. For more details on the definitions of these terms see the Requirements Notation and Conventions at the beginning of each document.

These documents may inform — but do not restrict or constrain — the development or use of standards for application outside the federal government, such as e-commerce transactions.

V

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63-3

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

These guidelines are organized as follows:

SP 800-63 Digital Identity Guidelines (This document)

SP 800-63 provides an overview of general identity frameworks, using authenticators, credentials, and assertions together in a digital system, and a risk-based process of selecting assurance levels. SP 800-63 contains both normative and informative material.

SP 800-63A Enrollment and Identity Proofing

NIST SP 800-63-A addresses how applicants can prove their identities and become enrolled as valid subscribers within an identity system. It provides requirements by which applicants can both identity proof and enroll at one of three different levels of risk mitigation in both remote and physically-present scenarios. SP 800-63A contains both normative and informative material.

SP 800-63A sets requirements to achieve a given IAL. The three IALs reflect the options agencies may select from based on their risk profile and the potential harm caused by an attacker making a successful false claim of an identity. The IALs are as follows:

IAL1: There is no requirement to link the applicant to a specific real-life identity. Any attributes provided in conjunction with the authentication process are self-asserted or should be treated as such (including attributes a Credential Service Provider, or CSP, asserts to an RP).

IAL2: Evidence supports the real-world existence of the claimed identity and verifies that the applicant is appropriately associated with this real-world identity. IAL2 introduces the need for either remote or physically-present identity proofing. Attributes can be asserted by CSPs to RPs in support of pseudonymous identity with verified attributes.

IAL3: Physical presence is required for identity proofing. Identifying attributes must be verified by an authorized and trained representative of the CSP. As with IAL2, attributes can be asserted by CSPs to RPs in support of pseudonymous identity with verified attributes.

SP 800-63B Authentication and Lifecycle Management

For services in which return visits are applicable, a successful authentication provides reasonable risk-based assurances that the subscriber accessing the service today is the same as that which accessed the service previously. The robustness of this confidence is described by an AAL categorization. NIST SP 800-63B addresses how an individual can securely authenticate to a CSP to access a digital service or set of digital services. SP 800-63B contains both normative and informative material.

The three AALs define the subsets of options agencies can select based on their risk profile and the potential harm caused by an attacker taking control of an authenticator and accessing agencies' systems. The AALs are as follows:

AAL1: AAL1 provides some assurance that the claimant controls an authenticator bound to the subscriber's account. AAL1 requires either single-factor or multi-factor authentication using a

vi

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63-3

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

wide range of available authentication technologies. Successful authentication requires that the claimant prove possession and control of the authenticator through a secure authentication protocol.

AAL2: AAL2 provides high confidence that the claimant controls authenticator(s) bound to the subscriber's account. Proof of possession and control of two distinct authentication factors is required through secure authentication protocol(s). Approved cryptographic techniques are required at AAL2 and above.

AAL3: AAL3 provides very high confidence that the claimant controls authenticator(s) bound to the subscriber's account. Authentication at AAL3 is based on proof of possession of a key through a cryptographic protocol. AAL3 authentication SHALL use a hardware-based authenticator and an authenticator that provides verifier impersonation resistance; the same device MAY fulfill both these requirements. In order to authenticate at AAL3, claimants SHALL prove possession and control of two distinct authentication factors through secure authentication protocol(s). Approved cryptographic techniques are required.

SP 800-63C Federation and Assertions

NIST SP 800-63C provides requirements when using federated identity architectures and assertions to convey the results of authentication processes and relevant identity information to an agency application. In addition, this volume offers privacy-enhancing techniques to share information about a valid, authenticated subject and describes methods that allow for strong multi-factor authentication (MFA) while the subject remains pseudonymous to the digital service. SP 800-63C contains both normative and informative material.

The three FALs reflect the options agencies can select based on their risk profile and the potential harm caused by an attacker taking control of federated transactions. The FALs are as follows:

FAL1: Allows for the subscriber to enable the RP to receive a bearer assertion. The assertion is signed by the IdP using approved cryptography.

FAL2: Adds the requirement that the assertion be encrypted using approved cryptography such that the RP is the only party that can decrypt it.

FAL3: Requires the subscriber to present proof of possession of a cryptographic key referenced in the assertion in addition to the assertion artifact itself. The assertion is signed by the IdP and encrypted to the RP using approved cryptography.

These guidelines are agnostic to the vast array of identity service architectures that agencies can develop or acquire, and are meant to be applicable regardless of the approach an agency selects. However, agencies are encouraged to use federation where possible, and the ability to mix and match IAL, AAL, and FAL is simplified when federated architectures are used. Furthermore, federation is a keystone in the ability to enhance the privacy of the federal government's constituents as they access valuable government digital services.

vii

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63-3

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

Table of Contents

Executive Summary ...... iv

1 Purpose....1

2 Introduction....2

2.1 Applicability....4

2.2 Considerations, Other Requirements, and Flexibilities .... 5

2.3 A Few Limitations.... 5

2.4 How to Use this Suite of SPs....5

2.5 Change History....6

2.5.1 SP 800-63-1 6

2.5.2 SP 800-63-2....6

2.5.3 SP 800-63-3....6

3 Definitions and Abbreviations 8

4 Digital Identity Model....9

4.1 Overview....9

4.2 Enrollment and Identity Proofing....12

4.3 Authentication and Lifecycle Management 12

4.3.1 Authenticators 12

4.3.2 Credentials 14

4.3.3 Authentication Process....14

4.4 Federation and Assertions....14

4.4.1 Assertions....15

4.4.2 Relying Parties 16

5 Digital Identity Risk Management....17

5.1 Overview....17

5.2 Assurance Levels....18

5.3 Risk and Impacts 19

5.3.1 Business Process vs. Online Transaction 20

5.3.2 Impacts per Category 21

5.4 Risk Acceptance and Compensating Controls....22

5.5 Digital Identity Acceptance Statement 23

5.6 Migrating Identities....23

viii

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63-3

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

6 Selecting Assurance Levels....25

6.1 Selecting IAL....26

6.2 Selecting AAL 29

6.3 Selecting FAL....31

6.4 Combining xALS....33

7 Federation Considerations....35

8 References....36

8.1 General References....36

8.2 Standards 37

8.3 NIST Special Publications....37

8.4 Federal Information Processing Standards....37

List of Appendices

Appendix A— Definitions and Abbreviations .... 39

A.1 Definitions....39

A.2 Abbreviations....58

List of Figures

Figure 4-1 Digital Identity Model....10

Figure 6-1 Selecting IAL....27

Figure 6-2 Selecting AAL .... 30

Figure 6-3 Selecting FAL....32

List of Tables

Table 2-1 Normative and Informative Sections of SP 800-63-3....4

Table 5-1 Identity Assurance Levels .... 18

Table 5-2 Authenticator Assurance Levels....19

Table 5-3 Federation Assurance Levels....19

Table 6-1 Maximum Potential Impacts for Each Assurance Level....25

Table 6-2 Acceptable Combinations of IAL and AAL....34

ix

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63-3

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

Errata

This table contains changes that have been incorporated into Special Publication 800-63-3. Errata updates can include corrections, clarifications, or other minor changes in the publication that are either editorial or substantive in nature.

<table><tr><td>Date</td><td>Type</td><td>Change</td><td>Location</td></tr><tr><td>2017-12-01</td><td>Editorial</td><td>Removed the term “cryptographic” from the AAL3 description.</td><td>Executive Summary</td></tr><tr><td></td><td>Editorial</td><td>Updated reference to Risk Management Framework</td><td>§5</td></tr><tr><td></td><td>Editorial</td><td>Fixed verbiage in xAL flowcharts</td><td>Figures 6-1, 6-2, and 6-3</td></tr><tr><td></td><td>Editorial</td><td>Added NISTIR 8062 as a reference</td><td>§8.1</td></tr><tr><td></td><td>Editorial</td><td>Added definitions for disassociability, manageability, processing, and predictability</td><td>Appendix A</td></tr><tr><td>2020-03-02</td><td>Editorial</td><td>Fixed wording of FAL3 definition</td><td>§5.2</td></tr><tr><td></td><td>Substantive</td><td>Clarified flowcharts for xAL selection</td><td>Figures 6-1, 6-2, and 6-3</td></tr><tr><td></td><td>Substantive</td><td>Added definition for Authorization Component</td><td>Appendix A</td></tr><tr><td></td><td>Editorial</td><td>Removed extraneous definition of Protected Session</td><td>Appendix A</td></tr></table>

X

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

1 Purpose

This section is informative.

This recommendation and its companion volumes, Special Publication (SP) 800-63A, SP 800-63B, and SP 800-63C, provide technical guidelines to agencies for the implementation of digital authentication.

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63-3

1

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63-3

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

2 Introduction

This section is informative.

Digital identity is the unique representation of a subject engaged in an online transaction. A digital identity is always unique in the context of a digital service, but does not necessarily need to uniquely identify the subject in all contexts. In other words, accessing a digital service may not mean that the subject's real-life identity is known. Identity proofing establishes that a subject is who they claim to be. Digital authentication is the process of determining the validity of one or more authenticators used to claim a digital identity. Authentication establishes that a subject attempting to access a digital service is in control of the technologies used to authenticate. Successful authentication provides reasonable risk-based assurances that the subject accessing the service today is the same as that which previously accessed the service. Digital identity presents a technical challenge because this process often involves proofing individuals over an open network, and typically involves the authentication of individual subjects over an open network to access digital government services. There are multiple opportunities for impersonation and other attacks that fraudulently claim another subject's digital identity.

This recommendation provides agencies with technical guidelines for digital authentication of subjects to federal systems over a network. This recommendation also provides guidelines for credential service providers (CSPs), verifiers, and relying parties (RPs).

These guidelines describe the risk management processes for selecting appropriate digital identity services and the details for implementing identity assurance, authenticator assurance, and federation assurance levels based on risk. Risk assessment guidance in these guidelines supplements the NIST Risk Management Framework [NIST RMF] and its component special publications. This guideline does not establish additional risk management processes for agencies. Rather, requirements contained herein provide specific guidance related to digital identity risk while executing all relevant RMF lifecycle phases.

Digital authentication supports privacy protection by mitigating risks of unauthorized access to individuals' information. At the same time, because identity proofing, authentication, authorization, and federation involve the processing of individuals' information, these functions can also create privacy risks. These guidelines therefore include privacy requirements and considerations to help mitigate potential associated privacy risks.

These guidelines support the mitigation of the negative impacts induced by an authentication error by separating the individual elements of identity assurance into discrete, component parts. For non-federated systems, agencies will select two components, referred to as Identity Assurance Level (IAL) and Authenticator Assurance Level (AAL). For federated systems, a third component, Federation Assurance Level (FAL), is included. Section 5, Digital Identity Risk Management provides details on the risk assessment process. Section 6, Selecting Assurance Levels combines the results of the risk assessment with additional context to support agency selection of the appropriate IAL, AAL, and FAL combinations based on risk.

2

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

These guidelines do not consider nor result in a composite level of assurance (LOA) in the context of a single ordinal that drives implementation-specific requirements. Rather, by combining appropriate risk management for business, security, and privacy side-by-side with mission need, agencies will select IAL, AAL, and FAL as distinct options. Specifically, this document does not recognize the four LOA model previously used by federal agencies and described in OMB M-04-04, instead requiring agencies to individually select levels corresponding to each function being performed. While many systems will have the same numerical level for each IAL, AAL, and FAL, this is not a requirement, and agencies should not assume they will be the same in any given system or application.

The components of identity assurance detailed in these guidelines are as follows:

• IAL refers to the identity proofing process.

• AAL refers to the authentication process.

- FAL refers to the assertion protocol used in a federated environment to communicate authentication and attribute information (if applicable) to an RP.

As such, SP 800-63 is organized as a suite of volumes as follows:

SP 800-63 Digital Identity Guidelines: Provides the risk assessment methodology and an overview of general identity frameworks, using authenticators, credentials, and assertions together in a digital system, and a risk-based process of selecting assurance levels. SP 800-63 contains both normative and informative material.

SP 800-63A Enrollment and Identity Proofing: Addresses how applicants can prove their identities and become enrolled as valid subjects within an identity system. It provides requirements for processes by which applicants can both proof and enroll at one of three different levels of risk mitigation in both remote and physically-present scenarios. SP 800-63A contains both normative and informative material.

SP 800-63B Authentication and Lifecycle Management: Addresses how an individual can securely authenticate to a CSP to access a digital service or set of digital services. This volume also describes the process of binding an authenticator to an identity. SP 800-63B contains both normative and informative material.

SP 800-63C Federation and Assertions: Provides requirements on the use of federated identity architectures and assertions to convey the results of authentication processes and relevant identity information to an agency application. Furthermore, this volume offers privacy-enhancing techniques to share information about a valid, authenticated subject, and describes methods that allow for strong multi-factor authentication (MFA) while the subject remains pseudonymous to the digital service. SP 800-63C contains both normative and informative material.

NIST anticipates that individual volumes in these guidelines will be revised asynchronously. At any time, the most recent revision of each should be used (e.g., if at a time in the future SP 800-63A-1 and SP 800-63B-2 are the most recent revisions of each volume, they should be used together even though the revision numbers do not match). To minimize the risk of compatibility

3

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

errors, a reference to the base document (i.e., SP 800-63 rather than SP 800-63-3) always refers to the current version of the document.

The following table states which sections of this volume are normative and which are informative:

Table 2-1 Normative and Informative Sections of SP 800-63-3

<table><tr><td>Section Name</td><td>Normative/Informative</td></tr><tr><td>1. Purpose</td><td>Informative</td></tr><tr><td>2. Introduction</td><td>Informative</td></tr><tr><td>3. Definitions and Abbreviations</td><td>Informative</td></tr><tr><td>4. Digital Identity Model</td><td>Informative</td></tr><tr><td>5. Digital Identity Risk Management</td><td>Normative</td></tr><tr><td>6. Selecting Assurance Levels</td><td>Normative</td></tr><tr><td>7. Federation Considerations</td><td>Informative</td></tr><tr><td>8. References</td><td>Informative</td></tr></table>

2.1 Applicability

Not all digital services require authentication or identity proofing; however, this guidance applies to all such transactions for which digital identity or authentication are required, regardless of the constituency (e.g. citizens, business partners, government entities).

Transactions not covered by this guidance include those associated with national security systems as defined in 44 U.S.C. § 3542(b)(2). Private sector organizations and state, local, and tribal governments whose digital processes require varying levels of assurance may consider the use of these standards where appropriate.

These guidelines primarily focus on agency services that interact with the non-federal workforce, such as citizens accessing benefits or private sector partners accessing information sharing collaboration spaces. However, it also applies to internal agency systems accessed by employees and contractors. These users are expected to hold a valid government-issued credential, primarily the Personal Identity Verification (PIV) card or a derived PIV. Therefore SP 800-63A and SP 800-63B are secondary to the requirements of FIPS 201 and its corresponding set of special publications and agency-specific instructions. However, SP 800-63C and the risk-based selection of an appropriate FAL applies, regardless of the credential type the internal user holds. FAL

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63

4

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

selection provides agencies guidance and flexibility in how to PIV-enable their applications based on system risk.

2.2 Considerations, Other Requirements, and Flexibilities

Agencies may employ other risk mitigation measures and compensating controls not specified herein. Agencies need to ensure that any mitigations and compensating controls do not degrade the selected assurance level's intended security and privacy protections. Agencies may consider partitioning the functionality of a digital service to allow less sensitive functions to be available at a lower level of authentication and identity assurance.

Agencies may determine based on their risk analysis that additional measures are appropriate in certain contexts. In particular, privacy requirements and legal risks may lead agencies to determine that additional authentication measures or other process safeguards are appropriate. When developing digital authentication processes and systems, agencies should consult OMB Guidance for Implementing the Privacy Provisions of the E-Government Act of 2002 [M-03-22]. See the Use of Electronic Signatures in Federal Organization Transactions [ESIG] for additional information on legal risks, especially those related to the need to 1) satisfy legal standards of proof and 2) prevent repudiation.

Additionally, federal agencies implementing these guidelines should adhere to their statutory responsibilities under the Federal Information Security Modernization Act (FISMA) of 2014, 44 U.S.C. § 3551 et seq., Public Law (P.L.) 113-283 [FISMA], and related NIST standards and guidelines. FISMA directs federal agencies to develop, document, and implement agency-wide programs to provide security for the information and systems that support the agency's operations and assets. This includes the security authorization and accreditation (SA&A) of IT systems that support digital authentication. NIST recommends that non-federal entities implementing these guidelines follow equivalent standards to ensure the secure operations of their digital systems.

2.3 A Few Limitations

These technical guidelines do not address the authentication of subjects for physical access (e.g., to buildings), though some authenticators used for digital access may also be used for physical access authentication. Additionally, this revision of these guidelines does not explicitly address device identity, often referred to as machine-to-machine (such as router-to-router) authentication or interconnected devices, commonly referred to as the internet of things (IoT). That said, these guidelines are written to refer to generic subjects wherever possible to leave open the possibility for applicability to devices. Also excluded are specific requirements for issuing authenticators to devices when they are used in authentication protocols with people.

2.4 How to Use this Suite of SPs

The business model, marketplace, and composition of how identity services are delivered has drastically changed since the first version of SP 800-63 was released. Notably, CSPs can be componentized and comprised of multiple independently-operated and owned business entities. Furthermore, there may be a significant security benefit to using strong authenticators even if no

5

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63-3

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

identity proofing is required. Therefore, in this revision, a suite of SPs under the 800-63 moniker has been created to facilitate these new models and make it easy to access the specific requirements for the function an entity may serve under the overall digital identity model.

2.5 Change History

2.5.1 SP 800-63-1

NIST SP 800-63-1 updated NIST SP 800-63 to reflect current authenticator (then referred to as “token”) technologies and restructured it to provide a better understanding of the digital identity architectural model used here. Additional (minimum) technical requirements were specified for the CSP, protocols used to transport authentication information, and assertions if implemented within the digital identity model.

2.5.2 SP 800-63-2

NIST SP 800-63-2 was a limited update of SP 800-63-1 and substantive changes were made only in Section 5, Registration and Issuance Processes. The substantive changes in the revised draft were intended to facilitate the use of professional credentials in the identity proofing process, and to reduce the need to send postal mail to an address of record to issue credentials for level 3 remote registration. Other changes to Section 5 were minor explanations and clarifications.

2.5.3 SP 800-63-3

NIST SP 800-63-3 is a substantial update and restructuring of SP 800-63-2. SP 800-63-3 introduces individual components of digital authentication assurance — AAL, IAL, and FAL — to support the growing need for independent treatment of authentication strength and confidence in an individual’s claimed identity (e.g., in strong pseudonymous authentication). A risk assessment methodology and its application to IAL, AAL, and FAL has been included in this guideline. It also moves the whole of digital identity guidance covered under SP 800-63 from a single document describing authentication to a suite of four documents (to separately address the individual components mentioned above) of which SP 800-63-3 is the top-level document.

Other areas updated in 800-63-3 include:

- Renamed to “Digital Identity Guidelines” to properly represent the scope includes identity proofing and federation, and to support expanding the scope to include device identity, or machine-to-machine authentication in future revisions.

- Terminology changes, including the use of authenticator in place of token to avoid conflicting use of the word token in assertion technologies.

- Updates to authentication and assertion requirements to reflect advances in both security technology and threats.

- Requirements on the storage of long-term secrets by verifiers.

• Restructured identity proofing model.

- Updated requirements regarding remote identity proofing.

- Clarification on the use of independent channels and devices as “something you have”.

6

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

- Removal of pre-registered knowledge tokens (authenticators), with the recognition that they are special cases of (often very weak) passwords.

- Requirements regarding account recovery in the event of loss or theft of an authenticator.

- Removal of email as a valid channel for out-of-band authenticators.

- Expanded discussion of re-authentication and session management.

- Expanded discussion of identity federation; restructuring of assertions in the context of federation.

This publication is available free of charge from: https://doi.org/10.6028/NIST.SP.800-63-3

7
