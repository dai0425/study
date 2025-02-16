import uuid
import boto3



def lambda_handler(event, context):
    # Agentへの入力テキスト
    input_text:str = "ポケポケのルールを日本語で3行で説明して"

    # Agentの定義
    agent_id:str = 'X05CQW3SNO' # ご自身のAgentのID
    agent_alias_id:str = 'Q5O4JCX3ZE' # ご自身のAgentのAlias ID
    session_id:str = str(uuid.uuid1()) # 乱数

    # Clientの定義
    client = boto3.client("bedrock-agent-runtime")

    # Agentの実行
    response = client.invoke_agent(
        inputText=input_text,
        agentId=agent_id,
        agentAliasId=agent_alias_id,
        sessionId=session_id,
        enableTrace=False
    )

    # Agent実行結果の取得
    event_stream = response['completion']
    print(event_stream)
    for event in event_stream:        
        if 'chunk' in event:
            data = event['chunk']['bytes'].decode("utf-8")
            print(data)
    
    return data

    