import execjs, requests, json

# print(execjs.get().name) # 运行环境
# Node.js (V8)

node = execjs.get()

method = 'GETCITYWEATHER'
city = '上海'
type = 'HOUR'
start_time = '2018-01-25 00:00:00'
end_time = '2018-01-25 23:00:00'

file = 'encryption.js'
ctx = node.compile(open(file).read())

js = 'getEncryptedData("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)
params = ctx.eval(js)

api = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response = requests.post(api, data={'d': params})

js = 'decodeData("{0}")'.format(response.text)
decrypted_data = ctx.eval(js)
data = json.loads(decrypted_data)
print(data)
