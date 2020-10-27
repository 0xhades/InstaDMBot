import requests, hashlib, string, random, uuid, time, calendar, re, json, urllib.parse
from sys import platform 

class colors:

    ENDC     = '\33[0m'
    BOLD     = '\33[1m'
    ITALIC   = '\33[3m'
    URL      = '\33[4m'
    BLINK    = '\33[5m'
    BLINK2   = '\33[6m'
    SELECTED = '\33[7m'

    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'

    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'

    GREY    = '\33[90m'
    RED2    = '\33[91m'
    GREEN2  = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2   = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2  = '\33[96m'
    WHITE2  = '\33[97m'

    GREYBG    = '\33[100m'
    REDBG2    = '\33[101m'
    GREENBG2  = '\33[102m'
    YELLOWBG2 = '\33[103m'
    BLUEBG2   = '\33[104m'
    VIOLETBG2 = '\33[105m'
    BEIGEBG2  = '\33[106m'
    WHITEBG2  = '\33[107m'

def escape(string):
    if platform == "win32" or platform == "win64" or platform == "windows":
        return string.replace('/', '\\')
    else: return string
    
def printc(value, color='', nonewline=None, more=''):

    end = '\n'
    if nonewline: end = ''

    if color: print(color + value + colors.ENDC + more, end=end)
    else: print(value + more, end=end)

def inputc(value, color='', more=''):

    if color: return input(color + value + colors.ENDC + more)
    else: return input(value + more) 

def RandomString(n = 10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))

def RandomStringUpper(n = 10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))

def RandomStringChars(n = 10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))

def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result

def printn(args): print(args, end='')
def ClearConsole(): printn("\033[H\033[2J")
def DeleteLine(): printn("\033[F"); print("\033[K")

