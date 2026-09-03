---
nav_title: ユーザー設定センター
article_title: ユーザー設定センター
page_order: 8
layout: dev_guide
guide_top_header: "ユーザー設定センター"
guide_top_text: "メールのユーザー設定センターを使用すると、ユーザーがアプリやWebサイト内のブランドページから、メールキャンペーンやニュースレターの通知設定を管理できます。以下の記事を参照して、<a href='/docs/api/endpoints/preference_center'>Brazeユーザー設定センターAPI</a> またはドラッグ＆ドロップエディターを使用したユーザー設定センターの作成・管理方法（購読グループ、オプトイン状態、ホストページのカスタマイズを含む）をご確認ください。"
description: "このランディングページには、Brazeメールのユーザー設定センターとユーザー設定センターAPIの使用方法に関する記事が含まれています。"
channel:
  - email

guide_featured_title: "セクションの記事"
guide_featured_list:
- name: APIメールユーザー設定センター
  link: /docs/user_guide/audience/subscription_preferences/preference_center/api_preference_center
  image: /assets/img/braze_icons/list.svg
- name: ドラッグ＆ドロップメールユーザー設定センター
  link: /docs/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center
  image: /assets/img/braze_icons/mail-01.svg

---

{% multi_lang_include alerts/tip_alerts.md alert="Landing pages manage subscriptions" %}

## よくある質問 {#frequently-asked-questions}

### メールユーザー設定センターとは何ですか？ {#what-is-an-email-preference-center}

メールユーザー設定センターは、ユーザーがメールの購読ステータスを更新し、メッセージカテゴリを選択できるホスト型ページです。Brazeでは、APIで構築するユーザー設定センターとドラッグ＆ドロップユーザー設定センターをサポートしています。

### ユーザー設定センターAPIとドラッグ＆ドロップエディターのどちらを使用すべきですか？ {#should-i-use-the-preference-center-api-or-the-drag-and-drop-editor}

コーディングを最小限に抑えてすばやく設定したい場合は、[ドラッグ＆ドロップメールユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center)を使用してください。レイアウト、ホスティング、カスタムロジックを完全にコントロールしたい場合は、[APIメールユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/api_preference_center)を使用してください。