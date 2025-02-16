import json
import boto3

bedrock_runtime = boto3.client('bedrock-runtime')
prompt = "bedrockを始めて使うおばあちゃんにわかるようにも解説して"

def lambda_handler(event, context):
    # 各種パラメーターの指定
    modelId = 'amazon.titan-text-express-v1'  
    accept = 'application/json'
    contentType = 'application/json'

    # リクエストBODYの指定
    body = json.dumps({
                "inputText": prompt,
                "textGenerationConfig": {
                    "maxTokenCount": 3072,
                    "stopSequences": [],
                    "temperature": 0.7,
                    "topP": 0.9
                }
    })


    response = bedrock_runtime.invoke_model(
        modelId=modelId,
        accept=accept,
        contentType=contentType,
        body=body
    )

    # APIレスポンスからBODYを取り出す
    response_body = json.loads(response.get('body').read())

    # レスポンスBODYから応答テキストを取り出す
    print(response_body)
    # outputText = response_body.get('completions')[0].get('data').get('text')

    output_text = response_body['results'][0]['outputText']
    print(output_text)


    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',  # CORS を許可
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'text': output_text
        })
    }