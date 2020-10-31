# Farmonaut API

[![N|Solid](https://i.imgur.com/EJSNAlm.jpg)](https://farmonaut.com/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

[![N|Solid](https://i.imgur.com/taBZAWn.png)](https://farmonaut.com/)
Farmonaut’s Satellite Based Crop Health Monitoring System is built to put satellite technology in the hands of each and every farmer in the most economical way. Our objective is to break the cost barrier and help democratize remote sensing in the farming community.


### Platforms

- Android: https://play.google.com/store/apps/details?id=com.farmonaut.android
- iOS: https://apps.apple.com/us/app/farmonaut/id1489095847
- Web App: http://farmonaut.com/web-app

### Tutorials
https://farmonaut.com/web-platform/farmonaut-web-app-tutorial/
https://farmonaut.com/blogs/remote-sensing/normalized-difference-vegetation-index-ndvi/
https://farmonaut.com/blogs/remote-sensing/ndvi-vs-ndre-and-their-applications-in-agriculture/
https://farmonaut.com/blogs/remote-sensing/normalized-difference-water-index-ndwi/
https://farmonaut.com/ios/farmonaut-ios-app-tutorial/



### How to submit a New Farmer Field

  - Submit a POST REQUEST ON THE FOLLOWING LINK:
https://us-central1-farmbase-b2f7e.cloudfunctions.net/submitField


Submit a request in the JSON Format
```sh
{Points:{
  a:{Latitude:0,
	Longitude:0
  },
	P_1:{Latitude:0,
	Longitude:0
  },
	.
	.
	.
},
PaymentType:6,
CropCode:,
UID: unique Identifier provided to your organization
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
//save this in the database of your user, and use this to access the satellite data

```

### Errors: 
{errorDescription: errorD}
errorDescriptions
1: invalid points format
2: Invalid Payment Type
3: Invalid crop code

### How to Retreive Farmer Data

Submit A POST REQUEST ON THE FOLLOWING LINK:
(https://us-central1-farmbase-b2f7e.cloudfunctions.net/getField)

Submit a request in the following JSON Format:
```sh
{fieldID: fieldID,
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
14. SensedDays == days on which satellite was successfully able to capture the satellite date (yyyymmdd)
15. UID == unique identifier of your organization
16. Weather == weather from the weather station nearest to the field.


| Crop | CropCode |
| ------ | ------ |
| Rice (Kharif) | 1k |
| Rice (Rabi) | [1r |
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


### To Retrieve a Field Image

Create a Reference Link:
```sh
final FirebaseStorage storage = FirebaseStorage.getInstance();
final StorageReference storageRef = storage.getReference();
final StorageReference gsReference = new StorageReference();
gsReference = storageRef.child("PaidMonitoredFields").child(uid).child(fieldID).child(sensedDay).child(imageType);
```
#### ImageTypes:

| Image Name | imageType |
| ------ | ------ |
| NDVI | ndvi |
| NDWI | ndwi |
| EVI | evi |
| NDRE | ndre |
| VARI | vari
| SOC | soc |
| TCI | tci |
| ETCI | etci |
| HYBRID | hybrid |



### To Retrieve a Field Report

Create a Reference Link:
```sh
final FirebaseStorage storage = FirebaseStorage.getInstance();
final StorageReference storageRef = storage.getReference();
final StorageReference gsReference = new StorageReference();
gsReference = storageRef.child("PaidMonitoredFields").child(uid).child(fieldID).child(sensedDay).child(report.pdf);
```


### To Retrieve a Field Area Index Image

Create a Reference Link:
```sh
final FirebaseStorage storage = FirebaseStorage.getInstance();
final StorageReference storageRef = storage.getReference();
final StorageReference gsReference = new StorageReference();
gsReference = storageRef.child("PaidMonitoredFields").child(uid).child(fieldID).child(sensedDay).child(imageType_index);

example: 
for NDVI, imageType_index = ndvi_pie
for NDRE, imageType_index = ndre_pie
and so on.
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
