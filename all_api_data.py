# keeping it for easy accessibility
import json

allAPIData = [
  {
    "name": "Submit New Farm/Plot",
    "desc": "It adds a new farm to your account with provided coordinates and enables it for getting satellite data (caution: it doesn't stop you from adding duplicate farms).\n\nOnce you submit the request it generally takes less than 15 mins for the first results to be generated. Once these results are generated they can be accessed instantaneously at any point of time.",
    "endpoint": "/submitField",
    "isDeprecated": False,
    "youtube": "https://youtu.be/lXNZvZ2nn1w",
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "CropCode",
        "dataType": "String",
        "dummyValue": "1r",
        "desc": "Crop code for the crop being cultivated at the farm. You can find the codes to use for various crops here. 🔗",
        "isOptional": False,
        "references": ["cropCodesList"]
      },
      {
        "name": "FieldName",
        "dataType": "String",
        "dummyValue": "My Field-3 Kanpur",
        "desc": "One can give a name to the field to identify it easily.",
        "isOptional": True
      },
      {
        "name": "PaymentType",
        "dataType": "int",
        "dummyValue": "6",
        "desc": "Number of months the satellite monitoring is activated for.",
        "isOptional": False
      },
      {
        "name": "Points",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
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
          },
        },
        "desc": "All the boundary points of the field in a clock-wise/counter-clock-wise order. First point is referred as 'a' and subsequent ones as 'P_1', 'P_2' and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field."
      }
    ],
    "sampleCodes": {},
    "errors": {
      "type": "Map", #means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Change Field Coordinates",
    "desc": "If you entered wrong coordinates before and wants to correct it, use this endpoint with corrected coordinates.",
    "endpoint": "/modifyFieldPoints",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "Points",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
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
          },
        },
        "desc": "All the boundary points of the field in a clock-wise/counter-clock-wise order. First point is referred as 'a' and subsequent ones as 'P_1', 'P_2' and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field."
      }
    ],
    "sampleCodes": {},
    "errors": {
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Field Area By Boundary Points",
    "desc": "Use it to get boundary area of any given field by submitting the boundary point coordinates.",
    "endpoint": "/getFieldAreaByBoundaryPoints",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "Points",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
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
          },
        },
        "desc": "All the boundary points of the field in a clock-wise/counter-clock-wise order. First point is referred as 'a' and subsequent ones as 'P_1', 'P_2' and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "FieldArea",
        "dataType": "int",
        "dummyValue": "232",
        "desc": "Field Area would be in sq. m."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get All Fields Data",
    "desc": "It returns all the data for all the fields in json object format with fieldID as keys.",
    "endpoint": "/getAllFarmersData",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "<FieldID>",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "CenterLat": 50.50679194429229,
          "CenterLatLarge": 50.50679194429229,
          "CenterLong": 14.280552814060654,
          "CenterLongLarge": 14.280552814060654,
          "Coordinates": {
            "P_1": {
              "Latitude": 50.509171005120145,
              "Longitude": 14.274860153744537
            },
            "P_2": {
              "Latitude": 50.50956603877697,
              "Longitude": 14.277074239540681
            },
            "P_3": {
              "Latitude": 50.509993050527804,
              "Longitude": 14.279200222992845
            },
            "a": {
              "Latitude": 50.508256707065996,
              "Longitude": 14.274431000302155
            }
          },
          "Email": "support@farmonaut.com",
          "Expiring": "no",
          "FailedDays": {
            "20200905": "yes",
            "20200925": "yes"
          },
          "FieldAddress": "Vrutice 85, 411 47 Vrutice, Czechia",
          "FieldArea": 396800,
          "FieldID": "1600502365642",
          "FieldLatLen": 0.016376154108932894,
          "FieldLatLenLarge": 0.03275230837586207,
          "FieldLongLen": 0.025749206542965197,
          "FieldLongLenLarge": 0.051498413085930395,
          "FieldMaxLat": 50.510218206844385,
          "FieldMaxLong": 14.286727673381936,
          "FieldMinLat": 50.5033656817402,
          "FieldMinLong": 14.274377954739371,
          "GenTif": "yes",
          "hUnits": 119,
          "Health": {
            "evi": {
              "20200912": "60",
              "20200917": "41"
            },
            "ndre": {
              "20200912": "32",
              "20200917": "23"
            },
            "ndvi": {
              "20200912": "40",
              "20200917": "27"
            },
            "ndwi": {
              "20200912": "29",
              "20200917": "41"
            },
            "soc": {
              "20200912": "4",
              "20200917": "3"
            },
            "vari": {
              "20200912": "24",
              "20200917": "32"
            }
          },
          "Yield": {
            "20200912": "24",
            "20200917": "32"
          },
          "Name": "Farmonaut Support",
          "OrderDate": "19-September-2020",
          "Paid": "Yes",
          "PaymentType": "3",
          "SensedDays": {
            "20200912": "yes",
            "20200917": "yes"
          },
          "SARDays": {
            "20200912": "yes",
            "20200917": "yes"
          },
          "UID": "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
          "URI": "https://lh6.googleusercontent.com/-lsH7M4Gr5wg/AAAAAAAAAAI/AAAAAAAAABM/eNUASvhfjs4/s96-c/photo.jpg",
          "Weather": {
            "20201028": {
              "cloud_cover": 100,
              "humidity": 79,
              "max_temp": 283.71,
              "min_temp": 274.82,
              "pressure": 1014,
              "station": "Polepy",
              "wind_deg": 90,
              "wind_speed": 0.89
            }
          }
        },
        "valueParams":[
          {
            "name":"CenterLat",
            "dataType":"double",
            "dummyValue":50.50679194429229,
            "desc":"The latitude of the center of the farm in decimal format."
          },
          {
            "name":"CenterLong",
            "dataType":"double",
            "dummyValue":14.280552814060654,
            "desc":"The longitude of the center of the farm in decimal format."
          },
          {
            "name":"CenterLongLarge",
            "dataType":"double",
            "dummyValue":14.280552814060654,
            "desc":"The longitude of the center of the farm in decimal format."
          },
          {
            "name":"Coordinates",
            "dataType":"Map (key-value pairs)",
            "dummyValue":{
              "P_1": {
                "Latitude": 50.509171005120145,
                "Longitude": 14.274860153744537
              },
              "P_2": {
                "Latitude": 50.50956603877697,
                "Longitude": 14.277074239540681
              },
              "P_3": {
                "Latitude": 50.509993050527804,
                "Longitude": 14.279200222992845
              },
              "a": {
                "Latitude": 50.508256707065996,
                "Longitude": 14.274431000302155
              }
            },
            "valueParams":[
              {
                "name":"a",
                "dataType":"Map (key-value pairs)",
                "dummyValue": {
                "Latitude": 50.508256707065996,
                "Longitude": 14.274431000302155
              },
              "desc":"'a' denotes the first point in the order. It has the latitude & longitude values as a Map."
              },
              {
                "name":"P_x",
                "dataType":"Map (key-value pairs)",
                "dummyValue": {
                  "Latitude": 50.508256707065996,
                  "Longitude": 14.274431000302155
                },
                "desc":"'P_x' denotes the (x+1)th point in the order. It has the latitude & longitude values as a Map."
                }
            ],
            "desc":"The coordinates of the farm in clock-wise/counter-clock-wise order. The coordinates have keys as 'a' for 1st point, 'P_1' for 2nd point, 'P_2' for 3rd point and so on.. Minimum number of points would be 3"
          },
          {
            "name":"CenterLatLarge",
            "dataType":"double",
            "dummyValue":50.50679194429229,
            "desc":"The latitude of the center of the farm in decimal format."
          },
          {
            "name":"Email",
            "dataType":"String",
            "dummyValue":"support@farmonaut.com",
            "desc":"The email address associated with the field owner's account."
          },
          {
            "name":"Expiring",
            "dataType":"String",
            "dummyValue":"no",
            "desc":"It tells if the satellite monitoring plan of the field is expiring soon or not. The possible values are 'yes', 'no' or null."
          },
          {
            "name":"FailedDays",
            "dataType":"Map (key-value pairs)",
            "dummyValue":{
              "20200905": "yes",
              "20200925": "yes"
            },
            "valueParams":[
              {
                "name":"<SatelliteVisitDate>",
                "dataType":"String",
                "dummyValue":"yes",
                "desc":"The value of this Map can be ignored, it's just meant to get the date value from the key."
              }
            ],
            "desc":"The satellite visit dates at which no satellite data was collected due to cloud over the farm. The value is in form of a Map with date as the key and value as 'yes' String."
          },
          {
            "name":"SensedDays",
            "dataType":"Map (key-value pairs)",
            "dummyValue":{
              "20200905": "yes",
              "20200925": "yes"
            },
            "valueParams":[
              {
                "name":"<SatelliteVisitDate>",
                "dataType":"String",
                "dummyValue":"yes",
                "desc":"The value of this Map can be ignored, it's just meant to get the date value from the key."
              }
            ],
            "desc":"The satellite visit dates of the farm. The value is in form of a Map with date as the key and value as 'yes' String."
          },
          {
            "name":"SARDays",
            "dataType":"Map (key-value pairs)",
            "dummyValue":{
              "20200905": "yes",
              "20200925": "yes"
            },
            "valueParams":[
              {
                "name":"<RadarVisitDate>",
                "dataType":"String",
                "dummyValue":"yes",
                "desc":"The value of this Map can be ignored, it's just meant to get the date value from the key."
              }
            ],
            "desc":"The dates at which radar data of the farm was collected. The value is in form of a Map with date as the key and value as 'yes' String."
          },
          {
            "name":"FieldAddress",
            "dataType":"String",
            "dummyValue":"Vrutice 85, 411 47 Vrutice, Czechia",
            "desc":"The street address of the field taken from google places API."
          },
          {
            "name":"FieldID",
            "dataType":"String",
            "dummyValue":"1600502365642",
            "desc":"It is an identifier for the the field. It's unique for every field."
          },
          {
            "name":"FieldArea",
            "dataType":"int",
            "dummyValue":396800,
            "desc":"The field area in sq. m."
          },
          {
            "name":"FieldLatLen",
            "dataType":"double",
            "dummyValue":0.016376154108932894,
            "desc":"The different of the max and min latitude of the field."
          },
          {
            "name":"FieldLatLenLarge",
            "dataType":"double",
            "dummyValue":0.016376154108932894,
            "desc":"The different of the max and min latitude of the field."
          },
          {
            "name":"FieldLongLen",
            "dataType":"double",
            "dummyValue":0.025749206542965197,
            "desc":"The different of the max and min longitude of the field."
          },
          {
            "name":"FieldLongLenLarge",
            "dataType":"double",
            "dummyValue":0.025749206542965197,
            "desc":"The different of the max and min longitude of the field."
          },
          {
            "name":"FieldMaxLat",
            "dataType":"double",
            "dummyValue":50.510218206844385,
            "desc":"The maximum latitude of the field."
          },
          {
            "name":"FieldMaxLong",
            "dataType":"double",
            "dummyValue":14.286727673381936,
            "desc":"The maximum longitude of the field."
          },
          {
            "name":"FieldMinLat",
            "dataType":"double",
            "dummyValue":50.510218206844385,
            "desc":"The minimum latitude of the field."
          },
          {
            "name":"FieldMinLong",
            "dataType":"double",
            "dummyValue":14.286727673381936,
            "desc":"The minimum longitude of the field."
          },
          {
            "name":"GenTif",
            "dataType":"String",
            "dummyValue":"yes",
            "desc":"Tells if the genTif image creation is enabled or not. The possible values are 'yes', 'no' or null."
          },
          {
            "name":"hUnits",
            "dataType":"int",
            "dummyValue":119,
            "desc":"The number of hectare units utilized for this field. Know more about hectare unit by usage chart section.🔗",
            "references":["hectareUnits"]
          },
          {
            "name":"Health",
            "dataType":"Map (key-value pairs)",
            "dummyValue":{
              "ndvi":{
                "20200912": "60",
                "20200917": "41"
              }
            },
            "valueParams":[
              {
                "name":"<ImageType>",
                "dataType":"Map (key-value pairs)",
                "dummyValue":{
                  "20200912": "60",
                  "20200917": "41"
                },
                "valueParams":[
                  {
                    "name":"<SatelliteVisitDate>",
                    "dataType":"String",
                    "dummyValue":"46",
                    "desc":"The health value or the average index value of the image of the given satellite visit date. (range from 0 to 100)"
                  }
                ],
                "desc":"The health values by image type and satellite visit date."
              }
            ],
            "desc":"Health tells average value of indexes of different image types at different satellite visits."
          },
          {
            "name":"Yield",
            "dataType":"Map (key-value pairs)",
            "dummyValue":{
              "20200912": "30",
              "20200917": "21"
            },
            "valueParams":[
              {
                "name":"<SatelliteVisitDate>",
                "dataType":"String",
                "dummyValue":"46",
                "desc":"The yeild estimate value at the satellite visit date for the field. The value is in tonnes."
              }
            ],
            "desc":"The yield estimation values at different satellite visit date for the field. The yeild value in tonnes."
          },
          {
            "name":"Name",
            "dataType":"String",
            "dummyValue":"Farmonaut Support",
            "desc":"The name associated with the field owner's account."
          },
          {
            "name":"OrderDate",
            "dataType":"String",
            "dummyValue":"19-September-2020",
            "desc":"The date of farm submission or the first monitoring order date."
          },
          {
            "name":"Paid",
            "dataType":"String",
            "dummyValue":"Yes",
            "desc":"Is the payment done for the current order. The possible values are 'Yes', 'No' or null."
          },
          {
            "name":"PaymentType",
            "dataType":"String",
            "dummyValue":"6",
            "desc":"The satellite monitoring plan choosen in the last order. The possible values are 1, 3, 6 and 12; representing the plan duration in months."
          },
          {
            "name":"UID",
            "dataType":"String",
            "dummyValue":"BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
            "desc":"Also referred as API ID at some places. It's basically an identifier for your account."
          },
          {
            "name":"Weather-",
            "dataType":"Map (key-value pairs)",
            "dummyValue":{
              "20201028": {
                "cloud_cover": 100,
                "humidity": 79,
                "max_temp": 283.71,
                "min_temp": 274.82,
                "pressure": 1014,
                "station": "Polepy",
                "wind_deg": 90,
                "wind_speed": 0.89
              }
            },
            "valueParams":[
              {
                "name":"<SatelliteVisitDate>",
                "dataType":"Map (key-value pairs)",
                "dummyValue":{
                  "cloud_cover": 100,
                  "humidity": 79,
                  "max_temp": 283.71,
                  "min_temp": 274.82,
                  "pressure": 1014,
                  "station": "Polepy",
                  "wind_deg": 90,
                  "wind_speed": 0.89
                },
                "valueParams":[
                  {
                    "name": "station",
                    "dataType": "String",
                    "dummyValue": "Hoskote",
                    "desc": "Weather station city name"
                  },
                  {
                    "name": "min_temp",
                    "dataType": "double",
                    "dummyValue": 280.37,
                    "desc": " Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit is Kelvin."
                  },
                  {
                    "name": "max_temp",
                    "dataType": "double",
                    "dummyValue": 284.26,
                    "desc": "Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit is Kelvin."
                  },
                  {
                    "name": "pressure",
                    "dataType": "int",
                    "dummyValue": 1023,
                    "desc": "Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa"
                  },
                  {
                    "name": "humidity",
                    "dataType": "int",
                    "dummyValue": 86,
                    "desc": "Humidity in %"
                  },
                  {
                    "name": "wind_speed",
                    "dataType": "double",
                    "dummyValue": 1.5,
                    "desc": "Wind speed. Unit int meter/sec."
                  },
                  {
                    "name": "wind_deg",
                    "dataType": "int",
                    "dummyValue": 350,
                    "desc": "Wind direction, degrees (meteorological)"
                  },
                  {
                    "name": "cloud_cover",
                    "dataType": "int",
                    "dummyValue": 90,
                    "desc": "Cloudiness in %"
                  }
                ],
                "desc":"The weather data at the specified satellite visit date."
              }
            ],
            "desc":"The weather data at different satellite visit dates."
          }
        ],
        "desc": "It's a map of all the data of a single field with key as that field's ID."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get A Single Field's Data",
    "desc": "It returns all the data for a single Field.",
    "endpoint": "/getFarmerData",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "<FieldID>",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
            "CenterLat": 50.50679194429229,
            "CenterLatLarge": 50.50679194429229,
            "CenterLong": 14.280552814060654,
            "CenterLongLarge": 14.280552814060654,
            "Coordinates": {
              "P_1": {
                "Latitude": 50.509171005120145,
                "Longitude": 14.274860153744537
              },
              "P_2": {
                "Latitude": 50.50956603877697,
                "Longitude": 14.277074239540681
              },
              "P_3": {
                "Latitude": 50.509993050527804,
                "Longitude": 14.279200222992845
              },
              "a": {
                "Latitude": 50.508256707065996,
                "Longitude": 14.274431000302155
              }
            },
            "Email": "support@farmonaut.com",
            "Expiring": "no",
            "FailedDays": {
              "20200905": "yes",
              "20200925": "yes"
            },
            "FieldAddress": "Vrutice 85, 411 47 Vrutice, Czechia",
            "FieldArea": 396800,
            "FieldID": "1600502365642",
            "FieldLatLen": 0.016376154108932894,
            "FieldLatLenLarge": 0.03275230837586207,
            "FieldLongLen": 0.025749206542965197,
            "FieldLongLenLarge": 0.051498413085930395,
            "FieldMaxLat": 50.510218206844385,
            "FieldMaxLong": 14.286727673381936,
            "FieldMinLat": 50.5033656817402,
            "FieldMinLong": 14.274377954739371,
            "GenTif": "yes",
            "hUnits": 119,
            "Health": {
              "evi": {
                "20200912": "60",
                "20200917": "41"
              },
              "ndre": {
                "20200912": "32",
                "20200917": "23"
              },
              "ndvi": {
                "20200912": "40",
                "20200917": "27"
              },
              "ndwi": {
                "20200912": "29",
                "20200917": "41"
              },
              "soc": {
                "20200912": "4",
                "20200917": "3"
              },
              "vari": {
                "20200912": "24",
                "20200917": "32"
              }
            },
            "Yield": {
              "20200912": "24",
              "20200917": "32"
            },
            "Name": "Farmonaut Support",
            "OrderDate": "19-September-2020",
            "Paid": "Yes",
            "PaymentType": "3",
            "SensedDays": {
              "20200912": "yes",
              "20200917": "yes"
            },
            "SARDays": {
              "20200912": "yes",
              "20200917": "yes"
            },
            "UID": "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
            "URI": "https://lh6.googleusercontent.com/-lsH7M4Gr5wg/AAAAAAAAAAI/AAAAAAAAABM/eNUASvhfjs4/s96-c/photo.jpg",
            "Weather": {
              "20201028": {
                "cloud_cover": 100,
                "humidity": 79,
                "max_temp": 283.71,
                "min_temp": 274.82,
                "pressure": 1014,
                "station": "Polepy",
                "wind_deg": 90,
                "wind_speed": 0.89
              }
            }
        },
        "valueParams":[
            {
              "name":"CenterLat",
              "dataType":"double",
              "dummyValue":50.50679194429229,
              "desc":"The latitude of the center of the farm in decimal format."
            },
            {
              "name":"CenterLong",
              "dataType":"double",
              "dummyValue":14.280552814060654,
              "desc":"The longitude of the center of the farm in decimal format."
            },
            {
              "name":"CenterLongLarge",
              "dataType":"double",
              "dummyValue":14.280552814060654,
              "desc":"The longitude of the center of the farm in decimal format."
            },
            {
              "name":"Coordinates",
              "dataType":"Map (key-value pairs)",
              "dummyValue":{
                "P_1": {
                  "Latitude": 50.509171005120145,
                  "Longitude": 14.274860153744537
                },
                "P_2": {
                  "Latitude": 50.50956603877697,
                  "Longitude": 14.277074239540681
                },
                "P_3": {
                  "Latitude": 50.509993050527804,
                  "Longitude": 14.279200222992845
                },
                "a": {
                  "Latitude": 50.508256707065996,
                  "Longitude": 14.274431000302155
                }
              },
              "valueParams":[
                {
                 "name":"a",
                 "dataType":"Map (key-value pairs)",
                 "dummyValue": {
                  "Latitude": 50.508256707065996,
                  "Longitude": 14.274431000302155
                },
                "desc":"'a' denotes the first point in the order. It has the latitude & longitude values as a Map."
                },
                {
                  "name":"P_x",
                  "dataType":"Map (key-value pairs)",
                  "dummyValue": {
                   "Latitude": 50.508256707065996,
                   "Longitude": 14.274431000302155
                 },
                 "desc":"'P_x' denotes the (x+1)th point in the order. It has the latitude & longitude values as a Map."
                 }
              ],
              "desc":"The coordinates of the farm in clock-wise/counter-clock-wise order. The coordinates have keys as 'a' for 1st point, 'P_1' for 2nd point, 'P_2' for 3rd point and so on.. Minimum number of points would be 3"
            },
            {
              "name":"CenterLatLarge",
              "dataType":"double",
              "dummyValue":50.50679194429229,
              "desc":"The latitude of the center of the farm in decimal format."
            },
            {
              "name":"Email",
              "dataType":"String",
              "dummyValue":"support@farmonaut.com",
              "desc":"The email address associated with the field owner's account."
            },
            {
              "name":"Expiring",
              "dataType":"String",
              "dummyValue":"no",
              "desc":"It tells if the satellite monitoring plan of the field is expiring soon or not. The possible values are 'yes', 'no' or null."
            },
            {
              "name":"FailedDays",
              "dataType":"Map (key-value pairs)",
              "dummyValue":{
                "20200905": "yes",
                "20200925": "yes"
              },
              "valueParams":[
                {
                  "name":"<SatelliteVisitDate>",
                  "dataType":"String",
                  "dummyValue":"yes",
                  "desc":"The value of this Map can be ignored, it's just meant to get the date value from the key."
                }
              ],
              "desc":"The satellite visit dates at which no satellite data was collected due to cloud over the farm. The value is in form of a Map with date as the key and value as 'yes' String."
            },
            {
              "name":"SensedDays",
              "dataType":"Map (key-value pairs)",
              "dummyValue":{
                "20200905": "yes",
                "20200925": "yes"
              },
              "valueParams":[
                {
                  "name":"<SatelliteVisitDate>",
                  "dataType":"String",
                  "dummyValue":"yes",
                  "desc":"The value of this Map can be ignored, it's just meant to get the date value from the key."
                }
              ],
              "desc":"The satellite visit dates of the farm. The value is in form of a Map with date as the key and value as 'yes' String."
            },
            {
              "name":"SARDays",
              "dataType":"Map (key-value pairs)",
              "dummyValue":{
                "20200905": "yes",
                "20200925": "yes"
              },
              "valueParams":[
                {
                  "name":"<RadarVisitDate>",
                  "dataType":"String",
                  "dummyValue":"yes",
                  "desc":"The value of this Map can be ignored, it's just meant to get the date value from the key."
                }
              ],
              "desc":"The dates at which radar data of the farm was collected. The value is in form of a Map with date as the key and value as 'yes' String."
            },
            {
              "name":"FieldAddress",
              "dataType":"String",
              "dummyValue":"Vrutice 85, 411 47 Vrutice, Czechia",
              "desc":"The street address of the field taken from google places API."
            },
            {
              "name":"FieldID",
              "dataType":"String",
              "dummyValue":"1600502365642",
              "desc":"It is an identifier for the the field. It's unique for every field."
            },
            {
              "name":"FieldArea",
              "dataType":"int",
              "dummyValue":396800,
              "desc":"The field area in sq. m."
            },
            {
              "name":"FieldLatLen",
              "dataType":"double",
              "dummyValue":0.016376154108932894,
              "desc":"The different of the max and min latitude of the field."
            },
            {
              "name":"FieldLatLenLarge",
              "dataType":"double",
              "dummyValue":0.016376154108932894,
              "desc":"The different of the max and min latitude of the field."
            },
            {
              "name":"FieldLongLen",
              "dataType":"double",
              "dummyValue":0.025749206542965197,
              "desc":"The different of the max and min longitude of the field."
            },
            {
              "name":"FieldLongLenLarge",
              "dataType":"double",
              "dummyValue":0.025749206542965197,
              "desc":"The different of the max and min longitude of the field."
            },
            {
              "name":"FieldMaxLat",
              "dataType":"double",
              "dummyValue":50.510218206844385,
              "desc":"The maximum latitude of the field."
            },
            {
              "name":"FieldMaxLong",
              "dataType":"double",
              "dummyValue":14.286727673381936,
              "desc":"The maximum longitude of the field."
            },
            {
              "name":"FieldMinLat",
              "dataType":"double",
              "dummyValue":50.510218206844385,
              "desc":"The minimum latitude of the field."
            },
            {
              "name":"FieldMinLong",
              "dataType":"double",
              "dummyValue":14.286727673381936,
              "desc":"The minimum longitude of the field."
            },
            {
              "name":"GenTif",
              "dataType":"String",
              "dummyValue":"yes",
              "desc":"Tells if the genTif image creation is enabled or not. The possible values are 'yes', 'no' or null."
            },
            {
              "name":"hUnits",
              "dataType":"int",
              "dummyValue":119,
              "desc":"The number of hectare units utilized for this field. Know more about hectare unit by usage chart section.🔗",
              "references":["hectareUnits"]
            },
            {
              "name":"Health",
              "dataType":"Map (key-value pairs)",
              "dummyValue":{
                "ndvi":{
                  "20200912": "60",
                  "20200917": "41"
                }
              },
              "valueParams":[
                {
                  "name":"<ImageType>",
                  "dataType":"Map (key-value pairs)",
                  "dummyValue":{
                    "20200912": "60",
                    "20200917": "41"
                  },
                  "valueParams":[
                    {
                      "name":"<SatelliteVisitDate>",
                      "dataType":"String",
                      "dummyValue":"46",
                      "desc":"The health value or the average index value of the image of the given satellite visit date. (range from 0 to 100)"
                    }
                  ],
                  "desc":"The health values by image type and satellite visit date."
                }
              ],
              "desc":"Health tells average value of indexes of different image types at different satellite visits."
            },
            {
              "name":"Yield",
              "dataType":"Map (key-value pairs)",
              "dummyValue":{
                "20200912": "30",
                "20200917": "21"
              },
              "valueParams":[
                {
                  "name":"<SatelliteVisitDate>",
                  "dataType":"String",
                  "dummyValue":"46",
                  "desc":"The yeild estimate value at the satellite visit date for the field. The value is in tonnes."
                }
              ],
              "desc":"The yield estimation values at different satellite visit date for the field. The yeild value in tonnes."
            },
            {
              "name":"Name",
              "dataType":"String",
              "dummyValue":"Farmonaut Support",
              "desc":"The name associated with the field owner's account."
            },
            {
              "name":"OrderDate",
              "dataType":"String",
              "dummyValue":"19-September-2020",
              "desc":"The date of farm submission or the first monitoring order date."
            },
            {
              "name":"Paid",
              "dataType":"String",
              "dummyValue":"Yes",
              "desc":"Is the payment done for the current order. The possible values are 'Yes', 'No' or null."
            },
            {
              "name":"PaymentType",
              "dataType":"String",
              "dummyValue":"6",
              "desc":"The satellite monitoring plan choosen in the last order. The possible values are 1, 3, 6 and 12; representing the plan duration in months."
            },
            {
              "name":"UID",
              "dataType":"String",
              "dummyValue":"BpkwnSJdwHTjKhdm8ZWKJBO1HUn2",
              "desc":"Also referred as API ID at some places. It's basically an identifier for your account."
            },
            {
              "name":"Weather-",
              "dataType":"Map (key-value pairs)",
              "dummyValue":{
                "20201028": {
                  "cloud_cover": 100,
                  "humidity": 79,
                  "max_temp": 283.71,
                  "min_temp": 274.82,
                  "pressure": 1014,
                  "station": "Polepy",
                  "wind_deg": 90,
                  "wind_speed": 0.89
                }
              },
              "valueParams":[
                {
                  "name":"<SatelliteVisitDate>",
                  "dataType":"Map (key-value pairs)",
                  "dummyValue":{
                    "cloud_cover": 100,
                    "humidity": 79,
                    "max_temp": 283.71,
                    "min_temp": 274.82,
                    "pressure": 1014,
                    "station": "Polepy",
                    "wind_deg": 90,
                    "wind_speed": 0.89
                  },
                  "valueParams":[
                    {
                      "name": "station",
                      "dataType": "String",
                      "dummyValue": "Hoskote",
                      "desc": "Weather station city name"
                    },
                    {
                      "name": "min_temp",
                      "dataType": "double",
                      "dummyValue": 280.37,
                      "desc": " Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit is Kelvin."
                    },
                    {
                      "name": "max_temp",
                      "dataType": "double",
                      "dummyValue": 284.26,
                      "desc": "Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit is Kelvin."
                    },
                    {
                      "name": "pressure",
                      "dataType": "int",
                      "dummyValue": 1023,
                      "desc": "Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa"
                    },
                    {
                      "name": "humidity",
                      "dataType": "int",
                      "dummyValue": 86,
                      "desc": "Humidity in %"
                    },
                    {
                      "name": "wind_speed",
                      "dataType": "double",
                      "dummyValue": 1.5,
                      "desc": "Wind speed. Unit int meter/sec."
                    },
                    {
                      "name": "wind_deg",
                      "dataType": "int",
                      "dummyValue": 350,
                      "desc": "Wind direction, degrees (meteorological)"
                    },
                    {
                      "name": "cloud_cover",
                      "dataType": "int",
                      "dummyValue": 90,
                      "desc": "Cloudiness in %"
                    }
                  ],
                  "desc":"The weather data at the specified satellite visit date."
                }
              ],
              "desc":"The weather data at different satellite visit dates."
            }
          ],
        "desc": "It's a map of all the data of a single field with key as that field's ID."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get My API Usage Data",
    "desc": "It returns accounts API usage data like purchased units, remaining units etc",
    "endpoint": "/getMyUsage",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "{n}_Month",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "6_Month": {
            "TotalArea":265.2,
            "TotalFields":139,
            "TotalUnitsExhausted":1025,
          },
        },
        "valueParams":[
          {
            "name": "TotalArea",
            "dataType": "double",
            "dummyValue": 256.2,
            "desc": "Cumulative area of all the fields with 'n'-months monitoring plan, till date.",
          },
          {
            "name": "TotatFields",
            "dataType": "int",
            "dummyValue": 139,
            "desc": "Total no of fields that opted for 'n'-months monitoring plan, till date.",
          },
          {
            "name": "TotalUnitsExhaused",
            "dataType": "int",
            "dummyValue": 1025,
            "desc": "Cumulative units exhausted by all the fields that opted for 'n'-months monitoring plan, till date.",
          }
        ],
        "desc": "It tells the data of fields with 'n'-months monitoring plan, till date.",
      },
      {
        "name": "IndividualUsage-",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "IndividualUsage":{
            "1585473801632":{
              "NumberOfMonths":"30",
              "FieldArea":2652000
            },
            "1588826147771":{
              "NumberOfMonths":"300",
              "FieldArea":683400
            },
          },
        },
        "valueParams":[
          {
            "name": "{FieldID}",
            "dataType": "Map (key-value pairs)",
            "dummyValue": {
              "1588826147771":{
                "NumberOfMonths":"300",
                "FieldArea":683400
              },
            },
            "valueParams":[
              {
                "name":"NumberOfMonths",
                "dataType":"String",
                "dummyValue":"300",
                "desc":"The total no of months of monitoring plan selected for the field, till date.",
              },
              {
                "name":"FieldArea",
                "dataType":"int",
                "dummyValue":257,
                "desc":"The field area in sq. m.",
              },
            ],
            "desc": "It gives usage per individual field.",
          },
        ],
        "desc": "Cumulative units exhausted by all the fields that opted for 'n'-months monitoring plan, till date.",
      },
      {
        "name":"Usage-",
        "dataType":"Map (key-value pairs)",
        "dummyValue":{
          "OrderedUnits":3500,
          "Orders":{
            "1665811437427":{
                "PhoneNo":"+91535",
                "RazorOrderID":"order_KTviWMTEPMxdJk",
                "TimeStamp":1665811437427,
                "UID":"BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
                "Units":1000
            },
            "1666761854030":{
                "PhoneNo":"+932",
                "RazorOrderID":"7A601844SR7207448",
                "TimeStamp":1666761854030,
                "UID":"MBFshQgimkS6AwSDtqAyOpRXZW12",
                "Units":1000
            }
          },
          "UsedUnits":1021,
          "WeatherRequests":542,
          "remainingUnits":2479
        },
        "valueParams":[
          {
            "name":"OrderedUnits",
            "dataType":"int",
            "dummyValue":3500,
            "desc":"The total no of hectare units purchased.",
            "references":["hectareUnits"],
          },
          {
            "name":"UsedUnits",
            "dataType":"int",
            "dummyValue":1021,
            "desc":"The total no of hectare units used.",
          },
          {
            "name":"Orders-",
            "dataType":"Map (key-value pairs)",
            "dummyValue":{
              "1666761854030":{
                  "PhoneNo":"+932",
                  "RazorOrderID":"7A601844SR7207448",
                  "TimeStamp":1666761854030,
                  "UID":"MBFshQgimkS6AwSDtqAyOpRXZW12",
                  "Units":1000,
              },
            },
            "valueParams":[
              {
                "name":"{orderID}",
                "dataType":"Map (key-value pairs)",
                "dummyValue":{
                  "PhoneNo":"+932546220011",
                  "RazorOrderID":"7A601844SR7207448",
                  "TimeStamp":1666761854030,
                  "UID":"MBFshQgimkS6AwSDtqAyOpRXZW12",
                  "Units":1000,
                },
                "valueParams":[
                  {
                    "name":"PhoneNo",
                    "dataType":"String",
                    "dummyValue":"+932546220011",
                    "desc":"The contact no given in the order.",
                  },
                  {
                    "name":"RazorOrderId",
                    "dataType":"String",
                    "dummyValue":"7A601844SR7207448",
                    "desc":"The payment gateway order ID.",
                  },
                  {
                    "name":"TimeStamp",
                    "dataType":"int",
                    "dummyValue":1666761854030,
                    "desc":"The timestamp at the order time.",
                  },
                  {
                    "name":"UID",
                    "dataType": "String",
                    "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
                    "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
                  },
                  {
                    "name":"Units",
                    "dataType":"int",
                    "dummyValue":1000,
                    "desc":"The no of units purchased.",
                  },                  
                ],
                "desc":"Units purchase order details.",
              },  
            ],
            "desc":"Details of all the units purchase orders.",
          },
          {
            "name":"WeatherRequests",
            "dataType":"int",
            "dummyValue":542,
            "desc":"The no of units utilised in weather data APIs.",
          },
          {
            "name":"remainingUnits",
            "dataType":"int",
            "dummyValue":2479,
            "desc":"The no of hectare units remaining in the account. Basically ordered units - used units.",
          },
        ],
        "desc":"Other Account Usage Data.",
      },
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Field Satellite Image By Image Type",
    "desc": "It returns a URL for the requested field satellite image for provided image type, color map and sensed date.",
    "endpoint": "/getFieldImage",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      },
      {
        "name": "ImageType",
        "dataType": "String",
        "dummyValue": "ndvi",
        "desc": "The image type of the image. The supported values can be found here.🔗",
        "isOptional": False,
        "references": ["imageTypeList"]
      },
      {
        "name": "SensedDay",
        "dataType": "String",
        "dummyValue": "20201025",
        "desc": "The date of satellite visit for which image is needed. The valid dates can be found in the 'SensedDays' parameter of the field data.",
        "isOptional": False
      },
      {
        "name": "Colormap",
        "dataType": "String",
        "dummyValue": "1",
        "desc": "The color-map for the image. Two values are supported- '1' used for good height vegetation, '2' used for small height vegetation. Colormap 2 is not available for TCI, ETCI, Hybrid, ColorBlind and Evapotranspiration images. See more about color-maps here. 🔗",
        "isOptional": False,
        "references": ["colorMaps"]
      }
    ],
    "response": [
      {
        "name": "url",
        "dataType": "String",
        "dummyValue": "https://lh3.googleusercontent.com/a/AATXAJxBJj0R9t3rka5q6kU40XhuXtg5ObhC8sbXPQ0f=s96-c",
        "desc": "The URL of the requested image."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Field Image Linegraph",
    "desc": "It returns a URL for the linegraph image of the requested field image. Linegraph is a graph showing average value of the image parameter over the field, for the last 7 satellite visits.",
    "endpoint": "/getFieldImageLinegraph",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      },
      {
        "name": "ImageType",
        "dataType": "String",
        "dummyValue": "ndvi",
        "desc": "The image type of the image. The supported values can be found here.🔗",
        "isOptional": False
      },
      {
        "name": "SensedDay",
        "dataType": "String",
        "dummyValue": "20201025",
        "desc": "The date of satellite visit for which image is needed.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "url",
        "dataType": "String",
        "dummyValue": "https://lh3.googleusercontent.com/a/AATXAJxBJj0R9t3rka5q6kU40XhuXtg5ObhC8sbXPQ0f=s96-c",
        "desc": "The URL of the requested image."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Field Area Index Image",
    "desc": "It returns a URL for the area index image of the requested field image. Area Index value tells the area which has a particular index value.",
    "endpoint": "/getFieldIndexAreaImage",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      },
      {
        "name": "ImageType",
        "dataType": "String",
        "dummyValue": "ndvi",
        "desc": "The image type of the image. The supported values can be found here.🔗",
        "isOptional": False
      },
      {
        "name": "SensedDay",
        "dataType": "String",
        "dummyValue": "20201025",
        "desc": "The date of satellite visit for which image is needed.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "url",
        "dataType": "String",
        "dummyValue": "https://lh3.googleusercontent.com/a/AATXAJxBJj0R9t3rka5q6kU40XhuXtg5ObhC8sbXPQ0f=s96-c",
        "desc": "The URL of the requested image."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Pause Satellite Monitoring for a field",
    "desc": "It can be used to pause satellite monitoring for any field. User may use the remaining service units at any later time at the same field.",
    "endpoint": "/pauseFieldMonitoring",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      }
    ],
    "response": {
      "dataType": "String",
      "successValue": "Field Monitoring Paused"
    },
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Resume Satellite Monitoring for a field",
    "desc": "It can be used to resume satellite monitoring for any field. The system would start generating satellite data from next satellite on the farm, till service plan exhausts for the field.",
    "endpoint": "/resumeFieldMonitoring",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      }
    ],
    "response": {
      "dataType": "String",
      "successValue": "Field Monitoring Resumed"
    },
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Change Field Crop Code",
    "desc": "It can be used to change the field's crop-code. Should be used if new crop is being cultivated at any field.",
    "endpoint": "/updateCropCode",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      },
      {
        "name": "CropCode",
        "dataType": "String",
        "dummyValue": "1r",
        "desc": "Crop code for the crop being cultivated at the farm. You can find the codes to use for various crops here. 🔗",
        "isOptional": False,
        "references": ["cropCodesList"]
      }
    ],
    "response": {
      "dataType": "String",
      "successValue": "Request submitted. New yield estimates will be available from the next satellite visit."
    },
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Yield Estimates of a Field",
    "desc": "It returns the yield estimate in tonnes for the field.",
    "endpoint": "/getYieldEstimates",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "<SatelliteVisitDate>",
        "dataType": "Map (key-value pairs)",
        "valueParams": [
          {
            "name": "Yield",
            "dummyValue": "5",
            "dataType": "int",
            "desc": "The yeild value in tonnes."
          }
        ],
        "desc": "The yeild estimate comes in map format with key as date of satellite visit. The yeild value in tonnes."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Request Historical Satellite Data",
    "desc": "It is used request satellite data from date before the start satellite service for any field. Eg. if the user submitted the farm on 15 June 2021 and wants data for date before 15th, say 5th June 2021, then can use this endpoint to request data for 5th June.",
    "endpoint": "/requestPreviousSatelliteData",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      },
      {
        "name": "RequestedDate",
        "dataType": "String",
        "dummyValue": "20210505",
        "desc": "The historical date for which satellite image is needed.",
        "isOptional": False
      }
    ],
    "response": {
      "dataType": "String",
      "successValue": "Request submitted. Data will be available within 15 mins. Please check the SensedDays Key for confirmation in 15 mins."
    },
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Sensed Days",
    "desc": "It returns the list all the dates of satellite visit or dates for which satellite data is available, of the farm.",
    "endpoint": "/getSensedDays",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "SensedDays",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "20200912": "yes",
          "20200917": "yes"
        },
        "valueParams": [
          {
            "name": "<SatelliteVisitDate>",
            "dataType": "String",
            "dummyValue": "yes",
            "desc": "The key is the date of satellite visit and the value is 'yes'."
          }
        ],
        "desc": "The satellite visit dates are provided as a Map with key as the date and value as 'yes'."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get SAR (Synthetic Aperture Radar) Days",
    "desc": "It returns the list all the dates for which radar data is available, of the farm.",
    "endpoint": "/getSARDays",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "SARDays",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "20200912": "yes",
          "20200917": "yes"
        },
        "valueParams": [
          {
            "name": "<RadarVisitDate>",
            "dataType": "String",
            "dummyValue": "yes",
            "desc": "The key is the date of radar visit and the value is 'yes'."
          }
        ],
        "desc": "The radar visit dates are provided as a Map with key as the date and value as 'yes'."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Change Language of Field Report",
    "desc": "Use it to change the language of field report of any field (multi-languages are supported). After change of language, the subsequent reports will be generated in those languages.",
    "endpoint": "/setReportLanguage",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      },
      {
        "name": "Language",
        "dataType": "List",
        "dummyValue": ["en", "hi"],
        "desc": "It should be list ISO 2 letter language codes. Currently supported languages are Hindi (hi), English (en), Bengali (bn), Punjabi (pa), Marathi (mr), Tamil (ta), Telugu (te), Arabic (ar) and Uzbek (uz)",
        "isOptional": False
      }
    ],
    "response": {
      "dataType": "String",
      "successValue": "Language Set"
    },
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Field Report",
    "desc": "It returns a url of the PDF report for any satellite visit.",
    "endpoint": "/getFieldReport",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      },
      {
        "name": "SensedDay",
        "dataType": "String",
        "dummyValue": "20201025",
        "desc": "The date of satellite visit for which image is needed. The valid dates can be found in the 'SensedDays' parameter of the field data.",
        "isOptional": False
      },
      {
        "name": "ReportFormat",
        "dataType": "String",
        "dummyValue": "PDF",
        "desc": "This has only one value for now i.e. 'PDF'.",
        "isOptional": False
      },
      {
        "name": "Language",
        "dataType": "String",
        "dummyValue": "en",
        "desc": "The code for the language of report, default is 'en'.",
        "isOptional": True,
        "references": ["langCodesList"]
      }
    ],
    "response": [
      {
        "name": "url",
        "dataType": "String",
        "dummyValue": "https://lh3.googleusercontent.com/a/AATXAJxBJj0R9t3rka5q6kU40XhuXtg5ObhC8sbXPQ0f=s96-c",
        "desc": "The URL of the requested report."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Weather Graph By Date",
    "desc": "It returns a URL for the selected sensed date weather graph. Weather graph image consists of linegraph data for 5 parameters, namely Min./Max. Temperature, cloud-cover, humidity, pressure, wind-speed; for last 7 satellite visits.",
    "endpoint": "/getPastWeatherGraph",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      },
      {
        "name": "SensedDay",
        "dataType": "String",
        "dummyValue": "20201025",
        "desc": "The date of satellite visit for which image is needed. The valid dates can be found in the 'SensedDays' parameter of the field data.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "url",
        "dataType": "String",
        "dummyValue": "https://lh3.googleusercontent.com/a/AATXAJxBJj0R9t3rka5q6kU40XhuXtg5ObhC8sbXPQ0f=s96-c",
        "desc": "The URL of the requested image."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Weather Forecast Data",
    "desc": "It returns weather forecast data of next 7 days for the field.",
    "endpoint": "/getForecastWeather",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "longitude",
        "dataType": "double",
        "dummyValue": 14.2744310003,
        "desc": "The longitude of the weather station in decimal format."
      },
      {
        "name": "latitude",
        "dataType": "double",
        "dummyValue": 50.508256707,
        "desc": "The latitude of the weather station in decimal format."
      },
      {
        "name": "timezone",
        "dataType": "String",
        "dummyValue": "Asia/Kolkata",
        "desc": "The name of the timezone"
      },
      {
        "name": "offset",
        "dataType": "double",
        "dummyValue": 5.5,
        "desc": "The timezone offset of the station location in hours."
      },
      {
        "name": "daily-",
        "dataType": "Map (key-value pairs)",
        "desc": "It has the map containing all the forecast data.",
        "valueParams": [
          {
            "name": "summary",
            "dataType": "String",
            "dummyValue": "Rain on Monday through next Wednesday.",
            "desc": "The overall forecast summary in one line."
          },
          {
            "name": "icon",
            "dataType": "String",
            "dummyValue": "rain",
            "desc": "Weather icon ID"
          },
          {
            "name": "data-",
            "dataType": "Map (key-value pairs)",
            "desc": "The forecast data Map with day-no in key and weather data in value. The day-no gives as 0, 1 upto 7 with 0 as today, 1 as next day and so on.",
            "valueParams": [
              {
                "name": "<DataDayNo>",
                "desc": "Weather forecast data for the day-no. The day-no gives as 0, 1 upto 7 with 0 as today, 1 as next day and so on.",
                "dataType": "Map (key-value pairs)",
                "dummyValue": {
                  "time": 1668537000,
                  "summary": "Partly cloudy throughout the day.",
                  "icon": "partly-cloudy-day",
                  "sunriseTime": 1668559740,
                  "sunsetTime": 1668601260,
                  "moonPhase": 0.75,
                  "precipIntensity": 0.0005,
                  "precipIntensityMax": 0.0033,
                  "precipIntensityMaxTime": 1668537000,
                  "precipProbability": 0.19,
                  "precipType": "rain",
                  "temperatureHigh": 78.96,
                  "temperatureHighTime": 1668585780,
                  "temperatureLow": 55.01,
                  "temperatureLowTime": 1668639960,
                  "apparentTemperatureHigh": 78.83,
                  "apparentTemperatureHighTime": 1668583860,
                  "apparentTemperatureLow": 55.5,
                  "apparentTemperatureLowTime": 1668639960,
                  "dewPoint": 61.96,
                  "humidity": 0.76,
                  "pressure": 1013.6,
                  "windSpeed": 6.13,
                  "windGust": 16.34,
                  "windGustTime": 1668605820,
                  "windBearing": 50,
                  "cloudCover": 0.6,
                  "uvIndex": 7,
                  "uvIndexTime": 1668579240,
                  "visibility": 10,
                  "ozone": 266,
                  "temperatureMin": 60.8,
                  "temperatureMinTime": 1668552480,
                  "temperatureMax": 78.96,
                  "temperatureMaxTime": 1668585780,
                  "apparentTemperatureMin": 62.14,
                  "apparentTemperatureMinTime": 1668552540,
                  "apparentTemperatureMax": 78.83,
                  "apparentTemperatureMaxTime": 1668583860
                },
                "valueParams": [
                  {
                    "name": "time",
                    "dataType": "int",
                    "dummyValue": 1668553200,
                    "desc": "The time of weather data capture in timestamp format."
                  },
                  {
                    "name": "summary",
                    "dataType": "String",
                    "dummyValue": "Light rain starting in the afternoon",
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "icon",
                    "dataType": "String",
                    "dummyValue": "rain",
                    "desc": "Weather icon ID"
                  },
                  {
                    "name": "sunriseTime",
                    "dataType": "int",
                    "dummyValue": 1668559740,
                    "desc": "The sunrise time at weather station in timestamp format."
                  },
                  {
                    "name": "sunsetTime",
                    "dataType": "int",
                    "dummyValue": 1668559740,
                    "desc": "The sunset time at weather station in timestamp format."
                  },
                  {
                    "name": "moonPhase",
                    "dataType": "double",
                    "dummyValue": 0.76,
                    "desc": "Moon phase. 0 and 1 are 'new moon', 0.25 is 'first quarter moon', 0.5 is 'full moon' and 0.75 is 'last quarter moon'. The periods in between are called 'waxing crescent', 'waxing gibous', 'waning gibous', and 'waning crescent', respectively."
                  },
                  {
                    "name": "precipIntensity",
                    "dataType": "double",
                    "dummyValue": 0.0066,
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "precipIntensityMax",
                    "dataType": "double",
                    "dummyValue": 0.0196,
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "precipIntensityMaxTime",
                    "dataType": "double",
                    "dummyValue": 1668537000,
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "precipProbability",
                    "dataType": "double",
                    "dummyValue": 0.88,
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "precipType",
                    "dataType": "String",
                    "dummyValue": "rain",
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "temperatureHigh",
                    "dataType": "double",
                    "dummyValue": 52.29,
                    "desc": "The max temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "temperatureHighTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of max temperature in the day."
                  },
                  {
                    "name": "temperatureLow",
                    "dataType": "double",
                    "dummyValue": 39.59,
                    "desc": "The min temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "temperatureLowTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of min temperature in the day."
                  },
                  {
                    "name": "apparentTemperatureHigh",
                    "dataType": "double",
                    "dummyValue": 51.79,
                    "desc": "The human perception max temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "apparentTemperatureHighTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of apparent max temperature in the day."
                  },
                  {
                    "name": "apparentTemperatureLow",
                    "dataType": "double",
                    "dummyValue": 35.63,
                    "desc": "The human perception min temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "apparentTemperatureLowTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of apparent min temperature in the day."
                  },
                  {
                    "name": "dewPoint",
                    "dataType": "double",
                    "dummyValue": 40.17,
                    "desc": "The current dew point at the location."
                  },
                  {
                    "name": "humidity",
                    "dataType": "double",
                    "dummyValue": 0.87,
                    "desc": "The current humidity ratio at the location."
                  },
                  {
                    "name": "pressure",
                    "dataType": "double",
                    "dummyValue": 1007.4,
                    "desc": "The current barometric pressure at the location."
                  },
                  {
                    "name": "windSpeed",
                    "dataType": "double",
                    "dummyValue": 2.1,
                    "desc": "The current wind speed in m/s at the location."
                  },
                  {
                    "name": "windGust",
                    "dataType": "double",
                    "dummyValue": 8.2,
                    "desc": "The current wind gust in m/s at the location."
                  },
                  {
                    "name": "windGustTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of wind gust data capture."
                  },
                  {
                    "name": "windBearing",
                    "dataType": "int",
                    "dummyValue": 67,
                    "desc": "The current wind bearing (in degrees) at the location."
                  },
                  {
                    "name": "cloudCover",
                    "dataType": "double",
                    "dummyValue": 0.93,
                    "desc": "Current cloud cover probability ratio."
                  },
                  {
                    "name": "uvIndex",
                    "dataType": "int",
                    "dummyValue": 1,
                    "desc": "The current UV index"
                  },
                  {
                    "name": "uvIndexTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The UV index data capture time"
                  },
                  {
                    "name": "visibility",
                    "dataType": "int",
                    "dummyValue": 10,
                    "desc": "Average visibility, metres. The maximum value of the visibility is 10km."
                  },
                  {
                    "name": "ozone",
                    "dataType": "int",
                    "dummyValue": 279,
                    "desc": "The current ozone value at the location. Unit is dobson unit."
                  },
                  {
                    "name": "temperatureMax",
                    "dataType": "double",
                    "dummyValue": 52.29,
                    "desc": "The max temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "temperatureMaxTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of max temperature in the day."
                  },
                  {
                    "name": "temperatureMin",
                    "dataType": "double",
                    "dummyValue": 39.59,
                    "desc": "The min temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "temperatureMinTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of min temperature in the day."
                  },
                  {
                    "name": "apparentTemperatureMax",
                    "dataType": "double",
                    "dummyValue": 51.79,
                    "desc": "The human perception max temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "apparentTemperatureMaxTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of apparent max temperature in the day."
                  },
                  {
                    "name": "apparentTemperatureMin",
                    "dataType": "double",
                    "dummyValue": 35.63,
                    "desc": "The human perception min temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "apparentTemperatureMinTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of apparent min temperature in the day."
                  }
                ]
              }
            ]
          }
        ]
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Latest Weather Data",
    "desc": "It returns latest weather data for the field.",
    "endpoint": "/getPresentWeatherData",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "coord",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "lon": 14.2744310003,
          "lat": 50.508256707
        },
        "valueParams": [
          {
            "name": "lon",
            "dataType": "double",
            "dummyValue": 14.2744310003,
            "desc": "The longitude of the location in decimal format."
          },
          {
            "name": "lat",
            "dataType": "double",
            "dummyValue": 50.508256707,
            "desc": "The latitude of the location in decimal format."
          }
        ],
        "desc": "The coordinates of the nearest weather station."
      },
      {
        "name": "base",
        "dataType": "String",
        "dummyValue": "stations",
        "desc": "Internal parameter"
      },
      {
        "name": "dt",
        "dataType": "int",
        "dummyValue": 1560350645,
        "desc": "Time of data calculation, unix, UTC"
      },
      {
        "name": "timezone",
        "dataType": "int",
        "dummyValue": -25200,
        "desc": "Shift in seconds from UTC"
      },
      {
        "name": "name",
        "dataType": "String",
        "dummyValue": "Mountain View",
        "desc": "City name"
      },
      {
        "name": "id",
        "dataType": "int",
        "dummyValue": 420006353,
        "desc": "City ID"
      },
      {
        "name": "cod",
        "dataType": "int",
        "dummyValue": 200,
        "desc": "Internal parameter"
      },
      {
        "name": "weather-",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01d"
        },
        "valueParams": [
          {
            "name": "id",
            "dataType": "int",
            "dummyValue": 800,
            "desc": "Weather condition ID"
          },
          {
            "name": "main",
            "dataType": "String",
            "dummyValue": "Clear",
            "desc": "Group of weather parameters (Rain, Snow, Extreme etc.)"
          },
          {
            "name": "description",
            "dataType": "String",
            "dummyValue": "clear sky",
            "desc": "Weather condition within the group."
          },
          {
            "name": "icon",
            "dataType": "String",
            "dummyValue": "01d",
            "desc": "Weather icon ID"
          }
        ],
        "desc": "Weather Summary with condition codes"
      },
      {
        "name": "main-",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "temp": 282.55,
          "feels_like": 281.86,
          "temp_min": 280.37,
          "temp_max": 284.26,
          "pressure": 1023,
          "humidity": 100
        },
        "valueParams": [
          {
            "name": "temp",
            "dataType": "double",
            "dummyValue": 282.55,
            "desc": "Temperature in Kelvin."
          },
          {
            "name": "feels_like",
            "dataType": "double",
            "dummyValue": 281.86,
            "desc": "Temperature. This temperature parameter accounts for the human perception of weather. Unit is Kelvin."
          },
          {
            "name": "temp_min",
            "dataType": "double",
            "dummyValue": 280.37,
            "desc": " Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit is Kelvin."
          },
          {
            "name": "temp_max",
            "dataType": "double",
            "dummyValue": 284.26,
            "desc": "Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit is Kelvin."
          },
          {
            "name": "pressure",
            "dataType": "int",
            "dummyValue": 1023,
            "desc": "Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa"
          },
          {
            "name": "humidity",
            "dataType": "int",
            "dummyValue": 100,
            "desc": "Humidity in %"
          }
        ],
        "desc": "Main/primary weather parameters in Map datatype."
      },
      {
        "name": "wind-",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "speed": 1.5,
          "deg": 350
        },
        "valueParams": [
          {
            "name": "speed",
            "dataType": "double",
            "dummyValue": 1.5,
            "desc": "Wind speed. Unit int meter/sec."
          },
          {
            "name": "deg",
            "dataType": "int",
            "dummyValue": 350,
            "desc": "Wind direction, degrees (meteorological)"
          }
        ],
        "desc": "The wind speed and direction values."
      },
      {
        "name": "clouds-",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "all": 1
        },
        "valueParams": [
          {
            "name": "all",
            "dataType": "int",
            "dummyValue": 1,
            "desc": "Cloudiness in %"
          }
        ],
        "desc": "Cloudiness in %"
      },
      {
        "name": "sys-",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "type": 1,
          "id": 5122,
          "message": 0.0139,
          "country": "US",
          "sunrise": 1560343627,
          "sunset": 1560396563
        },
        "valueParams": [
          {
            "name": "type",
            "dataType": "int",
            "dummyValue": 1,
            "desc": "Internal parameter"
          },
          {
            "name": "id",
            "dataType": "int",
            "dummyValue": 5122,
            "desc": "Internal parameter"
          },
          {
            "name": "message",
            "dataType": "double",
            "dummyValue": 0.0139,
            "desc": "Internal parameter"
          },
          {
            "name": "country",
            "dataType": "String",
            "dummyValue": "US",
            "desc": "Country 2 letter code like IN, US etc."
          },
          {
            "name": "sunrise",
            "dataType": "int",
            "dummyValue": 1560343627,
            "desc": "Sunrise time, unix, UTC"
          },
          {
            "name": "sunset",
            "dataType": "int",
            "dummyValue": 1560396563,
            "desc": "Sunset time, unix, UTC"
          }
        ],
        "desc": "Some system data"
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Past Weather Data",
    "desc": "It returns weather data for last requested no of days if available.",
    "endpoint": "/getHistoricalFieldWeather",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "FieldID",
        "dataType": "String",
        "dummyValue": "1668483626232",
        "desc": "It is an identifier for the the field. It's unique for every field.",
        "isOptional": False
      },
      {
        "name": "NumberOfDays",
        "dataType": "int",
        "dummyValue": 20,
        "desc": "The number of days of weather data needed, before current day.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "<WeatherDataDate>",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "cloud_cover": 40,
          "humidity": 83,
          "max_temp": 300.22,
          "min_temp": 294.33,
          "pressure": 1020,
          "station": "Hoskote",
          "wind_deg": 50,
          "wind_speed": 2.57
        },
        "valueParams": [
          {
            "name": "station",
            "dataType": "String",
            "dummyValue": "Hoskote",
            "desc": "Weather station city name"
          },
          {
            "name": "min_temp",
            "dataType": "double",
            "dummyValue": 280.37,
            "desc": " Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit is Kelvin."
          },
          {
            "name": "max_temp",
            "dataType": "double",
            "dummyValue": 284.26,
            "desc": "Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit is Kelvin."
          },
          {
            "name": "pressure",
            "dataType": "int",
            "dummyValue": 1023,
            "desc": "Atmospheric pressure (on the sea level, if there is no sea_level or grnd_level data), hPa"
          },
          {
            "name": "humidity",
            "dataType": "int",
            "dummyValue": 86,
            "desc": "Humidity in %"
          },
          {
            "name": "wind_speed",
            "dataType": "double",
            "dummyValue": 1.5,
            "desc": "Wind speed. Unit int meter/sec."
          },
          {
            "name": "wind_deg",
            "dataType": "int",
            "dummyValue": 350,
            "desc": "Wind direction, degrees (meteorological)"
          },
          {
            "name": "cloud_cover",
            "dataType": "int",
            "dummyValue": 90,
            "desc": "Cloudiness in %"
          }
        ],
        "desc": "The weather data for available days in Map datatype with date in key and all weather data in value."
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Weather Forecast Data By Latitude & Longitude",
    "desc": "It provides weather forecast from the nearest weather station from given latitude and longitude. The service is available for any latitude or longitude, across the globe.",
    "endpoint": "/getForecastWeatherFromLatLong",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "Latitude",
        "dataType": "String",
        "dummyValue": "50.5082567070",
        "desc": "The latitude of the location in decimal format.",
        "isOptional": False
      },
      {
        "name": "Longitude",
        "dataType": "String",
        "dummyValue": "14.2744310003",
        "desc": "The longitude of the location in decimal format.",
        "isOptional": False
      }
    ],
    "response": [
      {
        "name": "longitude",
        "dataType": "double",
        "dummyValue": 14.2744310003,
        "desc": "The longitude of the weather station in decimal format."
      },
      {
        "name": "latitude",
        "dataType": "double",
        "dummyValue": 50.508256707,
        "desc": "The latitude of the weather station in decimal format."
      },
      {
        "name": "timezone",
        "dataType": "String",
        "dummyValue": "Asia/Kolkata",
        "desc": "The name of the timezone"
      },
      {
        "name": "offset",
        "dataType": "double",
        "dummyValue": 5.5,
        "desc": "The timezone offset of the station location in hours."
      },
      {
        "name": "daily-",
        "dataType": "Map (key-value pairs)",
        "desc": "It has the map containing all the forecast data.",
        "valueParams": [
          {
            "name": "summary",
            "dataType": "String",
            "dummyValue": "Rain on Monday through next Wednesday.",
            "desc": "The overall forecast summary in one line."
          },
          {
            "name": "icon",
            "dataType": "String",
            "dummyValue": "rain",
            "desc": "Weather icon ID"
          },
          {
            "name": "data-",
            "dataType": "Map (key-value pairs)",
            "desc": "The forecast data Map with day-no in key and weather data in value. The day-no gives as 0, 1 upto 7 with 0 as today, 1 as next day and so on.",
            "valueParams": [
              {
                "name": "<DataDayNo>",
                "desc": "Weather forecast data for the day-no. The day-no gives as 0, 1 upto 7 with 0 as today, 1 as next day and so on.",
                "dataType": "Map (key-value pairs)",
                "dummyValue": {
                  "time": 1668537000,
                  "summary": "Partly cloudy throughout the day.",
                  "icon": "partly-cloudy-day",
                  "sunriseTime": 1668559740,
                  "sunsetTime": 1668601260,
                  "moonPhase": 0.75,
                  "precipIntensity": 0.0005,
                  "precipIntensityMax": 0.0033,
                  "precipIntensityMaxTime": 1668537000,
                  "precipProbability": 0.19,
                  "precipType": "rain",
                  "temperatureHigh": 78.96,
                  "temperatureHighTime": 1668585780,
                  "temperatureLow": 55.01,
                  "temperatureLowTime": 1668639960,
                  "apparentTemperatureHigh": 78.83,
                  "apparentTemperatureHighTime": 1668583860,
                  "apparentTemperatureLow": 55.5,
                  "apparentTemperatureLowTime": 1668639960,
                  "dewPoint": 61.96,
                  "humidity": 0.76,
                  "pressure": 1013.6,
                  "windSpeed": 6.13,
                  "windGust": 16.34,
                  "windGustTime": 1668605820,
                  "windBearing": 50,
                  "cloudCover": 0.6,
                  "uvIndex": 7,
                  "uvIndexTime": 1668579240,
                  "visibility": 10,
                  "ozone": 266,
                  "temperatureMin": 60.8,
                  "temperatureMinTime": 1668552480,
                  "temperatureMax": 78.96,
                  "temperatureMaxTime": 1668585780,
                  "apparentTemperatureMin": 62.14,
                  "apparentTemperatureMinTime": 1668552540,
                  "apparentTemperatureMax": 78.83,
                  "apparentTemperatureMaxTime": 1668583860
                },
                "valueParams": [
                  {
                    "name": "time",
                    "dataType": "int",
                    "dummyValue": 1668553200,
                    "desc": "The time of weather data capture in timestamp format."
                  },
                  {
                    "name": "summary",
                    "dataType": "String",
                    "dummyValue": "Light rain starting in the afternoon",
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "icon",
                    "dataType": "String",
                    "dummyValue": "rain",
                    "desc": "Weather icon ID"
                  },
                  {
                    "name": "sunriseTime",
                    "dataType": "int",
                    "dummyValue": 1668559740,
                    "desc": "The sunrise time at weather station in timestamp format."
                  },
                  {
                    "name": "sunsetTime",
                    "dataType": "int",
                    "dummyValue": 1668559740,
                    "desc": "The sunset time at weather station in timestamp format."
                  },
                  {
                    "name": "moonPhase",
                    "dataType": "double",
                    "dummyValue": 0.76,
                    "desc": "Moon phase. 0 and 1 are 'new moon', 0.25 is 'first quarter moon', 0.5 is 'full moon' and 0.75 is 'last quarter moon'. The periods in between are called 'waxing crescent', 'waxing gibous', 'waning gibous', and 'waning crescent', respectively."
                  },
                  {
                    "name": "precipIntensity",
                    "dataType": "double",
                    "dummyValue": 0.0066,
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "precipIntensityMax",
                    "dataType": "double",
                    "dummyValue": 0.0196,
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "precipIntensityMaxTime",
                    "dataType": "double",
                    "dummyValue": 1668537000,
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "precipProbability",
                    "dataType": "double",
                    "dummyValue": 0.88,
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "precipType",
                    "dataType": "String",
                    "dummyValue": "rain",
                    "desc": "The overall forecast summary in one line."
                  },
                  {
                    "name": "temperatureHigh",
                    "dataType": "double",
                    "dummyValue": 52.29,
                    "desc": "The max temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "temperatureHighTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of max temperature in the day."
                  },
                  {
                    "name": "temperatureLow",
                    "dataType": "double",
                    "dummyValue": 39.59,
                    "desc": "The min temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "temperatureLowTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of min temperature in the day."
                  },
                  {
                    "name": "apparentTemperatureHigh",
                    "dataType": "double",
                    "dummyValue": 51.79,
                    "desc": "The human perception max temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "apparentTemperatureHighTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of apparent max temperature in the day."
                  },
                  {
                    "name": "apparentTemperatureLow",
                    "dataType": "double",
                    "dummyValue": 35.63,
                    "desc": "The human perception min temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "apparentTemperatureLowTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of apparent min temperature in the day."
                  },
                  {
                    "name": "dewPoint",
                    "dataType": "double",
                    "dummyValue": 40.17,
                    "desc": "The current dew point at the location."
                  },
                  {
                    "name": "humidity",
                    "dataType": "double",
                    "dummyValue": 0.87,
                    "desc": "The current humidity ratio at the location."
                  },
                  {
                    "name": "pressure",
                    "dataType": "double",
                    "dummyValue": 1007.4,
                    "desc": "The current barometric pressure at the location."
                  },
                  {
                    "name": "windSpeed",
                    "dataType": "double",
                    "dummyValue": 2.1,
                    "desc": "The current wind speed in m/s at the location."
                  },
                  {
                    "name": "windGust",
                    "dataType": "double",
                    "dummyValue": 8.2,
                    "desc": "The current wind gust in m/s at the location."
                  },
                  {
                    "name": "windGustTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of wind gust data capture."
                  },
                  {
                    "name": "windBearing",
                    "dataType": "int",
                    "dummyValue": 67,
                    "desc": "The current wind bearing (in degrees) at the location."
                  },
                  {
                    "name": "cloudCover",
                    "dataType": "double",
                    "dummyValue": 0.93,
                    "desc": "Current cloud cover probability ratio."
                  },
                  {
                    "name": "uvIndex",
                    "dataType": "int",
                    "dummyValue": 1,
                    "desc": "The current UV index"
                  },
                  {
                    "name": "uvIndexTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The UV index data capture time"
                  },
                  {
                    "name": "visibility",
                    "dataType": "int",
                    "dummyValue": 10,
                    "desc": "Average visibility, metres. The maximum value of the visibility is 10km."
                  },
                  {
                    "name": "ozone",
                    "dataType": "int",
                    "dummyValue": 279,
                    "desc": "The current ozone value at the location. Unit is dobson unit."
                  },
                  {
                    "name": "temperatureMax",
                    "dataType": "double",
                    "dummyValue": 52.29,
                    "desc": "The max temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "temperatureMaxTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of max temperature in the day."
                  },
                  {
                    "name": "temperatureMin",
                    "dataType": "double",
                    "dummyValue": 39.59,
                    "desc": "The min temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "temperatureMinTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of min temperature in the day."
                  },
                  {
                    "name": "apparentTemperatureMax",
                    "dataType": "double",
                    "dummyValue": 51.79,
                    "desc": "The human perception max temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "apparentTemperatureMaxTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of apparent max temperature in the day."
                  },
                  {
                    "name": "apparentTemperatureMin",
                    "dataType": "double",
                    "dummyValue": 35.63,
                    "desc": "The human perception min temperature in the day. Unit is Fahrenheit."
                  },
                  {
                    "name": "apparentTemperatureMinTime",
                    "dataType": "int",
                    "dummyValue": 1668537000,
                    "desc": "The time of occurance of apparent min temperature in the day."
                  }
                ]
              }
            ]
          }
        ]
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  },
  {
    "name": "Get Crop Solution Database",
    "desc": "It returns a list diseases of the crop and solutions to it with dose values in a Map datatype format.",
    "endpoint": "/getDatabase",
    "isDeprecated": False,
    "body": [
      {
        "name": "UID",
        "dataType": "String",
        "dummyValue": "BpkwnSJdwHTjKhdm8ZWKJBO6HUn5",
        "desc": "Also referred as API ID at some places. It's basically an identifier for your account.",
        "isOptional": False
      },
      {
        "name": "Crop",
        "dataType": "String",
        "dummyValue": "apple",
        "desc": "The full name of the crop that need to be requested, in lower case. The supported values/crops can be found here. 🔗",
        "isOptional": False,
        "references": ["cropCodesList"]
      }
    ],
    "response": [
      {
        "name": "<DiseaseName>",
        "dataType": "Map (key-value pairs)",
        "dummyValue": {
          "downy leaf spot": {
            "captan 75% wp": {
              "formulation": "3 gm",
              "dilution": "10 per tree",
              "ai_gm": "1.5 gm"
            }
          },
        },
        "valueParams": [
          {
            "name": "formulation",
            "desc": "The type of formulation of the solution to use. The solution might be available in different formulations in the market.",
            "dataType": "String",
            "dummyValue": "3 gm"
          },
          {
            "name": "dilution",
            "desc": "The dilution to be used with 1L water.",
            "dataType": "String",
            "dummyValue": "10 per tree"
          },
          {
            "name": "ai_gm",
            "desc": "The Quantity to be used.",
            "dataType": "String",
            "dummyValue": "1.5 gm"
          }
        ],
        "desc": "The disease and solution data is returned in Map datatype with disease as key and solutions as value.",
      }
    ],
    "sampleCodes": {},
    "errors": {
      # TODO
      "type": "Map", # means {errorDescription: errorID}
      "value": {
        "keyName": "errorDescription",
        "values": [
          {
            "name": "invalid points format",
            "desc": "Please send boundary points in clock-wise/counter-clock-wise order with keys as 'a' for first point, 'P_1' for second point, 'P_2' for third point and so on.\nSo if you have 4 points, use keys as 'a', 'P_1', 'P_2' and 'P_3'."
          },
          {
            "name": "Invalid Payment Type",
            "desc": "Please send 'Payment Type' value as 1, 3, 6 or 12"
          },
          {
            "name": "invalid crop code",
            "desc": "Crop code value should be from the values specified in this table. 🔗",
            "references": ["cropCodesList"]
          },
          {
            "name": "invalid UID",
            "desc": "Please use the UID/API key you got after buying API credits. You check it at 'https://farmonaut.com/api'."
          }
        ]
      }
    }
  }
]

