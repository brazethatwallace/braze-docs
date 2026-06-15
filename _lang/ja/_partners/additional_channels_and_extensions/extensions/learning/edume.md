---
nav_title: eduMe
article_title: eduMe
description: "このリファレンス記事では、Brazeと eduMe のパートナーシップについて説明します。eduMe はモバイルベースのトレーニングツールであり、Braze コネクテッドコンテンツを利用して、ユーザーが Braze キャンペーンで eduMe のコースやレッスンにアクセスできるようにします。"
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# eduMe

> [eduMe](https://edume.com)はモバイルベースのトレーニングツールであり、従業員はどこにいても必要なときに、成功するために必要な知識を習得できます。

_この統合は eduMe によって管理されています。_

## 統合について {#about-the-integration}

Brazeと eduMe の統合では、Braze [コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)を利用して、ユーザーが Braze キャンペーンで eduMe のコースやレッスンにアクセスできるようにします。個人とグループの進捗状況は、eduMe のレポート機能で追跡できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| eduMe アカウント | このパートナーシップを活用するには、eduMe アカウントが必要です。 |
| eduMe APIキー | eduMe のカスタマーサクセス担当者にAPIキーをリクエストする必要があります。このキーは、Braze コネクテッドコンテンツの呼び出しで使用されます。 |
| eduMe リンク署名シークレット | eduMe のカスタマーサクセス担当者に、組織のリンク署名シークレットの設定を依頼する必要があります。このシークレットは、コネクテッドコンテンツでシームレスなリンクを有効にするために使用されます。このシークレットに対して特に操作を行う必要はありません。 |
| eduMe グループとコンテンツ ID | これらの識別子は、コネクテッドコンテンツの呼び出しを設定する際に必要です。これらの識別子の取得については、eduMe のカスタマーサービス担当者にお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### コネクテッドコンテンツの呼び出しを作成する {#create-your-connected-content-call}

ユーザーにコース、レッスン、または eNPS 調査へのアクセスを提供し、eduMe で内部ユーザー IDに対する進捗状況を追跡するには、次の例に示すAPI呼び出しに従ってください。

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. `YOUR-EDUME-API-KEY` を eduMe APIキーに置き換えます。<br><br>
2. `EDUME-CONTENT-LINK-AND-CONTENT-ID` を、対応するコンテンツリンク文字列とモジュール、レッスン、または調査の識別子に置き換えます。これらの識別子は、eduMe アカウントで確認できます。
  - コース: `getCourseLink?moduleId=12087`
  - レッスン: `getLessonLink?lessonId=25805`
  - eNPS 調査: `getSurveyLink?surveyId=654`<br><br>
3. このリンクを通じて eduMe にアクセスしたユーザーは、選択した eduMe チームまたはグループに追加されます。`groupId` を関連するチーム ID または eduMe グループ ID に置き換えます。通常はチーム ID を使用しますが、登録が必要なコースの場合はグループ ID を使用してください。<br><br>
4. `externalUserId` フィールドのマッピング先として適切なフィールドを含めます。コネクテッドコンテンツの呼び出し例では `driver_id` を使用していますが、実際のフィールドは異なる可能性があります。この ID は eduMe のレポートで利用でき、自社システムとの関連付けが可能です。<br><br>
5. 最後に、必要に応じてメッセージをカスタマイズしてテストします。少なくとも1つのテストメッセージを送信し、eduMe コンテンツにアクセスし、レッスンまたはコースを完了し、eduMe の分析が正しく記録されていることを確認することをお勧めします。