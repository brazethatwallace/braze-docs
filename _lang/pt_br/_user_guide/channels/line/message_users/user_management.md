---
nav_title: Gerenciamento de usuários
article_title: Gerenciamento de usuários LINE
page_order: 0
description: "Este artigo aborda o ID de usuário LINE e como configurá-lo."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# Gerenciamento de usuários LINE {#line-user-management}

> O ID de usuário LINE é armazenado no atributo de perfil de usuário chamado `native_line_id`, que é usado para enviar mensagens a um usuário no canal LINE. Este artigo aborda como configurar e encontrar o atributo `native_line_id`.

Os dados de usuários são representados em um [perfil de usuário da Braze]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle). Um perfil de usuário armazena informações e atributos sobre os usuários de uma empresa, como nomes e endereços de e-mail.

Quando você envia mensagens LINE pela Braze, a Braze usa o atributo `native_line_id` para identificar para quais usuários enviar a mensagem. Quando o LINE envia eventos de webhook para a Braze, como quando um usuário segue um canal ou responde a uma mensagem, o `native_line_id` é usado para buscar o perfil de usuário correspondente.

{% alert note %}
Os IDs de usuário LINE são distintos por provedor LINE. Um usuário específico terá IDs de usuário LINE diferentes para cada provedor que seguir. É improvável que os usuários saibam seu ID LINE (diferentemente do e-mail ou número de telefone), pois ele muda para cada marca que seguem.
{% endalert %}

## Configurando o atributo `native_line_id` {#setting-the-native_line_id-attribute}

Existem vários cenários em que o `native_line_id` é definido no perfil de usuário, descritos abaixo.

| Cenário | Se existe perfil de usuário com `native_line_id` | Resultado |
| --- | --- | --- |
| Um usuário segue um canal LINE | Não | Um perfil de usuário anônimo é criado (será necessário fazer merge):<br> - `native_line_id` é definido como o ID LINE do usuário <br>- O alias de usuário `line_id` é definido como o ID LINE do usuário<br>- O usuário é inscrito no grupo de inscrições da Braze do canal |
| Um usuário segue um canal LINE | Sim | Todos os perfis de usuário com o `native_line_id`:<br>- São inscritos no grupo de inscrições da Braze do canal |
| A empresa usa upload de CSV de usuários com uma coluna `native_line_id` | Não | Se não existir perfil de usuário para o `external_id` ou alias de usuário especificado:<br>- `native_line_id` é definido com o valor especificado<br> - Todos os outros atributos especificados no CSV são definidos no perfil de usuário |
| A empresa usa upload de CSV de usuários com uma coluna `native_line_id` | Sim | Se existir um perfil de usuário para o `external_id` ou alias de usuário especificado:<br>- `native_line_id` é definido com o valor especificado<br>- Todos os outros atributos especificados no CSV são definidos no perfil de usuário<br>- Múltiplos perfis terão o mesmo `native_line_id` |
| A empresa usa o endpoint `/users/track` e especifica o atributo `native_line_id` | Não | Se não existir perfil de usuário para o usuário especificado ([especificado por `external_id`, `user_alias`, `braze_id` ou `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens)):<br>- `native_line_id` é definido com o valor especificado<br>- Todos os outros atributos especificados na solicitação são definidos no perfil de usuário |
| A empresa usa o endpoint `/users/track` e especifica o atributo `native_line_id` | Sim | Se existir um perfil de usuário para o usuário especificado ([especificado por `external_id`, `user_alias`, `braze_id` ou `email`]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens)):<br>- `native_line_id` é definido com o valor especificado<br>- Todos os outros atributos especificados na solicitação são definidos no perfil de usuário<br>- Múltiplos perfis terão o mesmo `native_line_id` |
| A empresa solicita que a Braze execute o sincronizador de status de inscrição | Não | Se um ID de usuário LINE retornado pelo LINE não tiver um perfil de usuário correspondente na Braze, um perfil de usuário anônimo será criado:<br>- `native_line_id` é definido como o ID LINE do usuário<br>- O alias de usuário `line_id` é definido como o ID LINE do usuário<br>- O usuário é inscrito no grupo de inscrições da Braze do canal<br><br>Observe que, se um usuário com o mesmo ID LINE for criado posteriormente, haverá usuários duplicados, mas ambos terão o status de inscrição LINE correto. O merge de usuários pode limpar sua base de usuários nesses casos. |
| A empresa solicita que a Braze execute o sincronizador de status de inscrição | Sim | Se um ID de usuário LINE retornado pelo LINE tiver um perfil de usuário correspondente na Braze:<br>- O usuário é inscrito no grupo de inscrições da Braze do canal |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Configurando o atributo nativelineid" }

## Encontrando o `native_line_id` {#finding-the-native_line_id}

Ao visualizar um perfil de usuário no dashboard da Braze, você pode verificar se o atributo `native_line_id` está definido acessando a guia **Engagement** > seção **Contact Settings** > seção **LINE**.

Se o `native_line_id` tiver sido definido, ele será exibido em **LINE User ID**. Caso contrário, não aparecerá.

![Configurações de contato LINE na guia Engagement.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}