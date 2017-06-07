import re

def clean_address(addr):
    ## remove multiple spaces
    addr = " ".join(addr.split())

    addr = addr.upper()

    ##TODO check end of address field for periods/fullstop
    return addr

def while_replace(string):
    while '  ' in string:
        string = string.replace('  ', ' ')

    return string


### returns original string on fail
def postcode_extract(addr):
    p=re.compile('\\s*(.*\\S)?\\s*')
    addr = addr.replace("'", "")
    addr = addr.replace("_", "")
    addr = while_replace(addr)
    split_addr = addr.split(',')
    split_addr = p.match(split_addr[-1]).group(1)
    if split_addr is not None:
        split_addr = split_addr.replace("LONDON ","")
        split_addr = split_addr.replace("HOWDEN ","")


    custom, uk_f = validate_postcode(split_addr)


    if custom is False or uk_f is False:
        #if false, check in the middle of the string
        split_addr = postcode_clean(split_addr)



    return split_addr

### flatten the postcode to allow for more simplistic checking
def postcode_clean(split_addr):
    ### do some checking here of length - max should be 9 with a space
    ## could just be the first half - could betechnically valid, postcodes are hierarchical but won't resolve with any precision
    ###check that there are numbers in string
    if split_addr is None:
        return split_addr

    len_sa = len(split_addr)
    if hasNumbers(split_addr):
        if len_sa <= 4 and len_sa >= 2:
            ###does it contain a number? if not probably invalid
            pass
        elif len_sa > 4 and len_sa < 9 and ' ' not in split_addr:

            split_addr = split_addr[:(len_sa-3)] + ' ' + split_addr[(len_sa-3):]

        elif len_sa > 9:
            pass
        split_addr = split_addr.replace(" O"," 0")


    return split_addr

##used for when we have failed to find a valid postcode at end of address - might deprecate postcode_extract()
def postcode_extract_mid_sentence(addr):


    pass

###does the postcode match the regex - is it a valid postcode? Returns a generic/custom postcode match and the regexspecifid on the UK postcode wiki
def validate_postcode(arg):
    ###TODO deal with uppercase
    custom_r = re.compile(r'\b[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}\b')
    ##regex from #http://en.wikipedia.orgwikiUK_postcodes#Validation
    uk_r = re.compile(r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}')
    custom = False
    valid_uk = False
    if arg is not None:
        matchedobj = custom_r.search(arg)
        if matchedobj:
            custom = True
        #
        matchedobj = uk_r.search(arg)
        if matchedobj:
            valid_uk = True
    return custom, valid_uk

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