# language codes
allLangs = {
  "jv": {
    "EnglishName": "Javanese",
    "LangName": "basa jawa"
  },
  "he": {"EnglishName": "Hebrew", "LangName": "עִברִית"},
  "af": {
    "EnglishName": "Afrikaans",
    "LangName": "Afrikaans"
  },
  "am": {"EnglishName": "Amharic", "LangName": "አማርኛ"},
  "ar": {"EnglishName": "Arabic", "LangName": "عربي"},
  "hy": {"EnglishName": "Armenian", "LangName": "հայերեն"},
  "az": {
    "EnglishName": "Azerbaijani",
    "LangName": "Azərbaycan"
  },
  "eu": {"EnglishName": "Basque", "LangName": "euskara"},
  "bn": {"EnglishName": "Bengali", "LangName": "বাংলা"},
  "bg": {
    "EnglishName": "Bulgarian",
    "LangName": "български"
  },
  "km": {
    "EnglishName": "Cambodian",
    "LangName": "កម្ពុជា។"
  },
  "ca": {"EnglishName": "Catalan", "LangName": "català"},
  "zh": {"EnglishName": "Chinese", "LangName": "中国人"},
  "zh-TW": {
    "EnglishName": 'Chinese (Traditional)',
    "LangName": '中文（傳統的）'
  },
  "hr": {"EnglishName": "Croatian", "LangName": "Hrvatski"},
  "cs": {"EnglishName": "Czech", "LangName": "čeština"},
  "da": {"EnglishName": "Danish", "LangName": "dansk"},
  "nl": {"EnglishName": "Dutch", "LangName": "Nederlands"},
  "en": {"EnglishName": "English", "LangName": "English"},
  "fi": {
    "EnglishName": "Finnish",
    "LangName": "Suomalainen"
  },
  "fr": {"EnglishName": "French", "LangName": "Français"},
  "gl": {"EnglishName": "Galician", "LangName": "galego"},
  "ka": {"EnglishName": "Georgian", "LangName": "ქართული"},
  "el": {"EnglishName": "Greek", "LangName": "Ελληνικά"},
  "gu": {"EnglishName": "Gujarati", "LangName": "ગુજરાતી"},
  "hi": {"EnglishName": "Hindi", "LangName": "हिन्दी"},
  "hu": {"EnglishName": "Hungarian", "LangName": "Magyar"},
  "is": {
    "EnglishName": "Icelandic",
    "LangName": "íslenskur"
  },
  "id": {
    "EnglishName": "Indonesian",
    "LangName": "bahasa Indonesia"
  },
  "it": {"EnglishName": "Italian", "LangName": "Italiano"},
  "ja": {"EnglishName": "Japanese", "LangName": "日本"},
  "kn": {"EnglishName": "Kannada", "LangName": "ಕನ್ನಡ"},
  "ko": {"EnglishName": "Korean", "LangName": "한국인"},
  "lo": {"EnglishName": "Laothian", "LangName": "Laothian"},
  "lv": {"EnglishName": "Latvian", "LangName": "latviski"},
  "lt": {
    "EnglishName": "Lithuanian",
    "LangName": "lietuvių"
  },
  "ml": {"EnglishName": "Malayalam", "LangName": "മലയാളം"},
  "mr": {"EnglishName": "Marathi", "LangName": "मराठी"},
  "ne": {"EnglishName": "Nepali", "LangName": "नेपाली"},
  "no": {"EnglishName": "Norwegian", "LangName": "norsk"},
  "fa": {"EnglishName": "Persian", "LangName": "فارسی"},
  "pl": {"EnglishName": "Polish", "LangName": "Polski"},
  "pt": {
    "EnglishName": "Portuguese",
    "LangName": "Português"
  },
  "pa": {"EnglishName": "Punjabi", "LangName": "ਪੰਜਾਬੀ"},
  "ro": {"EnglishName": "Romanian", "LangName": "Română"},
  "ru": {"EnglishName": "Russian", "LangName": "Русский"},
  "sr": {"EnglishName": "Serbian", "LangName": "Српски"},
  "si": {"EnglishName": "Sinhalese", "LangName": "සිංහල"},
  "sk": {"EnglishName": "Slovak", "LangName": "slovenský"},
  "es": {"EnglishName": "Spanish", "LangName": "español"},
  "su": {
    "EnglishName": "Sundanese",
    "LangName": "basa Sunda"
  },
  "sw": {"EnglishName": "Swahili", "LangName": "kiswahili"},
  "sv": {"EnglishName": "Swedish", "LangName": "svenska"},
  "ta": {"EnglishName": "Tamil", "LangName": "தமிழ்"},
  "te": {"EnglishName": "Telugu", "LangName": "తెలుగు"},
  "th": {"EnglishName": "Thai", "LangName": "ไทย"},
  "tr": {"EnglishName": "Turkish", "LangName": "Türk"},
  "uk": {
    "EnglishName": "Ukrainian",
    "LangName": "українська"
  },
  "ur": {"EnglishName": "Urdu", "LangName": "اردو"},
  "zu": {"EnglishName": "Zulu", "LangName": "Zulu"}
}

