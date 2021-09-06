# Your imports go here
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
def extract_amount(dirpath: str) -> float:

    logger.info('extract_amount called for dir %s', dirpath)
    # your logic goes here
    file = os.path.join(dirpath, 'ocr.json')
    with open(file,mode='r') as f:
        data = json.load(f)
    blocks = data['Blocks']
    amount = []
    for block in blocks:
        if 'Text' in block.keys():
            #if '$' in block['Text'] or 'USD' in block['Text'] or '.' in block['Text']:
            if '.' in block['Text']:
                amount.append(block['Text'])
    values = []
    digits = list(range(10))
    digits.append('.')
    digits = [str(dig) for dig in digits]
    for amt in amount:
        value = []
        for let in amt:
            if let not in ['U',"S",'D','$'," ",',']:
                value.append(let)
        try:        
            values.append(float(''.join(value)))
        except:
            pass    
    ans = max(values)
    
    return ans
