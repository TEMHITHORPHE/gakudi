from requests import request
import  json



# class FLUTTER_WAVE_API():
#     API_ENDPOINTS = {
#         # "create_account_and_virtual_account" : "https://fsi.ng/api/v1/flutterwave/v3/virtual-account-numbers",
#         "https://fsi.ng/api/v1/flutterwave/v3/virtual-account-numbers",
#         # "flutter_get_virtual_account" : "https://fsi.ng/api/v1/flutterwave/v3/virtual-account-numbers/RND_2641579516055928?order_ref=RND_2641579516055928",
#         # "verify_transactions": "https://fsi.ng/api/v1/flutterwave/v3/transactions/1/verify?id=1"
#     }


#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'dskjdks',
#         'sandbox-key' : '4WfcTIAd0FbUBq8lGeWY8PhkdqTDnjMr1648661157'
#         }


#     def createNewUserAndVirtualAccount(self, user:dict[str, str]):

#         payload = json.dumps({
#         "email": "support@pennywise.com",
#         "is_permanent": True,
#         "bvn": "12345678901",
#         "tx_ref": "VA12",
#         "phonenumber": "08097237654",
#         "firstname": "Regina Wise",
#         "lastname": "Hue",
#         "narration": "Hue Regina-Penny"})

#         # response = request("POST", url=self.API_ENDPOINTS["verify_transactions"], headers=self.headers, data=json.dumps(user));
#         # # print(user);
#         # print(response.text);

#         response = request("POST", "https://fsi.ng/api/v1/flutterwave/v3/virtual-account-numbers" , headers=self.headers, data=json.dumps(user));
#         # print(user);
#         print(response.text);






# class WOVEN_FINACE_API():

#     API_ENDPOINTS = {
#         "create_account_and_virtual_account" : "https://fsi.ng/api/woven/vnubans/create_customer",
#         "lookup_account_details" : "https://fsi.ng/api/woven/vnubans/:vnuban",
#     }


#     headers = {
#         'Content-Type': 'application/json',
#         # 'Authorization': 'dskjdks',
#         'requestId': '2596b022-0d64-4359-a7d1-d35b981aa1ca',
#         'api-secret': 'vb_ls_bfac75fe54a952841971b6918d06aeb2659523dc92d6',
#         'sandbox-key' : '4WfcTIAd0FbUBq8lGeWY8PhkdqTDnjMr1648661157'
#         }


#     def createNewUserAndVirtualAccount(self, user:dict[str, str]):

#         payload = json.dumps({
#             "customer_reference": user["userID"],
#             "name": user["phoneNo"],
#             "email": "support@gakudi.com",
#             "mobile_number": user["phoneNo"],
#             "use_frequency": "100",
#         });

#         response = request("POST", self.API_ENDPOINTS["create_account_and_virtual_account"], headers=self.headers, data=json.dumps(payload));
#         # print(user);
#         # response = request("POST", self.API_ENDPOINTS["create_account_and_virtual_account"], headers=self.headers, data=payload);

#         print(response.json());
#         return response.json();


# if __name__ == "__main__":
#     import uuid
#     userFlutter = {
#     # "email": "johntochukwumax@gmail.com",
#     # "is_permanent": True,
#     # "bvn": "22386020296",
#     # #   "tx_ref": "VA12",
#     # "phonenumber": "08132853731",
#     # "firstname": "Martin Hills",
#     # "lastname": "John",
#     # "narration": "John Hills Martin"
#     }

#     userWave = {
#         "customer_reference" : str(uuid.uuid4()),
#         "mobile_number" : "098",
#         # "passwd" : "password",
#         # "balance" : 0,
#         "name" : "tyfdeq 01",
#         "email": "eqfw@gakudi.com",
#         "use_frequency": 100,
#         "max_amount": 3000,
#         # "walletAddress" : accountDetails;
#         # "account_name": 'Penny Wisemen'
#     } 
#     wfAPI = WOVEN_FINACE_API();
#     wfAPI.createNewUserAndVirtualAccount(userWave);

#     # fwAPI = FLUTTER_WAVE_API();
#     # fwAPI.createNewUserAndVirtualAccount(userWave);

