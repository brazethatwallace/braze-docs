---
nav_title: Práticas recomendadas de coleta
article_title: Práticas recomendadas de coleta
page_order: 4
page_type: reference
description: "O artigo a seguir ajuda a esclarecer diferentes métodos e práticas recomendadas para a coleta de dados de usuários novos e existentes."

---

# Práticas recomendadas de coleta {#collection-best-practices}

> Saber quando e como coletar dados de usuários conhecidos e desconhecidos pode ser um desafio quando se imagina o ciclo de vida do perfil do usuário de seus clientes. Este artigo ajuda a esclarecer diferentes métodos e práticas recomendadas para a coleta de dados de usuários novos e existentes, orientando você em um caso de uso.

O exemplo a seguir é um caso de uso de coleta de e-mail, mas a lógica se aplica a muitos cenários diferentes de coleta de dados. Neste exemplo, presumimos que você já tenha integrado um formulário de inscrição ou uma forma de coletar informações do usuário.

Depois que um usuário fornecer informações para registro, recomendamos que você verifique se os dados já existem no seu banco de dados e, quando necessário, crie um perfil de alias de usuário ou atualize o perfil de usuário existente.

Se um usuário desconhecido visualizar seu site e, posteriormente, criar uma conta ou se identificar por meio de inscrição por e-mail, a mesclagem de perfis deverá ser tratada com cuidado. Com base no método de mesclagem, as informações do usuário somente de alias ou os dados anônimos podem ser substituídos.

## Captura de dados de usuários por meio de um formulário web {#capturing-user-data-through-a-web-form}

### Etapa 1: Verificar se o usuário já existe {#step-1-check-if-the-user-exists}

Quando um usuário insere conteúdo por meio de um formulário web, verifique se já existe um usuário com esse e-mail no seu banco de dados. Você pode fazer isso de uma das seguintes maneiras:

- **Verificar no banco de dados interno (recomendado):** Se você tem um registro ou banco de dados externo contendo as informações do usuário fornecidas fora da Braze, consulte-o no momento do envio do e-mail ou da criação da conta para confirmar que as informações ainda não foram capturadas.
- **[Endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track):** Use `email` como identificador; um novo perfil de usuário será criado se o endereço de e-mail ainda não existir.
- **[Endpoint `/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status):** Se você coleta e-mails por meio de um formulário personalizado e depois define a associação ao grupo de inscrições pela REST API, chame esse endpoint primeiro. Se não houver um perfil correspondente, crie ou inscreva o usuário com o [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Caso contrário, atualize o perfil existente em vez de criar um duplicado.

### Etapa 2: Registrar ou atualizar o usuário {#step-2-log-or-update-user}

- **Se o usuário existir:**
  - Não crie um novo perfil.
  - Registre um atributo personalizado (por exemplo, `newsletter_subscribed: true`) no perfil do usuário para indicar que ele enviou seu e-mail por meio de uma inscrição em newsletter. Se existirem múltiplos perfis de usuário na Braze com o mesmo endereço de e-mail, todos os perfis serão exportados.<br><br>
- **Se o usuário não existir:**
  - Crie um perfil somente com alias por meio do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Esse endpoint aceita um [objeto `user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object) e cria um perfil somente com alias quando `update_existing_only` está definido como `false`. Defina o e-mail do usuário como o alias do usuário para referenciá-lo no futuro (já que o usuário não terá um `external_id`).

![Diagrama mostrando o processo para atualizar um perfil de usuário somente com alias. Um usuário envia seu endereço de e-mail e um atributo personalizado, seu CEP, em uma landing page de marketing. Uma seta apontando da coleta na landing page para um perfil de usuário somente com alias mostra uma solicitação da API da Braze ao endpoint Track user, com o corpo da solicitação contendo o nome do alias, o rótulo do alias, o e-mail e o CEP do usuário. O perfil tem o rótulo "Usuário somente com alias criado na Braze" com os atributos do corpo da solicitação para mostrar os dados refletidos no perfil recém-criado.]({% image_buster /assets/img/user_profile_process3.png %}){: style="max-width:90%;"}

## Capturando e-mails de usuários por meio de um formulário de captura de e-mail {#capturing-user-emails-through-an-email-capture-form}

Use um formulário de captura de e-mail para solicitar que os usuários enviem seus endereços de e-mail, que serão adicionados aos seus perfis de usuário. Para saber mais sobre como configurar esse formulário, confira [Formulário de captura de e-mail]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/email_capture_form).

Se você usar um formulário personalizado e definir a associação ao grupo de inscrições por meio da REST API, verifique se já existe um perfil antes de criar um usuário. Consulte [Etapa 1: Verifique se o usuário existe](#step-1-check-if-user-exists).

## Identificando usuários somente com alias {#identifying-alias-only-users}

Ao identificar usuários na criação de conta, usuários somente com alias podem ser identificados e receber um ID externo por meio do [endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), mesclando o usuário somente com alias ao perfil conhecido.

Para verificar se um usuário é somente com alias, [verifique se o usuário existe](#step-1-check-if-user-exists) no seu banco de dados.
- Se existir um registro externo, você pode chamar o endpoint `/users/identify/`.
- Se o [endpoint `/users/export/id`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) retornar um `external_id`, você pode chamar o endpoint `/users/identify/`.
- Se o endpoint não retornar nada, a chamada ao `/users/identify/` não deve ser feita.

## Capturando dados de usuários quando informações de usuários somente com alias já estão presentes {#capturing-user-data-when-alias-only-user-information-is-already-present}

Quando um usuário cria uma conta ou se identifica por meio de inscrição por e-mail, você pode mesclar os perfis. Para ver uma lista de campos que podem ser mesclados, consulte [Comportamento de atualização de mesclagem]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

### Mesclando perfis de usuários duplicados {#merging-duplicate-user-profiles}

À medida que seus dados de usuários crescem, você pode mesclar perfis de usuários duplicados no dashboard da Braze. Esses perfis duplicados devem ser encontrados usando a mesma consulta de pesquisa. Para saber mais sobre como duplicar perfis de usuários, confira [Mesclar usuários duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

Você também pode usar o [endpoint Mesclar usuários]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) para mesclar um perfil de usuário com outro.

{% alert note %}
Depois que os perfis de usuários são mesclados, essa ação não pode ser desfeita.
{% endalert %}

## Recursos adicionais {#additional-resources}
- Confira nosso artigo sobre o [ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) da Braze para mais contexto.<br>
- Consulte nossa documentação sobre como definir IDs de usuário e chamar o método `changeUser()` para [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#suggested-user-id-naming-convention) e [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).