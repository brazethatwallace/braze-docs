---
nav_title: ダークモードテーマ
article_title: ダークモードテーマ
page_order: 2
description: "このリファレンス記事では、Brazeのアプリ内メッセージにおけるダークモードのサポートについて、ダークモードテーマの設定方法や互換性に関する考慮事項を含めて説明します。"
channel:
  - in-app messages

---

# ダークモードテーマ {#dark-mode-themes}

> この記事は[従来のエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)に適用されます。ダークモードは、システム全体のカラー設定をユーザーが選択できる機能です（[Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme)および[iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)で導入）。「ダーク」テーマは、バッテリー寿命を節約し、ユーザーの目の負担を軽減すると同時に、アプリ開発者がダークカラーテーマを実装する方法を提供することを目的としています。

Brazeのアプリ内メッセージは、ユーザーの設定に基づいて適切なカラーメッセージを配信し、アプリのデザインとの一貫性を維持するために、代替のダークテーマの追加をサポートしています。

## ダークモードの仕組み {#how-dark-mode-works}

Android 10以降またはiOS 13以降のバージョンを使用しているユーザーは、デバイスの設定でダークモードのオン/オフを切り替えることができます。

ダークモードが有効になると、デバイスのネイティブメニューや画面（プッシュ通知、デバイス設定など）がダークグレーに変わります。アプリも、アプリのコードで代替テーマを指定することでダークモードをサポートすることができます。

## ダークモードテーマの設定 {#setting-a-dark-mode-theme}

ダークモードは、[アプリ内メッセージを作成する]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)際の**デザイン**タブにあり、デバイスでダークモードを使用しているユーザー向けに代替カラーテーマを追加できます。

![アプリ内メッセージ作成時のスタイルタブで、ライトモードスタイルとダークモードスタイルを切り替えるユーザー。]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

このオプションが有効になると、カラーピッカーを使用するか、既存の[カラープロファイル]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/#color-profile)を選択して既存のダークまたはライトテーマを再利用することで、アプリ内メッセージのダークテーマカラーを選択できます。

{% alert note %}
アプリが独自のダークテーマを提供していない場合でも、この機能を使用できます。ただし、ダークモードをサポートしていないデバイスでは、デフォルトでライトテーマが表示されます。Androidでアプリ内メッセージの表示中にデバイスのテーマを変更しても、そのアプリ内メッセージに使用されるテーマは変更されません。
{% endalert %}

### ダークモードを一貫して使用する {#using-dark-mode-consistently}

すべてのアプリ内メッセージでダークモードを使用するには、まずダークモードテーマに合ったカラープロファイルを作成します。

1. **コンテンツ** > **アプリ内メッセージ**に移動します。
2. **テンプレートを作成**を選択し、ドロップダウンから[カラープロファイル]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/#color-profile)を選択します。
3. カラープロファイルを作成して保存します。

アプリ内メッセージのダークモードバージョンを作成する際に、そのカラープロファイルを選択して、アプリ内メッセージの外観を一貫させることができます。

## 互換性 {#compatibility}

- ユーザーはiOSデバイスのバージョン13以降、またはAndroidデバイスのバージョン10以降を使用している必要があります。
- Braze iOS SDK v3.21.0以降、Braze Android SDK v3.8.0以降が必要です。

{% alert note %}
ダークモードアプリはAndroid 10およびiOS 13で導入されました。少なくともこれらのバージョンにスマートフォンをアップグレードしていないユーザーには、ライトテーマのみが表示されます。<br><br>Campaignsは、ユーザーのダークモード設定やOSバージョンに関係なく、選択したオーディエンスの対象となるすべてのユーザーに配信されます。
{% endalert %}

## HTMLアプリ内メッセージの使用 {#using-html-in-app-messages}

HTMLアプリ内メッセージのダークテーマとライトテーマを作成するには、[`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSSメディア機能を使用して、ユーザーの設定を検出できます。

例:

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```

