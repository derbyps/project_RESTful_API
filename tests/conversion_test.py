from unittest import mock
from unittest.mock import patch
from . import app, client, cache, create_token, init_database
import json

class TestConversion():
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code
            
            def json(self):
                return self.json_data
        if len(args) > 0:
            if args[0] == app.config['URL_MATAUANG']:
                return MockResponse({"status":"success","formula":"(amount * this.rates[from]) / this.rates[to]","currency_rates":{"USD":1,"EUR":1.11193,"GBP":1.30635,"CAD":0.766164,"ARS":0.0167424,"AUD":0.689864,"BRL":0.24416,"CLP":0.00129228,"CNY":0.144514,"CYP":0.397899,"CZK":0.044014,"DKK":0.148803,"EEK":0.0706676,"HKD":0.12875,"HUF":0.00332968,"ISK":0.00811755,"INR":0.0140899,"JMD":0.00756433,"JPY":0.00913556,"LVL":1.57329,"LTL":0.320236,"MTL":0.293496,"MXN":0.0532027,"NZD":0.663446,"NOK":0.112534,"PLN":0.262483,"SGD":0.741364,"SKK":21.5517,"SIT":175.439,"ZAR":0.0696308,"KRW":0.000862997,"SEK":0.10528,"CHF":1.02829,"TWD":0.0333588,"UYU":0.0267444,"MYR":0.245293,"BSD":1,"CRC":0.00175119,"RON":0.232698,"PHP":0.0197802,"AED":0.272294,"VEB":0.000100125,"IDR":0.0000726927,"TRY":0.170153,"THB":0.0330542,"TTD":0.147974,"ILS":0.288655,"SYP":0.00194175,"XCD":0.370038,"COP":0.000305672,"RUB":0.0163863,"HRK":0.149493,"KZT":0.00261756,"TZS":0.000435194,"XPT":980.171,"SAR":0.266667,"NIO":0.0296252,"LAK":0.000112574,"OMR":2.60078,"AMD":0.00208737,"CDF":0.000595358,"KPW":0.00111095,"SPL":6,"KES":0.00986433,"ZWD":0.00276319,"KHR":0.000245523,"MVR":0.0646417,"GTQ":0.129725,"BZD":0.49631,"BYR":0.000047203,"LYD":0.714477,"DZD":0.00836241,"BIF":0.00052928,"GIP":1.30635,"BOB":0.144697,"XOF":0.00169513,"STD":0.0000451005,"NGN":0.00276304,"PGK":0.293966,"ERN":0.0666667,"MWK":0.00135682,"CUP":0.0377358,"GMD":0.0195425,"CVE":0.0100837,"BTN":0.0140899,"XAF":0.00169513,"UGX":0.000272335,"MAD":0.104339,"MNT":0.000365509,"LSL":0.0696308,"XAG":18.123,"TOP":0.423786,"SHP":1.30635,"RSD":0.00944918,"HTG":0.010514,"MGA":0.000270721,"MZN":0.016141,"FKP":1.30635,"BWP":0.0937236,"HNL":0.0406242,"PYG":0.000153838,"JEP":1.30635,"EGP":0.0625224,"LBP":0.00066335,"ANG":0.559396,"WST":0.373265,"TVD":0.689864,"GYD":0.00480107,"GGP":1.30635,"NPR":0.00876512,"KMF":0.00226018,"IRR":0.0000237917,"XPD":2120,"SRD":0.134134,"TMM":0.0000570902,"SZL":0.0696308,"MOP":0.125,"BMD":1,"XPF":0.00931801,"ETB":0.0310496,"JOD":1.41044,"MDL":0.0578908,"MRO":0.00266288,"YER":0.00399623,"BAM":0.568523,"AWG":0.558659,"PEN":0.301427,"VEF":0.100125,"SLL":0.000102951,"KYD":1.21929,"AOA":0.00206499,"TND":0.355717,"TJS":0.103138,"SCR":0.0727999,"LKR":0.00551473,"DJF":0.00561844,"GNF":0.00010495,"VUV":0.0086502,"SDG":0.0221692,"IMP":1.30635,"GEL":0.34663,"FJD":0.46278,"DOP":0.0188002,"XDR":1.37979,"MUR":0.0273312,"MMK":0.000685193,"LRD":0.00528699,"BBD":0.5,"ZMK":0.0000714938,"XAU":1562.28,"VND":0.0000431401,"UAH":0.0417808,"TMT":0.285451,"IQD":0.000839991,"BGN":0.568523,"KGS":0.0143606,"RWF":0.00107037,"BHD":2.65957,"UZS":0.000105198,"PKR":0.00645544,"MKD":0.018053,"AFN":0.0129257,"NAD":0.0696308,"BDT":0.0117843,"AZN":0.588692,"SOS":0.00171881,"QAR":0.274725,"PAB":1,"CUC":1,"SVC":0.114286,"SBD":0.121104,"ALL":0.00911075,"BND":0.741364,"KWD":3.28874,"GHS":0.176186,"ZMW":0.0714938,"XBT":8036.99,"NTD":0.0337206,"BYN":0.47203,"CNH":0.144632,"MRU":0.0266288,"STN":0.0451005,"VES":0.000015042,"MXV":0.340722}}
                    , 200)
           
        else:
            return MockResponse(None, 404)
        
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_check_weather(self, get_mock, client):
        token = create_token()
        res = client.get('/conversion/con',
                         query_string={'from':"USD"},
                         headers={'Authorization':'Bearer ' + token})
        
        res_json = json.loads(res.data)
        assert res.status_code == 200
