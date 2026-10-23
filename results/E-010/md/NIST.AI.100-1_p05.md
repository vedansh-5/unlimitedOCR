#

Check for updates

NIST AI 100-1

Artificial Intelligence Risk Management Framework (AI RMF 1.0)

NIST

NATIONAL INSTITUTE OF
STANDARDS AND TECHNOLOGY
U.S. DEPARTMENT OF COMMERCE

NIST AI 100-1

Artificial Intelligence Risk Management Framework (AI RMF 1.0)

This publication is available free of charge from:

https://doi.org/10.6028/NIST.AI.100-1

January 2023

U.S. Department of Commerce

Gina M. Raimondo, Secretary

National Institute of Standards and Technology

Laurie E. Locascio, NIST Director and Under Secretary of Commerce for Standards and Technology

Certain commercial entities, equipment, or materials may be identified in this document in order to describe an experimental procedure or concept adequately. Such identification is not intended to imply recommendation or endorsement by the National Institute of Standards and Technology, nor is it intended to imply that the entities, materials, or equipment are necessarily the best available for the purpose.

This publication is available free of charge from: https://doi.org/10.6028/NIST.AI.100-1

Update Schedule and Versions

The Artificial Intelligence Risk Management Framework (AI RMF) is intended to be a living document.

NIST will review the content and usefulness of the Framework regularly to determine if an update is appropriate; a review with formal input from the AI community is expected to take place no later than 2028. The Framework will employ a two-number versioning system to track and identify major and minor changes. The first number will represent the generation of the AI RMF and its companion documents (e.g., 1.0) and will change only with major revisions. Minor revisions will be tracked using “.n” after the generation number (e.g., 1.1). All changes will be tracked using a Version Control Table which identifies the history, including version number, date of change, and description of change. NIST plans to update the AI RMF Playbook frequently. Comments on the AI RMF Playbook may be sent via email to AIframework@nist.gov at any time and will be reviewed and integrated on a semi-annual basis.

Table of Contents

Executive Summary 1

Part 1: Foundational Information 4

1 Framing Risk 4

1.1 Understanding and Addressing Risks, Impacts, and Harms 4

1.2 Challenges for AI Risk Management 5

1.2.1 Risk Measurement 5

1.2.2 Risk Tolerance 7

1.2.3 Risk Prioritization 7

1.2.4 Organizational Integration and Management of Risk 8

2 Audience 9

3 AI Risks and Trustworthiness 12

3.1 Valid and Reliable 13

3.2 Safe 14

3.3 Secure and Resilient 15

3.4 Accountable and Transparent 15

3.5 Explainable and Interpretable 16

3.6 Privacy-Enhanced 17

3.7 Fair – with Harmful Bias Managed 17

4 Effectiveness of the AI RMF 19

Part 2: Core and Profiles 20

5 AI RMF Core 20

5.1 Govern 21

5.2 Map 24

5.3 Measure 28

5.4 Manage 31

6 AI RMF Profiles 33

Appendix A: Descriptions of AI Actor Tasks from Figures 2 and 3 35

Appendix B: How AI Risks Differ from Traditional Software Risks 38

Appendix C: AI Risk Management and Human-AI Interaction 40

Appendix D: Attributes of the AI RMF 42

List of Tables

Table 1 Categories and subcategories for the GOVERN function. 22

Table 2 Categories and subcategories for the MAP function. 26

Table 3 Categories and subcategories for the MEASURE function. 29

Table 4 Categories and subcategories for the MANAGE function. 32

i

NIST AI 100-1

AI RMF 1.0

List of Figures

Fig. 1 Examples of potential harms related to AI systems. Trustworthy AI systems and their responsible use can mitigate negative risks and contribute to benefits for people, organizations, and ecosystems.

Fig. 2 Lifecycle and Key Dimensions of an AI System. Modified from OECD (2022) OECD Framework for the Classification of AI systems — OECD Digital Economy Papers. The two inner circles show AI systems' key dimensions and the outer circle shows AI lifecycle stages. Ideally, risk management efforts start with the Plan and Design function in the application context and are performed throughout the AI system lifecycle. See Figure 3 for representative AI actors.

Fig. 3 AI actors across AI lifecycle stages. See Appendix A for detailed descriptions of AI actor tasks, including details about testing, evaluation, verification, and validation tasks. Note that AI actors in the AI Model dimension (Figure 2) are separated as a best practice, with those building and using the models separated from those verifying and validating the models.

Fig. 4 Characteristics of trustworthy AI systems. Valid & Reliable is a necessary condition of trustworthiness and is shown as the base for other trustworthiness characteristics. Accountable & Transparent is shown as a vertical box because it relates to all other characteristics.

Fig. 5 Functions organize AI risk management activities at their highest level to govern, map, measure, and manage AI risks. Governance is designed to be a cross-cutting function to inform and be infused throughout the other three functions.

5

10

11

12

20

Page ii
