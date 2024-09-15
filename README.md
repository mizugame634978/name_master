# NameMaster
1. chatGPTに変数名、関数名を考えてもらうオフラインGUIプログラム

1. 自分でopenAIのapiキーを取得し、それをプログラム中に書くことで動作する

1. 起動には```pip install openai```が必要
# なぜ作ったのか
普段自分がchatGPTに変数名や関数名を考えてもらうときに少ない文字で聞くと、望んだ答えが１回で帰ってこないことがそこそこあったため。
# 工夫した点
jsonのような形でプロンプトを作って、それでchatGPTに質問を送った。
# 実際の画面
![image](https://user-images.githubusercontent.com/83535489/230809198-07e63d99-aaba-44ac-ab82-a9345d05418a.png)
# 参考
- chatGPT
- https://saasis.jp/2023/03/06/%E9%81%82%E3%81%AB%E5%85%AC%E9%96%8B%E3%81%95%E3%82%8C%E3%81%9Fchatgpt-api%E3%81%A8%E3%81%AF%EF%BC%9F-%E5%88%A9%E7%94%A8%E3%81%99%E3%82%8B%E3%81%BE%E3%81%A7%E3%81%AE%E6%B5%81%E3%82%8C%E3%80%90/

# バージョン
python 3.10.7