import urllib.request, urllib.parse, urllib.error
import json
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ISSN = input("Enter a journal ISSN. Make sure to include the dash:")

serviceurl = 'https://api.crossref.org/journals/'

try:
    url = serviceurl + urllib.parse.quote(ISSN) + "&mailto=ryregier@gmail.com" #Getting Crossref API for ISSN
    #print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    info = json.loads(data)

    print("Retrieving", url)
    print("\n")

    if info['status'] == 'ok': #Making sure journal is in Crossref
        #print ('Found this journal')
        journal_title = info['message']['title'] #Navigating to Journals title
        print("This Journal's title is:", journal_title)

        print ("\n")

        year = input("Enter a year to get the DOI count from that year:")
        year = int(year) #Converting year to integer to check in list
        #year = 2017
        years = info['message']["breakdowns"]['dois-by-issued-year'] #Grabbing the DOI per year list
        #print (year)

        DOIs_year = False #Making variable false in case no DOIs for that year
        for x in years:
            if x[0] != year:
                continue
            else:
                DOIs_year = x[1]

        print("\n")

        if DOIs_year != False: #To find if no DOIs were registered with Crossref that year
            print (journal_title,"had",DOIs_year,"DOIs registered with Crossref in",year)
        else:
            print (journal_title,"has no DOIs registered with Crossref in",year)

    else:
        print ('Could not find this journal in Crossref')


except:
    print ('ERROR. This is not a journal ISSN or it is not in Crossref')

print ("\n")
print("+++++++++++++++++++++++++++++++++++++++++")

if DOIs_year > 1000:
    print ("Sorry",DOIs_year,"is too many DOIs. My limit is 1000 DOIs at once.")
    quit()

if DOIs_year == 0:
    print ("Sorry I can't find any DOIs registered with Crossref I can work with.")
    quit()

print ("Ok! I can work with this many DOIs! Let me see how many are open access...")

year = str(year) #Converting the year back to a string so it can go in the API

serviceurl = 'https://api.crossref.org/journals/'

#https://api.crossref.org/journals/1935-990X
#print ("/works?filter=from-pub-date:2014,until-pub-date:2014&rows=1000&select=DOI")
#&mailto=ryregier@gmail.com

try: #Acquiring DOIs for that year and adding them to a list
    date_search= "/works?filter=from-pub-date:"+urllib.parse.quote(year)+",until-pub-date:"+urllib.parse.quote(year)+"&rows=1000&select=DOI" #Searching date
    #print (date_search)
    url = serviceurl + urllib.parse.quote(ISSN) + date_search + "&mailto=ryregier@gmail.com"
    #print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    info = json.loads(data)

    DOI_year_list = list() #predefining the lsit where DOIs will go

    if info['status'] == 'ok': #Making sure journal is in Crossref
        DOI_dict = info['message']['items'] #Pulling list of DOIs for that year
        #print (DOI_list)
        for q in DOI_dict: #Pulling DOIs from dictionary and organizing them into a list
            for key in q:
                DOI_year_list.append(q[key])
    else:
        print ("Error. Journal's DOIs not listed'.")

except:
    print ("ERROR with pulling DOIs")

print ("\nDetermining OA status. Please wait. Depending on the Number of DOIs, this may take awhile.")

#print (DOI_year_list[1])

oadoi_serviceurl = 'https://api.oadoi.org/v2/'
oa_count = 0
process_count = 1

for doi in DOI_year_list: #Finding OA count of DOIs
    if process_count == int(len(DOI_year_list)*0.25):
        print ("25% processed....")
    if process_count == int(len(DOI_year_list)*0.50):
        print ("50% processed...")
    if process_count == int(len(DOI_year_list)*0.75):
        print ("75% processed...")
    process_count = process_count +1
    try:
        url = oadoi_serviceurl + urllib.parse.quote(doi) + "?email=ryregier@gmail.com"
        #print('Retrieving', url)
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        info = json.loads(data)

        if info['is_oa'] is True:
            oa_count = oa_count + 1
        elif info["is_oa"] is False:
            continue
        else:
            print ("error with DOI")
    except:
        print ("Error parsing OAdoi")
        print (doi)
        break

print ("\nI found",oa_count,"open access of",len(DOI_year_list),"DOIs.")
