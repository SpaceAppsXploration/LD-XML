from subprocess import call
from urllib import quote_plus, urlencode
# load dict from "scidata_only_payloads.json"

from PL_fields import FIELDS

# cross mission+payload

parameters = []

for f in FIELDS.keys():
    #print f
    for m in FIELDS[f]['missions']:
        parameters.append(quote_plus(m+' '+FIELDS[f]['kw']))        

#print parameters

# run quickscrape on websites

options = {'NASA':
           {
              'url': 'http://nasasearch.nasa.gov/search?',
              'parameters': 'affiliate=nasa&query=%s&commit=Search',
              'scraper': 'scrapers/nasasearch.json',
              'output': 'outputs'
            },
           'ESA':
           {
              'url': 'http://www.esa.int/esasearch?',
              'parameters': 'q=%s',
              'scraper': 'scrapers/esasearch.json',
              'output': 'outputs'
            },
           'JAXA':
           {
              'url': 'http://global.jaxa.jp/search.html?',
              'parameters': '&q=%s&sa=Search&siteurl=global.jaxa.jp',
              'scraper': 'scrapers/jaxasearch.json',
              'output': 'outputs'
            },
           }

for p in parameters:
    for o in options.keys():
        params = options[o]['parameters'] % p

        '''with open("scrapers/urls", 'a') as f:
             f.write(qs_url+'\n')
        '''         
        params = quote_plus(params)
        qs_url = options[o]['url'] + params

        print qs_url

        scraper = options['NASA']['scraper']
        output = options['NASA']['output']
        bash = 'quickscrape --url "%s" --scraper %s -output %s --loglevel debug' % (qs_url, scraper, output)
        print bash

        #subprocess.Popen(bash)

        #call(bash)

#
#print FIELDS

