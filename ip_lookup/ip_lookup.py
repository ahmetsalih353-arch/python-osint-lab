import requests

def ip_lookup(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    data = response.json()
    for key, value in data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    target_ip = input("Enter IP address: ")
    ip_lookup(target_ip)
