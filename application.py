from flask import Flask, Response, request, jsonify
import requests
app = Flask(__name__)
import json
from xmlrpc import client

@app.route('/')
def index():
    return 'Index Home Page'

@app.route('/login', methods=['GET', 'POST'])
def connect():
    if request.method == 'POST':
        print (request.json)
        request_data = request.json
        username = request_data['email']
        password = request_data['password']
        print(username + ' pass ' + password)
        params = {
            'db': 'bel-20191013',
            'login': username,
            'password': password
        }
        odoo_url = 'http://localhost:8069/web/session/authenticate'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Content-Length': str(len(json.dumps(params)))
        }
        # headers = json.dumps(headers)

        response = requests.post(url = odoo_url, data= json.dumps({'params': params}) , headers= headers)

        print(response.json())
        # dump(response)

        return jsonify(response.json())
    else: 
        print('GET Request')

    # elif request.method == 'POST':
    #     print (request.json)
    #     request_data = request.json
    #     username_form = request_data['email']
    #     password_form = request_data['password']
    #     print(username_form + ' pass ' + password_form)
    #     response = json.dumps({'username' : username_form, 'password': password_form})
    #     return jsonify(response)

@app.route('/mobile/shop_list', methods=['GET', 'POST'])
def shop_list():
    params = {
        'db': 'bel-20191013',
        'login': 'admin@amarbay.com',
        'password': '123'
    }
    url = 'http://localhost:8069/mobile/shop_list'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': 'website_lang=en_US; _ga=GA1.1.33133517.1567570711; session_id=f1b1e668dd482c9de2a9ceb326632d8d6e214fff'
    }
    # headers = json.dumps(headers)

    response = requests.post(url = url, data = json.dumps({'jsonrpc': '2.0', 'method': 'call', 'params': params}) , headers = headers)

    shop_data = response.json()
    shop_list = json.loads(shop_data['result'])

    print(shop_data['result'])

    return jsonify(shop_list)

@app.route('/connect')
def login():
    url = 'http://localhost:8069'
    db = 'bel-20191013'
    username = 'admin@amarbay.com'
    password = '123'
    common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    version =  common.version()
    print(version)
    uid = common.authenticate(db, username, password, {})
    session = common.get_session_info(db, username, password, {})
    print(session)
    models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    shop_data =  models.execute_kw(db, uid, password, 'stock.location', 'shop_list', {'raise_exception': False})
    # print(type(response))

    response=Response(shop_data,content_type='application/json; charset=utf-8')
    response.headers.add('content-length',len(shop_data))
    response.status_code=200
    # return json.loads(shop_data)
    
    # response = str(uid)
    return str(uid)

