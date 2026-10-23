Withdrawn NIST Technical Series Publication

<table><tr><td colspan="2">Warning Notice</td></tr><tr><td colspan="2">The attached publication has been withdrawn (archived), and is provided solely for historical purposes. It may have been superseded by another publication (indicated below).</td></tr><tr><td colspan="2">Withdrawn Publication</td></tr><tr><td>Series/Number</td><td>NIST Special Publication 800-63-3</td></tr><tr><td>Title</td><td>Digital Identity Guidelines</td></tr><tr><td colspan="2">Publication Date(s)</td></tr><tr><td colspan="2">Withdrawn Date</td></tr><tr><td colspan="2">Withdrawn Date</td></tr><tr><td colspan="2">Withdrawn Date</td></tr><tr><td colspan="2">Withdrew Date</td></tr><tr><td colspan="2">Withdrew Date</td></tr><tr><td colspan="2">Withdrew Date</td></tr><tr><td colspan="2">With With</td></tr></table>

The attached publication is available free of charge from The With独联ado Foundation.

Date updated: July 24, 2025

NIST

© 2018 Published on 12/2018. Published in https://www.nist.gov/fiter/2018/12/18/2018

ANDREWS MCFARLAND

NIST Special Publication 800-63-3

Digital Identity Guidelines

Paul A. Grassi

Michael E. Garcia

Applied Cybersecurity Division Information Technology Laboratory

James L. Fenton

This publication is available free of charge from:

https://doi.org/10.6028/NIST.SP.800-63-3

June 2017

INCLUDES UPDATES AS OF 03-02-2020; PAGE X

ASSISTANT OF COMMANDER
UNITED STATES OF AMERICA

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

This publication is available free of charge from:

https://doi.org/10.6028/NIST.SP.800-63-3

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

These technical guidelines supersede NIST Special Publication SP 800-63-2. Agencies use these guidelines as part of the risk assessment and implementation of their digital service(s). These guidelines provide mitigations of an authentication error's negative impacts by separating the individual elements of identity assurance into discrete, component parts. For non-federated systems, agencies will select two components, referred to as Identity Assurance Level (LAL) and Authenticator Assurance Level (AAL). For federated systems, agencies will select a third component, Federation Assurance Level (FAL).

iv

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

These guidelines relate the concept of a level of assurance (LOA) as a single ordinal that drives implementation-specific requirements. Rather, by combining appropriate business and privacy risk management side-by-side with mission need, agencies will select IAL, AAL, and FAL as distinct options. While many systems will have the same numerical level for each of IAL, AAL, and FAL, this is not a requirement and agencies should not assume they will be the same in any given system.

The components of identity assurance detailed in these guidelines are as follows:



• IAL refers to the identity proofing process.

• AAL refers to the authentication process.

- FAL refers to the strength of an assertion in a federated environment, used to communicate authentication and attribute information (if applicable) to a relying party (RP).

The separation of these categories provides agencies flexibility in choosing identity solutions and increases the ability to include privacy-enhancing techniques as fundamental elements of identity systems at any assurance level. For example, these guidelines support scenarios that will allow pseudonymous interactions even when strong, multi-factor authenticators are used. In addition, these guidelines encourage minimizing the dissemination of identifying information by requiring federated identity providers (IdPs) to support a range of options for querying data, such as asserting whether an individual is older than a certain age rather than querying the entire date of birth. While many agency use cases will require individuals to be fully identified, these guidelines encourage pseudonymous access to government digital services wherever possible and, even where full identification is necessary, limiting the amount of personal information collected as much as possible.

In today's environment, an organization's identity solution need not be a monolith, where one system or vendor provides all functionality. The market for identity services is componentized, allowing organizations and agencies to employ standards-based, pluggable identity solutions based on mission need. As such, SP 800-63 has been split into a suite of documents. The suite as a whole is referred to as “the guidelines,” with the individual documents referred to as “volumes.” RPs are required to use SP 800-63; the remaining volumes may be used independently or in an integrated fashion, depending on the component service(s) an agency requires.

Each volume has adopted verbs that are internationally recognized in standards organizations as normative and requirements-based. When used in a normative statement in these guidelines, they are CAPITALIZED for ease of identification. For example, SHALL is used to denote a mandatory requirement, while SHOULD refers to a technique, technology, or process that is recommended but not mandatory. For more details on the definitions of these terms see the Requirements Notation and Conventions at the beginning of each document.

These documents may inform — but do not restrict or constrain — the development or use of standards for application outside the federal government, such as e-commerce transactions.

V

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

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

Table of Contents

<table><tr><td>Executive Summary ...... iv</td></tr><tr><td>1 Purpose...... 1</td></tr><tr><td>2 Introduction...... 2</td></tr><tr><td>2.1 Applicability...... 4</td></tr><tr><td>2.2 Considerations, Other Requirements, and Flexibilities...... 5</td></tr><tr><td>2.3 A Few Limitations...... 5</td></tr><tr><td>2.4 How to Use this Suite of SPs...... 5</td></tr><tr><td>2.5 Change History...... 6</td></tr><tr><td>2.5.1 SP 800-63-1...... 6</td></tr><tr><td>2.5.2 SP 800-63-2...... 6</td></tr><tr><td>2.5.3 SP 800-63-3...... 6</td></tr><tr><td>3 Definitions and Abbreviations...... 8</td></tr><tr><td>4 Digital Identity Model...... 9</td></tr><tr><td>4.1 Overview...... 9</td></tr><tr><td>4.2 Enrollment and Identity Proofing...... 12</td></tr><tr><td>4.3 Authentication and Lifecycle Management...... 12</td></tr><tr><td>4.3.1 Authenticators...... 12</td></tr><tr><td>4.3.2 Credentials...... 14</td></tr><tr><td>4.3.3 Authentication Process...... 14</td></tr><tr><td>4.4 Federation and Assertions...... 14</td></tr><tr><td>4.4.1 Assertions...... 15</td></tr><tr><td>4.4.2 Relying Parties...... 16</td></tr><tr><td>5 Digital Identity Risk Management...... 17</td></tr><tr><td>5.1 Overview...... 17</td></tr><tr><td>5.2 Assurance Levels...... 18</td></tr><tr><td>5.3 Risk and Impacts...... 19</td></tr><tr><td>5.3.1 Business Process vs. Online Transaction ...... 20</td></tr><tr><td>5.3.2 Impacts per Category ...... 21</td></tr><tr><td>5.4 Risk Acceptance and Compensating Controls...... 22</td></tr><tr><td>5.5 Digital Identity Acceptance Statement ...... 23</td></tr><tr><td>5.6 Migrating Identities...... 23</td></tr></table>

viii

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

6 Selecting Assurance Levels....25



6.1 Selecting IAL....26

6.2 Selecting AAL 29

6.3 Selecting FAL....31

6.4 Combining xALs.... 33

7 Federation Considerations.... 35

8 References....36



8.1 General References.... 36

8.2 Standards 37

8.3 NIST Special Publications.... 37

8.4 Federal Information Processing Standards.... 37

List of Appendices

Appendix A— Definitions and Abbreviations ...... 39



A.1 Definitions....39

A.2 Abbreviations....58

List of Figures



Figure 4-1 Digital Identity Model....10

Figure 6-1 Selecting IAL....27

Figure 6-2 Selecting AAL .... 30

Figure 6-3 Selecting FAL....32

List of Tables



Table 2-1 Normative and Informative Sections of SP 800-63-3....4

Table 5-1 Identity Assurance Levels 18

Table 5-2 Authenticator Assurance Levels.... 19

Table 5-3 Federation Assurance Levels.... 19

Table 6-1 Maximum Potential Impacts for Each Assurance Level....25

Table 6-2 Acceptable Combinations of IAL and AAL....34

ix

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

Errata

This table contains changes that have been incorporated into Special Publication 800-63-3. Errata updates can include corrections, clarifications, or other minor changes in the publication that are either editorial or substantive in nature.

