---
nav_title: 最適化
article_title: ABテストの最適化
page_order: 1
page_type: reference
description: "BrazeAIを使用して多変量テストやABキャンペーンテストを最適化する方法について説明します。"
---

# ABテストの最適化 {#optimizing-ab-tests}

> **BrazeAI<sup>TM</sup>で最適化**を使用すると、複数のバリアントを含むキャンペーンを自動的に最適化できます。

**ターゲットオーディエンス**ステップで**ABテスト**に移動し、**BrazeAI<sup>TM</sup>で最適化**をオンにします。

単発送信キャンペーンの場合、BrazeAI<sup>TM</sup>は初期テストを送信した後、最もパフォーマンスの高いバリアントを残りのオーディエンスに送信します。繰り返し送信キャンペーンの場合、BrazeAI<sup>TM</sup>は12時間ごとにパフォーマンスを確認し、より高いパフォーマンスのバリアントにより多くのユーザーを割り当てます。

前提条件、設定オプション、レポートの詳細については、[BrazeAIでABテストを最適化する]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)を参照してください。

{% alert note %}
パーソナライズされたバリアントを使用している既存のキャンペーンでは、引き続きその最適化と分析がサポートされます。新しいキャンペーンを作成する際には、パーソナライズされたバリアントは利用できません。
{% endalert %}

Brazeは、単発送信の最適化における2回目の送信前にユーザーの適格性を再度チェックします。初期テストの対象外だったユーザーが残りのオーディエンスに参加する場合があります。一方、適格でなくなったユーザーにはフォローアップの送信は行われません。

キャンペーン結果の詳細については、[ABテストの分析]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics)を参照してください。