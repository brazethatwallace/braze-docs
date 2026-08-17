{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
フリークエンシーキャップはContent Cardsには適用されません。
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
「12-1-2021」や「12/1/2021」などの日付文字列は、日時オブジェクトに変換され、[時間属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#time)として扱われます。
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
ユーザープロファイルのすべてのデータ（カスタムイベント、カスタム属性、カスタムデータ）は、それらのプロファイルがアクティブである限り保存されます。
{% endalert %}

{% endif %}

{% if include.alert == 'セグメント profiles first app use' %}

{% alert note %}
Brazeは、ユーザーが初めてアプリを使用するまでプロファイルを生成しないため、まだアプリを開いていないユーザーをターゲットにすることはできません。
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify attributes REST API' %}

{% alert note %}
すべての属性のソースはBraze REST APIです。
{% endalert %}

{% endif %}

{% if include.alert == 'subscription group limit' %}

{% alert note %}
1つのワークスペースにつき、最大450の購読グループを追加できます。
{% endalert %}

{% endif %}

{% if include.alert == 'GIF platform support' %}

{% alert note %}
GIFはAndroidプッシュ通知ではサポートされていません。これはAndroidプラットフォームの制限であり、Brazeの制限ではありません。
<br><br>
- Androidのアプリ内メッセージおよびContent Cardsでは、[Glide](https://bumptech.github.io/glide/)や[Fresco](https://frescolib.org/)などのサードパーティ画像ライブラリを統合することでGIFをサポートできます。
<br>
- iOSでは、プッシュ通知がGIFをサポートしています。アプリ内メッセージおよびContent CardsにはカスタムのGIF画像プロバイダーが必要です。
{% endalert %}

{% endif %}