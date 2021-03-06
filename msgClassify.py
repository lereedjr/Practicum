import json
import re


# convenience function: check if any topic term is contained within a sentence
def contains(a_list, a_sentence):
    for item in a_list:
        # handle patterned case (prefaced by asterisk)
        # eg. "*dd:ddam" will catch the pattern "10:30am"
        if item[0] == '*':
            if re.search(item.replace('*', '').replace('d', '\d'), a_sentence):
                return (item)
        else:
            if item.lower() in a_sentence.lower():
                return (item)


# convenience function: split text into one or more sentences
def split(text, rows_split_delim=['.', '!', '?']):
    # sentences after the split
    rows_split = []
    # pointer to position within text
    pointer = 0

    # don't try to split messages with links
    if 'http' in text.lower():
        return [text]

    # loop through each character in the message text
    for char in text:
        # if character is a sentence delimeter
        if char in rows_split_delim:
            # split out the text from the previous pointer to this delimeter
            sentence = text[pointer:text.index(char, pointer) + 1]
            # remove extra spaces
            sentence = sentence.lstrip().strip()
            rows_split.append(sentence)
            # update the pointer
            pointer = text.index(char, pointer) + 1

    # finish by splitting out the remaining text
    # from the previous pointer to this delimeter
    # this handles the case of text with no split sentences
    sentence = text[pointer:].lstrip().strip()
    rows_split.append(sentence)

    return rows_split


