### post code matching - does the post code match a list of post codes
## TODO think about heirarchical postcode_parse
import address_cleaner
import json
import requests
import pprint as pp

####pc_in = postcode in, pc_list = list of postcodes you want to match against
def postcode_matcher(pc_in, pc_list):

    ### look at end of string


    ### look for any
    pass

### if can't find postcode, go get a GPS or reverse lookup postcode
def address_matcher():

    ### success

    ### fail

    pass

### matches location of an
def location_matcher(address_in):
    ### if there's a postcode at end of string, or somewhere in there
    pass

def geocode_postcode(postcodes=["l120jq","DE39DY"]):
    #Accepts up to 100 postcodes!!!!

    responses = list()
#    #if len(postcodes) > 100:
#       #print(1)
    LOG_EVERY_N = 100

    for i in range(len(postcodes)):
        if (i % LOG_EVERY_N) == 0:

            end = i + 100
            if i + 100 > len(postcodes):
                end = len(postcodes)
            data = {
                "postcodes": postcodes[i:end]
            }

            r = requests.post('http://api.postcodes.io/postcodes', data)

            responses.extend(json.loads(r.text)['result'])


    return responses
