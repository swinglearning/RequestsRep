import requests











class requestsApi:
    def __init__(self, base_url):
        self.base_url = base_url
    def get(self,url):
        return requests.get(self.base_url+url)
    def post(self, url, payload):
        return requests.post(self.base_url+url,payload)

x=requestsApi("https://reqres.in")
y=x.post("/api/users",{'name': 'Adi', 'job': 'Qa Tester'})
z=x.get("/api/users/495")

print(z.content)



