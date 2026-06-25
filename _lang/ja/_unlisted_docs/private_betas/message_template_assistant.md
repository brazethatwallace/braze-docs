---
nav_title: HTMLメールテンプレート
article_title: HTMLメールテンプレートの生成
permalink: "/template_assistant/"
description: "このリファレンス記事では、Operatorを使用してHTMLメールテンプレートを生成する方法について、仕組みやプロンプトの例を含めて説明します。"
page_type: reference
---

# HTMLメールテンプレートの生成 {#generate-html-email-templates}

> Operatorを使用して、HTMLメールテンプレートを生成・改善できます。必要なテンプレートを自然言語で説明すると、Operatorがブランドガイドラインとグローバルスタイル設定を使用してテンプレートを構築または変更します。

{% alert important %}
OperatorによるHTMLメールテンプレートの生成は早期アクセス段階です。この早期アクセスへの参加にご興味がある場合は、Brazeアカウントマネージャーにお問い合わせください。

この機能はメールチャネルのHTMLエディターでのみサポートされており、その他のエディター（ドラッグ＆ドロップやAMPなど）ではサポートされていません。
{% endalert %}

{% multi_lang_include brazeai/generative_ai/unification_note.md %}

## アクセス方法 {#how-to-access}

{% multi_lang_include brazeai/generative_ai/access_html_template.md %}

## 仕組み {#how-it-works}

Operatorは、[ブランドガイドライン]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/)と[グローバルスタイル設定]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/)を使用して、メッセージのコンテンツとスタイルをブランドに合わせて調整します。

たとえば、グローバルスタイル設定が設定されている場合、Operatorはブランドのカラーやスタイルを取り入れます。Brazeでブランドガイドラインが定義されている場合、Operatorはそれらも参照して、ブランドのトーンやパーソナリティに合ったコピーを作成します。

Operatorは、モバイルレスポンシブ対応のテンプレートへの改善も行います。

## プロンプトの例 {#example-prompts}

{% include copy_block.html content="Build a responsive HTML email template for a product launch with a hero image and two feature blocks." %}

{% include copy_block.html content="Create a clean, single-column newsletter template that matches our brand guidelines." %}

{% include copy_block.html content="Add a feedback survey at the bottom of the email" %}

{% include copy_block.html content="Change font to [font name] and font size of the paragraph to size [number]" %}

{% include copy_block.html content="Make all the images have rounded corners" %}

{% include copy_block.html content="Add another section with an image and a call-to-action" %}