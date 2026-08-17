---
nav_title: Ciclo de vida do perfil do usuário
article_title: Ciclo de vida do perfil do usuário
page_order: 2
page_type: reference
description: "Este artigo de referência descreve o ciclo de vida do perfil de usuário da Braze e as várias maneiras pelas quais um perfil de usuário pode ser identificado e referenciado."

---

# Ciclo de vida do perfil do usuário {#user-profile-lifecycle}

> Este artigo descreve o ciclo de vida do perfil de usuário da Braze e as várias maneiras de identificar e fazer referência a um perfil de usuário. Se quiser entender melhor o ciclo de vida do cliente, confira nosso curso do Braze Learning sobre [Mapeamento do ciclo de vida do usuário](https://learning.braze.com/mapping-customer-lifecycles).

Todos os dados persistentes associados a um usuário são armazenados em seu perfil de usuário. Depois que um perfil de usuário é criado, seja por meio da API ou depois que um usuário é reconhecido pelo SDK, é possível atribuir vários parâmetros a esse perfil para identificar e fazer referência a esse usuário.

Esses parâmetros incluem:

* `braze_id` (atribuído pela Braze)
* `external_id`
* `email`
* `phone`
* Qualquer número de aliases de usuário personalizados que você definir

## Perfis de usuários anônimos {#anonymous-user-profiles}

Qualquer usuário sem um `external_id` designado é chamado de [usuário anônimo]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users). Por exemplo, podem ser usuários que visitaram seu website mas não se inscreveram, ou usuários que baixaram seu app móvel mas não criaram um perfil.

Inicialmente, quando um usuário é reconhecido pelo SDK, um perfil de usuário anônimo é criado com um `braze_id` associado: um identificador único que é atribuído automaticamente pela Braze, não pode ser editado e é específico do dispositivo. Esse identificador pode ser usado para atualizar o perfil de usuário por meio da [API]({{site.baseurl}}/api/endpoints/user_data).

## Perfis de usuário identificados {#identified-user-profiles}

Depois que um usuário é reconhecível no seu app (ao fornecer alguma forma de ID de usuário ou endereço de e-mail), recomendamos atribuir um `external_id` ao perfil desse usuário usando o método `changeUser` ([web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html)). Um `external_id` permite identificar o mesmo perfil de usuário em vários dispositivos.

Os benefícios adicionais de usar um `external_id` incluem:

- Oferecer uma experiência de usuário consistente em vários dispositivos e plataformas (por exemplo, não enviar notificações de usuário inativo para o tablet Android de um usuário quando ele é um usuário fiel do app no iPhone).
- Melhorar a precisão da sua análise de dados, confirmando que os usuários não estão criando um novo perfil de usuário toda vez que desinstalam e reinstalam, ou instalam o app em um dispositivo diferente.
- Permitir a importação de dados de usuários de fontes externas ao app usando os [endpoints de dados de usuários]({{site.baseurl}}/api/endpoints/user_data) e direcionar usuários com mensagens transacionais usando nossos [endpoints de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging).
- Pesquisar usuários individuais usando nossos [filtros]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) de "Teste" dentro do segmentador, e na página [**Pesquisar usuários**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

### Considerações sobre IDs externos {#considerations-for-external-ids}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

#### Risco de usar um e-mail ou e-mail com hash como ID externo {#risk-of-using-an-email-or-hashed-email-as-an-external-id}

Usar um endereço de e-mail ou um endereço de e-mail com hash como seu ID externo da Braze pode simplificar o gerenciamento de identidade entre suas fontes de dados. No entanto, é importante considerar os riscos potenciais para a privacidade do usuário e a segurança dos dados.

- **Informação previsível:** Endereços de e-mail são facilmente previsíveis, o que os torna vulneráveis a ataques.
- **Risco de exploração:** Se um usuário mal-intencionado alterar seu navegador web para enviar o endereço de e-mail de outra pessoa como seu ID externo, ele poderá acessar mensagens sensíveis ou informações da conta.

### O que acontece quando você identifica usuários anônimos {#what-happens-when-you-identify-anonymous-users}

Dois cenários podem ocorrer quando você identifica usuários anônimos:

1) **Um usuário anônimo se torna um novo usuário identificado:** <br>Se o `external_id` ainda não existir na Braze, o usuário anônimo se torna um novo usuário identificado e mantém todos os mesmos atributos e histórico do usuário anônimo.

