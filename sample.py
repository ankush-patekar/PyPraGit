# storage_inventory={"stor_inventory": {
# "controllers": [{"id": "RAID.Slot.7-1",
# "serial_number": "CALSOFT123","drives": [{"id": "drive1-id","size_gb": 1024}, {"id": "drive2-id","size_gb": 2048}]}]}}
#
# print(storage_inventory[storage_inventory.items()])


'''
#prime number

num = int(input("Enter Number: "))

for i in range(2, num):
    if num % i != 0:
        # i = i + 1
        continue
    else:
        print("entered number is: ",num,"and which is not prime")
        break
else:
    print("entered number is: ",num , "and which is prime")
'''

'''
print prime numbers from 1 to 100


for i in range(2,100):
    for j in range(2,i):
        if (i % j) == 0:
            break
    else:
        print(i)
'''

'''
# factorial

num = int(input(" Enter number: "))
# num = 5
fact = 1
for i in range(num, 0, -1):
    fact = fact * i
print("factorial of",num, 'is :', fact)

'''
'''

# d = { "ITR":{"ITR1":
#               {"CreationInfo":{"SWVersionNo":"R1","SWCreatedBy":"SW10112324","JSONCreatedBy":"SW10112324","JSONCreationDate":"2023-07-16","Digest":"bqtRknOTmi5EjLwbqkFwO8ze8QqTVdkmaBk27skJQ5M=","IntermediaryCity":"Delhi"},"Form_ITR1":{"FormName":"ITR-1","Description":"For Indls having Income from Salary, Pension, family pension and Interest","AssessmentYear":"2023","SchemaVer":"Ver1.0","FormVer":"Ver1.0"},"PersonalInfo":{"AssesseeName":{"FirstName":"ANKUSH","MiddleName":"SUDHAKAR","SurNameOrOrgName":"PATEKAR"},"Address":{"ResidenceNo":"Anjangaon kh","RoadOrStreet":"Anjangaon KH","LocalityOrArea":"SOLAPUR","CityOrTownOrDistrict":"Londewadi B.O","StateCode":"19","CountryCode":"91","PinCode":413214,"CountryCodeMobile":91,"MobileNo":9730732039,"EmailAddress":"patekarankush34@gmail.com"},"PAN":"BOSPP0675K","DOB":"1989-09-22","EmployerCategory":"OTH","AadhaarCardNo":"663308725029"},"FilingStatus":{"ReturnFileSec":11,"NewTaxRegime":"N","SeventhProvisio139":"N","IncrExpAggAmt2LkTrvFrgnCntryFlg":"N","IncrExpAggAmt1LkElctrctyPrYrFlg":"N","clauseiv7provisio139i":"N"},"ITR1_IncomeDeductions":{"AllwncExemptUs10":{"AllwncExemptUs10Dtls":[{"SalNatureDesc":"10(5)","SalOthAmount":83680},{"SalNatureDesc":"10(13A)","SalOthAmount":69084}],"TotalAllwncExemptUs10":152764},"OthersInc":{"OthersIncDtlsOthSrc":[{"OthSrcNatureDesc":"TAX","OthSrcOthAmount":230},{"DividendInc":{"DateRange":{"Upto15Of6":91,"Upto15Of9":0,"Up16Of9To15Of12":0,"Up16Of12To15Of3":0,"Up16Of3To31Of3":0}},"OthSrcNatureDesc":"DIV","OthSrcOthAmount":91},{"OthSrcNatureDesc":"SAV","OthSrcOthAmount":3675}]},"UsrDeductUndChapVIA":{"Section80C":150000,"Section80CCC":0,"Section80CCDEmployeeOrSE":0,"Section80CCD1B":0,"Section80CCDEmployer":0,"Section80D":0,"Section80DD":0,"Section80DDB":0,"Section80E":0,"Section80EE":0,"Section80GG":0,"Section80GGA":0,"Section80GGC":0,"Section80U":0,"Section80TTA":0,"Section80TTB":0,"TotalChapVIADeductions":150000,"Section80G":0},"DeductUndChapVIA":{"Section80C":150000,"Section80CCC":0,"Section80CCDEmployeeOrSE":0,"Section80CCD1B":0,"Section80CCDEmployer":0,"Section80D":0,"Section80DD":0,"Section80DDB":0,"Section80E":0,"Section80EE":0,"Section80EEA":0,"Section80EEB":0,"Section80G":0,"Section80GG":0,"Section80GGA":0,"Section80GGC":0,"Section80U":0,"Section80TTA":0,"Section80TTB":0,"AnyOthSec80CCH":0,"TotalChapVIADeductions":150000},"ExemptIncAgriOthUs10":{"ExemptIncAgriOthUs10Total":0},"GrossSalary":836972,"Salary":836972,"PerquisitesValue":0,"ProfitsInSalary":0,"IncomeNotified89A":0,"IncomeNotifiedOther89A":0,"NetSalary":684208,"DeductionUs16":52500,"DeductionUs16ia":50000,"EntertainmentAlw16ii":0,"ProfessionalTaxUs16iii":2500,"IncomeFromSal":631708,"AnnualValue":0,"StandardDeduction":0,"TotalIncomeOfHP":0,"IncomeOthSrc":3996,"DeductionUs57iia":0,"Increliefus89AOS":0,"GrossTotIncome":635704,"TotalIncome":485700},"ITR1_TaxComputation":{"IntrstPay":{"IntrstPayUs234A":0,"IntrstPayUs234B":0,"IntrstPayUs234C":0,"LateFilingFee234F":0},"TotalTaxPayable":11785,"Rebate87A":11785,"TaxPayableOnRebate":0,"EducationCess":0,"GrossTaxLiability":0,"Section89":0,"NetTaxLiability":0,"TotalIntrstPay":0,"TotTaxPlusIntrstPay":0},"TaxPaid":{"TaxesPaid":{"AdvanceTax":0,"TDS":0,"TCS":0,"SelfAssessmentTax":0,"TotalTaxesPaid":0},"BalTaxPayable":0},"Refund":{"BankAccountDtls":{"AddtnlBankDetails":[{"IFSCCode":"HDFC0001794","BankName":"HDFC BANK","BankAccountNo":"50100125095642","UseForRefund":"true"},{"IFSCCode":"SBIN0018853","BankName":"STATE BANK OF INDIA","BankAccountNo":"031706071130","UseForRefund":"false"}]},"RefundDue":0},"Schedule80G":{"Don100Percent":{"TotDon100PercentCash":0,"TotDon100PercentOtherMode":0,"TotDon100Percent":0,"TotEligibleDon100Percent":0},"Don50PercentNoApprReqd":{"TotDon50PercentNoApprReqdCash":0,"TotDon50PercentNoApprReqdOtherMode":0,"TotDon50PercentNoApprReqd":0,"TotEligibleDon50Percent":0},"Don100PercentApprReqd":{"TotDon100PercentApprReqdCash":0,"TotDon100PercentApprReqdOtherMode":0,"TotDon100PercentApprReqd":0,"TotEligibleDon100PercentApprReqd":0},"Don50PercentApprReqd":{"TotDon50PercentApprReqdCash":0,"TotDon50PercentApprReqdOtherMode":0,"TotDon50PercentApprReqd":0,"TotEligibleDon50PercentApprReqd":0},"TotalDonationsUs80GCash":0,"TotalDonationsUs80GOtherMode":0,"TotalDonationsUs80G":0,"TotalEligibleDonationsUs80G":0},"Schedule80GGA":{"TotalDonationAmtCash80GGA":0,"TotalDonationAmtOtherMode80GGA":0,"TotalDonationsUs80GGA":0,"TotalEligibleDonationAmt80GGA":0},"Schedule80D":{"Sec80DSelfFamSrCtznHealth":{"SeniorCitizenFlag":"S","SelfAndFamily":0,"SelfAndFamilySeniorCitizen":0,"ParentsSeniorCitizenFlag":"P","Parents":0,"ParentsSeniorCitizen":0,"EligibleAmountOfDedn":0}},"TDSonSalaries":{"TotalTDSonSalaries":0},"TDSonOthThanSals":{"TotalTDSonOthThanSals":0},"ScheduleTDS3Dtls":{"TotalTDS3Details":0},"ScheduleTCS":{"TotalSchTCS":0},"TaxPayments":{"TotalTaxPayments":0},"Verification":{"Declaration":{"AssesseeVerName":"ANKUSH SUDHAKAR PATEKAR","FatherName":"SUDHAKAR PATEKAR","AssesseeVerPAN":"BOSPP0675K"},"Capacity":"S","Place":"114.143.187.10"}}}}
student_data = {
    'Alice': {
        'age': 20,
        'major': 'Computer Science',
        'grades': {
            'math': 95,
            'physics': 88,
            'english': 92
        }
    },
    'Bob': {
        'age': 22,
        'major': 'Electrical Engineering',
        'grades': {
            'math': 78,
            'physics': 85,
            'english': 80
        }
    },
    'Charlie': {
        'age': 19,
        'major': 'Biology',
        'grades': {
            'math': 70,
            'physics': 65,
            'english': 75
        }
    }
}

# print(student_data['Alice']['grades']['physics'])
for k,v in student_data.items():
    for k1, v1 in v.items():
        if v1 == dict:
            
                print(v2)
        # print(v1)
        # for k2, v2 in v1:
        #     print(k, k1 )
'''

def arithmatic_ops(a,b):
    add = a + b
    sub = a - b
    muilt = a * b
    try:
        div = a / b
        print(div)
    except:
        print("division by zero not allowed")

    print(add, sub , muilt)

arithmatic_ops(15,0)
