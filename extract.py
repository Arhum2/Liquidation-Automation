import re
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import ollama

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-CA,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'FVSID=49-903178fe-d2a0-4cae-9b55-3dea19da498b; WFDC=IAD; i18nPrefs=lang%3Den-CA; CSNUtId=53ae9db0-be9b-4697-b964-c3a9a3764ba3; ExCSNUtId=53ae9db0-be9b-4697-b964-c3a9a3764ba3; vid=23f584c2-66dd-fbb2-80dd-9bfa81143b02; SFSID=7030ee7577607069374d34b6a40a4276; canary=0; serverUAInfo=%7B%22browser%22%3A%22Google%20Chrome%22%2C%22browserVersion%22%3A128%2C%22OS%22%3A%22Windows%22%2C%22OSVersion%22%3A%22%22%2C%22isMobile%22%3Afalse%2C%22isTablet%22%3Afalse%2C%22isTouch%22%3Afalse%7D; CSN_CSRF=a3de6124a5a8882fb53cbf10004d51614313b0033441fb514f2ae1de9c68284a; postalCode=M4C%201B5; pxcts=069fe1c5-6e19-11ef-aaea-235aba82a253; _pxvid=069fd7b5-6e19-11ef-aaea-c6baf8f02a2c; waychatShouldShowChatWindow=false; CSN=g_countryCode%3DCA%26g_zip%3DM4C%25201B5; __ssid=fdfe4133cde97cb34217d63c71a07a7; cjConsent=MHxOfDB8Tnww; cjUser=30d782c7-119f-49b8-877c-f6c1cacc322b; rskxRunCookie=0; rCookie=pm5zjvwhpps7u9zb2hrjt9m0tz07ln; __attentive_id=44b1b7aae55c49e8aa315b9b3d7889ba; _attn_=eyJ1Ijoie1wiY29cIjoxNzI1ODIzOTI1NjMxLFwidW9cIjoxNzI1ODIzOTI1NjMxLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjQ0YjFiN2FhZTU1YzQ5ZThhYTMxNWI5YjNkNzg4OWJhXCJ9In0=; __attentive_cco=1725823925632; __wid=782462873; _gcl_au=1.1.1101014872.1725823926; __attentive_dv=1; __attentive_ss_referrer=ORGANIC; _gid=GA1.2.844828548.1725823927; _gat_gtag_UA_70989678_1=1; hideGoogleYolo=true; _px3=35e3685a2bd62377e80a4dadf5774a8d582a1492bd44010b1e93cd0f0561f579:Nukbzsqe0WxJVsHhGiRyl11dCLT29oe0gquUVxfuAUB51J/9DvAXZ7O9auzoQ7/908JaVMTuIktpi7x1QGQ6Ig==:1000:0kDgqtwCrOjtkTKy/AW0M9G2dCkdECtN9DibBbiiKu1tPkvXEmLSO8U8AAJOIjDOukmdtYy9XYuicGjRkfdv+V0kqaBr276s0e06sd5iWZ8wYsDsOQKs+tx9ld5ttLzJ/tBiEps7nd/sPGtj0UT/FLH6YAIUg99cmuwre0tPTA/ksPNh5dtPDmGsLnR75OnfunsL0j5FvzTByb+qtEWx/8QzC6Uwmq8qzfgiNRnT6rg=; lastRskxRun=1725823942134; _uetsid=07dda8506e1911efafe4f962c5730d96; _uetvid=07ddac706e1911efab00db843c986920; CSNPersist=page_of_visit%3D7; _ga_G1TPJHGL53=GS1.1.1725823926.1.1.1725823942.44.0.0; __attentive_pv=2; _ga=GA1.2.804046048.1725823926; forterToken=c6ae4329dc2949218824ae42eb6639da_1725823942000__UDF43-m4_20ck_Uvd5PY9QW0Q%3D-13819-v2; forterToken=c6ae4329dc2949218824ae42eb6639da_1725823942000__UDF43-m4_20ck_Uvd5PY9QW0Q%3D-13819-v2; otx=I/WEwmbd+8OA3Zv6gUpEAg==',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

# Test link TODO: grab link from clipboard
r = requests.get('https://www.wayfair.ca/furniture/pdp/lark-manor-hilbert-upholstered-low-profile-platform-bed-frame-with-headboard-c011005079.html?piid=2081062955%2C2081158349', headers=headers)


soup = BeautifulSoup(r.text, 'html.parser')

# def get_english_text(soup):
#     tags_to_keep = {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head'} 

#     english_text = ""

#     for tag in soup.findAll(True):
#         if tag.text != '':
#             if tag.name in tags_to_keep:
#                 english_text += " ".join([word.strip() for word in tag.text.split() if is_english(word)]) 

#     return english_text

# def is_english(word):
#     return re.match(r'^[a-zA-Z0-9_]*$', word)

# english_text = get_english_text(soup)
# #print(english_text)

prompt = "Take this piece of text that I extracted from a furniture listing. Extract all the key details and return only the extracted product description and nothing else. remove all new line characters. here is the text:" + soup.text

response = ollama.chat(model='llama3.1', messages=[{
    'role': 'user',
    'content': prompt,
},
])

print(response['message'])