<table><tr><td>Date</td><td>Type</td><td>Change</td><td>Location</td></tr><tr><td>2017-12-01</td><td>Editorial</td><td>Removed the term ‘cryptographic’ from the AAL3 description.</td><td>Executive Summary</td></tr><tr><td></td><td>Editorial</td><td>Updated reference to Risk Management Framework</td><td>§5</td></tr><tr><td></td><td>Editorial</td><td>Fixed verbiage in xAL flowcharts</td><td>Figures 6-1, 6-2, and 6-3</td></tr><tr><td></td><td>Editorial</td><td>Added NISTIR 8062 as a reference</td><td>§8.1</td></tr><tr><td></td><td>Editorial</td><td>Added definitions for disassociability, manageability, processing, and predictability</td><td>Appendix A</td></tr><tr><td>2020-03-02</td><td>Editorial</td><td>Fixed wording of FAL3 definition</td><td>§5.2</td></tr><tr><td></td><td>Substantive</td><td>Clarified flowcharts for xAL selection</td><td>Figures 6-1, 6-2, and 6-3</td></tr><tr><td></td><td>Substantive</td><td>Added definition for Authorization Component</td><td>Appendix A</td></tr><tr><td></td><td>Editorial</td><td>Removed extraneous definition of Protected Session</td><td>Appendix A</td></tr></table>

This publication is available free of charge from https://doi.org/10.6028/NIST.SP 800-63-3

X

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

1 Purpose

This section is informative.

This recommendation and its companion volumes, Special Publication (SP) 800-63A, SP 800-63B, and SP 800-63C, provide technical guidelines to agencies for the implementation of digital authentication.

1

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

2 Introduction

This section is informative.

Digital identity is the unique representation of a subject engaged in an online transaction. A digital identity is always unique in the context of a digital service, but does not necessarily need to uniquely identify the subject in all contexts. In other words, accessing a digital service may not mean that the subject's real-life identity is known. Identity proofing establishes that a subject is who they claim to be. Digital authentication is the process of determining the validity of one or more authenticators used to claim a digital identity. Authentication establishes that a subject attempting to access a digital service is in control of the technologies used to authenticate.

Successful authentication provides reasonable risk-based assurances that the subject accessing the service today is the same as that which previously accessed the service. Digital identity presents a technical challenge because this process often involves proofing individuals over an open network, and typically involves the authentication of individual subjects over an open network to access digital government services. There are multiple opportunities for impersonation and other attacks that fraudulently claim another subject's digital identity.

This recommendation provides agencies with technical guidelines for digital authentication of subjects to federal systems over a network. This recommendation also provides guidelines for credential service providers (CSPs), verifiers, and relying parties (RPs).

These guidelines describe the risk management processes for selecting appropriate digital identity services and the details for implementing identity assurance, authenticator assurance, and federation assurance levels based on risk. Risk assessment guidance in these guidelines supplements the NIST Risk Management Framework [NIST RMF] and its component special publications. This guideline does not establish additional risk management processes for agencies. Rather, requirements contained herein provide specific guidance related to digital identity risk while executing all relevant RMF lifecycle phases.

Digital authentication supports privacy protection by mitigating risks of unauthorized access to individuals' information. At the same time, because identity proofing, authentication, authorization, and federation involve the processing of individuals' information, these functions can also create privacy risks. These guidelines therefore include privacy requirements and considerations to help mitigate potential associated privacy risks.

These guidelines support the mitigation of the negative impacts induced by an authentication error by separating the individual elements of identity assurance into discrete, component parts. For non-federated systems, agencies will select two components, referred to as Identity Assurance Level (IAL) and Authenticator Assurance Level (AAL). For federated systems, a third component, Federation Assurance Level (FAL), is included. Section 5, Digital Identity Risk Management provides details on the risk assessment process. Section 6, Selecting Assurance Levels combines the results of the risk assessment with additional context to support agency selection of the appropriate IAL, AAL, and FAL combinations based on risk.

This publication is available from the author(s) at publisher.

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

This publication is available free of charge from the author.

4

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

selection provides agencies guidance and flexibility in how to PIV-enable their applications based on system risk.

2.2 Considerations, Other Requirements, and Flexibilities

Agencies may employ other risk mitigation measures and compensating controls not specified herein. Agencies need to ensure that any mitigations and compensating controls do not degrade the selected assurance level's intended security and privacy protections. Agencies may consider partitioning the functionality of a digital service to allow less sensitive functions to be available at a lower level of authentication and identity assurance.

Agencies may determine based on their risk analysis that additional measures are appropriate in certain contexts. In particular, privacy requirements and legal risks may lead agencies to determine that additional authentication measures or other process safeguards are appropriate. When developing digital authentication processes and systems, agencies should consult OMB Guidance for Implementing the Privacy Provisions of the E-Government Act of 2002 [M-03-22]. See the Use of Electronic Signatures in Federal Organization Transactions [ESIG] for additional information on legal risks, especially those related to the need to 1) satisfy legal standards of proof and 2) prevent repudiation.

Additionally, federal agencies implementing these guidelines should adhere to their statutory responsibilities under the Federal Information Security Modernization Act (FISMA) of 2014, 44 U.S.C. § 3551 et seq., Public Law (P.L.) 113-283 [FISMA], and related NIST standards and guidelines. FISMA directs federal agencies to develop, document, and implement agency-wide programs to provide security for the information and systems that support the agency's operations and assets. This includes the security authorization and accreditation (SA&A) of IT systems that support digital authentication. NIST recommends that non-federal entities implementing these guidelines follow equivalent standards to ensure the secure operations of their digital systems.

2.3 A Few Limitations

These technical guidelines do not address the authentication of subjects for physical access (e.g., to buildings), though some authenticators used for digital access may also be used for physical access authentication. Additionally, this revision of these guidelines does not explicitly address device identity, often referred to as machine-to-machine (such as router-to-router) authentication or interconnected devices, commonly referred to as the internet of things (IoT). That said, these guidelines are written to refer to generic subjects wherever possible to leave open the possibility for applicability to devices. Also excluded are specific requirements for issuing authentications to devices when they are used in authentication protocols with people.

2.4 How to Use this Suite of SPs

The business model, marketplace, and composition of how identity services are delivered has drastically changed since the first version of SP 800-63 was released. Notably, CSPs can be componentized and comprised of multiple independently-operated and owned business entities. Furthermore, there may be a significant security benefit to using strong authentications even if no

5

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

- Clarification on the use of independent channels and devices as "something you have".

This publication is available free of charge from the华军科学技术学院学报

6

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES



- Removal of pre-registered knowledge tokens (authenticators), with the recognition that they are special cases of (often very weak) passwords.

- Requirements regarding account recovery in the event of loss or theft of an authenticator.

- Removal of email as a valid channel for out-of-band authenticators.

- Expanded discussion of re-authentication and session management.

- Expanded discussion of identity federation; restructuring of assertions in the context of federation.

7

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

3 Definitions and Abbreviations

See Appendix A for a complete set of definitions and abbreviations.

8

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

4 Digital Identity Model

This section is informative.

4.1 Overview

The digital identity model used in these guidelines reflects technologies and architectures currently available in the market. More complex models that separate functions — such as issuing credentials and providing attributes — among a larger number of parties are also available and may have advantages in some application classes. While a simpler model is used in this document, it does not preclude agencies from separating these functions. Additionally, certain enrollment, identity proofing, and issuance processes performed by the CSP are sometimes delegated to an entity known as either the registration authority (RA) or identity manager (IM). A close relationship between the RA and CSP is typical, and the nature of this relationship may differ among RAs, IMs, and CSPs. The type of relationship and its requirements is outside of the scope of this document. Accordingly, the term CSP will be inclusive of RA and IM functions. Finally, a CSP may provide other services in addition to digital identity services. In these situations, the requirements specified throughout these guidelines only apply to the CSP function(s), not the additional services.

Digital identity is the unique representation of a subject engaged in an online transaction. The process used to verify a subject's association with their real-world identity is called identity proofing. In these guidelines, the party to be proofed is called an applicant. When the applicant successfully completes the proofing process, they are referred to as a subscriber.

The strength of identity proofing is described by an ordinal measurement called the IAL. At IAL1, identity proofing is not required, therefore any attribute information provided by the applicant is self-asserted, or should be treated as self-asserted and not verified (even if provided by a CSP to an RP). IAL2 and IAL3 require identity proofing, and the RP may request the CSP assert information about the subscriber, such as verified attribute values, verified attribute references, or pseudonymous identifiers. This information assists the RP in making authorization decisions. An RP may decide that it requires IAL2 or IAL3, but may only need specific attributes, resulting in the subject retaining some degree of pseudonymity. This privacy-enhancing approach is a benefit of separating the strength of the proofing process from that of the authentication process. An RP may also employ a federated identity approach where the RP outsources all identity proofing, attribute collection, and attribute storage to a CSP.

