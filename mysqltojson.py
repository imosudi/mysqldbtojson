from dbconnect import engine, alchemyencoder
import json


class flatToCascadedJson(object):
    def __init__(self, dbtable, *args):
        super(flatToCascadedJson, self).__init__(*args) 
        self.dbtable =dbtable
    
    def reformatjson(self):
        dbtable = self.dbtable
        if dbtable not in ['patients', 'labtests', 'transactions', 'user']:
            return {'response':'Not available in database'}, inspect(engine)
        dbtableData = engine.execute('SELECT * FROM {dbtable}' .format(dbtable=dbtable))
        dataList = json.dumps([dict(row) for row in dbtableData], default=alchemyencoder, indent=4)
        with open(f'table_json/{dbtable}.json', 'w+') as file:
            file.write(dataList) 
        file.close()

        if dbtable == 'patients':
           patientList = json.loads(dataList)
           with open(f'table_json/{dbtable}_casded.json', 'w+') as file:
               for i in range(0, len(patientList)) :
                   data2 = json.dumps(
                       {
                           'patient_row_id' :   patientList[i]['patient_id'],
                           'patient_unique_ID': patientList[i]['patientID'],
                           'labsessioncount' :  '',
                           'PatientPersonalDetails' :[
                               {
                                   'patientSex':        patientList[i]['patientSex'],
                                   'patientStatus':     patientList[i]['patientStatus'],
                                   'patientType':       patientList[i]['patientType'],
                                   'ageGrade':          patientList[i]['ageGrade'],
                                   'patientDateofBirth':     patientList[i]['patientDateofBirth'],
                                   'patientTitle':      patientList[i]['patientTitle'],
                                   'patientFirstname':  patientList[i]['patientFirstname'], 
                                   'patientLastname':   patientList[i]['patientLastname'],
                                   'patientMiddlename': patientList[i]['patientMiddlename'],
                                   'patientEmail':      patientList[i]['patientEmail'],
                                   'patientAltEmail':   patientList[i]['patientAltEmail'],
                                   'patientPhonenumber':    patientList[i]['patientPhonenumber'],
                                   'patientAltPhonenumber': patientList[i]['patientAltPhonenumber'],
                                   'patientwhatsappnumber': patientList[i]['patientwhatsappnumber'],
                                   'patientAddress':    patientList[i]['patientAddress'],
                                   'patientCity':       patientList[i]['patientCity'],
                                   'patientState':      patientList[i]['patientState'],
                                   'patientCountry':    patientList[i]['patientCountry'],
                                   'patientpersonalEnroledby':  patientList[i]['patientpersonalEnroledby']
                               }
                           ],
                           'PatientCorporateDetails' :[
                               {
                                   'patientCompanyname':     patientList[i]['patientCompanyname'],
                                   'patientCorporateContactperson':     patientList[i]['patientCorporateContactperson'],
                                   'patientCorporateEmail':     patientList[i]['patientCorporateEmail'],
                                   'patientCorporatePhone':     patientList[i]['patientCorporatePhone'],
                                   'patientCorporatewhatsappnumber':    patientList[i]['patientCorporatewhatsappnumber'],
                                   'patientCorporateAddress':   patientList[i]['patientCorporateAddress'],
                                   'patientCorporateCity':      patientList[i]['patientCorporateCity'],
                                   'patientCorporateState':     patientList[i]['patientCorporateState'],
                                   'patientCorporateCountry':   patientList[i]['patientCorporateCountry'],
                                   'patientCorporateEnroledby': patientList[i]['patientCorporateEnroledby'],
                                   'enrolment_Time':    patientList[i]['enrolment_Time']

                                }
                           ]
                       },
                       indent=2
                   )
                   #print(data2)
                   file.write(data2) 
               file.close()
           #print(patientList)
           return data2, dataList


        elif dbtable == 'labtests' :
            testList = json.loads(dataList)
            with open(f'table_json/{dbtable}_casded.json', 'w+') as file:
               for i in range(0, len(testList)) :
                   data2 = json.dumps(
                       {
                           'test_id':       testList[i]['test_id'],
                           'testType':      testList[i]['testType'],
                           'testBottleType':    testList[i]['testBottleType'],
                           'testName':       testList[i]['testName'],
                           'testmnemonics':      testList[i]['testmnemonics'],
                           'testDetails':        testList[i]['testDetails'],
                           'testTAT':            testList[i]['testTAT'],
                           'testPrice':          testList[i]['testPrice']
                        },
                       indent=2
                   )
                   #print(data2)
                   file.write(data2) 
               file.close()
            return data2, dataList


        elif  dbtable == 'transactions'  :
            transactionList = json.loads(dataList)
            with open(f'table_json/{dbtable}_casded.json', 'w+') as file:
               for i in range(0, len(transactionList)) :
                   data2 = json.dumps(
                       {
                           'transaction_id': 1, 
                           'transactTime':      transactionList[i]['transactTime'],
                           'labSessionTestDetails' : [
                               {
                                   'invoicemnemonics':  transactionList[i]['invoicemnemonics'],
                                   'invoicetestname':   transactionList[i]['invoicetestname'],
                                   'invoiceprice':      transactionList[i]['invoiceprice'], 
                                   'invoicetat':        transactionList[i]['invoicetat']
                               }
                           ],
                           'PatientDetails' : [
                               {
                                   'CurrentpatientID':  transactionList[i]['CurrentpatientID'], 
                                   'fullName':          transactionList[i]['fullName'],
                                   'sex':               transactionList[i]['sex'], 
                                   'billto':            transactionList[i]['billto'],
                                   'testspriority':     transactionList[i]['testspriority'],
                                   'testscheduletype':  transactionList[i]['testscheduletype']
                               }
                           ],
                           'Payment_Reference' : [
                               {
                                   'subtotal':          transactionList[i]['subtotal'],
                                   'discount':          transactionList[i]['discount'],
                                   'equalltax':         transactionList[i]['equalltax'],
                                   'total':             transactionList[i]['total'],
                                   'paymentmethod':     transactionList[i]['paymentmethod'],
                                   'payment':           transactionList[i]['payment'],
                                   'referenceOrchange': transactionList[i]['referenceOrchange'], 
                                   'sessionconfirm':    transactionList[i]['sessionconfirm'],
                                   'paymentconfirm':    transactionList[i]['paymentconfirm'], 
                                   'barcode':           transactionList[i]['barcode'], 
                                   'phlebotomy_processed':  transactionList[i]['phlebotomy_processed']
                               }
                           ],
                           'PaymentPtocessor' : [
                               {
                                   'regtype':           transactionList[i]['regtype'],
                                   'cashier':           transactionList[i]['cashier'], 
                                   'paymentupdateamount':   transactionList[i][ 'paymentupdateamount'], 
                                   'paymentupdateby':       transactionList[i]['paymentupdateby'],
                                   'paymentupdateTime':     transactionList[i]['paymentupdateTime']
                               }
                           ]
                        },
                       indent=2
                   )
                   #print(data2)
                   file.write(data2) 
               file.close()
               #print(transactionList[0])
            return data2, dataList


        elif dbtable == 'user' :
            userList = json.loads(dataList)
            with open(f'table_json/{dbtable}_casded.json', 'w+') as file:
                for i in range(0, len(userList)) :
                    data2 =json.dumps( 
                        {
                            'userID': userList[i]['id'],
                            'loginDetails' :[{
                                'username': userList[i]['email'],
                                'password': userList[i]['password']
                            }],
                            'designation':  userList[i]['designation'],
                            'userDetails' :[{
                                'firstname' :   userList[i]['firstname'], 
                                'lastname':     userList[i]['lastname'], 
                                'email':        userList[i]['email'], 
                                'phonenumber':  userList[i]['phonenumber'],
                                'AlternatePhonenumber' : userList[i]['altnumber'],
                                'location' :[{ 
                                    'location':     userList[i]['location'],
                                     'city' :       userList[i]['city'],
                                     'state':       userList[i]['state'],
                                     'country':     userList[i]['country'] 
                                     }],
                                'zip_code' : userList[i]['zip_code']
                            }],
                            'Analytics' :[{
                                'last_login_at':    userList[i]['last_login_at'],
                                'current_login_at': userList[i]['current_login_at'],
                                'last_login_ip':    userList[i]['last_login_ip'],
                                'current_login_ip': userList[i]['current_login_ip'],
                                'login_count':      userList[i]['login_count'],
                                'confirmed_at':     userList[i]['confirmed_at'],
                                'active':           userList[i]['active']
                            }]
                        }, indent=2
                    )
                    #print(data2)
                    file.write(data2) 
                file.close()
                # End for statement'
            return data2, dataList
        #print(userList[0])
