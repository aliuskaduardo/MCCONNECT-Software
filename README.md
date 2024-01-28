# MCCONNECT-Software
MCCONNET: Markov Chains Connectivity Invariants for Networks

# MACCONNECT About
MCCONNECT: Markov Chains Connectivity Invariants for Networks is essentially a MARCH-INSIDE algorithm based software. MCCONNECT: Markov Chains Connectivity Invariants for Networks is essentially focus on the study/quantification of the dynamics changes in local/overall network structure after multiple types of attacks (connections/nodes removal) in biological, social, economical, political, or legal networks. Attacks are understood as different strategies/ways to remove nodes/links from the network an later using MI invariants to quantify changes in network structure.

# Authors Contributions:
MCCONNECT is a software developed by C.R. Muteanu (algorithm and software design, software programing, and author of papers, https://github.com/muntisa/), H. González-Díaz (algorithm and software design, and author of papers, https://github.com/glezdiazh), and A. Duardo-Sánchez (consulting on intellectual property issues and co-author of papers for social and legal networks analysis, https://github.com/aliuskaduardo). 

# Algorithm origin:

MCCONNECT is based on MARCH-INSIDE: Markov Chain Invariants for Networks Simulation and Design MARCH-INSIDE (MI), a well-known method introduced by Prof. Humbert G Díaz (Gonzaléz-Díaz et al.) as early as 2002 for the calculation of Markov Invariants (Moments, Shanon entropies, Mean Markov values) of molecular graphs and complext netxorks using a Markov chain stchastic approach. MCCONNET focus on the study/quantification of the changes in network local and overall structure after multiple types of attacks. Posterior to it, MINODES was created based on the same MI algorithms ideas in order to calculate MI node centralities of complex networks without performing attacks to networks and them increasing calculation speed notably. In this sense, MINONDES perform a more static study of networks than MCCONNECT and can bee seen as a child software of MCCONNCT and by extension of MARCH-INSIDE software. Some of these MI node centralities calculated by MCCONNECT / MINODES are Markov kth-node degrees, Markov kth-node clossenes, etc.; which are kth higher order analogues of classic node centralities now re-calculated and extended to higher order analogues using a MI approach. MINODES is able to read multiple files of complex networks (protein interaction networks, metabolic networks, social networks, etc.) in .mat, .net, and other formats and return MI node centralities of all nodes in the network. In case you want to develop new collaborations, applications, etc. related to MI algorith please do not hesitate to contact us at Linkedin: Prof. Humbert g. Díaz https://www.linkedin.com/in/humbertgdiaz/ and/or Prof. C.R. Munteanu https://www.linkedin.com/in/muntisa/.

# Related Algorithms:

MARCH-INSIDE (MI) algorithm is the original algorithm https://github.com/glezdiazh/MARCH-INSIDE on which MINODES is based. Other algorithms based also on MI and then related to MINDOES somehow are: Sequence to Stars Networks (S2SNET) by C.R. Munteanu and González-Díaz H. https://github.com/muntisa/S2SNet); R-Markov Topological Indices (RMARKOVTI) by C.R. Munteanu https://github.com/muntisa/RMarkovTI, S2SNET Phyton (PyS2SNET) by C.R. Munteanu https://github.com/muntisa/pyS2SNet, etc.

# MCCONNECT - MINODES Main authors contributions:

C.R. munteanu (algorithm and software design, software programing, AI/ML applications, main author of papers, https://github.com/muntisa/).

H. Gónzalez-Díaz (algorithm and software design, AI/ML applications, main author of papers, https://github.com/glezdiazh),

A. Duardo-Sánches (assistance with intellectual proprty issues and co-author of papers for social and legal networks analysis, https://github.com/aliuskaduardo)

# MCCONNECT Applications: 

MCCONNECT parameters can be used to study the Markov Chain stochastic behaviour of graph or network-like systems to the quantify the dynamic variations/changes in the structure of complex biomo-lecular systems as well as social, political, economical, or legal networks.

# See references:

1: Duardo-Sánchez A, Munteanu CR, Riera-Fernández P, López-Díaz A, Pazos A,
González-Díaz H. Modeling complex metabolic reactions, ecological systems, and
financial and legal networks with MIANN models based on Markov-Wiener node
descriptors. J Chem Inf Model. 2014 Jan 27;54(1):16-29. doi: 10.1021/ci400280n.
Epub 2013 Dec 23. PMID: 24320872. 

2: Riera-Fernández P, Munteanu CR, Dorado J, Martin-Romalde R, Duardo-Sanchez A,
González-Diaz H. From chemical graphs in computer-aided drug design to general
Markov-Galvez indices of drug-target, proteome, drug-parasitic disease,
technological, and social-legal networks. Curr Comput Aided Drug Des. 2011
Dec;7(4):315-37. doi: 10.2174/157340911798260340. PMID: 22050683.

3: Riera-Fernández P, Munteanu CR, Escobar M, Prado-Prado F, Martín-Romalde R,
Pereira D, Villalba K, Duardo-Sánchez A, González-Díaz H. New Markov-Shannon
Entropy models to assess connectivity quality in complex networks: from
molecular to cellular pathway, Parasite-Host, Neural, Industry, and Legal-Social
networks. J Theor Biol. 2012 Jan 21;293:174-88. doi: 10.1016/j.jtbi.2011.10.016.
Epub 2011 Oct 25. PMID: 22037044.

4: González-Díaz H, Herrera-Ibatá DM, Duardo-Sánchez A, Munteanu CR, Orbegozo-
Medina RA, Pazos A. ANN multiscale model of anti-HIV drugs activity vs AIDS
prevalence in the US at county level based on information indices of molecular
graphs and social networks. J Chem Inf Model. 2014 Mar 24;54(3):744-55. doi:
10.1021/ci400716y. Epub 2014 Feb 21. PMID: 24521170.

