import csv
import operator
from operator import itemgetter
data_dict={}
data_is_loaded = False

def load_data():

    with open('US_County_Level_Presidential_Results_12-16.csv', 'r') as csvfile:
        reader = [tuple(row) for row in csv.reader(csvfile)]
        for row in reader:
            if row[9]=="AK":
                pass
            elif row[0]=="":
                pass
            else:
                if row[9] not in data_dict:
                    data_dict[row[9]]=[float(row[2]),float(row[3]),float(row[4])]
                elif row[9] in data_dict:
                    abbre=row[9]
                    dem_info=data_dict[abbre][0]
                    gop_info=data_dict[abbre][1]
                    info_total=data_dict[abbre][2]
                    cal_dem=float(dem_info)+float(row[2])
                    cal_gop=float(gop_info)+float(row[3])
                    cal_total=float(info_total)+float(row[4])
                    data_dict[abbre][0]=cal_dem
                    data_dict[abbre][1]=cal_gop
                    data_dict[abbre][2]=cal_total
    global data_is_loaded
    data_is_loaded = True

def get_data(party="dem", raw=True, sort_ascending=True, year=2016):
    global data_is_loaded
    default_info=[]
    if not data_is_loaded:
            load_data()
    for i in data_dict:

        total_votes=data_dict[i][2]
        if party=="dem":
            votes=data_dict[i][0]
        if party=="gop":
            votes=data_dict[i][1]
        if raw==True:
            default_info.append((i,votes))
        if raw==False:
            percent=((float(votes)/float(total_votes)))*100
            default_info.append((i,percent))

    if sort_ascending==True:
        sorted_list=sorted(default_info,key=itemgetter(1))
    else:
        sorted_list=sorted(default_info,key=itemgetter(1),reverse=True)
    return(sorted_list)


# if __name__ == "__main__":
#
#     points = 0
# # #
#     data = get_data()
#     if data[0] == ('WY', 55949.0) and data[-1] == ('CA', 7362490.0):
#         points += 3.33
#         print("1,ok")
# #
#     data = get_data(party='gop', raw=False)
#     if data[0][0] == 'DC' and int(data[0][1]) == 4 and \
#                     data[-1][0] == 'WY' and int(data[-1][1]) == 70:
#         points += 3.33
#         print("2,ok")
# # # #
#     data = get_data(party='dem', raw=True, sort_ascending=False)
#     if data[0] == ('CA', 7362490.0) and data[-1] == ('WY', 55949.0):
#         points += 3.34
#         print("3,ok")
# # #
#     print("points :", points)
