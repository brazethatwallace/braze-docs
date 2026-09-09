## Roku SDKの統合 {#integrating-the-roku-sdk}

### ステップ1：ファイルを追加する {#step-1-add-files}

Braze SDKファイルは、[Braze Roku SDKリポジトリ](https://github.com/braze-inc/braze-roku-sdk)の`sdk_files`ディレクトリにあります。

1. `BrazeSDK.brs`をアプリの`source`ディレクトリに追加します。
2. `BrazeTask.brs`と`BrazeTask.xml`をアプリの`components`ディレクトリに追加します。

### ステップ2：参照を追加する {#step-2-add-references}

以下の`script`要素を使用して、メインシーンに`BrazeSDK.brs`への参照を追加します。

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### ステップ3：設定する {#step-3-configure}

`main.brs`内で、グローバルノードにBrazeの設定を行います。

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

[SDKエンドポイント]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)とAPIキーは、Brazeダッシュボードで確認できます。

### ステップ4：Brazeを初期化する {#step-4-initialize-braze}

Brazeインスタンスを初期化します。

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## オプション設定 {#optional-configurations}

### ログ {#logging}

Brazeの統合をデバッグするには、RokuデバッグコンソールでBrazeのログを確認できます。詳しくは、Roku Developersの[Debugging code](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md)を参照してください。