In these guidelines, the party to be authenticated is called a claimant and the party verifying that identity is called a verifier. When a claimant successfully demonstrates possession and control of one or more authenticators to a verifier through an authentication protocol, the verifier can verify that the claimant is a valid subscriber. The verifier passes on an assertion about the subscriber, who may be either pseudonymous or non-pseudonymous, to the RP. That assertion includes an identifier, and may include identity information about the subscriber, such as the name, or other attributes that were collected in the enrollment process (subject to the CSP's policies, the RP's

This publication is available from the author et al. 2014.

9

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

needs, and consent for disclosure of attributes given by the subject). Where the verifier is also the RP, the assertion may be implicit. The RP can use the authenticated information provided by the verifier to make authorization decisions.

Authentication establishes confidence that the claimant has possession of an authenticator(s) bound to the credential, and in some cases in the attribute values of the subscriber (e.g., if the subscriber is a U.S. citizen, is a student at a particular university, or is assigned a particular number or code by an agency or organization). Authentication does not determine the claimant's authorizations or access privileges; this is a separate decision, and is out of these guidelines' scope. RPs can use a subscriber's authenticated identity and attributes with other factors to make authorization decisions. Nothing in this document suite precludes RPs from requesting additional information from a subscriber that has successfully authenticated.

The strength of the authentication process is described by an ordinal measurement called the AAL. AAL1 requires single-factor authentication and is permitted with a variety of different authenticator types. At AAL2, authentication requires two authentication factors for additional security. Authentication at the highest level, AAL3, additionally requires the use of a hardware-based authenticator and verifier impersonation resistance.

The various entities and interactions that comprise the digital identity model used here are illustrated in Figure 4-1.

Figure 4-1 Digital Identity Model

The left side of the diagram shows the enrollment, credential issuance, lifecycle management activities, and various states of an identity proofing and authentication process. The usual sequence of interactions is as follows:

10

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES



1. An applicant applies to a CSP through an enrollment process.

2. The CSP identity proofs that applicant. Upon successful proofing, the applicant becomes a subscriber.

3. Authenticator(s) and a corresponding credential are established between the CSP and the subscriber.

4. The CSP maintains the credential, its status, and the enrollment data collected for the lifetime of the credential (at a minimum). The subscriber maintains his or her authenticator(s).

Other sequences are less common, but could also achieve the same functional requirements.

The right side of Figure 4-1 shows the entities and interactions involved in using an authenticator to perform digital authentication. A subscriber is referred to as a claimant when he or she needs to authenticate to a verifier. The interactions are as follows:



1. The claimant proves possession and control of the authenticator(s) to the verifier through an authentication protocol.

2. The verifier interacts with the CSP to validate the credential that binds the subscriber's identity to their authenticator and to optionally obtain claimant attributes.

3. The CSP or verifier provides an assertion about the subscriber to the RP, which may use the information in the assertion to make an authorization decision.

4. An authenticated session is established between the subscriber and the RP.

In all cases, the RP should request the attributes it requires from a CSP before authenticating the claimant. In addition, the claimant should be requested to consent to the release of those attributes prior to generation and release of an assertion.

In some cases, the verifier does not need to communicate in real time with the CSP to complete the authentication activity (e.g., some uses of digital certificates). Therefore, the dashed line between the verifier and the CSP represents a logical link between the two entities. In some implementations, the verifier, RP, and CSP functions may be distributed and separated as shown in Figure 4-1. However, if these functions reside on the same platform, the interactions between the components are local messages between applications running on the same system rather than protocols over shared, untrusted networks.

As noted above, a CSP maintains status information about the credentials it issues. CSPs will generally assign a finite lifetime when issuing credentials to limit the maintenance period. When the status changes, or when the credentials near expiration, credentials may be renewed or re-issued; or, the credential may be revoked and destroyed. Typically, the subscriber authenticates to the CSP using their existing, unexpired authenticator and credential in order to request issuance of a new authenticator and credential. If the subscriber fails to request authenticator and credential re-issuance prior to their expiration or revocation, they may be required to repeat the enrollment process to obtain a new authenticator and credential. Alternatively, the CSP may choose to accept a request during a grace period after expiration.

This publication is available from the author要么何土木和社会 ScienceDirect

11

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

4.2 Enrollment and Identity Proofing

Normative requirements can be found in SP 800-63A, Enrollment and Identity Proofing.

The previous section introduced the participants in the conceptual digital identity model. This section provides additional details regarding the participants' relationships and responsibilities in enrollment and identity proofing.

An individual, referred to as an applicant at this stage, opts to be identity proofed by a CSP. If the applicant is successfully proofed, the individual is then termed a subscriber of that CSP.

The CSP establishes a mechanism to uniquely identify each subscriber, register the subscriber's credentials, and track the authenticators issued to that subscriber. The subscriber may be given authenticators at the time of enrollment, the CSP may bind authenticators the subscriber already has, or they may be generated later as needed. Subscribers have a duty to maintain control of their authenticators and comply with CSP policies in order to maintain active authenticators. The CSP maintains enrollment records for each subscriber to allow recovery of authenticators, for example, when they are lost or stolen.

4.3 Authentication and Lifecycle Management

Normative requirements can be found in SP 800-63B, Authentication and Lifecycle Management.

4.3.1 Authenticators

The classic paradigm for authentication systems identifies three factors as the cornerstones of authentication:



• Something you know (e.g., a password).

- Something you have (e.g., an ID badge or a cryptographic key).

- Something you are (e.g., a fingerprint or other biometric data).

MFA refers to the use of more than one of the above factors. The strength of authentication systems is largely determined by the number of factors incorporated by the system — the more factors employed, the more robust the authentication system. For the purposes of these guidelines, using two factors is adequate to meet the highest security requirements. As discussed in Section 5.1, other types of information, such as location data or device identity, may be used by an RP or verifier to evaluate the risk in a claimed identity, but they are not considered authentication factors.

In digital authentication the claimant possesses and controls one or more authenticators that have been registered with the CSP and are used to prove the claimant's identity. The authenticator(s) contains secrets the claimant can use to prove that he or she is a valid subscriber, the claimant authenticates to a system or application over a network by proving that he or she has possession and control of one or more authenticators.

This publication is available from the author et al. 2014.

12

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

The secrets contained in authenticators are based on either public key pairs (asymmetric keys) or shared secrets (symmetric keys). A public key and a related private key comprise a public key pair. The private key is stored on the authenticator and is used by the claimant to prove possession and control of the authenticator. A verifier, knowing the claimant's public key through some credential (typically a public key certificate), can use an authentication protocol to verify the claimant's identity by proving that the claimant has possession and control of the associated private key authenticator.

Shared secrets stored on authenticators may be either symmetric keys or memorized secrets (e.g., passwords and PINs), as opposed to the asymmetric keys described above, which subscribers need not share with the verifier. While both keys and passwords can be used in similar protocols, one important difference between the two is how they relate to the subscriber. While symmetric keys are generally stored in hardware or software that the subscriber controls, passwords are intended to be memorized by the subscriber. Since most users choose short passwords to facilitate memorization and ease of entry, passwords typically have fewer characters than cryptographic keys. Furthermore, whereas systems choose keys at random, users attempting to choose memorable passwords will often select from a very small subset of the possible passwords of a given length, and many will choose very similar values. As such, whereas cryptographic keys are typically long enough to make network-based guessing attacks untenable, user-chosen passwords may be vulnerable, especially if no defenses are in place.

In this volume, authenticators always contain a secret. Some of the classic authentication factors do not apply directly to digital authentication. For example, a physical driver's license is something you have, and may be useful when authenticating to a human (e.g., a security guard), but is not in itself an authenticator for digital authentication. Authentication factors classified as something you know are not necessarily secrets, either. Knowledge-based authentication, where the claimant is prompted to answer questions that are presumably known only by the claimant, also does not constitute an acceptable secret for digital authentication. A biometric also does not constitute a secret. Accordingly, these guidelines only allow the use of biometrics for authentication when strongly bound to a physical authenticator.

