from importio import *
import logging, json, io

# To use an API key for authentication, use the following code:
client = importio.importio(user_id="2f655b7b-e35e-478a-abb6-d190a99335ac", api_key="JjzCdj7jXY5L8cpgemKkR8ICAFy2kx3abpWWCXH8MKDdLX5BpTDGvLkNOCCMkScQPHh2yCWh0z7W2eeOXaaJGw==", host="https://query.import.io")

# Once we have started the client and authenticated, we need to connect it to the server:
client.connect()

# Because import.io queries are asynchronous, for this simple script we will use a "latch"
# to stop the script from exiting before all of our queries are returned
# For more information on the latch class, see the latch.py file included in this client library
queryLatch = latch.latch(1)

# Define here a global variable that we can put all our results in to when they come back from
# the server, so we can use the data later on in the script
dataRows = []

# In order to receive the data from the queries we issue, we need to define a callback method
# This method will receive each message that comes back from the queries, and we can take that
# data and store it for use in our app
def callback(query, message):
  global dataRows
  
  # Disconnect messages happen if we disconnect the client library while a query is in progress
  if message["type"] == "DISCONNECT":
    print "Query in progress when library disconnected"
    print json.dumps(message["data"], indent = 4)

  # Check the message we receive actually has some data in it
  if message["type"] == "MESSAGE":
    if "errorType" in message["data"]:
      # In this case, we received a message, but it was an error from the external service
      print "Got an error!" 
      print json.dumps(message["data"], indent = 4)
    else:
      # We got a message and it was not an error, so we can process the data
      print "Got data!"
      # print json.dumps(message["data"], indent = 4)
      # Save the data we got in our dataRows variable for later
      dataRows.extend(message["data"]["results"])
  
  # When the query is finished, countdown the latch so the program can continue when everything is done
  if query.finished(): queryLatch.countdown()

urls = ["http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+gravitational+wave&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=2001+Mars+Odyssey+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=ATHENA+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=ATHENA+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=ATHENA+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Cassini+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Chandra+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Chandra+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Deep+Impact+%28EPOXI%29+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Deep+Impact+%28EPOXI%29+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Euclid+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Euclid+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gaia+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gaia+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gaia+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gaia+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gaia+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gpm+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Gpm+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=GRAIL+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+gravitational+wave&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=HERSCHEL+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Hubble+Space+Telescope+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Hubble+Space+Telescope+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Hubble+Space+Telescope+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Huygens+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Huygens+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Huygens+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Integral+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Integral+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=JUICE+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Juno+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Juno+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Juno+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Juno+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LISA+gravitational+wave&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LISA+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LISA+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LISA+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LOFT+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LOFT+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LOFT+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=LOFT+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+2020+Rover+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+2020+Rover+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+2020+Rover+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+2020+Rover+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Express+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Mars+Global+Surveyor+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MAVEN+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MAVEN+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MAVEN+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MESSENGER+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MESSENGER+gravitational+wave&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MESSENGER+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MESSENGER+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=MESSENGER+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Nasa+Fermi+GLAST+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=New+Horizons+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=New+Horizons+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=New+Horizons+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=New+Horizons+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Nustar+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Nustar+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Nustar+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+gravitational+wave&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Rosetta+x-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Solar-Orbiter+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Solar-Orbiter+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STE-QUEST+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STE-QUEST+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STE-QUEST+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STEREO+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STEREO+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STEREO+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=STEREO+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=THEMIS+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=TRMM+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=TRMM+microwaves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=TRMM+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Van_Allen+RBSP+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Van_Allen+RBSP+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Venus+Express+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Venus+Express+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Venus+Express+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Venus+Express+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Venus+Express+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+1+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+infrared+spectrum&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+magnetic+fields&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+particles&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+plasma&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+radio+waves&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+ultraviolet&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=Voyager+2+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=WISE+%28NEOWISE%29+visible+light+optical&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=XMM-Newton+gamma-rays&commit=Search",
        "http://nasasearch.nasa.gov/search?affiliate=nasa&query=XMM-Newton+x-rays&commit=Search"]

for url in urls:

  # Issue queries to your data sources and with your inputs
  # You can modify the inputs and connectorGuids so as to query your own sources
  # Query for tile Esa LD-XML
  client.query({
    "connectorGuids": [
      "82bb077d-ad3e-491b-95e5-6915cfd78fed"
    ],
    "input": {
      "webpage/url": url
    }
  }, callback)

  print "Queries dispatched, now waiting for results"

  # Now we have issued all of the queries, we can "await" on the latch so that we know when it is all done
  queryLatch.await()

  print "Latch has completed, all results returned"

  # It is best practice to disconnect when you are finished sending queries and getting data - it allows us to
  # clean up resources on the client and the server
  client.disconnect()

  # Now we can print out the data we got
  print "All data received"
  #print json.dumps(dataRows, indent = 4)

  #out_file = open(url[55:-14] + ".txt","w")
  #out_file.write(json.dumps(dataRows, indent = 4).replace("link/_text", "title").replace("detail", "abstract"))
  #out_file.close()
  with io.open(url[55:-14] + ".txt","w", encoding='utf-8') as out_file:
    out_file.write(unicode(json.dumps(dataRows, ensure_ascii=False, indent = 4)).replace("link/_text", "title").replace("detail", "abstract"))
  out_file.close()