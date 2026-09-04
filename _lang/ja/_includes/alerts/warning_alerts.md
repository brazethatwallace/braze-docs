{% if include.alert == 'User profile external_id' %}

{% alert warning %}
ユーザープロファイルを一意に識別できるようになる前に、`external_id` を割り当てないでください。ユーザーを識別した後、匿名ユーザーに戻すことはできません。
<br><br>
`external_id`は[`/users/external_ids/rename` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename)を使用して更新できます。ただし、ユーザーのセッション中に異なる `external_id` を設定しようとすると、新しい `external_id` が関連付けられた新しいユーザープロファイルが作成されます。2つのプロファイル間でデータが引き継がれることはありません。
{% endalert %}

{% endif %}

{% if include.alert == 'セグメント Currents multiple connectors' %}

{% alert warning %}
同じCurrentsコネクターを複数作成する場合（たとえば、2つのメッセージエンゲージメントイベントコネクター）、それらは別々のワークスペースに配置する必要があります。Brazeセグメント Currentsの統合では、1つのワークスペース内で異なるアプリごとにイベントを分離することができないため、これを行わないと不必要なデータの重複排除やデータの損失が発生します。
{% endalert %}

{% endif %}

{% if include.alert == 'キャンバス race condition audience trigger' %}

{% alert warning %}
オーディエンスフィルターと同じトリガー（属性の変更やカスタムイベントの実行など）でアクションベースのキャンペーンやキャンバスを設定しないでください。[競合]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions)が発生し、ユーザーがトリガーイベントを実行した時点でオーディエンスに含まれていないために、キャンペーンを受信できなかったりキャンバスに入れなかったりする可能性があります。
{% endalert %}

{% endif %}