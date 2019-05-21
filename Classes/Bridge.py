import requests
from Classes.Tools import Tools
import json
import logging

Result = Tools.Result
Dumps = Tools.dumps
Error = Tools.errors


def send_authentication_email(email, code):
    try:
        # get dynamicurl
        content = requests.post("https://chichiapp.ir:3008/email/authentication/send",
                                data={"Email": email, "Code": code}, verify=False).content
        logging.warning(content)

        # content = json.loads(content)
        return content

    except Exception as ex:
        return Result(False, ex.args)


def gen_token_authentication(user_id):
    try:

        content = requests.post('{0}/system/users/token/add'.format('https://chichiapp.ir:3031'),
                                data={"UserId": user_id}, verify=False).content
        logging.warning(content)
        content = json.loads(content)

        if content["State"]:
            # log
            return content["Description"]
        else:
            return False
    except Exception as ex:
        logging.warning(ex.args)
        return False


def is_auth(user_id, token):
    try:
        content = requests.get('{0}/users/auth/check/{1}/{2}'.format("https://chichiapp.ir:3031",
                                                                     user_id,
                                                                     token), verify=False).content
        content = json.loads(content)

        if content["State"]:
            return True
        else:
            return False
    except Exception as ex:
        logging.warning(ex.args)
        return False


def log_out(user_id, token):
    try:
        content = requests.get(
            '{0}system/users/logoout/{1}/{2}'.format('https://chichiapp.ir:3031/', user_id, token),
            verify=False).content
        content = json.loads(content)
        if content['State']:
            return True
        else:
            return False
    except Exception as ex:
        return Result(False, ex.args)


def get_coins_box_items():
    return {"Box1": 100}


def get_exps_dic():
    return {"Box1": 100}


def get_point_dics():
    return {"Box1": 100}


def get_golden_coin_dics():
    return {"Box1": 100}

# if __name__ == '__main__':
# a = is_auth('5cdc39eeb321f68b2b9e6174','acbca7bcc5da74b4208cd51263bed1e7cf475e6a2e45962cd35f4affbe703f35')
# print(a)