class account:

    def __init__(self, username: str, password: str, version: str):
        #self.fheaders = self.fetch_headers()
        self.username = username
        self.password = password
        self.cookies = dict()
        self.csrftoken = ''#self.fheaders['csrftoken']
        self.mid = ''#self.fheaders['mid']
        self.UserAgent = self.randDevice().replace('(VERSION)', version)
        self.DeviceID = self.generate_device_id(self.hex_digest(username, password))
        self.guid1 = str(uuid.uuid4())
        self.guid2 = str(uuid.uuid4())
        self.guid3 = str(uuid.uuid4())
        self.checkpoint = bool()
        self.loggedIn = bool()
        self.ds_user_id = str()
        self.threads = list()
        self.last_thread = str()

        headers = {}
        headers['User-Agent'] = self.UserAgent
        headers['Host'] = 'i.instagram.com'
        headers['x-ig-app-locale'] = 'en_SA'
        headers['x-ig-device-locale'] = 'en_SA' 
        headers['x-ig-mapped-locale'] = 'en_US'
        headers['x-pigeon-session-id'] = '29739560-730e-41dc-a065-eae576baba2c'
        headers['x-pigeon-rawclienttime'] = '1599515404.254'
        headers['x-ig-connection-speed'] = '643kbps'
        headers['x-ig-bandwidth-speed-kbps'] = '1236.889'
        headers['x-ig-bandwidth-totalbytes-b'] = '6672937'
        headers['x-ig-bandwidth-totaltime-ms'] = '7015'
        headers['x-ig-app-startup-country'] = 'SA'
        headers['x-bloks-version-id'] = '85e371bf185c688d008ad58d18c84943f3e6d568c4eecd561eb4b0677b1e4c55'
        headers['x-ig-www-claim'] = '0'
        headers['x-bloks-is-layout-rtl'] = 'false'
        headers['x-ig-device-id'] = 'f4aa25e2-1663-4545-afa4-9b770ae5476d'
        headers['x-ig-android-id'] = self.DeviceID
        headers['x-ig-connection-type'] = 'WIFI'
        headers['x-ig-capabilities'] = '3brTvw8='
        headers['x-ig-app-id'] = '567067343352427'
        headers['accept-language'] = 'en-SA, en-US'
        headers['x-mid'] = self.mid
        headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8' 
        headers['accept-encoding'] = 'gzip, deflate'
        headers['x-fb-http-engine'] = 'Liger'
        headers['Connection'] = 'close'
        self.headers = headers
        self.login()

    def fetch_headers(self) -> dict:
        url = 'https://i.instagram.com/api/v1/si/fetch_headers/'

        headers = {}
        headers['Host'] = 'i.instagram.com'
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:80.0) Gecko/20100101 Firefox/80.0'
        headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        headers['Accept-Language'] = 'ar,en-US;q=0.7,en;q=0.3'
        headers['Accept-Encoding'] = 'gzip, deflate, br'
        headers['Connection'] = 'close'

        return requests.get(url, headers=headers).cookies.get_dict()

    def hex_digest(self, *args):
        m = hashlib.md5()
        m.update(b''.join([arg.encode('utf-8') for arg in args]))
        return m.hexdigest()

    def generate_device_id(self, seed):
        volatile_seed = "12345"
        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]

    def randDevice(self) -> str:

        dpi = [
        '480', '320', '640', '515', '120', '160', '240', '800'
        ]
        manufacturer = [
            'HUAWEI', 'Xiaomi', 'samsung', 'OnePlus', 'LGE/lge', 'ZTE', 'HTC',
            'LENOVO', 'MOTOROLA', 'NOKIA', 'OPPO', 'SONY', 'VIVO', 'LAVA'
        ]
        
        randResolution = random.randrange(2, 9) * 180
        lowerResolution = randResolution - 180

        DEVICE = {
            'android_version': random.randrange(18, 25),
            'android_release': f'{random.randrange(1, 7)}.{random.randrange(0, 7)}',
            'dpi': f'{random.choice(dpi)}dpi',
            'resolution': f'{lowerResolution}x{randResolution}',
            'manufacturer': random.choice(manufacturer),
            'device': f'{random.choice(manufacturer)}-{RandomStringUpper(5)}',
            'model': f'{randomStringWithChar(4)}',
            'cpu': f'{RandomStringChars(2)}{random.randrange(1000, 9999)}'
        }

        if random.randrange(0, 2):
            DEVICE['android_release'] = f'{random.randrange(1, 7)}.{random.randrange(0, 7)}.{random.randrange(1, 7)}'

        USER_AGENT_BASE = (
            'Instagram (VERSION) '
            'Android ({android_version}/{android_release}; '
            '{dpi}; {resolution}; {manufacturer}; '
            '{device}; {model}; {cpu}; en_US)'
        )

        return USER_AGENT_BASE.format(**DEVICE)

    def sendCode(self, url, security_code):
        postData = {}
        guid = str(uuid.uuid4())

        postData['security_code'] = security_code
        postData['guid'] = self.guid1
        postData['_csrftoken'] = self.cookies['csrftoken']
        postData['device_id'] = self.DeviceID
        
        payload = {}
        payload['signed_body'] = f'SIGNATURE.{json.dumps(postData)}'

        response = requests.post(url, headers=self.headers, cookies=self.cookies, data=payload, verify=True)
        return response

    def sendMethod(self, url, choice):
        postData = {}
        guid = str(uuid.uuid4())

        postData['choice'] = choice # (Phone number = 0, email = 1)
        postData['guid'] = self.guid1
        postData['_csrftoken'] = self.cookies['csrftoken']
        postData['device_id'] = self.DeviceID

        payload = {}
        payload['signed_body'] = f'SIGNATURE.{json.dumps(postData)}'

        return requests.post(url, headers=self.headers, cookies=self.cookies, data=payload, verify=True)

    def login(self):

        TimeStamp = calendar.timegm(time.gmtime())

        data = {}
        data['jazoest'] = '22713'
        data['phone_id'] = self.guid1
        data['enc_password'] = f'#PWD_INSTAGRAM_BROWSER:0:{TimeStamp}:{self.password}'
        data['_csrftoken'] = self.csrftoken
        data['username'] = self.username
        data['adid'] = self.guid2
        data['guid'] = self.guid3
        data['device_id'] = self.DeviceID
        data['google_tokens'] = '[]'
        data['login_attempt_count'] = '0'

        payload = {}
        payload['signed_body'] = f'SIGNATURE.{json.dumps(data)}'

        response = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=self.headers, data=payload, verify=True)
        if 'logged_in_user' in response.text:
            self.loggedIn = True
            self.cookies = response.cookies.get_dict()
            self.csrftoken = self.cookies['csrftoken']
            self.ds_user_id = self.cookies['ds_user_id']
            printc('Logged In Successfully', colors.GREEN2)
        elif 'challenge_required' in response.text:
            self.checkpoint = True
            self.cookies = response.cookies.get_dict()

            checkpoint_path = re.findall(r'"api_path": "(.*?)"', response.text)[0]
            challenge_url = f'https://i.instagram.com/api/v1{checkpoint_path}'

            getMethods = requests.get(challenge_url, headers=self.headers, cookies=self.cookies)

            phone = bool()
            email = bool()
            try:
                step_name = getMethods.json()['step_name'] 
            except Exception as ex:
                printc('Error, @ctpe', colors.RED)
                print(getMethods.text)
                exit()
           
            if step_name == "select_verify_method":
                if "phone_number" in getMethods.text:
                    phone = True
                if "email" in getMethods.text:
                    email = True
            elif step_name == "delta_login_review":
                choice = 0
            else:
                print(f'Strange step_name: {step_name}\n Send me this {insta}')
                choice = 0

            printc('Challenge is required', colors.RED)
            if email:
                printc('1', colors.YELLOW, more=') email')
            if phone:
                printc('0', colors.YELLOW, more=') phone number')
            choice = inputc('Choose a method to unlock your account: ', colors.YELLOW)
            
            res = self.sendMethod(challenge_url, choice)
            sendto = res.json()['step_data']['contact_point']
            print(f'A code has been sent to {sendto}')
            
            code = inputc('Enter code: ', colors.YELLOW)
            response = self.sendCode(challenge_url, code)
            if 'logged_in_user' in response.text:
                self.loggedIn = True
                self.cookies = response.cookies.get_dict()
                self.csrftoken = self.cookies['csrftoken']
                self.ds_user_id = self.cookies['ds_user_id']
                printc('Logged In Successfully', colors.GREEN2)
            else: printc('Login failure, try again', colors.GREEN2); exit()

        elif "Incorrect Username" in response.text:
            printc("The username you entered doesn't appear to belong to an account.", colors.RED)
            exit()
        elif 'Incorrect password' in response.text:
            printc("The password you entered is incorrect.", colors.RED)
            exit()
        elif 'active user' in response.text:
            printc('Your account has been disabled for violating instagtam\'s terms.', colors.RED)
            exit()
        else:
            printc(f'Unknown error: {response.text}', colors.RED)
            exit()

    def getID(self, us):
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:78.0) Gecko/20100101 Firefox/78.0"
        headers["Host"] = "www.instagram.com"
        headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        headers["Accept-Language"] = "ar,en-US;q=0.7,en;q=0.3"
        headers["Accept-Encoding"] = "gzip, deflate, br"
        headers["Connection"] = "keep-alive"

        res = requests.get(f'https://www.instagram.com/{us}/?__a=1', headers=headers, cookies=self.cookies)
        return res.json()['graphql']['user']['id'] 

    def sendMessage(self, text, threads):
        ''' one thread = send to one conv/group, muliple threads = send to multiple conv/group '''
        thread_ids = ''
    
        if type(threads) == str:
            thread_ids = threads
        else:
            for i in range(len(threads)):
                if i == len(threads) - 1:
                    thread_ids += f'{threads[i]}'
                else:
                    thread_ids += f'{threads[i]},'

        data = {
            "client_context": str(uuid.uuid4()),
            "action": "send_item",
            'thread_ids': f'[{thread_ids}]',
            'text': text,
            'send_attribution': 'direct_thread',
            'device_id': self.DeviceID,
            '_uuid': self.guid2,
            '_csrftoken': self.csrftoken,
            '_uid': self.ds_user_id
        }

        url = "https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/"
        response = requests.post(url, headers=self.headers, data=data, cookies=self.cookies)
        if response.json()['status'] == 'ok':
            printc(f'Sent Successfully to thread/s: ', color=colors.GREEN, more=thread_ids)
        

    def changeGroupName(self, thread_id, name):
        data = {
            'title': f'{name}',
            '_uuid': self.guid2,
            '_csrftoken': self.csrftoken,
            '_uid': self.ds_user_id
        }

        url = f"https://i.instagram.com/api/v1/direct_v2/threads/{thread_id}/update_title/"
        response = requests.post(url, headers=self.headers, data=data, cookies=self.cookies)
        if response.json()['status'] == 'ok':
            printc(f'title of thread {thread_id} changed to: ', color=colors.GREEN, more=name)

    def createThread(self, text, users, name=str()):
        ''' one user = one conv, muliple users = group '''
        recipient_users = ''
    
        if type(users) == str:
            recipient_users = users
        else:
            for i in range(len(users)):
                if i == len(users) - 1:
                    recipient_users += f'{users[i]}'
                else:
                    recipient_users += f'{users[i]},'

        data = {
            "client_context": self.guid1,
            "action": "send_item",
            'recipient_users': f'[[{recipient_users}]]',
            'text': text,
            'send_attribution': 'inbox_new_message',
            'device_id': self.DeviceID,
            '_uuid': self.guid2,
            '_csrftoken': self.csrftoken,
            '_uid': self.ds_user_id
        }

        url = "https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/"
        response = requests.post(url, headers=self.headers, data=data, cookies=self.cookies)
        res = response.json()
        thread_id = res['payload']['thread_id']
        self.threads.append(thread_id)
        self.last_thread = thread_id
        if res['status'] == 'ok':
            printc(f'a new Thread created: ', color=colors.GREEN, more=account.last_thread)
        if name != '': self.changeGroupName(self.last_thread, name)

