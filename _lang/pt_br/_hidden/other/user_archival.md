---
nav_title: Arquivamento de usuários
article_title: Arquivamento de usuários
permalink: /user_archival/
page_order: 0
page_type: reference
description: "Este artigo de referência aborda as definições de arquivamento de usuários, o bloqueio de spam e como personalizar a política de arquivamento de usuários."

---
# Arquivamento de usuários {#user-archival}

> Toda semana, no domingo, às 5:30 am EST, a Braze executa um processo para remover usuários ociosos e usuários inativos dos Serviços da Braze. Note que a Braze não arquiva usuários a menos que o número de usuários no espaço de trabalho atinja o limite de 250 mil.

Esse processo tem o objetivo de ajudar a Braze a fornecer estatísticas precisas com relação aos públicos alcançáveis por Campaign. Ele também está de acordo com dois conceitos-chave do [GDPR][1]:

1. O princípio da limitação de armazenamento — os dados pessoais processados e armazenados não devem ser mantidos por mais tempo do que o necessário
2. Ter uma finalidade comercial legítima para processar dados pessoais.

Ou seja, os dados pessoais processados e armazenados não devem ser mantidos por mais tempo do que o necessário, e os dados pessoais só devem ser processados para fins comerciais legítimos. Os usuários arquivados também terão seu status de cancelamento de inscrição excluído em conformidade com o GDPR.

