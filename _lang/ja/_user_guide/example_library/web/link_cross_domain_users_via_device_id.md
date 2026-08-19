---
nav_title: クロスドメインの Web SDK ユーザーをリンクする
article_title: デバイス ID を使用してクロスドメインの Web SDK ユーザーをリンクする
page_order: 1
page_type: reference
description: "Braze Web SDKのデバイス ID を Kitchenerie のマーケティングサイトから別のショップドメインに渡し、匿名アクティビティが1つのユーザープロファイルを共有するようにします。"
---

# デバイス ID を使用してクロスドメインの Web SDK ユーザーをリンクする {#link-cross-domain-web-sdk-users-through-device-id}

> 2つのドメインでCookieを共有できない場合、Braze Web SDKのデバイス ID をリンク先 URL に渡すことで、両方のサイトの匿名セッションを同じ Braze ユーザープロファイルにマッピングできます。

## この例について {#about-this-example}

架空のキッチン用品小売店 Kitchenerie は、マーケティングサイト（`kitchenerie.com`）とショップ（`kitchenerie.shop`）を運営しています。各ドメインにはそれぞれ独自の Braze Web SDK 統合があります。ブラウザのCookieはドメインをまたがないため、同じユーザーがマーケティングサイトからショップに移動すると、Braze は別々のデバイス ID（および別々の匿名プロファイル）を割り当てます。

このパターンでは以下を行います。

1. SDK 初期化後にソースドメインで `getDeviceId` を使用してデバイス ID を読み取ります
2. クエリパラメーター（例: `brazeDeviceId`）として送信リンクに追加します
3. リンク先ドメインでそのパラメーターを読み取り、`deviceId` オプションを通じて `braze.initialize` に渡します

このハンドオフは匿名ユーザーにとって最も重要です。ユーザーがショップでログインした後は、`external_id` を指定した `changeUser` がデバイスをまたぐ永続的な識別子になります。[ユーザー ID の設定]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)を参照してください。

両方のドメインで同じ Braze ワークスペースAPIキーとSDKエンドポイントを使用し、イベントが1つのプロファイルに記録されるようにしてください。

## 考慮事項 {#considerations}

- デバイス ID はブラウザごとに固有です。このパターンでは、異なるブラウザ、デバイス、またはプロファイル間のアクティビティはリンクされません。認証済みのクロスデバイス ID には、`changeUser` を通じて `external_id` を使用してください。
- デバイス ID は、ソースドメインで Web SDKが初期化された後にのみ取得してください。`initialize` の前に `getDeviceId` を呼び出しても値は返されません。
- Web SDKは `initialize` 時に `deviceId` を1回だけ読み取ります。初期化後にアクティブなデバイス ID を変更する `setDeviceId` はありません。リンク先ドメインでは `initialize` を呼び出す前に URL パラメーターを読み取ってください。
- `brazeDeviceId` なしでショップに直接アクセスした場合、ブックマークやサードパーティからの参照は、デフォルトのデバイス ID 割り当てにフォールバックします。これは、継承するソースドメイン ID がない場合に想定される動作です。
- クエリパラメーターはブラウザ履歴やサーバーログに表示されます。
- クエリパラメーターはリファラーヘッダーを通じて漏洩する可能性があります。デバイス ID 単体では PII ではありませんが、プライバシーチームが要求する場合は、使用後にパラメーターを削除してください（ステップ 2 を参照）。
- エンドツーエンドのテストを行ってください。ドメイン 2 のイベントが期待されるデバイス ID を使用していることを、ネットワーク検査で確認してください。
- ホスト名、リンクセレクター、エラーハンドリングをサイトに合わせて調整してください。本番環境に適用する前に開発環境でテストしてください。

## 設定 {#setup}

### ステップ 1: ソースドメインのクロスドメインリンクにデバイス ID を追加する {#step-1-append-the-device-id-to-cross-domain-links-on-the-source-domain}

`kitchenerie.com`（ドメイン 1）で、通常どおり Web SDKを初期化し、`kitchenerie.shop`（ドメイン 2）へのリンクに現在のデバイス ID を追加します。

サイトと競合しないクエリパラメーター名を選択してください（この例では `brazeDeviceId` を使用します）。同じアイデアは、サーバーレンダリングされたリンク、クライアントサイドナビゲーション、または制御可能な iframe の `src` 値にも適用されます。

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});
braze.openSession();

const destinationHost = "kitchenerie.shop";

braze.getDeviceId(function (deviceId) {
  if (!deviceId) {
    return;
  }

  const links = document.querySelectorAll('a[href*="' + destinationHost + '"]');

  links.forEach(function (link) {
    try {
      const url = new URL(link.href);
      url.searchParams.set("brazeDeviceId", deviceId);
      link.href = url.toString();
    } catch (e) {
      // Skip malformed hrefs (for example, javascript:, mailto:, or unparsable relative paths).
    }
  });
});
```

SDKバージョンが `getDeviceId` を同期的に公開している場合（コールバックなし）、初期化後に代わりに呼び出してください。

```javascript
const deviceId = braze.getDeviceId();
```

[Web SDK リポジトリガイド — デバイス ID の取得]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#get-device-id)および[初期化オプション — `deviceId`]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#initialization-options)を参照してください。

### ステップ 2: リンク先ドメインでデバイス ID を読み取り、Web SDKを初期化する {#step-2-read-the-device-id-and-initialize-the-web-sdk-on-the-destination-domain}

`kitchenerie.shop`（ドメイン 2）で、`initialize` の前にクエリ文字列から `brazeDeviceId` を読み取り、存在する場合は初期化オプションに渡します。

```javascript
import * as braze from "@braze/web-sdk";

const urlParams = new URLSearchParams(window.location.search);
const passedDeviceId = urlParams.get("brazeDeviceId");

const initOptions = {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
};

if (passedDeviceId) {
  initOptions.deviceId = passedDeviceId;
}

braze.initialize("YOUR-API-KEY-HERE", initOptions);
braze.openSession();

// Optional: remove the parameter from the visible URL after consumption.
if (passedDeviceId) {
  const cleanUrl = new URL(window.location.href);
  cleanUrl.searchParams.delete("brazeDeviceId");
  window.history.replaceState({}, document.title, cleanUrl.toString());
}
```

ユーザーがログインしたら、`external_id` を指定して `changeUser` を呼び出し、以降のアクティビティが識別済みプロファイルに紐付けられるようにします。

### ステップ 3: ハンドオフを検証する {#step-3-verify-the-handoff}

1. ログインしていないブラウザでドメイン 1 を開きます。
2. クロスドメインリンクをたどってドメイン 2 に移動します。
3. ブラウザのネットワークタブで、ドメイン 2 がドメイン 1 と同じデバイス ID でイベントを送信していることを確認します。
4. クエリパラメーターなしでドメイン 2 に直接アクセスし、新しいデバイス ID が割り当てられることを確認します。

## 関連記事 {#related-articles}

- [Web SDK リポジトリガイド]({{site.baseurl}}/developer_guide/sdk_repository_guides/web)
- [Braze Web SDKのマルチドメイン統合]({{site.baseurl}}/developer_guide/platforms/web/multi_domain_integration)
- [Braze SDKを使用したユーザー ID の設定]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)
- [匿名ユーザー]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)
- [ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [Web SDK ストレージ]({{site.baseurl}}/developer_guide/storage)