from langchain.llms import Bedrock
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


# LangChainのLLMモジュールを設定する
llm = Bedrock(
    model_id="anthropic.claude-v2:1"
)

# LangChainの会話チェーンを設定する
conversation = ConversationChain(
    llm=llm, verbose=True, memory=ConversationBufferMemory()
)

# LangChainの会話チェーンにプロンプトを渡して実行する
result = conversation.predict(input="ガンダムSEEDの主人公はだれですか？")

# 実行結果を画面に出力する
print(result)