{% alert important %}
Os usuários arquivados serão excluídos permanentemente. <br><br>É possível [personalizar a política de arquivamento do usuário](#customizing-your-user-archival-policy) usando o Canvas. Os clientes têm controle total sobre se um usuário está ocioso ou inativo. O Canvas oferece a capacidade de fazer isso automaticamente, o que permite desativar efetivamente essa funcionalidade para alguns ou todos os seus usuários ociosos ou inativos.
{% endalert %}

## Definições de arquivamento de usuário {#user-archival-definitions}

### Usuários ativos {#active-users}

A Braze define um "usuário ativo" em um determinado período como qualquer usuário que registrou uma sessão em um app móvel ou website, foi atualizado, recebeu uma mensagem ou interagiu com uma mensagem.

Se você definir IDs de usuário para identificar usuários quando um novo usuário faz login, ele será contado como um usuário ativo separado. Usuários atualizados pela API também serão contados como usuários ativos no período em que forem atualizados.

{% alert important %}
Tanto os usuários inativos quanto os usuários inativos (dormant) serão arquivados, a menos que o usuário esteja excluído do arquivamento pelos motivos listados abaixo.
{% endalert %}

### Usuários inativos {#inactive-users}

"Usuários inativos" são usuários que não podem ser alcançados e provavelmente sofreram churn. Usuários inativos são aqueles que atendem a todos estes critérios:

- Não podem receber e-mail. Por exemplo, não possuem um endereço de e-mail ou cancelaram a inscrição de todas as listas de e-mails.
- Não podem receber SMS. Por exemplo, não possuem um número de telefone válido ou cancelaram a inscrição de todos os grupos de inscrições de SMS.
- Não podem receber push. Por exemplo, desinstalaram o app ou desativaram as permissões de push.
- Não podem receber uma mensagem de WhatsApp. Por exemplo, não possuem um número de telefone válido ou cancelaram a inscrição de todos os grupos de inscrições de WhatsApp.
- Não podem receber uma mensagem de LINE. Por exemplo, não possuem um LINE ID ou cancelaram a inscrição de todos os grupos de inscrições de LINE.
- Não usaram nenhum app móvel nem visitaram um website em um espaço de trabalho por mais de seis meses.
- Não receberam nenhuma mensagem de um espaço de trabalho por mais de seis meses.
- Não foram atualizados por mais de seis meses.

Nesse caso, esses usuários não podem receber mensagens e não estão engajando com a sua marca. Esses usuários efetivamente sofreram churn.

### Usuários inativos (dormant) {#dormant-users}

"Usuários inativos (dormant)" são usuários que não tiveram nenhuma atividade nos últimos doze meses e:

- Não usaram nenhum app móvel nem visitaram um website em um espaço de trabalho por mais de 12 meses.
- Não receberam nenhuma mensagem de um espaço de trabalho por mais de 12 meses.
- Não foram atualizados por mais de 12 meses.

## Usuários do grupo de controle global {#global-control-group-users}

Usuários no grupo de controle global nunca serão arquivados, mesmo que atendam à definição de usuários inativos.

### Grupo de amostra de tratamento {#treatment-sample-group}

Usuários do grupo de amostra de tratamento em um relatório de grupo de controle global são excluídos do arquivamento.

## Usuários teste {#test-users}

Usuários teste nunca serão arquivados, mesmo que atendam à definição de usuários inativos.

## Bloqueio de SPAM {#spam-blocking}

A Braze bloqueia perfis de usuário individuais que crescem de forma anormalmente grande ("usuários fictícios"), pois geralmente são resultado de uma integração incorreta. Um perfil é bloqueado quando excede qualquer um dos seguintes limites:

| Limite | Descrição |
| --- | --- |
| Mais de 5.000.000 de sessões | Normalmente causado pela reutilização de um único `external_id` em vários usuários. |
| Mais de 20.000 nomes distintos de eventos personalizados | Normalmente causado pela geração de um novo nome de evento para cada evento, em vez de reutilizar um conjunto fixo de nomes. |
| Mais de 20.000 nomes distintos de produtos em compras | Normalmente causado pela geração de um novo `product_id` para cada compra, em vez de reutilizar um conjunto fixo de IDs de produto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites de bloqueio de usuários fictícios" }

Depois que um perfil é bloqueado, a Braze para de ingerir todos os dados de entrada desse perfil, tanto dos SDKs quanto da REST API. Requisições para [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) que referenciam um identificador bloqueado retornam o erro `"provided external_id is blacklisted and disallowed"`. Esse texto é extraído literalmente da resposta da API. A Braze também notifica o gerente da sua conta Braze para que ele possa levantar o problema de integração com você.

Se você descobrir que isso aconteceu com um usuário legítimo, abra um ticket com o [suporte]({{site.baseurl}}/braze_support) da Braze.

Para encontrar os usuários fictícios do seu dashboard, siga estas etapas:

1. Crie um [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Selecione o filtro `Session Count` e defina como `more than 5,000,000`.
3. Exporte o Segment via CSV.

O filtro **Session Count** encontra apenas usuários fictícios baseados em sessão. Não existe um filtro de segmentação para o número de nomes distintos de eventos personalizados ou nomes de produtos em um perfil. Entre em contato com o gerente da sua conta Braze para identificar perfis bloqueados por esses motivos.

Se necessário, você pode excluir os usuários por meio do [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete).

## Personalizando sua política de arquivamento de usuário {#customizing-your-user-archival-policy}

A Braze oferece recursos de orquestração de dados que permitem personalizar sua política de arquivamento de usuário. Crie uma política de arquivamento de usuário que ofereça o melhor dos dois mundos com o componente [User Update]({{site.baseurl}}/user_update) do Canvas.

Isso permite que você:

- Siga as melhores práticas de GDPR e privacidade, excluindo perfis de usuário que não são mais valiosos.
- Retenha qualquer perfil de usuário para o qual você tenha uma necessidade comercial legítima.

### Etapas {#steps}

1. Direcione os usuários que atendem aos critérios de arquivamento da sua marca e que você gostaria de reter. Por exemplo, você pode reter usuários que:
    - Receberam uma mensagem pela última vez há mais de 23 semanas ou nunca receberam uma mensagem<br>E<br>
    - Usaram seu app pela última vez há mais de 23 semanas ou tiveram zero sessões no seu app<br><br>
      ![Direcione usuários que receberam qualquer mensagem pela última vez há mais de 23 semanas, nunca receberam uma mensagem de uma Campaign ou etapa do Canvas, usaram esses apps pela última vez há mais de 23 semanas e usaram esses apps exatamente zero vezes.][2]<br><br>
2. Defina a reelegibilidade para um período um pouco menor que 6 meses.<br><br>
      ![Controles de entrada com reelegibilidade ativada e a janela de reelegibilidade definida para 23 semanas.][3]<br><br>
3. Configure a etapa User Update para adicionar um evento a cada perfil.<br><br>
      ![Etapa User Update que adiciona o evento "do_not_archive" ao perfil do usuário.][4]
{% details Exemplo de objeto User Update %}

{% raw %}
```json
{
    "events": [
        {
            "name": "do_not_archive",
            "time": "{{ 'now' | time_zone: 'UTC' | date: '%Y-%m-%dT%H:%M:%SZ' }}"
        }
    ]
}
```
{% endraw %}

{% enddetails %}

[1]: {{site.baseurl}}/dp-technical-assistance/#the-right-to-erasure
[2]: {% image_buster /assets/img_archive/user_archival_policy1.png %}
[3]: {% image_buster /assets/img_archive/user_archival_policy2.png %}
[4]: {% image_buster /assets/img_archive/user_archival_policy3.png %}