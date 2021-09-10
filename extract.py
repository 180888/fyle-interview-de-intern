import logging
import json
import os
logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''

# dirpath='data/'
def extract_amount(dirpath: str) -> float:
    logger.info('extract_amount called for dir %s', dirpath)
    # Opening JSON file
    
    full_path=os.path.join(dirpath,'ocr.json')
    f = open(full_path,mode='r')
    asd=[]
 
    data = json.load(f)
#     print(type(data))
    for a in reversed(data['Blocks']):
        for key,val in a.items():
            if(key=='Text'):
#                 print(key,val)
                asd.append(val)
                
#     print(asd)
    def isnum(amount1):       
        bad_chars = ['$', 'Rs', ':', "!"]
        print(amount)
        # initializing test string
        test_string = amount1

    #     printing original string
    #     print ("Original String : " + test_string)

    #     using replace() to
    #     remove bad_chars

        for i in bad_chars :
            test_string = test_string.replace(i, '')
            print ("Resultant list is : " + (test_string))
            try:
                amount1=float(test_string)
                variab=isinstance(amount1,float)
            except ValueError:
                return -1
            if variab:
                return amount1
            else:
                return -1
    amount=0
    x=0
    itr1=0
    for itr in asd:
        
        if(itr.upper()=='CREDIT' or itr.upper()=="PAYMENT" or itr.upper()=="TOTAL VALUE" or itr.upper()=="TOTAL" or itr.upper()=="VALUE" or itr.upper()=="AMOUNT" or itr.upper()=="DEBIT" or itr.upper()=="TOTAL AMOUNT"):
            var2=isnum(itr1)
            if(var2!=-1):
                var1=isinstance(var2,float)
                print(var1)
                print("$$$$")
                if var1:
                    x=1
            continue
        if x==1:
            amount=itr1
            break
        itr1=itr

    amount=isnum(amount)
    f.close()
#     print(amount)
   
    logger.info('extract_amount called for dir %s', dirpath)

    

    return amount
    

    

