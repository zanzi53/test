# Flask on Wasmer — GitHubインポート用

WasmerのWeb画面からGitHubリポジトリをインポートして公開するFlaskサンプルです。
Wasmer CLIのインストール、手動のパッケージ公開、依存の同梱作業は不要です。
WasmerのPython/Flask自動検出と依存インストールを利用します。

## ファイル構成

```text
app.py                      Flaskアプリのエントリーポイント（app変数）
requirements.txt            Python依存
templates/index.html       あいさつフォーム
tests/test_app.py           Flaskの機能テスト
.github/workflows/test.yml  GitHub Actionsのテスト
```

## GitHubから公開する

1. GitHubでリポジトリを作り、このサンプルの**フォルダの中身**をリポジトリのルートへアップロードします。ルートに`app.py`と`requirements.txt`がある状態にしてください。
2. [Wasmer](https://wasmer.io/)にログインし、アプリの作成画面からGitHubリポジトリのインポートを選びます。
3. GitHubとの連携を許可して、アップロードしたリポジトリを選択します。
4. 公開対象のブランチ（例: `main`）を選び、Python / Flaskとして検出されていることを確認します。
5. アプリ名などを設定し、画面からデプロイを開始します。
6. ビルド・デプロイログを確認し、表示された公開URLを開きます。

Wasmerが`requirements.txt`から依存をインストールし、アプリをパッケージ化して公開します。
エントリーポイントの指定欄がある場合は`app:app`（`app.py`内の`app`）を指定します。
画面の名称は変更される場合があるため、最新の操作は下の公式ガイドを参照してください。

このサンプルには`wasmer.toml`や`app.yaml`を置いていません。
実行環境の生成とアプリ名・所有者の設定は、インポート時にWasmer側で行います。
GitHub Actionsは機能テストだけを実行し、公開はWasmerのGitHub連携が担当します。
公開ブランチへのpushで更新する構成です。

## 動作

| パス | 内容 |
| --- | --- |
| `/` | 名前を入力してあいさつを表示 |
| `/api/hello?name=太郎` | 日本語のあいさつをJSONで返す |
| `/healthz` | `{"status":"ok"}` |

## ローカル開発（任意）

公開だけならローカル環境は不要です。開発する場合はPython 3.12を使います。

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m flask --app app run --port 8080
```

http://localhost:8080 を開きます。

```bash
python -m unittest discover -s tests -v
```

## 検証状況

Flaskの機能テスト5件をローカルで検証しています。
Wasmerへの実際のGitHubインポート・ビルド・公開は未検証です。
自動検出や起動に失敗した場合は、Wasmerのビルド・実行ログで原因を確認してください。

## 公式ドキュメント

- [Gitリポジトリからのデプロイ](https://docs.wasmer.io/edge/git/)
- [Python / Flaskの検出と依存インストール](https://docs.wasmer.io/edge/learn/supported-frameworks-and-languages/)
