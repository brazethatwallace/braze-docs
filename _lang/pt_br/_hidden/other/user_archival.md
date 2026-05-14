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

## Definições de arquivamento de usuários {#user-archival-definitions}

### Usuários ativos {#active-users}

A Braze define um "usuário ativo" por um determinado período de tempo como qualquer usuário que tenha registrado uma sessão em um app móvel ou site, que tenha sido atualizado, que tenha recebido uma mensagem ou que tenha interagido com uma mensagem.

Se você definir IDs de usuário para identificar usuários quando um novo usuário se registrar, ele será contado como um usuário ativo separado. Os usuários que forem atualizados por meio da API também serão contados como usuários ativos no período em que forem atualizados.

{% alert important %}
Tanto os usuários ociosos quanto os usuários inativos serão arquivados, a menos que o usuário seja excluído do arquivamento pelos motivos listados abaixo.
{% endalert %}

### Usuários ociosos {#inactive-users}

"Usuários ociosos" são usuários que não podem ser contatados e que provavelmente sofreram churn. Os usuários ociosos são aqueles que atendem a todos esses critérios:

- Não podem receber e-mails. Por exemplo, não têm um endereço de e-mail ou cancelaram a inscrição em todas as listas de e-mail.
- Não podem receber SMS. Por exemplo, não têm um número de telefone válido ou cancelaram a inscrição em todos os grupos de inscrições de SMS.
- Não podem receber push. Por exemplo, desinstalaram o app ou desativaram as permissões de push.
- Não podem receber uma mensagem do WhatsApp. Por exemplo, não têm um número de telefone válido ou cancelaram a inscrição em todos os grupos de inscrições do WhatsApp.
- Não podem receber uma mensagem LINE. Por exemplo, não têm um ID do LINE ou cancelaram a inscrição em todos os grupos de inscrições do LINE.
- Não usaram nenhum app móvel nem visitaram um site em um espaço de trabalho há mais de seis meses.
- Não receberam nenhuma mensagem de um espaço de trabalho há mais de seis meses.
- Não foram atualizados há mais de seis meses.

Nesse caso, esses usuários não podem receber mensagens e não estão se engajando com a sua marca. Esses usuários efetivamente sofreram churn.

### Usuários inativos {#dormant-users}

"Usuários inativos" são usuários que não tiveram nenhuma atividade nos últimos doze meses e:

- Não usaram nenhum app móvel nem visitaram um site em um espaço de trabalho há mais de 12 meses.
- Não receberam nenhuma mensagem de um espaço de trabalho há mais de 12 meses.
- Não foram atualizados há mais de 12 meses.

## Usuários do grupo de controle global {#global-control-group-users}

Os usuários do grupo de controle global nunca serão arquivados, mesmo que atendam à definição de usuários ociosos ou inativos.

### Amostra do grupo de tratamento {#treatment-sample-group}

Os usuários da amostra do grupo de tratamento em um relatório do grupo de controle global são excluídos do arquivamento.

## Usuários teste {#test-users}

Os usuários teste nunca serão arquivados, mesmo que atendam à definição de usuários ociosos ou inativos.

## Bloqueio de spam {#spam-blocking}

A Braze bloqueia usuários individuais com mais de 5 milhões de sessões ("usuários fictícios") e não ingere mais seus eventos de SDK, porque eles geralmente são o resultado de uma integração incorreta. Se você descobrir que isso aconteceu com um usuário legítimo, abra um ticket para o [suporte]({{site.baseurl}}/braze_support/) da Braze.

Para encontrar os usuários fictícios do dashboard, execute as etapas a seguir:

1. Crie um [segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/).
2. Selecione o filtro `Session Count` e defina-o como `more than 5,000,000`.
3. Exporte o segmento via CSV.

Se necessário, você pode excluir os usuários por meio do [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).

## Personalização da política de arquivamento do usuário {#customizing-your-user-archival-policy}

A Braze fornece recursos de orquestração de dados que permitem personalizar sua política de arquivamento de usuários. Crie uma política de arquivamento de usuários que ofereça o melhor dos dois mundos com o componente [Atualização de usuário]({{site.baseurl}}/user_update/) do Canvas.

Isso permite que você:

- Siga o GDPR e as práticas recomendadas de privacidade, excluindo perfis de usuários que não são mais valiosos.
- Mantenha todos os perfis de usuário para os quais você tenha uma necessidade comercial legítima.

### Etapas {#steps}

1. Direcione usuários que atendem aos critérios de arquivamento da sua marca e que você gostaria de reter. Por exemplo, você pode reter usuários que:
    - Receberam uma mensagem pela última vez há mais de 23 semanas ou nunca receberam uma mensagem<br>E<br>
    - Usaram seu app pela última vez há mais de 23 semanas ou tiveram zero sessões no app<br><br>
      ![Usuários-alvo que receberam qualquer mensagem pela última vez há mais de 23 semanas, nunca receberam uma mensagem de uma Campaign ou etapa do Canvas, usaram esses apps pela última vez há mais de 23 semanas e usaram esses apps exatamente zero vezes.][2]<br><br>
2. Defina a reelegibilidade para um período de pouco menos de 6 meses.<br><br>
      ![Controles de entrada com a reelegibilidade ativada e o período de reelegibilidade definido para 23 semanas.][3]<br><br>
3. Configure a etapa de Atualização de usuário para adicionar um evento a cada perfil.<br><br>
      ![Etapa de Atualização de usuário que adiciona o evento "do_not_archive" ao perfil do usuário.][4]
{% details Exemplo de objeto de Atualização de usuário %}

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