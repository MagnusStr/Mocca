import os
import wget

class Webmodule:             
    global aux
    aux = 1
    
    def checar_winget(self):
        dir = "C:\\Program Files\\WindowsApps\\"
        winget = "Microsoft.DesktopAppInstaller_1.19.10173.0_x64__8wekyb3d8bbwe"
        list = os.listdir(dir)
        for i in list:
            if(i == winget):
                print("Winget instalado na máquina!\n")
                aux = 1
            else:
                aux = 0

        if(aux == 1):
            pass
        else:
            print("Winget não instalado na máquina\n")
            print("Baixando winget!\n")
            url = "https://github.com/microsoft/winget-cli/releases/download/v1.4.10173/Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle"
            wget.download(url)
        


    def download_apps(self):
        print("Baixando os programas...\n")
        with open("database.txt") as f:
            lines = f.readlines()
            for url in lines:
                wget.download(url)

teste = Webmodule()
teste.download_apps()