ClearConsole()
printc('''
    ____  __  _______        __ 
   / __ \/  |/  / __ )____  / /_
  / / / / /|_/ / __  / __ \/ __/
 / /_/ / /  / / /_/ / /_/ / /_  
/_____/_/  /_/_____/\____/\__/  

''', colors.BLUE)

printc(f'By Hades, inst: @0xhades', colors.BLUE2)
print()

username = inputc('Username: ', colors.YELLOW)
password = inputc('Password: ', colors.YELLOW)
t = int(inputc('sleep (milliseconds, best: 300, no? = 0): ', colors.YELLOW))

version = '155.0.0.37.107'

print()
account = account(username, password, version)

target = str()
later = bool()
IDs = []
choice = str()
multi = bool()
texts = []
users = []
groups = bool()
groupname = str()

choice = inputc('Users / From File? (U/F): ', colors.YELLOW)

if choice.lower() == 'u':

    printc('Enter the target/s (u can set multi-Target add (,) )', colors.YELLOW)
    printc('Single: (username) | multi: username1,2,3,... (max 32)', colors.YELLOW)
    target = inputc('Target/s: ', colors.YELLOW)
    print()


    if ',' in target:
        multi = True
        targets = target.replace(' ', '').split(',')
        if len(targets) > 32: later = True; multi = False

    if multi:
        for user in targets:
            ID = account.getID(user)
            printc(f'{user}: {ID}', color=colors.GREEN2)
            IDs.append(ID)
    elif not later: ID = account.getID(target); printc(f'{target}: {ID}', color=colors.GREEN2)

