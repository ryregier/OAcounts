# OAcounts

This python code makes use of the free [Crossref Rest API](https://www.crossref.org/services/metadata-delivery/rest-api/) and the free [Unpaywall Rest API](http://unpaywall.org/api/v2) to analyze how open access DOIs a journal has. It also has an option to export the results and see the information for the Unpaywall recommended best Open Access link for each DOI.

## OAISSN.py for those without programming experience

The OAISSN program can be used by those unfamilar with python or programing. Four key steps need to be followed:
  1. [Download Python 3](https://www.python.org/downloads/)
  2. Copy and paste the program code to a [text editor](https://en.wikipedia.org/wiki/Text_editor) (e.g. Notepad) and make sure it is saved as a ".py" program (e.g. OAISSN5.py)
  3. Open and edit (e.g. Right click and select "Open with") the firstline of the code in the text editor to add your email. (e.g. email = "ryan@email.com")
  4. Open and run the code with the Python intrepreter (i.e. IDLE) 
  
Your email is required so that Crossref and Unpaywall can keep an idea how their API is being used and can contact you if any overuse or problems. This is a standard practice with most free and public APIs these days. Crossref gives a [good explaination](https://github.com/CrossRef/rest-api-doc) why they require an email.

## Using OAISSN.py

If don't add you email to the first line, the program will not run, so be sure to do this.

The first prompt when your run the program will be to enter a journal ISSN:
  >Enter a journal ISSN. Make sure to include the dash:

Any ISSN attached to the journal should work. It does not matter if it is a online or print ISSN. OAISSN.py will quickly check to see if this journal is registered in Crossref via the Crossref API. If it can not find the journal, it will prompt you to re-enter. Crossref indexes most journals, but not all of them. It's possible the journal you search for is not indexed in Crossref.

The second prompt will prompt you to enter the year you wish to anaylze for that journal:
  >Enter a year to get the DOI count from that year:
 
This will again check the Crossref API to see if their are any DOIs registered for that year. Please note, a journal may be registered with Crossref and not have any DOIs registered. If you keep getting errors for these two prompts, it's worth checking the [Crossref Metadata](https://search.crossref.org/) search to see if your Journal or Journal years are in there. If they are, please contact me! There could be issue with my code. 

If OAISSN.py can find this journal and DOIs for that year registered with Crossref, it will show this information and an approximate estimate of how long the open access analysis will take. e.g:
  >Journal of Clinical Microbiology had 454 analyzable DOIs registered with Crossref in 2017
  >With 454 DOIs the open access analysis could take approximately 5 minutes

It seems to take about 1 minute per every 100 DOIs registered. Some large journals (e.g Nature) that publish around 4000 DOIs a year can take 40 - 50 minutes. The limit that this program can handle is 12,000 DOIs. The only large journals could publish this many DOIs are Open Access MegaJournals and since all their DOIs are open, they do not need to be run through this program.

If the Open Access analysis will take longer than 10 minutes, OAISSN.py will ask you if you want to continue:
  >Do you want to go ahead with the open access analysis? (y/n):

This is just so you don't run a fifty minute program unawares. You can let these longer ones run in the background while you do other stuff on your computer.

The next prompt will be for the option to export the Best Open Access DOI link from Unpaywall:
  >You can choose to export info for the best OA link for each DOI to an csv file.
  >Would you like to do this? It's possible it could increase the estimated time above by 25%. (y/n):

This csv file (which can be opened in Excel or another spreedsheet software) will be saved to the same folder the OAISSN.py program is. It will be named with the Journal title and year (e.g. Nature2015.csv). The exported file will look like so when opened in Excel:

DOI Link | OA? | Genre | Version | Host Type | OA Link
------------ | ------------- | ------------- | ------------- | ------------- | -------------
https://doi.org/10.11... | Y | journal-article | publishedVersion | repository | http://europepmc.org/articles...
https://doi.org/10.12... |  | journal-article |  |  | 
https://doi.org/10.12... | DOI Error... | journal-article |  |  |

If the article is not OA then the OA? value will remain blank. Sometimes the Unpaywall DOI can not regonize Crossref DOIs. This can be an error with the DOI or with Unpaywall. If this happens a "DOI Error. Unpaywall can not regonize this DOI" will appear as the OA? value.

The open access version returned is the Unpaywall's "best OA location". How this is determined can be found on [their website](http://unpaywall.org/api/v2):
>The "best" location is determined using an algorithm that prioritizes publisher-hosted content first (eg Hybrid or Gold), then prioritizes versions closer to the version of record (PublishedVersion over AcceptedVersion), then more authoritative repositories (PubMed Central over CiteSeerX).

This csv file will fully export when the program is done running. You will see it has been created once the program begins though. Do not open it till the program is done.

The open access analysis begins after you select y/n for the csv export prompt. Each DOI will be run through the Unpaywall API.

As the program runs, it will show when it is 25%, 50%, and 75% done so you can get an idea how much longer it needs to go for. 

When finished, it will show you the total count of open access DOIs and how many DOI errors there were:
  >I found 238 open access of 454 DOIs.
  >There were 2 DOI errors.

If you enter y to export the csv file it will tell you the csv file has been exported, along with the file name.
  >Journal of Clinical Microbiology2017.csv exported

## Potential Errors and Concerns

If you do enter the ISSN for an open access journal, OAISSN.py will run you through the first couple steps, till it begins to check the DOIs in Unpaywall. It will then exit the analysis and let you know the journal is an open acces journal:
   >College and Research Libraries is an Gold Open Access Journal! All DOIs are open!
   
Crossref and Unpaywall can time out on occasion. If you keep getting errors and it seems like it should be working, please wait an hour or so before trying again. If it's still not working, please let me know! It may be bad code. 

I have noticed that just because a DOI is registered with Crossref, it does not mean that OADOI can find it. You may see quite a few DOI errors for some journals because of this.

## What is OAISSN for?

I'm hoping it can be a tool for librarians evaluating their journal subscriptions and can help them create a open access adjusted cost per use. It could also be used by journal editors who want to see where researchers are depositing green OA copies of their articles.



