import requests
import time
import ddddocr


def verify_code():
    while True:
        img = session.get(
            f'https://bill.shfft.com/verify/ajax/getverifyCodeImg?d={int(round(time.time() * 1000))}').content
        code = ocr.classification(img)
        res = session.post(
            f"https://bill.shfft.com/verify/ajax/checkVerifyCode?verifyCode={code}").text
        if res == "success":
            return code
        time.sleep(1)


def search_bill_info_by_account(bill_no):
    url = 'https://bill.shfft.com/bill/ajax/searchBillInfoByAccount'
    params = {
        'billNo': bill_no,
        'billOrgId': '888880000502900',
        'productId': '1000000210',
        'billNoType': 0,
        'startMonth': '202208',
        'endMonth': '202208',
        'checked': 'false',
        'displayType': 3,
        'oweFlag': 1,
        'verifyCode': verify_code()
    }
    res = session.post(url=url, params=params).json()
    print(res)


if __name__ == '__main__':
    ocr = ddddocr.DdddOcr()
    session = requests.session()
    search_bill_info_by_account("xxxxxxxx") # 输入待查询户号