else:

    later = True
    f = open(escape(inputc('Enter the path to file: ', colors.BLUE)))
    for i in f.readlines():
        valid = False
        user = i.replace(' ', '').replace('\n', '').replace('\r', '').strip()
        for char in string.ascii_letters + string.digits:
            if char in user: valid = True
        if user != '' and valid:
            users.append(user)

print()

if multi or later:
    choice = inputc('You want to put all the users in group/s ?(Y/N): ', colors.YELLOW)
    if choice.lower() == 'y':
        groups = True
        choice = inputc('Do you want to name the groups ?(Y/N): ', colors.YELLOW)
        if choice.lower() == 'y': groupname = inputc('Name: ', colors.YELLOW)

choice = inputc('Text / From File? (T/F): ', colors.YELLOW)

if choice.lower() == 't':
    text = inputc('Text (limit is 1000 character):\n', colors.YELLOW)
    if len(text) > 1000: text = text[:1000]
    texts.append(text)
else:
    printc('every line has 1000 character limit', colors.YELLOW)
    printc('So if a line has more than 1000, I\'ll send the first 1000 character', colors.YELLOW)
    f = open(escape(inputc('Enter the path to file: ', colors.BLUE)))
    for i in f.readlines():
        line = i
        if len(line) > 1000: line = line[:1000] 
        texts.append(line)

