---
nav_title: HTMLメールテンプレート
article_title: HTMLメールテンプレートの生成
permalink: "/template_assistant/"
description: "このリファレンス記事では、オペレーターを使用してHTMLメールテンプレートを生成する方法について、仕組みやプロンプトの例を含めて説明します。"
page_type: reference
---

# HTMLメールテンプレートの生成 {#generate-html-email-templates}

> オペレーターを使用して、HTMLメールテンプレートを生成・改善できます。必要なテンプレートを自然言語で説明すると、オペレーターがブランド・ガイドラインとグローバルスタイル設定を使用してテンプレートを構築または変更します。

{% alert important %}
オペレーターによるHTMLメールテンプレートの生成は早期アクセス段階です。この早期アクセスへの参加にご興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。

この機能はメールチャネルのHTMLエディターでのみサポートされており、その他のエディター（ドラッグ＆ドロップやAMPなど）ではサポートされていません。
{% endalert %}

{% multi_lang_include brazeai/generative_ai/unification_note.md %}

## アクセス方法 {#how-to-access}

HTMLメールテンプレートエディターで、**生成**サイドバーグループに**テンプレート**オプションがあります。これを選択すると、ブランドに沿ったHTMLメールテンプレートを生成または改善できます。オペレーターが[ブランド・ガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)を適用し、ブランドのボイスやスタイルに合った結果を生成します。


## 仕組み {#how-it-works}

オペレーターは、[ブランド・ガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)と[グローバルスタイル設定]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings)を使用して、メッセージのコンテンツとスタイルをブランドに合わせて調整します。

たとえば、グローバルスタイル設定が設定されている場合、オペレーターはブランドのカラーやスタイルを取り入れます。Brazeでブランド・ガイドラインが定義されている場合、オペレーターはそれらも参照して、ブランドのトーンやパーソナリティに合ったコピーを作成します。

オペレーターは、モバイルレスポンシブ対応のテンプレートへの改善も行います。

## プロンプトの例 {#example-prompts}

{% include copy_block.html content="Build a responsive HTML email template for a product launch with a hero image and two feature blocks." %}

{% include copy_block.html content="Create a clean, single-column newsletter template that matches our brand guidelines." %}

{% include copy_block.html content="Add a feedback survey at the bottom of the email" %}

{% include copy_block.html content="Change font to [font name] and font size of the paragraph to size [number]" %}

{% include copy_block.html content="Make all the images have rounded corners" %}

{% include copy_block.html content="Add another section with an image and a call-to-action" %}