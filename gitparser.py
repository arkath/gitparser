import requests
import json

def parse(org,n_pop_repo,m_top_commiters):
    if org == None or org == "":
        raise "please provide the organisation name"
    if n_pop_repo == None or n_pop_repo == 0:
        n_pop_repo = 1
    if m_top_commiters == None or m_top_commiters == 0:
        m_top_commiters = 1
    repo = get_repos(org,n_pop_repo,m_top_commiters)
    print repo

def get_repos(org,npr,tmc):
    url="https://api.github.com/orgs/"+str(org)+"/repos"
    response=requests.get(url)
    repodata=json.loads(response.content)
    if "message" in repodata:
        raise Exception("IP is blocked try again from other ip address authentication model isnt been done in this code")
    sorted_repodata = sorted(repodata, key=lambda k:k['forks'], reverse=True)
    res = list()
    if int(npr) <= len(sorted_repodata):
        for i in xrange(npr):
            res.append(final_dict(sorted_repodata[i],tmc))
    else:
        for i in xrange(len(sorted_repodata)):
            res.append(final_dict(sorted_repodata[i],tmc))
    return json.dumps(res)



def final_dict(dictonary,tmc):
    data = {}
    data["name"] = dictonary["name"]
    data["full_name"] = dictonary["full_name"]
    data["forks"] = dictonary["forks"]
    data["committees_info"] = get_top_commitors(dictonary["contributors_url"],tmc)
    return data


def committees_dict(dictonary):
    d = {}
    d["git_username"] = dictonary["login"]
    d["user_contributions"] = dictonary["contributions"]
    user_info = get_user_details(dictonary["url"])
    data = dict(user_info.items() + d.items())
    return data


def get_user_details(url):
    response = requests.get(url)
    user_data = json.loads(response.content)
    data = {}
    data["users_full_name"] = user_data["name"]
    data["public_repos"] = user_data["public_repos"]
    return data

def get_top_commitors(url,num):
    response = requests.get(url)
    sorted_committees_data = json.loads(response.content)
    res = list()
    if int(num) <= len(sorted_committees_data):
        for i in xrange(num):
            res.append(committees_dict(sorted_committees_data[i]))
    else:
        for i in xrange(len(sorted_committees_data)):
            res.append(committees_dict(sorted_committees_data[i]))
    return res

