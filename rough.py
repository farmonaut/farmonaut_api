from matplotlib import pyplot as plt
import requests

raw = '''<tr>
      <td>
        <p><span style="font-weight: 400;">Rice (Kharif)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">1k</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Rice (Rabi)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">1r</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Wheat</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">2r</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Coarse Cereals (Kharif)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">3k</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Coarse Cereals (Rabi)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">3r</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Jowar (Kharif)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">4k</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Jowar (Rabi)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">4r</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Bajra (Kharif)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">5k</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Maize (Kharif)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">6k</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Maize (Rabi)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">6r</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Pulse (Kharif)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">7k</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Pulse (Rabi)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">7r</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Gram (Rabi)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">8r</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Tur (Kharif)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">9k</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Rapeseed and Mustard (Rabi)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">10r</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Soyabean (Kharif)</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">11k</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Sunflower</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">12</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Sugarcane</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">13</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Cotton</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">14</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Jute and Mesta</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">15</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Potato</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">16</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Onion</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">17</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Coconut</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">18</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Tobacco</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">19</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Groundnut</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">20</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Turmeric</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">21</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Corn</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">22</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Chili</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">23</span></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><span style="font-weight: 400;">Other</span></p>
      </td>
      <td>
        <p><span style="font-weight: 400;">999</span></p>
      </td>
    </tr>'''

raw2 = '''<tr>
      <td>NDVI</td>
      <td>ndvi</td>
    </tr>
    <tr>
      <td>NDWI</td>
      <td>ndwi</td>
    </tr>
    <tr>
      <td>EVAPO</td>
      <td>evapo</td>
    </tr>
    <tr>
      <td>NDMI</td>
      <td>ndmi</td>
    </tr>
    <tr>
      <td>EVI</td>
      <td>evi</td>
    </tr>
    <tr>
      <td>RVI</td>
      <td>rvi</td>
    </tr>
    <tr>
      <td>NDRE</td>
      <td>ndre</td>
    </tr>
    <tr>
      <td>VARI</td>
      <td>vari</td>
    </tr>
    <tr>
      <td>SAVI</td>
      <td>savi</td>
    </tr>
    <tr>
      <td>AVI</td>
      <td>avi</td>
    </tr>
    <tr>
      <td>BSI</td>
      <td>bsi</td>
    </tr>
    <tr>
      <td>SI</td>
      <td>si</td>
    </tr>
    <tr>
      <td>SOC</td>
      <td>soc</td>
    </tr>
    <tr>
      <td>TCI</td>
      <td>tci</td>
    </tr>
    <tr>
      <td>ETCI</td>
      <td>etci</td>
    </tr>
    <tr>
      <td>HYBRID</td>
      <td>hybrid</td>
    </tr>
    <tr>
      <td>COLORBLIND</td>
      <td>hybrid_blind</td>
    </tr>
    <tr>
      <td>DEM</td>
      <td>dem</td>
    </tr>'''

rawCoords = "79.01194103184389,86.54814698122209 79.6882152313483,82.98974488227395 78.85500068377587,82.21385715919314 72.73563286988065,80.10919574074796 67.66350614727708,78.30439125813427 62.9510315193329,77.02950961960596 52.97268588343286,75.30769729570602 56.20293913796195,62.82017187072779 59.897152207035106,49.422368386614835 62.251366716081975,40.91546788311098 64.67018616161658,32.342693313315976 66.93654466874432,24.8091227846744 67.6975225515198,23.19476820115233 72.81660658351029,20.787219726393232 77.74843715006136,19.057039848528802 83.22447593795368,17.13410348474281 90.0302055523207,15.261312964605168 95.96266587689752,13.407012256677262 101.62673312588595,11.897250830370467 106.22931799705839,10.35529961794964 110.80089989420958,8.303969195112586 111.5635382537148,7.417424323910382 114.09817540767835,7.285282356897369 124.87137279805029,7.2442154854070395 134.58335034319316,6.3828644904715475 135.8011324708641,17.026816222060006 136.87895867429324,26.62240356442635 137.86642226873664,30.46967207576381 143.107320449315,30.18691303837113 150.43900091559044,29.450247156928526 151.47909634545795,41.04819016752299 152.29015511707985,52.32960744231241 152.72949016097118,61.21236095999484 153.1380962546973,69.73262752589653 152.82051807738026,78.52871636245982 148.86751095837099,79.33636251103599 145.2208092911169,79.88980151576106 138.99617170286365,80.66244603300584 134.35631874611136,81.11472048523137 123.63876609830186,82.36221386189573 116.07931723233196,83.41541298222728 113.0157463660289,84.08165594842285 111.18221889503184,85.83791841374477 109.35947257533553,87.05698240720085 106.80694560654229,88.08657321339706 103.67486371658742,87.98374591089669 93.70746755591244,87.29693661848432 83.73341351380805,86.87054453749442 79.01194103184389,86.54814698122209"

