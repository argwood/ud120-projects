#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

for key in (enron_data['SKILLING JEFFREY K'].keys()):
    print(key)
pois = 0
salary_c = 0
email_c = 0
no_total_pay = 0
poi_no_pay = 0
for name in enron_data.keys():
#    print(name)
    if enron_data[name]["poi"]==1:
        pois+=1
    if not enron_data[name]['salary']=='NaN':
        salary_c+=1
    if not enron_data[name]['email_address']=='NaN':
        email_c+=1
    if enron_data[name]['total_payments']=='NaN':
        no_total_pay+=1
        if enron_data[name]["poi"]==1:
            poi_no_pay+=1




print(' ')
print('There are {} POIs in the dataset'.format(pois))

print('Total stock value for J. Prentice is {}'.format(enron_data['PRENTICE JAMES']['total_stock_value']))
print('There are {} email messages from W. Colwell to a POI'.format(enron_data['COLWELL WESLEY']['from_this_person_to_poi']))
print('Value of stock options exercised for J. K. Skilling is {}'.format(enron_data['SKILLING JEFFREY K']['exercised_stock_options']))



print('Total payments for J. K. Skilling is {}'.format(enron_data['SKILLING JEFFREY K']['total_payments']))
print('Total payments for A. Fastow is {}'.format(enron_data['FASTOW ANDREW S']['total_payments']))
print('Total payments for K. Lay is {}'.format(enron_data['LAY KENNETH L']['total_payments']))

print('There are {} valid emails'.format(email_c))
print('There are {} valid salaries'.format(salary_c))
print('There are {} missing total payments, which is {}% of the dataset'.format(no_total_pay, 100*no_total_pay/len(enron_data.keys())))
print('There are {} missing total payments from POIs, which is {}% of the POIs'.format(poi_no_pay, 100*poi_no_pay/pois))
print(len(enron_data.keys()))