# crop codes
cropCodes = {
  "Rice (Kharif)": "1k",
  "Rice (Rabi)": "1r",
  "Wheat": "2r",
  "Coarse Cereals (Kharif)": "3k",
  "Coarse Cereals (Rabi)": "3r",
  "Jowar (Kharif)": "4k",
  "Jowar (Rabi)": "4r",
  "Bajra (Kharif)": "5k",
  "Maize (Kharif)": "6k",
  "Maize (Rabi)": "6r",
  "Pulse (Kharif)": "7k",
  "Pulse (Rabi)": "7r",
  "Gram (Rabi)": "8r",
  "Tur (Kharif)": "9k",
  "Rapeseed and Mustard (Rabi)": "10r",
  "Soyabean (Kharif)": "11k",
  "Sunflower": "12",
  "Sugarcane": "13",
  "Cotton": "14",
  "Jute and Mesta": "15",
  "Potato": "16",
  "Onion": "17",
  "Coconut": "18",
  "Tobacco": "19",
  "Groundnut": "20",
  "Turmeric": "21",
  "Corn": "22",
  "Chili": "23",
  "Other": "999"
}

# image types
satImgTypes = {
  "NDVI": "ndvi",
  "NDWI": "ndwi",
  "EVAPO": "evapo",
  "NDMI": "ndmi",
  "EVI": "evi",
  "RVI": "rvi",
  "RSM": "rsm",
  "NDRE": "ndre",
  "VARI": "vari",
  "SAVI": "savi",
  "AVI": "avi",
  "BSI": "bsi",
  "SI": "si",
  "SOC": "soc",
  "TCI": "tci",
  "ETCI": "etci",
  "HYBRID": "hybrid",
  "COLORBLIND": "hybrid_blind",
  "DEM": "dem",
  "LULC": "lulc"
}

