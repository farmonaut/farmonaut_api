# Farmonaut Satellite & Weather API

[![N|Solid](https://i.imgur.com/EJSNAlm.jpg)](https://farmonaut.com/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

[![N|Solid](https://i.imgur.com/taBZAWn.png)](https://farmonaut.com/)

## Table Of Content
#### [Introduction](#introduction-1)
#### [Image Types](#imagetypes)
#### [Get Your Unique ID and Start Using Farmonaut API](#get-your-unique-id-and-start-using-farmonaut-api-1)
#### [What is a Hectare Unit?](#what-is-a-hectare-unit-1)
#### [How to submit a New Farmer Field](#how-to-submit-a-new-farmer-field-1)
#### [How to modify Field Coordinates of Already Submitted Field](#how-to-modify-field-coordinates-of-already-submitted-field-1)
#### [To Pause Field Monitoring](#to-pause-field-monitoring-1)
#### [To Resume Field Monitoring](#to-resume-field-monitoring-1)
#### [How to Retreive All Farmers Data](#how-to-retreive-all-farmers-data-1)
#### [How to Retreive My Usage Data](#how-to-retreive-my-usage-data-1)
#### [How to Retreive A Single Farmer's Data](#how-to-retreive-a-single-farmers-data-1)
#### [Crop Codes](#crop-codes-1)
#### [How to Retrieve a Field Image](#how-to-retrieve-a-field-image-1)
#### [How to Retrieve a Radar Vegetation Field Image](#how-to-retrieve-a-radar-vegetation-field-image-1)
#### [To Retrieve a Field Report](#to-retrieve-a-field-report-1)
#### [To Define Language of the HTML Field Report](#to-define-language-of-the-hTML-field-report-1)
#### [To Retrieve Yield Estimates Of A Field](#to-retrieve-yield-estimates-of-a-field-1)
#### [To Retrieve a Field Area Index Image](#to-retrieve-a-field-area-index-image-1)
#### [To Retrieve Present Weather Data](#to-retrieve-present-weather-data-1)
#### [To Retrieve Present Weather Data From Latitude and Longitude](#to-retrieve-present-weather-data-from-latitude-and-longitude)
#### [To Retrieve Forecast Weather Data](#to-retrieve-forecast-weather-data-1)
#### [To Retrieve Forecast Weather Data From Latitude and Longitude](#to-retrieve-forecast-data-from-latitude-and-longitude)
#### [To Retrieve Historical Weather For A Field](#to-retrieve-historical-weather-for-a-field-1)
#### [Analysis Scales](#analysis-scales-1)

### Introduction:
Farmonaut’s Satellite Based Crop Health Monitoring System is built to put satellite technology in the hands of each and every farmer in the most economical way. Our objective is to break the cost barrier and help democratize remote sensing in the farming community. Satellite Data is updated every 2 to 5 days.


#### ImageTypes:

| Image Name | Resolution |
| ------ | ------ |
| NDVI: Normalized Difference Vegetation Index | 10 meters/pixel |
| NDWI: Normalized Difference Water Index | 20 meters/pixel |
| EVAPO: Evapotranspiration | 20 meters/pixel |
| NDMI: Normalized Difference Moisture Index | 20 meters/pixel |
| EVI: Enhanced Vegetation Index | 10 meters/pixel |
| RVI: Radar Vegetation Index | 10 meters/pixel |
| NDRE: Normalized Difference Red Edge | 20 meters/pixel |
| VARI: Visible Atmospherically Resistant Index | 10 meters/pixel
| SAVI: Soil Adjusted Vegetation Index | 10 meters/pixel |
| AVI: Advanced Vegetation Index | 10 meters/pixel
| BSI: Bare Soil Index | 10 meters/pixel |
| SI: Shadow Index | 10 meters/pixel |
| SOC: Soil Organic carbon | 10 meters/pixel |
| TCI: True color image | 10 meters/pixel |
| ETCI: Enhanced true color image | 10 meters/pixel |
| HYBRID: Hybrid Image | 20 meters/pixel |
| DEM: Digital Elevation Model Image | 10 meters/pixel |

[![N|Solid](https://farmonaut.com/Images/images.JPG)](https://farmonaut.com/)

[![N|Solid](https://secureservercdn.net/160.153.137.14/ox4.27a.myftpupload.com/wp-content/uploads/2020/11/farmonaut_api.jpg)](https://farmonaut.com/)

### Get Your Unique ID and Start Using Farmonaut API

- #### 1000 Hectare Units: (https://rzp.io/l/farmonaut1000)
- #### 5000 Hectare Units: (https://rzp.io/l/farmonaut5000)
- #### 10000 Hectare Units: (https://rzp.io/l/farmonaut10000)
- #### 25000 Hectare Units: (https://rzp.io/l/farmonaut25000)

Once a payment is made, you will receive a unique user id (UID) on your provided email address within 48 hours. With this unique user id (UID), you can start using Farmonaut's API.

##### DO NOT SHARE THIS UID WITH ANYONE. KEEP IT SECURE AND CONFIDENTIAL.


### What is a Hectare Unit?
- A hectare unit is defined as a single satellite observation of 1 hectare of land. Example: if total 6 successful satellite observations are captured for an area of 1 hectare, the hectare units consumed from the subscription will be 1*6 = 6 hectare units.

### Platforms

- Android: https://play.google.com/store/apps/details?id=com.farmonaut.android
- iOS: https://apps.apple.com/us/app/farmonaut/id1489095847
- Web App: http://farmonaut.com/web-app

### Tutorials
- https://farmonaut.com/web-platform/farmonaut-web-app-tutorial/
- https://farmonaut.com/blogs/remote-sensing/normalized-difference-vegetation-index-ndvi/
- https://farmonaut.com/blogs/remote-sensing/ndvi-vs-ndre-and-their-applications-in-agriculture/
- https://farmonaut.com/blogs/remote-sensing/normalized-difference-water-index-ndwi/
- https://farmonaut.com/ios/farmonaut-ios-app-tutorial/



### How to submit a New Farmer Field

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/submitField


Submit a request in the JSON Format

### Example Request Obj
```sh
{
	"UID": "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
	"Points": {
		"a": {
			"Latitude": 12.975601039033629,
			"Longitude": 77.76385936886072
		},
		"P_1": {
			"Latitude": 12.980210619777425,
			"Longitude": 77.76523131877184
		},
		"P_2": {
			"Latitude": 12.9802524385325,
			"Longitude": 77.76818878948689
		},
		"P_3": {
			"Latitude": 12.976061053481807,
			"Longitude": 77.768659517169
		},
		"P_4": {
			"Latitude": 12.975984275561343,
			"Longitude": 77.76420503854752
		}
	},
	"CropCode": "1r",
	"PaymentType": 6
}
```

### Defintions
1. Points == All the boundary points of the field in a clock-wise/counter-clock wise order
2. a == First Point of the field
3. P_x == (x+1)th point of the field, where x = 1,2,3,...
4. Each Field Point is a JSON Object:
```sh
P_x:{
  Latitude: latitude_value,
  Longitude: longitude_value
  }
```
5. PaymentType == Number of months the satellite monitoring is activated for.
6. CropCode = The code of the crop sown in the field

### Response

Upon successful submission:
```sh

{FieldID: uniqueIdentifier of the field}
//save this in the database of your user, and use this to access the satellite data of this field

```

### Errors: 
{errorDescription: errorD}
errorDescriptions
1: invalid points format
2: Invalid Payment Type
3: Invalid crop code
4: Invalid UID



### How to modify Field Coordinates of Already Submitted Field

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/modifyFieldPoints


Submit a request in the JSON Format

### Example Request Obj
```sh
{
	"UID": "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
	"Points": {
		"a": {
			"Latitude": 12.975601039033629,
			"Longitude": 77.76385936886072
		},
		"P_1": {
			"Latitude": 12.980210619777425,
			"Longitude": 77.76523131877184
		},
		"P_2": {
			"Latitude": 12.9802524385325,
			"Longitude": 77.76818878948689
		},
		"P_3": {
			"Latitude": 12.976061053481807,
			"Longitude": 77.768659517169
		},
		"P_4": {
			"Latitude": 12.975984275561343,
			"Longitude": 77.76420503854752
		}
	},
	"FieldID": "1637947932892",
}
```

### Defintions
1. Points == All the boundary points of the field in a clock-wise/counter-clock wise order
2. a == First Point of the field
3. P_x == (x+1)th point of the field, where x = 1,2,3,...
4. Each Field Point is a JSON Object:
```sh
P_x:{
  Latitude: latitude_value,
  Longitude: longitude_value
  }
```


### Response

Upon successful submission:
```sh

{FieldID: uniqueIdentifier of the field}
//save this in the database of your user, and use this to access the satellite data of this field

```

### Errors: 
{errorDescription: errorD}
errorDescriptions
1: invalid points format
2: Invalid field ID
4: Invalid UID



### How to Retreive All Farmers Data

Submit A POST REQUEST ON THE FOLLOWING LINK:
(https://us-central1-farmbase-b2f7e.cloudfunctions.net/getAllFarmersData)

Submit a request in the following JSON Format:
```sh
{UID: UID
}
```


### How to Retreive My Usage Data

Submit A POST REQUEST ON THE FOLLOWING LINK:
(https://us-central1-farmbase-b2f7e.cloudfunctions.net/getMyUsage)

Submit a request in the following JSON Format:
```sh
{UID: UID
}
```

### How to Retreive A Single Farmer's Data

Submit A POST REQUEST ON THE FOLLOWING LINK:
(https://us-central1-farmbase-b2f7e.cloudfunctions.net/getFarmerData)

Submit a request in the following JSON Format:
```sh
{FieldID: fieldID,
    UID: UID
}
```

### Sample JSON Farmer Data

```sh
{
  "1600502365642" : {
    "CenterLat" : 50.50679194429229,
    "CenterLatLarge" : 50.50679194429229,
    "CenterLong" : 14.280552814060654,
    "CenterLongLarge" : 14.280552814060654,
    "Coordinates" : {
      "P_1" : {
        "Latitude" : 50.509171005120145,
        "Longitude" : 14.274860153744537
      },
      "P_10" : {
        "Latitude" : 50.507888945186714,
        "Longitude" : 14.286577469677102
      },
      "P_11" : {
        "Latitude" : 50.507107677856425,
        "Longitude" : 14.286727673381936
      },
      "P_12" : {
        "Latitude" : 50.505429103452045,
        "Longitude" : 14.2861268585626
      },
      "P_13" : {
        "Latitude" : 50.504355135805845,
        "Longitude" : 14.28591875433387
      },
      "P_14" : {
        "Latitude" : 50.5033656817402,
        "Longitude" : 14.285478872055428
      },
      "P_15" : {
        "Latitude" : 50.50470174713382,
        "Longitude" : 14.282217305893319
      },
      "P_16" : {
        "Latitude" : 50.505943644125296,
        "Longitude" : 14.279384893173592
      },
      "P_17" : {
        "Latitude" : 50.506674003699004,
        "Longitude" : 14.277850278783347
      },
      "P_18" : {
        "Latitude" : 50.50730175366734,
        "Longitude" : 14.276745208669212
      },
      "P_19" : {
        "Latitude" : 50.50771455450234,
        "Longitude" : 14.27597558455981
      },
      "P_2" : {
        "Latitude" : 50.50956603877697,
        "Longitude" : 14.277074239540681
      },
      "P_20" : {
        "Latitude" : 50.508193077754505,
        "Longitude" : 14.274377954739371
      },
      "P_21" : {
        "Latitude" : 50.508256707065996,
        "Longitude" : 14.274431000302155
      },
      "P_3" : {
        "Latitude" : 50.509993050527804,
        "Longitude" : 14.279200222992845
      },
      "P_4" : {
        "Latitude" : 50.510218206844385,
        "Longitude" : 14.280643251442857
      },
      "P_5" : {
        "Latitude" : 50.510180680866185,
        "Longitude" : 14.282488611245103
      },
      "P_6" : {
        "Latitude" : 50.50989432732506,
        "Longitude" : 14.283821387053699
      },
      "P_7" : {
        "Latitude" : 50.50937919184884,
        "Longitude" : 14.284921092749805
      },
      "P_8" : {
        "Latitude" : 50.50900453158635,
        "Longitude" : 14.285558230251443
      },
      "P_9" : {
        "Latitude" : 50.50817893195429,
        "Longitude" : 14.28638435062803
      },
      "a" : {
        "Latitude" : 50.508256707065996,
        "Longitude" : 14.274431000302155
      }
    },
    "Email" : "support@farmonaut.com",
    "Expiring" : "no",
    "FailedDays" : {
      "20200905" : "yes",
      "20200925" : "yes",
      "20200927" : "yes",
      "20200930" : "yes",
      "20201007" : "yes",
      "20201015" : "yes",
      "20201017" : "yes",
      "20201020" : "yes",
      "20201027" : "yes"
    },
    "FieldAddress" : "Vrutice 85, 411 47 Vrutice, Czechia",
    "FieldArea" : 396800,
    "FieldID" : "1600502365642",
    "FieldLatLen" : 0.016376154108932894,
    "FieldLatLenLarge" : 0.03275230837586207,
    "FieldLongLen" : 0.025749206542965197,
    "FieldLongLenLarge" : 0.051498413085930395,
    "FieldMaxLat" : 50.510218206844385,
    "FieldMaxLong" : 14.286727673381936,
    "FieldMinLat" : 50.5033656817402,
    "FieldMinLong" : 14.274377954739371,
    "GenTif" : "yes",
    "hUnits" : 119,
    "Health" : {
      "evi" : {
        "20200912" : "60",
        "20200917" : "41",
        "20200920" : "61",
        "20200922" : "59",
        "20201002" : "68",
        "20201022" : "31",
        "20201025" : "52"
      },
      "ndre" : {
        "20200912" : "32",
        "20200917" : "23",
        "20200920" : "33",
        "20200922" : "31",
        "20201002" : "33",
        "20201022" : "19",
        "20201025" : "27"
      },
      "ndvi" : {
        "20200912" : "40",
        "20200917" : "27",
        "20200920" : "41",
        "20200922" : "39",
        "20201002" : "44",
        "20201022" : "21",
        "20201025" : "34"
      },
      "ndwi" : {
        "20200912" : "29",
        "20200917" : "41",
        "20200920" : "28",
        "20200922" : "29",
        "20201002" : "41",
        "20201022" : "44",
        "20201025" : "38"
      },
      "soc" : {
        "20200912" : "4",
        "20200917" : "3",
        "20200920" : "4",
        "20200922" : "4",
        "20201002" : "0",
        "20201022" : "0",
        "20201025" : "0"
      },
      "vari" : {
        "20200912" : "24",
        "20200917" : "32",
        "20200920" : "20",
        "20200922" : "20",
        "20201002" : "42",
        "20201022" : "63",
        "20201025" : "31"
      }
    },
    "Yield":{
        "20200912" : "24",
        "20200917" : "32",
        "20200920" : "20",
        "20200922" : "20",
        "20201002" : "42",
        "20201022" : "63",
        "20201025" : "61"
    }
    "Name" : "Farmonaut Support",
    "OrderDate" : "19-September-2020",
    "Paid" : "Yes",
    "PaymentType" : "3",
    "SensedDays" : {
      "20200912" : "yes",
      "20200917" : "yes",
      "20200920" : "yes",
      "20200922" : "yes",
      "20201002" : "yes",
      "20201022" : "yes",
      "20201025" : "yes"
    },
    "SARDays" : {
      "20200912" : "yes",
      "20200917" : "yes",
      "20200920" : "yes",
      "20200922" : "yes",
    },
    "UID" : "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
    "URI" : "https://lh6.googleusercontent.com/-lsH7M4Gr5wg/AAAAAAAAAAI/AAAAAAAAABM/eNUASvhfjs4/s96-c/photo.jpg",
    "Weather" : {
      "20201028" : {
        "cloud_cover" : 100,
        "humidity" : 79,
        "max_temp" : 283.71,
        "min_temp" : 274.82,
        "pressure" : 1014,
        "station" : "Polepy",
        "wind_deg" : 90,
        "wind_speed" : 0.89
      },
      "20201029" : {
        "cloud_cover" : 75,
        "humidity" : 81,
        "max_temp" : 283.15,
        "min_temp" : 279.26,
        "pressure" : 1017,
        "station" : "Polepy",
        "wind_deg" : 260,
        "wind_speed" : 5.7
      },
      "20201030" : {
        "cloud_cover" : 100,
        "humidity" : 87,
        "max_temp" : 286.48,
        "min_temp" : 277.04,
        "pressure" : 1018,
        "station" : "Polepy",
        "wind_deg" : 270,
        "wind_speed" : 0.89
      }
    }
  }
}
```

### Definitions

1. CenterLat == latitude value of the center of the field
2. CenterLong == longitude value of the center of the field
3. Expiring == whether field is expiring or not
4. FailedDays == days on which satellite could not capture data due to cloud cover
5. FieldAddress == Address of the location of the field
6. FieldArea == area of the field in sqaure meters
7. FieldID == uniqueID of the field
8. FieldMaxLat == maximum latitude value of all the field points
9. FieldMinLat == minimum latitude value of all the field points
10. FieldMaxLong == maximum longitude value of all the field points
11. FieldMinLong == minimum longitude value of all the field points
11. Health == value of indexes on different satellite visit dates (range from 0 to 100)
12. OrderDate == date on which field was added
13. PaymentType == number of months for which satellite monitoring is activated for the field
14. SensedDays == days on which satellite was successfully able to capture the satellite data (yyyymmdd)
15. SARDays == days on which satellite captured the radar vegetation data (yyyymmdd)
15. UID == unique identifier of your organization
16. Weather == weather from the weather station nearest to the field.
17. hUnits == Number of hectare units utilized for this field
18. Yield == Total Yield in Tonnes For The Field Area

### Crop Codes
| Crop | CropCode |
| ------ | ------ |
| Rice (Kharif) | 1k |
| Rice (Rabi) | 1r |
| Wheat | 2r |
| Coarse Cereals (Kharif) | 3k |
| Coarse Cereals (Rabi) | 3r |
| Jowar (Kharif) | 4k |
| Jowar (Rabi) | 4r |
| Bajra (Kharif) | 5k |
| Maize (Kharif) | 6k |
| Maize (Rabi) | 6r |
| Pulse (Kharif) | 7k |
| Pulse (Rabi) | 7r |
| Gram (Rabi) | 8r |
| Tur (Kharif) | 9k |
| Rapeseed and Mustard (Rabi) |10r |
| Soyabean (Kharif) | 11k |
| Sunflower | 12 |
| Sugarcane | 13 |
| Cotton | 14 |
| Jute and Mesta | 15 |
| Potato | 16 |
| Onion | 17 |
| Coconut | 18 |
| Tobacco | 19 |
| Groundnut | 20 |
| Turmeric | 21 |
| Corn | 22 |
| Chili | 23 |
| Other | 999 |



#### ImageTypes:

| Image Name | imageType |
| ------ | ------ |
| NDVI | ndvi |
| NDWI | ndwi |
| EVAPO | evapo |
| EVI | evi |
| RVI | rvi |
| NDRE | ndre |
| VARI | vari
| SAVI | savi |
| AVI | avi
| BSI | bsi |
| SI | si |
| SOC | soc |
| TCI | tci |
| ETCI | etci |
| HYBRID | hybrid |

### How to Retrieve a Field Image

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/getFieldImage



### Example Request Obj
```sh
{
	"UID": "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
	"FieldID": "1600503072436",
	"SensedDay": "20201025",
	"ImageType": "ndvi",
	"Colormap": "1" (optional values can be 1 or 2)
}
```
### Response
```sh
{
"url":url
}
```
Note: replace 'media1' with 'media' at the end of the provided URL in the response.


### How to Retrieve a Radar Vegetation Field Image

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/getFieldImage



### Example Request Obj
```sh
{
	"UID": "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
	"FieldID": "1600503072436",
	"SensedDay": "20201025",
	"ImageType": "rvi",
	"Colormap": "1" (optional values can be 1 or 2)
}
```

Note:In the SensedDay key, provide the date from the "SARDays" object of the Field Data Object. This is applicable only for radar vegetation images.

### Response
```sh
{
"url":url
}
```
Note: replace 'media1' with 'media' at the end of the provided URL in the response.


### To Resume Field Monitoring


  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/resumeFieldMonitoring

### Example Request Obj
```sh
{
	"UID": "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
	"FieldID": "1600503072436",
}

```
### Response
```sh
Field Monitoring Resumed.
```




### To Pause Field Monitoring


  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/pauseFieldMonitoring

### Example Request Obj
```sh
{
	"UID": "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
	"FieldID": "1600503072436",
}

```
### Response
```sh
Field Monitoring Paused.
```


### To Define Language of the HTML Field Report


  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/setReportLanguage

### Example Request Obj
```sh
{
	"UID": "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
	"FieldID": "1600503072436",
	"Language": "en"
}

```
### Response
```sh
Language Set.
```

#### Language Codes:
```sh
Afrikaans:   af
Albanian:   sq
Amharic:	am
Arabic:	ar
Armenian:	hy
Azerbaijani:	az
Basque:	eu
Belarusian:	be
Bengali:	bn
Bosnian:	bs
Bulgarian:	bg
Catalan:	ca
Cebuano:	ceb (ISO-639-2)
Chinese (Simplified):	zh-CN or zh (BCP-47)
Chinese (Traditional):	zh-TW (BCP-47)
Corsican:	co
Croatian:	hr
Czech:	cs
Danish:	da
Dutch:	nl
English:	en
Esperanto:	eo
Estonian:	et
Finnish:	fi
French:	fr
Frisian:	fy
Galician:	gl
Georgian:	ka
German:	de
Greek:	el
Gujarati:	gu
Haitian Creole:	ht
Hausa:	ha
Hawaiian:	haw (ISO-639-2)
Hebrew:	he or iw
Hindi:	hi
Hmong:	hmn (ISO-639-2)
Hungarian:	hu
Icelandic:	is
Igbo:	ig
Indonesian:	id
Irish:	ga
Italian:	it
Japanese:	ja
Javanese:	jv
Kannada:	kn
Kazakh:	kk
Khmer:	km
Kinyarwanda:	rw
Korean:	ko
Kurdish:	ku
Kyrgyz:	ky
Lao:	lo
Latin:	la
Latvian:	lv
Lithuanian:	lt
Luxembourgish:	lb
Macedonian:	mk
Malagasy:	mg
Malay:	ms
Malayalam:	ml
Maltese:	mt
Maori:	mi
Marathi:	mr
Mongolian:	mn
Myanmar (Burmese):	my
Nepali:	ne
Norwegian:	no
Nyanja (Chichewa):	ny
Odia (Oriya):	or
Pashto:	ps
Persian:	fa
Polish:	pl
Portuguese (Portugal, Brazil):	pt
Punjabi:	pa
Romanian:	ro
Russian:	ru
Samoan:	sm
Scots Gaelic:	gd
Serbian:	sr
Sesotho:	st
Shona:	sn
Sindhi:	sd
Sinhala (Sinhalese):	si
Slovak:	sk
Slovenian:	sl
Somali:	so
Spanish:	es
Sundanese:	su
Swahili:	sw
Swedish:	sv
Tagalog (Filipino):	tl
Tajik:	tg
Tamil:	ta
Tatar:	tt
Telugu:	te
Thai:	th
Turkish:	tr
Turkmen:	tk
Ukrainian:	uk
Urdu:	ur
Uyghur:	ug
Uzbek:	uz
Vietnamese:	vi
Welsh:	cy
Xhosa:	xh
Yiddish:	yi
Yoruba:	yo
Zulu:	zu

```

### To Retrieve a Field Report

![alt text](https://secureservercdn.net/160.153.137.14/ox4.27a.myftpupload.com/wp-content/uploads/2019/12/reportScreen.jpg)


  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/getFieldReport

### Example Request Obj
```sh
{
	"UID": "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
	"FieldID": "1600503072436",
	"SensedDay": "20201025",
	"ReportFormat" "PDF"
}

```
### Response
```sh
{
"url":url
}
```

```sh
Report Formats: "PDF", "HTML"
```
Note: replace 'media1' with 'media' at the end of the provided URL in the response.


### To Retrieve Yield Estimates Of A Field

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/getYieldEstimates

### Example Request Obj

```sh
{    UID: UID,
FieldID:fieldID,
}
```

### Response
Yield == Total Yield Estimated in Tonnes For Given The Field Area

### To Retrieve a Field Area Index Image

![alt text](https://firebasestorage.googleapis.com/v0/b/farmbase-b2f7e.appspot.com/o/PaidMonitoredFields%2FFnXlVukcRvYd28FhZsEM7BTMAPv1%2F1601277947835%2F20201031%2Fndvi_pie?alt=media&token=4d9acab5-e441-4098-98f8-1c319e25ac4c)

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/getFieldIndexAreaImage

### Example Request Obj
```sh
{
	"UID": "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
	"FieldID": "1600503072436",
	"SensedDay": "20201025",
	"ImageType": "ndvi"
}
```

### Response
```sh
{
"url":url
}
```

Note: replace 'media1' with 'media' at the end of the provided URL in the response.




### To Retrieve Forecast Weather Data

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/getForecastWeather

### Example Request Obj

```sh
{FieldID: fieldID,
    UID: UID
}
```


### To Retrieve Forecast Data From Latitude and Longitude

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/getForecastWeatherFromLatLong

### Example Request Obj

```sh
{    UID: UID,
Latitude: lat,
Longitude: lon
}
```

### To Retrieve Present Weather Data

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/getPresentWeather

### Example Request Obj

```sh
{FieldID: fieldID,
    UID: UID
}
```

### Response
A JSON object containing current weather information from the nearest weather station

```sh

{
  "coord": {
    "lon": -122.08,
    "lat": 37.39
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 16093,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
  } 
```


### Fields in API response
```sh
coord
coord.lon City geo location, longitude
coord.lat City geo location, latitude
weather (more info Weather condition codes)
weather.id Weather condition id
weather.main Group of weather parameters (Rain, Snow, Extreme etc.)
weather.description Weather condition within the group. You can get the output in your language. Learn more
weather.icon Weather icon id
base Internal parameter
main
main.temp Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.feels_like Temperature. This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.pressure Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
main.humidity Humidity, %
main.temp_min Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.temp_max Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.sea_level Atmospheric pressure on the sea level, hPa
main.grnd_level Atmospheric pressure on the ground level, hPa
wind
wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
wind.deg Wind direction, degrees (meteorological)
wind.gust Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
clouds
clouds.all Cloudiness, %
rain
rain.1h Rain volume for the last 1 hour, mm
rain.3h Rain volume for the last 3 hours, mm
snow
snow.1h Snow volume for the last 1 hour, mm
snow.3h Snow volume for the last 3 hours, mm
dt Time of data calculation, unix, UTC
sys
sys.type Internal parameter
sys.id Internal parameter
sys.message Internal parameter
sys.country Country code (GB, JP etc.)
sys.sunrise Sunrise time, unix, UTC
sys.sunset Sunset time, unix, UTC
timezone Shift in seconds from UTC
id City ID
name City name
cod Internal parameter
```



### To Retrieve Weather Data From Latitude and Longitude

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/getPresentWeatherFromLatLong

### Example Request Obj

```sh
{    UID: UID,
Latitude: lat,
Longitude: lon
}
```

### Response
A JSON object containing current weather information from the nearest weather station

```sh

{
  "coord": {
    "lon": -122.08,
    "lat": 37.39
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 16093,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
  } 
```


### Fields in API response
```sh
coord
coord.lon City geo location, longitude
coord.lat City geo location, latitude
weather (more info Weather condition codes)
weather.id Weather condition id
weather.main Group of weather parameters (Rain, Snow, Extreme etc.)
weather.description Weather condition within the group. You can get the output in your language. Learn more
weather.icon Weather icon id
base Internal parameter
main
main.temp Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.feels_like Temperature. This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.pressure Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa
main.humidity Humidity, %
main.temp_min Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.temp_max Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
main.sea_level Atmospheric pressure on the sea level, hPa
main.grnd_level Atmospheric pressure on the ground level, hPa
wind
wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
wind.deg Wind direction, degrees (meteorological)
wind.gust Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
clouds
clouds.all Cloudiness, %
rain
rain.1h Rain volume for the last 1 hour, mm
rain.3h Rain volume for the last 3 hours, mm
snow
snow.1h Snow volume for the last 1 hour, mm
snow.3h Snow volume for the last 3 hours, mm
dt Time of data calculation, unix, UTC
sys
sys.type Internal parameter
sys.id Internal parameter
sys.message Internal parameter
sys.country Country code (GB, JP etc.)
sys.sunrise Sunrise time, unix, UTC
sys.sunset Sunset time, unix, UTC
timezone Shift in seconds from UTC
id City ID
name City name
cod Internal parameter
```



### To Retrieve Historical Weather For A Field

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/getHistoricalFieldWeather

### Example Request Obj

```sh
{    UID: UID,
FieldID:fieldID,
NumberOfDays: numberOfDays
}
```

#### Analysis Scales:

NDVI: https://farmonaut.com/Images/ndvi_scale.jpg

![alt text](https://farmonaut.com/Images/ndvi_scale.jpg)

NDRE: https://farmonaut.com/Images/ndre_scale.jpg

![alt text](https://farmonaut.com/Images/ndre_scale.jpg)

EVI: https://farmonaut.com/Images/evi_scale.jpg

![alt text](https://farmonaut.com/Images/evi_scale.jpg)

VARI: https://farmonaut.com/Images/vari_scale.jpg

![alt text](https://farmonaut.com/Images/vari_scale.jpg)

NDWI: https://farmonaut.com/Images/ndwi_scale.jpg

![alt text](https://farmonaut.com/Images/ndwi_scale.jpg)

HYBRID: https://farmonaut.com/Images/hybrid_scale.jpg

![alt text](https://farmonaut.com/Images/hybrid_scale.jpg)
