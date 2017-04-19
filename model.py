import csv
import operator
from operator import itemgetter

data_is_loaded = False
def load_data():
    model_list=[]
    with open('US_County_Level_Presidential_Results_12-16.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[9]=="AK":
                pass
            elif row[0]=="":
                pass
            else:
                model_list.append(row)
        data_is_loaded = True
    return model_list  # process the data

def get_data(party="dem", raw=True, sort_ascending=True, year=2016):
    if not data_is_loaded:
            load_data()
            #default=data1
            if party=="dem" and raw==True and sort_ascending==True:
                dem_cdict={}
                for i in load_data():
                    dem_votes=i[2]
                    dem_abbre=i[9]
                    if dem_abbre in dem_cdict:
                        dem_cdict[dem_abbre]+= float(dem_votes)
                    else:
                        dem_cdict[dem_abbre] = float(dem_votes)

                dem_default=sorted(dem_cdict.items(), key=operator.itemgetter(1))
                return dem_default
            #data2
            if party=="gop" and raw==True and sort_ascending==True:
                gop_cdict = {}
                for i in load_data():
                    gop_abbre = i[9]
                    gop_votes=i[3]

                    if gop_abbre in gop_cdict:
                        gop_cdict[gop_abbre] += float(gop_votes)
                    else:
                        gop_cdict[gop_abbre] = float(gop_votes)
                gop_default = sorted(gop_cdict.items(), key=operator.itemgetter(1))
                return gop_default
            #data3
            if party=="dem" and raw==False and sort_ascending==True:
                dem_cdict_indi = {}
                dem_cdict_total={}
                for i in load_data():
                    dem_abbre = i[9]
                    dem_indi=float(i[2])
                    dem_total = float(i[4])
                    if dem_abbre in dem_cdict_indi:
                        dem_cdict_indi[dem_abbre] += dem_indi
                        dem_cdict_total[dem_abbre] += dem_total

                    else:
                        dem_cdict_indi[dem_abbre] = dem_indi
                        dem_cdict_total[dem_abbre] = dem_total
                dem = {dem: dem_cdict_indi[dem] / dem_cdict_total[dem] * 100 for dem in dem_cdict_indi}
                demraw = sorted(dem.items(), key=operator.itemgetter(1))
                return demraw

            #data4
            if party=="gop" and raw==False and sort_ascending==True:
                gop_cdict_indi = {}
                gop_cdict_total = {}
                for i in load_data():
                    gop_abbre = i[9]
                    gop_indi = float(i[3])
                    gop_total = float(i[4])

                    if gop_abbre in gop_cdict_indi:
                        gop_cdict_indi[gop_abbre] += gop_indi
                        gop_cdict_total[gop_abbre] += gop_total

                    else:
                        gop_cdict_indi[gop_abbre] = gop_indi
                        gop_cdict_total[gop_abbre] = gop_total
                gopchange = {gop: gop_cdict_indi[gop] / gop_cdict_total[gop]*100 for gop in gop_cdict_indi}

                gop_change = sorted(gopchange.items(), key=operator.itemgetter(1))
                return gop_change
            #data5
            if party=="dem" and raw==True and sort_ascending==False:
                dem_dict = {}
                for i in load_data():
                    dem_votes = i[2]
                    dem_abbre = i[9]
                    if dem_abbre in dem_dict:
                        dem_dict[dem_abbre] += float(dem_votes)
                    else:
                        dem_dict[dem_abbre] = float(dem_votes)
                dem_change = sorted(dem_dict.items(), key=operator.itemgetter(1),reverse=True)
                return dem_change

            #data6
            if party == "gop" and raw == True and sort_ascending == False:
                gop_cdict = {}
                for i in load_data():
                    gop_abbre = i[9]
                    gop_votes = i[3]

                    if gop_abbre in gop_cdict:
                        gop_cdict[gop_abbre] += float(gop_votes)
                    else:
                        gop_cdict[gop_abbre] = float(gop_votes)
                gop_default_sort = sorted(gop_cdict.items(), key=operator.itemgetter(1),reverse=True)
                return gop_default_sort
            #data7
            if party=="gop" and raw==False and sort_ascending == False:
                gop_cdict_indi = {}
                gop_cdict_total = {}
                for i in load_data():
                    gop_abbre = i[9]
                    gop_indi = float(i[3])
                    gop_total = float(i[4])

                    if gop_abbre in gop_cdict_indi:
                        gop_cdict_indi[gop_abbre] += gop_indi
                        gop_cdict_total[gop_abbre] += gop_total

                    else:
                        gop_cdict_indi[gop_abbre] = gop_indi
                        gop_cdict_total[gop_abbre] = gop_total
                gopchange = {gop: gop_cdict_indi[gop] / gop_cdict_total[gop]*100 for gop in gop_cdict_indi}

                gop_raw = sorted(gopchange.items(), key=operator.itemgetter(1),reverse=True)
                return gop_raw
            # data8
            if party=="dem" and raw==False and sort_ascending==False:
                dem_cdict_indi = {}
                dem_cdict_total={}
                for i in load_data():
                    dem_abbre = i[9]
                    dem_indi=float(i[2])
                    dem_total = float(i[4])
                    if dem_abbre in dem_cdict_indi:
                        dem_cdict_indi[dem_abbre] += dem_indi
                        dem_cdict_total[dem_abbre] += dem_total

                    else:
                        dem_cdict_indi[dem_abbre] = dem_indi
                        dem_cdict_total[dem_abbre] = dem_total
                dem= {dem: dem_cdict_indi[dem] / dem_cdict_total[dem]*100 for dem in dem_cdict_indi}
                dempercentage=sorted(dem.items(), key=operator.itemgetter(1),reverse=True)
                return dempercentage


if __name__ == "__main__":

    points = 0
# #
    data = get_data()
    if data[0] == ('WY', 55949.0) and data[-1] == ('CA', 7362490.0):
        points += 3.33
#
    data = get_data(party='gop', raw=False)
    if data[0][0] == 'DC' and int(data[0][1]) == 4 and \
                    data[-1][0] == 'WY' and int(data[-1][1]) == 70:
        points += 3.33
# # #
    data = get_data(party='dem', raw=True, sort_ascending=False)
    if data[0] == ('CA', 7362490.0) and data[-1] == ('WY', 55949.0):
        points += 3.34
# #
    print("points :", points)