endpointBase = "https://us-central1-farmbase-b2f7e.cloudfunctions.net"
def createSampleCodeForSingleEndpoint(data):
  # import 'dart:async';
  # import 'dart:convert';
  # import 'dart:io';
  # import 'package:http/http.dart' as http;
  # 
  # Future postRequest () async {
  # var url ='https://us-central1-farmbase-b2f7e.cloudfunctions.net/getForecastWeather';
  
  # Map farmObj = {
  # 'UID': 'BpkwnSJdwHTjKhdm8ZWKJBO1HUn2',
  # 'FieldID': '1600503072436'
  # }
  # //encode Map to JSON
  # var body = json.encode(farmObj);
  
  # var response = await http.post(url,
  # headers: {"Content-Type": "application/json"},
  # body: body
  # );
  # print("${response.statusCode}");
  # print("${response.body}");
  # return response;
  # }
  bodyCodeStr = (getBodyCodeStr(data["body"], "    ") or "")
  bodyCodeStr2 = (getBodyCodeStr(data["body"], "    ", True) or "")

  dartCode = '''import 'dart:convert' show json;
import 'package:http/http.dart' as http;

Future postRequest () async {
  const endpointUrl = '%s%s';
    
  final bodyMap = {
%s  };

  final response = await http.post(
    endpointUrl,
    headers : {'Content-Type': 'application/json'},
    body: json.encode(bodyMap),
  );

  print(response.statusCode);
  print(response.body);
  return response;
}''' % (endpointBase, data["endpoint"], bodyCodeStr)

  pythonCode = '''import requests

endpointUrl = '%s%s'
bodyObj = {
%s}
 
response = requests.post(
  endpointUrl, 
  json = bodyObj
)
 
print("Status code: ", response.status_code)
print("Printing Entire Post Request")
print(response.json())''' % (endpointBase, data["endpoint"], bodyCodeStr)

  swiftCode = '''import Foundation

let url = URL(string: "%s%s")!

// prepare json data
let json: [String: Any] = [
%s] 
let jsonData = try? JSONSerialization.data(withJSONObject: json)
 
// create post request
var request = URLRequest(url: url)
request.httpMethod = "POST"
 
// insert json data to the request
request.httpBody = jsonData
 
let task = URLSession.shared.dataTask(with: request) { (data, response, error) in
  guard let data = data, error == nil else {
    print(error?.localizedDescription ?? "No data")
    return
  }
  let responseJSON = try? JSONSerialization.jsonObject(with: data, options: [])
  if let responseJSON = responseJSON as? [String: Any] {
    print(responseJSON)
  }
}
 
task.resume()''' % (endpointBase, data["endpoint"], bodyCodeStr)

