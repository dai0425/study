import json
import boto3
import pandas as pd
import io


def lambda_handler(event, context):
    # JSONデータの取得（eventに含まれていると想定）
    # json_data = event["body"]
    # pokemon_data = json.loads(json_data)
    
    # 変換用のリスト
    rows = []

    # for pokemon in event:
    #     row = {
    #         "Weakness": pokemon.get("weakness", ""),
    #         "id": pokemon.get("id",""),
    #         "category":pokemon.get("category",""),
    #         "name":pokemon.get("name",""),
    #         "evolvesTo":pokemon.get("evolvesTo","")
    #     }
    #     rows.append(row)
    # return rows
    for pokemon in event:
        for attack in pokemon.get("attacks", []):
            row = {
                "id":pokemon.get("id",""),
                "category":pokemon.get("category",""),
                "name":pokemon.get("name",""),
                "evolvesTo":pokemon.get("evolvesTo","") ,
                "species":pokemon.get("species","") ,
                "stage":pokemon.get("stage",""),
                "type":pokemon.get("type",""),
                "Weakness": pokemon.get("weakness", ""),
                "HP": pokemon.get("hp", ""),
                "Attack/技": attack.get("name", ""),
                "Damage": attack.get("damage", ""),
                "Attack Cost": ", ".join([f"{k} {int(v)}" for k, v in attack.get("cost", {}).items()]),
                "Converted Energy Cost": attack.get("convertedEnergyCost", ""),
                "Retreat Cost": ", ".join([f"{k} {int(v)}" for k, v in pokemon.get("retreatCost", {}).items()]),
                "Converted Retreat Cost": pokemon.get("convertedRetreatCost", ""),
                "Set Name": pokemon["set"].get("name", ""),
                "Set Release Date": pokemon["set"].get("releaseDate", ""),
                "Set Sub Name": pokemon["set"].get("subName", ""),
                "Flavor Text": pokemon.get("flavor", "")
            }
            rows.append(row)


    # # pandasのデータフレーム作成
    df = pd.DataFrame(rows)

    # Excelファイル名
    excel_file = "pokemon.xlsx"
    bucket_name = "test-shintani-sam"

    # メモリ内にExcelファイルを作成
    excel_buffer = io.BytesIO()
    df.to_excel(excel_buffer, index=False)
    excel_buffer.seek(0)

    # S3にアップロード
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket_name, Key='pokemon.xlsx', Body=excel_buffer.getvalue())
    

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "ExcelファイルをS3にアップロードしました", "file_url": f"s3://{bucket_name}/{excel_file}"})
    }