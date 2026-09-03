[Braze SDKを統合]({{site.baseurl}}/developer_guide/sdk_integration)した後、アプリを初めて起動したユーザーは、`changeUser` メソッドを呼び出して `external_id` を割り当てるまで「匿名」とみなされます。一度割り当てると、再び匿名にすることはできません。ただし、アプリをアンインストールして再インストールした場合は、`changeUser` が呼び出されるまで再び匿名になります。

以前に識別されたユーザーが新しいデバイスでセッションを開始した場合、そのデバイスでそのユーザーの `external_id` を使用して `changeUser` を呼び出すと、Brazeは匿名プロファイルの特定のフィールドのうち、識別済みプロファイルにまだ存在しないものをマージします。すべてのデータが転送されるわけではなく、識別済みプロファイルにまだ設定されていないフィールドのみがマージされます。転送されるフィールドの完全なリストについては、[マージの動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)を参照してください。

{% if include.section == "user_guide" %}
{% alert tip %}
詳しい手順については、[ユーザーIDの設定]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)を参照してください。
{% endalert %}
{% endif %}