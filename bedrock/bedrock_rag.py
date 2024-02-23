import boto3

# RAGを使ったサンプル
agent = boto3.client(service_name='bedrock-agent-runtime', region_name="us-east-1")

model_id = "anthropic.claude-v2:1"
model_arn = f'arn:aws:bedrock:us-east-1::foundation-model/{model_id}'
kb_id = "NCEEYSCDUO"         # ナレッジベースのID
query = "KAGってどんな会社？"   # 質問

# Bedrock Agent APIをクライアントから実行する
response = agent.retrieve_and_generate(
    input={
        'text': query
    },
    retrieveAndGenerateConfiguration={
        'type': 'KNOWLEDGE_BASE',
        'knowledgeBaseConfiguration': {
            'knowledgeBaseId': kb_id,
            'modelArn': model_arn
        }
    },
)

generated_text = response['output']['text']
print(generated_text)
