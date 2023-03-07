import json
import requests


global reqapi
reqapi = ''


def APISet(APIkey):
    """드웨인을 사용하시 위한 초기 설정 함수입니다.

    Args:
        APIkey (string): openAPI에서 발급받은 인증 키를 이 곳에 입력합니다.
    """
    global reqapi
    reqapi = APIkey
    return reqapi == APIkey


def APIReq():
    if(len(reqapi)):
        return True
    else:
        print('인증 키가 발급되지 않아 요청할 수 없습니다.')
        return False