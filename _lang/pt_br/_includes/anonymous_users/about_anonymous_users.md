Após [integrar o SDK da Braze]({{site.baseurl}}/developer_guide/sdk_integration), os usuários que iniciarem seu app pela primeira vez serão considerados "anônimos" até que você chame o método `changeUser` e atribua a eles um `external_id`. Uma vez atribuído, não é possível torná-los anônimos novamente. No entanto, se o usuário desinstalar e reinstalar o app, ele se tornará anônimo novamente até que `changeUser` seja chamado.

Se um usuário previamente identificado iniciar uma sessão em um novo dispositivo, a Braze fará o merge de campos específicos do perfil anônimo que ainda não existam no perfil identificado depois que você chamar `changeUser` nesse dispositivo usando o `external_id` dele. Nem todos os dados são transferidos — apenas os campos que ainda não estão preenchidos no perfil identificado são mesclados. Para ver a lista completa dos campos transferidos, consulte [comportamento de merge]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

{% if include.section == "user_guide" %}
{% alert tip %}
Para um passo a passo completo, consulte [Definição de IDs de usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_ids).
{% endalert %}
{% endif %}