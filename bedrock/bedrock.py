import boto3
import json

bedrock = boto3.client(service_name='bedrock-runtime')
# Bedrock APIに渡す必要のある変数を事前に定義する
accept = 'application/json'
contentType = 'application/json'
modelId = 'anthropic.claude-v2:1'

body = json.dumps({
    "prompt": "\n\nHuman: ガンダムSEEDの登場人物、ラクス・クラインの恋人は？\n\nAssistant:",  # ここにAIへの質問を入れる
    "max_tokens_to_sample": 300,
})

response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
response_body = json.loads(response.get('body').read())
print(response_body.get('completion'))