# //farmObj.put("UID", "BpkwnSJdwHTjKhdm8ZWKJBO1HUn2");
# //farmObj.put("FieldID", "1600503072436");
  javaCode = '''OkHttpClient client = new OkHttpClient();

String endpointUrl = "%s%s";

MediaType mediaType = MediaType.parse("application/json");
String value = "{\\r
%s}";
RequestBody body = RequestBody.create(mediaType, value);

Request request = new Request.Builder()
	.url(endpointUrl)
	.post(body)
	.addHeader("content-type", "application/json")
	.build();

Response response = client.newCall(request).execute();''' % (endpointBase, data["endpoint"], bodyCodeStr2)

  kotlinCode = '''val client = OkHttpClient()

val mediaType = MediaType.parse("application/json")
val body = RequestBody.create(mediaType, "{\\r
%s}")
val request = Request.Builder()
	.url("%s%s")
	.post(body)
	.addHeader("content-type", "application/json")
	.build()

val response = client.newCall(request).execute()''' % (bodyCodeStr2, endpointBase, data["endpoint"])

  jsCode = '''const endpointUrl = '%s%s';
const bodyObj = {
%s};
 
const httpRequest = new XMLHttpRequest();
httpRequest.open('POST', endpointUrl,true);
httpRequest.onload = function(){
  let responseData = httpRequest.responseText;
};
httpRequest.send(json.stringify(bodyObj));''' % (endpointBase, data["endpoint"], bodyCodeStr)

  phpCode = '''<?php

$client = new http\Client;
$request = new http\Client\Request;

$body = new http\Message\Body;
$body->append("{
%s}");

$request->setRequestUrl('%s%s');
$request->setRequestMethod('POST');
$request->setBody($body);

$request->setHeaders([
	'content-type' => 'application/json'
]);

$client->enqueue($request)->send();
$response = $client->getResponse();

echo $response->getBody();''' % (bodyCodeStr, endpointBase, data["endpoint"])

  return {"dart":dartCode, "java":javaCode,"kotlin": kotlinCode,"swift": swiftCode,"python": pythonCode,"javascript": jsCode,"php": phpCode}
  sampleCode = "const endpointUrl = '%s%s';\n\nfinal bodyMap = {\n" % (endpointBase, data["endpoint"])
  sampleCode += (getBodyCodeStr(data["body"], "  ") or "")
  codeEnd = "};\n\nfinal response = await http.post(\n  endpointUrl,\n  headers : {'Content-Type': 'application/json'},\n  body: json.encode(bodyMap),\n);\n\nprint(response.statusCode);\nprint(response.body);"
  sampleCode += codeEnd
  return sampleCode
  
