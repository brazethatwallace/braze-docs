---
nav_title: iOS向けアプリ内評価プロンプト
article_title: iOS向けアプリ内評価プロンプト
page_order: 6
description: "この記事では、Brazeを使用してユーザーにアプリのレビューを依頼するためのアプローチとその影響について説明します。"
channel:
  - in-app messages

---

# iOS向けアプリ内評価プロンプト {#in-app-rating-prompt-for-ios}

> この記事では、Brazeを使用してユーザーにアプリのレビューを依頼するためのアプローチとその影響について説明します。効果的なアプリ評価キャンペーンを作成するためのヒントについては、[顧客アプリ評価のすべきこととすべきでないこと](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings)をご覧ください。

AppleはiOS 10.3で導入されたネイティブプロンプトを提供しており、ユーザーがアプリ内からアプリを評価できるようにしています。iOSでアプリ内メッセージを使用してユーザーにアプリの評価を依頼する場合は、ネイティブプロンプトを使用する必要があります。Appleはカスタムレビュープロンプトを禁止しているためです（[App Storeレビューガイドライン](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct)のセクション5.6.1を参照）。

Appleのガイドラインに従い、アプリレビュープロンプトはユーザーに対して年間最大3回まで表示できるため、アプリレビューキャンペーンでは[レート制限]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/)を活用する必要があります。ユーザーはアプリ設定でアプリレビュープロンプトの表示を完全にオプトアウトすることもできます。App Storeの評価について詳しくは、Appleの記事[評価、レビュー、および返信](https://developer.apple.com/app-store/ratings-and-reviews/)を参照してください。

## Brazeを使用してユーザーにアプリレビューを依頼する {#using-braze-to-ask-users-for-app-reviews}

Appleはネイティブプロンプトの使用を要求していますが、Brazeのキャンペーンを活用して適切なタイミングでユーザーにアプリの評価とレビューを依頼することができます。主に2つのアプローチがあります。

### アプローチ1：App Storeへのディープリンク {#approach-1-deep-linking-to-the-app-store}

このアプローチでは、ユーザーにApp Storeにアクセスしてレビューを追加するよう促します。これを行うには、App Storeへの[ディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/)を設定したアプリ内メッセージキャンペーンを作成します。

![2つのモバイル画面を並べて表示。1つ目はApp Storeでアプリを評価するようユーザーに依頼するアプリ内メッセージ。2つ目はそのアプリのiOS App Storeページ。]({% image_buster /assets/img_archive/app_store_app_review.png %})

### アプローチ2：ソフトプライミング {#approach-2-soft-priming}

ユーザーにアプリを離れてほしくない場合は、まず別のアプリ内メッセージでユーザーにプライミングを行うことができます。プライミングとは、ネイティブのApp Storeレビュープロンプトを送信する前にユーザーに許可を求める方法です。これを行うには、アプリ内メッセージキャンペーンを作成し、クリック時に`requestReview`メソッドを呼び出すカスタムディープリンクを追加します。

詳細な手順については、[カスタムApp Storeレビュープロンプト]({{site.baseurl}}/developer_guide/in_app_messages/customization/#swift_customizing-the-app-store-review-prompt)を参照してください。

![2つのアプリ内メッセージを並べて表示。1つ目はアプリを評価する時間があるかどうかを尋ねることでユーザーにプライミングを行うメッセージ。2つ目はネイティブのiOS App Storeレビューメッセージで、ユーザーがアプリを評価するために選択できる5つ星のスケールを表示。]({% image_buster /assets/img_archive/prime_app_review.png %})

ユーザーはネイティブのApp Storeレビュープロンプトを通じて評価を送信し、アプリを離れることなくレビューを書いて送信できます。

### 考慮事項 {#considerations}

ソフトプライミングの代替として、Brazeのソフトプライマーメッセージを事前に表示せずに、iOSアプリ評価プロンプトを直接表示することもできます。この利点は、ユーザーがアプリレビュープロンプトをオプトアウトしている場合、アプリを評価しようとしてもプロンプトが表示されないという最適でないユーザー体験を避けられることです。

{% alert important %}
ネイティブのiOSアプリ評価プロンプトを模倣するカスタムHTMLアプリ内メッセージを作成しないでください。これはAppleのガイドラインに違反します。
{% endalert %}