2) **Um usuário anônimo é identificado como um usuário já existente:** <br>Se o `external_id` já existir na Braze, então esse usuário foi previamente identificado como um usuário no sistema de alguma outra forma, como por meio de outro dispositivo (como um tablet) ou dados de usuário importados.

Em outras palavras, você já tem um perfil de usuário para esse usuário. Nesse caso, a Braze fará o seguinte:
1. Tornar o usuário anônimo órfão
2. Mesclar [campos específicos do perfil de usuário]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) que ainda não existem no perfil do usuário identificado a partir do perfil anônimo
3. Remover o perfil anônimo da sua base de usuários para que a contagem de usuários não fique inflada

Se tanto o usuário anônimo quanto o usuário conhecido tiverem um nome, o nome do usuário conhecido é mantido. Se o usuário conhecido tiver um valor nulo e o usuário anônimo tiver um valor, o valor do usuário anônimo é mesclado no perfil do usuário conhecido se o valor estiver entre esses [campos específicos do perfil de usuário]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior).

{% alert important %}
Nem todos os dados são mesclados a partir do perfil anônimo. Tokens por push e histórico de mensagens são transferidos, e atributos personalizados, eventos personalizados e histórico de compras do perfil anônimo são mesclados no usuário identificado somente quando esses campos ainda não existem no perfil do usuário identificado. Quando há dados conflitantes, os valores do usuário identificado são mantidos. Consulte [comportamento de mesclagem]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior) para a lista completa de campos que são e não são transferidos.
{% endalert %}

Para saber mais sobre como definir um `external_id` em um perfil de usuário, consulte nossa documentação ([iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android), [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)).

{% alert note %}
Usuários órfãos não são elegíveis para receber mensagens.
{% endalert %}

### Mesclando usuários duplicados {#merging-duplicate-users}

Quando você identifica perfis de usuário duplicados no seu espaço de trabalho, é possível mesclá-los usando a REST API. Para saber mais sobre a mesclagem de usuários e os métodos disponíveis, consulte [Mesclar usuários duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users).

## Aliases de usuário {#user-aliases}

Para se referir a usuários por identificadores diferentes do `external_id` da Braze, defina aliases de usuário em um perfil de usuário. Qualquer alias definido em um perfil de usuário funcionará em adição ao `braze_id` ou `external_id` do usuário, em vez de substituí-lo. Não há limite para o número de aliases que você pode definir em um perfil de usuário.

Cada alias funciona como um par chave-valor composto por duas partes: um `alias_label`, que define a chave do alias, e um `alias_name`, que define o valor. Um `alias_name` para qualquer label individual deve ser único em toda a sua base de usuários (assim como o `external_id`). Se você tentar atualizar um segundo perfil de usuário com uma combinação de label e nome já existente, o perfil de usuário não será atualizado.

### Atualizando aliases de usuário {#updating-user-aliases}