A digital authentication system may incorporate multiple factors in one of two ways:

1. The system may be implemented so that multiple factors are presented to the verifier; or

2. Some factors may be used to protect a secret that will be presented to the verifier.



For example, item 1 can be satisfied by pairing a memorized secret (what you know) with an out-of-band device (what you have). Both authenticator outputs are presented to the verifier to authenticate the claimant. For item 2, consider a piece of hardware (the authenticator) that contains a cryptographic key (the authenticator secret) where access is protected with a fingerprint. When used with the biometric, the cryptographic key produces an output that is used to authenticate the claimant.

As noted above, biometrics, when employed as a single factor of authentication, do not constitute acceptable secrets for digital authentication — but they do have their place in the authentication of digital identities. Biometric characteristics are unique personal attributes that can be used to

13

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

verify the identity of a person who is physically present at the point of verification. They include facial features, fingerprints, iris patterns, voiceprints, and many other characteristics. SP 800-63A, Enrollment and Identity Proofing recommends that biometrics be collected in the enrollment process to later help prevent a registered subscriber from repudiating the enrollment, and to help identify those who commit enrollment fraud.

4.3.2 Credentials

As described in the preceding sections, a credential binds an authenticator to the subscriber, via an identifier, as part of the issuance process. A credential is stored and maintained by the CSP, though the claimant may possess it. The claimant possesses an authenticator, but is not necessarily in possession of the credential. For example, database entries containing the user attributes are considered to be credentials for the purpose of this document but are possessed by the verifier. X.509 public key certificates are a classic example of credentials the claimant can, and often does, possess.

4.3.3 Authentication Process

The authentication process begins with the claimant demonstrating to the verifier possession and control of an authenticator that is bound to the asserted identity through an authentication protocol. Once possession and control have been demonstrated, the verifier verifies that the credential remains valid, usually by interacting with the CSP.

The exact nature of the interaction between the verifier and the claimant during the authentication protocol is extremely important in determining the overall security of the system. Well-designed protocols can protect the integrity and confidentiality of communication between the claimant and the verifier both during and after the authentication, and can help limit the damage that can be done by an attacker masquerading as a legitimate verifier.

Additionally, mechanisms located at the verifier can mitigate online guessing attacks against lower entropy secrets — like passwords and PINs — by limiting the rate at which an attacker can make authentication attempts, or otherwise delaying incorrect attempts. Generally, this is done by keeping track of and limiting the number of unsuccessful attempts, since the premise of an online guessing attack is that most attempts will fail.

The verifier is a functional role, but is frequently implemented in combination with the CSP, the RP, or both. If the verifier is a separate entity from the CSP, it is often desirable to ensure that the verifier does not learn the subscriber's authenticator secret in the process of authentication, or at least to ensure that the verifier does not have unrestricted access to secrets stored by the CSP.

4.4 Federation and Assertions

Normative requirements can be found in SP 800-63C, Federation and Assertions.

Overall, SP 800-63 does not presuppose a federated identity architecture; rather, these guidelines are agnostic to the types of models that exist in the marketplace, allowing agencies to deploy a

14

