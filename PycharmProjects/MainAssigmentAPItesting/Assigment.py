import json

import openpyxl
import requests
from BaseClass import test_Base
from config import Test_Data

baseUrl = 'https://api-nodejs-todolist.herokuapp.com'


class Test_API_User:
    def test_registeruser(self):
        try:
            log = test_Base.getLogger()
            url = baseUrl + '/user/register'
            headers = {'content-type': 'application/json'}
            dataObj = Test_Data()
            dictionaryData = dataObj.getTestData("registeruser")
            name = str(dictionaryData['name'])
            email = str(dictionaryData['email'])
            password = str(dictionaryData['password'])
            age = int(dictionaryData['age'])
            payload = {
                "name": "" + name + "",
                "email": "" + email + "",
                "password": "" + password + "",
                "age": age
            }
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            statuscode = response.status_code
            print(statuscode)
            log.info(statuscode)
            assert statuscode == 201
            log.info("Successfully Resgistered")
        except Exception as e:
            print("Exception occured", e)

    def test_Loginuser(self):
        try:
            log = test_Base.getLogger()
            url = baseUrl + '/user/login'
            headers = {'content-type': 'application/json'}
            dataObj = Test_Data()
            dictionaryData = dataObj.getTestData("loginuser")
            email = str(dictionaryData['email'])
            password = str(dictionaryData['password'])
            payload = {
                "email": "" + email + "",
                "password": "" + password + ""
            }
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            statuscode = response.status_code
            data = response.json()
            bearer_token = data['token']
            print(statuscode)
            print(bearer_token)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfully Logged in")
            return bearer_token
        except Exception as e:
            print("Exception occured", e)

    def test_Logoutuser(self):
        try:
            log = test_Base.getLogger()
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            url = baseUrl + '/user/logout'
            headers = {'content-type': 'application/json',
                       'Authorization': 'Bearer ' + bearertoken
                       }

            payload = {}
            response = requests.post(url, data=payload, headers=headers)
            statuscode = response.status_code
            data = response.json()
            print(statuscode)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfully Logged out")
        except Exception as e:
            print("Exception occured", e)

    def test_LoginViaAuth(self):
        try:
            log = test_Base.getLogger()
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            url = baseUrl + '/user/me'
            headers = {'content-type': 'application/json',
                       'Authorization': 'Bearer ' + bearertoken
                       }

            payload = {}
            response = requests.get(url, data=payload, headers=headers)
            statuscode = response.status_code
            data = response.json()
            print(statuscode)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfully Logged in")
        except Exception as e:
            print("Exception occured", e)

    def test_UpdateUser(self):
        try:
            log = test_Base.getLogger()
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            url = baseUrl + '/user/me'
            headers = {'content-type': 'application/json',
                       'Authorization': 'Bearer ' + bearertoken
                       }
            dataObj = Test_Data()
            dictionaryData = dataObj.getTestData("updateuser")
            age = int(dictionaryData['age'])
            payload = {
                "age": age
            }
            response = requests.put(url, data=json.dumps(payload), headers=headers)
            statuscode = response.status_code
            data = response.json()
            print(statuscode)
            print(data)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfully Updated User")
        except Exception as e:
            print("Exception occured", e)

    def test_UploadImage(self):
        try:
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            log = test_Base.getLogger()
            url = baseUrl + '/user/me/avatar'
            headers = {
                'Authorization': 'Bearer ' + bearertoken
            }

            payload = {}
            files = [
                ('avatar', (
                    'blog-header.jpeg', open('/Users/mohdsalekhan/PycharmProjects/MainAssigmentAPI/blog-header.jpeg',
                                             'rb'), 'image/jpeg'))
            ]
            response = requests.post(url, data=payload, headers=headers, files=files)
            statuscode = response.status_code
            data = response.json()
            print(statuscode)
            print(data)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfully Uploaded image")
        except Exception as e:
            print("Exception occured", e)

    def test_GetUserImage(self):
        try:
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            log = test_Base.getLogger()
            url = baseUrl + '/user/5ddccbec6b55da001759722c/avatar'
            headers = {'content-type': 'application/json',
                       'Authorization': 'Bearer ' + bearertoken
                       }
            payload = {}
            response = requests.get(url, data=payload, headers=headers)
            statuscode = response.status_code
            print(statuscode)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfull!!")
        except Exception as e:
            print("Exception occured!!", e)

    def test_DeleteUserImage(self):
        try:
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            log = test_Base.getLogger()
            url = baseUrl + '/user/me/avatar'
            headers = {'content-type': 'application/json',
                       'Authorization': 'Bearer ' + bearertoken
                       }
            payload = {}
            response = requests.delete(url, data=payload, headers=headers)
            statuscode = response.status_code
            print(statuscode)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfull!!")
        except Exception as e:
            print("Exception occured!!", e)

    def test_addMultipleTask(self):
        ref = Test_API_User()
        dataObj = Test_Data()
        task_dict = dataObj.getBulkValue("addtasks")
        for key in task_dict:
            try:
                ref.test_AddTask(task_dict[key])
            except Exception as e:
                print(e)

    def test_AddTask(self, addtask):
        try:
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            log = test_Base.getLogger()
            url = baseUrl + '/task'
            headers = {'content-type': 'application/json',
                       'Authorization': 'Bearer ' + bearertoken
                       }
            payload = {
                "description": "" + addtask + ""

            }
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            statuscode = response.status_code
            data = response.json()
            print(statuscode)
            log.info(statuscode)
            print(data)
            assert statuscode == 201
            log.info("Successfull!!")
        except Exception as e:
            print("Exception occured!!", e)

    def test_GetAllTask(self):
        try:
            log = test_Base.getLogger()
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            url = baseUrl + '/task'
            headers = {'content-type': 'application/json',
                       'Authorization': 'Bearer ' + bearertoken
                       }

            payload = {}
            response = requests.get(url, data=payload, headers=headers)
            statuscode = response.status_code
            data = response.json()
            print(data)
            print(statuscode)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfull!!")
        except Exception as e:
            print("Exception occured!!", e)

    def test_GetTaskByID(self):
        try:
            log = test_Base.getLogger()
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            url = baseUrl + '/task/620a5b123238b70017d5fd88'
            headers = {'content-type': 'application/json',
                       'Authorization': 'Bearer ' + bearertoken
                       }

            payload = {}
            response = requests.get(url, data=payload, headers=headers)
            statuscode = response.status_code
            data = response.json()
            print(data)
            print(statuscode)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfull!!")
        except Exception as e:
            print("Exception occured!!", e)

    def test_UpdateTaskID(self):
        try:
            log = test_Base.getLogger()
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            url = baseUrl + '/task/620a5b123238b70017d5fd88'

            headers = {'content-type': 'application/json',
                       'Authorization': 'Bearer ' + bearertoken
                       }
            payload = {
                "completed": True
            }
            response = requests.put(url, data=json.dumps(payload), headers=headers)
            statuscode = response.status_code
            data = response.json()
            print(statuscode)
            print(data)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfully Updated User")
        except Exception as e:
            print("Exception occured", e)

    def test_DeleteUserTask(self):
        try:
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            log = test_Base.getLogger()
            url = baseUrl + '/task/620a54a13238b70017d5fd6c'
            headers = {'content-type': 'application/json',
                       'Authorization': 'Bearer ' + bearertoken
                       }
            payload = {}
            response = requests.delete(url, data=payload, headers=headers)
            statuscode = response.status_code
            print(statuscode)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfull!!")
        except Exception as e:
            print("Exception occured!!", e)

    def test_GetTaskByPagination(self):
        try:
            log = test_Base.getLogger()
            ref = Test_API_User()
            bearertoken = ref.test_Loginuser()
            dataObj = Test_Data()
            dictionaryData = dataObj.getTestData("page")
            limit = str(dictionaryData['limit'])
            skip = str(dictionaryData['skip'])
            param = {"limit": "" + limit + "", "skip": "" + skip + ""}
            url = baseUrl + '/task?'
            headers = {'content-type': 'application/json',
                       'Authorization': 'Bearer ' + bearertoken
                       }

            payload = {}
            response = requests.get(url, data=payload, headers=headers, params=param)
            statuscode = response.status_code
            data = response.json()
            print(data)
            descriptions = data['data']
            print(statuscode)
            print(descriptions)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfull!!")
        except Exception as e:
            print("Exception occured!!", e)




