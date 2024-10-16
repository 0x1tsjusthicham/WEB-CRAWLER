import urllib.parse
import requests, re, urllib, optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="target_url", help="Specify URL, -h for help")
    options, arguments = parser.parse_args()

    if not options.target_url:
        parser.error("[-] Please Specify Url -h for help")
    
    return options.target_url

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

def check_available_domains(target_url):
    with open("./Subdomain.txt") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = word + "." + target_url
            response = request(test_url)
            if response:
                print("Discover domaine --> " + test_url)

def check_available_files(target_url):
    with open("./files.txt") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = target_url + "/" + word
            response = request(test_url)
            if response:
                print("Discover file --> " + test_url)

def get_links(url):
    response = request(url)
    return re.findall('(?:href=")(.*?)"', response.content.decode())

target_links = []
target_url = get_arguments()

def crawl(url):
    href_links = get_links(url)

    for link in href_links:
        link = urllib.parse.urljoin(url, link)
        if "#" in link:
            link = link.split("#")[0]

        if url in link not in target_links:
            target_links.append(link)
            print(link)