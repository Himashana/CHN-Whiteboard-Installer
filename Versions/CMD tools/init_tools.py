try:
    from tqdm import tqdm
    import requests
except e as exception:
    print(e)

try:
    f1 = open('installing-data.txt', 'r')
    f1_data = f1.read()
    f1.close()
except:
    print('Installing Python modules required for CHN Whiteboard...', end='\r')
    f1 = open('installing-data.txt', 'w')
    f1.write('installing-py-modules-required')
    f1.close()
    f2 = open('data000.txt', 'w')
    f2.write('Installing Python modules required for CHN Whiteboard...')
    f2.close()
    quit()

if f1_data == 'installing-py-modules-required':
    f3 = open('data001.txt', 'w')
    f3.write('Getting user input...')
    f3.close()

    f1 = open('installing-data.txt', 'w')
    f1.write('get-user-input')
    f1.close()

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

elif f1_data == 'get-user-input':
    print('Downloading required files...', end='\r')
    
    f4 = open('data002.txt', 'w')
    f4.write('Downloading required files...')
    f4.close()

    f1 = open('installing-data.txt', 'w')
    f1.write('download-files')
    f1.close()

elif f1_data == 'download-files':
    print('Extracting required files...', end='\r')
    
    f5 = open('data003.txt', 'w')
    f5.write('Extracting required files...')
    f5.close()

    f1 = open('installing-data.txt', 'w')
    f1.write('unzip-files')
    f1.close()

elif f1_data == 'unzip-files':
    print('Thanks for installing CHN Whiteboard. Now you can delete the data folder.')
    
    f6 = open('data004.txt', 'w')
    f6.write('Extracting required files...')
    f6.close()

    f1 = open('installing-data.txt', 'w')
    f1.write('success')
    f1.close()
else:
    print('An error occured')
