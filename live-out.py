import requests

# Function to check if a domain is active
def is_domain_active(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        
        # Check if the response status code indicates success (e.g., 200 OK)
        if response.status_code <= 200:
            return True
    except requests.ConnectionError:
        pass
    except requests.Timeout:
        pass
    except Exception as e:
        pass
    return False

# Input file containing subdomains
input_file = "/home/karthithehacker/recon/dsci/domains.txt"

# Output file to store live URLs
output_file = "/home/karthithehacker/recon/dsci/live.txt"

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            subdomain = line.strip()
            if is_domain_active(subdomain):
                live_url = f"http://{subdomain}"
                print(f"Domain {live_url} is active.")
                outfile.write(f"{live_url}\n")
except FileNotFoundError:
    print(f"Input file '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