Um alias pode ser atualizado com um novo nome para um determinado label após ser definido, usando nossos [endpoints de dados de usuário]({{site.baseurl}}/developer_guide/rest_api/user_data#new-user-alias-endpoint) ou passando um novo nome pelo SDK. O alias de usuário ficará então visível ao exportar os dados desse usuário.

![Dois perfis de usuário diferentes para usuários distintos com o mesmo label de alias de usuário, mas com nomes de alias diferentes]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### Marcando usuários anônimos com tags {#tagging-anonymous-users}

Os aliases de usuário também permitem que você marque usuários anônimos com um identificador. Por exemplo, se um usuário fornecer ao seu site de eCommerce o endereço de e-mail, mas ainda não tiver se inscrito, o endereço de e-mail pode ser usado como alias para esse usuário anônimo. Esses usuários podem então ser exportados usando seus aliases ou referenciados pela API.

### Comportamento de aliases em perfis de usuários anônimos {#behavior-of-aliases-on-anonymous-user-profiles}

Se um perfil de usuário anônimo com um alias for posteriormente reconhecido com um `external_id`, ele será tratado como um perfil de usuário identificado normal, mas manterá seu alias existente e ainda poderá ser referenciado por esse alias.

### Pesquisando um alias de usuário {#searching-for-a-user-alias}

Se você souber o nome e o label do alias de um usuário, poderá encontrar o usuário em **Pesquisar Usuários** com o formato `alias_label:alias_name`. Por exemplo, se você tiver um perfil somente com alias com o nome `alias_name: bobby_alias` e o label `alias_label: m4pzOndtA-CnO0u`, poderá encontrar esse usuário digitando `m4pzOndtA-CnO0u:bobby_alias`.

Se você não souber essas informações, poderá chamar o [endpoint `Export user profile by identifier`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) e encontrar o alias de usuário na resposta da API.

### Definindo aliases em perfis de usuários conhecidos {#setting-aliases-on-known-user-profiles}

Um alias de usuário também pode ser definido em um perfil de usuário conhecido para referenciar um usuário conhecido por outro ID externamente conhecido. Por exemplo, um usuário pode ter um ID de ferramenta de business intelligence (como um ID do Amplitude) que você deseja referenciar na Braze.

Para saber mais sobre como definir um alias de usuário, consulte nossa documentação para cada plataforma ([iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#aliasing-users), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids#aliasing-users), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#aliasing-users)).

![Um fluxograma do ciclo de vida de um perfil de usuário na Braze. Quando changeUser() é chamado para um usuário anônimo, esse usuário se torna um Usuário Identificado e os dados são migrados para o perfil de usuário identificado. O Usuário Identificado possui um Braze ID e um ID externo. Nesse ponto, se um segundo usuário anônimo tiver changeUser() chamado, os campos de dados de usuário que ainda não existem no Usuário Identificado serão mesclados. Se o Usuário Identificado tiver um alias adicionado ao perfil de usuário existente, nenhum dado será afetado, mas ele se tornará um Usuário Identificado com alias. Se um terceiro usuário anônimo com o mesmo label de alias do Usuário Identificado, mas com um nome de alias diferente, tiver changeUser() chamado, quaisquer campos que não existam no Usuário Identificado serão mesclados e o label de alias no perfil do Usuário Identificado será mantido.]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
Está com dificuldade para visualizar como isso pode funcionar no ciclo de vida do perfil de usuário dos seus clientes? Acesse [Práticas recomendadas]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices) para ver as práticas recomendadas de coleta de dados de usuários.
{% endalert %}

## Caso de uso avançado {#advanced-use-case}

Você pode definir um novo alias de usuário para perfis de usuário identificados existentes por meio do nosso SDK e da nossa API usando os [endpoints de dados de usuário]({{site.baseurl}}/developer_guide/rest_api/user_data#new-user-alias-endpoint). No entanto, aliases de usuário não podem ser definidos pela API para um perfil de usuário desconhecido existente.

Os aliases de usuário também são mesclados no processo. No entanto, se tanto o usuário a ser órfão quanto o usuário de destino tiverem um alias com o mesmo rótulo, apenas o alias do usuário de destino será mantido.

Desinstalar e reinstalar um app gerará um novo `braze_id` anônimo para esse usuário.

### Solução de problemas com IDs de usuário {#troubleshooting-with-user-ids}

Todos os IDs de usuário podem ser usados para encontrar e identificar usuários no seu dashboard para testes. Para encontrar seu usuário no dashboard da Braze, consulte [Adicionando usuários teste]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users).

{% alert important %}
A Braze bloqueia perfis de usuário que crescem de forma anormalmente grande ("usuários fictícios"), pois esses perfis geralmente são resultado de uma integração incorreta. Um perfil é bloqueado quando excede qualquer um dos seguintes limites:

- Mais de 5.000.000 de sessões
- Mais de 20.000 nomes distintos de eventos personalizados
- Mais de 20.000 nomes distintos de produtos em compras

Depois que um perfil é bloqueado, a Braze para de ingerir todos os dados de entrada para esse perfil, tanto dos SDKs quanto da REST API. Se você descobrir que isso aconteceu com um usuário legítimo, entre em contato com o gerente de conta da Braze. Para saber mais, consulte [Bloqueio de spam]({{site.baseurl}}/user_archival).
{% endalert %}