NIST SP 800-63-3
<|det|>header [677,好客屋客

digital authentication scheme according to their own requirements. However, identity federation is preferred over a number of siloed identity systems that each serve a single agency or RP.

Federated architectures have many significant benefits, including, but not limited to:



- Enhanced user experience. For example, an individual can be identity proofed once and reuse the issued credential at multiple RPs.

- Cost reduction to both the user (reduction in authenticators) and the agency (reduction in information technology infrastructure).

- Data minimization as agencies do not need to pay for collection, storage, disposal, and compliance activities related to storing personal information.

- Pseudonymous attribute assertions as agencies can request a minimized set of attributes, to include claims, to fulfill service delivery.

- Mission enablement as agencies can focus on mission, rather than the business of identity management.

The following sections discuss the components of a federated identity architecture should an agency elect this type of model.

4.4.1 Assertions

Upon completion of the authentication process, the verifier generates an assertion containing the result of the authentication and provides it to the RP. The assertion is used to communicate the result of the authentication process, and optionally information about the subscriber, from the verifier to the RP. Assertions may be communicated directly to the RP, or can be forwarded through the subscriber, which has further implications for system design.

An RP trusts an assertion based on the source, the time of creation, how long the assertion is valid from time of creation, and the corresponding trust framework that governs the policies and processes of CSPs and RPs. The verifier is responsible for providing a mechanism by which the integrity of the assertion can be confirmed.

The RP is responsible for authenticating the source (the verifier) and for confirming the integrity of the assertion. When the verifier passes the assertion through the subscriber, the verifier must protect the integrity of the assertion in such a way that it cannot be modified. However, if the verifier and the RP communicate directly, a protected session may be used to preserve the integrity of the assertion. When sending assertions across an open network, the verifier is responsible for ensuring that any sensitive subscriber information contained in the assertion can only be extracted by an RP that it trusts to maintain the information's confidentiality.

Examples of assertions include:

- Security Assertion Markup Language (SAML) assertions are specified using a mark-up language intended for describing security assertions. They can be used by a verifier to make a statement to an RP about the identity of a claimant. SAML assertions may optionally be digitally signed.

15

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES



- OpenID Connect claims are specified using JavaScript Object Notation (JSON) for describing security, and optionally, user claims. JSON user info claims may optionally be digitally signed.

- Kerberos tickets allow a ticket-granting authority to issue session keys to two authenticated parties using symmetric key based encapsulation schemes.

4.4.2 Relying Parties

An RP relies on results of an authentication protocol to establish confidence in the identity or attributes of a subscriber for the purpose of conducting an online transaction. RPs may use a subscriber's authenticated identity (pseudonymous or non-pseudonymous), the IAL, AAL, and FAL (FAL indicating the strength of the assertion protocol), and other factors to make authorization decisions. The verifier and the RP may be the same entity, or they may be separate entities. If they are separate entities, the RP normally receives an assertion from the verifier. The RP ensures that the assertion came from a verifier trusted by the RP. The RP also processes any additional information in the assertion, such as personal attributes or expiration times. The RP is the final arbiter concerning whether a specific assertion presented by a verifier meets the RP's established criteria for system access regardless of IAL, AAL, or FAL.

16

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

5 Digital Identity Risk Management

This section is normative.

This section and the corresponding risk assessment guidance supplement the NIST Risk Management Framework [NIST RMF] and its component special publications. This does not establish additional risk management processes for agencies. Rather, requirements contained herein provide specific guidance related to digital identity risk that agency RPs SHALL apply while executing all relevant RMF lifecycle phases.

5.1 Overview

In today's digital services, combining proofing, authenticator, and federation requirements into a single bundle sometimes has unintended consequences and can put unnecessary implementation burden on the implementing organization. It is quite possible that an agency can deliver the most effective set of identity services by assessing the risk and impacts of failures for each individual component of digital authentication, rather than as a single, all-encompassing LOA. To this end, these guidelines recognize that an authentication error is not a singleton that drives all requirements.

This volume details requirements to assist agencies in avoiding:



1. Identity proofing errors (i.e., a false applicant claiming an identity that is not rightfully theirs);

2. Authentication errors (i.e., a false claimant using a credential that is not rightfully theirs); and

3. Federation errors (i.e., an identity assertion is compromised).

From the perspective of an identity proofing failure, there are two dimensions of potential failure:



1. The impact of providing a service to the wrong subject (e.g., an attacker successfully proofs as someone else).

2. The impact of excessive identity proofing (i.e., collecting and securely storing more information about a person than is required to successfully provide the digital service).

As such, agencies SHALL assess the risk of proofing, authentication, and federation errors separately to determine the required assurance level for each transaction.

Section 5.3 provides impact categories specific to digital identity to assist in the overall application of the RMF.

Risk assessments determine the extent to which risk must be mitigated by the identity proofing, authentication, and federation processes. These determinations drive the relevant choices of applicable technologies and mitigation strategies, rather than the desire for any given technology driving risk determinations. Once an agency has completed the overall risk assessment; selected

17

NIST SP 800-63-3
<|det|>header [677,好客屋客

DIGITAL IDENTITY GUIDELINES

individual assurance levels for identity proofing, authentication, and federation (if applicable); and determined the processes and technologies they will employ to meet each assurance level, agencies SHALL develop a “Digital Identity Acceptance Statement”, in accordance with SP 800-53 IA-1 a.1. See Section 5.5 for more detail on the necessary content of the Digital Identity Acceptance Statement.

5.2 Assurance Levels

An agency RP SHALL select, based on risk, the following individual assurance levels:



- IAL: The robustness of the identity proofing process to confidently determine the identity of an individual. IAL is selected to mitigate potential identity proofing errors.

- AAL: The robustness of the authentication process itself, and the binding between an authenticator and a specific individual's identifier. AAL is selected to mitigate potential authentication errors (i.e., a false claimant using a credential that is not rightfully theirs).

- FAL: The robustness of the assertion protocol the federation uses to communicate authentication and attribute information (if applicable) to an RP. FAL is optional as not all digital systems will leverage federated identity architectures. FAL is selected to mitigate potential federation errors (an identity assertion is compromised).

A summary of each of the identity, authenticator, and federation assurance levels is provided below.

Table 5-1 Identity Assurance Levels

<table><tr><td></td><td>Identity Assurance Level</td></tr><tr><td>IAL1: At IAL1, attributes, if any, are self-asserted or should be treated as self-asserted.</td><td></td></tr><tr><td>IAL2: At IAL2, either remote or in-person identity proofing is required. IAL2 requires identifying attributes to have been verified in person or remotely using, at a minimum, the procedures given in SP 800-63A.</td><td></td></tr><tr><td>IAL3: At IAL3, in-person identity proofing is required. Identifying attributes must be verified by an authorized CSP representative through examination of physical documentation as described in SP 800-63A.</td><td></td></tr></table>

18

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

Table 5-2 Authenticator Assurance Levels

<table><tr><td>Authenticator Assurance Level</td></tr><tr><td>AAL1: AAL1 provides some assurance that the claimant controls an authenticator registered to the subscriber. AAL1 requires single-factor authentication using a wide range of available authentication technologies. Successful authentication requires that the claimant prove possession and control of the authenticator(s) through a secure authentication protocol.</td></tr><tr><td>AAL2: AAL2 provides high confidence that the claimant controls authenticator(s) registered to the subscriber. Proof of possession and control of two different authentication factors is required through a secure authentication protocol. Approved cryptographic techniques are required at AAL2 and above.</td></tr><tr><td>AAL3: AAL3 provides very high confidence that the claimant controls authenticator(s) registered to the subscriber. Authentication at AAL3 is based on proof of possession of a key through a cryptographic protocol. AAL3 is like AAL2 but also requires a “hard” cryptographic authenticator that provides verifier impersonation resistance.</td></tr></table>

Table 5-3 Federation Assurance Levels

<table><tr><td>FAL1: FAL1 permits the RP to receive a bearer assertion from an identity provider (IdP). The IdP must sign the assertion using approved cryptography.</td></tr><tr><td>FAL2: FAL2 adds the requirement that the assertion be encrypted using approved cryptography such that the RP is the only party that can decrypt it.</td></tr><tr><td>FAL3: FAL3 requires the subscriber to present proof of possession of a cryptographic key referenced in the assertion along with the assertion itself. The assertion must be signed using approved cryptography and encrypted to the RP using approved cryptography.</td></tr></table>

When described generically or bundled, these guidelines will refer to IAL, AAL, and FAL as xAL.

5.3 Risk and Impacts

This section provides details on the impact categories used to determine IAL, AAL, and FAL.

Potential Impact Categories: To determine the appropriate level of assurance of the user's asserted identity, agencies SHALL assess the potential risks and identify measures to minimize their impact.

19

This publication and information contained herein are subject to space constraints and the Commission's 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

Authentication, proofing, and federation errors with potentially worse consequences require higher levels of assurance. Business process, policy, and technology may help reduce risk.

Categories of harm and impact include:



1. Inconvenience, distress, or damage to standing or reputation;

2. Financial loss or agency liability;

3. Harm to agency programs or public interests;

4. Unauthorized release of sensitive information;

5. Personal safety; and

6. Civil or criminal violations.

Required assurance levels for digital transactions are determined by assessing the potential impact of each of the above categories using the potential impact values described in Federal Information Processing Standard (FIPS) 199 [FIPS 199].

The three potential impact values are:



1. Low impact,

2. Moderate impact, and

3. High impact.

5.3.1 Business Process vs. Online Transaction

The assurance level determination is only based on transactions that are part of a digital system. An online transaction may not be equivalent to a complete business process that requires offline processing, or online processing in a completely segmented system. In selecting the appropriate assurance levels, the agency should assess the risk associated with online transactions they are offering via the digital service, not the entire business process associated with the provided benefit or service. For example, in an online survey, personal information may be collected, but it is never made available online to the submitter after the information is saved. In this instance, it is important for the information to be carefully protected in backend systems, but there is no reason to identify proof or even authenticate the user providing the information for the purposes of their own access to the system or its associated benefits. The online transaction is solely a submission of the data. The entire business process may require a significant amount of data validation, without ever needing to know if the correct person submitted the information. In this scenario, there is no need for any identity proofing nor authentication.

Another example where the assessed risk could differ if the agency evaluated the entire business process rather than the online transaction requirements is a digital service that accepts resumés to apply for open job postings. In this use case, the digital service allows an individual to submit – or at least does not restrict an individual from submitting – a résumé on behalf of anyone else, and in subsequent visits to the site, access the résumé for various purposes. Since the résumé information is available to the user in later sessions, and is likely to contain personal information, the agency must select an AAL that requires MFA, even though the user self-asserted the personal information. In this case, the requirements of [EO 13681] apply and the application

This publication and /or design are for profit / but not for profit; may not be copied or distributed; is subject to the Editors discretion

20

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

must provide at least AAL2. However, the identity proofing requirements remain unclear. The entire business process of examining a résumé and ultimately hiring and onboarding a person requires a significant amount of identity proofing. The agency needs a high level of confidence that the job applicant is in fact the subject of the résumé submitted online if a decision to hire is made. Yet this level of proofing is not required to submit the résumé online. Identity proofing is not required to complete the digital portion of the transaction successfully. Identity proofing the submitter would create more risk than required in the online system as excess personal information would be collected when no such information is needed for the portion of the hiring process served by the digital job application portal and may reduce usability. Therefore, the most appropriate IAL selection would be 1. There is no need to identify proof the user to successfully complete the online transaction. This decision for the online portal itself is independent of a seemingly obvious identity proofing requirement for the entire business process, lest a job be offered to a fraudulent applicant.

5.3.2 Impacts per Category

This section defines the potential impacts for each category of harm. Each assurance level, IAL, AAL, and FAL (if accepting or asserting a federated identity) SHALL be evaluated separately.

Note: If an error in the identity system causes no measurable consequences for a category, there is no impact.

Potential impact of inconvenience, distress, or damage to standing or reputation:



- Low: at worst, limited, short-term inconvenience, distress, or embarrassment to any party.

- Moderate: at worst, serious short-term or limited long-term inconvenience, distress, or damage to the standing or reputation of any party.

- High: severe or serious long-term inconvenience, distress, or damage to the standing or reputation of any party. This is ordinarily reserved for situations with particularly severe effects or which potentially affect many individuals.

Potential impact of financial loss:



- Low: at worst, an insignificant or inconsequential financial loss to any party, or at worst, an insignificant or inconsequential agency liability.

- Moderate: at worst, a serious financial loss to any party, or a serious agency liability.

- High: severe or catastrophic financial loss to any party, or severe or catastrophic agency liability.

Potential impact of harm to agency programs or public interests:



- Low: at worst, a limited adverse effect on organizational operations or assets, or public interests. Examples of limited adverse effects are: (i) mission capability degradation to the extent and duration that the organization is able to perform its primary functions with noticeably reduced effectiveness, or (ii) minor damage to organizational assets or public interests.

21

This publication and does not necessarily reflect the views of the authors

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES



- Moderate: at worst, a serious adverse effect on organizational operations or assets, or public interests. Examples of serious adverse effects are: (i) significant mission capability degradation to the extent and duration that the organization is able to perform its primary functions with significantly reduced effectiveness; or (ii) significant damage to organizational assets or public interests.

- High: a severe or catastrophic adverse effect on organizational operations or assets, or public interests. Examples of severe or catastrophic effects are: (i) severe mission capability degradation or loss of to the extent and duration that the organization is unable to perform one or more of its primary functions; or (ii) major damage to organizational assets or public interests.

Potential impact of unauthorized release of sensitive information:



- Low: at worst, a limited release of personal, U.S. government sensitive, or commercially sensitive information to unauthorized parties resulting in a loss of confidentiality with a low impact as defined in FIPS 199.

- Moderate: at worst, a release of personal, U.S. government sensitive, or commercially sensitive information to unauthorized parties resulting in loss of confidentiality with a moderate impact as defined in FIPS 199.

- High: a release of personal, U.S. government sensitive, or commercially sensitive information to unauthorized parties resulting in loss of confidentiality with a high impact as defined in FIPS 199.

Potential impact to personal safety:



- Low: at worst, minor injury not requiring medical treatment.

- Moderate: at worst, moderate risk of minor injury or limited risk of injury requiring medical treatment.

• High: a risk of serious injury or death.

The potential impact of civil or clinical violations is:



- Low: at worst, a risk of civil or criminal violations of a nature that would not ordinarily be subject to enforcement efforts.

- Moderate: at worst, a risk of civil or criminal violations that may be subject to enforcement efforts.

- High: a risk of civil or criminal violations that are of special importance to enforcement programs.

5.4 Risk Acceptance and Compensating Controls

The SP 800-63 suite specifies baseline requirements for digital identity services based on assurance level. Agencies SHOULD implement identity services per the requirements in these guidelines and SHOULD consider additional techniques and technologies to further secure and privacy-enhance their services.

This publication and /or the content / e-version 25 March 2018. 3-5

22

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES

Agencies MAY determine alternatives to the NIST-recommended guidance, for the assessed xALs, based on their mission, risk tolerance, existing business processes, special considerations for certain populations, availability of data that provides similar mitigations to those described in this suite, or due to other capabilities that are unique to the agency.

Agencies SHALL demonstrate comparability of any chosen alternative, to include any compensating controls, when the complete set of applicable SP 800-63 requirements is not implemented. For example, an agency may choose a National Information Assurance Partnership (NIAP) protection profile over FIPS, where the profile is equivalent to or stronger than the FIPS requirements. That said, agencies SHALL NOT alter the assessed xAL based on agency capabilities. Rather, the agency MAY adjust their implementation of solutions based on the agency's ability to mitigate risk via means not explicitly addressed by SP 800-63 requirements. The agency SHALL implement procedures to document both the justification for any departure from normative requirements and detail the compensating control(s) employed.

This guidance addresses only those risks associated with authentication and identity proofing errors. NIST Special Publication 800-30, Risk Management Guide for Information Technology Systems [SP 800-30] recommends a general methodology for managing risk in federal systems.

5.5 Digital Identity Acceptance Statement

Agencies SHOULD include this information in existing artifacts required to achieve a SA&A.

The statement SHALL include, at a minimum:



1. Assessed xAL,

2. Implemented xAL,

3. Rationale, if implemented xAL differs from assessed xAL,

4. Comparability demonstration of compensating controls when the complete set of applicable 800-63 requirements are not implemented, and

5. If not accepting federated identities, rationale.

5.6 Migrating Identities

As these guidelines are revised, CSPs SHALL consider how changes in requirements affect their user population. In some instances, the user population will be unaffected, yet in others, the CSP will require users undergo a transitional activity. For example, CSPs may request users — upon initial logon since last revision — to supply additional proofing evidence to adhere to new IAL requirements. This SHALL be a risk-based decision, made to the context of the CSP, any RPs that use the CSP, mission, and the population served. The following considerations serve only as a guide to agencies when considering the impacts of requirements changes:

1. If the RP is experiencing identity-related fraud, a migration may prove beneficial. If not, migration times may not be an added value.

23

This publication and information contained herein are proprietary and not publicly disclosed.

NIST SP 800-63-3

DIGITAL IDENTITY GUIDELINES



2. New, stronger, or user-friendly authentication options are added to individual AALs the CSP could issue new authenticators or allow users to register authenticators they already have.

3. Federation requirements may or may not have a user impact. For example, consent requirements for information requirements could necessitate an infrastructure or protocol upgrade.

4. Addition or removal of xALs may not require a migration, but would trigger a new risk assessment to determine if a change is necessary for the RP.

The guidance does not prescribe that any migration needs to occur, only that it be considered as revisions are released. It is up to the CSP and RP, based on their risk tolerance and mission, to determine the best approach.

24

NIST SP 800-63-3

DIGITAL IDENTITY DIGUELIDNES

6 Selecting Assurance Levels

This section is normative.

The risk assessment results are the primary factor in selecting the most appropriate levels. This section details how to apply the results of the risk assessment with additional factors unrelated to risk to determine the most advantageous xAL selection.

First, compare the risk assessment impact profile to the impact profiles associated with each assurance level, as shown in Table 6-1 below. The determination regarding the impact of the risk is based on the results of the analysis of the requirements for every category of the survey.

Despite the user being pseudonymous, the agency should select AAL2 or AAL3 for authentication because a malicious action card is given by the person who is not necessarily a member of the U.S. Department of State.

Note: AAL1, identity was a member of the U.S. Department of State, which is a member of the U.S. Department of State. The U.S. Department of State was a member of the U.S. Department of State. The U.S. Department of State was a member of the U.S. Department of State. The U.S. department of State was a member of the U.S. Department of State. The U.S. Department of State was a member of the U.S. Department of State. The data was obtained from the U.S. Department of State, which was obtained from the U.S. Department of State, which was obtained from the U.S. Department of State, which was obtained from the U.S. Department of State.

The U.S. Department of State was a member of the U.S. Department of State and U.S. Department of State. The data was obtained from the U.S. Department of State, which was obtained from the U.S. Department of State and from the U.S. Department of State. The data was obtained from the U.S. Department of State and from the U.S. Department of State. The data was obtained from the U.S. Department of State and from

The U.S. Department of State was obtained from the U.S. Department of State and from the U.S. Department of State. The data was obtained from the U.S. Department of State and from The U.S. Department of State. The data was obtained from the U.S. Department of State and from The U.S. Department of State. The data was obtained from The U.S. Department of State and from The U.S. Department of State. The data was obtained from The U.S. Department of State and from The U.S.Department of State. The data was obtained from The U.S. Department of State and from The U.S. Department of State. The data was obtained from The U.S.Department of State and from The U.S. Department of State. The data was obtained from The U.S. Department of State and from The U.S. Department of State. This research made use of the following: The research of the University of California, 2005, was conducted by UC Davis, funded by UC Davis, funded by UC Davis, and the U.S. Department of State, funded by The University of California, 2005, was conducted by The University of California, 2005, and the U.S. Department of State, funded by The University of California, 2005, was conducted by The U.S. Department of State, funded by The University of California, 2005, and the U.S. Department of State, 2005, was conducted by The University of California, 2005, and the U.S. Department of State, 2005, and the U.S. Department of State, 2005, and the U.S. Department of State, 2005, and the U. S. Department of State, 2005, and the U. S. Department of State, 2005, and the U. S. Department of State, 2

The United States is a member of the U.S. Department of Science, 2005, and the U.S. Department of Science, 2005, and the U.S. Department of Science, 2005, and the U.S. Department of Science, USA.

The United States is a member of the U.S. Department of Science, 2005, is a member of the U.S. Department of Science, 2005, and the U.S. Department of Science, 2005, is a member of the U.S. Department of Science, 2005, and the U.S. Department's Office of Science, 2005, is a member of the U.S. Department of Science, 2005, and the U.S. Department's Office of Science, USA.

The United States is a member of the U.S. Department of Science and Technology, 2005, and the U.S. Department of Science, 2005, and the U.S. Department of Science, 2005, and the U. S. Department of Science, 2005, and the U. S. Department of Science, 2005, and the U. S. Department of Science, 20

The United States is a member of the U.S. Department of Science and Technology, 2004, and the U.S. Department of Science, 2004, and the U.S. Department of Science, 2004, and the U.S. Department of Science, 2004, and the U. S. Department of Science, 2004, and the U.S. Department of Science, 2004, and the U.S. Department of Science, 2004,

is a member of the U.S. Department of Science and Technology, 2004, and the U.S. Department of Science, 2004, and the U.S.

is a member of the U.S. Department of Science and Technology, 2004, and

is a member of the U.S. Department of Science and Technology, 2004, and The U.S.

is a member of the U.S. Department of Science and Technology, 2003, and

is a member of the U.S. Department of Science and Technology, 2003, and The U.S.

is a member of the U.S. Department of Science and Technology,

is a member of the U.S. Department of Science and Technology, 2003, and Thorne.

is a member of the U.S. Department of Science and Technology,

is a member of the U.S. Department of Science and Technology, 2003, and Thorne.
<|det|>text {is a member of the U.S. Department of Science and Technology, 2003, and Thorne.}

is a member of the U.S. Department of Science and Technology,

is a member of the U.S. Department of Science and Technology, 2003, and Thorne.
is a member of the U.S. Department of Science and Technology, 2003, and Thorne.
is a member of the U.S. Department of Science an d Technology, 2003, and Thorne.
is a member of the U.S. Department of Science an d Technology, 2003, and Thorne.
is a member of the U.S. Department of Science an d Technology, 2003, and Thorne.
is a member of the U.S. Department of Technology, 2003, and Thorne.
is a member of the U.S. Department of Science an d Technology, 2003, and Thorne.
is a member of the U.S. Department of Science an d Technology, 2003, and Thorne.
is a member of the U.S. Department ofScience an dTechnology, 2003, and Thorne.
is a member of the U.S. Department of Science an dTechnology, 2003, and Thorne.
is a member of the U.S. Department of Science an dTechnology, 2003, and Thone an be

Spatial distribution of the U.S. Department of Science an d Technology an be a member of the United States. The Department of Technology is developing the Science and Technology Data System (NIST) to support the transfer of technology to the National Institute of Technology. The Department of Technology is developing the Science and Technology Data System (NIST) an be a member of the United States. The Department of Technology is developing the Science and Technology Data System (NIST) an be a member of the United States. The Department of Technology is developing the Science Data System (NIST) an be a member of the United States. The Department of Technology is developing the Science and Technology Data System (NIST) an a member of the United States. The Department of Technology is developing the Science and Technology Data System (NIST) an a member of the United States. The Department of Science and Technology is developing the Science and Technology Data System (NIST) an a member of the United States. The Department of Science and Technology is developing the Science and Technology Data (NIST) an a member of the United States. The Department of Science and Technology is developing the Science and Technology Data System (NIST) an a member of

The Department of Science and Technology is developing the major scientific and technology education programs that are currently being developed. The Department of Science and Technology is developing the Science and Technology Data System (NIST) an a member of the United States. The Department of Science and Technology is also developing the Science and Technology Data System (NIST) an a member of the United States. The Department of Science and Technology is developing the Science and Technology Data System (nndt) an a member of the United States. The Department of Science and Technology is developing the Science and Technology Data System (nndt) an a member of the United Kingdom. The Department of Science and Technology is developing the Science and Technology Data System (nndt) an a member of the United States. The Department of Science and Technology has been developed by the United States, and it is also member of the United States. The Department of Science and Technology has been developed by the United States, and it is also member of the United States. The Department of Science, Technology and Technology has been developed by the United States, and it is also member of the United States. The Department of Science and Technology has been developed by the United States, which is also member of the United States. The Department of Science and Technology has been developed by the United States, which is also member of the United States. The Department of Technology has been developed by the United States, which is also member of the United States. The Department of Science and Technology has been developed by the United States, which is

University of Science and Technology, China 2011. The Department of Science and Technology has been developed by the United States, and the Department of Science and Technology has been developed by the United States, China 2011.

The Department of Science and Technology has been developed by the United States, China 2011. The Department of Science and Technology has been developed by the United States, China 2011.

The Department of Science and Technology has been developed by the United States, China 2011. The Department of Science and Technology has been developed by the United States.

The Department of Science and Technology has been developed by the United States, China 2011. The Department of Science and Technology has been developed by the United States of America.

The Department of Science and Technology has been developed by the United States, China 2011. The Department of Science and Technology has been developed by the United States. The Department of Science and Technology has been developed by the United States of America, China 2011. The Department of Science and Technology has been developed by the United States of America, China 2011. The Department of Science and Technology has been developed by the United Kingdom, China 2011. The Department of Science and Technology has been developed by the United States of America, China 2011. The Department of Science and Technology hasbeen developed by the United States of America, China 2011. The Department of Science and Technology has been developed by the United States of America, China 2011. This publication provides a summary of the research findings of the United States of America, which are critical to the United States of America, and the research findings of the United States of America are critical to the United States of America, which is also critical to the United States of America, and the research findings of the United States of America are critical to the United States of America, which is also critical to the United State

The United States of America is a major university in the United States, with a research school in the United States of America. The research centers of the United States of America are the United States of America, with a research school in the United States of America, and the United States of America are the United States of America, with a research school in the United States of America, and the United States of America are the United States of India.

The United States of America is the United States of America, with a research school in the United States of America, and the United States of America are the United States of India, with a research school in the United States of India, and the United States of India are the United States of India, with a research school in the United States of India, and the United States of India are the United States of India, with a research

The United States of America is the United States of America, with a research school in the United States of India, and the United States of India are the United States of India, with a research school in the United States of America, and the United States of India are the United States of India, with a research school in the United States of India, and the United States of India are the United State

The United States of America is the United States of America, with a research school in the United States of India, and the United States of India are the United State of India, with a research school in the United States of India, and the United States of India are the United States of India, with a research school in the United State of India, and the United States of India are the United States of India, with a research school in the United States of India, and the United States of India are

The United States of America is the United States of India, with a research school in the United States of India, and the United States of India are the United States of India, with a research school of India in the United States of India, and the United States of India are the United States of India, with a research school of India in the United States of India, and

The United States of India is the United States of India, with a research school of India in the United States of India, and the United States of India are the United States of India, with a Research school of India in the United States of India, and the United States of India are the United States of India, with a research school of India in the United States of

The United States of India is the United States of India, with a research school of India in the United States of India, and the United States of India are also the United States of India, with a research school of India in the United States of India, and the United States of India are the United States of India, with a

The United States of India is the United States of India, with a research school of India in the United States of India, and the United States of India are

The United States of India is the United States of India, with a research school of India in the United States of India, and the United States of India are in the United States of India, with a research school of India in the United States of India, and the United States of India are in the United States of India, with

The United States of India is the United States of India, with a research school of India in the United States of India, and the United States of India are included in the United States of India, with a research school of India in the United States of India, and the United States of India are included in the United States of India, and the United States of India are included in the United States of India, with a research school of India in the United States of India.

The United States of India is the United States of India, with a research school of India in the United States of India, and the United States of India are published in the United States of India, with a research school of India in the United States of India, and the United States of India are published in the United States of India, and the United States of India are published in the United States of India, with a research school of India in the United States of India.

The United States of India is the United States of India, with a research school of India in the United States of India, and the United States of India are released from the United States of India by the United States of India, and the United States of India are released from the United States of India.

The United States of India is the United States of India, with a research school of India in the United States of India, and the United States of India are replaced by the United States of India, and the United States of India are released from the United States of India.

The United States of India is the United States of India, with a research school of India in the United States of India, and the United States of India are release from the United States of India, and the United States of India are released from the United States of India.

The United States of India is the United States of India, and the United States of India are released from the United States of India, and the United States of India are released from the United States of India.

The United States of India is the United States of India, and the United States of India are released from the United States of India, and the United States of

The United States of India is the United States of India, and the United States of India are released from the United States of India, and the United States ofIndia are released from the United States of India, and the United States of India are released from the United States of India, and the United States of India are released from the United States ofIndia, and the United States of India are released from the United States of India, and the United States of India are released from the United States of India, and the United States of India are released from theUnited States of India, and the United States of India are released from the United States of India, and the United States of India are released from the United States of India, and the United states of India are released from the United States of India, and the United States of India are released from the United States of India, and the United States of India are released

The United States of India is a member of the United States of India, which is a member of the United States of India. The United States of India is released from the United States of India, and the United States of India is released from the United States of India. The United States of India is released from the United States of India, and the United States of India is released from the United States of India, and the United States of India is released from the United States of India. The United States of India is also released from the United States of India, and the United States of India is released from the United States of India, and the United States of India is released from the United State

The United States of India is released from the United States of India, and the United States of India is released from the United States of India, and the United States of India are released from the United States of India, and the United States of India is released from the United States of India, and the United States of India is released from the United Kingdom. The United States of India is released from the United States of India, and the United States of India is released from the United States of India, and the United States is released from the United States of India, and the United States of India is released from the United States of India, and the United States of India is released from theUnited States of India, and the United States of India is released from the United States of India, and the United States of India is released from the United States of India, and the United States of Indiais released from the United States of India, and the United States of India is released from the United States of India, and the United States of India is released from the United states of India, and the United States of India is released from the United States of India, and the United States of India is released from the United States of India, and then from the United States of India, we can release the United States of India, and then from the United States of India, we can also be licensed to release the United States of India, and then from the United States of India, we can also be licensed to release the United States of India, and then from the United State, we can also be licensed to release the United States of India, and then from the United States of India, we can also be licensed to release the United States of North America, and then from the United States of India, we can also be licensed to release the United States of India, and then from the United States of India, we can be also licensed to release the United States of India, and then from the United States of India, we can also be licensed to release the United States of India, and then from

The United States of India has been licensed to release the United States of India, and then from the United States of India, we can also be licensed to release the United States of India, and then from it we can also be licensed to release the United States of India, we can also be licensed to release the United States of India, and then from it we can also be licensed to release the United States ofIndia, and then from it we can also be licensed to release the United States of India, and then from it we can also be licensed to release the United States of India, and then from it we can also be licensed to release the United States of India and then from it we can also be licensed to release the United States of India, and then from it we can also be licensed to release the United States of India, from which we can also be licensed to release the United States of India, and then from it we can also be licensed to release the United States of India, and from it we can also be licensed to release the United States of India, and then from it we can also be licensed to release the United States of India, and from it we also can be licensed to release the United States of India, and from it we can also be licensed to release the United States of India, and from it we can also be licensed to release the United States of India, and from it we can also be licensed

and from it we can also be released to release the United States of India, and from it we can also be released to release the United States of India, and from it we can also be released to release the United States of India, and from it from the United States of India, we can also be released to release the United States of India, and from it we can also be released to release the United States of India, and from it we can be released to release the United States of India, and from it we can also be released to release the United States of India, and from it we can also be released from the United States of India, and from it we can also be released to release the United States of India, and from it we can also be released to release the United State

1.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.

2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.22.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2

2.2.2.2.2.2.2.2.2.2.2.2.2.22.2.2.2.22.2.2.2.2.2.2.2.2.2.2.2.2.2.
<|det|>text [515, 90, 885, 90.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.2.<ecel><nl>
<|det|>text [515, 90, 885, 90.2.2.2.2.2.2.2.2.2.2.22.2.2.2.2.2.2.
<|det|>text [515, 90, 885, 90.2.2.2.2.
<|det|>text [515, 90, 885, 90.2.2.2.2.2.2.
<|det|>text [515, 90, 885, 90.2.2.2.2
<|det|>text [515, 90, 885, 90.2.2.2.2.
<|det|>text [515, 90, 885, 10, 92.2.2.2.
<|det|>text [515, 90, 885, 10.2.2.2.
<|det|>text [515, 90, 885, 10.2.2.2.
<|det|>text [515, 90,
<|det|>text [515, 90, 885, 10.2.2.2.
<|det|>text [515, 90, 885, 10.22.2.2.
<|det|>text [515, 90, 885, 10.2.2.2.
<|det|>text [515, 90, 485, 10.2.2.2.
<|det|>text [515, 90, 485, 10.2.2.2.
<|det|>text [515 , 90, 485, 10.2.2.2.
<|det|>text [515, 90, 485, 10.2.2.2
<|det|>text [515, 90, 485, 10.2.2.2.
<|det|>text [515, 90, 485, 10.22.2.2.
<|det|>text [515, 90, 485, 10.2.2.2.
<|det|>text [515, 90, 500, 10.2.2.2.
<|det|>text [515, 90, 500, 10.2.2.2.
<|det|>text [515,
<|det|>text [515, 90, 500, 10.2.2.2.
<|det|>text [515, 90, 500, 10.22.2.2.
<|det|>text [515, 90, 500, 10.2.2.2.
<|det|>text [515, 90, 900, 10.2.2.2.
<|det|>text [515, 90, 900, 10.2.2.2.
<|det|>text [515 , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
<|det|>text [515, 90, 900, 10.2.2.2.
<|det|>text [515, 90, 900, 10.22.2.2.
<|det|>text [515, 90, 900, 10.2.2.2.
<|det|>text [515, 90, 700, 10.2.2.2.
<|det|>text [515, 90, 700, 10.2.2.2.
<|det|>text [515 , 90, 700, 10.2.2.2.
<|det|>text [515, 90, 700, 10.2.2.2
<|det|>text [515, 90, 700, 10.2.2.2.
<|det|>text [515, 90, 700, 10.22.2.2.
<|det|>text [515, 90, 700, 10.2.2.2.
<|det|>text [515, 90, 600, 10.2.2.2.
<|det|>text [515, 90, 600, 10.2.2.2.
<|det|>text [515 , , , , , , , , , , , , , , , , , , , , ,
<|det|>text [515, 90, 600, 10.2.2.2.
<|det|>text [515, 90, 600, 10.22.2.2.
<|det|>text [515, 90, 600, 10.2.2.2.
<|det|>text [515, 90, 620, 10.2.2.2.
<|det|>text [515, 90, 620, 10.2.2.2.
<|det|>text [515 , 90, 620, 10.2.2.2.
<|det|>text [515, 90, 620, 10.2.2.2
<|det|>text [515, 90, 620, 10.2.2.2.
<|det|>text [515, 90, 620, 10.22.2.2.
<|det|>text [515, 90, 620, 10.2.2.2.
<|det|>text [515, 90, 632, 10.2.2.2.
<|det|>text [515, 90, 632, 10.2.2.2.
<|det|>text [515 , 90, 632, 10.2.2.2.
<|det|>text [515, 90, 632, 10.2.2.2
<|det|>text [515, 90, 632, 10.2.2.2.
<|det|>text [515, 90, 632, 10.22.2.2.
<|det|>text [515, 90, 632, 10.2.2.2.
<|det|>text [515, 90, 692, 10.2.2.2.
<|det|>text [515, 90, 692, 10.2.2.2.
<|det|>text [515 , , , , , , , , , , , , , , , , , , , , . , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , . , , , , , , , , , , , , , . , , , , , , , , , , , , , , , , , , , , . , , , , , , , , , , , , , ,

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
<|det|>text (1, 33, 925, 42]<|/det|>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 2. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.

1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1

1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1
1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 2

1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.

1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.   [Non-Text]

1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.   1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
<|det|>header [0, 1, 999, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
<|det|>header [0, 1, 999, 1, 1, 1, 1, 1, 1, 1, 1,
<|det|>header [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, \end{array}
\]
<|det|>header [0, 1, 999, 1, 1, 1, 1, 1, 1, 1, 1
<|det|>header [0, 1, 999, 1, 1, 1, 1, 1, 1, 1, 1}, \\ \end{array}
\]
<|det|>header [0, 1, 999, 1, 1, 1, 1, 1, 1,
<|det|>header [0, 1, 999, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, \]
<|det|>header [0, 1, 999, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, \]
<|det|>header [0, 1, 999, 1, 1, 1, 1,
<|det|>header [0, 1, 999, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, \]
<|det|>header [0, 1, 999,
<|det|>header [0, 1, 999, 1, 1, 1, 1, 1, 1, 1, 2,
<|det|>header [0, 1, 999, 1, 1, 1, 1, 1, 1, 1, 3,
<|det|>header [0, 1, 999, 1, 1, 1, 1, 1, 1, 1, 4,
<|det|>header [0, 1, 999, 1, 1, 1, 1, 1, 1, 1, 5,
<|det|>header [0, 1, 999, 1, 1, 1, 1, 1, 1, 1, 6,
<|det|>header [0, 1, 999, 1, 1, 1, 1,
