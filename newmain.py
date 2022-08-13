
# -*- coding: utf-8 -*-

# Si on veut juste update status de gdc: changer status a 1
status = 1
#Si on veut juste update status de gdc: changer status a 2




import json

import requests, csv

csv_file = open('CoC_314159.csv', 'w', encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Scoooooooore: ", "Nom:","Tag: ","Trophees: ", "Hdv: ", "Joyaux: ", "Dons: ", "Jdc: ", "War Activity: ", "clanWarStars: ", "Xp Lvl: ","Ldc: "])

#update data
# csv_file2 = open('War_status_314159.csv', 'w', encoding="utf-8")
# csv_writer2 = csv.writer(csv_file2)
# csv_writer2.writerow(["Ancien Score de gdc", "Ancien Score de ldc"])

#KEY D'AUTH
headers = {
    "Accept" : "application/json",
    "Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImJiOTQyZGExLTYyZjYtNGRhOC1iYjRjLTA3MWExNzcyMTVhYyIsImlhdCI6MTY2MDIzNTYwNCwic3ViIjoiZGV2ZWxvcGVyL2VhMmY0NWQzLWQ1MGUtOWU3MC1lYjdlLTk0NDY4ZmY1Y2RjZSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjkyLjEwNi41MC44NyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.WxgBlubkCZiYdquFVNRdODBBFtAx8wFzZFoWIfbi1V0w2whnXsHNHekhABDM3CI9WvwwV3msIdM0Xq2-1N_r5g"
}
def get_clanlist():
    # list membres du clan AVEC TROP DINFO
    response = requests.get("https://api.clashofclans.com/v1/clans/%232Q2UVGC09/members", headers=headers)
    user_json = response.json()
    #print(user_json)
    memberlist = user_json["items"]
    
    return memberlist



def get_memberinfo(id):

    id2 = str(id)
    adresse = "https://api.clashofclans.com/v1/players/%23"+id2[1:]
    response = requests.get(adresse, headers=headers)
    user_json = response.json()
    memberinfo = user_json
    return memberinfo
    #print(memberinfo)
    
    
#pas important, c'est juste peut etre pour apres ameliorer le code
# def update(clanWarStars, ldc):
#     with open('CoC_314159.csv', encoding="utf-8") as file:

#         reader = csv.reader(file)
#         print(writer)
#         for row in reader:
#             if len(row)!=0:
#                 print(row[0])
                
#             else:
#                 continue
            
memberlist = get_clanlist()
#print(len(memberlist))
taglist = []
for i in memberlist:
    # LISTE DES TAGS POUR RECUP LES INFOS 
    name = i["name"]
    tag = i["tag"]
    
    taglist.append(tag)
#print(taglist)

for member in taglist:
    #RECUP INFO POUR LE SCORE
    mInfo = get_memberinfo(member)
    #print(mInfo)
    trophees = mInfo["trophies"]#3
    name = mInfo["name"]#1
    tag = mInfo["tag"]#2
    hdv = mInfo["townHallLevel"]#4
    joyaux = mInfo["achievements"][-1]["value"]#5
    dons = mInfo["donations"]#6
    jdc = mInfo["achievements"][31]["value"]#7
    warActivity = 0#8
    Actif = False
    if Actif == True:
        warActivity = 5000
    else:
        warActivity = 0
    role = mInfo["role"]
    if role == "coLeader":
        clBonus = 25000
    clanWarStars = mInfo["warStars"]#9
    xpLvl = mInfo["expLevel"]#10
    ldc = mInfo["achievements"][-10]["value"]#11
    print("nom:",name," tag:", tag,"Trophees: ",trophees, "Hdv: ", hdv, "Joyaux: ", joyaux, "Dons: ", dons, "Jdc: ", jdc, "War Activity: ", warActivity, "clanWarStars: ", clanWarStars, "Xp Lvl: ", xpLvl,"Ldc: ", ldc, "Role", role)
    Score = joyaux + dons*10 + trophees*5 + hdv*1000+ 5*jdc+warActivity+clanWarStars*150 + ldc*1000+xpLvl*50+clBonus
    print(Score)

    csv_writer.writerow([Score, name, tag, trophees, hdv, joyaux, dons, jdc, warActivity, clanWarStars, xpLvl, ldc])


clanTag = "#2Q2UVGC09"
# JoyauxMois done + Dons*10 done+ Trophees*5 done+ 1000*hdv done+ 5*jdc done+ waractivity? -> 5000 + 1000*cwlStars done+ 150*cwStars done+ 50*xpLvl done
# JOYAUX DONS THROPHEES HDV JDC CWL CW XPLVL
csv_file.close()
# csv_file2.close()