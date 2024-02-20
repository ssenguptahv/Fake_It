import random, csv
import pandas as pd
from datetime import timedelta, datetime
from faker import Faker
from faker.providers import person
from faker.providers import date_time

fake = Faker(locale="en_US")
fake.add_provider(person)
fake.add_provider(date_time)

#function to create fake data
def create_data(numRows):
   live_fire= []
   for i in range(1,numRows):
      d={}
      d['Subject ID'] = fake.number.int({ min: 10, max: 200000 })
      #d['first_name'] = fake.first_name()
      d['Last Name'] = fake.last_name()
      d['Date of birth'] = fake.date_between_dates(date_start=datetime(1960, 1, 1),
                                                   date_end=datetime(2000, 1, 1)).strftime("%m/%d/%Y")
      d['Sex'] = random.choice(['F', 'M', 'O'])
      d['Address']= random.choice(['251 Harlan Rd SW, Atlanta, GA, 30311-2001',
                                   '2907 Renfro Dr NW, Atlanta, GA, 30318-7320',
                                   '26W101 Wisconsin Ave, Naperville, IL, 60563-3371',
                                   "3832 Celeste Ln, Naperville, IL, 60564-3105",
                                   "919 Coleman St SW, Atlanta, GA, 30310-2905",
                                   "1857 Dixie Line Rd, Newark, DE, 19702-1037",
                                   "35611 Pine Dr, Millsboro, DE, 19966-5875",
                                   "100 Dickey Ct, Middletown, DE, 19709-8845",
                                   "33177 Cherry Ct, Lewes, DE, 19958-5227",
                                   "19 Melanie Dr, New Castle, DE, 19720-3930",
                                   "29 Silverwood Blvd, Newark, DE, 19711-8303",
                                   "3570 Eagle Ct SW, Atlanta, GA, 30331-3145",
                                   "4421 N 82nd St, Milwaukee, WI, 53218-4515",
                                   "2909 Ridgeview Dr SW, Atlanta, GA, 30331-2935",
                                   "311 Argus Cir NW, Atlanta, GA, 30331-1607",
                                   "1296 Cassia Ave, Idaho Falls, ID, 83402-1938",
                                   "449 Cedarvalley Dr, Nashville, TN, 37211-6620",
                                   "W310 King Rd, Brooklyn, WI, 53521 - 9769",
                                   "W310S478 Maple Ave, Waukesha, WI, 53188 - 9448",
                                   "W310S7586 Arbor Dr, Mukwonago, WI, 53149 - 9214",
                                   "W310S4271 Brookhill Rd, Waukesha, WI, 53189 - 9156",
                                   "514 S Route 59, Naperville, IL, 60540 - 0915",
                                   "24605 W 103rd St Naperville IL 60565",
                                   "900 E Fayette St Rm 118 PO Box, Baltimore, MD, 21273",
                                   "HC 71 Box 8, Taos, NM, 87571-9500",
                                   "RR 3 Box 3, Franklin, AR, 72512 - 9700",
                                   "RR 2 Box A, Daleville, AL, 36322 - 9802",
                                   "RR 1 Box A, Geneva, AL, 36340 - 9801",
                                   "3177 S Vine Ct, Englewood, CO, 80113",
                                   "185 Farm St, Blackstone, MA, 01504",
                                   "185 Franklin Farm Ln, Chambersburg, PA, 17202"

                                   ])

      d["HIPAA"]= fake.date_between_dates(date_start=datetime(2024, 3,3), date_end=datetime(2040, 1, 1)).strftime("%m/%d/%Y")
      d["Primary"]= fake.date_between_dates(date_start=datetime(2024, 3,3), date_end=datetime(2040, 1, 1)).strftime("%m/%d/%Y")
      live_fire.append(d)
   return pd.DataFrame(live_fire)

data=create_data(numRows=50)
#linking first name to gender
def get_random_person():
   data['First Name'] = ""

   for i in range(len(data)):
      if data['Sex'].values[i] == 'M':
         data['First Name'].values[i] = fake.first_name_male()
      if data['Sex'].values[i] == 'F':
         data['First Name'].values[i] = fake.first_name_female()
      else:
         data['First Name'].values[i] = fake.first_name()
   return data

# adding  first name and gender to the dataframe
new_data = get_random_person()
#reordering the dataframe
new_data = new_data[['Subject ID', 'First Name','Last Name','Date of birth','Sex',"Address",'HIPAA','Primary']]
print(new_data)
#converting dataframe to csv
new_data.to_csv('live.csv')