def getBodyCodeStr(bodyArgsArray, indentStr, isForOkHttp= False):
  if bodyArgsArray == None:
    return None
  result = ""
  backslashTxt = '\\' if isForOkHttp else ""
  endTxt = '\\r' if isForOkHttp else ""
  for args in bodyArgsArray:
    if args["dataType"] == "Map (key-value pairs)":
      result += "%s%s\"%s%s\" : {%s\n%s%s},%s\n" % (indentStr, backslashTxt, args["name"], backslashTxt, endTxt, getBodyCodeStr(args["valueParams"], indentStr+"  ", isForOkHttp) if "valueParams" in args else getDummyValueCodeStr(args["dummyValue"], indentStr+"  ", isForOkHttp), indentStr, endTxt)
    else:
      result += "%s%s\"%s%s\" : %s\"%s%s\",%s\n" % (indentStr, backslashTxt, args["name"], backslashTxt, backslashTxt, args["dummyValue"], backslashTxt, endTxt)
  return result

def getDummyValueCodeStr(dummyValue, indentStr, isForOkHttp):
  if type(dummyValue) == "dict":
    result = ""
    backslashTxt = '\\' if isForOkHttp else ""
    endTxt = '\\r' if isForOkHttp else ""
    for key,value in dummyValue.items():
      if type(dummyValue) == "dict":
        result += "%s%s\"%s%s\" : {%s\n%s%s},%s\n" % (indentStr, backslashTxt, key, backslashTxt, endTxt, getDummyValueCodeStr(value, indentStr+"  ", isForOkHttp), indentStr, endTxt)
      else:
        result += "%s%s\"%s%s\" : %s\"%s%s\",%s\n" % (indentStr, backslashTxt, key, backslashTxt, backslashTxt, value, backslashTxt, endTxt)
    return result
  else:
    return dummyValue
  
