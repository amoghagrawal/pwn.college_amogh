import requests
from itertools import product

slots = [
    ["c", "s"],
    ["g", "q"],
    ["x", "y"],
    ["n", "h", "r"],
    ["x", "v"],
    ["B", "D"],
    ["h", "n", "r"],
    ["Z", "S"]
]

combinations = [''.join(p) for p in product(*slots)]
pastebin_links = [f"https://pastebin.com/{combo}" for combo in combinations]

def check_links(links, timeout=5):
    existing = []
    missing = []
    for link in links:
        try:
            response = requests.get(link, timeout=timeout)
            if response.status_code == 200:
                existing.append(link)
            elif response.status_code == 404:
                missing.append(link)
            else:
                print(f"{link} returned status {response.status_code}")
        except Exception as e:
            print(f"{link} error: {e}")
    return existing, missing

existing_links, missing_links = check_links(pastebin_links)

with open("existing_links.txt", "w") as f:
    for link in existing_links:
        f.write(link + "\n")

with open("missing_links.txt", "w") as f:
    for link in missing_links:
        f.write(link + "\n")

print(f"Done! {len(existing_links)} links exist, {len(missing_links)} links missing.")
print("Results saved to existing_links.txt and missing_links.txt")