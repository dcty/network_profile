import requests
import os
import sys


current_document = os.getcwd() + "/"
print(current_document)


def get_rules(url):
    if type(url) is list:
        return get_multi_rules(url)
    else:
        res = requests.get(url)
        if res.status_code == 200 and len(res.content):
            return res.content
        else:
            return ""


def get_multi_rules(urls):
    rules = []
    for url in urls:
        content = get_rules(url)
        for line in content.splitlines():
            line = line.replace(" ", "").replace(",no-resolve", "", 1).replace("IP-CIDR6", "IP6-CIDR").replace(",AdBlock", "")
            if not line.startswith("#") and len(line) > 0:
                if line.count(",") == 1:
                    rules.append(line+",direct")
                else:
                    rules.append(line)

    print (len(rules))
    print len(set(rules))
    return sorted(set(rules))


def save_rules(rules, file_name):
    new_content = ""
    for rule in rules:
        new_content += rule + "\n"
    return smart_save(file_name, new_content)


def get_file_content(path):
    if not os.path.isfile(path):
        f = open(path, "w")
        f.close()
        return ""
    else:
        f = open(path, "r")
        content = f.read()
        f.close()
        return content


def smart_save(path, new_content):
    old_content = get_file_content(path)
    if old_content != new_content:
        f = open(path, "w")
        f.write(new_content)
        f.close()
    flag = old_content == new_content
    if flag:
        print("above url(s) not need update")
    else:
        print("above url(s) is finish update")
    return flag


def get_rules_and_save(urls, file_name):
    print (urls)
    save_rules(get_rules(urls), file_name)

urls = []
urls.append("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/LocalAreaNetwork.list")
urls.append("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaDomain.list")
urls.append("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaCompanyIp.list")
urls.append("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaIp.list")


# get_rules_and_save(urls, "direct.conf")

urls = []
urls.append("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list")
urls.append("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list")
urls.append("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyList.list")
urls.append("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list")
urls.append("https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyPrivacy.list")
urls.append("https://raw.githubusercontent.com/NobyDa/ND-AD/master/QuantumultX/AD_Block_Plus.txt")
urls.append("https://raw.githubusercontent.com/eHpo1/Rules/master/QuantumultX/Filter/Liby.txt")
urls.append("https://raw.githubusercontent.com/NobyDa/Script/master/QuantumultX/AdRule.list")
# get_rules_and_save(urls, "block.conf")

os.system("git add .")
os.system("git commit -m 'auto commit'")
os.system("git push")