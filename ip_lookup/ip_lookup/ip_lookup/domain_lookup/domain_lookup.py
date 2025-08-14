import whois
import dns.resolver

def domain_lookup(domain):
    print("WHOIS Info:")
    try:
        w = whois.whois(domain)
        for key, value in w.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"WHOIS error: {e}")

    print("\nDNS Records:")
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print(f"A Record: {rdata}")
    except Exception as e:
        print(f"DNS error: {e}")

if __name__ == "__main__":
    target_domain = input("Enter domain: ")
    domain_lookup(target_domain)