@app.route('/shop_list')
def get_shop_list():
    shop_data ="""{"result": "success", "shop_list": [{"data": [{"contact_no": "01787673802", "shop_id": "SHOP004", "shop_manager": "Mr. Kaylesh Chandra Mondol", "shop_name": "RAPA PLAZA"}, {"contact_no": "01787673806", "shop_id": "SHOP008", "shop_manager": "Md. Anowar Hossen Jony", "shop_name": "BALAKA"}, {"contact_no": "01787673803", "shop_id": "SHOP005", "shop_manager": "Md. Alomgir Hossain", "shop_name": "SHIMANTO SQUARE"}, {"contact_no": "01787673868", "shop_id": "SHOP070", "shop_manager": "Md. Mosharaf Hossain", "shop_name": "NARSINGDI"}, {"contact_no": "01787673805", "shop_id": "SHOP007", "shop_manager": "Md. Perves Mosharof", "shop_name": "SHYAMOLI"}, {"contact_no": "01787673834", "shop_id": "SHOP036", "shop_manager": "Mahbub Mia", "shop_name": "DOYAGONJ"}, {"contact_no": "01313098904", "shop_id": "SHOP081", "shop_manager": "Md. Sahab Uddin", "shop_name": "RING ROAD"}, {"contact_no": "01787673839", "shop_id": "SHOP041", "shop_manager": "Shariful Islam", "shop_name": "JATRABARI"}, {"contact_no": "01787673830", "shop_id": "SHOP032", "shop_manager": "Aftab Uddin Ahmed", "shop_name": "NARAYANGANJ"}, {"contact_no": "01787673835", "shop_id": "SHOP037", "shop_manager": "Md. Mahafuzur Rahman Sabbir", "shop_name": "GULISTAN"}, {"contact_no": "01787673807", "shop_id": "SHOP009", "shop_manager": "Ibrahim Khalil", "shop_name": "43, ELEPHANT ROAD"}, {"contact_no": "01787673800", "shop_id": "SHOP001", "shop_manager": "Emon Khan", "shop_name": "98, ELEPHANT ROAD"}], "territory_name": "DHAKA WEST"}, {"data": [{"contact_no": "01787673827", "shop_id": "SHOP029", "shop_manager": "Md. Rafiqur Rahman", "shop_name": "PALLABI"}, {"contact_no": "01787673801", "shop_id": "SHOP002", "shop_manager": "Md. Abdur Rahman", "shop_name": "BASHUNDHARA CITY - 02"}, {"contact_no": "01787673853", "shop_id": "SHOP055", "shop_manager": "Md. Maynul Islam", "shop_name": "MANIKGANJ"}, {"contact_no": "01787673808", "shop_id": "SHOP010", "shop_manager": "Robin Khan", "shop_name": "FARMGATE - 01"}, {"contact_no": "+8801787673855", "shop_id": "SHOP080", "shop_manager": "Rubel Nath", "shop_name": "MIRPUR - 10"}, {"contact_no": "01787673865", "shop_id": "SHOP069", "shop_manager": "Md. Samidul Islam", "shop_name": "SAVAR - 02"}, {"contact_no": "01787673804", "shop_id": "SHOP006", "shop_manager": "Shankar Chandra Howlader", "shop_name": "FARMGATE - 02"}, {"contact_no": "01787673852", "shop_id": "SHOP054", "shop_manager": "Md. Miraj Hossain Mazumder", "shop_name": "MUKTABANGLA"}, {"contact_no": "01787673821", "shop_id": "SHOP023", "shop_manager": "Rafiqur Rahman", "shop_name": "SHEWRAPARA"}, {"contact_no": "01787673856", "shop_id": "SHOP057", "shop_manager": "H. M. Rana", "shop_name": "SAVAR - 01"}, {"contact_no": "01787673822", "shop_id": "SHOP024", "shop_manager": "Md. Mijanur Rahman", "shop_name": "SHAH ALI PLAZA"}, {"contact_no": "01787673814", "shop_id": "SHOP016", "shop_manager": "Joynal Abedin Shajol", "shop_name": "BANANI"}, {"contact_no": "01787673869", "shop_id": "SHOP072", "shop_manager": "Md. Al Masum Shekh", "shop_name": "SAVAR - 03"}, {"contact_no": "01787673871", "shop_id": "SHOP003", "shop_manager": "Abu Bashar Kaiyum", "shop_name": "BASHUNDHARA CITY - 01"}], "territory_name": "DHAKA CENTRAL"}, {"data": [{"contact_no": "01787673818", "shop_id": "SHOP020", "shop_manager": "Rasel Hossain", "shop_name": "ASHKONA"}, {"contact_no": "+8801787673864", "shop_id": "SHOP077", "shop_manager": "Md. Abdul Haque", "shop_name": "UTTARA - 03"}, {"contact_no": "01787673816", "shop_id": "SHOP018", "shop_manager": "Md. Rasel Ahmed", "shop_name": "KAKRAIL"}, {"contact_no": "01787673815", "shop_id": "SHOP017", "shop_manager": "Md. Maruf", "shop_name": "BADDA - 01"}, {"contact_no": "01787673813", "shop_id": "SHOP015", "shop_manager": "Md. Mohi Uddin", "shop_name": "BANASREE"}, {"contact_no": "'01787673811", "shop_id": "SHOP013", "shop_manager": "Md. Ibrahim Khalil", "shop_name": "UTTARA - 01"}, {"contact_no": "01313098902", "shop_id": "SHOP094", "shop_manager": "Md. Hasibul Hasan", "shop_name": "HAZIPARA"}, {"contact_no": "01787673810", "shop_id": "SHOP012", "shop_manager": "Md. Hasibul Hasan", "shop_name": "RAMPURA"}, {"contact_no": "01787673842", "shop_id": "SHOP044", "shop_manager": "Amarat Hossain Milon", "shop_name": "KONABARI"}, {"contact_no": "01787673812", "shop_id": "SHOP014", "shop_manager": "MD. Bahar Uddin", "shop_name": "UTTARA - 02"}, {"contact_no": "01787673862", "shop_id": "SHOP067", "shop_manager": "Achinta Mondal", "shop_name": "MAWNA"}, {"contact_no": "01787673843", "shop_id": "SHOP045", "shop_manager": "Moshiur Rahman", "shop_name": "JOYDEBPUR"}, {"contact_no": "01787673817", "shop_id": "SHOP019", "shop_manager": "Ohidul Islam", "shop_name": "BADDA - 02"}, {"contact_no": "01787673809", "shop_id": "SHOP011", "shop_manager": "Shamsuddin Md Muhtasim", "shop_name": "JAMUNA FUTURE PARK"}], "territory_name": "DHAKA EAST"}, {"data": [{"contact_no": "01313098901", "shop_id": "SHOP082", "shop_manager": "Kawsar Kazi", "shop_name": "COX'S BAZAR - 02"}, {"contact_no": "01787673850", "shop_id": "SHOP052", "shop_manager": "Md. Wahiduzzaman (Jalil)", "shop_name": "BHAIRAB"}, {"contact_no": "01787673831", "shop_id": "SHOP033", "shop_manager": "Md.Saifuddin", "shop_name": "CHAWKBAZAR"}, {"contact_no": "01787673846", "shop_id": "SHOP048", "shop_manager": "Abu Sayed", "shop_name": "SREEMANGAL"}, {"contact_no": "01787673841", "shop_id": "SHOP043", "shop_manager": "Syed Abul Hasan", "shop_name": "UPASHAHAR"}, {"contact_no": "01787673844", "shop_id": "SHOP046", "shop_manager": "Md. Hafizul Islam", "shop_name": "ZINDABAZAR"}, {"contact_no": "01787673870", "shop_id": "SHOP073", "shop_manager": "Kazi Jahirul Islam", "shop_name": "HALISHAHAR"}, {"contact_no": "01787673845", "shop_id": "SHOP047", "shop_manager": "Kobir Ahmed", "shop_name": "MOULVIBAZAR - 02"}, {"contact_no": "01787673832", "shop_id": "SHOP034", "shop_manager": "Md. Fazar Ali", "shop_name": "COMILLA"}, {"contact_no": "01787673840", "shop_id": "SHOP042", "shop_manager": "Md Nazim uddin", "shop_name": "CITY CENTER"}, {"contact_no": "01787673829", "shop_id": "SHOP031", "shop_manager": "Golam Faruk", "shop_name": "COX'S BAZAR - 01"}, {"contact_no": "01787673863", "shop_id": "SHOP068", "shop_manager": "Faruk Ahmed", "shop_name": "FENI"}, {"contact_no": "01787673838", "shop_id": "SHOP040", "shop_manager": "Pankaj ", "shop_name": "BRAHMANBARIA"}, {"contact_no": false, "shop_id": "SHOP083", "shop_manager": false, "shop_name": "CHAPAINAWABGANJ"}, {"contact_no": "01787673849", "shop_id": "SHOP051", "shop_manager": "Numan Ahmad Juyel", "shop_name": "AMBARKHANA-02"}, {"contact_no": "01787673836", "shop_id": "SHOP038", "shop_manager": "Sohidul Islam", "shop_name": "O.R. NIZAM ROAD"}, {"contact_no": "01787673833", "shop_id": "SHOP035", "shop_manager": "Md. Shahidul Islam Mazumder", "shop_name": "BIPONI BITAN"}], "territory_name": "CTG & SYLHET"}, {"data": [{"contact_no": "+8801787673872", "shop_id": "SHOP074", "shop_manager": false, "shop_name": "BOGRA - 02"}, {"contact_no": "01787673820", "shop_id": "SHOP022", "shop_manager": "Md. Perves Mosharof", "shop_name": "TANGAIL"}, {"contact_no": "01787673867", "shop_id": "SHOP071", "shop_manager": "Md. Shariful Islam", "shop_name": "RANGPUR - 02"}, {"contact_no": "01787673825", "shop_id": "SHOP027", "shop_manager": "Shahidul Islam", "shop_name": "DINAJPUR"}, {"contact_no": "01787673826", "shop_id": "SHOP028", "shop_manager": "Mohammad Ali", "shop_name": "BOGRA - 01"}, {"contact_no": "01787673848", "shop_id": "SHOP050", "shop_manager": "Md. Imran Hossain", "shop_name": "JAMALPUR - 01"}, {"contact_no": "01787673847", "shop_id": "SHOP049", "shop_manager": "Md. Harun Ar Rashid", "shop_name": "MYMENSINGH - 01"}, {"contact_no": "+8801787673873", "shop_id": "SHOP079", "shop_manager": "Md. Kazi Rustom", "shop_name": "JAMALPUR - 02"}, {"contact_no": "01787673874", "shop_id": "SHOP078", "shop_manager": "Ahidul Islam Khan", "shop_name": "MYMENSINGH - 02"}, {"contact_no": "01787673823", "shop_id": "SHOP025", "shop_manager": "Shamim Osman", "shop_name": "JOYPURHAT"}, {"contact_no": false, "shop_id": "SHOP084", "shop_manager": false, "shop_name": "POLICE PLAZA"}, {"contact_no": "01787673861", "shop_id": "SHOP061", "shop_manager": "Md. Jasim Uddin", "shop_name": "RAJSHAHI - 02"}, {"contact_no": "01787673819", "shop_id": "SHOP021", "shop_manager": "Md. Shafiqul Islam Khan", "shop_name": "RAJSHAHI - 01"}, {"contact_no": "01787673824", "shop_id": "SHOP026", "shop_manager": "Mr. Sarafat ", "shop_name": "RANGPUR - 01"}, {"contact_no": "01787673828", "shop_id": "SHOP030", "shop_manager": "Md. Nadir Hossain", "shop_name": "SHIRAJGANJ"}], "territory_name": "NORTH BENGAL"}, {"data": [{"contact_no": "01313098905", "shop_id": "SHOP095", "shop_manager": "Md. Rasel Howlader", "shop_name": "BARISAL - 02"}, {"contact_no": "01787673860", "shop_id": "SHOP059", "shop_manager": "Modon Kumar Mondol", "shop_name": "CHUADANGA"}, {"contact_no": "01787673851", "shop_id": "SHOP053", "shop_manager": "Md. Rasel Mridha", "shop_name": "KHULNA"}, {"contact_no": "01787673854", "shop_id": "SHOP056", "shop_manager": "Aminul Islam", "shop_name": "BARISAL - 01"}, {"contact_no": "01313098903", "shop_id": "SHOP093", "shop_manager": "Mohammad Ismail", "shop_name": "KUSHTIA"}, {"contact_no": "01787673858", "shop_id": "SHOP058", "shop_manager": "Ashraful Islam", "shop_name": "RAJBARI"}], "territory_name": "SOUTH BENGAL"}, {"data": [{"contact_no": false, "shop_id": "SHOP064", "shop_manager": false, "shop_name": "DEFECTIVE SUPPLIER"}, {"contact_no": false, "shop_id": "SHOP062", "shop_manager": false, "shop_name": "GUARANTEE"}, {"contact_no": false, "shop_id": "SHOP076", "shop_manager": false, "shop_name": "Head Office"}, {"contact_no": "01709995722", "shop_id": "SHOP000", "shop_manager": "Babul Das", "shop_name": "CDC"}], "territory_name": "Territory 100"}, {"data": [{"contact_no": false, "shop_id": "SHOP066", "shop_manager": false, "shop_name": "FAIR SHOP"}, {"contact_no": false, "shop_id": "SHOP063", "shop_manager": "Md. Saifur Rahman", "shop_name": "E-COMMERCE"}, {"contact_no": false, "shop_id": "SHOP060", "shop_manager": "Corporate user", "shop_name": "CORPORATE"}, {"contact_no": false, "shop_id": "SHOP065", "shop_manager": "Ashifuzzaman", "shop_name": "WHOLE SALE"}], "territory_name": "Territory 200"}, {"data": [{"contact_no": false, "shop_id": "SHOP086", "shop_manager": false, "shop_name": "STOCK SP - 02"}, {"contact_no": false, "shop_id": "SHOP090", "shop_manager": false, "shop_name": "STOCK SP - 06"}, {"contact_no": false, "shop_id": "SHOP091", "shop_manager": false, "shop_name": "STOCK SP - 07"}, {"contact_no": false, "shop_id": "SHOP092", "shop_manager": false, "shop_name": "STOCK SP - 01"}, {"contact_no": false, "shop_id": "SHOP089", "shop_manager": false, "shop_name": "STOCK SP - 05"}, {"contact_no": false, "shop_id": "SHOP088", "shop_manager": false, "shop_name": "STOCK SP - 04"}, {"contact_no": false, "shop_id": "SHOP087", "shop_manager": false, "shop_name": "STOCK SP - 03"}], "territory_name": "Territory 300"}]}"""
    response=Response(shop_data,content_type='application/json; charset=utf-8')
    response.headers.add('content-length',len(shop_data))
    response.status_code=200
    return response