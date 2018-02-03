email = "" #Please enter your email here in between the quotes. This is so the Crossref and OADOI know who is making use of their APIs.

import urllib.request, urllib.parse, urllib.error
import json
import ssl
import re
from datetime import datetime

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

if email == "":
    print ("You need to enter your email in the first line of code.")
    print ("When you using Public APIs like this python code does, entering an email is standard practice.")
    quit()

while True:

    ISSN = input("Enter a journal ISSN. Make sure to include the dash:")
    if len(ISSN) ==0:
        quit()

    serviceurl = 'https://api.crossref.org/journals/'

    try:
        url = serviceurl + urllib.parse.quote(ISSN) + "&mailto=" + email #Getting Crossref API for ISSN
        #print('Retrieving Crossref API at', url)
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        info = json.loads(data)

    except:
        print ('ERROR. Some data entered was incorrect or Crossref may be updating')
        continue

    if info['status'] == 'ok': #Making sure journal is in Crossref
        #print ('Found this journal')
        journal_title = info['message']['title'] #Navigating to Journals title
        #print("This Journal's title is:", journal_title)

    else:
        print ('Sorry! Could not find this journal in Crossref.')
        continue

    #year = 2017

    #e.g. https://api.crossref.org/journals/1476-4687&mailto=ryregier@gmail.com/works?filter=from-pub-date:2014,until-pub-date:2014&rows=1000&select=DOI

    while True: #OA may take awhile. Double checking users wants to do it
        year = input("Enter a year to get the DOI count from that year:")
        if len(year)==0:
            quit()
        #year = int(year) #Converting year to integer to check in list
        print ("Please wait...")
        try: #Finding how many DOIs can be analyzed in that year
            d = "/works?filter=from-pub-date:"+ urllib.parse.quote(year) +",until-pub-date:" + urllib.parse.quote(year) +"&rows=1000&select=DOI"
            count_link = serviceurl + urllib.parse.quote(ISSN) + d + "&mailto=" + email
            #print (count_link)
            uh = urllib.request.urlopen(count_link)
            data = uh.read().decode()
            info = json.loads(data)

            if info['status'] == 'ok' and info['message']['total-results'] != 0: #Making sure status of results show up
                DOIs_year = info['message']['total-results'] #Finding total results
                #print (DOIs_in_year)
                break

            else:
                print ("I can't seem to find any info for that year. Please try again")
                continue

        except:
            print ("Error. I'm not getting anything for that year. Please try again")
            continue

    #year = str(year)
    print("---")
    print (journal_title,"had",DOIs_year,"analyzable DOIs registered with Crossref in",year)

 #Converting the year back to a string so it can go in the API

    if DOIs_year < 1000:
        d1= "/works?filter=from-pub-date:"+urllib.parse.quote(year)+",until-pub-date:"+urllib.parse.quote(year)+"&rows=1000&select=DOI"
        crossref_date_list = [d1]
    if 1000 < DOIs_year and DOIs_year < 4000:
        d1="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-01,until-pub-date:" + urllib.parse.quote(year) + "-03&rows=1000&select=DOI"
        d2="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-04,until-pub-date:" + urllib.parse.quote(year) + "-06&rows=1000&select=DOI"
        d3="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-07,until-pub-date:" + urllib.parse.quote(year) + "-09&rows=1000&select=DOI"
        d4="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-10,until-pub-date:" + urllib.parse.quote(year) + "-12&rows=1000&select=DOI"
        crossref_date_list = [d1,d2,d3,d4]
    if DOIs_year > 4000 and DOIs_year < 12000:
        d1="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-01,until-pub-date:" + urllib.parse.quote(year) + "-01&rows=1000&select=DOI"
        d2="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-02,until-pub-date:" + urllib.parse.quote(year) + "-02&rows=1000&select=DOI"
        d3="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-03,until-pub-date:" + urllib.parse.quote(year) + "-03&rows=1000&select=DOI"
        d4="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-04,until-pub-date:" + urllib.parse.quote(year) + "-04&rows=1000&select=DOI"
        d5="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-05,until-pub-date:" + urllib.parse.quote(year) + "-05&rows=1000&select=DOI"
        d6="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-06,until-pub-date:" + urllib.parse.quote(year) + "-06&rows=1000&select=DOI"
        d7="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-07,until-pub-date:" + urllib.parse.quote(year) + "-07&rows=1000&select=DOI"
        d8="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-08,until-pub-date:" + urllib.parse.quote(year) + "-08&rows=1000&select=DOI"
        d9="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-09,until-pub-date:" + urllib.parse.quote(year) + "-09&rows=1000&select=DOI"
        d10="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-10,until-pub-date:" + urllib.parse.quote(year) + "-10&rows=1000&select=DOI"
        d11="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-11,until-pub-date:" + urllib.parse.quote(year) + "-11&rows=1000&select=DOI"
        d12="/works?filter=from-pub-date:"+urllib.parse.quote(year)+"-12,until-pub-date:" + urllib.parse.quote(year) + "-12&rows=1000&select=DOI"
        crossref_date_list = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12]
    if DOIs_year > 12000:
        print ('Sorry my limit is 12000 DOIs at the moment.')
        continue

    print ("With",DOIs_year,"DOIs the open access analysis could take approximately", int(DOIs_year/100)+1,"minutes")

    if DOIs_year > 1000:
        while True: #OA may take awhile. Double checking users wants to do it
            OA_analysis = input("Do you want to go ahead with the open access analysis? (y/n):")
            if OA_analysis == "y" or OA_analysis == "n":
                break
        if OA_analysis == "n":
            continue
    print("---")
    print ("You can choose to export info for the best OA link for each DOI to an csv file.")
    while True: #exporting data takes longer. Checking with users
        OA_export = input("Would you like to do this? It's possible it could increase the estimated time above by 25%. (y/n):")
        if OA_export == "y" or OA_export == "n":
            break

    if OA_export == "y":
        file_title = journal_title+str(year)+".csv"
        f = open(file_title,'w')
        f.write("DOI Link"+","+"OA?"+","+"Genre"+","+"Version"+","+"Host Type"+","+"OA Link")
        f.write("\n")

    print ("Analyzing...")
    #print(datetime.now())

    serviceurl = 'https://api.crossref.org/journals/'

    #https://api.crossref.org/journals/1935-990X&mailto=ryregier@gmail.com/works?filter=from-pub-date:2014,until-pub-date:2014&rows=1000&select=DOI

    #https://api.crossref.org/journals/1935-990X
    #print ("/works?filter=from-pub-date:2014,until-pub-date:2014&rows=1000&select=DOI")
    #&mailto=ryregier@gmail.com

    DOI_year_list = list() #predefining the list where DOIs will go

    for d in crossref_date_list:
        try: #Acquiring DOIs for that year and adding them to a list
            url = serviceurl + urllib.parse.quote(ISSN) + d + "&mailto=" + email
            #print("Retrieving", url)
            uh = urllib.request.urlopen(url)
            data = uh.read().decode()
            info = json.loads(data)

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

    #print (DOI_year_list)
    #break

    oadoi_serviceurl = 'https://api.unpaywall.org/v2/'
    oa_count = 0
    doi_error_count = 0
    doi_info = dict()
    process_count = 1
    journal = "closed"

    for doi in DOI_year_list: #Finding OA count of DOIs
        if process_count == int(len(DOI_year_list)*0.25):
            print ("25% processed....")
        if process_count == int(len(DOI_year_list)*0.50):
            print ("50% processed...")
        if process_count == int(len(DOI_year_list)*0.75):
            print ("75% processed...")
        process_count = process_count +1
        try:
            url = oadoi_serviceurl + urllib.parse.quote(doi) + "?email="+ email
            #print('Retrieving', url)
            uh = urllib.request.urlopen(url)
            data = uh.read().decode()
            info = json.loads(data)

            if info["journal_is_oa"] is True:
                print(journal_title,"is an Gold Open Access Journal! All DOIs are open!")
                journal = "open"
                break

            if info['is_oa'] is True:
                oa_count = oa_count + 1
                if OA_export == "y":
                    doi_info[doi]={"OA" : "Y",
                                    "Genre":info["genre"],
                                    "Version":info["best_oa_location"]["version"],
                                    "Host Type":info["best_oa_location"]["host_type"],
                                    "Link":info["best_oa_location"]["url"]}
                continue

            if info['is_oa'] is False:
                if OA_export == "y":
                    doi_info[doi]={"OA": " ",
                                    "Genre":info["genre"],
                                    "Version":" ",
                                    "Host Type":" ",
                                    "Link":" "}
                continue
            else:
                doi_error_count = doi_error_count + 1
                if OA_export == "y":
                    doi_info[doi]={"OA" : "DOI Error",
                                    "Genre":" ",
                                    "Version":" ",
                                    "Host Type":" ",
                                    "Link":" "}
                continue
        except:
            #print ("Error parsing OAdoi")
            #print ('DOI causing the error is:', uh)
            doi_error_count = doi_error_count + 1
            if OA_export == "y":
                doi_info[doi]={"OA" : "DOI Error. Unpaywall can not regonize this DOI",
                                "Genre":" ",
                                "Version":" ",
                                "Host Type":" ",
                                "Link":" "}
            continue
    if journal is "open":
        continue

    print ("++++++")
    #print("The process count is",process_count)
    print ("I found",oa_count,"open access of",len(DOI_year_list),"DOIs.")
    print ("There were", doi_error_count,"DOI errors.")
    if OA_export == "y":
        #print("Exporting csv file. Please wait...")
        for a, b in doi_info.items():
            export = "https://doi.org/"+str(a)+","+str(b["OA"])+","+str(b["Genre"])+","+str(b["Version"])+","+str(b["Host Type"])+","+str(b["Link"])
            f.write(export)
            f.write("\n")
        f.close()
        print (file_title,"exported")
    #print(datetime.now())
    print ("++++++")
    print ("\n")
