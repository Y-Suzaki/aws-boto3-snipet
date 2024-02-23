import boto3
import uuid

# Agentを使ったサンプル
client = boto3.client(service_name='bedrock-agent-runtime', region_name="us-east-1")

session_id = str(uuid.uuid1())
agent_id = '2OMR2XC0JO'
agent_alias_id = 'GX8YHOBGZK'  # ここにAgentのエイリアスIDを入れる
input_text = "KAGってどんな会社？"

response = client.invoke_agent(
    inputText=input_text,
    agentId=agent_id,
    agentAliasId=agent_alias_id,
    sessionId=session_id,
    enableTrace=False
)

event_stream = response['completion']
for event in event_stream:
    if 'chunk' in event:
        text = event['chunk']['bytes'].decode("utf-8")

print(text)
