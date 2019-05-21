import requests






def singup():
    a = requests.post("https://chichiapp.ir:3002/users/signup",json={"PhoneNumber":"09119518867",
                                                                     "FirstName":'امین',
                                                                     "LastName":"جمال"},verify=False).content
    print(a)


def verify():
    a = requests.get("http://localhost:3002/users/phonenumber/verification/09119518867/3717").content
    print(a)


if __name__ == '__main__':
    verify()