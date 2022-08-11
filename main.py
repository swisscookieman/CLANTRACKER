import requests
#KEY D'AUTH
headers = {
   "Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImJiOTQyZGExLTYyZjYtNGRhOC1iYjRjLTA3MWExNzcyMTVhYyIsImlhdCI6MTY2MDIzNTYwNCwic3ViIjoiZGV2ZWxvcGVyL2VhMmY0NWQzLWQ1MGUtOWU3MC1lYjdlLTk0NDY4ZmY1Y2RjZSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjkyLjEwNi41MC44NyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.WxgBlubkCZiYdquFVNRdODBBFtAx8wFzZFoWIfbi1V0w2whnXsHNHekhABDM3CI9WvwwV3msIdM0Xq2-1N_r5g"
}
def get_clanlist():
    # list membres du clan AVEC TROP DINFO
    response = requests.get("https://api.clashofclans.com/v1/clans/%232Q2UVGC09/members", headers=headers)
    user_json = response.json()
    memberlist = user_json["items"]
    return memberlist
    #print(user_json["items"])


def get_memberinfo(id):
    # info par membre
    #POUR HAYK: CA MARCHE PAS DSL JE VEUX AUTOMATISER LES REQUESTS AVEC LES DIOFFERENTS ID C'EST DUR DSL
    id2 = str(id)
    adresse = "https://api.clashofclans.com/v1/players/%23"+id2[1:]
    response = requests.get(adresse, headers=headers)
    user_json = response.json()
    memberinfo = user_json
    return memberinfo
    print(memberinfo)

memberlist = get_clanlist()
taglist = []
for i in memberlist:
    # LISTE DES TAGS POUR RECUP LES INFOS 
    name = i["name"]
    tag = i["tag"]
    
    taglist.append(tag)

for member in memberlist:
    # RECUP INFO POUR LE SCORE
    mInfo = get_memberinfo(member)
    print(mInfo)
    #Trophees = mInfo["trophies"]
    #name = mInfo["name"]
    #tag = mInfo["tag"]
    #print("nom:",name," tag:", tag," throphees:",Trophees)
















clanTag = "#2q2uvgc09"
# JoyauxMois + Dons*10 + Trophees*5 + 1000*hdv + 5*jdc + waractivity? -> 5000 + 1000*cwlStars + 150*cwStars + 50*xpLvl
# JOYAUX DONS THROPHEES HDV JDC CWL CW XPLVL