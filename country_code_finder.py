import pprint
s = []
# load the file
def loadthefile(filename):
	try:
		with open(filename) as f:
			for listy in f:
				s.append(listy.strip())
		return s
	except IOError as err:
		print("file not found")
		
m = {}
a = {}	

a = {'a': 'Afghanistan 93,Albania 355,Algeria 213,American Samoa 1684,Andorra 376,Angola 244,Anguilla 1264,Antarctica 672,Antigua and Barbuda 1268,Argentina 54,Armenia 374,Aruba 297,Ascension Island 247,Australia 61,Austria 43,Azerbaijan 994,', 'b': ',Bahamas 1242,Bahrain 973,Bangladesh 880,Barbados 1246,Belarus 375,Belgium 32,Belize 501,Benin 229,Bermuda 1441,Bhutan 975,Bolivia 591,Bosnia and Herzegovina 387,Botswana 267,Brazil 55,British Virgin Islands 1284,Brunei 673,Bulgaria 359,BurkinaFaso 226,Burma(Myanmar) 95,Burundi 257,', 'c': ',Cambodia 855,Cameroon 237,Canada 1,Cape Verde 238,Cayman Islands 1345,Central African Republic 236,Chad 235,Chile 56,China 86,ChristmasIsland 61,Cocos(Keeling)Islands 61,Colombia 57,Comoros 269,Congo 242,CookIslands 682,CostaRica 506,Croatia 385,Cuba 53,Cyprus 357,CzechRepublic 420,', 'd': ',Democratic Republic of the Congo 243,Denmark 45,Diego Garcia 246,Djibouti 253,Dominica 1767,Dominican Republic 1809,', 'e': ',Ecuador 593,Egypt 20,ElSalvador 503,Equatorial Guinea 240,Eritrea 291,Estonia 372,Ethiopia 251,', 'f': ',Falkl and Islands 500,Faroe Islands 298,Fiji 679,Finland 358,France 33,French Guiana 594,French Polynesia 689,', 'g': ',Gabon 241,Gambia 220,Georgia 995,Germany 49,Ghana 233,Gibraltar 350,Greece 30,Greenland 299,Grenada 1473,Guadeloupe 590,Guam 1671,Guatemala 502,Guinea 224,Guinea-Bissau 245,Guyana 592,', 'h': ',Haiti 509,HolySee (VaticanCity) 39,Honduras 504,HongKong 852,Hungary 36,', 'i': ",Iceland 354,India 91,Indonesia 62,Iran 98,Iraq 964,Ireland 353,IsleofMan 44,Israel 972,Italy 39,IvoryCoast (Côted'Ivoire) 225,", 'j': ',Jamaica 1876,Japan 81,Jersey 44,Jordan 962,', 'k': ',Kazakhstan 7,Kenya 254,Kiribati 686,Kuwait 965,Kyrgyzstan 996,', 'l': ',Laos 856,Latvia 371,Lebanon 961,Lesotho 266,Liberia 231,Libya 218,Liechtenstein 423,Lithuania 370,Luxembourg 352,', 'm': ',Macau 853,Macedonia 389,Madagascar 261,Malawi 265,Malaysia 60,Maldives 960,Mali 223,Malta 356,MarshallIslands 692,Martinique 596,Mauritania 222,Mauritius 230,Mayotte 262,Mexico 52,Micronesia 691,Moldova 373,Monaco 377,Mongolia 976,Montenegro 382,Montserrat 1664,Morocco 212,Mozambique 258,', 'n': ',Namibia 264,Nauru 674,Nepal 977,Netherlands 31,Netherlands Antilles 599,NewCaledonia 687,NewZealand 64,Nicaragua 505,Niger 227,Nigeria 234,Niue 683,NorfolkIsland 672,NorthKorea 850,Northern Mariana Islands 1670,Norway 47,', 'o': ',Oman 968,', 'p': ',Pakistan 92,Palau 680,Palestine 970,Panama 507,PapuaNewGuinea 675,Paraguay 595,Peru 51,Philippines 63,Pitcairn Islands 870,Poland 48,Portugal 351,PuertoRico 1787,', 'q': ',Qatar 974,', 'r': ',Republic of the Congo 242,Reunion Island 262,Romania 40,Russia 7,Rwanda 250,', 's': ',Saint Barthelemy 590,Saint Helena 290,Saint Kitts and Nevis 1869,Saint Lucia 1758,Saint Martin 590,Saint Pierre and Miquelon 508,Saint Vincent and theGrenadines 1784,Samoa 685,SanMarino 378,Sao Tome and Principe 239,Saudi Arabia 966,Senegal 221,Serbia 381,Seychelles 248,SierraLeone 232,Singapore 65,Sint Maarten 1721,Slovakia 421,Slovenia 386,Solomon Islands 677,Somalia 252,South Africa 27,SouthKorea 82,South Sudan 211,Spain 34,SriLanka 94,Sudan 249,Suriname 597,Svalbard 47,Swaziland 268,Sweden 46,Switzerland 41,Syria 963,', 't': ',Taiwan 886,Tajikistan 992,Tanzania 255,Thailand 66,Timor-Leste(EastTimor) 670,Togo 228,Tokelau 690,Tonga Islands 676,Trinidad and Tobago 1868,Tunisia 216,Turkey 90,Turkmenistan 993,Turks and Caicos Islands 1649,Tuvalu 688,', 'u': ',Uganda 256,Ukraine 380,United Arab Emirates 971,United Kingdom 44,United States 1,Uruguay 598,US Virgin Islands 1340,Uzbekistan 998,', 'v': ',Vanuatu 678,Venezuela 58,Vietnam 84,', 'w': ',Wallis and Futuna 681,Western Sahara 212,', 'y': ',Yemen 967,', 'z': ',Zambia 260,Zimbabwe 263'}

	
def loadthecntry(p):
	for country in range(0, len(p)):
		(cntry,cd) = p[country].split(' ')
		m[cntry.lower().replace("/"," ")] = cd
		x = cntry[:1]
		y = cntry
		a[cntry[:4].lower()] = cntry.replace("/"," ")
		#m['codse'] = cd.lower()


def tryorelse():
	try:
		kk = str(input("type first 4 character country name for dial-code \n "))
		print("\n")
		x = a[kk].lower()
		y = str(x)
		yx = str(input(f"are you searching dial code for {y} y/n ?? "))
		if yx == "y":	
			inornot(y)
		elif yx == "n":
			print("\n")
			print(f"oh, your country not a {y}, it's fine")
			print(f"type first letter & list all country name for you \n")
			sst = str(input("try first character: "))
			print("\n")
			print("possible country names with dial code in this list below: \n")
			pprint.pprint(a[sst].split(','))
			print("\n")
			print("thank you for using a ai_country.py: \n")
	except:
		print("first four letters not match by any country!!")
		tryorelse()
def inornot(matchy):
	try:
		if m[matchy]:
			print("dialcode -",m[matchy])
		else:
			tryorelse()
			#print(m[tryorelse])
	except KeyError:
		print("your country name doesn't exist \n")
		tryorelse()
			
alllist = loadthefile("country.txt")

loadit = loadthecntry(s)

st = str(input("country name: "))

inornot(st)



