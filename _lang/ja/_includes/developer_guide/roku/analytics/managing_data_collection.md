{% multi_lang_include developer_guide/prerequisites/roku.md %}

## 以前に保存されたデータを消去する {#wiping-previously-stored-data}

Roku SDKには`wipeData`メソッドが含まれていません。他のBraze SDKの`wipeData()`と機能的に同等のクリーンな状態を作成するには、4つのBrazeレジストリセクションをクリアしてから、SDKを再初期化します。

Braze Roku SDKは、以下のレジストリセクションにデータを保持します。

| セクション | 内容 |
|---------|----------|
| `braze.section.device_id` | Brazeでこのデバイスを識別するために使用されるデバイスUUID。 |
| `braze.section.user_id` | 設定されている場合の外部ユーザー ID。 |
| `braze.section.session` | アクティブなセッションUUID、開始時刻、終了時刻。 |
| `braze.section.config` | キャッシュされたSDK設定とフィーチャーフラグデータ。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="以前に保存されたデータを消去する" }

### ステップ1：レジストリセクションをクリアする {#step-1-clear-the-registry-sections}

[`roRegistry.Delete()`](https://developer.roku.com/docs/references/brightscript/components/roregistry.md)を使用して各Brazeセクションを削除し、`Flush()`を呼び出して変更を保持します。

```brightscript
sub WipeBrazeData()
    registry = CreateObject("roRegistry")
    registry.Delete("braze.section.device_id")
    registry.Delete("braze.section.user_id")
    registry.Delete("braze.section.session")
    registry.Delete("braze.section.config")
    registry.Flush()
end sub
```

### ステップ2：Braze SDKを再初期化する {#step-2-re-initialize-the-braze-sdk}

[Braze SDKを初期化]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku)し直すと、SDKは欠落しているレジストリデータを適切に処理します。

- デバイスIDセクションが空のため、SDKは新しいUUIDを生成し、デバイスを匿名として扱います。
- ユーザー IDセクションが空のため、SDKはデフォルトで匿名ユーザー（空の文字列`""`）になります。
- セッションセクションが空のため、SDKは新しいセッションを開始します。
- 設定セクションが空のため、SDKはサーバーから設定を再取得します。

{% alert note %}
Roku SDKは、レジストリをクリアしてもサーバー側の削除リクエストを生成しません。Brazeからユーザーを削除する必要がある場合は、ユーザーの`external_id`または`braze_id`を使用して[`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)にリクエストを送信してください。
{% endalert %}

## ログアウトとプッシュ登録解除 {#logout-and-unregister-push}

この機能はRoku SDKではまだサポートされていません。