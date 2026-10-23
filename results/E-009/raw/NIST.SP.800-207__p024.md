<|det|>header [115, 44, 248, 59]<|/det|>NIST SP 800-207
<|det|>header [684, 44, 884, 59]<|/det|>ZERO TRUST ARCHITECTURE
<|det|>image [225, 90, 775, 337]<|/det|>
<|det|>image_caption [379, 354, 620, 370]<|/det|>Figure 4: Enclave Gateway Model
<|det|>text [111, 383, 861, 437]<|/det|>It is possible for this model to be a hybrid with the device agent/gateway model. In this model, enterprise assets have a device agent that is used to connect to enclave gateways, but these connections are created using the same process as the basic device agent/gateway model.
<|det|>text [111, 451, 885, 555]<|/det|>This model is useful for enterprises that have legacy applications or on-premises data centers that cannot have individual gateways in place. The enterprise needs a robust asset and configuration management program in place to install/configure the device agents. The downside is that the gateway protects a collection of resources and may not be able to protect each resource individually. This may also allow for subjects to see resources which they do not have privileges to access.
<|det|>title [113, 570, 485, 589]<|/det|>3.2.3 Resource Portal-Based Deployment
<|det|>text [111, 602, 851, 675]<|/det|>In this deployment model, the PEP is a single component that acts as a gateway for subject requests. The gateway portal can be for an individual resource or a secure enclave for a collection of resources used for a single business function. One example would be a gateway portal into a private cloud or data center containing legacy applications as shown in Figure 5.
<|det|>page_number [490, 923, 511, 937]<|/det|>15
