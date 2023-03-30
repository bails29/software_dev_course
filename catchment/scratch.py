# #anja on object oriented programming, day 3
#
# import pandas as pd
# import numpy as np
# from catchment.models import Site
# import datetime
# data = pd.DataFrame([[1.,2.2,3.],[4.,5.,6.]], index=['fp35','fp56'])
#
# print(data)
#
# location_measurement = [
#     ("FP", "FP35", "Rainfall"),
#     ("FP", "FP56", "River Level"),
#     ("PL", "PL23", "River Level"),
#     ("PL", "PL23", "Water pH")
# ]
# index_names = ["Catchment", "Site", "Measurement"]
# index = pd.MultiIndex.from_tuples(location_measurement, names=index_names)
# data =[
#     [0., 2., 1.],
#     [30., 29., 34.],
#     [34.,32.,33.],
#     [7.8,8.,7.9]
# ]
# data2 = pd.DataFrame(data,index=index)
# print(data2)
#
# measurement_data = [
#     {
#         'site': 'FP35',
#         'measurement': 'Rainfall',
#         'data' : [0., 2., 1.]
#     },
#     {
#         'site': 'FP56',
#         'measurement': 'River level',
#         'data': [30., 29., 34.]
#     },
# ]
#
# print(measurement_data)
#
#
# def attach_sites(data, sites, measurements):
#     initial_list = []
#     for i in range(len(data)):
#         initial_list.append({'site' : sites[i],
#                             'measurements' : measurements[i],
#                              'data' : data[i]})
#     return initial_list
#
#
#

#print(Site.version)
#FP35 = Site('FP35')

#print(FP35.name)

#rainfall_data = pd.Series(
#    [0.0, 2.0, 1.0],
#    index=[
#        datetime.date(2000,1,1),
#        datetime.date(2000, 1, 2),
#        datetime.date(2000, 1, 3)
#    ]
#)

#FP35.add_measurement('Rainfall', rainfall_data)

#print(FP35.measurements.keys())

#from catchment.models import Book
#book = Book('A Book ', ' Me')

#print(book)


###########################################
from catchment.models import Site
from catchment.models import Location
import pandas as pd
import datetime

FP23 = Site('FP23')

print(FP23)

riverlevel_data = pd.Series(
    [34.0,32.0,33.0,31.0],
    index=[
        datetime.date(2000,1,1),
        datetime.date(2000,1,2),
        datetime.date(2000,1,3),
        datetime.date(2000,1,4),
        ]
    )

FP23.add_measurement('River Level',riverlevel_data,'mm')

print(FP23.measurements['River Level'].series)

PL12 = Location('PL12')
print(PL12)

PL12.add_measurement('River Level',riverlevel_data,'mm')