def getNSaveAllSampleCodes():
  allCodes = {}
  for i in range(len(allAPIData)):
    print("starting %s" % i)
    apiData = allAPIData[i]
    sampleCodeGetDB = createSampleCodeForSingleEndpoint(apiData)
    allCodes[apiData["endpoint"][1:]] = sampleCodeGetDB
    # for code in sampleCodeGetDB:
      # print(code)
  
  print(len(allCodes))
  with open("sampleCodes.json", "w", encoding="utf8") as f:
    f.write(str(allCodes))

def sortNSaveAPIData():
  def sortingParamsValue(apiInfo):
    return apiInfo["name"]

  def sortItemList(mList, mapValueName="valueParams"):
    # print(type(mList))
    if type(mList) == list:
      # print("type check done")
      mList.sort(key=sortingParamsValue)
      # print(mList[0]['name'])
      if mapValueName!=None:
        for item in mList:
          if mapValueName in item and item["dataType"] == "Map (key-value pairs)":
            sortItemList(item[mapValueName])
  
  print(len(allAPIData))
  allAPIData.sort(key=sortingParamsValue)
  for apiInfo in allAPIData:
    sortItemList(apiInfo["body"])
    sortItemList(apiInfo["response"])
    if apiInfo["errors"]["type"] == "Map":
      sortItemList(apiInfo['errors']['value']['values'], None)

  print(len(allAPIData))
  # json.dump("api_data.json", allAPIData[0])
  with open("api_data.json", "w", encoding="utf8") as f:
    f.write(json.dumps(allAPIData))

