
# Find the total of leads generated in each category in the combination of Source
# Medium and Keyword Columns
# Add total for rows and columns

import pandas
from numpy import nan

data = pandas.read_csv("CRM-Data 15-21 June 2022.csv")
print(data)

#print(data)
#print(data.iloc[:,0:3]) #all rows and columns 0 to 3
#print(data.loc[0:1,"Medium":"Keywords"]) # row 0 and 1 for columns Medium and Keywords
print(data.loc[1,"Medium"])

data_source_unique = data.Source.unique()
print(data_source_unique)
# print(type(data_source_unique)) #<class 'numpy.ndarray'>
#
data_source_valuecounts = data["Source"].value_counts()
print(data_source_valuecounts)
# print(print(data_source_valuecounts)) #Name: Source, dtype: int64
#
data_source_valuecountssum = data["Source"].value_counts().sum()
print(data_source_valuecountssum)
# print(type(data_source_valuecountssum)) #<class 'numpy.int64'>
#
# # print(data.Medium.unique())
# print(data["Medium"].value_counts())
# print(data["Medium"].value_counts().sum())
#
# # print(data.Keywords.unique())
# print(data["Keywords"].value_counts())
# print(data["Keywords"].value_counts().sum())

report ={}
count_adwords = 0
count_direct = 0
count_referral = 0
count_krishna = 0
count_displayplacements = 0
count_displayplsearch = 0
count_displayJune2022 = 0
count_emailnetcoremcaclr = 0
count_emailnetcoremdceo = 0
count_emailmailjetwebinar = 0
count_emailmailjetkrishna = 0
count_emailmailjetcrm = 0
count_emailother = 0
count_referral = 0
count_krishna = 0
total_leads = 0



for i, row in data.iterrows():
	if row["Source"] == "Adwords":
		count_adwords += 1
	elif row["Source"] == "Google Ads" and row["Medium"] == 'Display Placements':
		count_displayplacements += 1
	elif row["Source"] == "Google Ads" and row["Medium"] == 'Search':
		count_displayplsearch += 1
	elif row["Source"] == "Google Ads" and row["Medium"] == 'Display-June22':
		count_displayJune2022 += 1
	elif row["Source"] == "Email" and row["Medium"] == "Netcore" and row["Keywords"] == "MCA CLR":
		count_emailnetcoremcaclr += 1
	elif row["Source"] == "Email" and row["Medium"] == "Netcore" and row["Keywords"] == "MD CEO":
		count_emailnetcoremdceo += 1
	elif row["Source"] == "Email" and row["Medium"] == "Mailjet" and row["Keywords"] == "Webinar":
		count_emailmailjetwebinar += 1
	elif row["Source"] == "Email" and row["Medium"] == "Mailjet" and row["Keywords"] == "Krishna":
		count_emailmailjetkrishna += 1
	elif row["Source"] == "Email" and row["Medium"] == "Mailjet" and row["Keywords"] == "CRM":
		count_emailmailjetcrm += 1
	elif row["Source"] == "Email": #and row["Medium"] == nan and row["Keywords"] == nan: #oesnot work why?
		count_emailother += 1
	elif row["Source"] == "Direct":
		count_direct += 1
	elif row["Source"] == "Referral":
		count_referral += 1
	elif row["Source"] == "Krishna":
		count_krishna += 1


print(f"Adwords = {count_adwords}")
print(f"Google Ads- Display Placements = {count_displayplacements}")
print(f"Google Ads- Display Search = {count_displayplsearch}")
print(f"Google Ads- Display Display June 2022 = {count_displayJune2022}")
print(f"Email Netcore MCA CLR = {count_emailnetcoremcaclr}")
print(f"Email Netcore MD CEO = {count_emailnetcoremdceo}")
print(f"Email Mailjet Webinar = {count_emailmailjetwebinar}")
print(f"Email Mailjet Krishna = {count_emailmailjetkrishna}")
print(f"Email Mailjet CRM = {count_emailmailjetcrm}")
print(f"Email Others = {count_emailother}")
print(f"Direct = {count_direct}")
print(f"Referral = {count_referral}")
print(f"Krishna = {count_krishna}")


# data_dict = data.to_dict()
#
# #print(source_list)
# source_list = data.Source.to_list()
# source_count = Counter(source_list) # Counts number of instances for each unique value in list, returns dictionary
# print(sum(source_count.values()))
# print(source_count)
#
#
# #print(medium_list)
# medium_list = data.Medium.to_list()
# medium_count = Counter(medium_list) # Counts number of instances for each unique value in list, returns dictionary
# print(sum(medium_count.values()))
# print(medium_count)
#
# #print(keyword_list)
#
# keyword_list = data.Keywords.to_list()
# keyword_count = Counter(keyword_list)
# print(sum(keyword_count.values()))
# print(keyword_count)
#
# #leadtype_list = data["Lead Type"].to_list()
#
# report = {}
# for item_source in source_count:
#         if item_source != "Google Ads": # instead of and sequential if loop
#             if item_source != "Email":
#                 report[item_source] = source_count[item_source]
#
# for item_medium in medium_count:
#        if item_medium == "Display Placements" or item_medium == "Search" or item_medium == "Display-June22":
#            report["Google Ads- " + item_medium] = medium_count[item_medium]
#
# for item_keyword in keyword_count:
#        if item_keyword == "MD CEO":
#            report["Email- Netcore- " + item_keyword] = keyword_count[item_keyword]
#        elif item_keyword == "MCA CLR":
#            report["Email- Netcore- " + item_keyword] = keyword_count[item_keyword]
#        elif item_keyword == "CRM":
#            report["Email- Mailjet- " + item_keyword] = keyword_count[item_keyword]
#        elif item_keyword == "Webinar":
#            report["Email- Mailjet- " + item_keyword] = keyword_count[item_keyword]
#        elif item_keyword == "Krishna":
#            report["Email- Mailjet- " + item_keyword] = keyword_count[item_keyword]
#
#
# for item_source in source_count: #not able to find Emails with no Medium and Keywords
#     if item_source == "Email":
#         report["Email- Others-"] = keyword_count[item_source]
#
# print(report)
# print(sum(report.values())) #add sum of integer value in dictionary






# Note that in this particular case there is no need to create lists of individual dataframe columns
# It is better to user dictionary

#print(data.Source.value_counts()) # calculates the unique value instances in a column
# print(data.Medium.value_counts())
#print(type(data.Medium.value_counts()))  #method 2 count unique values in a list ie. column in this case

#medium_count = data.Medium.value_counts()
#print(*medium_count) # prints all values in a list w/o for loop

