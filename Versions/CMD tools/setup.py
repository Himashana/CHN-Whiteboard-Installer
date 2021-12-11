try:
    from tqdm import tqdm
    import requests

    print("_______________________________________________________________")
    print("")
    print("        _______      _        _       _       _")
    print("       / /____/     / /_____ / /     /  \    / /")
    print("      / /          /  _____   /     / /\ \  / /")
    

    print('Loading data...', end="\r")
    chunk_size = 1
    download_file_url = "https://github.com/Himashana/CHN-Whiteboard/releases/download/v1.2.0/cmdinstallpackage.zip"
    r = requests.get(download_file_url, stream = True)
    total = int(r.headers['content-length'])

    print("     / /_____     / /      / /     / /  \ \/ /")
    print("    /_______/    /_/      /_/     /_/    \ _/")
    print("             CHN Software Developers")
    print("_______________________________________________________________")
    print("")

    print('4) 1.3.0[preview] - Not available to download\n')
    print('3) 1.2.0[LTS] - Available to download\n')
    print('2) 1.0.1 - End-of-service\n')
    print('1) 1.0.0 - End-of-service\n')
    
    v = input("Please enter the list no of the version of CHN Whiteboard you want to install. Leave it blank if you want to install the latest available version. > ").strip()

    f1 = open('data000.txt', 'w')
    f1.write(v)
    f1.close()
    
    if v == '1':
        print('This version is end-of-service')
    elif v == '2':
        print('This version is end-of-service')
    elif v == '3' or v == '':
        print("starting download operation...", end="\r")
        f2 = open('data001.txt', 'w')
        f2.write(download_file_url)
        f2.close()
        
        with open("cmdinstallpackage.zip", 'wb') as f:
            for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total/chunk_size, unit='KB'):
                f.write(data)
        print("Setup compleated!")
    else:
        print('The version you entered is not available to download!')
except e as exception:
    print(e)
    
input("Click enter to end the setup!")