# Classify class definition
class Classifier(object):
    """A classification object, for topics defined in a json definiton

    Attributes:
        topics_file: a json structure containing words/patterns for a list of topics
    """

    def __init__(self, topics_file):
        """Return a Classify object given a topics definition file

        hotels.json
{
  "99-Inn Management Co. Ltd.": [
    "99-inn",
    "99 inn"
  ],
  "AccorHotels": [
    "Sofitel",
    "Legend",
    "Fairmont",
    "Raffles",
    "Pullman",
    "Swissotel",
    "MGallery",
    "Sebel",
    "Adagio",
    "Premium",
    "Grand Mercure",
    "Novotel",
    "Suite",
    "Adagio",
    "Mama",
    "Shelter",
    "Mercure",
    "ibis Budget",
    "Formule 1",
    "ibis",
    "Styles",
    "Adagio",
    "Access",
    "Coralia"
  ],
  "Aman Resorts": [
    "Aman"
  ],
  "APA Group": [
    "APA"
  ],
  "The Ascott Limited": [
    "Crest Collection",
    "Ascott",
    "Ascott Residence",
    "Citadine",
    "Citadines",
    "Citadines Apart hotel",
    "Somerset",
    "Somerset Serviced",
    "Quest",
    "Quest Apartment",
    "lyf"
  ],
  "Banyan Tree Holdings": [
    "Banyan",
    "Angsana",
    "Cassia",
    "Dhawa"
  ],
  "Barriere": [
    "Fouquet",
    "Le Fouquet's Paris",
    "Majestic",
    "Cannes",
    "Le Majestic Cannes",
    "Neiges",
    "Neiges",
    "Courchevel",
    "Les Neiges Courchevel",
    "Le Normandy Deauville"
  ],
  "Best Western Hotels": [
    "BW",
    "BW Signature Collection",
    "Best Western",
    "SureStay",
    "SureStay Plus",
    "SureStay Collection"
  ],
  "The Dedica Anthology Hotels": [
    "Palazzo Naiadi",
    "Palazzo Naiadi Rome",
    "Palazzo Matteotti",
    "Matteotti",
    "Palazzo Matteotti Milan",
    "Dei Dogi",
    "Grand Hotel Dei Dogi Venice",
    "New York Palace",
    "New York Palace Budapest",
    "Carlo",
    "Carlo IV",
    "Carlo IV Prague"
  ],
  "BTG Homeinn hotel group": [
    "Yitel",
    "Homeinn",
    "Home Inn",
    "Home Inns",
    "Motel 168",
    "Fairyland"
  ],
  "Radisson Hotel Group": [
    "Quorvus",
    "Quorvus Collection",
    "Radisson",
    "Blu",
    "Radisson Blu",
    "Park Plaza",
    "Red",
    "Park Inn",
    "Country Inn",
    "Country Inns & Suites"
  ],
  "China Lodging Group, Limited (Huazhu Hotels Group)": [
    "JI",
    "Starway",
    "Joya",
    "Manxin",
    "HanTing",
    "HanTing Plus",
    "Orange Selected",
    "Hi Inn",
    "Elan Hotel",
    "Orange Hotel"
  ],
  "Choice Hotels": [
    "Ascend",
    "Ascend Collection",
    "Cambria",
    "Cambria Suites",
    "Clarion",
    "Comfort Suites",
    "Clarion Inn",
    "Mainstay",
    "Mainstay Suites",
    "Quality Inn",
    "Comfort Inn",
    "Sleep Inn",
    "EconoLodge",
    "Econo Lodge",
    "Rodeway Inn",
    "Suburban Extended Stay"
  ],
  "Coast Hotels": [
    "Coast"
  ],
  "Dorchester Collection": [
    "Dorchester",
    "Meurice",
    "Le Meurice",
    "Hotel Plaza Athenee",
    "Eden",
    "Principe di Savoia",
    "Beverly Hills Hotel",
    "Hotel Bel Air",
    "45 Park Lane",
    "Coworth Park"
  ],
  "Dossen International Group": [],
  "Drury Hotels": [
    "Drury",
    "Drury Plaza",
    "Drury Suites",
    "Drury Inn",
    "Drury Inn and Suites",
    "Pear Tree",
    "Pear Tree Inn"
  ],
  "Dusit Thani Group": [
    "Devarana",
    "Dusit Devarana",
    "Thani",
    "Dusit Thani",
    "dusitD2",
    "Dusit",
    "Princess"
  ],
  "Elegant Hotels Group": [
    "Colony Club",
    "Crystal Cove",
    "Tamarind",
    "The House",
    "Turtle Beach",
    "Waves",
    "Landings",
    "Hodges",
    "Hodges Bay"
  ],
  "Extended Stay America, Inc.": [
    "Extended Stay America"
  ],
  "FIH Regent Group": [
    "Regent",
    "Silk Place",
    "Just Sleep"
  ],
  "First Hotels": [
    "First Hotel"
  ],
  "Four Seasons Hotels and Resorts": [
    "Four Seasons"
  ],
  "G6 Hospitality LLC.": [
    "Motel 6",
    "Studio 6",
    "Estudio 6",
    "Hotel 6"
  ],
  "GreenTree Inns Hotel Management Group, Inc.": [
    "GreenTree",
    "GreenTree Inn",
    "Vatica",
    "GTA",
    "GreenTree Eastern",
    "Shell"
  ],
  "Hilton Worldwide": [
    "Waldorf Astoria",
    "Conrad",
    "Hilton",
    "DoubleTree",
    "Canopy",
    "Curio",
    "Curio Collection",
    "Embassy",
    "Embassy Suites",
    "Garden Inn",
    "Homewood",
    "Homewood Suites",
    "Home2 Suites",
    "Home 2Suites",
    "Home 2 Suites",
    "Home2Suites",
    "Tru",
    "Hampton"
  ],
  "HNA Hospitality Group": [
    "Tang",
    "Tang Grand Place",
    "Tangla",
    "Tang Hotel",
    "HNA",
    "HNA Business",
    "Garden Lane",
    "HNA Express",
    "HNA Grand"
  ],
  "Hongkong and Shanghai Hotels": [
    "Peninsula Hotels"
  ],
  "Hoshino Resorts": [
    "The Peninsula Hotels"
  ],
  "Hyatt Hotels Corporation": [
    "Hyatt",
    "Park Hyatt",
    "Grand Hyatt",
    "Andaz",
    "Regency",
    "Centric",
    "Hyatt Place",
    "Hyatt House"
  ],
  "InterContinental Hotels Group (IHG)": [
    "InterContinental",
    "Crown",
    "Crowne",
    "Crowne Plaza",
    "Kimpton",
    "Indigo",
    "EVEN",
    "Staybridge",
    "Staybridge Suites",
    "Holiday Inn Select",
    "HUALUXE",
    "Holiday Inn",
    "Holiday Inn Express",
    "Candelwood",
    "Candlewood",
    "Candlewood Suites",
    "Avid"
  ],
  "Interstate Hotel & Resorts": [],
  "InTown Suites": [
    "InTown Suites",
    "InTown"
  ],
  "Jin Jiang International": [
    "Jinjiang",
    "Jinjiang Inns",
    "Rock Garden",
    "Jinjiang",
    "Kunlun",
    "Jinjiang Metropolis",
    "Campanile",
    "Tulip Golden Tulip",
    "7 days",
    "Li Feng",
    "Zhe",
    "Brown",
    "Vienna"
  ],
  "Jumeirah": [
    "Jumeirah"
  ],
  "Kempinski": [
    "Kempinski"
  ],
  "Langham Hospitality Group": [
    "Langham",
    "Langham Place",
    "Cordis",
    "Eaton",
    "Chelsea"
  ],
  "Loews Hotels": [
    "Loews"
  ],
  "Lotte Hotels & Resorts": [
    "Signiel",
    "Lotte",
    "L7",
    "Lotte City",
    "Lotte Resorts"
  ],
  "Magnuson Hotels": [
    "Magnuson Grand",
    "Magnuson",
    "M Star",
    "M-Star"
  ],
  "Mandarin Oriental Hotel Group": [
    "Mandarin Oriental"
  ],
  "Marriott International": [   
    "Ritz",
    "Ritz-Carlton",
    "Bulgari",
    "Edition",
    "Marriott",
    "JW Marriott",
    "St. Regis",
    "Luxury Collection",
    "Renaissance",
    "Autograph",
    "Autograph Collection",
    "Delta",
    "Marriott Executive Apartment",
    "Gaylord",    
    "W Hotels",
    "Design",
    "Westin",
    "Le Meridien",
    "Sheraton",
    "Tribute Portfolio",
    "AC",
    "Fairfield Inn",
    "Courtyard",
    "SpringHill",
    "SpringHill Suites",
    "Residence Inn",
    "Four Points by Sheraton",
    "Aloft",
    "Element",
    "MOXY",
    "Protea",
    "TownePlace",
    "TownePlace Suites"
  ],
  "Melia Hotels International, S.A.": [
    "Gran Melia",
    "ME",
    "Paradisus",
    "Melia",
    "Innside",
    "Tryp",
    "Sol"
  ],
  "Millennium & Copthorne Hotels": [
    "Grand Millenium",
    "Grand Millenium Hotels",
    "Millennium",
    "Grand Copthrone",
    "Copthorne",
    "M Hotels",
    "Kingsgate"
  ],
  "MGM Resorts International": [
    "VDARA",
    "ARIA",
    "MGM",
    "PARK MGM",
    "NEW YORK-NEW YORK",
    "EXCALIBUR",
    "LUXOR",
    "DELANO",
    "MANDALAY BAY",
    "CIRCUS CIRCUS",
    "MIRAGE",
    "BELLAGIO",
    "SIGNATURE",
    "MGM GRAND"
  ],
  "Minor Hotels": [
    "Anantara",
    "Per Aquum",
    "Avani",
    "Tivoli",
    "Oaks"
  ],
  "NH Hotel Group": [
    "NHow",
    "NH",
    "NH Collection",
    "Hesperia"
  ],
  "The Oberoi Group": [
    "Oberoi",
    "Trident"
  ],
  "Okura Nikko Hotel Management": [
    "Okura",
    "Nikko",
    "JAL",
    "JAL City"
  ],
  "Omni Hotels & Resorts": [
    "Omni"
  ],
  "Pan Pacific Hotels and Resorts": [
    "Pan Pacific",
    "PARKROYAL"
  ],
  "Prince Hotels": [
    "The Prince",
    "Grand Prince",
    "Prince"
  ],
  "Red Lion Hotels Corporation": [
    "Hotel RL",
    "Red Lion",
    "Settle Inn",
    "Signature Inn",
    "Guest House",
    "Americas Best Value",
    "Canadas Best Value",
    "Country Hearth"
  ],
  "Red Roof Inn": [
    "Red Roof",
    "The Red Collection"
  ],
  "RIU Hotels & Resorts": [
    "RIU",
    "Robinson Club",
    "Grecotel",
    "Grupotel",
    "Iberotel",
    "Magic Life",
    "Sol y Mar",
    "PURAVIDA",
    "Sensimar",
    "Viverde aqi",
    "Dorfhotel",
    "Gran Resort",
    "Atlantica",
    "Rocco Forte Hotels",
    "Britannia",
    "Innkeepers Lodge",
    "Metro Inns",
    "Premier Inn",
    "YOTEL",
    "Mid-market",
    "Mid market",
    "Apex",
    "Crerar",
    "Four-Pillars",
    "Jurys Inn",
    "McMillan",
    "Peel",
    "Principal",
    "Hayley",
    "Hayley Quality Hotels",
    "Thistle Hotels",
    "Wetherspoons",
    "Belmond",
    "Champneys",
    "Clermont",
    "Corus",
    "Club Quarters",
    "Dorchester Collection",
    "Epoque",
    "Exclusive Hotels",
    "Hand Picked",
    "du Vin",
    "Hotel du Vin",
    "Malmaison",
    "Morgans",
    "Maybourne",
    "Ralph Trustees",
    "Rocco Forte",
    "Crest",
    "Jarvis",
    "The Real Hotels",
    "Stakis",
    "Swallow",
    "Trusthouse Forte"
  ],
  "Rosewood Hotel Group": [
    "Rosewood",
    "New World Hotels",
    "Pentahotels"
  ],
  "Scandic Hotels": [
    "Scandic"
  ],
  "Shangri-La Hotels and Resorts": [
    "ShangriLa",
    "Shangri La",
    "Shangri-La",
    "Kerry",
    "Traders",
    "Jen"
  ],
  "Shilo Inns": [
    "Shilo",
    "Shilo Inns"
  ],
  "Sunmei Group": [
    "LANO",
    "Midi",
    "Thank",
    "Thank Inn",
    "Feronia",
    "Lippo"
  ],
  "Taj Hotels Resorts and Palaces": [
    "Taj",
    "Exotica",
    "Taj Exotica",
    "Vivanta",
    "Vivanta by Taj",
    "Gateway",
    "The Gateway Hotels",
    "Ginger"
  ],
  "Tokyu Hotels": [
    "Tokyu",
    "Excel",
    "REI"
  ],
  "Toyoko Inn": [
    "Toyoko",
    "Toyoko Inn"
  ],
  "Travelodge": [
    "Travel",
    "Lodge",
    "Travelodge"
  ],
  "Treebo": [
    "Treebo"
  ],
  "Walt Disney Parks and Resorts": [
    "Aulani",
    "Disneyland Resort",
    "Disney World Resort",
    "Shanghai Disney Resort",
    "Tokyo Disney Resort",
    "Disney Resort"
  ],
  "Warwick Hotels and Resorts": [
    "Warwick",
    "Royal Windsor",
    "Westminster",
    "Hotel Westminster",
    "Naviti"
  ],
  "Wyndham Worldwide": [
    "Dolce",
    "Dolce Hotels",
    "Wyndham Grand",
    "Viva Wyndham",
    "Wyndham",
    "TRYP",
    "TRYP by Wyndham",
    "Esplendor",
    "Esplendor Boutique Hotels",
    "Dazzler",
    "Wyndham Garden",
    "Hawthorn Suites",
    "Wingate",
    "Ramada",
    "Trademark Hotel",
    "Howard Johnson",
    "Baymont",
    "AmericInn",
    "La Quinta",
    "Days Inn",
    "Super 8",
    "Knights Inn",
    "Microtel",
    "Microtel by Wyndham"
  ],
  "Whitbread plc": [
    "Premier Inn",
    "hub"
  ]
}
        c = Classifier('../hotels.json')

        """
        # load topics and their words
        try:
            self.topics = json.load(open(topics_file))
        except:
            print ('error opening file', topics_file)

    def classify(self, text):
        """Returns a json structure with classification for sentences within the text

        c.classify("The nurse will be there. We'll be there around 10:30")
        {'medpro': ['The nurse will be there.'], 'scheduling': ["We'll be there around 10:30"]}

        """

        topics_data = {}
        # split out sentences from the text
        sentences = split(text)

        for sentence in sentences:
            # loop through the topics
            for key in self.topics.keys():
                # if the sentence contains any of the words for this topic, add to results
                if contains(self.topics[key], sentence):
                    if key not in topics_data:
                        topics_data[key] = [sentence]
                    else:
                        topics_data[key].append(sentence)

        return topics_data