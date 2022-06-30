#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys

file = """ΑΑ Achaia prefecture - Patras
ΑΒ Kavala prefecture - Kavala {motorcycles}
ΑΕ Lasithi prefecture - Agios Nikolaos (future use)
ΑΖ Achaia prefecture - Patras
ΑΗ Xanthi prefecture - Xanthi (ΑΗΗ is omitted)
ΑΙ Aitoloakarnania prefecture - Agrinio area (ΑΙΙ is omitted)
ΑΚ Laconia prefecture - Sparti
ΑΜ Phokida prefecture - Amfissa
ΑΜ [Ο, Ρ, Τ, Υ, Χ] (red letters) tax free cars
ΑΝ Lasithi prefecture - Agios Nikolaos
ΑΟ Achaia prefecture - Patras {motorcycles}
AO also used in Mount Athos in style of AO-NNN-NN.
ΑΡ Argolis (Argolida) prefecture - Nafplio
ΑΤ Arta prefecture - Arta
AY Achaia prefecture - Patras {motorcycles}
ΑΧ Achaia prefecture - Patras
ΒΑ Magnesia prefecture - Volos (future use)
ΒΒ Magnesia prefecture - Volos {motorcycles}
ΒΕ Piraeus prefecture {motorcycles}
BZ Piraeus prefecture {motorcycles}
ΒΗ Piraeus prefecture {motorcycles}
ΒΙ Boeotia (Viotia) prefecture - Livadeia
ΒΚ East Attica prefecture - Pallini
ΒΜ East Attica prefecture - Pallini (future use)
ΒΝ West Attica prefecture - Elefsina (future use)
ΒΟ Magnesia prefecture - Volos (ΒΟΡ plates were also issued for cars in Pella Prefecture due to lack of ΕΕΚ plates at that time)
ΒΡ West Attica prefecture - Elefsina (future use)
ΒΤ Magnesia prefecture - Volos (future use)
ΒΥ Boeotia (Viotia) prefecture - Livadeia (future use)
ΒΧ Piraeus prefecture {motorcycles}
ΕΑ Dodecanese prefecture - Kos island {motorcycles}
ΕΒ Evros prefecture - Alexandroupoli (ΕΒΒ is omitted)
ΕΕ Pella Prefecture - Edessa (ΕΕΕ is omitted)
ΕΖ Cyclades prefecture - Ermoupoli {motorcycles}
ΕΗ Euboea (Evia) prefecture - Chalkida {motorcycles}
EI Euboea (Evia) prefecture - Chalkida {motorcycles}
EK Trucks
ΕΚ [Α, Β, Ε] (introduced maybe in 2003/2004, yellow colored) trucks and other vehicles used for national transport of goods
ΕΜ Cyclades prefecture - Ermoupoli
ΕΡ Serres prefecture - Serres
ΕΤ Corfu (Kerkyra) prefecture - Corfu {motorcycles}
ΕΥ Lefkada prefecture - Lefkada (ΕΥΑ plates were also issued in Rodos Island due to lack of ΡΟΝ plates at that time)
ΕΥ [Υ] tax free cars of offshore companies
ΕΧ Kilkis prefecture - Kilkis (future use)
ΖΑ Zakynthos prefecture - Zakynthos
ΖΒ Zakynthos prefecture - Zakynthos (future use)
ΖΕ Thessaloniki prefecture (future use)
ΖΖ Athens prefecture
ΖΗ Athens prefecture
ΖΙ Thessaloniki prefecture (future use)
ΖΚ Athens prefecture
ΖΜ Athens prefecture
ΖΝ Piraeus prefecture
ΖΟ Thessaloniki prefecture (future use)
ΖΡ Piraeus prefecture {motorcycles}
ΖΤ West Attica prefecture - Elefsina {motorcycles}
ΖΥ East Attica prefecture - Pallini
ΖΧ East Attica prefecture - Pallini
ΗΑ Ilia prefecture - Pyrgos
ΗΒ Athens prefecture {motorcycles}
ΗΕ Ilia prefecture - Pyrgos {motorcycles}
ΗΖ Heraklion prefecture - Heraklion
ΗΗ Heraklion prefecture - Heraklion {motorcycles}
ΗΙ Heraklion prefecture - Heraklion {motorcycles}
ΗΚ Heraklion prefecture - Heraklion (ΗΚΗ and ΗΚΖ plates were also issued in nearby Chania Prefecture due to lack of ΧΝΜ plates at that time)
ΗΜ Imathia prefecture - Veria
ΗΝ Thesprotia prefecture - Igoumenitsa
ΗΟ Xanthi prefecture - Xanthi {motorcycles}
ΗΡ Heraklion prefecture - Heraklion
ΗΤ Xanthi prefecture - Xanthi (future use)
ΗΥ Phthiotis (Fthiotida) prefecture - Lamia (future use)
ΗΧ Imathia prefecture - Veria (future use)
ΙΑ Trucks
ΙΑ [Α, Β, Ε] (yellow colored) trucks used for international transport
ΙΒ Athens prefecture
ΙΕ Athens prefecture
ΙΖ Athens prefecture
ΙΗ Athens prefecture (IHA plates were also issued for cars in Euboea Prefecture due to lack of XAI plates at that time)
ΙΙ Ioannina prefecture - Ioannina (future use)
ΙΚ Athens prefecture
ΙΜ Athens prefecture
ΙΝ Ioannina prefecture - Ioannina
ΙΟ Athens prefecture
ΙΡ Athens prefecture {not solely for motorcycles as previously stated}
ΙΤ Athens prefecture
ΙΥ Athens prefecture
ΙΧ Serres prefecture
ΚΑ Karditsa prefecture - Karditsa (ΚΑΑ is omitted)
ΚΒ Kavala prefecture - Kavala (ΚΒΒ is omitted)
ΚΕ Kefalonia and Ithaca prefecture - Argostoli (KEE is omitted)
ΚΖ Kozani prefecture - Kozani (ΚΖΖ is omitted)
ΚΗ Evrytania prefecture - Karpenisi
ΚΗ [Ι, Ο, Υ] (orange colored) state cars
ΚΙ Kilkis prefecture - Kilkis
ΚΚ Rhodope prefecture - Komotini {motorcycles}
ΚΜ Messinia prefecture - Kalamata
ΚΝ Pieria prefecture - Katerini (ΚΝΖ is omitted)
ΚΟ Rhodope (Rodopi) prefecture - Komotini (exception: ΚΟΗ and ΚΟΚ --> Thessaloniki prefecture, ΚΟΡ --> Heraklio prefecture {motorcycles})
ΚΡ Corinthia prefecture - Corinth (Korinthos)
ΚΤ Kastoria prefecture - Kastoria
ΚΤ [Ι, Ο, Τ] (red letters) tax free cars
ΚΤ [Υ] (orange colored) state cars
ΚΥ Corfu (Kerkyra) prefecture - Corfu
ΚΧ Dodecanese prefecture - Kos island (ΚΧΑ plates were also issued for cars in Rodos Island due to lack of ΡΟΖ plates at that time)
ΚΧ [O, Υ, X] (red letters) tax free cars
ΜΑ Chalkidiki prefecture - Polygyros (future use)
ΜΒ Samos prefecture - Samos (future use)
ΜΕ Aitoloakarnania prefecture - Messolongi
ΜΖ Messinia prefecture - Kalamata {motorcycles}
ΜΗ Lesvos prefecture - Myrina (Limnos island)
MH [Ι, Ο, Υ] (red letters) tax free cars
ΜΙ Phthiotis (Fthiotida) prefecture - Lamia
ΜΚ Karditsa prefecture - Karditsa (future use)
ΜΜ Pella Prefecture - Edessa (future use)
ΜΝ Kozani prefecture - Kozani
ΜΟ Samos prefecture - Samos (ΜΟΚ, ΜΟΜ and ΜΟΡ plates for motorcycles were also issued in Rodos Island due to lack of ΡΚΜ plates at that time)
ΜΟ [Ι, Ο, Υ] (red letters) {tax free cars}
ΜΡ Laconia prefecture - Sparti (future use)
ΜΤ Lesbos prefecture - Mytilini {motorcycles}
ΜΥ Lesbos (Lesvos) prefecture - Mytilini (ΜΥΖ plates were also issued for cars in Rodos Island due to lack of ΡΟΜ plates at that time)
ΜΧ Evros prefecture - Alexandroupoli (future use)
ΝΑ Thessaloniki prefecture - Thessaloniki
ΝΒ Thessaloniki prefecture - Thessaloniki
ΝΕ Thessaloniki prefecture - Thessaloniki
ΝΖ Thessaloniki prefecture - Thessaloniki
ΝΗ Thessaloniki prefecture - Thessaloniki
ΝΙ Thessaloniki prefecture - Thessaloniki
ΝΚ Thessaloniki prefecture - Thessaloniki
ΝΜ Thessaloniki prefecture - Thessaloniki {motorcycles}
ΝΝ Thessaloniki prefecture - Thessaloniki {motorcycles}
ΝΟ Thessaloniki prefecture - Thessaloniki {motorcycles}
ΝΡ Thessaloniki prefecture {motorcycles}
ΝΤ Thessaloniki prefecture (future use)
ΝΥ Thessaloniki prefecture (future use)
NX Thessaloniki prefecture (future use)
ΝΧ Trucks
ΝΧ [Α, Υ] (yellow colored) {trucks for transport of goods in a prefecture}
ΟΑ Athens {motorcycles}
ΟΒ Athens {motorcycles}
ΟΕ Athens {motorcycles}
ΟΖ Athens (future use)
ΟΗ Athens {motorcycles}
ΟΙ Athens {motorcycles}
ΟΚ Athens {motorcycles}
ΟΜ Athens {motorcycles}
ΟΝ Athens {motorcycles}
ΟΟ Athens {motorcycles}
ΟΡ Evros prefecture - Orestiada area
ΟΤ Athens (future use)
ΟΥ Athens {motorcycles}
ΟΧ Athens (future use)
ΡΑ Florina prefecture - Florina (ΡΑΑ is omitted)
ΡΑ [Ι, Ο, Υ] (red letters) tax free cars
ΡΒ Corinthia prefecture - Corinth (future use)
ΡΕ Rethymno prefecture - Rethymno (ΡΕΕ appears not to have been omitted as previously stated)
ΡΖ Preveza prefecture - Preveza (ΡΖΒ is omitted)
ΡΗ Rethymno prefecture - Rethymno {motorcycles}
ΡΙ Larissa prefecture - Larissa
ΡΚ Dodecanese prefecture - Rodos (Rhodes)
ΡΜ Drama prefecture - Drama (ΡΜΖ is omitted)
ΡΝ Grevena prefecture - Grevena
ΡΝ [Ι, Μ, Ν, Ο, Ρ] (red letters) trucks
ΡΟ Dodecanese prefecture - Rhodes (Rodos)
ΡΡ Larissa prefecture - Larissa
ΡΤ Larissa prefecture - Larissa (future use)
ΡΥ Dodecanese prefecture - Rodos (Rhodes) {motorcycles}
ΡΧ Dodecanese prefecture - Rodos (Rhodes) (future use)
ΤΑ Taxis
ΤΑ [Α, Β, Ε, Ζ, Η] (marked in yellow) taxis
ΤΒ Corfu (Kerkyra) prefecture - Corfu {motorcycles}
ΤΕ Corfu (Kerkyra) prefecture - Corfu (future use)
ΤΖ Piraeus prefecture {motorcycles}
ΤΗ Aitoloakarnania prefecture - Agrinio area (future use)
ΤΙ Pieria prefecture - Katerini (future use)
ΤΚ Trikala prefecture - Trikala
ΤΜ Argolis (Argolida) prefecture - Nafplio (future use)
ΤΝ Trikala prefecture - Trikala (future use)
ΤΟ Drama prefecture - Drama (future use)
ΤΡ Arcadia prefecture - Tripoli
ΤΤ Rhodope prefecture (future use)
ΤΥ Chania prefecture - Chania {motorcycles}
ΤΧ Preveza prefecture - Preveza (future use)
ΥΑ Athens prefecture
ΥΒ Athens prefecture
ΥΕ Athens prefecture
ΥΖ Athens prefecture
ΥΗ Athens prefecture (YHA plates were also issued for cars in Euboea Prefecture due to lack of XAN plates at that time)
ΥΙ Piraeus prefecture
ΥΚ Piraeus prefecture
ΥΜ Piraeus prefecture
ΥΝ Piraeus prefecture
ΥΟ West Attica prefecture - Elefsina
ΥΡ West Attica prefecture - Elefsina
ΥΤ West Attica prefecture - Elefsina
ΥΥ East Attica prefecture - Pallini
ΥΧ East Attica prefecture - Pallini
ΧΑ Euboea (Evia) prefecture - Chalkida
ΧΒ Chania prefecture - Chania {motorcycles}
ΧΕ Athens prefecture {now used for both motorcycles and cars}
ΧΖ Athens prefecture {motorcycles}
ΧΗ Athens prefecture {motorcycles}
ΧΙ Chios prefecture - Chios
ΧΚ Chalkidiki prefecture - Polygyros
ΧΜ Athens prefecture (future use)
ΧΝ Chania prefecture - Chania (ΧΝΟ were skipped for cars, but were used for motorcycles)
ΧΟ Chios prefecture - Chios {motorcycles}
ΧΡ Athens prefecture {motorcycles}
ΧΤ Athens prefecture {motorcycles}
ΧΥ Athens prefecture {motorcycles}
ΧΧ Athens prefecture {motorcycles}
"""


def get_license_plate_district(license_plate):
    print(f'{license_plate}:')
    area_part = license_plate[:2]
    for f in file.split('\n'):
        if f.split():
            if area_part == f.split()[0]:
                print(f)


get_license_plate_district(input('Εισάγετε μια πινακίδα αυτοκινήτου: '))
input()