choice = inputc('Do want to repeat the text (loop)? (Y/N): ', colors.YELLOW)
if choice.lower() == 'y':
    loop = True
    eloop = int(inputc('Enter the number of loops for each line/text (no = 1): ', colors.YELLOW))
    wloop = int(inputc('Enter the number of loops for the whole lines/text (no = 1): ', colors.YELLOW))

print()
if multi:
    
    if groups:
        members_list = IDs
        members = len(members_list)
        group_limit = 32
        groups = 0
        groups_list = []
        if members > group_limit:
            group = []
            for i in range(members):
                if i != 0 and i % group_limit == 0:
                    groups += 1
                    groups_list.append(group)
                    group = []
                    if (members - (groups * group_limit)) < group_limit: break 
                group.append(members_list[i])
            left = (members - (groups * group_limit))
            groups_list.append(members_list[-left:])
            groups += 1
            for group in groups_list:
                account.createThread('By @0xhades', group, groupname)
                time.sleep(t / 1000)
        else:
            account.createThread('By @0xhades', IDs, groupname)
            time.sleep(t / 1000)
    else:
        for user in IDs:
            account.createThread('By @0xhades', user)
            time.sleep(t / 1000)

    for thread in account.threads:

        if loop:
            for lap in range(wloop):
                for text in texts:
                    for lap in range(eloop):
                        account.sendMessage(text, thread)
                        time.sleep(t / 1000)
        else:
            for text in texts:
                account.sendMessage(text, thread)
                time.sleep(t / 1000)

elif later:

    if groups:
        members_list = users
        members = len(members_list)
        group_limit = 32
        groups = 0
        groups_list = []
        if members > group_limit:
            group = []
            for i in range(members):
                if i != 0 and i % group_limit == 0:
                    groups += 1
                    groups_list.append(group)
                    group = []
                    if (members - (groups * group_limit)) < group_limit: break 

                ID = account.getID(members_list[i])
                time.sleep(t / 1000)
                printc(f'{members_list[i]}: {ID}', color=colors.GREEN2)
                group.append(ID)
            left = (members - (groups * group_limit))

            group = []
            for user in members_list[-left:]:
                ID = account.getID(user)
                time.sleep(t / 1000)
                printc(f'{user}: {ID}', color=colors.GREEN2)
                group.append(ID)
            groups_list.append(group)
            groups += 1
            for group in groups_list:
                account.createThread('By @0xhades', group, groupname)
                time.sleep(t / 1000)
        else:
            group = []
            for user in users:
                ID = account.getID(user)
                time.sleep(t / 1000)
                printc(f'{user}: {ID}', color=colors.GREEN2)
                group.append(ID)
            account.createThread('By @0xhades', group, groupname)
            time.sleep(t / 1000)
    else:
        for user in users:
            ID = account.getID(user)
            time.sleep(t / 1000)
            printc(f'{user}: {ID}', color=colors.GREEN2)
            account.createThread('By @0xhades', ID)
            time.sleep(t / 1000)

    for thread in account.threads:
        if loop:
            for lap in range(wloop):
                for text in texts:
                    for _lap in range(eloop):
                        account.sendMessage(text, thread)
                        time.sleep(t / 1000)
        else:
            for text in texts:
                account.sendMessage(text, thread)
                time.sleep(t / 1000)

else:

    account.createThread('By @0xhades', ID)
    
    if loop:
            for lap in range(wloop):
                for text in texts:
                    for _lap in range(eloop):
                        account.sendMessage(text, account.last_thread)
                        time.sleep(t / 1000)
    else:
        for text in texts:
            account.sendMessage(text, last_thread)
            time.sleep(t / 1000)
