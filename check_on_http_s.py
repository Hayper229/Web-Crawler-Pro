import requests


try:
    with open("domains.txt", "r") as f:
        domains = f.read().split()
except:
    print(
        "[Error]: File domains.txt not found.\nPlease create file domains.txt with domains\nExample format:\n\ntestphp.vulnweb.com\nvulnweb.com"
    )


try:
    with open("check_domains.txt", "w") as f:
        f.write("\n")
except:
    print("[Error]: File check_domains.txt not found.")


try:
    codes = [200, 201, 300, 301, 302, 303]
    for domain in domains:
        url = f"http://{domain}"
        response = requests.get(url, timeout=10)
        for code in codes:
            if response.status_code == code:
                print(f"{response.url}")
                with open("check_domains.txt", "a") as f:
                    f.write(f"{response.url}\n")
            else:
                pass
except:
    try:
        for domain in domains:
            url = f"https://{domain}"
            response = requests.get(url, timeout=10)
            for code in codes:
                if response.status_code == code:
                    print(f"{response.url}")
                    with open("check_domains.txt", "a") as f:
                        f.write(f"{response.url}\n")

    except:
        pass


print("Results save in check_domains.txt")