def pre():
  rows = raw2.split("</tr>")[:-1]

  print(len(rows))
  resultObj = {}

  for row in rows:
    keyIndex = row.index("<td")
    keyEndIndex = row.index("<", keyIndex+1)
    print(keyIndex, keyEndIndex)
    key = row[keyIndex+4:keyEndIndex]
    valueIndex = row.index("<td", keyEndIndex)
    valueEndIndex = row.index("<", valueIndex+1)
    value = row[valueIndex+4:valueEndIndex]
    resultObj[key] = value
    
  with open("cropCodes.json", "w", encoding= "utf8") as f:
    f.write(str(resultObj))

def plotRawPoints():
  pointStrs = rawCoords.split(" ")
  pointsList = []
  maxLat = -180
  maxLong = -180
  minLat = 180
  minLong = 180

  for i in range(len(pointStrs)):
    pointStr = pointStrs[i]
    coords = pointStr.split(",")
    x = float(coords[0])
    y = float(coords[1])
    pointsList.append({"x":x, "y":y})
    # Plotting
    plt.plot(x,y,'bo')

    if x>maxLat: 
      maxLat = x
    if y>maxLong: 
      maxLong = y
    if y<minLat: 
      minLat = y
    if y<minLong: 
      minLong = y


  # print(pointsList)

  # Displaying grid
  plt.grid()

  # Controlling axis
  plt.axis([minLat-2, maxLat+2, minLong-2, maxLong+2])

  # Adding title
  plt.title('Raw Points Plot')

  # Displaying plot
  plt.show()

def plotRandomPoints():
  points = [{'x':1, 'y':1},{'x':2, 'y':1},{'x':2, 'y':2},{'x':1, 'y':2},]
  print(points)

  for point in points:
    #  Plotting
    plt.plot(point['x'],point['y'],'bo')


  # Displaying grid
  plt.grid()

  # Controlling axis
  plt.axis([-8, 8, -8, 8])

  # Adding title
  plt.title('Raw Points Plot')

  # Displaying plot
  plt.show()

def getTransMap():
  keys = ["north",
"east",
"west",
"south",
"ceNter",]
  
  results = []
  for values in [ar, bn, te, kn, mr, hi, ta, uz]:
    result = {}
    for i in range(len(keys)):
      result[keys[i]] = values[i]

    results.append(result)
  with open("cropCodes.json", "w", encoding="utf8") as f:
    f.write(str(results))

ta= ["வடக்கு",
"கிழக்கு",
"மேற்கு",
"தெற்கு",
"மையம்",]
uz=["shimol",
"sharq",
"g'arbiy",
"janubiy",
"markaz",]
hi=["उत्तर",
"पूर्व",
"पश्चिम",
"दक्षिण",
"केंद्र",]
mr = ["उत्तर",
"पूर्व",
"पश्चिम",
"दक्षिण",
"मध्यभागी",]
ar =["شمال",
"الشرق",
"الغرب" ,
"جنوب",
"المركز" ,]
bn =["উত্তর",
"পূর্ব",
"পশ্চিম",
"দক্ষিণ",
"কেন্দ্র",]
te = ["ఉత్తర",
"తూర్పు",
"పశ్చిమ",
"దక్షిణం",
"కేంద్రం",]
kn = ["ಉತ್ತರ",
"ಪೂರ್ವ",
"ಪಶ್ಚಿಮ",
"ದಕ್ಷಿಣ",
"ಕೇಂದ್ರ",]

# getTransMap()

# plotRandomPoints()
# plotRawPoints()

def checkAPI():
  endpointUrl = 'https://us-central1-farmbase-b2f7e.cloudfunctions.net/getMyUsage'
  bodyObj = {
      "UID" : "MBFshQgimkS6AwSDtqAyOpRXZW12",}
  
  response = requests.post(
    endpointUrl, 
    json = bodyObj
  )
  
  print("Status code: ", response.status_code)
  print("Printing Entire Post Request")
  print(response.json()["Usage"])

# checkAPI()