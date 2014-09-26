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

urls = ["http://www.esa.int/esasearch?q=2001+Mars+Odyssey+gamma-rays",
        "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+gravitational+wave",
        "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+infrared+spectrum",
        "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+magnetic+fields",
        "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+microwaves",
        "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+particles",
        "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+radio+waves",
        "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+ultraviolet",
        "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+visible+light+optical",
        "http://www.esa.int/esasearch?q=2001+Mars+Odyssey+x-rays",
        "http://www.esa.int/esasearch?q=ATHENA+gamma-rays",
        "http://www.esa.int/esasearch?q=ATHENA+visible+light+optical",
        "http://www.esa.int/esasearch?q=ATHENA+x-rays",
        "http://www.esa.int/esasearch?q=Cassini+gamma-rays",
        "http://www.esa.int/esasearch?q=Cassini+infrared+spectrum",
        "http://www.esa.int/esasearch?q=Cassini+particles",
        "http://www.esa.int/esasearch?q=Cassini+plasma",
        "http://www.esa.int/esasearch?q=Cassini+ultraviolet",
        "http://www.esa.int/esasearch?q=Cassini+visible+light+optical",
        "http://www.esa.int/esasearch?q=Chandra+visible+light+optical",
        "http://www.esa.int/esasearch?q=Chandra+x-rays",
        "http://www.esa.int/esasearch?q=Deep+Impact+%28EPOXI%29+infrared+spectrum",
        "http://www.esa.int/esasearch?q=Deep+Impact+%28EPOXI%29+visible+light+optical",
        "http://www.esa.int/esasearch?q=Euclid+infrared+spectrum",
        "http://www.esa.int/esasearch?q=Euclid+visible+light+optical",
        "http://www.esa.int/esasearch?q=Gaia+infrared+spectrum",
        "http://www.esa.int/esasearch?q=Gaia+radio+waves",
        "http://www.esa.int/esasearch?q=Gaia+ultraviolet",
        "http://www.esa.int/esasearch?q=Gaia+visible+light+optical",
        "http://www.esa.int/esasearch?q=Gaia+x-rays",
        "http://www.esa.int/esasearch?q=Gpm+microwaves",
        "http://www.esa.int/esasearch?q=Gpm+radio+waves",
        "http://www.esa.int/esasearch?q=GRAIL+radio+waves",
        "http://www.esa.int/esasearch?q=HERSCHEL+gamma-rays",
        "http://www.esa.int/esasearch?q=HERSCHEL+gravitational+wave",
        "http://www.esa.int/esasearch?q=HERSCHEL+infrared+spectrum",
        "http://www.esa.int/esasearch?q=HERSCHEL+magnetic+fields",
        "http://www.esa.int/esasearch?q=HERSCHEL+microwaves",
        "http://www.esa.int/esasearch?q=HERSCHEL+particles",
        "http://www.esa.int/esasearch?q=HERSCHEL+plasma",
        "http://www.esa.int/esasearch?q=HERSCHEL+radio+waves",
        "http://www.esa.int/esasearch?q=HERSCHEL+ultraviolet",
        "http://www.esa.int/esasearch?q=HERSCHEL+visible+light+optical",
        "http://www.esa.int/esasearch?q=HERSCHEL+x-rays",
        "http://www.esa.int/esasearch?q=Hubble+Space+Telescope+infrared+spectrum",
        "http://www.esa.int/esasearch?q=Hubble+Space+Telescope+ultraviolet",
        "http://www.esa.int/esasearch?q=Hubble+Space+Telescope+visible+light+optical",
        "http://www.esa.int/esasearch?q=Huygens+particles",
        "http://www.esa.int/esasearch?q=Huygens+plasma",
        "http://www.esa.int/esasearch?q=Huygens+ultraviolet",
        "http://www.esa.int/esasearch?q=Integral+gamma-rays",
        "http://www.esa.int/esasearch?q=Integral+x-rays",
        "http://www.esa.int/esasearch?q=JUICE+infrared+spectrum",
        "http://www.esa.int/esasearch?q=JUICE+magnetic+fields",
        "http://www.esa.int/esasearch?q=JUICE+microwaves",
        "http://www.esa.int/esasearch?q=JUICE+particles",
        "http://www.esa.int/esasearch?q=JUICE+plasma",
        "http://www.esa.int/esasearch?q=JUICE+radio+waves",
        "http://www.esa.int/esasearch?q=JUICE+ultraviolet",
        "http://www.esa.int/esasearch?q=JUICE+visible+light+optical",
        "http://www.esa.int/esasearch?q=JUICE+x-rays",
        "http://www.esa.int/esasearch?q=Juno+magnetic+fields",
        "http://www.esa.int/esasearch?q=Juno+microwaves",
        "http://www.esa.int/esasearch?q=Juno+ultraviolet",
        "http://www.esa.int/esasearch?q=Juno+visible+light+optical",
        "http://www.esa.int/esasearch?q=LISA+gravitational+wave",
        "http://www.esa.int/esasearch?q=LISA+infrared+spectrum",
        "http://www.esa.int/esasearch?q=LISA+microwaves",
        "http://www.esa.int/esasearch?q=LISA+x-rays",
        "http://www.esa.int/esasearch?q=LOFT+magnetic+fields",
        "http://www.esa.int/esasearch?q=LOFT+particles",
        "http://www.esa.int/esasearch?q=LOFT+visible+light+optical",
        "http://www.esa.int/esasearch?q=LOFT+x-rays",
        "http://www.esa.int/esasearch?q=Mars+2020+Rover+radio+waves",
        "http://www.esa.int/esasearch?q=Mars+2020+Rover+ultraviolet",
        "http://www.esa.int/esasearch?q=Mars+2020+Rover+visible+light+optical",
        "http://www.esa.int/esasearch?q=Mars+2020+Rover+x-rays",
        "http://www.esa.int/esasearch?q=Mars+Express+infrared+spectrum",
        "http://www.esa.int/esasearch?q=Mars+Express+particles",
        "http://www.esa.int/esasearch?q=Mars+Express+plasma",
        "http://www.esa.int/esasearch?q=Mars+Express+radio+waves",
        "http://www.esa.int/esasearch?q=Mars+Express+ultraviolet",
        "http://www.esa.int/esasearch?q=Mars+Express+visible+light+optical",
        "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+gamma-rays",
        "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+infrared+spectrum",
        "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+magnetic+fields",
        "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+particles",
        "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+radio+waves",
        "http://www.esa.int/esasearch?q=Mars+Global+Surveyor+visible+light+optical",
        "http://www.esa.int/esasearch?q=MAVEN+particles",
        "http://www.esa.int/esasearch?q=MAVEN+plasma",
        "http://www.esa.int/esasearch?q=MAVEN+ultraviolet",
        "http://www.esa.int/esasearch?q=MESSENGER+gamma-rays",
        "http://www.esa.int/esasearch?q=MESSENGER+gravitational+wave",
        "http://www.esa.int/esasearch?q=MESSENGER+magnetic+fields",
        "http://www.esa.int/esasearch?q=MESSENGER+radio+waves",
        "http://www.esa.int/esasearch?q=MESSENGER+x-rays",
        "http://www.esa.int/esasearch?q=Nasa+Fermi+GLAST+gamma-rays",
        "http://www.esa.int/esasearch?q=New+Horizons+infrared+spectrum",
        "http://www.esa.int/esasearch?q=New+Horizons+radio+waves",
        "http://www.esa.int/esasearch?q=New+Horizons+ultraviolet",
        "http://www.esa.int/esasearch?q=New+Horizons+visible+light+optical",
        "http://www.esa.int/esasearch?q=Nustar+radio+waves",
        "http://www.esa.int/esasearch?q=Nustar+visible+light+optical",
        "http://www.esa.int/esasearch?q=Nustar+x-rays",
        "http://www.esa.int/esasearch?q=Rosetta+gamma-rays",
        "http://www.esa.int/esasearch?q=Rosetta+gravitational+wave",
        "http://www.esa.int/esasearch?q=Rosetta+infrared+spectrum",
        "http://www.esa.int/esasearch?q=Rosetta+magnetic+fields",
        "http://www.esa.int/esasearch?q=Rosetta+microwaves",
        "http://www.esa.int/esasearch?q=Rosetta+particles",
        "http://www.esa.int/esasearch?q=Rosetta+plasma",
        "http://www.esa.int/esasearch?q=Rosetta+radio+waves",
        "http://www.esa.int/esasearch?q=Rosetta+ultraviolet",
        "http://www.esa.int/esasearch?q=Rosetta+visible+light+optical",
        "http://www.esa.int/esasearch?q=Rosetta+x-rays",
        "http://www.esa.int/esasearch?q=Solar-Orbiter+particles",
        "http://www.esa.int/esasearch?q=Solar-Orbiter+plasma",
        "http://www.esa.int/esasearch?q=STE-QUEST+microwaves",
        "http://www.esa.int/esasearch?q=STE-QUEST+radio+waves",
        "http://www.esa.int/esasearch?q=STE-QUEST+visible+light+optical",
        "http://www.esa.int/esasearch?q=STEREO+plasma",
        "http://www.esa.int/esasearch?q=STEREO+radio+waves",
        "http://www.esa.int/esasearch?q=STEREO+ultraviolet",
        "http://www.esa.int/esasearch?q=STEREO+visible+light+optical",
        "http://www.esa.int/esasearch?q=THEMIS+magnetic+fields",
        "http://www.esa.int/esasearch?q=TRMM+infrared+spectrum",
        "http://www.esa.int/esasearch?q=TRMM+microwaves",
        "http://www.esa.int/esasearch?q=TRMM+radio+waves",
        "http://www.esa.int/esasearch?q=Van_Allen+RBSP+particles",
        "http://www.esa.int/esasearch?q=Van_Allen+RBSP+plasma",
        "http://www.esa.int/esasearch?q=Venus+Express+magnetic+fields",
        "http://www.esa.int/esasearch?q=Venus+Express+plasma",
        "http://www.esa.int/esasearch?q=Venus+Express+radio+waves",
        "http://www.esa.int/esasearch?q=Venus+Express+ultraviolet",
        "http://www.esa.int/esasearch?q=Venus+Express+visible+light+optical",
        "http://www.esa.int/esasearch?q=Voyager+1+infrared+spectrum",
        "http://www.esa.int/esasearch?q=Voyager+1+magnetic+fields",
        "http://www.esa.int/esasearch?q=Voyager+1+particles",
        "http://www.esa.int/esasearch?q=Voyager+1+plasma",
        "http://www.esa.int/esasearch?q=Voyager+1+ultraviolet",
        "http://www.esa.int/esasearch?q=Voyager+1+visible+light+optical",
        "http://www.esa.int/esasearch?q=Voyager+2+infrared+spectrum",
        "http://www.esa.int/esasearch?q=Voyager+2+magnetic+fields",
        "http://www.esa.int/esasearch?q=Voyager+2+particles",
        "http://www.esa.int/esasearch?q=Voyager+2+plasma",
        "http://www.esa.int/esasearch?q=Voyager+2+radio+waves",
        "http://www.esa.int/esasearch?q=Voyager+2+ultraviolet",
        "http://www.esa.int/esasearch?q=Voyager+2+visible+light+optical",
        "http://www.esa.int/esasearch?q=WISE+%28NEOWISE%29+visible+light+optical",
        "http://www.esa.int/esasearch?q=XMM-Newton+gamma-rays",
        "http://www.esa.int/esasearch?q=XMM-Newton+x-rays"]

for url in urls:

  # Issue queries to your data sources and with your inputs
  # You can modify the inputs and connectorGuids so as to query your own sources
  # Query for tile Esa LD-XML
  client.query({
    "connectorGuids": [
      "814b10a5-1d4f-46dd-b8d7-a15ae0d2a439"
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

  #out_file = open(url[31:] + ".txt","w")
  #out_file.write(json.dumps(dataRows, indent = 4).replace("link/_text", "title"))
  #out_file.close()
  with io.open(url[31:] + ".txt","w", encoding='utf-8') as out_file:
    out_file.write(unicode(json.dumps(dataRows, ensure_ascii=False, indent = 4)).replace("link/_text", "title").replace("detail", "abstract"))
  out_file.close()