# def replaceHtmlData(elementKey, value, htmlStr, initialIndex):
#     # assuming elements to be none container type
#     # print(startIndex)
#     keyIndex = htmlStr.index(elementKey, initialIndex)
#     startIndex = htmlStr.index(">", keyIndex)
#     endIndex = htmlStr.index("<", startIndex)
#     return htmlStr[:startIndex+1]+value+htmlStr[endIndex:], startIndex+len(value)+1


# def replaceHtmlEleStyle(elementKey, style, htmlStr, initialIndex):
#     # assuming elements to be none container type
#     # print(startIndex)
#     keyIndex = htmlStr.index(elementKey, initialIndex)
#     startIndex = htmlStr.index("style=", keyIndex)
#     endIndex = htmlStr.index('"', startIndex+7)
#     return htmlStr[:startIndex+7]+style+htmlStr[endIndex:], initialIndex


# def replaceHtmlImgSrc(elementKey, src, htmlStr, initialIndex):
#     # assuming element id is added before src parameter in html
#     # and also that some src is already added there
#     keyIndex = htmlStr.index(elementKey, initialIndex)
#     startIndex = htmlStr.index("src", keyIndex)
#     endIndex = htmlStr.index('"', startIndex+5)
#     return htmlStr[:startIndex+5]+src+htmlStr[endIndex:], startIndex+len(src)+1


# def replaceHtmlStyle(className, style, htmlStr, initialIndex):
#     keyIndex = htmlStr.index(className, initialIndex)
#     startIndex = htmlStr.index("{", keyIndex)
#     endIndex = htmlStr.index("}", startIndex+1)
#     return htmlStr[:startIndex+1]+style+htmlStr[endIndex:], startIndex+len(style)+1


# def replaceHtmlComments(htmlStr):
#     pattern = re.compile("\/\*([^\*\/]|\n)*\*\/|<!--.*-->",  re.MULTILINE)
#     return re.sub(pattern, "", htmlStr)



############------------------------------################
# getNSaveAllSampleCodes()
sortNSaveAPIData()
