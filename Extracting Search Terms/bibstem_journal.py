# -*- coding: utf-8 -*-

import pprint

a=('''

    TDR          3D Research
    AASHS        AAS Hist. Ser.
    AASPB        AAS Photo Bulletin
    AAN          AAVSO Alert Notice
    AAVSC        AAVSO Circular
    AAVSN        AAVSO Newsletter
    AAVSB        AAVSO Solar Bulletin
    AbaOB        Abastumanskaia Astrofizicheskaia Observatoriia Byulleten
    AbbOO        Abbadia Observatory Observations
    ABWG         Abh. Braunschweigische Wissenschaftliche Ges.
    AbhP         Abh. der Preuß. Akademie der Wissenschaften Jahrg
    AbhKP        Abh. Konigl. Preuss. Akad. Wissenschaften Jahre 1906,92, Berlin,1907
    AbhBr        Abh. naturwiss. Verein Bremen
    AADDR        Abhandlungen Akad. Wiss. DDR
    AAGot        Abhandlungen Akad. Wiss. Göttingen
    AbApA        Abstract and Applied Analysis
    ASFAS        Academia Scientiarum Fennica Annales Series Physica
    AOIJ         Academic Open Internet Journal
    CR2          Academie des Sciences Comptes Rendus Serie Mecanique Physique Chimie Sciences de la Terre et de l Univers
    CRAS         Academie des Sciences Paris Comptes Rendus
    CRASB        Academie des Sciences Paris Comptes Rendus Serie B Sciences Physiques
    CRASG        Academie des Sciences Paris Comptes Rendus Serie Generale La Vie des Sciences
    CRASP        Academie des Sciences Paris Comptes Rendus Serie Physique Astrophysique
    CRASM        Academie des Sciences Paris Comptes Rendus Serie Sciences Mathematiques
    CRASA        Academie des Sciences Paris Comptes Rendus Vie Academique Semester Supplement
    MeARB        Academie Royale de Belgique Classe des Sciences Memoires
    ASSAB        Academie Serbe des Sciences et des Arts Bulletin Classe des Sciences Techniques
    ASLLR        Accademia di Scienze e Lettere Istituto Lombardo Rendiconti Serie della Classe di Scienze Matematiche e Naturali Sezione Scienze Matematiche Fisiche Chimiche e Geologiche
    ANLAM        Accademia Nazionale dei Lincei Atti Rendiconti Classe di Matematica e Applicazioni
    ANLAF        Accademia Nazionale dei Lincei Atti Rendiconti Classe di Scienze Fisiche e Naturali
    ANLAR        Accademia Nazionale dei Lincei Atti Rendiconti Classe di Scienze Fisiche Matematiche e Naturali
    AcChR        Accounts Chem. Res.
    AcBu         Acoust. Bull.
    AIH          Acoustical Imaging and Holography
    APhy         Acoustical Physics
    ASAJ         Acoustical Society of America Journal
    AcouL        Acoustics Letters
    AcAcu        Acta Acustica
    AcAer        Acta Aerodynamica Sinica
    AcAAS        Acta Aeronautica et Astronautica Sinica
    AcAri        Acta Arithmetica
    AcArm        Acta Armamentarii
    AcAau        Acta Astronautica
    AcA          Acta Astronomica
    AcASn        Acta Astronomica Sinica
    AcApS        Acta Astrophysica Sinica
    AcAuS        Acta Automatica Sinica
    ACIP         Acta Cienc. Indica Phys.
    AcC          Acta Cosmologica
    AcCrA        Acta Crystallographica Section A
    AcCrD        Acta Crystallographica Section D
    AcESn        Acta Electron. Sinica
    AcEle        Acta Electronica
    AcElS        Acta Electronica Sinica
    AcGG         Acta Geod. Geophys.
    AcGSn        Acta Geophys. Sinica
    AcGeo        Acta Geophysica
    AcGeP        Acta Geophysica Polonica
    AcHA         Acta Historica Astronomiae
    AcMCS        Acta Materiae Compositae Sinica
    AcMat        Acta Materialia
    AcMa         Acta Mathematica
    AcMaS        Acta Mathematica Sinica
    AcMSw        Acta Mathematica Sweden
    AcMec        Acta Mechanica
    AcMSn        Acta Mechanica Sinica
    AcMSS        Acta Mechanica Solida Sinica
    AcMet        Acta Metallurgica
    AcM&M        Acta Metallurgica et Materialia
    AcMeS        Acta Meteorologica Sinica
    AcNum        Acta Numerica
    AcOSi        Acta Oceanica Sinica
    AcO          Acta Oecologica
    AcOpS        Acta Optica Sinica
    AcPSi        Acta Photonica Sinica
    AcPhy        Acta Physica
    AcPhA        Acta Physica Austriaca
    AcPAS        Acta Physica Austriaca Supplement
    AcPhC        Acta Physica et Chemica
    AcPhH        Acta Physica Hungarica
    APHHI        Acta Physica Hungarica Heavy Ion Physics
    APHQE        Acta Physica Hungarica Quantum Electronics
    AcPP         Acta Physica Polonica
    AcPPA        Acta Physica Polonica A
    AcPPB        Acta Physica Polonica B
    AcPSn        Acta Physica Sinica
    AcPSl        Acta Physica Slovaca
    AcPhS        Acta Physiologica Scandinavica
    AcPol        Acta Polytechnica
    AcPSc        Acta Polytechnica Scandinavica Applied Physics Series
    AcSSn        Acta Seismologica Sinica
    ASSF         Acta Societatis Scientarum Fennicae
    ASSFA        Acta Societatis Scientarum Fennicae Series A
    AcTec        Acta Technica
    AcUni        Acta Universitaria
    AcMPh        Acta Universitatis Caroliae. Mathematica et Physica
    AcMPS        Acta Universitatis Caroliae. Mathematica et Physica Supplement
    Acu          Acustica
    AdAs         Ad Astra
    ARPM         Adgeziia Rasplavov i Paika Materialov
    AAMS         Adv. Appl. Mech. Suppl.
    AdCM         Advanced Ceramic Materials
    AdCoL        Advanced Composites Letters
    AMP          Advanced Materials and Processes
    AdOT         Advanced Optical Technologies
    ASL          Advanced Science Letters
    AdSAC        Advanced Series in Astrophysics and Cosmology
    AdAnS        Advances in the Astronautical Sciences
    AdApM        Advances in Applied Mathematics
    AdAst        Advances in Astronomy
    AdA&A        Advances in Astronomy and Astrophysics
    AASP         Advances in Astronomy and Space Physics
    AdAtS        Advances in Atmospheric Sciences
    AdAMP        Advances in Atomic and Molecular Physics
    AAMOP        Advances in Atomic Molecular and Optical Physics
    AdChP        Advances in Chemical Physics
    AdCIS        Advances in Colloid and Interface Science
    AdCMP        Advances in Condensed Matter Physics
    AdEPS        Advances in Earth and Planetary Sciences
    AEEP         Advances in Electronics and Electron Physics
    AEEPS        Advances in Electronics and Electron Physics Supplement
    AdGeo        Advances in Geophysics
    AdG          Advances in Geosciences
    AdHEP        Advances in High Energy Physics
    AdMRe        Advances in Magnetic Resonance
    AdMPC        Advances in Materials Physics and Chemistry
    AdMS         Advances in Materials Science
    AdMSE        Advances in Materials Science and Engineering
    AdMaP        Advances in Mathematical Physics
    AdMUM        Advances in Mechanics Uspekhi Mekhaniki
    AdMet        Advances in Meteorology
    AdNOp        Advances in Nonlinear Optics
    AdNuP        Advances in Nuclear Physics
    AdPhy        Advances in Physics
    AdPlP        Advances in Plasma Physics
    AdQC         Advances in Quantum Chemistry
    AdRS         Advances in Radio Science
    AdSR         Advances in Science and Research
    AdSSP        Advances in Solid State Physics
    AdSpR        Advances in Space Research
    AdTAM        Advances in Theoretical and Applied Mechanics
    AdTMP        Advances in Theoretical and Mathematical Physics
    AdThP        Advances in Theoretical Physics
    AdWR         Advances in Water Resources
    ATTM         AEG Telefunken Technische Mitteilungen
    AeoRe        Aeolian Research
    Aekv         Aerodinamika kanalov i ventiliatorov
    AeRaG        Aerodinamika Razrezhennykh Gazov
    AerTe        Aerojet Technology
    AeIBu        Aerokosmicheski Izsledvaniia B lgariia
    AeJ          Aeronautical Journal
    AeQ          Aeronautical Quarterly
    AeSIJ        Aeronautical Society India Journal
    AerST        Aerosol Science Technology
    AeAm         Aerospace America
    AeCh         Aerospace China
    AeCM         Aerospace Composites and Materials
    AeDy         Aerospace Dynamics
    AeEn         Aerospace Engineering
    AeMat        Aerospace Materials
    AeMed        Aerospace Medicine
    ARBl         Aerospace Research in Bulgaria
    AeTJa        Aerospace Technology Japan
    Aero         Aerospace UK
    AFGL         AFGL-TR-0208 Environemental Research papers
    AfrSk        African Skies
    AGUFM        AGU Fall Meeting Abstracts
    AGUSM        AGU Spring Meeting Abstracts
    AIAAJ        AIAA Journal
    AIASJ        AIAA Student Journal
    AIChE        AIChE Journal
    AIHAJ        AIHA Journal
    AIPA         AIP Advances
    AirSp        Air and Space
    AirCo        Air et Cosmos
    AFMa         Air Force Magazine
    AiInt        Air International
    APCAJ        Air Pollution Control Association Journal
    AirE         Aircraft Engineering
    AkAtP        Akademia Athenon Praktika
    DoArm        Akademiia Nauk Armianskoi SSR Doklady
    DoAze        Akademiia Nauk Azerbaidzhanskoi SSR Doklady
    IzAze        Akademiia Nauk Azerbaidzhanskoi SSR Izvestiia Seriia Fiziko Tekhnicheskikh i Matematicheskikh Nauk
    IFBel        Akademiia Nauk Belorusskoi SSR Institut Fiziki Nauchnaia Sessiia Minsk Belorussian SSR Zhurnal Prikladnoi Spektroskopii
    DoBel        Akademiia Nauk BSSR Doklady
    SoGru        Akademiia Nauk Gruzii Soobshcheniia
    VeKaz        Akademiia Nauk Kazakhskoi SSR Vestnik
    IzLat        Akademiia Nauk Latviiskoi SSR Izvestiia Seriia Fizicheskikh i Tekhnicheskikh Nauk
    IzMol        Akademiia Nauk Moldavskoi SSR Izvestiia Seriia Fiziko Tekhnicheskikh i Matematicheskikh Nauk
    DoSSR        Akademiia Nauk SSSR Doklady
    FizAO        Akademiia Nauk SSSR Fizika Atmosfery i Okeana
    InSSR        Akademiia Nauk SSSR Investiia Mekhanika Zhidkosti i Gaza
    IzFZ         Akademiia Nauk SSSR, Izvestiia, Fizika Zemli
    IzSSR        Akademiia Nauk SSSR Izvestiia Seriia Fizicheskaia
    MeSSR        Akademiia Nauk SSSR Mekhanika Zhidkosti i Gaza
    FiMos        Akademiia Nauk SSSR Otdelenie Obshchei Fiziki i Astronomii Nauchnaia Sessiia Moscow USSR Uspekhi Fizicheskikh Nauk
    IzSib        Akademiia Nauk SSSR Sibirskoe Otdelenie Izvestiia
    SiSSR        Akademiia Nauk SSSR Sibirskoe Otdelenie Izvestiia Seriia Tekhnicheskie Nauki
    KzSib        Akademiia Nauk SSSR Sibirskoi Otdelenie Izvestiia Seriia Tekhnicheskikh Nauk
    VeSSR        Akademiia Nauk SSSR Vestnik
    DoTad        Akademiia Nauk Tadzhikskoi SSR Doklady
    FiSSR        Akademiia Nauk Tadzhikskoi SSR Fiziko Tekhnicheskii Institut Dyushambe Tadzhik SSR Akademiia Nauk Tadzhikskoi SSR Doklady
    IzTur        Akademiia Nauk Turkmenskoi SSR Izvestiia Seriia Fiziko Tekhnicheskikh Khimicheskikh i Geologicheskikh Nauk
    FiUkr        Akademiia Nauk Ukrain skoi RSR Dopovidi Seriia Fiziko Matematichni ta Tekhnichni Nauki
    IzUkr        Akademiia Nauk Ukrainian SSSR Izvestiia Seriia Fizicheskaia
    PrUkr        Akademiia Nauk Ukrains koi RSR Dopovidi Matematika Prirodoznavstvo Tekhnichni Nauki
    DoUkr        Akademiia Nauk Ukrains koi RSR Dopovidi Seriia Fiziko Matematichni ta Tekhnichni Nauki
    ViUkr        Akademiia Nauk Ukrains koi RSR Visnik
    MGUkr        Akademiia Nauk Ukrainskoi SSR Morskie Gidrofizicheskie Issledovaniia
    DoUzb        Akademiia Nauk Uzbekskoi SSR Doklady
    IzUzb        Akademiia Nauk Uzbekskoi SSR Izvestiia Seriia Fiziko Matematicheskikh Nauk
    VeNav        Akademiia Navuk BSSR Vestsi Seryia Fizika Tekhnichnykh Navuk
    AkZh         Akusticheskii Zhurnal
    AkTek        Akustika i Ul trazvukovaia Tekhnika
    AAIzN        Alma Ata Izdatel Nauka
    ALMAN        ALMA Newsletter
    AlFr         Alta Frequenza
    AFRE         Alta Frequenza Rivista di Elettronica
    Ambio        Ambio
    AVSOM        American Association of Variable Stars Observers Monographs
    AVSOR        American Association of Variable Stars Observers Reports
    ACSB         American Ceramic Society Bulletin
    ACSC         American Ceramic Society Communications
    ACSJ         American Ceramic Society Journal
    AHSJ         American Helicopter Society Journal
    AmJC         American Journal of Cardiology
    AJGeo        American Journal of Geoscience
    AmJM         American Journal of Mathematics
    AmJPh        American Journal of Physics
    AmJS         American Journal of Science
    AmJSA        American Journal of Science and Arts
    AmMin        American Mineralogist
    AmSci        American Scientist
    ASME         American Society of Mechanical Engineers
    AnFis        Anales de Fisica
    AnMP         Analysis and Mathematical Physics
    Ana          The Analyst
    AnaCh        Analytical Chemistry
    AnaIn        Analytical Instrumentation
    AAONw        Anglo-Australian Observatory Epping Newsletter
    AAOPr        Anglo-Australian Observatory Epping Preprint
    CSMPA        Ankara Universite Faculte des Sciences Communications Serie Mathematiques Physique et Astronomie
    AASF         Ann. Acad. Sci. Fennicae
    AnStr        Annalen der Kaiserlichen Universitats-Sternwarte in Strassburg
    AnWie        Annalen der K.K. Sternwarte Wien
    AnMun        Annalen der Koeniglichen Sternwarte bei Muenchen
    AnP          Annalen der Physik
    AnWiD        Annalen der Universitaets-Sternwarte Wien, Dritter Folge
    AnMet        Annalen Meteorologie
    AnLei        Annalen van de Sterrewacht te Leiden
    AnAp         Annales d'Astrophysique
    AFLB         Annales de la Fondation Louis de Broglie
    ASSB         Annales de la Societe Scietifique de Bruxelles
    AnCPh        Annales de Chimie et de Physique
    AnG          Annales de Geophysique
    AnIHP        Annales de L'Institut Henri Poincare Section Physique Theorique
    AnTou        Annales de l'Observatoire Astron. et Meteo. de Toulouse
    AnAIK        Annales de l'Observatoire astronomique de l'Université imériale de Kharkow
    AOTok        Annales de l'Observatoire astronomique de Tokyo
    AnZoC        Annales de l'Observatoire astronomique de Zô-sè (Chine)
    AnAPM        Annales de l'Observatoire d'astronomie physique de Paris, Section d'astrophysique, à Meudon
    AnBes        Annales de l'Observatoire de Besancon
    AnBor        Annales de l'Observatoire de Bordeaux
    AnNic        Annales de l'Observatoire de Nice
    AnPar        Annales de l'Observatoire de Paris
    AnPOb        Annales de l'Observatoire de Paris. Observations
    AnOSt        Annales de l'Observatoire de Strasbourg
    AnRio        Annales de l'Observatoire Imperial de Rio de Janeiro
    AnOB         Annales de l'Observatoire Royal de Belgique
    AnOBN        Annales de l'Observatoire Royal de Belgique Nouvelle serie
    AnBru        Annales de l'Observatoire Royal de Bruxelles
    AnPh         Annales de Physique
    AnPCS        Annales de Physique Colloque Supplement
    AnTel        Annales des Telecommunications
    AnGVP        Annales du Bureau des Longitudes, Gauthier-Villars, Paris
    AFChr        Annales Francaises de Chronometrie
    AnGeo        Annales Geophysicae
    AnHP         Annales Henri Poincaré
    AnTec        Annales Tectonicae
    AUGGM        Annales UMCS, Geographia, Geologia, Mineralogia et Petrographia
    AUSPh        Annales UMCS, Sectio AAA: PHYSICA
    AnSAO        Annals of the Astrophysical Observatory of the Smithsonian Institution
    AnBos        Annals of the Bosscha Observatory Lembang (Java) Indonesia
    AnCap        Annals of the Cape Observatory
    AnDea        Annals of the Dearborn Observatory
    AnDud        Annals of the Dudley Observatory
    AIQSY        Annals of the IQSY
    AnIPS        Annals of the Israel Physical Society
    AnLow        Annals of the Lowell Observatory
    NYASA        Annals of the New York Academy of Sciences
    AnLL         Annals of the Observatory of Lucien Libert
    AnLun        Annals of the Observatory of Lund
    AnLuS        Annals of the Observatory of Lund Supplement
    AnOLL        Annals of the Private Observatory of Lucien Libert
    AnEdi        Annals of the Royal Observatory, Edinburgh
    AnSPC        Annals of the Solar Physics Observatory Cambridge England
    AnTok        Annals of the Tokyo Astronomical Observatory
    AnUCP        Annals of the University of Craiova Physics AUC
    AnApS        Annals of Applied Statistics
    AnGp         Annals of Geophysics
    AnGla        Annals of Glaciology
    AnHar        Annals of Harvard College Observatory
    AnMat        Annals of Mathematics
    AnPhy        Annals of Physics
    AnCGH        Annals of Royal Observatory, Cape of Good Hope
    AnSci        Annals of Science
    AnSta        Annals of Statistics
    YalAR        Annual report of the Astronomer of the Winchester Observatory of Yale College
    MMAAR        Annual Report of the Maria Mitchell Association
    ARAOJ        Annual Report of the National Astronomical Observatory of Japan
    WinAR        Annual Report of the Windsor Observatory, New South Wales
    ARAC         Annual Review of Analytical Chemistry
    ARA&A        Annual Review of Astronomy and Astrophysics
    ARCMP        Annual Review of Condensed Matter Physics
    AREPS        Annual Review of Earth and Planetary Sciences
    AnRE         Annual Review of Energy
    AnRFM        Annual Review of Fluid Mechanics
    ARIST        Annual Review of Information Science and Technology
    ARMS         Annual Review of Marine Science
    AnRMS        Annual Review of Materials Science
    ARNPS        Annual Review of Nuclear and Particle Science
    ARPC         Annual Review of Physical Chemistry
    AnMN         Antarctic Meteorite Newsletter
    AMR          Antarctic Meteorite Research
    Antk         Antarktika
    Anten        Antenny
    IORAS        Anuario publicado pelo Imperial Observatorio do Rio de Janeiro Suplemento
    ApAN         Apatity Akademiia Nauk SSSR
    ApKF         Apatity Kol skii Filial AN SSSR
    Apei         Apeiron
    ApMat        Aplikace Matematiky, Applied Mathematics
    AppAn        Applicable Analysis
    ApAc         Applied Acoustics
    ApCM         Applied Composite Materials
    ACESJ        Applied Computational Electromagnetics Society Journal
    ApEn         Applied Energy
    ApEnM        Applied Environmental Microbiology
    ApGeo        Applied Geophysics
    ApHyd        Applied Hydrogeology
    AMat         Applied Mathematics
    ApMM         Applied Mathematics and Mechanics
    ApMaC        Applied Mathematics Computation
    ApMaL        Applied Mathematics Letters
    ApMaM        Applied Mathematics Mechanics English Edition
    ApMaO        Applied Mathematics Optimization
    AMM          Applied Mechanics and Materials
    ApMRv        Applied Mechanics Reviews
    ApMic        Applied Microbiology
    ApMT         Applied Microgravity Technology
    ApNan        Applied Nanoscience
    ApNM         Applied Numerical Mathematics
    ApOpt        Applied Optics
    ApPhy        Applied Physics
    ApPhA        Applied Physics A: Materials Science & Processing
    ApPhB        Applied Physics B: Lasers and Optics
    ApPPL        Applied Physics B Photophysics Laser Chemistry
    ApPhC        Applied Physics Communications
    APExp        Applied Physics Express
    ApPhL        Applied Physics Letters
    ApPhR        Applied Physics Research
    ApScR        Applied Scientific Research
    ApSRA        Applied Scientific Research Section A
    ApSRB        Applied Scientific Research Section B
    ApSpe        Applied Spectroscopy
    ApSRv        Applied Spectroscopy Reviews
    ApSup        Applied Superconductivity
    ApSS         Applied Surface Science
    ApWS         Applied Water Science
    AJSE         Arabian Journal of Science Engineering
    Arch         Archaeoastronomy
    ArchS        Archaeoastronomy Supplement
    ASBTV        Archenhold-Sternwarte Berlin-Treptow, Vortrage Schr.
    ArElU        Archiv Elektronik und Uebertragungstechnik
    ArMaN        Archiv for Mathematik og Naturvidenskab
    AMGBK        Archiv Meteorologie Geophysik und Bioklimatologie Serie B Klimatologie und Umweltmeteorologie Strahlungsforschung
    AMGBS        Archiv Meteorologie Geophysik und Bioklimatologie Serie Meteorologie und Geophysik
    ArMeS        Archiv of Mechanics, Archiwum Mechaniki Stosowanej
    AHES         Archive for History of Exact Sciences
    ArRMA        Archive for Rational Mechanics and Analysis
    AAM          Archive of Applied Mechanics
    ArApM        Archive of Applied Mechanics
    ArAco        Archives Acoustics
    ArS          Archives des Sciences
    ArSPN        Archives des Sciences Physiques et Naturelles
    AMGBA        Archives for Meteorology Geophysics and Bioclimatology Series A Meteorology and Atmopsheric Physics
    AMGBB        Archives for Meteorology Geophysics and Bioclimatology Series B Theoretical and Applied Climatology
    ArNSc        Archives Neerlandaises des Sciences Exactes et Naturelles
    ArTh         Archives of Thermodynamics
    ArTr         Archives of Transport
    ArCom        Archivum Combustionis
    ArAku        Archiwum Akustyki
    ArAuT        Archiwum Automatyki i Telemechaniki
    ArBuM        Archiwum Budowy Maszyn
    ArEle        Archiwum Elektrotechniki
    ArPSp        Archiwum Procesow Spalania
    ArTSp        Archiwum Termodynamiki i Spalania
    AAAR         Arctic, Antarctic and Alpine Research
    ArA          Arkiv for Astronomi
    ArM          Arkiv for Matematik
    ArMAF        Arkiv for Matematik, Astronomi och Fysik
    ArJPh        Armenian Journal of Physics
    ArtSa        Artificial Satellites
    astro ph     ArXiv Astrophysics e-prints
    arXiv        ArXiv e-prints
    gr qc        ArXiv General Relativity and Quantum Cosmology e-prints
    hep ex       ArXiv High Energy Physics - Experiment e-prints
    hep lat      ArXiv High Energy Physics - Lattice e-prints
    hep ph       ArXiv High Energy Physics - Phenomenology e-prints
    hep th       ArXiv High Energy Physics - Theory e-prints
    math ph      ArXiv Mathematical Physics e-prints
    math         ArXiv Mathematics e-prints
    nucl ex      ArXiv Nuclear Experiment e-prints
    nucl th      ArXiv Nuclear Theory e-prints
    physics      ArXiv Physics e-prints
    ASHRA        ASHRAE Journal
    AsJPh        Asian Journal of Physics
    ATJEM        ASME Transactions Journal Engineering Materials and Technology
    ATJDS        ASME Transactions Journal of Dynamic Systems and Measurement Control B
    ATJEl        ASME Transactions Journal of Electronic Packaging
    ATJEG        ASME Transactions Journal of Engineering Gas Turbines and Power
    ATJEP        ASME Transactions Journal of Engineering Power
    ATJFE        ASME Transactions Journal of Fluids Engineering
    ATJHT        ASME Transactions Journal of Heat Transfer
    ATJLT        ASME Transactions Journal of Lubrication Technology
    ATJSE        ASME Transactions Journal of Solar Energy and Engineering
    ATJTr        ASME Transactions Journal of Tribology
    ATJTu        ASME Transactions Journal of Turbomachinery
    ATJVA        ASME Transactions Journal of Vibration Acoustics
    ATJAM        ASME Transactions Series E Journal of Applied Mechanics
    ATMAB        Association Technique Maritime et Aeronautique Bulletin
    ATMAS        Association Technique Maritime et Aeronautique Session Paris France ONERA TP
    Aster        Aster
    StNws        ASTM Standardization News
    AsBio        Astrobiology
    AISAO        Astrofizicheskie Issledovaniia Izvestiya Spetsial'noj Astrofizicheskoj Observatorii
    AISof        Astrofizicheskie Issledovaniya Sofia
    Afz          Astrofizika
    Agrph        The Astrograph
    AAfz         Astrometriia i Astrofizika
    Anews        ASTRON Newsletter
    AsAc         Astronautica Acta
    AsAer        Astronautics Aeronautics
    Asnau        Astronautik
    Astr         The Astronomer
    ATel         The Astronomer's Telegram
    AsUAI        Astronomia. La rivista dell' Unione Astrofili Italiani
    Astnm        Astronomia UAI
    A&AT         Astronomical and Astrophysical Transactions
    USNOM        Astronomical and Meteorological Observations made at the U.S. Naval Observatory
    ACiCh        Astronomical Circular
    ACMan        Astronomical Contributions from the University of Manchester
    TamCo        Astronomical Contributions from the University of South Florida Tampa
    adass        Astronomical Data Analysis Software and Systems
    ADCBu        Astronomical Data Center Bulletin
    AstHe        Astronomical Herald
    AJ           The Astronomical Journal
    AJS          The Astronomical Journal Supplement
    USNOA        Astronomical Observations made at the U.S. Naval Observatory
    UCLAP        Astronomical Papers University of California Los Angeles
    AReg         Astronomical register
    AR&T         Astronomical Research and Technology
    AstRv        The Astronomical Review
    AVest        Astronomicheskii Vestnik
    AVISS        Astronomicheskii Vestnik Issledovaniia Solnechnoi Sistemy
    AZh          Astronomicheskii Zhurnal
    ATsir        Astronomicheskij Tsirkulyar
    KazOB        Astronomicheskoj Observatorii Kazan Byulleten
    AsSch        Astronomie in der Schule
    A&R          Astronomie und Raumfahrt
    AAAN         Astronomische Abhandlungen als Erganzungshefte zu den Astronomische Nachrichten
    AAHam        Astronomische Abhandlungen der Hamburger Sternwarte
    ABMun        Astronomische Beobachtungen angestellt auf der K. Sternwarte zu Bogenhausen bei Muenchen
    ABSBe        Astronomische Beobachtungen auf der Koniglichen Sternwarte zu Berlin
    ABKie        Astronomische Beobachtungen auf der Sternwarte der Koeniglichen Christian-Albrechts-Universitaet zu Kiel
    MiZur        Astronomische Mitteilungen der Eidgenössischen Sternwarte Zurich
    MiBre        Astronomische Mitteilungen der Koeniglichen Universitaets-Sternwarte zu Breslau
    MiGoe        Astronomische Mitteilungen der Universitaets-Sternwarte zu Goettingen
    AN           Astronomische Nachrichten
    ANS          Astronomische Nachrichten Supplement
    MitSZ        Astronomischen Mitteilungen Eidgen. Sternwarte Zurich
    AJB          Astronomischer Jahresbericht
    MiARI        Astronomisches Rechen-Institut Heidelberg Mitteilungen Serie A
    MiARB        Astronomisches Rechen-Institut Heidelberg Mitteilungen Serie B
    ATi          Astronomisk Tidsskrift
    As&Ge        Astronomiya i geodeziya
    Ast          Astronomy
    Astro        Astronomy
    A&A          Astronomy and Astrophysics
    A&AA         Astronomy and Astrophysics Abstracts Heidelberg
    AstAp        Astronomy and Astro-Physics (formerly The Sidereal Messenger)
    A&ARv        Astronomy and Astrophysics Review
    A&AS         Astronomy and Astrophysics Supplement Series
    A&G          Astronomy and Geophysics
    ADIL         Astronomy Data Image Library
    AEdRv        Astronomy Education Review
    AExpr        Astronomy Express
    AstL         Astronomy Letters
    AsNow        Astronomy Now
    AstQ         Astronomy Quarterly
    ARep         Astronomy Reports
    AASPP        Astrononomy and Astrophysics Series
    APh          Astroparticle Physics
    ApNr         Astrophysica Norvegica
    AstBu        Astrophysical Bulletin
    ApInv        Astrophysical Investigations
    ApJ          The Astrophysical Journal
    ApJL         The Astrophysical Journal Letters
    ApJS         The Astrophysical Journal Supplement Series
    ApL          Astrophysical Letters
    ApL&C        Astrophysical Letters and Communications
    Ap           Astrophysics
    ASPRv        Astrophysics and Space Physics Reviews
    Ap&SS        Astrophysics and Space Science
    ApSSP        Astrophysics and Space Science Proceedings
    ApSSS        Astrophysics and Space Science Supplement
    ASTRA        Astrophysics and Space Sciences Transactions
    MKAtl        Astrophysics monographs University of Chicago Press
    ArBei        Astrophysics Reports Publications of the Beijing Astronomical Observatory
    asd  soft    Astrophysics Software Database
    ascl soft    Astrophysics Source Code Library
    ApT          Astrophysics Today
    AstPo        Astropolitics
    ATTTJ        AT T Technical Journal
    BLabR        AT&T Bell Laboratories Record
    AJSEd        Atlas Journal of Science Education
    AtlVS        Atlas Poiskovykh Kart Peremennykh Zvezd
    Atmos        Atmosphere
    AtO          Atmosphere Ocean
    AtOpt        Atmosphere Optics
    ACP          Atmospheric Chemistry & Physics
    ACPD         Atmospheric Chemistry & Physics Discussions
    AtmEn        Atmospheric Environment
    AMT          Atmospheric Measurement Techniques
    AMTD         Atmospheric Measurement Techniques Discussions
    AtmRe        Atmospheric Research
    AtSc         Atmospheric Science
    AtScL        Atmospheric Science Letters
    AtmTe        Atmospheric Technology
    atnf prop    ATNF Proposal
    Atom         Atom
    AD           Atomic Data
    ADNDT        Atomic Data and Nuclear Data Tables
    AtERv        Atomic Energy Review
    AtPhy        Atomic Physics
    AtST         Atomisation Spray Technology
    AtKe         Atomkernenergie
    AtEn         Atomnaia Energiia
    AVET         Atomno Vodorodnaia Energetika i Tekhnologiia
    ATR          ATR Australian Telecommunication Research
    AALST        Atti Accad. Ligure Sci. Lett.
    AAPon        Atti Accad. Pontaniana
    AAST         Atti Accad. Sco. Torino I
    AurPh        Auroral physics
    AuJA         Australian Journal of Astronomy
    AJCh         Australian Journal of Chemistry
    AuJES        Australian Journal of Earth Sciences
    AuJPh        Australian Journal of Physics
    AuJPA        Australian Journal of Physics Astrophysical Supplement
    AuSRA        Australian Journal of Scientific Research A Physical Sciences
    AuMSJ        Australian Mathematical Society Journal Series B -- Applied Mathematics
    AuMM         Australian Meteorological Magazine
    ACTAp        Automatic Control Theory Applications
    Autom        Automatica
    AuRob        Autonomous Robots
    AvSeM        Aviation Space and Environmental Medicine
    AvWST        Aviation Week Space Technology
    AvKos        Aviatsiia i Kosmonavtika
    AvTek        Aviatsionnaia Tekhnika
    AvTel        Avtomatika i Telemekhanika
    AvPE         Avtomatizatsiia Proektirovaniia Elektronike
    Avtme        Avtometriia
    BBUSS        Babes Bolyai Universitas Studia Series Mathematica
    BBUSM        Babes Bolyai Universitas Studia Series Physica
    BaPhL        Balkan Physics Letters
    BaltA        Baltic Astronomy
    BAVRu        BAV Rundbrief
    BAVSR        BAV Rundbrief - Mitteilungsblatt der Berliner Arbeits-gemeinschaft fuer Veraenderliche Sterne
    BAWMN        Bayerische Akademie Wissenschaften mathematisch naturwissenschaftliche Klasse Sitzungsberichte
    BayAn        Bayesian Analysis
    BBCEn        BBC Engineering
    BeSN         Be Star Newsletter
    BRMIC        Behavior Research Methods Instruments and Computers
    BIT          Behaviour & Information Technology
    BUAAJ        Beijing University Aeronautics and Astronautics Journal
    BePl         Beitraege Plasmaphysik
    BeiGe        Beitraege zur Geophysik
    BeiMP        Beitraege zur Mineralogie und Petrographie
    BROGS        Belgian Royal Observatory Communications Series Geophysics Series
    BKAD         Beobachtungen der Kaiserlichen Universitaets-Sternwarte Dorpat
    BKUJ         Beobachtungen der Kaiserlichen Universitaets-Sternwarte Jurjew
    BESBe        Beobachtungs-Ergebnisse der Koniglichen Sternwarte zu Berlin
    ANZi         Beobachtungs-Zirkular der Astronomischen Nachrichten
    BBGPC        Berichte der Bunsen-Gesellschaft Physical Chemistry Chemical Physics Berichte
    BADPG        Berlin East Germany Akademie Verlag GmbH Ergebnisse Plasmaphysik und Gaselektronik
    BAVMM        Berlin East Germany Akademie Verlag GmbH Shriftenreihe des Zentralinstituts Mathematik und Mechanik
    BGBGM        Berlin Gebrueder Borntraeger Geoexploration Monographs Series
    BAVSM        Berliner Arbeitsgemeinschaft fuer Veraenderliche Sterne - Mitteilungen
    BeElM        Beskontaktnye Elektricheskie Mashiny
    AstBa        Biblioteca "Astrei Basarabene"
    BEPM         Bielefeld Encounters in Physics and Mathematics
    BiLuf        Bildmessung und Luftbildwessen
    BioFa        Biofabrication
    BGeo         Biogeosciences
    BGD          Biogeosciences Discussions
    BMNAS        Biographical Memoirs National Academy of Sciences
    BMFRS        Biographical Memoirs of Fellows of the Royal Society
    BiBi         Bioinspiration and Biomimetics
    BMP          Biological and Medical Physics
    BioMa        Biomedical Materials
    Bion         Bionika
    BpJ          Biophysical Journal
    BpBeS        Biophysics and Bioengineering Series
    Biopk        Biophysik
    BioSc        BioScience
    BOTor        Biuletyn Obserwatoium Astronomicznego Uniwersytetu M. Kopernika w Toruniu
    BITad        Biulletini of the Astronomical Institute Akademiia Nauk Tadzhikskoi
    BIAst        Bjull. Inst. Astrofizikii
    BlazD        BLAZAR Data
    BAAA         Boletin de la Asociacion Argentina de Astronomia La Plata Argentina
    BAOM         Boletin de la Astronomico Observatorio de Madrid
    BOTT         Boletin de los Observatorios Tonantzintla y Tacubaya
    BIMAF        Boletin del Instituto de Matematica Astronomica y Fisica Universidad Nacional de Cordoba Argentina
    BITon        Boletin del Instituto de Tonantzintla
    BMOE         Boletin mensual del Observatorio del Ebro
    BlDok        Bolgarska Akademiia Nauk Doklady
    BoSAI        Bollettino della Societa Astronomica Italiana
    BGSA         Bollettino Geod. Scienzi Affini
    BoLMe        Boundary-Layer Meteorology
    BVVSA        Bratislava Veda Vydavatelstvo Slovenskej Akademie Vied
    BFWSG        Braunschweig Friedr Vieweg und Sohn GmbH
    BTUM         Braunschweig Technische Universitaet Mitteilungen
    BrJPh        Brazilian Journal of Physics
    BrWK         Brennstoff Waerme Kraft
    BJHS         The British Journal for the History of Science
    BJAP         British Journal of Applied Physics
    BTE          British Telecommunications Engineering
    BIRM         Brussels Institute Royal Meteorologique de Belgique
    BSSR         AN BSSR Institut Teplo i Massoobmena Vsesoiuznaia Konferentsiia Teplomassoobmenu Minsk Belorussian SSR Preprint
    BuAkK        Budapest Akademiai Kiado
    BlgAJ        Bulgarian Astronomical Journal
    BlGJ         Bulgarian Geophysical Journal
    BlJMH        Bulgarian Journal of Meteorology and Hydrology
    BlJPh        Bulgarian Journal of Physics
    BlJPS        Bulgarian Journal of Physics Supplement
    BlGeo        Bulgarska Akademiia Naukite Geofizichni Institut Izvestiia
    BlTek        Bulgarska Akademiia Naukite Institut Tekhnicheska Kibernetika Izvestiia
    BlMat        Bulgarska Akademiia Naukite Matematicheski Institut Izvestiia
    BlSpi        Bulgarska Akademiia Naukite Spisanie
    BlTse        Bulgarska Akademiia Naukite Tsentralna Laboratoriia Geodeziia Izvestiia
    BlGSp        Bulgarsko Geofizichno Spisanie
    BAFOE        Bulletin Association Fran. Obs. Etoiles Variables
    BuAst        Bulletin Astronomique
    BABel        Bulletin Astronomique de Belgrade
    BuAsR        Bulletin Astronomique, Revue Generale des Travaux Astronomiques
    BuAsI        Bulletin Astronomique, Serie I
    BuChr        Bulletin Chronometrique (Besancon)
    BCSAB        Bulletin Cl. Science Academy Royal de Belgique
    BCrAO        Bulletin Crimean Astrophysical Observatory
    BSAF         Bulletin de la Societe Astronomique de France
    BSAFR        Bulletin de la Societe Astronomique de France et Revue Mensuelle d'Astronomie, de Meteorologie et de Physique du Globe
    BSAL         Bulletin de la Societe Astronomique de Liege
    BSBA         Bulletin de la Societe Belge d'Astronomie
    BSRSL        Bulletin de la Societe Royale des Sciences de Liege
    BMai         Bulletin de la Station Astrophotographique de Mainterne
    BAPSS        Bulletin de l'Academie Polonaise des Sciences Series des Sciences Mathematiques Astronomiques et Physiques
    BARB         Bulletin de l'Academie Royale de Belgique
    AFOEV        Bulletin de l'Association Francaise d'Observateurs d'Etoiles Variables
    BOBeo        Bulletin de l'Observatoire Astronomique de Belgrade
    BBSAG        Bulletin der Bedeckungsveraenderlichen-Beobachter der Schweizerischen Astronomischen Gesellschaft
    BIEBe        Bulletin d'Information d'Etoiles Be
    BIBGI        Bulletin d'Information du Bureau Gravimetrique International
    BICDS        Bulletin d'Information du Centre de Donnees Stellaires
    BCFHT        Bulletin d'information du telescope Canada-France-Hawaii
    BGeod        Bulletin Geodesique
    BGNS         Bulletin Geodesique, Nouvelle Series
    BOPul        Bulletin (Izvestiya) de l'Observatoire Central a Poulkovo
    BuMat        Bulletin Mathematique
    BAAPG        Bulletin of the American Association of Petroleum Geologists
    BAVSO        Bulletin of the American Association of Variable Stars Observers
    BAAS         Bulletin of the American Astronomical Society
    BAMaS        Bulletin of the American Mathematical Society
    BAMS         Bulletin of the American Meteorological Society
    BAPS         Bulletin of the American Physical Society
    BAN          Bulletin of the Astronomical Institutes of the Netherlands
    BANS         Bulletin of the Astronomical Institutes of the Netherlands Supplement Series
    BAICz        Bulletin of the Astronomical Institutes of Czechoslovakia
    BAORB        Bulletin of the Astronomical Observatoire Royale de Belgique
    IllOB        Bulletin of the Astronomical Observatory of the University of Illinois
    BASBr        Bulletin of the Astronomical Society of Brazil
    BASI         Bulletin of the Astronomical Society of India
    BCAIC        Bulletin of the Central Astronomical Institute of Czechoslovakia
    BIMIA        Bulletin of the Institute of Mathematics and Its Applications
    BuIPS        Bulletin of the Israel Physical Society
    BKobO        Bulletin of the Kobe Marine Observatory Kobe Japan
    BLPI         Bulletin of the Lebedev Physics Institute
    BuLMS        Bulletin of the London Mathematical Society
    BRASP        Bulletin of the Russian Academy of Science, Phys.
    BSAst        Bulletin of the Section of Astronomy
    BuSSA        The Bulletin of the Seismological Society of America
    BSAE         Bulletin of the Soviet Antarctic Expedition
    BuONC        Bulletin of the Special Astrophysical Observatory, Northern Caucasus
    BSAO         Bulletin of the Special Astrophysics Observatory
    BTasO        Bulletin of the Tashkent Observatory
    BTok         Bulletin of the Tokyo Astronomical Observatory
    BToIT        Bulletin of the Tokyo Institute of Technology
    BUBes        Bulletin of the University of Besancon Observatory
    BYam         Bulletin of the Yamagata University Yamagata Japan
    YerOB        Bulletin of the Yerkes Observatory of the University of Chicago
    BuGeo        Bulletin of Geosciences
    BKoAS        Bulletin of Korean Astronomical Society
    BPAS         Bulletin of Pure and Applied Science (Physics)
    BVol         Bulletin of Volcanology
    BCNRS        Bulletin Signaletique - Centre National de la Recherche Scientifique
    BIHCD        Bureau Internationale Heure, Paris, Circulaire
    BDus         Byulleten' Instituta Astrofiziki Dushanbe Akademiya Nauk Tadzhikskoj SSR
    BITA         Byulleten' Instituta Teoreticheskoj Astronomii (Leningrad)
    BStaO        Byulleten' Stalinabadskoj Astronomicheskoj Observatorii Akademiya Nauk Tadzhikskoj SSR
    ByuRe        Byurakan Astrophysical Observatory Armenia USSR Reprints
    CahPh        Cahiers de Physique
    CAS          Cambridge Astrophysics Series
    CMPNC        Cambridge Monographs on Particle Physics, Nuclear Physics and Cosmology
    CMPPh        Cambridge Monographs on Plasma Physics
    CTMPC        Cambridge Topics in Mineral Physics and Chemistry
    BCNRC        Canada National Research Council Division Mechanical Engineering National Aeronautical Establishment Quarterly Bulletin
    CASJ         Canadian Aeronautics and Space Journal
    CASJQ        Canadian Aeronautics and Space Journal Quarter
    CEEJ         Canadian Electrical Engineering Journal
    CIPSG        Canadian Information Processing Society Graphics Interface
    CJChE        Canadian Journal of Chemical Engineering
    CaJCh        Canadian Journal of Chemistry
    CaJES        Canadian Journal of Earth Sciences
    CJECE        Canadian Journal of Electrical Computer Engineering
    CaJPh        Canadian Journal of Physics
    CaJPS        Canadian Journal of Physics Supplement
    CaJRS        Canadian Journal of Remote Sensing
    CJSMT        Canadian Journal of Science Mathematics and Technology Education
    CaRes        Cancer Research
    CPhD         Cape Photographic Durchmusterung
    GCRV         Carnegie Institute Washington D.C. Publication
    CarOB        Carter Observatory Wellington New Zealand Astronomical Bulletins
    CASI         CASI Transactions
    CCDA         CCD Astronomy
    CEGB         CEGB Research
    CeMec        Celestial Mechanics
    CeMDA        Celestial Mechanics and Dynamical Astronomy
    Cent         Centaurus
    CBET         Central Bureau Electronic Telegrams
    CEAB         Central European Astrophysical Bulletin
    CEJE         Central European Journal of Engineering
    CEJG         Central European Journal of Geosciences
    CEJPh        Central European Journal of Physics
    CCpFS        Ceskoslovensky Casopis pro Fyziku Sekce
    CKH          Chagyo Kenkyu Hokoku (Tea Research Journal)
    ChNew        Chandra News
    Chaos        Chaos
    CSF          Chaos Solitons and Fractals
    ChCom        Chemical Communications
    ChEnC        Chemical Engineering Communications
    ChEnN        Chemical Engineering News
    ChEnS        Chemical Engineering Science
    ChGeo        Chemical Geology
    CP           Chemical Physics
    CPL          Chemical Physics Letters
    CPSS         Chemical Physics of Solid Surfaces
    CPR          Chemical Physics Reports
    ChEG         Chemie der Erde / Geochemistry
    CEJ          Chemistry A European Journal
    ChOE         China Ocean Engineering
    ChRST        China Rept Sci Technol JPRS CST
    ChA          Chinese Astronomy
    ChA&A        Chinese Astronomy and Astrophysics
    ChIEJ        Chinese Institute of Engineers Journal
    ChJA         Chinese Journal of Aeronautics
    ChJAA        Chinese Journal of Astronomy and Astrophysics
    ChJAS        Chinese Journal of Astronomy and Astrophysics Supplement
    ChJCP        Chinese Journal of Chemical Physics
    ChJG         Chinese Journal of Geophysics
    ChJIR        Chinese Journal of Infrared Research
    ChJL         Chinese Journal of Lasers
    ChJLB        Chinese Journal of Lasers B
    CJLTP        Chinese Journal of Low Temperature Physics
    ChJME        Chinese Journal of Mechanical Engineering
    ChJNP        Chinese Journal of Nuclear Physics
    ChJOL        Chinese Journal of Oceanology and Limnology
    ChJPh        Chinese Journal of Physics
    ChJS         Chinese Journal of Semiconductors
    ChJSS        Chinese Journal of Space Science
    ChOpL        Chinese Optics Letters
    ChPhy        Chinese Physics
    ChPhB        Chinese Physics B
    ChPhC        Chinese Physics C
    ChPhL        Chinese Physics Letters
    ChSBu        Chinese Science Bulletin
    ChSAJ        Chinese Society of Astronautics Journal
    ChSMJ        Chinese Society of Mechanical Engineers Journal
    ChSST        Chinese Space Science Technology
    CMDRG        Chislennye Metody Dinamike Razrezhennykh Gazov
    CHOCS        CHOCS
    CITM         Chubu Institute Technology Memoirs
    CIDA         CIDA
    Ciel         Le Ciel
    C&E          Ciel et Espace
    C&T          Ciel et Terre
    CTE          Ciencias de la Tierra y del Espacio
    CiInf        Circ. Inf.
    CiSSV        Circolare Interna della Sezione Stelle Variabili dell'Unione Astrofili Italiani
    CSSP         Circuits Systems and Signal Processing
    CiBAA        Circular of the British Astronomical Association
    CiUO         Circular of the Union Observatory Johannesburg
    CiPoJ        Circumpolar Journal
    CQGra        Classical and Quantum Gravity
    CCM          Clays and Clay Minerals
    ClDy         Climate Dynamics
    CliPa        Climate of the Past
    CliPD        Climate of the Past Discussions
    ClCh         Climatic Change
    CPPM         Clinical Physics and Physiological Measurement
    CNRAe        CNR Aeritalia S
    CODAB        CODATA Bulletin
    Coel         Coelum Periodico Bimestrale per la Divulgazione dell'Astronomia
    ColSu        Colloids and Surfaces
    CoFl         Combustion and Flame
    CST          Combustion Science and Technology
    CTM          Combustion Theory Modelling
    CNSMP        Comet News Service, McDonnell Planetarium
    CPMCM        Commentationes Physico-Mathematicae et Chemico-Medicae
    ComMP        Comments in Modern Physics
    ComAp        Comments on Astrophysics
    CoASP        Comments on Astrophysics and Space Physics
    CoAMP        Comments on Atomic and Molecular Physics
    CoCMP        Comments on Condensed Matter Physics
    CoNPP        Comments on Nuclear and Particle Physics
    CoPPC        Comments on Plasma Physics and Controlled Fusion
    ComSp        Commercial Space
    CoKon        Commmunications of the Konkoly Observatory Hungary
    CAPJ         Communicating Astronomy with the Public Journal
    ComBr        Communication Broadcasting
    Commu        Communications
    CoORB        Communications de l'Observatoire Royal de Belgique
    MonAP        Communications du Departement d'Astrophysique de la Faculte des Sciences de Mons Mons Astrophysical Papers
    CoDDO        Communications from the David Dunlap Observatory
    CoROE        Communications from the Royal Observatory Edinburgh
    CoStA        Communications from the University Observatory St Andrews Scotland
    CEST         Communications Gillies Inc Electronic Systems in Transportation
    CANM         Communications in Applied Numerical Methods
    CoAst        Communications in Asteroseismology
    CCoPh        Communications in Computational Physics
    CMaPh        Communications in Mathematical Physics
    CNSNS        Communications in Nonlinear Science and Numerical Simulations
    CNME         Communications in Numerical Methods in Engineering
    CPAM         Communications in Pure Applied Mathematics
    CoTPh        Communications in Theoretical Physics
    CoAnk        Communications of the Department of Astronomy of Ankara University
    CoLPL        Communications of the Lunar and Planetary Laboratory
    CoLon        Communications of the University of London Observatory
    CRLJ         Communications Research Laboratory Journal
    CRLRv        Communications Research Laboratory Review
    ComSo        Communications Society
    CmpSt        Composite Structures
    Compo        Composites
    CmpEn        Composites Engineering
    CmpMa        Composites Manufacturing
    ComST        Composites Science Technology
    CRSPH        Compte Rendu des Seances de la Societe de Physique et d'Histoire Naturelle de Geneve
    CR           Comptes Rendus Academie des Sciences (serie non specifiee)
    CRASE        Comptes Rendus de l'Académie des Sciences - Series IIA - Earth and Planetary Science
    CRABS        Comptes Rendus de l'Academie Bulgare des Sciences
    CRGeo        Comptes Rendus Geoscience
    CRMat        Comptes Rendus Mathematique
    CRMec        Comptes Rendus Mecanique
    CRPhy        Comptes Rendus Physique
    ComMS        Computational Materials Science
    CMMPh        Computational Mathematics and Mathematical Physics
    CompM        Computational Mechanics
    CS&D         Computational Science and Discovery
    CSMA         Computational Structural Mechanics and Applications
    Compr        Computer
    CGIP         Computer Graphics Image Processing
    CompJ        The Computer Journal
    CMAME        Computer Methods in Applied Mechanics and Engineering
    CoPhC        Computer Physics Communications
    CoPhR        Computer Physics Reports
    CSEd         Computer Science Education
    CVGIP        Computer Vision Graphics and Image Processing
    CAD          Computer-Aided Design
    CEE          Computers and Electrical Engineering
    CF           Computers and Fluids
    CG           Computers and Geosciences
    CMwA         Computers and Mathematics with Applications
    CoStr        Computers and Structures
    ComPh        Computers in Physics
    Compu        Computing
    CSE          Computing in Science and Engineering
    ComSE        Computing Systems in Engineering
    COMTR        COMSAT Technical Review
    CoCoi        Comunicacoes do Observatonio Astronomico da Universidade de Coimbra
    CoMRA        Concepts in Magnetic Resonances A
    CoMRB        Concepts in Magnetic Resonances B
    CMPhy        Condensed Matter Physics
    CGDAM        Conformal Geometry and Dynamics of the American Mathematical Society
    ConSc        Connection Science
    CoFra        Consiglio Nazionale delle Ricerche Italia. Laboratorio di Astrofisica Frascati Roma Contributi
    ConCP        Contemporary Concepts in Physics
    ConPh        Contemporary Physics
    CSR          Continental Shelf Research
    CMT          Continuum Mechanics and Thermodynamics
    CoIAP        Contributions de l'Institut d'Astrophysique de Paris Serie A
    CoAsi        Contributions dell'Osservatorio Astrofisica dell'Universita di Padova in Asiago
    CoMil        Contributions dell'Osservatorio Astrononia di Milano-Merate
    CoThe        Contributions from the Astronomical Department of the University of Thessaloniki
    CoBos        Contributions from the Bosscha Observervatory
    CoCam        Contributions from the Cambridge Observatory England
    CoTol        Contributions from the Cerro Tololo Inter-American Observatory
    CoTok        Contributions from the Department of Astronomy University of Tokyo
    CoDAO        Contributions from the Dominion Astrophysical Observatory in Victoria
    CoDun        Contributions from the Dunsink Observatory Dublin Ireland
    CoKyo        Contributions from the Institute of Astrophysics and Kwasan Observatory Kyoto
    CoKit        Contributions from the Kitt Peak National Observatory
    CoKwa        Contributions from the Kwasan and Hida Observatories University of Kyoto
    CoMcD        Contributions from the McDonald Observatory University of Texas Fort Davis
    CMWCI        Contributions from the Mount Wilson Observatory / Carnegie Institution of Washington
    CoPri        Contributions from the Princeton University Observatory
    CoRut        Contributions from the Rutherford Observatory of Columbia University New York
    CoWas        Contributions from the Washburn Observatory of the University of Wisconsin
    CoSka        Contributions of the Astronomical Observatory Skalnate Pleso
    CoSkL        Contributions of the Astronomical Observatory Skalnate Pleso Letters
    CoSkS        Contributions of the Astronomical Observatory Skalnate Pleso Supplement
    CoLou        Contributions of the Louisiana State University Observatory Baton Rouge Louisiana
    CoBrn        Contributions of the Public Observatory and Planetarium in Brno
    CSASG        Contributions of the Slovak Academy Sciences Geophysical Institute
    CoWat        Contributions of the University of Waterloo Observatory
    CoVVO        Contributions of the Van Vleck Observatory
    CoLic        Contributions of Lick Observatory
    CLic2        Contributions of Lick Observatory, Series II
    CoPer        Contributions of Perkins Observatory
    ConAP        Contributions to Atmospheric Physics/Beitraege zur Physik Atmosphaere
    CoGG         Contributions to Geophysics and Geodesy
    CoMP         Contributions to Mineralogy and Petrology
    CoPP         Contributions to Plasma Physics
    CoCom        Control and Computers
    CorRe        Coral Reefs
    CAGHS        Correspondance Astronomique, Geographique, Hydrographique et statistique
    CosEl        Cosmic Electrodynamics
    CosRe        Cosmic Research
    CosSe        Cosmic Search
    CRB          C.R. Acad. Sci. Ser. B1
    CRSSM        Critical Reviews in Solid State & Materials Sciences
    Cryo         Cryogenics
    TCD          The Cryosphere Discussions
    CryRp        Crystallography Reports
    CSSE         Cultural Studies of Science Education
    CuCo         Culture and Cosmos
    CAP          Current Applied Physics
    CNan         Current Nanoscience
    COSSM        Current Opinion in Solid State and Materials Science
    CSci         Current Science
    CzJPh        Czechoslovak Journal of Physics
    CzJPS        Czechoslovak Journal of Physics Supplement
    CzMJ         Czechoslovak Mathematical Journal
    DatSJ        Data Science Journal
    DSRI         Deep Sea Research Part I: Oceanographic Research
    DSR          Deep Sea Research Part II: Topical Studies in Oceanography
    DSNPR        Deep Space Network Progress Report
    Defek        Defektoskopiia
    DefEl        Defense Electronics
    DMJ          Defense Management Journal
    DeScE        Defense Science Electronics
    DSJ          Defense Science Journal
    DSRMC        Defense Systems Review Military Communications
    DSSN         Delta Scuti Star Newsletter
    Sterb        Der Sternenbote Monatsschrift fuer Oesterreichs Amateur-astronomen
    DGKBA        Deutsche Geodaetische Kommission Bayer. Akad. Wiss.
    DGKBB        Deutsche Geodaetische Kommission Bayer. Akad. Wiss. B
    DGKGN        Deutsche Geodaetische Kommission Gravity Network West Germany DSGN Data Adjustment
    DeHyZ        Deutsche Hydrographische Zeitschrift
    DPhyG        Deutsche Physikalische Gesellschaft
    DFVLR        DFVLR
    DRM          Diamond and Related Materials
    DnU          Differentsial nye Uravneniia
    DSP          Digital Signal Processing
    Dimen        Dimensions
    DiSis        Dinamicheskie Sistemy
    DPM          Dinamika i Prochnost Mashin
    DiRaG        Dinamika razrezhennykh gazov
    DIO          DIO
    DISA         DISA Information
    Disc         Discover
    DImTe        Display Imaging Technology
    Displ        Displays
    DSE          Distributed Systems Engineering
    DLGRM        DLGR Magnetofluiddyn
    Dlib         D-Lib Magazine
    DLRNa        DLR Nachrichten
    DOIAP        Documentation des Observateurs Institut d'Astrophysique de Paris
    DokAN        Doklady Akad Nauk Minerologia USSR
    DoANT        Doklady Akademiia Nauk TadzhSSR
    DoBan        Doklady Bolgarskoi Akademiia Nauk
    DokES        Doklady Earth Sciences
    DorPo        Dornier Post
    DSO          Double Star Observer
    DSSC         Double Star Section Circulars
    DudOR        Dudley Observatory Reports
    PODE         Dun Echt Observatory Publications
    DunOP        Dunsink Observatory Publications
    DunRe        Dunsink Observatory Reprints
    IzDus        Dushanbe Izdatel Donish
    DynCo        Dynamics and Control
    DyAtO        Dynamics of Atmospheres and Oceans
    EaEvS        Earth and Evolution Sciences
    EExSc        Earth and Extraterrestrial Sciences
    E&PSL        Earth and Planetary Science Letters
    E&S          Earth in Space
    EaInt        Earth Interactions
    EM&P         Earth Moon and Planets
    EP&S         Earth, Planets, and Space
    ESRv         Earth Science Reviews
    ESPL         Earth Surface Processes and Landforms
    ESD          Earth System Dynamics
    ESDD         Earth System Dynamics Discussion
    ESSD         Earth System Science Data
    ESSDD        Earth System Science Data Discussions
    EOAST        Earth-Oriented Applications and Space Technology
    EEEV         Earthquake Engineering and Engineering Vibration
    EaSci        Earthquake Science
    EERSA        East Europe Rept Sci Affairs JPRS
    EERST        East European Rept Sci. Technol. JPRS ESA
    EBCi         Eclipsing Binaries Circulars
    EcGH         Eclogae geologae Helvetii
    EcGou        Ecole de Goutelas
    Earth        eEarth
    EartD        eEarth Discussions
    ETATF        Eesti NSV Teaduste Akadeemia Toimetised Fuusika Matemaatika
    EJSM         e-Journal of Soft Materials
    OED          El Observador de Estrellas Dobles
    ElUn         El Universo
    Elast        Elastic
    ECLRv        Electrical Communication Laboratories Review
    JElEn        Electrical Engineering of Japan
    EOSD         Electro Optical Systems Design
    Elecm        Electromagnetics
    EJSta        Electronic Journal of Statistics
    EJTP         Electronic Journal of Theoretical Physics
    EML          Electronic Materials Letters
    ElPro        Electronic Progress
    JElCo        Electronics Communications of Japan
    ElL          Electronics Letters
    ElP          Electronics Power
    ElLC         Electrotechnical Laboratory Circulars
    ElW          Electrowaerme International
    ElBah        Elektrische Bahnen
    E&E          Elektromashinostroenie i Elektrooborudovanie
    Elem         Elektromekhanika
    Elek         Elektronika
    ElTA         Elektronnaia Tekhnika Avtomatike
    ElMod        Elektronnoe Modelirovanie
    ETRE         Elektrosviaz Telecommunications Radio Engineering Telecommunications
    E&M          Elektrotechnik und Maschinenbau
    EVest        Elektrotehniski Vestnik
    EMCT         EMC Technology
    EBBT         Emerging Biochemical and Biophysical Techniques
    Endvr        Endeavour
    Energ        Energetika
    EnAt         Energia es Atomtechnika
    EnUK         Energy
    EnC          Energy Conversion
    ECM          Energy Conversion Management
    EnTR         Energy Technology Review
    EngAn        Engineering Analysis
    EnSci        Engineering and Science
    EngCo        Engineering Computations
    EnFM         Engineering Fracture Mechanics
    EnOp         Engineering Optimization
    CEnTp        Engineering Thermophysics China
    Entro        Entropie
    Entrp        Entropy
    EES          Environmental Earth Sciences
    EnEng        Environmental Engineering
    EFM          Environmental Fluid Mechanics
    EnGeo        Environmental Geology
    EnMan        Environmental Management
    ER           Environmental Research
    ERL          Environmental Research Letters
    EnST         Environmental Science Technology
    ETWQ         Environmental Toxicology and Water Quality
    EOSTr        EOS Transactions
    EL           EPL (Europhysics Letters)
    EPRIJ        EPRI Journal
    AnErg        Ergaenzungshefte zu den Astronomischen Nachrichten
    ErNW         Ergebnisse der exakten Naturwissenschaften
    ESABu        ESA Bulletin
    ESAHR        ESA History Study Reports
    EIUEN        ESA IUE Newsletter
    ESAJ         ESA Journal
    ESASM        ESA Scientific & Technical Memoranda
    ESAST        ESA Scientific Technical Review
    ESATM        ESA Training Manual
    EssPh        Essays in Physics
    ECSS         Estuarine Coastal and Shelf Science
    EUCAS        EUCASS Proceedings Series
    EurSS        Eurasian Soil Science
    EJASP        EURASIP Journal on Applied Signal Processing
    ERST         Europe Report Science Technology
    EJMF         European Journal of Mechanics B Fluids
    EJMS         European Journal of Mechanics Solids
    EJPh         European Journal of Physics
    EPJA         European Physical Journal A
    EPJAS        European Physical Journal A Supplement
    EPJAP        European Physical Journal Applied Physics
    EPJB         European Physical Journal B
    EPJC         European Physical Journal C
    EPJCS        European Physical Journal C Supplement
    EPJD         European Physical Journal D
    EPJE         European Physical Journal E
    EPJH         European Physical Journal H
    EPJP         European Physical Journal Plus
    EPJST        European Physical Journal Special Topics
    EuRv         European Review
    ESN          European Science Notes
    ESOB         European Southern Observatory ESO Bulletin
    ESOSP        European Southern Observatory Scientific Preprints
    ESOSR        European Southern Observatory Scientific Report
    ETTRT        European Transactions Telecommunications Related Technologies
    ENews        Europhysics News
    EXOSA        EXOSAT Express
    ExA          Experimental Astronomy
    ExHT         Experimental Heat Transfer
    ExM          Experimental Mechanics
    ExT          Experimental Techniques
    ExTFS        Experimental Thermal Fluid Science
    ExFl         Experiments in Fluids
    ExG          Exploration Geophysics
    Extr         Extraction
    PMtv         Facultad de Humanidades y Ciencias Universidad de la Republica Montevideo
    FaDi         Faraday Discussions
    FaTr         Faraday Transactions
    FFEMS        Fatigue and Fracture of Engineering Materials and Structures
    F&M          Feinwerktechnik und Messtechnik
    FBS          Few-Body Systems
    FiIO         Fiber and Integrated Optics
    FizEl        Fizicheskaia Elektronika
    FiMek        Fizicheskaia Mekhanika
    Fiz          Fizika
    FizA         Fizika A
    FizAS        Fizika Aerodispersnykh Sistem
    FizB         Fizika B
    FizGV        Fizika Goreniia i Vzryva
    FizKO        Fizika i Khimiia Obrabotki Materialov
    FizTV        Fizika i Tekhnika Vysokikh Davlenii
    FizMM        Fizika Metallov i Metallovedenie
    FizMS        Fizika Mnogochastichnykh Sistem
    FizNT        Fizika Nizkikh Temperatur
    FizPl        Fizika Plazmy
    FizSz        Fizika Sz.
    FizTT        Fizika Tverdogo Tela
    FizZS        Fizika Zhidkogo Sostoianiia
    FizKM        Fiziko Khimicheskaia Mekhanika Materialov
    FizCh        Fizyki i Chemii Seria Fizyka
    F&CRe        Flower and Cook Observatory Reprints
    FRFI         Flug Revue Flugwelt International
    FlDy         Fluid Dynamics
    FlDyR        Fluid Dynamics Research
    FlDyT        Fluid Dynamics Transactions
    FlMSR        Fluid Mechanics Soviet Research
    Fluid        Fluidika
    FluQ         Fluids Quarterly
    F&I          Forschung im Ingenieurwesen
    F&IER        Forschung im Ingenieurwesen Engineering Research
    ForPh        Fortschritte der Physik
    FoGeo        Fotointerpretacja w Geografii
    FoPh         Foundations of Physics
    FoPhL        Foundations of Physics Letters
    Fract        Fractals
    Freq         Frequenz
    FrES         Frontiers of Earth Science
    FrMS         Frontiers of Materials Science
    FrME         Frontiers of Mechanical Engineering
    FrPhy        Frontiers of Physics
    FrPhC        Frontiers of Physics in China
    IzFru        Frunze Izdatel Ilim
    FSTJ         Fujitsu Scientific Technical Journal
    FST          Fullerene Science and Technology
    FML          Functional Materials Letters
    FACM         Functiones et Approximatio Commentarii Mathematici
    OOPS         Fundamental nye Osnovy Opticheskoi Pamiati i Sredy
    FTP          Fundamental Theories of Physics
    FCPh         Fundamentals of Cosmic Physics
    Futur        Future Spring
    Gaea         Gaea - Journal of Geoscience
    GCNew        Galactic Center Newsletter
    galx prop    GALEX Proposal
    GalEl        Galilean Electrodynamics
    GGMit        Gauss-Gesellschaft e.V. Göttingen, Mitteilungen
    GazA         Gazette Astronomique
    GazAM        Gazette Astronomique Memoires
    GazT         Gazodinamika i Teploobmen
    GCNR         GCN Report
    GECJR        GEC Journal Research
    Gelio        Geliotekhnika
    Gemin        GEMINI Newsletter Royal Greenwich Observatory
    GReGr        General Relativity and Gravitation
    GeoIn        Geocarto International
    GeocJ        Geochemical Journal
    Geoch        Geochemistry
    GGG          Geochemistry, Geophysics, Geosystems
    GeocI        Geochemistry International
    GeCoA        Geochimica et Cosmochimica Acta
    GeCAS        Geochimica et Cosmochimica Acta Supplement
    GeCar        Geodesy and Cartography
    GeAer        Geodeziia i Aerofotos
    GeKar        Geodeziia i Kartografiia
    GKA          Geodeziia i Kartografiia Aehrofotosemka, L'vov
    GeKaA        Geodeziia Kartografiia i Aerofotos
    GeoK         Geodezja i Kartografia
    GeoAc        Geodinamica Acta
    GeofI        Geofisica Internacional
    GeoPA        Geofisica Pura e Applicata
    GeoSb        Geofizicheskii Sbornik
    GeoZh        Geofizicheskii Zhurnal
    GeIss        Geoinformation Issues
    Geokh        Geokhimiia
    GCarp        Geologica Carpathica
    GeoM         Geological Magazine
    GeoSJ        Geological Society Journal
    GSAB         Geological Society of America Bulletin
    GSAMm        Geological Society of America Memoir
    GSASP        Geological Society of America Special Papers
    GSLSP        Geological Society of London Special Publications
    Geolo        Geologija
    GeoRu        Geologische Rundschau
    Geolg        Geologos
    Geo          Geology
    GeoOD        Geology of Ore Deposits
    Ge&Ae        Geomagnetism and Aeronomy/Geomagnetizm i Aeronomiia
    GeoIs        Geomagnitnye Issledovaniia
    GML          Geo-Marine Letters
    Geomo        Geomorphology
    Geoph        Geophysica
    GeGe         Geophysica et Geodaetica
    GeoNr        Geophysica Norvegica
    GApFD        Geophysical and Astrophysical Fluid Dynamics
    GDS          Geophysical Developments Series
    GeoJ         Geophysical Journal
    GeoJI        Geophysical Journal International
    GeopP        Geophysical Prospecting
    GeoRL        Geophysical Research Letters
    GeoSu        Geophysical Surveys
    Geop         Geophysics
    GAM          Geophysics and Astrophysics Monographs
    GEOCE        GEOS Circular on Eclipsing Binaries
    GEOCR        GEOS Circular on RR Lyr Type Variables
    GEOCA        GEOS Circular on Small-Amplitude Variables
    GEOSN        GEOS Note Circulaire
    GSDJ         Geoscience Data Journal
    GSEng        GeoScience Engineering
    GI           Geoscientific Instrumentation, Methods and Data Systems
    GID          Geoscientific Instrumentation, Methods and Data Systems Discussions
    GMD          Geoscientific Model Development
    GMDD         Geoscientific Model Development Discussions
    Geote        Geotectonics
    TrGRC        Geothermal Resources Council Transactions
    Geoth        Geothermics
    Geot         Geotimes
    Gerb         Gerbertvs, International Academic Publication on History of Medieval Science
    GBzG         Gerlands Beitraege zur Geophysik
    GUL          Geschichte und Lichtwechsel der Veraenderlichen Sterne (Potsdam)
    GATAN        Gesellschaft Aerosolforschung Tagung ueber Aerosole Naturwissenschaft Medizin und Technik Messtechnik und technische Anwendung
    GMMWJ        Gesellschaft angewandte Mathematik und Mechanik Jahrestagung Goettingen West Germany Zeitschrift Flugwissenschaften
    GaMuM        Gesellschaft Angewandte Mathematik und Mechanik Workshop Paris France
    GMuD         Gesellschaft Mathematik und Datenverarbeitung mbH Multigrid Methods Special Topics Applications
    GVMK         Gibridnye Vychislitel nye Mashiny i Kompleksy
    Gidro        Gidromekhanika
    GiGi         Gidroprivod i Gidropnevmoavtomatika
    GiSan        Gigiena i Sanitariia
    GTPZ         Gigiena Truda i Professional nye Zabolevaniia
    GAst         Giornale di Astronomia
    GPC          Global and Planetary Change
    GBioC        Global Biogeochemical Cycles
    GPSW         GPS World
    GrCo         Gravitation and Cosmology
    GrTOn        Gravitatsiia i Teoriia Otnositel nosti
    GCN          GRB Coordinates Network
    GGMM         Greenhouse Gas Measurement & Management
    GriO         Griffith Observer
    GrAeH        Grumman Aerospace Horizons
    Grund        Grundwasser
    HadJ         Hadronic Journal
    HadJS        Hadronic Journal Supplement
    LS           Hamburger Sternw. Warner & Swasey Obs.
    BSD          Hamburger Sternwarte Bergedorf
    HamS         Hamburger Sternwarte Sonderdrucke
    HAAG         Handbook of Astronomy Astrophysics and Geophysics
    HPCRE        Handbook on the Physics and Chemistry of Rare Earths
    HDA          Handbuch der Astrophysik
    HDP          Handbuch der Physik
    HarZi        Harthaer Beobachtungs-Zirkular
    HarAC        Harvard College Observatory Announcement Card
    BHarO        Harvard College Observatory Bulletin
    HarCi        Harvard College Observatory Circular
    HarRe        Harvard College Observatory Reprints
    HarMo        Harvard Observatory Monographs
    HeaPh        Health Physics
    HMT          Heat and Mass Transfer
    HTrEn        Heat Transfer Engineering
    HTJR         Heat Transfer Japanese Research
    HTSR         Heat Transfer Soviet Research
    Heavn        Heavens
    HMR          Helgoland Marine Research
    HWM          Helgoländer Wissenschaftliche Meeresuntersuchungen
    AcHPh        Helvetica Physica Acta
    AcHPS        Helvetica Physica Acta Supplementum
    HelOB        Helwan Institute of Astronomy and Geophysics Bulletins
    HemD         Hemel en Dampkring
    HEDP         High Energy Density Physics
    HEPNP        High Energy Physics and Nuclear Physics
    HPR          High Pressure Research
    HiTec        High Technology
    HTemS        High Temperature Science
    HTHP         High Temperatures and High Pressures
    HiA          Highlights of Astronomy
    HARSB        Histoire de l'Academie Royale des Sciences et des Belles-Lettres de Berlin
    HGSS         History of Geo- and Space Sciences
    HisSc        History of Science
    HUFEB        Hokkaido University Faculty Engineering Bulletin
    HUFEM        Hokkaido University Faculty Engineering Memoirs
    HWP          Horizons in World Physics
    LHBl         La Houille Blanche
    HCHy         Hovering Craft and Hydrofoil
    HvaOB        Hvar Observatory Bulletin
    HvOBS        Hvar Observatory Bulletin Supplement
    HyBio        Hydrobiologia
    HydJ         Hydrogeology Journal
    HyPr         Hydrological Processes
    HESS         Hydrology and Earth System Sciences
    HESSD        Hydrology and Earth System Sciences Discussions
    HyInt        Hyperfine Interactions
    IadEn        Iadernaia Energiia
    BSEEA        Iasi Institutul Politehnic Buletinul Sectia Electrotehnica Electronica Automatizari
    BSMMT        Iasi Institutul Politehnic Buletinul Sectia Matematica Mecanica Teoretica Fizica
    BSMT         Iasi Institutul Politehnic Buletinul Sectia Mecanica Tehnica
    IAUCB        IAU Commission on Close Binary Stars
    IAUDS        IAU Commission on Double Stars
    IAUIn        IAU Commission on Instruments
    IAUGA        IAU General Assembly
    IAUIB        IAU Information Bulletin
    IAUSS        IAU Special Session
    WFINw        IAU Working Group on Wide-Field Imaging, Newsletter
    IBMJ         IBM Journal of Research and Development
    ICAOB        ICAO Bulletin
    Icar         Icarus
    JMOA         IEE Journal of Microwaves Optics and Acoustics
    JSSED        IEE Journal of Solid-State Electron Devices
    IPEPA        IEE Proceedings B: Electric Power Applications
    IPGTD        IEE Proceedings C: Generation Transmission Distribution
    IPCSV        IEE Proceedings: Communications Speech and Vision
    IPCTA        IEE Proceedings D: Control Theory Applications
    IPCDT        IEE Proceedings E: Computers and Digital Techniques
    IPCRS        IEE Proceedings F: Communications Radar and Signal Processing
    IPRSP        IEE Proceedings F: Radar and Signal Processing
    IPMAP        IEE Proceedings H: Microwaves Antennas and Propagation
    IPMOA        IEE Proceedings H: Microwaves Optics and Antennas
    IPOpt        IEE Proceedings J: Optoelectronics
    IPPSM        IEE Proceedings: Physical Science Measurement and Instrumentation Management and Education Reviews
    IPSSE        IEE Proceedings: Solid-State Electron Devices
    IEERv        IEE Reviews
    IAESM        IEEE Aerospace Electronic Systems Magazine
    IAWPL        IEEE Antennas and Wireless Propagation Letters
    IAPM         IEEE Antennas Propagation Magazine
    IASSP        IEEE ASSP Magazine
    ICiSM        IEEE Circuits Systems Magazine
    IComM        IEEE Communications Magazine
    ICSEn        IEEE Computational Science and Engineering
    ICGA         IEEE Computer Graphics Applications
    ICSM         IEEE Computer Systems Magazine
    IDTC         IEEE Design Test Computers
    IEDL         IEEE Electron Device Letters
    IExp         IEEE Expert
    IGRSL        IEEE Geoscience and Remote Sensing Letters
    IISys        IEEE Intelligent Systems
    IJOE         IEEE Journal of Oceanic Engineering
    IJQE         IEEE Journal of Quantum Electronics
    IJRA         IEEE Journal of Robotics Automation
    ISTSP        IEEE Journal of Selected Topics in Signal Processing
    IJSSC        IEEE Journal of Solid-State Circuits
    IJSAC        IEEE Journal on Selected Areas in Communications
    ILCSM        IEEE LCS Magazine
    ILTS         IEEE LTS
    IMGWL        IEEE Microwave and Guided Wave Letters
    IMMag        IEEE Microwave Magazine
    IEEEN        IEEE Network
    IPTL         IEEE Photonics Technology Letters
    IEEEP        IEEE Proceedings
    ISPL         IEEE Signal Processing Letters
    ISPM         IEEE Signal Processing Magazine
    IEEES        IEEE Spectrum
    ISysJ        IEEE Systems Journal
    ITASS        IEEE Transactions on Acoustics Speech and Signal Processing
    ITAES        IEEE Transactions on Aerospace Electronic Systems
    ITAP         IEEE Transactions on Antennas and Propagation
    ITAS         IEEE Transactions on Applied Superconductivity
    ITAC         IEEE Transactions on Automatic Control
    ITBE         IEEE Transactions on Biomedical Engineering
    ITB          IEEE Transactions on Broadcasting
    ITCS         IEEE Transactions on Circuits Systems
    ITCom        IEEE Transactions on Communications
    ITCHM        IEEE Transactions on Components Hybrids and Manufacturing Technology
    ITCAD        IEEE Transactions on Computer Aided Design
    ITCmp        IEEE Transactions on Computers
    ITEdu        IEEE Transactions on Education
    ITEI         IEEE Transactions on Electrical Insulation
    ITElC        IEEE Transactions on Electromagnetic Compatibility
    ITED         IEEE Transactions on Electron Devices
    ITEnC        IEEE Transactions on Energy Conversion
    ITEM         IEEE Transactions on Engineering Management
    ITGRS        IEEE Transactions on Geoscience and Remote Sensing
    ITGE         IEEE Transactions on Geoscience Electronics
    ITIP         IEEE Transactions on Image Processing
    ITIE         IEEE Transactions on Industrial Electronics
    ITIEC        IEEE Transactions on Industrial Electronics and Control Instrumentation
    ITIA         IEEE Transactions on Industry Applications
    ITIT         IEEE Transactions on Information Theory
    ITIM         IEEE Transactions on Instrumentation Measurement
    ITM          IEEE Transactions on Magnetics
    ITMTT        IEEE Transactions on Microwave Theory Techniques
    ITME         IEEE Transactions on Military Electronics
    ITNan        IEEE Transactions on Nanotechnology
    ITNN         IEEE Transactions on Neural Networks
    ITNS         IEEE Transactions on Nuclear Science
    ITPHP        IEEE Transactions on Parts Hybrids and Packaging
    ITPAM        IEEE Transactions on Pattern Analysis and Machine Intelligence
    ITPS         IEEE Transactions on Plasma Science
    ITPAS        IEEE Transactions on Power Apparatus Systems
    ITPE         IEEE Transactions on Power Electronics
    ITR          IEEE Transactions on Reliability
    ITRA         IEEE Transactions on Robotics Automation
    ITSP         IEEE Transactions on Signal Processing
    ITSU         IEEE Transactions on Sonics Ultrasonics
    ITSMC        IEEE Transactions on Systems Man and Cybernetics
    ITUFF        IEEE Transactions on Ultrasonics Ferroelectrics and Frequency Control
    ITVT         IEEE Transactions on Vehicular Technology
    ITEIS        IEEJ Transactions on Electronics, Information and Systems
    IJTFM        IEEJ Transactions on Fundamentals and Materials
    IJTIA        IEEJ Transactions on Industry Applications
    IJTPE        IEEJ Transactions on Power and Energy
    IJTSM        IEEJ Transactions on Sensors and Micromachines
    ESSFR        IEICE ESS Fundamentals Review
    IEITC        IEICE Transactions on Communications
    IEITE        IEICE Transactions on Electronics
    IEITF        IEICE Transactions on Fundamentals of Electronics Communications and Computer Sciences
    IEITI        IEICE Transactions on Information and Systems
    ITN          IERS Technical Note
    IESJ         IES Journal
    IHWN         IHW Newsletter
    JApMa        IMA Journal of Applied Mathematics
    IJNA         IMA Journal of Numerical Analysis
    ICSE         Impact of Computing in Science and Engineering
    InEPS        Indian Academy of Sciences Proceedings: Earth and Planetary Sciences
    InMS         Indian Academy of Sciences Proceedings Mathematical Sciences
    InASP        Indian Academy of Sciences Proceedings Section
    InES         Indian Academy of Sciences Proceedings: Section C Engineering Sciences
    IIApN        Indian Institute of Astrophysics Newsletter
    InISJ        Indian Institute of Science Journal
    InISA        Indian Institute of Science Journal of Aeronautical Society of India
    ITJSE        Indian Institute of Technology Journal on Section Engineering Technology
    InJHS        Indian Journal of the History of Science
    InJAE        Indian Journal of Aerospace Engineering Division
    InJET        Indian Journal of Electronics Telecommunication Engineering Division
    InJME        Indian Journal of Mechanical Engineering Division
    IJMHG        Indian Journal of Meteorology Hydrology and Geophysics
    InJPh        Indian Journal of Physics
    InJP         Indian Journal of Physics and Proceedings of the Indian Assocatiation for the Cultivation of Science
    InJPA        Indian Journal of Physics Section A
    InJPB        Indian Journal of Physics Section B
    IJPAM        Indian Journal of Pure and Applied Mathematics
    IJPAP        Indian Journal of Pure and Applied Physics
    IJRSP        Indian Journal of Radio and Space Physics
    InJTP        Indian Journal of Theoretical Physics
    INSAP        Indian National Science Academy Proceedings Supplement
    IUMJ         Indiana University Mathematics Journal
    IBVS         Information Bulletin on Variable Stars
    InfCo        Information Control
    InfD         Information Display
    IPM          Information Processing and Management
    ISNL         Information Systems Newsletter
    IBSH         Informational Bulletin of the Southern Hemisphere
    IBUAA        Informational Bulletin of the Ukrainian Astronomical Association
    IRA          Infrared Astronomy
    InfPh        Infrared Physics
    InPhT        Infrared Physics and Technology
    Ingeg        Ingegneria
    IA&A         Ingenieria Aeronautica y Astronautica
    IngAr        Ingenieur Archiv
    InCh         Inorganic Chemistry
    IAL1K        Institut d'Astronomie de Lausanne
    IRMBP        Institut Royal Meteorologique de Belgique Publications Serie
    ITAB         Institut Teoreticheskoi Astronomii Byulleten
    TrITA        Institut Teoreticheskoi Astronomii Trudy
    IMA          Institute for Mathematics and Its Applications
    InFuJ        Institute Fuel Journal
    JIECE        Institute of Electronics Communication Engineers of Japan Transactions Section E English
    ISASS        Institute of Space and Astronautical Science Report
    OslR         Institute of Theoretical Astrophysics Blindern Oslo Reports
    ITABO        Institute of Theoretical Astrophysics, Blindern-Oslo
    IEEP         Institution of Electrical Engineers Proceedings
    IEREJ        Institution of Electronic Radio Engineers Journal
    IETE         Institution of Electronics Telecommunication Engineers
    IAFET        Instituto de Astronomia y Fisica del Espacio Buenos Aires
    MerRe        Instituto Venezolano de Astronomia Merida Venezuela
    IS&T         Instrumentation Science & Technology
    IET          Instruments and Experimental Techniques
    InLoP        Instytut Lotnictwa Prace
    InMPP        Instytut Maszyn Przeplywowych Prace
    IntaC        Inta Conie
    Inter        Interavia
    IntSM        Interavia Space Markets
    ARIJ         An Interdisciplinary Journal of Physical and Engineering Sciences
    ISRv         Interdisciplinary Science Reviews
    IPAUC        INTERKOSMOS Prague Astronomicky Ustav Ceskoslovenske Akademie Ved
    IANT         International Advances in Nondestructive Testing
    IntAg        International Agrophysics
    IAPPP        International Amateur-Professional Photoelectric Photometry Communications
    IAM          International Applied Mechanics
    IAUC         International Astronomical Union Circular
    ICQ          International Comet Quarterly
    ICHMT        International Communications in Heat and Mass Transfer
    ICML         International Conference on Machine Learning
    InGeo        International Geophysics Series
    IJCEM        International Journal for Computational Methods in Engineering Science and Mechanics
    IJNAM        International Journal for Numerical and Analytical Methods in Geomechanics
    IJNME        International Journal for Numerical Methods in Engineering
    IJNMF        International Journal for Numerical Methods in Fluids
    IJRPC        International Journal for Radiation Physics and Chemistry
    IJACS        International Journal of Adaptive Control and Signal Processing
    IJAdA        International Journal of Adhesion Adhesives
    IJASS        International Journal of Aeronautical and Space Sciences
    IJAEM        International Journal of Analytical and Experimental Modal Analysis
    IJAEO        International Journal of Applied Earth Observation and Geoinformation
    IJAIS        International Journal of Applied Information Systems
    IJAM         International Journal of Applied Mechanics
    IJAsB        International Journal of Astrobiology
    IJAA         International Journal of Astronomy and Astrophysics
    IJAP         International Journal of Aviation Psychology
    IJBC         International Journal of Bifurcation and Chaos
    IJBB         International Journal of Bioclimatology Biometeorology
    IJBm         International Journal of Biometeorology
    IJCli        International Journal of Climatology
    IJCFD        International Journal of Computational Fluid Dynamics
    IJCMS        International Journal of Computational Materials Science and Engineering
    IJCA         International Journal of Computer Applications
    IJCAT        International Journal of Computer Applications and Technology
    IJCMB        International Journal of Computer Mathematics Section B
    IJC          International Journal of Control
    IJDM         International Journal of Damage Mechanics
    IJDE         International Journal of Digital Earth
    IJEaS        International Journal of Earth Sciences
    IJE          International Journal of Electronics
    IJEEP        International Journal of Emerging Electric Power Systems
    IJER         International Journal of Energy Research
    IJEFM        International Journal of Engineering and Fluid Mechanics Spring
    IJES         International Journal of Engineering Science
    IJFa         International Journal of Fatigue
    IJFD         International Journal of Fluid Dynamics
    IJFr         International Journal of Fracture
    IJFE         International Journal of Fusion Energy
    IJGS         International Journal of General Systems
    IJGA         International Journal of Geomagnetism and Aeronomy
    IJGMM        International Journal of Geometric Methods in Modern Physics
    IJGeo        International Journal of Geophysics
    IJG          International Journal of Geosciences
    IJGNP        International Journal of Green Nanotechnology Physics and Chemistry
    IJHFF        International Journal of Heat and Fluid Flow
    IJHMT        International Journal of Heat and Mass Transfer
    IJHM         International Journal of Hybrid Microelectronics Fall
    IJHE         International Journal of Hydrogen Energy
    IJIDF        International Journal of Image and Data Fusion
    IJIST        International Journal of Imaging Systems Technology
    IJIE         International Journal of Impact Engineering
    IJIMW        International Journal of Infrared and Millimeter Waves
    IJMSE        International Journal of Mars Science and Exploration
    IJMSp        International Journal of Mass Spectrometry
    IJMSI        International Journal of Mass Spectrometry and Ion Processes
    IJMES        International Journal of Mathematical Education in Science and Technology
    IJMS         International Journal of Mechanical Sciences
    IJMW         International Journal of Mine Water
    IJMM         International Journal of Mini Microcomputers
    IJMoS        International Journal of Modelling and Simulation
    IJMPA        International Journal of Modern Physics A
    IJMPB        International Journal of Modern Physics B
    IJMPC        International Journal of Modern Physics C
    IJMPS        International Journal of Modern Physics Conference Series
    IJMPD        International Journal of Modern Physics D
    IJMPE        International Journal of Modern Physics E
    IJMF         International Journal of Multiphase Flow
    IJN          International Journal of Nanoscience
    IJNT         International Journal of Nanotechnology
    IJNS         International Journal of Neural Systems
    IJNLM        International Journal of Non Linear Mechanics
    IJOpt        International Journal of Optics
    IJPRS        International Journal of Photogrammetry and Remote Sensing
    IJP          International Journal of Plasticity
    IJQC         International Journal of Quantum Chemistry
    IJRAI        International Journal of Radiation Applications and Instrumentation D Nuclear Tracks and Radiation Measurements
    IJRS         International Journal of Remote Sensing
    IJRR         International Journal of Robotics Research
    IJSC         International Journal of Satellite Communications
    IJSME        International Journal of Science and Mathematics Education
    IJSEd        International Journal of Science Education
    IJSER        International Journal of Scientific and Engineering Research
    IJSE         International Journal of Solar Energy
    IJSS         International Journal of Solids and Structures
    IJScA        International Journal of Supercomputer Applications
    IJTP         International Journal of Theoretical Physics
    IJT          International Journal of Thermophysics
    IJTJE        International Journal of Turbo Jet Engines
    IMRv         International Materials Reviews
    IMeRv        International Metals Reviews
    INL          International Nano Letters
    IREdu        International Review of Education
    IRH          International Review of Hydrobiology
    IRNP         International Review of Nuclear Physics
    IRPC         International Reviews in Physical Chemistry
    ISBRv        International Space Business Review
    IUGG         International Union of Geodesy and Geophysics General Assembly
    IER          Internationale Elektronische Rundschau
    IPNPR        Interplanetary Network Progress Report
    IMPA         Interscience Monographs in Physics and Astronomy
    ITPA         Interscience Tracts on Physics and Astronomy
    InMat        Inventiones Mathematicae
    InvPr        Inverse Problems
    InFiZ        Inzhenerno Fizicheskii Zhurnal
    IonIs        Ionosfernye Issledovaniia
    Iono         Ionosphere
    E&ES         IOP Conference Series: Earth and Environmental Science
    Ippa         Ipparchos
    IrJST        Iranian Journal of Science Technology
    IRETE        IRE Transactions on Education
    IrAJ         Irish Astronomical Journal
    IrAJS        Irish Astronomical Journal Supplement
    ISAP         ISA Proceedings
    ISAT         ISA Transactions
    IHERv        Ishikawajima Harima Engineering Review
    Isis         Isis. Journal of the History of Science Society
    IPBS         Isotopes in the Physical and Biomedical Sciences
    IsJT         Israel Journal of Technology
    IsSRT        Israel Space Research and Technology Information Bulletin
    ISRAA        ISRN Astronomy and Astrophysics
    ISCJS        ISRO Satellite Centre Journal of Spacecraft Technology
    ISSIR        ISSI Scientific Reports Series
    IssZK        Issledovanie Zemli Fiz Kosmosa
    IGAFS        Issledovaniia Geomagnetizmu Aeronomii i Fizike Solntsa
    IsMTD        Issledovaniia Mekhanike i Teploobmenu Dvukhfaznykh Sred
    IssUP        Issledovaniia Uprugosti i Plastichnosti
    ISKZ         Issledovaniya Solntsa i Krasnykh Zvezd
    IST          Issues in Science and Technology
    IsJAP        Istanbul University Faculty of Science Journal of Astronomy Physics
    IsRvC        Istanbul University Faculty Science Review Serie C
    IINA         Istituto Italiano di Navigazione Atti
    IAIss        Istoriko-Astronomicheskie Issledovaniya
    ITCJ         ITC Journal
    INTSA        Itogi Nauki i Tekhniki Seriia Astronomiia
    INTSF        Itogi Nauki i Tekhniki Seriia Fizika Plazmy
    INTSI        Itogi Nauki i Tekhniki Seriia Issledovanie Kosmicheskogo Prostranstva
    INTMK        Itogi Nauki i Tekhniki Seriia Meteorologiia i Klimatologiia
    INTSO        Itogi Nauki i Tekhniki Seriia Okeanologiia
    INTSR        Itogi Nauki i Tekhniki Seriia Radiotekhnika
    INTSS        Itogi Nauki i Tekhniki Seriia Sovremennye Problemy Matematiki
    INTSV        Itogi Nauki i Tekhniki Seriia Vozdushnyi Transport
    ITUTJ        ITU Telecommunication Journal
    IUEEN        IUE ESA Newsletter
    IUENN        IUE NASA Newsletter
    IzSF         Izvestiia Akademii Nauk Seriya Fizicheskaya
    IzTad        Izvestiia Akademiia Nauk TadzhSSR
    IzGla        Izvestiia Glavnoi rossiiskoi astronomicheskoi observatorii
    IzVGA        Izvestiia vuzov. Geodeziia Aehrofotosemka
    IzVF         Izvestiia Vysshaia Uchebn. Zaved., Fizika
    IzVUZ        Izvestiia Vysshaia Uchebn. Zaved., Radiofizika
    IzAsh        Izvestiya Akademii Nauk Turkmenskoj SSR Ashkhabad
    IzArm        Izvestiya Akademiya Nauk Armyanskoi
    IzAlm        Izvestiya Astrofizicheskogo Instituta Alma-Ata
    IzEhn        Izvestiya Astronomicheskoj Engel'gardt obskoj Observatorii Kazan
    IzAOP        Izvestiya Atmospheric and Oceanic Physics
    IzKie        Izvestiya Glavnoj Astronomicheskoj Observatorii Kiev
    IzPul        Izvestiya Glavnoj Astronomicheskoj Observatorii v Pulkove
    IzMat        Izvestiya: Mathematics
    IzKry        Izvestiya Ordena Trudovogo Krasnogo Znameni Krymskoj Astrofizicheskoj Observatorii
    IzPSE        Izvestiya Physics of the Solid Earth
    IzAvT        Izvestiya VUZ Aviatsionnaya Tekhnika
    IzRad        Izvestiya VUZ Radiofizika
    JWUDF        Jahns Wöchentliche Unterhaltungen Für Dilettanten und Freunde der Astronomie, Georgraphie und Witterungskunde
    JRE          Jahrbuch der Radioaktivität und Elektronik
    JASAC        Japan Astronomical Study Association Circulars
    JaIMJ        Japan Institute of Metals Journal
    JSASS        Japan Society of Aeronautical Space Sciences
    JSAST        Japan Society of Aeronautical Space Sciences Transactions
    JSAPJ        Japan Society of Air Pollution Journal
    JSCMJ        Japan Society of Composite Materials Journal
    JSLEJ        Japan Society of Lubrication Engineers Journal
    JSMSJ        Japan Society of Materials Science Journal
    JSPS         Japan Society of Promotion Science
    JaJAP        Japanese Journal of Applied Physics
    JJAPL        Japanese Journal of Applied Physics Letters B
    JJAPR        Japanese Journal of Applied Physics Regular Papers Short Notes and Review Papers
    JJAPS        Japanese Journal of Applied Physics Supplement
    JaJAG        Japanese Journal of Astronomy and Geophysics
    JMMPS        Japanese Magazine of Mineralogical and Petrological Sciences
    JSMAJ        JASMA Japan Society of Microgravity Application Journal
    JMeOp        Jemna Mechanika Optika
    JenRv        Jena Review
    JenRu        Jenaer Rundschau
    JBASP        Jodrell Bank Ann Ser Pt
    JHATD        Johns Hopkins APL Technical Digest
    JOM          JOM - Journal of the Minerals, Metals and Materials Society
    RSNSW        Journal and Proceedings of the Royal Society of New South Wales
    JAco         Journal d'Acoustique
    JCP          Journal de Chimie Physique
    JMec         Journal de Mecanique
    JMecA        Journal de Mecanique Appliquee
    JMecT        Journal de Mecanique Theorique et Appliquee
    JMTAS        Journal de Mecanique Theorique et Appliquee Supplement
    JPhys        Journal de Physique
    JPhyC        Journal de Physique Colloque
    JPhy1        Journal de Physique I
    JPhy2        Journal de Physique II
    JPhy3        Journal de Physique III
    JPhy4        Journal de Physique IV
    JPhTA        Journal de Physique Theorique et Apliquee
    JReAt        Journal de Recherches Atmospheriques
    JAF          Journal des Astronomes Francais
    JO           Journal des Observateurs
    JHA          Journal for the History of Astronomy
    JHAS         Journal for the History of Astronomy Supplement
    JTP          Journal for Technology of Plasticity
    JRAM         Journal fur die reine und angewandte Mathematik
    JNanU        Journal Nanjing Univ
    JNIRE        Journal NIRE
    JASJa        Journal of the Acoustical Society of Japan
    JAVSO        Journal of the American Association of Variable Star Observers (JAAVSO)
    JAChS        Journal of the American Chemical Society
    JAMS         Journal of the American Mathematical Society
    JASIS        Journal of the American Society for Information Science and Technology
    JASCE        Journal of the American Society of Civil Engineers
    JAWRA        Journal of the American Water Resources Association
    JALPO        Journal of the Association of Lunar and Planetary Observers, the Strolling Astronomer
    JAnSc        Journal of the Astronautical Sciences
    JASEg        Journal of the Astronomical Society of Egypt
    JASSA        Journal of the Astronomical Society of Southern Africa
    JASV         Journal of the Astronomical Society of Victoria Melbourne
    JASWA        Journal of the Astronomical Society of Western Australia
    JBAA         Journal of the British Astronomical Association
    JBAS         Journal of the British Astronomical Society
    JBIS         Journal of the British Interplanetary Society
    JCSS         Journal of the Chinese Silicate Society
    JElS         Journal of the Electrochemical Society
    FrInJ        Journal of The Franklin Institute
    JGSJ         Journal of the Geodetic Society of Japan
    JIEEJ        Journal of The Institute of Electrical Engineers of Japan
    JIMIA        Journal of the Institute of Mathematics and Its Applications
    JIPNT        Journal of the Institute of Positioning, Navigation and Timing of Japan
    JIETE        Journal of the Institution of Electronics and Telecommunication Engineers
    JIEIA        Journal of The Institution of Engineers (India): Series A
    JIEIB        Journal of The Institution of Engineers (India): Series B
    JIEIC        Journal of The Institution of Engineers (India): Series C
    JIEID        Journal of The Institution of Engineers (India): Series D
    JIEIE        Journal of The Institution of Engineers (India): Series E
    JJSMS        Journal of the Japan Society for Marine Surveys and Technology
    JLMS         Journal of the London Mathematical Society
    JMBM         Journal of the Mechanical Behavior of Materials
    JOSAA        Journal of the Optical Society of America A
    JOSA         Journal of the Optical Society of America (1917-1983)
    JOSAB        Journal of the Optical Society of America B Optical Physics
    JPSJ         Journal of the Physical Society of Japan
    JPSJS        Journal of the Physical Society of Japan Supplement
    JRASA        Journal of the Royal Aeronautical Society of London
    JRASC        Journal of the Royal Astronomical Society of Canada
    JSRP         Journal of the Society for Radiological Protection
    JSPST        Journal of The Society of Photographic Science and Technology of Japan
    JSARA        Journal of the Southeastern Association for Research in Astronomy
    JSD          Journal of the Structural Division, American Society of Civil Engineers
    JVSJ         Journal of the Vacuum Society of Japan
    JAE          Journal of Acoustic Emission
    JAMDS        Journal of Advanced Mechanical Design, Systems, and Manufacturing
    JAMES        Journal of Advances in Modeling Earth Systems
    JAerS        Journal of Aerosol Science
    JAerE        Journal of Aerospace Engineering
    JAerP        Journal of Aerospace Power
    JAfES        Journal of African Earth Sciences
    JAS          The Journal of Agricultural Science
    JAir         Journal of Aircraft
    JAllC        Journal of Alloys and Compounds
    JACS         Journal of American Ceramic Society
    JApCr        Journal of Applied Crystallography
    JApEl        Journal of Applied Electrochemistry
    JAGeo        Journal of Applied Geodesy
    JAG          Journal of Applied Geophysics
    JApMM        Journal of Applied Mathematics and Mechanics
    JAM          Journal of Applied Mechanics
    JAMTP        Journal of Applied Mechanics and Technical Physics
    JApMw        Journal of Applied Metalworking
    JApMe        Journal of Applied Meteorology
    JApMC        Journal of Applied Meteorology and Climatology
    JAPE         Journal of Applied Photographic Engineering
    JAP          Journal of Applied Physics
    JAPh         Journal of Applied Physiology
    JARS         Journal of Applied Remote Sensing
    JASE         Journal of Applied Science and Engineering Section on Electrical Power and Information Systems
    JApSc        Journal of Applied Sciences
    JApSp        Journal of Applied Spectroscopy
    JAGI         Journal of Artificial General Intelligence
    JAESc        Journal of Asian Earth Sciences
    JAD          Journal of Astronomical Data
    JAHH         Journal of Astronomical History and Heritage
    JAI          Journal of Astronomical Instrumentation
    JAsPh        Journal of Astronomy and Physics (Turkey)
    JASS         Journal of Astronomy and Space Sciences
    JApA         Journal of Astrophysics and Astronomy
    JApAS        Journal of Astrophysics and Astronomy Supplement
    JAtOT        Journal of Atmospheric and Oceanic Technology
    JASTP        Journal of Atmospheric and Solar-Terrestrial Physics
    JATP         Journal of Atmospheric and Terrestrial Physics
    JAtC         Journal of Atmospheric Chemistry
    JAtS         Journal of Atmospheric Sciences
    JAMOP        Journal of Atomic, Molecular and Optical Physics
    JAES         Journal of Audio Engineering Society
    JAuGG        Journal of Australian Geology and Geophysics
    JBall        Journal of Ballistics
    JBiom        Journal of Biomechanics
    JBO          Journal of Biomedical Optics
    JBiop        Journal of Biophysics
    JBR          Journal of Breath Research
    JChEd        Journal of Chemical Education
    JChPh        Journal of Chemical Physics
    JChS         Journal of Chromatographic Science
    JCh          Journal of Chromatography
    JCli         Journal of Climate
    JCAM         Journal of Climate and Applied Meteorology
    JClim        Journal of Climatology
    JClP         Journal of Clinical Pharmacology
    JCIS         Journal of Colloid and Interface Science
    JCoSc        Journal of Colloid Science
    JCom         Journal of Communications
    CoNet        Journal of Communications and Networks
    JComp        Journal of Complexity
    JCoMa        Journal of Composite Materials
    JCTR         Journal of Composites and Technology Research
    JTCN         Journal of Computatational and Theoretical Nanoscience
    JCoAM        Journal of Computational and Applied Mathematics
    JCoCh        Journal of Computational Chemistry
    JCM          Journal of Computational Mathematics
    JCoPh        Journal of Computational Physics
    JCST         Journal of Computational Science and Technology
    JCMD         Journal of Computer-Aided Materials Design
    JCAMD        Journal of Computer-Aided Molecular Design
    JCHyd        Journal of Contaminant Hydrology
    JConP        Journal of Contemporary Physics (Armenian Academy of Sciences)
    JCos         Journal of Cosmology
    JCAP         Journal of Cosmology and Astro-Particle Physics
    JCrGr        Journal of Crystal Growth
    JDE          Journal of Differential Equations
    JDGeo        Journal of Differential Geometry
    JoDI         Journal of Digital Information
    JDST         Journal of Dispersion Science and Technology
    JDisT        Journal of Display Technology
    JDSO         Journal of Double Star Observations
    JDDE         Journal of Dynamics and Differential Equations
    JESS         Journal of Earth System Science
    JElas        Journal of Elasticity
    JEEEA        Journal of Electrical and Electronics Engineering Australia
    JEE          Journal of Electrical Engineering
    JEAA         Journal of Electromagnetic Analysis and Application
    JEWA         Journal of Electromagnetic Waves and Applications
    JEMT         Journal of Electron Microscopy Technique
    JESRP        Journal of Electron Spectroscopy and Related Phenomena
    JECS         Journal of Electronic Circuits and Systems
    JEI          Journal of Electronic Imaging
    JEMat        Journal of Electronic Materials
    JEPub        Journal of Electronic Publishing
    JECTC        Journal of Electronics Cooling and Thermal Control
    JESEd        Journal of Elementary Science Education
    JEner        Journal of Energy
    JEAS         Journal of Engineering and Applied Sciences
    JEngM        Journal of Engineering and Mechanics
    JETh         Journal of Engineering and Thermophysics
    JEER         Journal of Engineering Education Research
    JEnMa        Journal of Engineering Mathematics
    JEP          Journal of Engineering Physics
    JEPT         Journal of Engineering Physics and Thermophysics
    JEngS        Journal of Engineering Sciences
    JEEM         Journal of Environmental and Economics Management
    JECE         Journal of Environmental Conservation Engineering
    JEnvS        Journal of Environmental Sciences
    JENan        Journal of Experimental Nanoscience
    JFF          Journal of Fire Flammability
    JFC          Journal of Fluid Control
    JFM          Journal of Fluid Mechanics
    JFST         Journal of Fluid Science and Technology
    JFS          Journal of Fluids and Structures
    JFAA         Journal of Fourier Analysis and Applications
    JFuA         Journal of Functional Analysis
    JGeod        Journal of Geodesy
    JGeoS        Journal of Geodetic Science
    JGeo         Journal of Geodynamics
    JGIS         Journal of Geographic Information System
    JGS          Journal of Geographical Systems
    JG           Journal of Geology
    JGG          Journal of Geomagnetism and Geoelectricity
    JGGS         Journal of Geomagnetism and Geoelectricity Supplement
    JGP          Journal of Geometry and Physics
    JGR          Journal of Geophysical Research
    JGRD         Journal of Geophysical Research (Atmospheres)
    JGRG         Journal of Geophysical Research (Biogeosciences)
    JGRF         Journal of Geophysical Research (Earth Surface)
    JGRC         Journal of Geophysical Research (Oceans)
    JGRE         Journal of Geophysical Research (Planets)
    JGRB         Journal of Geophysical Research (Solid Earth)
    JGRA         Journal of Geophysical Research (Space Physics)
    JGRS         Journal of Geophysical Research Supplement
    JGE          Journal of Geophysics and Engineering
    JGZG         Journal of Geophysics Zeitschrift Geophysik
    JGeEd        Journal of Geoscience Education
    JGlac        Journal of Glaciology
    JGrPh        Journal of Gravitational Physics
    JGHyd        Journal of Groundwater Hydrology
    JGuC         Journal of Guidance Control
    JGCD         Journal of Guidance Control Dynamics
    JHENP        Journal of High Energy and Nuclear Physics
    JHEP         Journal of High Energy Physics
    JHTS         Journal of High Temperature Society
    JHyd         Journal of Hydrology
    JHyMe        Journal of Hydrometeorology
    JHyn         Journal of Hydronautics
    JIST         Journal of Imaging Science and Technology
    JIEI         Journal of Industrial Engineering International
    JIPM         Journal of Information Processing and Management
    JInfo        Journal of Informetrics
    JIMW         Journal of Infrared and Millimeter Waves
    JInst        Journal of Instrumentation
    JIntS        Journal of Integer Sequences
    JIEq         Journal of Integral Equations
    JIMSS        Journal of Intelligent Material Systems and Structures
    JIEx         Journal of Ion Exchange
    JJAEE        Journal of Japan Association for Earthquake Engineering
    JSCSE        Journal of Japan Society of Civil Engineers, Ser. A1 (Structural Engineering & Earthquake Engineering (SE/EE))
    JSCAM        Journal of Japan Society of Civil Engineers, Ser. A2 (Applied Mechanics (AM))
    JSCHE        Journal of Japan Society of Civil Engineers, Ser. B1 (Hydraulic Engineering)
    JSCGE        Journal of Japan Society of Civil Engineers, Ser. C (Geosphere Engineering)
    JSCAI        Journal of Japan Society of Civil Engineers, Ser. D1 (Architecture of Infrastructure and Environment)
    JSCHS        Journal of Japan Society of Civil Engineers, Ser. D2 (Historical Studies in Civil Engineering)
    JSCIP        Journal of Japan Society of Civil Engineers, Ser. D3 (Infrastructure Planning and Management)
    JSCPE        Journal of Japan Society of Civil Engineers, Ser. E1 (Pavement Engineering)
    JSCMC        Journal of Japan Society of Civil Engineers, Ser. E2 (Materials and Concrete Structures)
    JSCTE        Journal of Japan Society of Civil Engineers, Ser. F1 (Tunnel Engineering)
    JSCUS        Journal of Japan Society of Civil Engineers, Ser. F2 (Underground Space Research)
    JSCCE        Journal of Japan Society of Civil Engineers, Ser. F3 (Civil Engineering Informatics)
    JSCCM        Journal of Japan Society of Civil Engineers, Ser. F4 (Construction and Management)
    JSCPP        Journal of Japan Society of Civil Engineers, Ser. F5 (Professional Practices in Civil Engineering)
    JSCSP        Journal of Japan Society of Civil Engineers, Ser. F6 (Safety Problem)
    JSCER        Journal of Japan Society of Civil Engineers, Ser. G (Environmental Research)
    JJAHS        Journal of Japanese Association of Hydrological Sciences
    JJSEE        Journal of Japanese Society for Engineering Education
    JKAS         Journal of Korean Astronomical Society
    JKASS        Journal of Korean Astronomical Society Supplement
    JKPS         Journal of Korean Physical Society
    JLasA        Journal of Laser Applications
    JLCM         Journal of Less Common Metals
    JLVEn        Journal of Light & Visual Environment
    JLwT         Journal of Lightwave Technology
    JLTP         Journal of Low Temperature Physics
    JLum         Journal of Luminescence
    JMagR        Journal of Magnetic Resonance
    JMMM         Journal of Magnetism and Magnetic Materials
    JMR          Journal of Marine Research
    JMSA         Journal of Marine Science and Application
    JMS          Journal of Marine Systems
    JMarA        Journal of Maritime Archaeology
    JMEP         Journal of Materials Engineering and Performance
    JMPMS        Journal of Materials Processing and Manufacturing Science
    JMatR        Journal of Materials Research
    JMatS        Journal of Materials Science
    JMSME        Journal of Materials Science and Materials Electronics
    JMSL         Journal of Materials Science Letters
    JMAA         Journal of Mathematical Analysis and Applications
    JMCS         Journal of Mathematical and Computational Science
    JMPS         Journal of Mathematical and Physical Sciences
    JMaCh        Journal of Mathematical Chemistry
    JMFM         Journal of Mathematical Fluid Mechanics
    JMP          Journal of Mathematical Physics
    JMaSc        Journal of Mathematical Sciences
    JMaMe        Journal of Mathematics and Mechanics
    JMaPh        Journal of Mathematics and Physics
    JMecE        Journal of Mechanical and Engineering Science
    JMSTL        Journal of Mechanical Systems for Transportation and Logistics
    JMPSo        Journal of Mechanics Physics of Solids
    JMet         Journal of Metals
    JMemS        Journal of Microelectromechanical Systems
    JMiMi        Journal of Micromechanics and Microengineering
    JMM&M        Journal of Micro/Nanolithography, MEMS, and MOEMS
    JMic         Journal of Microscopy
    JMPeS        Journal of Mineralogical and Petrological Sciences
    JMOp         Journal of Modern Optics
    JMPh         Journal of Modern Physics
    JMoEl        Journal of Molecular Electronics
    JMolE        Journal of Molecular Evolution
    JMoSp        Journal of Molecular Spectroscopy
    JMoSt        Journal of Molecular Structure
    JNUNS        Journal of Nanjing University (Natural Sciences)
    JNano        Journal of Nanophotonics
    JNav         Journal of Navigation
    JNIS         Journal of Near Infrared Spectroscopy
    JNEng        Journal of Neural Engineering
    JNeur        Journal of Neurochemistry
    JNCS         Journal of Non Crystalline Solids
    JNET         Journal of Non Equilibrium Thermodynamics
    JNLM         Journal of Non Linear Mechanics
    JNE          Journal of Nondestructive Evaluation
    JNMP         Journal of Nonlinear Mathematical Physics
    JNOPM        Journal of Nonlinear Optical Physics and Materials
    JNS          Journal of NonLinear Science
    JNuE         Journal of Nuclear Energy
    JNuM         Journal of Nuclear Materials
    JOUC         Journal of Ocean University of China
    JOC          Journal of Optical Communications
    JON          Journal of Optical Networking
    JOptT        Journal of Optical Technology
    JOpt         Journal of Optics
    JOptA        Journal of Optics A: Pure and Applied Optics
    JOptB        Journal of Optics B: Quantum and Semiclassical Optics
    JOTA         Journal of Optimization Theory Applications
    JPal         Journal of Paleontology
    JPDC         Journal of Parallel and Distributed Computing
    JPet         Journal of Petrology
    JPCRD        Journal of Physical and Chemical Reference Data
    JPCA         Journal of Physical Chemistry A
    JPhCh        Journal of Physical Chemistry
    JPCB         Journal of Physical Chemistry B
    JPO          Journal of Physical Oceanography
    JPhSt        Journal of Physical Studies
    JPhA         Journal of Physics A Mathematical General
    JPCS         Journal of Physics and Chemistry of Solids
    JPhB         Journal of Physics B Atomic Molecular Physics
    JPhC         Journal of Physics C Solid State Physics
    JPCM         Journal of Physics Condensed Matter
    JPhCS        Journal of Physics Conference Series
    JPhD         Journal of Physics D Applied Physics
    JPhE         Journal of Physics E Scientific Instruments
    JPhF         Journal of Physics F Metal Physics
    JPhG         Journal of Physics G Nuclear Physics
    JPhGS        Journal of Physics G Nuclear Physics Supplement
    JPE          Journal of Physics of the Earth
    JPFR         Journal of Plasma and Fusion Research
    JPlPh        Journal of Plasma Physics
    JPoSc        Journal of Polymer Science
    JPoSA        Journal of Polymer Science A Polymer Chemistry
    JPoSB        Journal of Polymer Science B Polymer Physics
    JPoSL        Journal of Polymer Science: Polymer Letters Edition
    JPES         Journal of Power and Energy Systems
    JPS          Journal of Power Sources
    JPAS         Journal of Practical Applications in Space
    JPP          Journal of Propulsion and Power
    JPT          Journal of Propulsion Technology
    JPApS        Journal of Pure Applied Sciences
    JQT          Journal of Quality Technology
    JQSRT        Journal of Quantitative Spectroscopy and Radiative Transfer
    JQS          Journal of Quaternary Science
    JRNC         Journal of Radioanalytical and Nuclear Chemistry
    JRAC         Journal of Radioanalytical Chemistry
    JRP          Journal of Radiological Protection
    JRSp         Journal of Raman Spectroscopy
    JRPC         Journal of Reinforced Plastics and Composites
    JRes         Journal of Research
    JRPhy        Journal of Research in Physics
    JRScT        Journal of Research in Science Teaching
    JRIST        Journal of Research Institute of Science and Technology, College of Science and Technology, Nihon University
    JRNBS        Journal of Research of the National Bureau of Standards
    JRNBA        Journal of Research of the National Bureau of Standards A Physica and Chemsitry
    JRNBB        Journal of Research of the National Bureau of Standards B Mathematical Sciences
    JResB        Journal of Research Section B Mathematical Sciences B
    JRheo        Journal of Rheology
    JRoS         Journal of Robotic Systems
    JSEdT        Journal of Science Education and Technology
    JSTEd        Journal of Science Teacher Education
    JSCom        Journal of Scientific Computing
    JScI         Journal of Scientific Instruments
    JSR          Journal of Sea Research
    JSedR        Journal of Sedimentary Research
    JSeis        Journal of Seismology
    JSemi        Journal of Semiconductors
    JSGeo        Journal of Series Geophysics
    JShR         Journal of Ship Research
    JSMME        Journal of Solid Mechanics and Materials Engineering
    JSSCh        Journal of Solid State Chemistry France
    JSV          Journal of Sound Vibration
    JSAES        Journal of South American Earth Sciences
    JSLR         Journal of Soviet Laser Research
    JSAR         Journal of Space Astronomy Research
    JSpEn        Journal of Space Engineering
    JSWSC        Journal of Space Weather and Space Climate
    JSpRo        Journal of Spacecraft and Rockets
    JSpT         Journal of Spacecraft Technology
    JSMTE        Journal of Statistical Mechanics: Theory and Experiment
    JSP          Journal of Statistical Physics
    JStA         Journal of Strain Analysis and Engineering Design
    JSG          Journal of Structural Geology
    JSM          Journal of Structural Mechanics
    JSup         Journal of Superconductivity
    JSymC        Journal of Symbolic Computation
    JSDD         Journal of System Design and Dynamics
    JTePh        Journal of Technical Physics
    JTech        Journal of Technology
    JTeEv        Journal of Testing Evaluation
    JTAM         Journal of Theoretical and Applied Mechanics
    JTAP         Journal of Theoretical and Applied Physics
    JThSc        Journal of Thermal Science
    JJTST        Journal of Thermal Science and Technology
    JTST         Journal of Thermal Spray Technology
    JThSt        Journal of Thermal Stresses
    JTh          Journal of Thermodynamics
    JTHT         Journal of Thermophysics and Heat Transfer
    JThCM        Journal of Thermoplastic Composite Materials
    JTF          Journal of Time and Frequency
    JTurb        Journal of Turbulence
    JVST         Journal of Vacuum Science Technology
    JVSTA        Journal of Vacuum Science Technology A: Vacuum Surfaces and Films
    JVSTB        Journal of Vacuum Science Technology B: Microelectronics and Nanometer Structures
    JVE          Journal of Vibration Engineering
    JVCIR        Journal of Visual Communication and Image Representation
    JVGR         Journal of Volcanology and Geothermal Research
    JWMSE        Journal of Women and Minorities in Science and Engineering
    JXST         Journal of X-Ray Science and Technology
    RpScT        JPRS Report Science Technology USSR Space
    JSMEJ        JSME International Journal
    JSMEA        JSME International Journal Series A
    JSMEB        JSME International Journal Series B
    JSMEC        JSME International Journal Series C
    JSMET        JSME Transactions
    KKR          Kagaku Kogaku Ronbunshu
    MmKMO        Kakioka Magnetic Observatory Memoirs
    KEIJ         Kansei Engineering International Journal
    KIzKU        Kazan Izdatel Kazanskogo Universiteta
    MeeRe        Kenneth Mees Observatory Reprints
    KernR        Kernforschungsanlage Rept Res Results Solid State Nucl Phys
    KexT         Kexue Tongbao
    Khago        Khagol
    KharI        Kharkov Izdanie IRE AN USSR
    KTTM         Khimiia i Tekhnologiia Topliv i Masel
    KhPl         Khimiia Plazmy
    KVnT         Kibernetika i Vychislitel naia Tekhnika
    KiInF        Kiev Institut Fiziki AN USSR
    KiInM        Kiev Institut Matematiki AN USSR
    KIPME        Kiev Institut Problem Modelirovaniia Energetike AN USSR
    KIzIM        Kiev Izdanie Instituta Matematiki AN USSR
    KiIND        Kiev Izdatel Naukova Dumka
    KiIzT        Kiev Izdatel Tekhnika
    KIzVS        Kiev Izdatel Vishcha Shkola
    KPCB         Kinematics and Physics of Celestial Bodies
    KPCBS        Kinematics and Physics of Celestial Bodies, Supplement
    KFNT         Kinematika i Fizika Nebesnykh Tel
    KFNTS        Kinematika i Fizika Nebesnykh Tel Supplement
    KIzS         Kishinev Izdatel Shtiintsa
    KPNON        Kitt Peak National Observatory Newsletter
    KVeBB        Kleine Veroeffentlichungen der Universitaetssternwarte zu Berlin Babelsberg
    KlBer        Kleinheubacher Berichte
    KodOB        Kodaikanal Observatory Bulletins
    KodRe        Kodaikanal Observatory Reprints
    KomTs        Kometnyj Tsirkulyar
    KomMe        Komety i Meteory
    KNAB         Koninklijke Nederlandse Akademie van Weteschappen Proceedings Series B Physical Sciences
    KIMMJ        Korean Institute of Metals and Materials Journal
    KNT          Kosmicheskaia Nauka i Tekhnika
    KosIs        Kosmicheskie Issledovaniia
    KosIU        Kosmicheskie Issledovaniia Ukraine
    KosLu        Kosmicheskie Luchi
    KosNT        Kosmichna Nauka i Tekhnologiya
    Kozmo        Kozmos
    KSVH         Kungl. Svenska Vetenskapsakademiens Handlingar
    KvanE        Kvantovaia Elektronika Moscow
    KyoMe        Kyoto University Faculty Engineering Memoirs
    KyITB        Kyushu Institute Technology Bulletin
    KUFEM        Kyushu University Faculty Engineering Memoirs
    KyUAM        Kyushu University Research Institute Applied Mechanics Reports
    KyUSR        Kyushu University Research Institute Industrial Science Reports
    KyUTR        Kyushu University Technology Reports
    AerAs        L'Aeronautique et L'Astronautique
    AerMS        L'Aerotecnica Missili e Spazio
    LanB         Landolt Börnstein
    Langm        Langmuir
    LaJ          Lapidary Journal
    LPB          Laser and Particle Beams
    LaEO         Laser Elektro Optik
    LaFoc        Laser Focus
    LasJ         Laser Journal
    LaPhy        Laser Physics
    LaPhL        Laser Physics Letters
    LAstr        L'Astronomie
    LatJP        Latvian Journal of Physics and Technical Sciences
    LatME        Latviiskii Matematicheskii Ezhegodnik
    LawOB        Laws Observatory Bulletin, University of Missouri
    LBLRR        LBL Research Review
    ASPL         Leaflet of the Astronomical Society of the Pacific
    ASPLS        Leaflet of the Astronomical Society of the Pacific (Supplement)
    LePub        Learned Publishing
    LERec        L'Echo des Recherches
    LNEA         Lecture Notes and Essays in Astrophysics
    LNSP         Lecture Notes and Supplements in Physics
    LNCS         Lecture Notes in Computer Science
    LNES         Lecture Notes in Earth Sciences, Berlin Springer Verlag
    LNEn         Lecture Notes in Engineering, Berlin Springer Verlag
    LNM          Lecture Notes in Mathematics, Berlin Springer Verlag
    LNP          Lecture Notes in Physics, Berlin Springer Verlag
    LeBAN        Leningrad Biblioteka Akademii Nauk SSSR
    LeEne        Leningrad Energoizdat
    LeGid        Leningrad Gidrometeoizdat
    PrAtO        Leningrad Gidrometeoizdat Sovremennye Problemy Atmosfernoi Optiki
    LeIzE        Leningrad Izdatel Energiia
    LeIzG        Leningrad Izdatel Gidrometeoizdat
    LeIzK        Leningrad Izdatel Khimiia
    LeIzU        Leningrad Izdatel Leningradskogo Universiteta
    LeIzM        Leningrad Izdatel Mashinostroenie
    LeIzN        Leningrad Izdatel Nauka
    LIzNe        Leningrad Izdatel Nedra
    LeIzS        Leningrad Izdatel Sudostroenie
    IzLen        Leningrad, Izdatel'stvo Nauka
    LeLen        Leningrad Lenizdat
    LGUPM        Leningradskii Gosudarstvennyi Universitet Problemy Matematicheskoi Fiziki
    VeLen        Leningradskii Universitet Vestnik Matematika Mekhanika Astronomiia
    LFTR         LEST Foundation, Technical Report
    LHMT         Letters Heat Mass Transfer
    LAES         Letters in Applied and Engineering Sciences
    LMaPh        Letters in Mathematical Physics
    LicOB        Lick Observatory Bulletin
    LFR          Lietuvos Fizikos Rinkinys
    LLabJ        Lincoln Laboratory Journal
    LiCr         Liquid Crystals
    Litho        Lithos
    LitJP        Lithuanian Journal of Physics and Technical Sciences
    LRR          Living Reviews in Relativity
    LRSP         Living Reviews in Solar Physics
    LockH        Lockheed Horizons
    LOEle        L'Onde Electrique
    LTP          Low Temperature Physics
    LowOB        Lowell Observatory Bulletin
    LPIBu        LPI Bulletin
    LPICo        LPI Contributions
    LubEn        Lubrication Engineering
    LR           Luft und Raumfahrt
    LuRaQ        Luft und Raumfahrt Quarter
    LPSC         Lunar and Planetary Science Conference Proceedings
    LCEC         Luxembourg Commission European Communities
    LIVS         Lvov Izdatel Vishcha Shkola
    LvoTs        L'vovskij Ordena Lenina Gosudarstvennyj Universitet Tsirkulyar
    MaDes        Machine Design
    MmCP         Macromolecular Chemistry and Physics
    MaMol        Macromolecules
    MadOO        Madras Observatory Astronomical Observations
    MadOb        Madras Observatory Observations
    MagFE        Magnetic Fusion Energy
    MRRev        Magnetic Resonance Review
    MHD          Magnetohydrodynamics
    MagGi        Magnitnaia Gidrodinamika
    MagIs        Magnitosfernye Issledovaniia
    MAWMN        Mainz Akademie Wissenschaften Mathematisch Naturwissenschaftliche Klasse
    Lapa         Majalah LAPAN
    MWGBI        Mannheim West Germany Bibliographisches Institut AG
    MaTeJ        ManTech Journal
    MGeo         Manuscr. Geod.
    ManGe        Manuscripta Geodaetica
    MarRv        Marconi Review
    MarGe        Marine Geodesy
    MarGR        Marine Geophysical Research
    MarPG        Marine Petroleum Geology
    Mashi        Mashinostroenie
    MsT          Masters Thesis
    MaFiz        Matematicheskaia Fizika
    MFiNM        Matematicheskaia Fizika i Nelineinaia Mekhanika
    MatIs        Matematicheskie Issledovaniia
    MMFMP        Matematicheskie Metody i Fiziko Mekhanicheskie Polia
    MISTr        Matematicheskii Institut imeni Steklova Trudy
    MMTET        Matematicheskoe Modelirovanie i Teoriia Elektricheskikh Tsepei
    MatVe        Matematichki Vesnik
    Mater        Materialpruefung
    Mate         Materials
    MaHT         Materials at High Temperatures
    MatEv        Materials Evaluation
    MatL         Materials Letters
    MaRBu        Materials Research Bulletin
    MRSSP        Materials Research Society Symposia Proceedings
    MSEnA        Materials Science and Engineering A
    MSEng        Materials Science and Engineering
    MSEnB        Materials Science and Engineering B
    MSEnC        Materials Science and Engineering C
    MS&E         Materials Science and Engineering Conference Series
    MSEnR        Materials Science and Engineering R Reports
    MSF          Materials Science Forum
    MatSP        Materials Science Poland
    MatST        Materials Science Technology
    MatTr        Materials Transactions JIM
    MatTe        Materiaux et Techniques
    MComM        Mathematical and Computer Modelling
    MEI          Mathematical Engineering Industry
    MatG         Mathematical Geology
    MMAS         Mathematical Methods in the Applied Sciences
    MatM         Mathematical Modelling
    MMNA         Mathematical Modelling Numerical Analysis
    MPAG         Mathematical Physics, Analysis and Geometry
    MaPEJ        Mathematical Physics Electronic Journal
    MaPhS        Mathematical Physics Studies
    MaPr         Mathematical Proceedings
    MPCPS        Mathematical Proceedings of the Cambridge Philosophical Society
    MatPr        Mathematical Programming
    MatRv        Mathematical Reviews
    MEdRJ        Mathematics Education Research Journal
    MaCom        Mathematics of Computation
    MatAn        Mathematische Annalen
    MatNa        Mathematische Nachrichten
    MatZe        Mathematische Zeitschrift
    MatMo        The Mathemtical Monthly
    MitAe        Max Planck Institut Aeronomie Mitteilungen
    MPARp        Max Planck Institut fur Astrophysik Report
    MeScT        Measurement Science and Technology
    MeScR        Measurement Science Review
    Meas         Measurements
    Mecc         Meccanica
    MecEn        Mechanical Engineering
    MSSP         Mechanical Systems and Signal Processing
    MPDS         Mechanics and Physics of Discrete Systems
    MSM          Mechanics of Structures and Machines
    MTDM         Mechanics of Time-Dependent Materials
    MeReC        Mechanics Research Communications
    MeTeS        Mechanika Teoretyczna i Stosowana
    MeMaT        Mechanism and Machine Theory
    MeUpp        Meddelanden fran Astronomiska Observatorium Uppsala
    MeLu1        Meddelanden fran Lunds Astronomiska Observatorium Serie I
    MeLu2        Meddelanden fran Lunds Astronomiska Observatorium Serie II
    MeAar        Meddelser fra Ole Romer Observatoriet Aarhus
    MeGen        Mededelingen Universiteit te Gent Sterrenkundig Instituut
    MeLeu        Mededelingen van het Astronomisch Instituut van de Katholieke Universiteit Leuven
    MedPh        Medical Physics
    MAA          Mediterranean Archaeology and Archaeometry
    MekGS        Mekhanika Giroskopicheskikh Sistem
    MekKM        Mekhanika Kompozitnykh Materialov
    MekP         Mekhanika Polimerov
    MekTT        Mekhanika Tverdogo Tela
    MelOO        Melbourne Observatory Observations
    MmARB        Memoires of the Academie Royale de Belgique
    MmMtS        Memoires of the Mount Stromlo Observervatory
    MSRSL        Memoires of the Societe Royale des Sciences de Liege
    MeSRM        Memoires Scientifiques de la Revue de Metallurgie
    MmKyo        Memoirs Faculty of Sciences University of Kyoto
    MmASI        Memoirs of the Astronomical Society of India
    MmBAA        Memoirs of the British Astronomical Association
    MmRAS        Memoirs of the Royal Astronomical Society
    MmNap        Memorie del R. Osservatorio di Capodimonte in Napoli
    MmSAI        Memorie della Societa Astronomica Italiana
    MSAIS        Memorie della Societa Astronomica Italiana Supplementi
    MmSSI        Memorie della Societa Degli Spettroscopisti Italiani
    MmSS         Memorie della Societa Degli Spettroscopisti Italiani, serie 2
    MmSGI        Memorie della Societa Geologica Italiana
    Mercu        Mercury
    MeAut        Meres es Automatika
    Msngr        The Messenger
    MeRAu        Mesures Regulation Automatisme
    Metal        Metallofizika
    MTObM        Metallovedenie i Termicheskaia Obrabotka Metallov
    MMTA         Metallurgical and Materials Transactions A
    MMTB         Metallurgical and Materials Transactions B
    MTA          Metallurgical Transactions A
    MTB          Metallurgical Transactions B
    MTPMM        Metallurgical Transactions Physical Metallurgy Materials Science
    MetaM        Metamaterials
    MTRMA        Meteor Forschungsergebnisse Reihe B Meteorologie und Aeronomie
    MeRR         Meteor. rasprostr. radiovoln, Kazan
    Met          Meteorite - The International Quarterly of Meteorites and Meteorite Science
    Metit        Meteorites
    Metic        Meteoritics
    M&PS         Meteoritics and Planetary Science
    M&PSA        Meteoritics and Planetary Science Supplement
    Metik        Meteoritika
    MetRR        Meteornoe Rasprostranenie Radiovoln
    MetIs        Meteornye Issledovaniia
    MeApp        Meteorological Applications
    MetMa        Meteorological Magazine
    MetMo        Meteorological Monographs
    MSCTN        Meteorological Satellite Center Technical Note
    MeSJJ        Meteorological Society of Japan Journal
    MetZp        Meteorologicke Zpravy
    Meteo        La Meteorologie
    MeGid        Meteorologiia i Gidrologiia
    MetRu        Meteorologische Rundschau
    MetZe        Meteorologische Zeitschrift
    MAP          Meteorology and Atmospheric Physics
    MetAP        Meteorology Atmospheric Physics
    MetHy        Meteorology Hydrology JPRS
    MVMP         Methoden und Verfahren der Mathematischen Physik
    MApAn        Methods and Applications of Analysis
    MComP        Methods in Computational Physics
    MSB          Methods in Subnuclear Physics
    MExP         Methods of Experimental Physics
    MetVy        Metody Vychislenii
    Metro        Metrologia
    MicEc        Microbial Ecology
    MPFD         Microdevices: Physics and Fabrication Technologies
    MiRe         Microelectronics Reliability
    MicgQ        Microgravity Quarterly
    MiST         Microgravity Science and Technology
    MTEng        Microscale Thermophysical Engineering
    MiMic        Microscopy and Microanalysis
    MiOTL        Microwave and Optical Technology Letters
    MiJo         Microwave Journal
    MicWa        Microwaves
    AcMik        Mikrochimica Acta
    Mikro        Mikroelektronika
    MikSb        Mikroelektronika Sbornik
    MSMFR        Milano Seminario Matematico e Fisico Rendiconti
    MiElC        Military Electronics Countermeasures
    MWE          Mine Water and The Environment
    MinDe        Mineralium Deposita
    Miner        Mineralogia
    MinM         Mineralogical Magazine
    MinPe        Mineralogy and Petrology
    MPBu         Minor Planet Bulletin
    MPC          Minor Planet Circulars
    MPEC         Minor Planet Electronic Circulars
    IzMin        Minsk Izdatel BGU
    MiINT        Minsk Izdatel Nauka i Tekhnika
    MisSp        Missiles Spacecraft
    MAPSE        Mission Analysis Program Solar Electric Propulsion MAPSEP
    MHITR        Mitsubishi Heavy Industries Technical Review
    MitAG        Mitteilungen der Astronomischen Gesellschaft Hamburg
    MiBon        Mitteilungen der Astronomischen Institute der Universitaet Bonn
    MiBas        Mitteilungen der Astronomisch-Meteorologischen Anstalt der Universitaet Basel Astronomische Reihe
    MiHar        Mitteilungen der Bruno-H.-Buergel-Sternwarte Hartha DDR
    MiHam        Mitteilungen der Hamburger Sternwarte in Bergedorf
    MiKon        Mitteilungen der Konkoly Sternwarte Budapest-Szabadsaghegy
    MiPul        Mitteilungen der Nikolai-Hauptsternwarte zu Pulkowo
    MiInn        Mitteilungen der Sternwarte Innsbruck
    MiMun        Mitteilungen der Sternwarte Munchen
    MiSon        Mitteilungen der Sternwarte zu Sonneberg
    MiGra        Mitteilungen der Universitaets-Sternwarte Graz
    MiWie        Mitteilungen der Universitaets-Sternwarte Wien
    MiJen        Mitteilungen der Universitaets-Sternwarte zu Jena
    MiTue        Mitteilungen des Astronomischen Instituts der Universitaet Tuebingen
    MiMue        Mitteilungen des Astronomischen Instituts des Universitaet Munster
    MiPot        Mitteilungen des Astrophysikalischen Observatoriums Potsdam
    MiGIR        Mitteilungen Geod. Institut Rheinischen Friedrich-Wilhelms-Universitaets. Bonn
    MSMSE        Modelling Simul. Mater. Sci. Eng.
    ModGe        Modern Geology
    ModIn        Modern Instrumentation
    MIMPE        Modern Instrumentation and Measurements in Physics and Engineering
    ModPh        Modern Physics
    MPLA         Modern Physics Letters A
    MPLB         Modern Physics Letters B
    MJPS         Moldavian Journal of the Physical Sciences
    MBB          Molecular Biology and Biophysics
    MolPh        Molecular Physics
    MoSim        Molecular Simulation
    MCBEH        Monatliche Correspondenz zur Beforderung der Erd- und Himmels-kunde
    WisBB        Monatsber. Deutsch. Akad Wissenschaftliche Berlin
    MEEP         Monographs on Environment, Earth and Planets
    MNSSA        Monthly Notes of the Astronomical Society of South Africa
    MNSSJ        Monthly notes of the Astronomical Society of South Africa
    MNRAS        Monthly Notices of the Royal Astronomical Society
    MWRv         Monthly Weather Review
    Moon         Moon
    M&P          Moon and Planets
    MorGI        Morskie Gidrofizicheskie Issledovaniia
    MAtom        Moscow Atomizdat
    MoEBA        Moscow Energoatomizdat Biblioteka Automatike
    MEner        Moscow Energoizdat
    MoGid        Moscow Gidrometeoizdat
    MoIKI        Moscow Institut Kosmicheskikh Issledovanii AN SSSR
    MoIPM        Moscow Institut Prikladnoi Matematiki AN SSSR
    MoIzA        Moscow Izdatel Atomizdat
    MoIzE        Moscow Izdatel Energiia
    MIEBA        Moscow Izdatel Energiia Biblioteka Avtomatike
    MIEBR        Moscow Izdatel Energiia Biblioteka Radioelektronike
    MoIzK        Moscow Izdatel Khimiia
    MIzLI        Moscow Izdatel Legkaia Industriia
    MIzMa        Moscow Izdatel Mashinostroenie
    MIzMe        Moscow Izdatel Metallurgiia
    MoIzM        Moscow Izdatel Moskovskogo Universiteta
    MIzMU        Moscow Izdatel Moskovskogo Universiteta Pt
    MoIzN        Moscow Izdatel Nauka
    MINFI        Moscow Izdatel Nauka AN SSR Fizicheskii Institut Trudy
    MINCV        Moscow Izdatel Nauka AN SSSR Chteniia imeni Vernadskogo
    MINGI        Moscow Izdatel Nauka AN SSSR Geologicheskoi Institut Trudy
    MINMI        Moscow Izdatel Nauka AN SSSR Matematicheskii Institut Trudy
    MoINI        Moscow Izdatel Nauka Issledovaniia Geomagnetizmu Aeronomii i Fizike Solntsa
    MINTF        Moscow Izdatel Nauka Teoreticheskaia Fizika
    MINVS        Moscow Izdatel Nauka Vychislitel naia Seismologiia
    MIzNe        Moscow Izdatel Nedra
    MIzRS        Moscow Izdatel Radio Sviaz
    MIzSR        Moscow Izdatel Sovetskoe Radio
    MoIzS        Moscow Izdatel Sviaz
    MISST        Moscow Izdatel Sviaz Statisticheskaia Teoriia sviazi
    MoIzT        Moscow Izdatel Transport
    MoIzV        Moscow Izdatel VINITI
    MIzVS        Moscow Izdatel Vysshaia Shkola
    MoIzZ        Moscow Izdatel Znanie
    MIZNZ        Moscow Izdatel Znanie Novoe Zhizni Nauke Tekhnike Seriia Fizika
    MosIZ        Moscow IZMIRAN
    MoMTN        Moscow Mezhdunarodnyi Tsentr Nauchnoi i Tekhnicheskoi Informatsii
    MoMGK        Moscow Mezhduvedomstvennyi Geofizicheskii Komitet
    MUPB         Moscow University Physics Bulletin
    MoVIN        Moscow VINITI
    MosVo        Moscow Voenizdat
    MosVI        Moscow Voennoe Izdatel
    MoVNT        Moscow Vychislitel nyi Tsentr AN SSSR
    MoVyS        Moscow Vysshaia Shkola
    MoLLP        Moshchnye lazery i lazernaia plazma
    MoEIT        Moskovskii Energeticheskii Institut Trudy
    MGUMN        Moskovskii Gosudarstvennyi Universitet Institut Mekhaniki Nauchnye Trudy
    MGIMO        Moskovskii Gosudarstvennyi Universitet Institut Mekhaniki Otchet
    MVSFA        Moskovskii Universitet Vestnik Seriia Fizika Astronomiia
    MUVSK        Moskovskii Universitet Vestnik Seriia Khimiia
    MVSMM        Moskovskii Universitet Vestnik Seriia Matematika Mekhanika
    MGTVM        Moskovskij Gosudarstvennyj Tekhnicheskij Universitet Vestnik Seriya Mashinostroenie
    MGTVP        Moskovskij Gosudarstvennyj Tekhnicheskij Universitet Vestnik Seriya Priborostroenie
    MotZe        Motortechnische Zeitschrift
    MtSOM        Mount Stromlo Observatory Mimeographs
    MtWAR        Mount Wilson and Palomar Observatory Annual Report
    MWOAR        Mount Wilson Observatory Annual Report
    MPERp        MPE Report
    MRSBu        MRS Bulletin
    MUSS         Muenchen Universitaets Schriften Serie
    MROVG        Munich R Oldenbourg Verlag GmbH
    NISZ         Nabliudeniia Iskusstvennykh Sputnikov Zemli
    NINT         Nablyud. Iskusstvennykh Nebesnykh Tel
    NOGB         Nachr. Olbers-Ges. Bremen
    NacEl        Nachrichten Elektronik
    NAZ          Nachrichtenblatt der Astronomischen Zentralstelle Heidelberg
    NVS          Nachrichtenblatt der Vereinigung der Sternfreunde
    NGFAW        Nachrichtentechnische Gesellschaft Fachtagung ueber Antennen
    NacZe        Nachrichtentechnische Zeitschrift
    NUFEM        Nagoya University Faculty Engineering Memoirs
    NURIA        Nagoya University Research Institute of Atmospherics Proceedings
    NUSEM        Nagoya University School Engineering Memoirs
    NaAIJ        Nanjing Aeronautical Institute Journal
    NUAAJ        Nanjing University Aeronautics and Astronautics Journal
    NanoL        Nano Letters
    Nanop        Nanophotonics
    Nanos        Nanoscale
    NRL          Nanoscale Research Letters
    Nanot        Nanotechnology
    NIUNA        Napoli Istituto Universitario Navale Annali
    NASCL        NASA Circular Letter
    PDSS         NASA Planetary Data System
    NASRP        NASA Reference Publication
    NASSP        NASA Special Publication
    STIA         NASA STI/Recon Technical Report A
    STIN         NASA STI/Recon Technical Report N
    NASTM        NASA Technical Memo
    NBSSP        National Bureau of Standards Special Publication
    NBSTN        National Bureau of Standards Technical Note
    NaGe         National Geographic
    NISTJ        National Institute of Standards and Technology Journal of Research
    PolRe        National Institute Polar Research Memoirs
    BAth         National Observatory of Athens Greece Bulletin of the Astronomical Institute
    NRAON        National Radio Astronomy Observatory Newsletter
    nrao pres    National Radio Astronomy Observatory Press Release
    NRAOR        National Radio Astronomy Observatory Reprints
    NRAOW        National Radio Astronomy Observatory Workshop
    NUDTJ        National University Defense Technology Journal
    NHESS        Natural Hazards and Earth System Sciences
    NHESD        Natural Hazards and Earth System Sciences Discussions
    NatH         Natural History
    NatSc        Natural Science
    Natur        Nature
    NatBi        Nature Biotechnology
    NatCh        Nature Chemistry
    NatCC        Nature Climate Change
    NatCo        Nature Communications
    NatGe        Nature Geoscience
    NatMa        Nature Materials
    NatNa        Nature Nanotechnology
    NaPho        Nature Photonics
    NPhS         Nature Physical Science
    NatPh        Nature Physics
    NatSR        Nature Scientific Reports
    NW           Naturwissenschaften
    NInfo        Nauchnye Informatsii
    NRRv         Naval Research Reviews
    Navig        Navigation
    NavAu        Navigation Australia
    NavPa        Navigation Paris
    NCNS         Network: Computation in Neural Systems
    AnBog        Neue Annalen der Koeniglichen Sternwarte in Bogenhausen bei Muenchen
    NJMM         Neues Jahrbuch Mineralogie Monatshefte
    NN           Neural Networks
    NeuL         Neuroscience Letters
    NPNDS        Neutron Physics and Nuclear Data in Science and Technology
    NewA         New Astronomy
    NewAR        New Astronomy Reviews
    NJPh         New Journal of Physics
    NewSc        New Scientist
    NTN          New Technology News
    NZJS         New Zealand Journal of Science
    ASNYN        News Letter of the Astronomical Society of New York
    INGN         The Newsletter of the Isaac Newton Group of Telescopes
    ICHIN        Newsletters of the Interdivisional Commission on History of the IAGA
    NKG          Nihon Kessho Gakkaishi
    NOHIC        Nizamiah JAPAL Rangapur Observatories Hyderabad India Contributions
    noao prop    NOAO Proposal
    NCE          Noise Control Engineering Journal
    NTE          Nondestructive Testing And Evaluation
    NDTI         Nondestructive Testing and Evaluation International
    NTCo         Nondestructive Testing Communications
    NPPSB        Nonequilibrium Problems in the Physical Sciences and Biology
    NATM         Nonlinear Analysis Theory Methods Applications
    NPGeo        Nonlinear Processes in Geophysics
    NSAP         Nonlinear, Statistical and Applied Physics
    NTA          Nonlinear Theory and Its Applications, IEICE
    Nonli        Nonlinearity
    NATi         Nordisk Astronomisk Tidsskrift
    NHCWP        North Hollywood Calif Western Periodicals Co
    NPUJ         Northwestern Polytechnical University Journal
    NoDef        Not Defined
    NoPar        Notes et Informations
    NRA&A        Nouvelle Revue d'Aeronautique et d'Astronautique
    NROpt        Nouvelle Revue d'Optique
    NROA         Nouvelle Revue d'Optique Appliquee
    UGC          Nova Acta Regiae Soc. Sci. Upsaliensis Ser. V
    NTvA         Novaya tekhn. v astron.
    NoIGG        Novosibirsk Institut Geologii i Geofiziki SO AN SSSR
    NovIG        Novosibirsk Institut Gidrodinamiki SO AN SSSR Dinamika Sploshnoi Sredy
    NoIzN        Novosibirsk Izdatel Nauka
    NSSDC        NSSDC Publication
    NTTRv        NTT Review
    NDS          Nuclear Data Sheets
    NDT          Nuclear Data Tables
    NuEnD        Nuclear Engineering and Design
    NucFu        Nuclear Fusion
    NucFS        Nuclear Fusion Special Supplement
    NuGeo        Nuclear Geophysics
    NucIM        Nuclear Instruments and Methods
    NIMPA        Nuclear Instruments and Methods in Physics Research A
    NIMPR        Nuclear Instruments and Methods in Physics Research
    NIMPB        Nuclear Instruments and Methods in Physics Research B
    NucPh        Nuclear Physics
    NuPhA        Nuclear Physics A
    NuPhB        Nuclear Physics B
    NuPhS        Nuclear Physics B Proceedings Supplements
    NSE          Nuclear Science Engineering
    NucTe        Nuclear Technology
    NucTF        Nuclear Technology Fusion
    NuAlg        Numerical Algorithms
    NumHT        Numerical Heat Transfer
    NHTA         Numerical Heat Transfer Part A - Applications
    NHTB         Numerical Heat Transfer Part B - Fundamentals
    NuMat        Numerische Mathematik
    NCimA        Nuovo Cimento A Serie
    NCimB        Nuovo Cimento B Serie
    NCimC        Nuovo Cimento C Geophysics Space Physics C
    NCimD        Nuovo Cimento D Serie
    NCimL        Nuovo Cimento Lettere
    NCimR        Nuovo Cimento Rivista Serie
    NCimS        Nuovo Cimento Serie
    OCSC         OAA Compututer Section Circular
    OVS          Observation of Variable Stars
    Obser        Observation pi
    OSUC         Observationes Astronomicas Insitutas in Specula Universitatis Caesareae Dorpatensis
    OAORP        Observations astronomiques faites a l'Observatoire royal de Paris
    O&T          Observations et Travaux
    USNOO        Observations made at the U.S. Naval Observatory
    OOVRO        Observations Owens Valley Radio Observatory
    OSFOT        Observatoire de la Société Astronomique de France Observations et Travaux
    Bes1K        Observatoire de Besancon
    OBN1K        Observatoire de Besancon - CNES
    Gen1K        Observatoire de Geneve
    Meu1K        Observatoire de Meudon
    Nic1K        Observatoire de Nice
    LPlaC        Observatorio Astronomico de La Plata Circular
    LPlaS        Observatorio Astronomico de La Plata Separata Astronomica
    RosOB        Observatorio Astronomico Municipal de Rosario Argentia  Boletin
    Obs          The Observatory
    HelR         Observatory and Astrophysics Laboratory University of Helsinki Report
    PLPla        Observatory Astronomical La Plata Series Astronomies
    ObVyS        Obzory Vysokotemperaturnoi Sverkhprovodimosti
    ONRAS        Occasional Notes of the Royal Astronomical Society
    ORROE        Occasional Reports of the Royal Observatory Edinburgh
    OccN         Occultation Newsletter, International Occultation Timing Association (IOTA)
    OcDyn        Ocean Dynamics
    OcEng        Ocean Engineering
    OcMod        Ocean Modelling
    OcSci        Ocean Science
    OcScD        Ocean Science Discussions
    OSJ          Ocean Science Journal
    OSJaJ        Oceanographical Society of Japan Journal
    Ocgy         Oceanology
    Ocean        Oceanus Summer
    OAP          Odessa Astronomical Publications
    BOOde        Odesskij Gosudarstvennyi Universitet im. I. I. Mechnikova Byulletin Astronomicheskoj Observatorii
    IzOde        Odesskij Gosudarstvennyi Universitet im. I. I. Mechnikova Izvestiya Astronomicheskoj Observatorii
    OAWMN        Oesterreichische Akademie Wissenschaften Mathematisch naturwissenschaftliche Klasse Sitzungsberichte Abteilung
    Okean        Okeanologiia
    ONCP         Old and New Concepts of Physics
    OCzAS        Ondrejov Czechoslovakia Czechoslovak Academy Sciences CAS Astronomical Institute Publications
    ONERA        ONERA TP
    OAcJ         The Open Acoustics Journal
    OAeEJ        The Open Aerospace Engineering Journal
    OAPJ         The Open Applied Physics Journal
    OAJ          The Open Astronomy Journal
    OASJ         The Open Atmospheric Science Journal
    OCPJ         The Open Chemical Physics Journal
    OCMPJ        The Open Condensed Matter Physics Journal
    OEJV         Open European Journal on Variable Stars
    OGC          The Open Geology Journal
    OHJ          The Open Hydrology Journal
    OJA          Open Journal of Acoustics
    OJAS         Open Journal of Applied Sciences
    OJBp         Open Journal of Biophysics
    OJFD         Open Journal of Fluid Dynamics
    OJGeo        Open Journal of Geology
    OJMic        Open Journal of Microphysics
    OMEJ         The Open Mechanical Engineering Journal
    OMJ          The Open Mechanics Journal
    OMPJ         The Open Mineral Processing Journal
    OMnJ         The Open Mineralogy Journal
    ONJ          The Open Nanoscience Journal
    ONPPJ        The Open Nuclear & Particle Physics Journal
    ONMJ         The Open Numerical Methods Journal
    OOEJ         The Open Ocean Engineering Journal
    OOcJ         The Open Oceanagraphy Journalurnal
    OOJ          The Open Optics Journal
    OPalJ        The Open Paleontology Journal
    OPCJ         The Open Physical Chemistry Journal
    OPPJ         The Open Plasma Physics Journal
    ORSJ         The Open Remote Sensing Journal
    OREJ         The Open Renewable Energy Journal
    OSPJ         The Open Signal Processing Journal
    OSpeJ        The Open Spectroscopy Journal
    OSuJ         The Open Superconductors Journal
    OSSJ         The Open Surface Science Journal
    OSID         Open Systems and Information Dynamics
    AcOpt        Optica Acta
    OptEn        Optical Engineering
    OptFT        Optical Fiber Technology
    OptMa        Optical Materials
    OptPE        Optical Physics and Engineering
    OptRv        Optical Review
    OpSCN        Optical Sciences Center Newsletter
    OptPN        Optics & Photonics News
    OptLE        Optics and Lasers in Engineering
    OPJ          Optics and Photonics Journal
    OptSp        Optics and Spectroscopy
    OptCo        Optics Communications
    OExpr        Optics Express
    OptLT        Optics Laser Technology
    OptL         Optics Letters
    OptN         Optics News
    Optik        Optik
    OpAt         Optika Atmosfery
    OpAtO        Optika Atmosfery i Okeana
    OpSp         Optika i Spektroskopiia
    OpMeP        Optiko Mekhanicheskaia Promyshlennost
    OCAM         Optimal Control Applications and Methods
    OptEL        Optoelectronics Letters
    OERv         Opto-Electronics Review
    OpPuT        Optoelektronika i Poluprovodnikovaia Tekhnika
    OrGeo        Organic Geochemistry
    OrLi         Origins of Life
    OLEB         Origins of Life and Evolution of the Biosphere
    Orion        Orion: Zeitschrift für Amateur-Astronomie
    Ori          Orione
    IGS          Orlando FL Academic Press Inc International Geophysics Series
    OrNav        Ortung und Navigation
    BuENS        Osaka Prefecture University Bulletin Series Engineering Natural Sciences
    OsUTR        Osaka University Technology Reports
    Osir         Osiris
    NapCo        Osservatorio Astronomico di Capodimonte Napoli Contributi Astronomici
    TerCo        Osservatorio Astronomico di Collurania Teramo Contributi
    TerMm        Osservatorio Astronomico di Collurania Teramo Memorie ed Osservazioni
    TerNC        Osservatorio Astronomico di Collurania Teramo Note e Comunicazioni
    PadCR        Osservatorio Astronomico di Padova Comunicazioni e Rassegne
    RomCo        Osservatorio Astronomico di Roma su Monte Mario Contributi Scientifici
    TriP         Osservatorio Astronomico di Trieste Pubblicazioni
    TreP         Osservatorio Privato Specola Ariel Treviso Italia Pubblicazione
    MmArc        Osservazioni e memorie dell'Osservatorio astrofisico di Arcetri
    MmArS        Osservazioni e memorie dell'Osservatorio astrofisico di Arcetri - Appendici
    OtObI        Otbor i Obrabotka Informatsii
    OtPI         Otbor i Peredacha Informatsii
    OISNP        Oxford Pergamon Press International Series on Natural Philosophy
    OISTS        Oxford Pergamon Press International Tables Selected Constants
    OxfOO        Oxford University Observatory Observations
    PalOc        Paleoceanography
    PMetR        Papers in Meteorological Research
    PPh          Papers in Physics
    PMG          Papers Meteorology Geophysics
    PGC          Papers on Global Change IGBP
    ParC         Parallel Computing
    PPhI         Particle Physics Insights
    PRP          Pattern Recognition in Physics
    PaReL        Pattern Recognition Letters
    PerMS        Perceptual Motor Skills
    PZ           Peremennye Zvezdy
    PZP          Peremennye Zvezdy Prilozhenie
    PPEE         Periodica Polytechnica Electrical Engineering
    PPME         Periodica Polytechnica Mechanical Engineering
    PPTE         Periodica Polytechnica Transportation Engineering
    PerCo        Perkins Observatory Contributions
    PMO          Perth Meridien Observations
    PhDT         Ph.D. Thesis
    PhiJR        Philips Journal Research
    PhiRR        Philips Research Reports
    PhiTR        Philips Technical Review
    PMag         Philosophical Magazine
    PMagL        Philosophical Magazine Letters
    PMagA        Philosophical Magazine, Part A
    PMagB        Philosophical Magazine, Part B
    PFP          Philosophy and Foundations of Physics
    Phoen        Phoenix Mitteilungsblatt fuer Veraenderlichenbeobachter
    PhInt        Photo Interpretation
    Pg           Photogrammetria
    PgE          Photogrammetric Engineering
    PgERS        Photogrammetric Engineering and Remote Sensing
    PhSen        Photonic Sensors
    PhNan        Photonics and Nanostructures
    PhoSp        Photonics Spectra
    PhyOJ        Physcs Online Journal
    Phy          Physica
    PhyA         Physica A Statistical Mechanics and its Applications
    PhyB         Physica B Condensed Matter
    PhyBC        Physica B+C
    PhyC         Physica C Superconductivity
    PhyD         Physica D Nonlinear Phenomena
    PhyE         Physica E Low-Dimensional Systems and Nanostructures
    PEFPN        Physica Energiae Fortis et Physica Nuclearis
    PhyNr        Physica Norvegica
    PhyS         Physica Scripta
    PhySB        Physica Scripta B
    PhST         Physica Scripta Volume T
    PSSAR        Physica Status Solidi Applied Research
    PSSBR        Physica Status Solidi B Basic Research
    PSSCR        Physica Status Solidi C Current Topics
    PSSRR        Physica Status Solidi Rapid Research Letters
    PhBio        Physical Biology
    PCCP         Physical Chemistry Chemical Physics (Incorporating Faraday Transactions)
    PCSE         Physical Chemistry: Science and Engineering
    PPHTS        Physical Properties of High Temperature Superconductors
    PhyR         Physical Research
    PhRv         Physical Review
    PhRvA        Physical Review A
    PhRvB        Physical Review B
    PhRvC        Physical Review C
    PhRvD        Physical Review D
    PhRvE        Physical Review E
    PhRvL        Physical Review Letters
    PhRvI        Physical Review Series I
    PhRvS        Physical Review Special Topics Accelerators and Beams
    PRSTP        Physical Review Special Topics Physics Education
    PhRvX        Physical Review X
    PSCEC        Physical Sciences Series of the Commission of European Communities
    PhChH        PhysicoChemical Hydrodynamics
    Physi        Physics
    DokPh        Physics - Doklady
    PCS          Physics and Chemistry in Space
    PCE          Physics and Chemistry of the Earth
    PCEA         Physics and Chemistry of the Earth A
    PCEB         Physics and Chemistry of the Earth B
    PCEC         Physics and Chemistry of the Earth C
    PCED         Physics and Chemistry of the Earth Delta
    PhChE        Physics and Chemistry of Earth
    PCMLD        Physics and Chemistry of Materials with Low-Dimensional Structures
    PCMLA        Physics and Chemistry of Materials with Low-Dimensional Structures Series A
    PCMLB        Physics and Chemistry of Materials with Low-Dimensional Structures Series B
    PCMLC        Physics and Chemistry of Materials with Low-Dimensional Structures Series C
    PCM          Physics and Chemistry of Minerals
    PEEI         Physics and Evolution of the Earth's Interior
    PhApp        Physics and its Applications
    PTPPB        Physics and Technology of Particle and Photon Beams
    PhB          Physics Bulletin
    PhyEd        Physics Education
    PhyEs        Physics Essays
    PCHEI        Physics in Collision: High-Energy ee/ep/pp Interactions
    PMB          Physics in Medicine and Biology
    PhP          Physics in Perspective
    PhTec        Physics in Technology
    PhyIn        Physics International
    PhLF         Physics Laser Fusion
    PhL          Physics Letters
    PhLA         Physics Letters A
    PhLB         Physics Letters B
    PhLC         Physics Letters Section C Physics Reports C
    PhyNY        Physics New York
    PhyN         Physics Notes
    PDU          Physics of the Dark Universe
    PEPI         Physics of the Earth and Planetary Interiors
    PhSS         Physics of the Solid State
    PAN          Physics of Atomic Nuclei
    PAM          Physics of Atoms and Molecules
    PhFl         Physics of Fluids
    PhFlB        Physics of Fluids B
    PhLRv        Physics of Life Reviews
    PLDS         Physics of Low-Dimensional Structures
    PhMet        Physics of Metals
    PMM          Physics of Metals and Metallography
    PPN          Physics of Particles and Nuclei
    PPNL         Physics of Particles and Nuclei Letters
    PhPl         Physics of Plasmas
    PhQE         Physics of Quantum Electronics
    PSL          Physics of Solids and Liquids
    PWP          Physics of Wave Phenomena
    PhR          Physics Reports
    PRI          Physics Research International
    PhTea        The Physics Teacher
    PhT          Physics Today
    PhyU         Physics Uspekhi
    PhyW         Physics World
    PKM          Physik der Kondensierten Materie
    PhuZ         Physik in unserer Zeit
    PCTM         Physikalisch-Chemische Trenn- und Messmethoden
    PhyBl        Physikalische Blötter
    PhyG         Physikalische Gesellschaft
    PhyGZ        Physikalische Gesellschaft Zürich
    PhyZ         Physikalische Zeitschrift
    PhyM         Physiological Measurement
    PhylS        Physiologist Supplement
    PAZh         Pisma v Astronomicheskii Zhurnal
    PZETF        Pisma Zhurnal Eksperimental noi i Teoreticheskoi Fiziki
    PZhTF        Pisma Zhurnal Tekhnischeskoi Fiziki
    P&SS         Planetary and Space Science
    PlAst        Planetary Astronomy
    PlR          Planetary Report
    PlSci        Planetary Science
    PFR          Plasma and Fusion Research
    PlPh         Plasma Physics
    PPCF         Plasma Physics and Controlled Fusion
    PlPhR        Plasma Physics Reports
    PlST         Plasma Science and Technology
    PSST         Plasma Sources Science Technology
    PRFVT        Plastiques Renforces Fibres de Verre Textile
    PLSCB        PLoS Computational Biology
    PLoSO        PLoS ONE
    PMCPA        PMC Physics A
    PMCPB        PMC Physics B
    PMCPC        PMC Physics C
    PMTF         PMTF Zhurnal Prikladnoi Mekhaniki i Tekhnicheskoi Fiziki
    PnGid        Pnevmatika i Gidravlika
    PolSc        Polar Science
    PolSi        Poliarnye Siianiia
    PSSNN        Poliarnye Siianiia i Svechenie Nochnogo Neba
    PASAM        Polish Academy of Science Arch Mech
    PASAS        Polish Academy of Science Artificial Satellites
    PASIG        Polish Academy of Sciences Institute of Geophysics Publications
    PJMPE        Polish Journal of Medical Physics And Engineering
    PCZNN        Politechnika Czestochowska Zeszyty Naukowe Nauki Techniczne Mechanika
    PGZNM        Politechnika Gdanska Zeszyty Naukowe Mechanika
    PSZNM        Politechnika Slaska Zeszyty Naukowe Mechanika
    PolAt        Pollution Atmospherique
    PolTM        Poluprovodnikovaia Tekhnika i Mikroelektronika
    PolPP        Poluprovodnikovye Pribory i ikh Primenenie
    PoCom        Polymer Composites
    PolPh        Polymer Physics
    PomAK        Pomiary Automatyka Kontrola
    PA           Popular Astronomy
    PorMe        Poroshkovaia Metallurgiia
    PoAn         Postepy Astronautyki
    PoAst        Postepy Astronomii Krakow
    PSci         Pour la Science
    PDiff        Powder Diffraction
    PUAMA        Poznan Uniwersytet im Adama Mickiewicza Seria Akustyka
    PUAMF        Poznan Uniwersytet im Adama Mickiewicza Seria Fizyka
    PrAst        Practical Astronomy
    PraAc        Prague Academia
    Prama        Pramana
    PreR         Precambrian Research
    Prib         Priborostroenie
    PriTE        Pribory i Tekhnika Eksperimenta
    PriMM        Prikladnaia Matematika i Mekhanika
    PriMP        Prikladnaia Matematika i Programmirovanie
    PriM         Prikladnaia Mekhanika
    PPPLR        Princeton Plasma Physics Laboratory Report
    Prir         Priroda
    Priv         Private Communication
    PrEM         Probabilistic Engineering Mechanics
    PrAiA        Problemy Arktiki i Antarktiki
    PrBio        Problemy Bioniki
    PrDRV        Problemy Difraktsii i Rasprostraneniia Voln
    PrFA         Problemy Fiziki Atmosfery
    PrFKL        Problemy Iadernoi Fiziki i Kosmicheskikh Luchei
    PrKFi        Problemy Kosmicheskoi Fiziki
    PrMas        Problemy Mashinostroeniia
    PrPro        Problemy Prochnosti
    PrSP         Problemy Sluchainogo Poiska
    PrTE         Problemy Tekhnicheskoi Elektrodinamiki
    PrTGE        Problemy Teorii Gravitatsii i Elementarnykh Chastits
    PrTPT        Problemy Teploenergetiki i Prikladnoi Teplofiziki
    PJAB         Proceeding of the Japan Academy, Series B
    PAPhS        Proceedings of the American Philosophical Society
    PASAu        Proceedings of the Astronomical Society of Australia
    PCAS         Proceedings of the California Academy of Sciences
    PCPS         Proceedings of the Cambridge Philosophical Society
    PIASE        Proceedings of the Indian Academy of Science, Earth and Planetary Sciences
    PINSA        Proceedings of the Indian National Science Academy Part A
    PINSB        Proceedings of the Indian National Science Academy Part B
    PIGP         Proceedings of the Institute of General Physics, Adademy of the Sciences of Russia
    PILOM        Proceedings of the International Latitude Observatory at Mizusawa
    PIRE         Proceedings of the IRE
    PNAS         Proceedings of the National Academy of Science
    PNSC         Proceedings of the National Science Council
    PNSBP        Proceedings of the National Society of Black Physicists
    PPS          Proceedings of the Physical Society
    PPSA         Proceedings of the Physical Society A
    PPSB         Proceedings of the Physical Society B
    PPSL         Proceedings of the Physical Society of London
    PRIAN        Proceedings of the Research Institute of Atmospherics, Nagoya University
    PRIAA        Proceedings of the Royal Irish Academy Section A
    PrVP         Proceedings of Vibration Problems
    PrAeS        Progress in Aerospace Sciences
    PrAA         Progress in Astronautics and Aeronautics
    PABei        Progress in Astronomy
    PrA          Progress in Astronomy
    PrECS        Progress in Energy and Combustion Science
    PrMS         Progress in Materials Science
    PMatP        Progress in Mathematical Physics
    PMRP         Progress in Medical Radiation Physics
    PMetP        Progress in Metal Physics
    PNSci        Progress in Natural Science
    PrOce        Progress in Oceanography
    POrCo        Progress in Organic Coatings
    PrPNP        Progress in Particle and Nuclear Physics
    PPcPp        Progress in Photochemistry and Photophysics
    PrPh         Progress in Physics
    PQE          Progress in Quantum Electronics
    PrSS         Progress In Surface Science
    PTCP         Progress in Theoretical Chemistry and Physics
    PTEP         Progress of Theoretical and Experimental Physics
    PThPh        Progress of Theoretical Physics
    PThPS        Progress of Theoretical Physics Supplement
    ProTe        Promyshlennaia Teplotekhnika
    PrEx         Propellants and Explosives
    PrExP        Propellants and Explosives Pyrotechnics
    PMMin        Proper Motion Survey, University of Minnesota
    PUFir        Pubblicazioni della R. Universita degli studi di Firenze
    PSAIL        Pubblicazioni della Stazione Astronomica Internazionale di Latitudine
    POMil        Pubblicazioni dell'Osservatorio Astronomico di Milano-Merate
    POPad        Pubblicazioni dell'Osservatorio Astronomico di Padova
    POTor        Pubblicazioni Varie Fuori Serie dell'Osservatorio Astronomico di Torino
    PKCat        Publ. House Czech. Acad. Sci.
    POStr        Publication de l'Observatoire de Strasbourg
    PUSK         Publication der Koeniglichen Sternwarte in Kiel
    PPCAS        Publication of the Pomona College Astronomical Society
    PKAS         Publication of Korean Astronomical Society
    PSCDS        Publication Speciale du Centre de Donnees Stellaires
    PIAGL        Publications de l'Institut d'Astronomie et de Geophysique Georges Lemaitre
    POBeo        Publications de l'Observatoire Astronomique de Beograd
    PASK         Publications of the Academy of Science Kasakstan Sect. Astrobotanics
    PAllO        Publications of the Allegheny Observatory of the University of Pittsburgh
    PAICU        Publications of the Astronomical Institute of the Charles University
    PAICz        Publications of the Astronomical Institute of the Czechoslovak Academy of Sciences
    PUAms        Publications of the Astronomical Institute of the University of Amsterdam
    PBrn         Publications of the Astronomical Institute of the University of Borneo
    POHel        Publications of the Astronomical Observatory Helsinki
    PAOS         Publications of the Astronomical Observatory of Sarajevo
    POMin        Publications of the Astronomical Observatory University of Minnesota
    PASP         Publications of the Astronomical Society of the Pacific
    PASA         Publications of the Astronomical Society of Australia
    PASJ         Publications of the Astronomical Society of Japan
    PASRB        Publications of the Astronomical Society "Rudjer Boskovic"
    PADEU        Publications of the Astronomy Department of the Eotvos Lorand University
    PAIB         Publications of the Astronomy Institute of Bonn
    PAB          Publications of The Astrophysics Branch Ottawa
    PBeiO        Publications of the Beijing Astronomical Observatory
    PBosO        Publications of the Bosscha Observatory Lembang Indonesia
    PCinO        Publications of the Cincinnati Observatory
    PCooO        Publications of the Cook Observatory
    PDDO         Publications of the David Dunlap Observatory
    PDAUC        Publications of the Department of Astronomy University of Chile
    PDAO         Publications of the Dominion Astrophysical Observatory Victoria
    PDO          Publications of the Dominion Observatory Ottawa
    PDreO        Publications of the Dresden Observatory
    PGLO         Publications of the Goethe Link Observatory
    PGooO        Publications of the Goodsell Observatory, Carleton College
    ILOMP        Publications of the International Latitude Observatory at Mizusawa
    PIstO        Publications of the Istanbul University Observatory
    PGro         Publications of the Kapteyn Astronomical Laboratory Groningen
    PKirO        Publications of the Kirkwood Observatory of Indiana University
    PAth         Publications of the Laborotory of Astronomy University of Athens
    PMcCO        Publications of the Leander McCormick Observatory
    PManO        Publications of the Manila Observatory
    PMunO        Publications of the Munich Observatory
    PNAOC        Publications of the National Astronomical Observatories of China
    PNAOJ        Publications of the National Astronomical Observatory of Japan
    POLyo        Publications of the Observatoire de Lyon
    PGenA        Publications of the Observatoire Geneve Series A
    PGenB        Publications of the Observatoire Geneve Series B
    POHP         Publications of the Observatoire Haute-Provence
    POANC        Publications of the Observatorie Astronomie Nacional Cerro Calan
    POVRO        Publications of the Owens Valley Observatory
    PPMtO        Publications of the Purple Mountain Observatory
    PRCO         Publications of the Riverview College Observatory
    PROE         Publications of the Royal Observatory of Edinburgh
    PSAO         Publications of the Shaanxi Astronomical Observatory
    PShaO        Publications of the Shaanxi Astronomy Observatory
    PSprO        Publications of the Sproul Observatory
    PTarO        Publications of the Tartu Astrofizica Observatory
    PTasO        Publications of the Tashkent Astronomical Observatory
    PUPFA        Publications of the University of Pennsylvania Flower Astronomical Observatory
    PUSNO        Publications of the U.S. Naval Observatory Second Series
    PVVO         Publications of the Van Vleck Observatory
    PVasO        Publications of the Vassar College Observatory
    PW&SO        Publications of the Warner & Swasey Observatory
    PWasO        Publications of the Washburn Observatory
    PYerO        Publications of the Yerkes Observatory
    PYunO        Publications of the Yunnan Observatory
    PDHO         Publications of Debrecen Heliophysical Observatory
    POBol        Publications of dell'Osservatorio Astronomie de Bologna
    PLicO        Publications of Lick Observatory
    POMic        Publications of Michigan Observatory
    PCat         Publications of Osservatorio Astrofisico di Catania
    PWHHO        Publications of West Hendon House Observatory, Sunderland
    POxf         Publications University of Oxford Department of Astrophysics
    PKUJ         Publikationen der Kaiserlichen Universitaets-Sternwarte Jurjew
    PAIKH        Publikationen des Astrophysikalischen Instituts Koenigstuhl-Heidelberg
    POPot        Publikationen des Astrophysikalischen Observatoriums zu Potsdam
    PCopO        Publikationer og mindre Meddeler fra Kobenhavns Observatorium
    PGAOI        Pulkovo Glavnaia Astronomicheskaia Observatoriia Izvestiia
    PApCh        Pure & Applied Chemistry
    PApGe        Pure and Applied Geophysics
    PApPh        Pure and Applied Physics
    PApOp        Pure Applied Optics
    QREI         Quality Reliability Engineering International
    QuFin        Quantitative Finance
    QuEle        Quantum Electronics
    QuIP         Quantum Information Processing
    QuOpt        Quantum Optics
    QBSA         Quarterly Bulletin on Solar Activity
    QJRAS        Quarterly Journal of the Royal Astronomical Society
    QJRMS        Quarterly Journal of the Royal Meteorological Society
    QJMat        The Quarterly Journal of Mathematics
    QJMAM        Quarterly Journal of Mechanics and Applied Mathematics
    QJPAM        The Quarterly Journal of Pure and Applied Mathematics
    QApMa        Quarterly of Applied Mathematics
    QuInt        Quaternary International
    QuRes        Quaternary Research
    QSRv         Quaternary Science Reviews
    Rad          Radiant, Journal of the Dutch Meteor Society
    RadEf        Radiation Effects
    REDS         Radiation Effects and Defects in Solids
    RaPC         Radiation Physics and Chemistry
    RaEE         Radio and Electronic Engineer
    RPRA         Radio Physics and Radio Astronomy
    RaRLJ        Radio Research Laboratory, Journal
    RaRLR        Radio Research Laboratory, Review
    RaSc         Radio Science
    Radel        Radioehlektronika
    RaF          Radiofizika
    R&QE         Radiophysics and Quantum Electronics
    RaEl         Radiotekhnika i Elektronika
    RTRE         Radiotekhnika Tecommunications Radio Engineering Radio Engineering
    LeRad        Le Radium
    RF           Raumfahrtforschung
    RRDAP        Recent Research Development in Applied Physics
    RRDBC        Recent Research Development in Biophysical Chemistry
    RRDBB        Recent Research Development in Biophysics and Biochemistry
    RRDCP        Recent Research Development in Chemical Physics
    RRDPC        Recent Research Development in Physical Chemistry
    RRDP         Recent Research Development in Physics
    RRDPF        Recent Research Development in Physics of Fluids
    RRDSP        Recent Research Development in Statistical Physics
    Rech         La Recherche
    RAOU         Recherches Astronomiques de l'Observatoire d'Utrecht
    RZh          Referationyj Zhurnal
    RCD          Regular and Chaotic Dynamics
    RSEMS        Remote Sensing Electro Magnetic Spectrum
    RSEnv        Remote Sensing of Environment
    RSQ          Remote Sensing Quarterly
    HarOR        Report of the Committee of the Overseers of Harvard College appointed to visit the Observatory
    RNAOJ        Report of the National Astronomical Observatory of Japan
    RSPUT        Report Series of the Department of Physics and Science, University of Turku
    YalRY        Reports for the year presented by the Board of Managers of the Observatory of Yale University to the President and Fellows
    ROLun        Reports of the Lund Observatory
    RpMP         Reports on Mathematical Physics
    RPPh         Reports on Progress in Physics
    BeiRe        Reprints Beijing Astronomical Observatory Academia Sinica
    ROCi         Republic Observatory Johannesburg Circular
    ChPAS        Republic of China National Science Council Proceedings Applied Sciences
    RAA          Research in Astronomy and Astrophysics
    ReNEv        Research in Nondestructive Evaluation
    RSTEd        Research in Science and Technological Education
    RScEd        Research in Science Education
    RLOpt        Research Letters in Optics
    RLPhy        Research Letters in Physics
    RNOST        Research News & Opportunities in Science and Theology
    RPFSU        Research Papers Faculty of Materials Science and Technology Slovak University of Technology
    RRP          Research Reports in Physics
    RTP          Research Trends in Physics
    RNAO         Resultados del Observatorio Nacional Argentino
    ROCor        Resultados del Observatorio Nacional Argentino en Cordoba
    ResPh        Results in Physics
    RvPT         Review of Physics in Technology
    RScI         Review of Scientific Instruments
    RvAqS        Reviews in Aquatic Sciences
    RvMaP        Reviews in Mathematical Physics
    RvMA         Reviews in Modern Astronomy
    RvRRL        Reviews of the Radio Research Laboratory
    RvGeo        Reviews of Geophysics
    RvGSP        Reviews of Geophysics and Space Physics
    RvGeS        Reviews of Geophysics Supplement
    RvMin        Reviews of Mineralogy
    RvMP         Reviews of Modern Physics
    RvMPS        Reviews of Modern Physics Supplement
    RvOp         Reviews of Optics
    RvPP         Reviews of Plasma Physics
    RvA          Revista Astronomica Organo de la Asociacion Argengina Amigos de la Astronomia Buenos Aires
    RBrFi        Revista Brasileira de Fisica
    RvCF         Revista Colombiana de Fisica
    RMxAA        Revista Mexicana de Astronomia y Astrofisica
    RMxF         Revista Mexicana de Fisica
    RMxFE        Revista Mexicana de Fisica E
    RMxFS        Revista Mexicana de Fisica Supplement
    RvMad        Revista Real Acad. Ciencias Exact. Fis. Nat. Madrid
    RTrTe        Revista Transporturilor si Telecomunicatiilor
    AerRv        Revue Aerospatiale
    RvAc         Revue d'Acoustique
    RvPA         Revue de Physique Appliquee
    RvPD         Revue du Palais de la Decouverte
    RFrM         Revue Francaise de Mecanique
    RRMPA        Revue Roumaine de Mathematiques Pures et Appliquees
    RvRP         Revue Roumaine de Physique
    RvRST        Revue Roumaine des Sciences Techniques Serie de Mecanique Appliquee
    RST          Revue Scientifique et Technique CECLES CERS
    RvT          Revue Technique Thomson CSF
    RNISZ        Rezul taty Nabliudenii Iskusstvennykh Sputnikov Zemli
    RWTHA        Rheinisch Westfaelische Technische Hochschule Aerodynamisches Institut Abhandlungen
    AcRhe        Rheologica Acta
    RA           Ricerche Astronomiche
    Rise         Rise Hvezd
    RIG          Rivista Italiana di Geofisica
    RvTS         Rivista Tecnica Selenia
    Robot        Robotica
    RMRE         Rock Mechanics and Rock Engineering
    RMFMR        Rock Mechanics Felsmechanik Mecanique des Roches
    Roczn        Rocznik Astronomiczny Observatorjum Krakowskiego Krakow
    RoAJ         Romanian Astronomical Journal
    RoJPh        Romanian Journal of Physics
    RoRPh        Romanian Reports in Physics
    RoIE         Rossiiskaia Akademiia Nauk Izvestiia Energetika
    RoIMZ        Rossiiskaia Akademiia Nauk Izvestiia Mekhanika Zhidkosti i Gaza
    RoISF        Rossiiskaia Akademiia Nauk Izvestiia Seriia Fizicheskaia
    RoDok        Rossijskaya Akademiya Nauk Doklady
    RoIMT        Rossijskaya Akademiya Nauk Izvestiya Mekhanika Tverdogo Tela
    RoIzF        Rossijskaya Akademiya Nauk Izvestiya Seriya Fizicheskaya
    RWPWZ        Rostock Wilhelm Pieck Universitaet Wissenschaftliche Zeitschrift Mathematisch Naturwissenschaftliche Reihe
    PVSS         Royal Astronomical Society of New Zealand Publications of Variable Star Section
    VSSCi        Royal Astronomical Society of New Zealand Variable Star Section Circulars
    RGOB         Royal Greenwich Observatory Bulletins
    ROAn         Royal Observatory Annals
    CoRSE        Royal Society Edinburgh Communications Physical Sciences
    RSCT         Royal Society of Canada Transactions
    RSEPS        Royal Society of Edinburgh Proceedings Section
    RSET         Royal Society of Edinburgh Transactions
    RSN&R        Royal Society of London Notes & Records
    RSPTA        Royal Society of London Philosophical Transactions Series A
    RSPTB        Royal Society of London Philosophical Transactions Series B
    RSPT         Royal Society of London Philosophical Transactions Series I
    RSPSA        Royal Society of London Proceedings Series A
    RSPSB        Royal Society of London Proceedings Series B
    RSPS         Royal Society of London Proceedings Series I
    RoIn         Rozprawy Inzynierskie
    RoIET        Rozprawy Inzynierskie Engineering Transactions
    Ruimt        Ruimtevaart
    RuCRv        Russian Chemical Reviews
    RuGG         Russian Geology and Geophysics
    RJMP         Russian Journal of Mathematical Physics
    RuMaS        Russian Mathematical Surveys
    RuMet        Russian Metallurgy
    RuPhJ        Russian Physics Journal
    RALR         Rutherford Appleton Laboratory Report
    rxte prop    RXTE Proposal
    Sadha        Sadhana
    STVF         Samoletostroenie Tekhnika Vozdushnogo Flota
    SAMPJ        SAMPE Journal
    SAMPQ        SAMPE Quarterly
    UISTS        San Diego CA Univelt Inc Science Technology Series
    MaMeA        Sankt Peterburgskii Universitet Vestnik Seriia Matematika Mekhanika Astronomiia
    SAOSR        SAO Special Report
    SatCo        Satellite Communications
    SBARM        SBARMO Bulletin
    SbMat        Sbornik: Mathematics
    SUVSR        Scandinavian Union of Amateur Astronomers Variable Star Section
    ScReE        Scholarly Research Exchange
    SNG          Schweizerische Naturforschende Gesellschaft
    SRToh        Sci. Rep. Tohoku Univ. Eighth Ser.
    Sci          Science
    Sc&Ed        Science & Education
    SCSA         Science and Culture Series: Astrophysics
    SCSP         Science and Culture Series: Physics
    SECM         Science and Engineering of Composite Materials
    STAdM        Science and Technology of Advanced Materials
    SCSMP        Science China Series Mathematics Physics Astronomy Technological Sciences
    SciDi        Science Dimension
    SciEd        Science Education
    ScEdR        Science Education Research
    SFCh         Science Foundation in China
    ScChA        Science in China A: Mathematics
    ScChB        Science in China B: Chemistry
    ScChD        Science in China D: Earth Sciences
    ScChG        Science in China G: Physics and Astronomy
    SISN         Science Information Systems Newsletter
    SciN         Science News
    ScTEn        Science of the Total Environment
    ScPr         Science Progress
    Scis         Sciences
    Sc&Te        Sciences et Techniques
    SciB         Scientia (Bologna)
    SciSn        Scientia Sinica
    SSPMA        Scientia Sinica Physica, Mechanica & Astronomica
    SSSMP        Scientia Sinica Series Mathematical Physical Technical Sciences
    SciAm        Scientific American
    SMS          Scientific Modeling and Simulation SMNS
    SciMo        The Scientific Monthly
    Scim         Scientometrics
    SFSN         Scripta Faculty Science Nat. Ujep Brunensis Physica
    ScM          Scripta Metallurgica
    ScMM         Scripta Metallurgica et Materialia
    SedG         Sedimentary Geology
    Sedim        Sedimentology
    SeiKa        Seikei-Kakou
    BSSA         Seismological Society America Bulletin
    SEGeo        Seismology and Exploration Geophysics
    STSSP        Selected Topics in Solid State Physics
    SeScT        Semiconductor Science Technology
    Semic        Semiconductors
    TrKra        Seminar Kraevym Zadacham Trudy
    SCB          Seminars in Cancer Biology
    GEOCS        Semi-Regular Variables
    SenAR        Sendai Astronomiaj Raportoj
    SenIm        Sensing and Imaging
    SPTS         Sensor Physics and Technology Series
    SeAc         Sensors and Actuators
    SAERI        Seoul Korea Atomic Energy Research Institute
    SanS         Separata Universidad de Chile Departamento de Astronomia Santiago
    SerAJ        Serbian Astronomical Journal
    AnShO        Shanghai Observatory Annals
    SVD          Shock Vibration Digest
    SVICB        Shock Vibration Information Center Shock Vibration Bulletin
    SVICP        Shock Vibration Information Center Shock Vibration Computer Programs
    SVICD        Shock Vibration Information Center Shock Vibration Digest
    SVICI        Shock Vibration Information Center Shock Vibration Inform Digest
    ShWav        Shock Waves
    SJAM         SIAM Journal of Applied Mathematics
    SJCO         SIAM Journal of Control Optimization
    SJMA         SIAM Journal of Mathematical Analysis
    SJADS        SIAM Journal on Applied Dynamical Systems
    SJNA         SIAM Journal on Numerical Analysis
    SIAMR        SIAM Review
    SiFTZ        Sibirskii Fiziko Tekhnicheskii Zhurnal
    JCMSI        SICE Journal of Control, Measurement, and System Integration
    SIDPQ        SID Proceedings Quarter
    SiFoE        Siemens Forschungs und Entwicklungsberichte
    SIGMA        SIGMA
    Sig          Signal
    SigPr        Signal Processing
    Simul        Simulation
    SiMol        Single Molecules
    SZPA         SIRIUS. Zeitschrift fuer Populaere Astronomie
    Situ         Situ
    SkInq        Skeptical Inquirer
    S&T          Sky and Telescope
    SkyN         Sky News
    SlaOb        Slaboproudy Obzor
    SJCE         Slovak Journal of Civil Engineering
    SMaS         Smart Material Structures
    Smith        Smithsonian
    SmCES        Smithsonian Contributions to the Earth Sciences
    SCoA         Smithsonian Contributions to Astrophysics
    SCoK         Smithsonian Contributions to Knowledge
    SSS          Social Studies of Science
    MSAIQ        Societa Astronomica Italiana Memorie Quarter
    SFPTB        Societe Francaise de Photogrammetrie et de Teledetection Bulletin
    SASS         Society for Astronomical Sciences Annual Symposium
    SEEJ         Society of Environmental Engineers Journal
    SIAM         Society of Industrial and Applied Mathematics
    SIBAN        Sofia Izdatel Bolgarskoi Akademii Nauk
    SMat         Soft Matter
    SSSAJ        Soil Science Society of America Journal
    SoCe         Solar Cells
    SoEn         Solar Energy
    SoEnM        Solar Energy Materials
    SoPh         Solar Physics
    SoSyR        Solar System Research
    STERJ        Solar Terrestrial and Environmental Research Japan
    SolE         Solid Earth
    SolED        Solid Earth Discussions
    SMArc        Solid Mechanics Archives
    SSCom        Solid State Communications
    SSEle        Solid State Electronics
    SSPAR        Solid State Physics Advances in Research and Applications
    SSPAS        Solid State Physics Advances in Research and Applications Supplement
    SSSci        Solid State Sciences
    SSTec        Solid State Technology
    BSolD        Solnechnye Dann. Bull. Akad. Nauk SSSR
    SoKie        Sonderdrucke der Sternwarte Kiel
    SoMue        Sonderdrucke Universitaet Muenster Astronomisches Institut
    Sonne        Sonne
    SoShe        Soobshchenie Shemakhinskoj Astrofizicheskoj Observatorii
    SoByu        Soobshcheniya Byurakanskoj Observatorii Akademiya Nauk Armyanskoj SSR Erevan
    SoSht        Soobshcheniya Gosudarstvennogo Astronomicheskogo Instituta
    SoSAO        Soobshcheniya Spetsial'noj Astrofizicheskoj Observatorii
    SMTS         Soprotivlenie Materialov i Teoriia Sooruzhenii
    SSHMP        Sources and Studies in the History of Mathematics and Physical Sciences
    SHMPS        Sources in the History of Mathematics and Physical Sciences
    SAAOC        South African Astronomical Observatory Circular
    SAAOR        South African Astronomical Observatory Republic
    SAJPh        South African Journal of Physics
    SAJSc        South African Journal of Science
    SouSt        Southern Stars
    IBSAE        Sovetskaia Antarkticheskaia Ekspeditsiia Informatsionnyi Byulleten
    SovAe        Soviet Aeronomii
    SvApM        Soviet Applied Mechanics
    SvA          Soviet Astronomy
    SvAL         Soviet Astronomy Letters
    JETP         Soviet Journal of Experimental and Theoretical Physics
    JETPL        Soviet Journal of Experimental and Theoretical Physics Letters
    SvJNP        Soviet Journal of Nuclear Physics
    SvJOT        Soviet Journal of Optical Technology
    SvJPP        Soviet Journal of Plasma Physics
    SvJQE        Soviet Journal of Quantum Electronics
    SvPhA        Soviet Physics Astronomy
    SPhD         Soviet Physics Doklady
    SvPhJ        Soviet Physics Journal
    SPTP         Soviet Physics Technical Physics
    SvPhU        Soviet Physics Uspekhi
    SvRP         Soviet Radiophysics
    SSRvA        Soviet Scientific Reviews A Physics Reviews
    SSRvC        Soviet Scientific Reviews C Mathematical Physics Reviews
    SSRvD        Soviet Scientific Reviews D Physicochemical Biology Reviews
    Space        Space
    SSPRv        Space and Solar Power Review
    SpCoB        Space Communication Broadcasting
    SpCom        Space Communications
    SpEd         Space Education
    SLSci        Space Life Sciences
    SpMar        Space Markets
    SpMME        Space Medicine Medical Engineering
    SpPol        Space Policy
    SpPow        Space Power
    SPRMD        Space Power - Resources, Manufacturing and  Development
    SpRBu        Space Research Bulgaria
    SpReT        Space Research Today
    SSI          Space Science Instrumentation
    SSRv         Space Science Reviews
    SpT          Space Technology
    STICA        Space Technology Industrial and Commercial Applications
    asc  rept    Space Telescope ASC Instrument Science Report
    STECF        Space Telescope European Coordinating Facility Newsletter
    nicm rept    Space Telescope NICMOS Instrument Science Report
    stis rept    Space Telescope STIS Instrument Science Report
    wfc  rept    Space Telescope WFC Instrument Science Report
    wfpc rept    Space Telescope WFPC2 Instrument Science Report
    SpWea        Space Weather
    SpWd         Space World
    SpWdU        Space World U
    SpWdW        Space World W
    SpWdY        Space World Y
    SpFl         Spaceflight
    Spvw         Spaceview
    Spark        Spark, the AAS Education Newsletter
    VatAR        Specola Astronomica Vaticana Annual Reports
    VatCo        Specola Astronomica Vaticana Comunicazione
    VatMA        Specola Astronomica Vaticana Miscellanea Astronomica
    VatPS        Specola Astronomica Vaticana Pubblicazioni Serie Seconda
    VatRS        Specola Astronomica Vaticana Ricerche Spettroscopiche
    VatRA        Specola Astronomica Vaticana Richerche Astronomiche
    AcSpe        Spectrochimica Acta
    AcSpA        Spectrochimica Acta Part A: Molecular Spectroscopy
    SpecL        Spectroscopy Letters
    SRMO         Specula Regia Monachiensi Observationes astronomicae
    SScT         Speculations in Science and Technology
    Spika        Spika
    sptz prop    Spitzer Proposal
    SSSSc        Springer Series in Surface Sciences
    STMP         Springer Tracts in Modern Physics
    SSCP         Springer Verlag Springer Series on Chemical Physics
    SSEp         Springer Verlag Springer Series on Electrophysics
    SSGSR        Springer Verlag Springer Series on Group Geophysics Space Research
    SSOS         Springer Verlag Springer Series on Optical Sciences
    SVPCS        Springer Verlag Springer Series on Physics Chemistry Space
    SSSSS        Springer Verlag Springer Series on Solid State Sciences
    SSSyn        Springer Verlag Springer Series on Synergetics
    SSWP         Springer Verlag Springer Series on Wave Phenomena
    SrLJP        Sri Lankan Journal of Physics
    SANUG        Srpska Akademiia Nauka i Umetnosti Glas Odeljenje Tekhnichkikh Nauka
    SRXPh        SRX Physics
    StSky        Star Sky
    StarD        StarDate Magazine
    StMet        Statistical Methodology
    StaSc        Statistical Science
    StReL        Staub Reinhaltung Luft
    SMSPS        Stephan Mueller Special Publication Series
    Stern        Die Sterne
    S&W          Sterne und Weltraum
    Sterz        Sternzeit Mitteilungen der Astrnomischen Vereinigungen Aachen
    IEWS         Stevenage Herts England Peter Peregrinus Ltd IEE Electromagnetic Waves Series
    TriTr        STLE Tribology Transactions
    SHH          Stochastic Hydrology and Hydraulics
    StoAn        Stockholms Observatoriums Annaler
    StoOR        Stockholms Observatoriums Reports
    Strai        Strain
    SGC          Stratigraphy and Geological Correlation
    Stroj        Strojarstvo
    StAst        Strolling Astronomer
    StrOp        Structural Optimization
    SASn         Studia Astronomica Sinica
    StGG         Studia Geophysica et Geodaetica
    StuMa        Studia Mathematica
    SSTor        Studia Societatis Scientiarum Torunensis Sectio F Astronomia
    StHPM        Studies in the History and Philosophy of Modern Physics
    StHMP        Studies in the History of Mathematics and the Physical Sciences
    StAM         Studies in Applied Mathematics
    SCMP         Studies in Condensed Matter Physics
    SGORS        Studies in Geophysical Optics and Remote Sensing
    StGeo        Studies in Geophysics
    StHEP        Studies in High Energy Physics
    StHCG        Studies in High Energy Physics Cosmology and Gravitation
    SScEd        Studies in Science Education
    Sttur        Studies in turbulence
    SCA          Studii si Cercetari de Astronomie Bucuresti
    StCeF        Studii si Cercetari de Fizica
    StCeM        Studii si Cercetari Matematice
    StCMA        Studii si Cercetary de Mecanica Aplicata
    suba prop    Subaru Proposal
    SunGe        Sun and Geosphere
    Sunwo        Sunworld
    SuScT        Superconductor Science Technology
    SuMi         Superlattices and Microstructures
    JPhSu        Supplement au Journal de Physique
    AnMuS        Supplementband zu den Annalen der Munchener Sternwarte
    SAnAp        Supplements aux Annales d'Astrophysique
    SurIA        Surface and Interface Analysis
    SRL          Surface Review and Letters
    SurSc        Surface Science
    SurSR        Surface Science Reports
    SurSS        Surface Science Spectra
    SGeo         Surveys in Geophysics
    SHEP         Surveys in High Energy Physics
    SvPro        Svarochnoe Proizvodstvo
    SvUNT        Sverdlovsk Ural skii Nauchnyi Tsentr AN SSSR
    SydOP        Sydney Observatory Papers
    SyTec        Systems Technology
    TMPGO        Tagung ueber Mathematische Probleme Geodaesie Oberwolfach West Germany Bulleting Geodesique
    TANEs        Tartu Akademiia Nauk Estonskoi SSR
    TarOT        Tartu Astrofuusika Observatoorium Teated
    IzTas        Tashkent Izdatel Fan
    IzGeo        Tbilisi Georgian SSR Izdatel Metsniereba
    TIzSS        Tbilisi Izdatel Sabchota Sakartvelo
    TecN         Technical News
    TePhL        Technical Physics Letters
    TeLoA        Technika Lotnicza i Astronautyczna
    TBBM         Techniques of Biochemical and Biophysical Morphology
    TPhy         Techniques of Physics
    ToIzL        Technisch oekonomische Informationen zivilen Luftfahrt
    TMKF         Technische Mitteilungen Krupp Forschungsberichte
    TUnGG        Technische Univ Geodesy Global Geodyn
    Tech         Technology
    TecRv        Technology Review
    Tecto        Tectonics
    Tectp        Tectonophysics
    TekEl        Tekhnicheskaia Elektrodinamika
    TJAu         Telecommunication Journal of Australia
    TDAPR        Telecommunications and Data Acquisition Progress Report
    TMOPR        Telecommunications and Mission Operations Progress Report
    TRET         Telecommunications and Radio Engineering Telecommunications
    TelIn        Telematics Informatics
    Telet        Telettra S
    Tell         Tellus
    TellA        Tellus Series A
    TellB        Tellus Series B Chemical and Physical Meteorology B
    TSDMO        Tellus Series Dynamic Meteorology and Oceanography
    TeoEl        Teoreticheskaia Elektrotekhnika
    TeoPM        Teoreticheskaia i Prikladnaia Mekhanika
    TFFAP        Teoriia Funktsii Funktsional nyi Analiz i ikh Prilozheniia
    TeoVP        Teoriia Veroiatnostei i ee Primeneniia
    Teplo        Teploenergetika
    Tepsg        Teplofizicheskie svoistva gazov
    TepT         Teplofizika i Teplotekhnika
    TepVT        Teplofizika Vysokikh Temperatur
    TFizG        Teploobmen i Fizicheskaia Gazodinamika
    TNEK         Teplovye Napriazheniia Elementakh Konstruktsii
    LTerm        La Termotecnica
    TeMAE        Terrestrial Magnetism and Atmospheric Electricity (Journal of Geophysical Research)
    TeMag        Terrestrial Magnetism (Journal of Geophysical Research)
    Tesla        TESLA Electronics
    AcTC         Theoretica Chimica Acta
    ThApC        Theoretical and Applied Climatology
    ThAFM        Theoretical and Applied Fracture Mechanics
    TAM          Theoretical and Applied Mechanics
    ThCFD        Theoretical and Computational Fluid Dynamics
    TMP          Theoretical and Mathematical Physics
    ThAst        Theoretical Astrophysics
    TPAG         Theory and Practice of Applied Geophysics
    ThEng        Thermal Engineering
    TSE          Thermal Science and Engineering
    Th&Ae        Thermophysics and Aeromechanics
    TSF          Thin Solid Films
    TETB         Thyssen Edelstahl Technische Berichte
    TrTIM        Tiflis Izdatel Metsniereba Akademiia Nauk Gruzinskoi SSR Institut Geofiziki Trudy
    TrGru        Tiflis Izdatel Metsniereba Akademiia Nauk Gruzinskoi SSR Matematicheskii Institut Trudy
    IzTif        Tiflis Izdatel Tbilisskogo Universiteta
    TNKS         Tochnost i Nadezhnost Kiberneticheskikh Sistem
    TSRSG        Tohoku University Science Reports Series Geophysics
    TokAB        Tokyo Astronomical Bulletin
    TokRe        Tokyo Astronomical Observatory Reprints
    TUFER        Tokyo Denki University Faculty of Engineering Research Reports
    TAEMm        Tokyo Metropolitan College Aeronautical Engineering Memoirs
    TUFEJ        Tokyo University Faculty of Engineering Journal Series
    TUISR        Tokyo University Institute Industrial Science Report
    TUASB        Tokyo University Institute of Space and Aeronautical Science Bulletin
    TUASR        Tokyo University Institute of Space and Aeronautical Science Report
    TIOA         Tomsk Institut Optiki Atmosfery CO AN SSSR
    TApPh        Topics in Applied Physics
    TAASS        Topics in Astrophysics, Astrononmy, and Space Science
    TCPh         Topics in Current Physics
    TPhCh        Topics in Physical Chemistry
    ToASC        Torino Accademia delle Scienze Classe di Scienze Fisiche Matematiche e Naturali Atti
    TosRv        Toshiba Review
    TouCE        Toulouse Cepadues Editions
    TrAGU        Transactions, American Geophysical Union
    TAPS         Transactions of the American Philosophical Society
    TOYal        Transactions of the Astronomical Observatory of Yale University
    TCaPS        Transactions of the Cambridge Philosophical Society
    TISCI        Transactions of the Institute of Systems, Control and Information Engineers
    IAUTA        Transactions of the International Astronomical Union, Series A
    IAUTB        Transactions of the International Astronomical Union, Series B
    TIUCS        Transactions of the International Union for Cooperation in Solar Research
    TRACE        Transactions of the Japan Society of Refrigerating and Air Conditioning Engineers
    TJSAI        Transactions of the Japanese Society for Artificial Intelligence
    TATJ         Transactions of the Japanese Society for Artificial Intelligence, Aerospace Technology Japan
    TJSIE        Transactions of The Japanese Society of Irrigation, Drainage and Rural Engineering
    TLHSQ        Transactions of the Literary and Historical Society of Quebec
    TrOS         Transactions of the Optical Society
    TSICE        Transactions of the Society of Instrument and Control Engineers
    TrSpT        Transactions of Space Technology Japan
    TTSP         Transport Theory and Statistical Physics
    TvOC         Transvaal Observatory Circular
    TSSLW        Travaux de la Societe des Sciences et des Letters de Wroclaw
    TOMar        Travaux de l'Observatoire de Marseille
    TraGe        Travaux Geophysiques
    TrGeo        Treatise on Geochemistry
    TTP          Trends in Theoretical Physics
    TrLit        Trudy Akademiia Nauk Litovskoi
    TrSSR        Trudy Akademiia Nauk SSSR Fizicheskii Institut
    TrRig        Trudy Astrofiz. Lab. Riga
    TrAlm        Trudy Astrofizicheskogo Instituta Alma-Ata
    TrLen        Trudy Astronomicheskoj Observatorii Leningrad
    TrPul        Trudy Glavnoj Astronomicheskoj Observatorii v Pulkovo
    TrSht        Trudy Gosudarstvennogo Astronomicheskogo Instituta
    TrDus        Trudy Instituta Astrofiziki Dushanbe
    TrSta        Trudy Instituta Astrofiziki Stalinabad
    TrKaz        Trudy Kazanskaia Gorodkoj Astronomicheskoj Observatorii
    TrMMO        Trudy Moskovskoe Matematicheskoe Obshchestvo
    TrPet        Trudy Seminar imeni G Petrovskogo
    TrTas        Trudy Tashkentskoj Astronomicheskoj Observatorii
    TrTsA        TsAGI Trudy
    ZaTsA        TsAGI Uchenye Zapiski
    TrTsI        TsIAM Trudy
    TsHUJ        Tsing Hua University Journal
    TITas        Tsirkulyar Astronomicheskogo Instituta Akademiya Nauk Uzbekskoj SSR
    TsLvo        Tsirkulyar Astronomicheskoj Observatorii Lvov
    TsShe        Tsirkulyar Shemakhinskoj Astrofizicheskoj Observatorii
    TsSta        Tsirkulyar Stalinabadskoj Astronomicheskoj Observatorii
    TsTas        Tsirkulyar Tashkentskoj Astronomicheskoj Observatorii
    TsVse        Tsirkulyar Vses. astron.-geod. o-va
    TsPul        Tsirkulyary Glavnoj Astronomicheskoj Observatorii i Pulkove
    TUAID        Tuebingen Universitaet Astronomisches Institut Diplomarbeit
    TJJPT        Tuijin Jishu Journal of Propulsion Technology
    TurTe        Turbulentnye techeniia
    TJPh         Turkish Journal of Physics
    UGSJR        U S Geological Survey Journal Research
    UkJPO        Ukrainian Journal of Physical Optics
    UkFiZ        Ukrainskii Fizicheskii Zhurnal
    UkMaZ        Ukrainskii Matematicheskii Zhurnal
    Ultmi        Ultramicroscopy
    UltIm        Ultrasonic Imaging
    Ultra        Ultrasonics
    Umsch        Umschau
    USOC         Unified System Orbit Computation USOC
    UMIB         Unione Matematica Italiana Bollettino
    UNPSA        United Nations Programme on Space Applications
    UniCl        Universe Classroom
    UNAer        Universita di Napoli Aeritalia S
    UCAFR        Universitas Comeniana Acta Facultatis Rerum Naturalium Physica
    UMt1K        Universite de Montpellier
    UECBu        University Electro Communications Bulletin
    UnECR        University Electro Communications Reports
    MAUTx        University of Texas Monographs in Astronomy
    PAUTx        University of Texas Publications in Astronomy
    UppAn        Uppsala Astronomical Observatory Annals
    UppOR        Uppsala Astronomical Observatory Reports
    UrBar        Urania (Bracelona)
    Urani        Urania (Krakow)
    USNOC        U.S. Naval Observatory Circulars
    UsFiN        Uspekhi Fizicheskikh Nauk
    UMAM         Uspekhi Mekhaniki Advances Mechanics
    RpCCA        USSR Report Cybernetics Computers Automation Technology JPRS UCC
    RpESc        USSR Report Earth Sciences JPRS UES
    RpSpR        USSR Report Space
    RpBAM        USSR Report Space Biology Aerospace Medicine JPRS USB
    RpEEE        USSR Rept Electron Elec Eng JPRS UEE
    RpEn         USSR Rept Energy JPRS UEN
    RpEE         USSR Rept Eng Equipment JPRS UEQ
    RMTME        USSR Rept Machine Tools Metalworking Equipment JPRS UMM
    RpMSM        USSR Rept Mater Sci Met JPRS
    RpPhM        USSR Rept Phys Math JPRS UPM
    RpSBA        USSR Rept Space Biol Aerospace Med Sep
    RpTr         USSR Rept Transportation JPRS UTR
    UtMat        Utilitas Mathematica
    UtrOv        Utrechtse Sterrekundige Overdrukken
    Vacuu        Vacuum
    Vasio        Vasiona
    VatOP        Vatican Observatory Publications
    VDIF         VDI Forschungsheft
    VDIZ         VDI Z
    VDIZF        VDI Zeitschriften Fortschritt Berichte Reihe Stroemungstechnik
    VKAWA        Verhandelingen der Koninklijke Akademie van Wetenschappen te Amsterdam
    Verme        Vermessungstechnik
    VeWFS        Veroeffentlichung der Wilhelm Foerster Sterwarte
    ViHei        Veroeffentlichungen der Badischen Landes-Sternwarte zu Heidelberg
    VeHei        Veroeffentlichungen der Badischen Sternwarte zu Heidelberg
    VeGG         Veroeffentlichungen der Geod. Geophys
    VeKar        Veroeffentlichungen der Grossherzoglichen Sternwarte zu Karlsruhe
    VeBam        Veroeffentlichungen der Remeis-Sternwarte zu Bamberg
    VeBab        Veroeffentlichungen der Sternwarte Babelsberg
    VeMun        Veroeffentlichungen der Sternwarte Munchen
    VeSon        Veroeffentlichungen der Sternwarte Sonneberg
    VeKie        Veroeffentlichungen der Universitaets-Sternwarte Kiel
    VeKoe        Veroeffentlichungen der Universitaets-Sternwarte Koenigsberg Pr.
    VeBB         Veroeffentlichungen der Universitaetssternwarte zu Berlin-Babelsberg
    VeGoe        Veroeffentlichungen der Universitaets-Sternwarte zu Goettingen
    VeJen        Veroeffentlichungen der Universitaets-Sternwarte zu Jena
    VeLei        Veroeffentlichungen der Universitaetssternwarte zu Leipzig
    VeBoc        Veroeffentlichungen des Astronomischen Instituts der Ruhr-Universitaet Bochum
    VeARI        Veroeffentlichungen des Astronomischen Rechen-Instituts Heidelberg
    VeABD        Veroeffentlichungen des Astronomischen Rechen-Instituts zu Berlin-Dahlem
    VeBon        Veroeffentlichungen des Astronomisches Institute der Universitaet Bonn
    VeFra        Veroeffentlichungen des Astronomisches Institute der Universitaet Frankfurt
    VeBKI        Veroeffentlichungen des Bayerische Kommission Int. Erdmessung
    VeKAB        Veroeffentlichungen des Koeniglichen Astronomischen Rechen-Instituts zu Berlin
    VeZPE        Veroffentlichungen des Zentralinstituts Physik der Erde
    VeLdn        Verslag van den staat der Sterrewacht te Leiden
    VMKAN        Verslagen en Mededeelingen der Kon. Academie van Wetenschappen, Afd. Natuurkunde
    Vert         Vertica
    Vertf        Vertiflite
    Vesmi        Vesmir
    VeKha        Vestnik Khar'kov Universitet
    VKha         Vestnik Khar'kovskogo Universiteta
    VKie         Vestnik Kievskogo Universiteta Seriya Astronomii
    VeLGU        Vestnik LGU
    VeMos        Vestnik Moskovskogo Universiteta Seriya 3 Fizika Astronomiya
    VISBD        Vibration Inst Shock Vibration Digest
    VIAEA        Vienna International Atomic Energy Agency
    VAG          Vierteljahresschrift der Astronomischen Gesellschaft
    VMed         Vierteljahrschrift für Gerichtliche Medizin und Öffentliches Sanitätswesen
    VNG          Vierteljahrsschrift der Naturforschenden Gesellschaft in Zürich
    VilCo        Villanova University Observatory Contributions
    VilOB        Vilnius Astronomijos Observatorijos Biuletenis
    IzVil        Vilnius Izdatel Mokslas
    VJS          Virginia Journal of Science
    VisKi        Visnik Kiiv. Univ., Fiz.-Mat. Nauki, Astron
    ViGeo        Vissha Geodeziia
    VA           Vistas in Astronomy
    VTJ          Vitro Technical Journal
    yCat         VizieR Online Data Catalog
    yCatp        VizieR Online Data Catalog
    VICFD        VKI An Introduction to Computational Fluid Dynamics
    VIMT         VKI An Introduction to Modeling Turbulence
    VADVS        VKI Advanced Design of Ventilation Systems
    VAFC         VKI Axial Flow Compressors
    VBLT         VKI Boundary Layers in Turbomachines
    VCCPP        VKI Combined Cycles for Power Plants
    VCFDI        VKI Computational Fluid Dynamics for Industrial Flows
    VCGFV        VKI Computer Graphics Flow Visualization and Computational Fluid Dynamics
    VGTET        VKI Gas Turbine Engine Transient Behaviour
    VIHE         VKI Industrial Heat Exchangers
    VKILV        VKI Laser Velocimetry
    VKIMT        VKI Measurement and Techniques
    VMTA         VKI Measurement Techniques in Aerodynamics
    VMHT         VKI Methodology Hypersonic Testing
    VMATP        VKI Modeling and Applications of Transport Phenomena in Porous Media
    VADMT        VKI New Approaches in the Description and Modeling of Turbulence
    VNGG         VKI Numerical Grid Generation
    VNMFT        VKI Numerical Methods for Flows in Turbomachinery
    VPIDV        VKI Particle Image Displacement Velocimetry
    VKIRT        VKI Radial Turbines
    VKISP        VKI Spacecraft Propulsion
    VTSF         VKI Turbulent Shear Flows
    VVRD         VKI Vibration Rotor Dynamics
    VAC          Voies Aviation Civile Fall Winter
    VANTS        Voprosy Atomnoi Nauki i Tekhniki Seriia Fizika Plazmy i Problemy Upravliaemykh Termoiadernykh Reaktsii
    VopDP        Voprosy Dinamiki i Prochnosti
    VETT         Voprosy Elektroniki Tverdogo Tela
    VopGA        Voprosy Gidrodinamiki Atmosfery
    VopK         Voprosy Kibernetiki
    VMOIP        Voprosy Metrologicheskogo Obespecheniia Izmereniia Parametrov Tekhnologicheskikh Lazerov
    VoTAS        Voprosy Teorii Atomnykh Stolknovenii
    VopTP        Voprosy Teorii Plazmy
    VTSAU        Voprosy Teorii Sistem Avtomaticheskogo Upravleniia
    VossZ        Vossische Zeitung
    IzYak        Vsesoiuznaia Konferentsiia Kosmicheskim Lucham Yakutsk USSR Akademiia Nauk SSSR Izvestiia Seriia Fizicheskaia
    IzYer        Vsesoiuznaia Konferentsiia Kosmicheskim Lucham Yerevan Armenian SSR Aademiia Nauk SSSR Izvestiia Seriia Fizicheskaia
    VnPM         Vychislitel naia i Prikladnaia Matematika
    VnMP         Vychislitel nye Metody i Programmirovanie
    W&S          Waerme und Stoffuebertragung
    GMS          Washington DC American Geophysical Union Geophysical Monograph Series
    WRR          Water Resources Research
    WavEl        Wave Electronics
    WaMot        Wave Motion
    WRCM         Waves in Random and Complex Media
    WRM          Waves in Random Media
    Wear         Wear
    WearB        Wear B
    Wthr         Weather
    WtFor        Weather and Forecasting
    WeiEn        Weight Engineering
    WeldJ        Welding Journal
    Welt         Die Weltall
    Werk         Werkgroepnieuws
    JIMO         WGN, Journal of the International Meteor Organization
    WiEn         Wind Energy
    WiEng        Wind Engineering
    WisBT        Wissenschaftliche Berichte AEG Telefunken
    WisZe        Wissenschaftliche Zeitschrift
    WSAAA        Workshop Series of the Asociacion Argentina de Astronomia
    WCRp         World Climate Report
    WJCMP        World Journal of Condensed Matter Physics
    WJM          World Journal of Mechanics
    WJNSE        World Journal of Nano Science and Engineering
    WJNST        World Journal of Nuclear Science and Technology
    Wuli         Wuli
    xmm  pres    XMM-Newton Press Release
    xmm  prop    XMM-Newton Proposal
    YaFiz        Yadernaya Fizika
    YUFEM        Yamaguchi University Faculty of Engineering Memoirs
    YUTR         Yamaguchi University Technology Reports
    YamC         Yamamoto Circular
    ZaDN         Zagadnienia Drgan Nieliniowych
    ZaLab        Zavodskaia Laboratoriia
    ZaMM         Zeitschrift Angewandte Mathematik und Mechanik
    ZaMP         Zeitschrift Angewandte Mathematik und Physik
    ZeIE         Zeitschrift elektrische Informations und Energietechnik
    ZAGeo        Zeitschrift fur Angewandte Geographie
    ZAPhy        Zeitschrift fur Angewandte Physik
    ZA           Zeitschrift fur Astrophysik
    ZEVGA        Zeitschrift fur Eisenbahnwesen und Verkehrstechnik Glasers Annalen
    ZFlu         Zeitschrift fur Flugwissenschaften
    ZFlWe        Zeitschrift fur Flugwissenschaften und Weltraumforschung
    ZGm          Zeitschrift fur Geomorphologie
    ZGmS         Zeitschrift fur Geomorphologie Supplement
    ZGeo         Zeitschrift fur Geophysik
    ZGlGl        Zeitschrift fur Gletscherkunde und Glazialgeologie
    ZK           Zeitschrift fur Kristallographie
    ZKMP         Zeitschrift fur Kristallographie Mineralogie und Petrographie
    ZKS          Zeitschrift fur Kristallographie Supplements
    ZMetl        Zeitschrift fur Metallkunde
    ZeMet        Zeitschrift fur Meteorologie
    ZPhy         Zeitschrift fur Physik
    ZPhyA        Zeitschrift fur Physik A Hadrons and Nuclei
    ZPhyB        Zeitschrift fur Physik B Condensed Matter
    ZPhyC        Zeitschrift fur Physik C Particles and Fields
    ZPhyD        Zeitschrift fur Physik D Atoms Molecules Clusters
    ZPC          Zeitschrift fur Physikalische Chemie
    ZPCF         Zeitschrift fur Physikalische Chemie Frankfurt
    ZPCNF        Zeitschrift fur Physikalische Chemie Neue Folge
    ZPCW         Zeitschrift fur Physikalische Chemie Wiesbaden
    ZEAPC        Zeitschrift für Elektrochemie und Angewandte Physikalische Chemie
    ZMP          Zeitschrift für Mathematik und Physik
    ZNatA        Zeitschrift Naturforschung Teil A
    ZePAN        Zeitschrift Physik Atomic Nuclei
    ZVer         Zeitschrift Vermessungswes.
    ZWer         Zeitschrift Werkstofftechnik
    ZemVs        Zemlia i Vselennaia
    Zenit        Zenit
    MiTau        Zentralinstitut fuer Astrophysik Mitteilungen des Karl-Schwarzschild-Observatoriums Tautenburg
    MitVS        Zentralinstitut fuer Astrophysik Sternwarte Sonneberg Mitteilungen ueber Veraenderliche Sterne
    ZhPmR        ZhETF Pis ma Redaktsiiu
    ZhETF        Zhurnal Eksperimental noi i Teoreticheskoi Fiziki
    ZNPFK        Zhurnal Nauchnoi i Prikladnoi Fotografii i Kinematografii
    ZhPhy        Zhurnal Physik
    ZhPS         Zhurnal Prikladnoi Spektroskopii
    ZhTFi        Zhurnal Tekhnicheskoi Fiziki
    ZVMMF        Zhurnal Vychislitel noi Matematiki i Matematicheskoi Fiziki
    ZiZa         Ziran Zazhi
    Zprav        Zpravodaj VZLU
    ZvDeb        Zvaigsnota Debess ''')
b=a.split('\n')

b=[x for x in b if x!='']

b=[x.strip() for x in b]

b=[(x.split('        ')) for x in b]


c= [a for a in b if len(a) != 2]

d=[x for x in b if x not in c]


d=[[a, b.strip()] for a,b in d]

for i in range(len(d[:])):
    if len(d[i][0])==5:
        continue
    elif len(d[i][0])==4:
        d[i][0]= d[i][0]+'.'
    elif len(d[i][0])==3:
        d[i][0]= d[i][0]+'..'
    elif len(d[i][0])==2:
        d[i][0]= d[i][0]+'..'
    elif len(d[i][0])==1:
        d[i][0]= d[i][0]+'....'



journaldict= dict(d)

bibstemdict= [(y,x) for (x,y) in journaldict.items()]

bibstemdict=dict(bibstemdict)







