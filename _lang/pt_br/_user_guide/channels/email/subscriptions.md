---
nav_title: "Inscrições"
article_title: "Inscrições"
page_order: 5
description: "Este artigo de referência aborda os diferentes estados de inscrição de usuários, como criar e gerenciar grupos de inscrições e como segmentar usuários com base em suas inscrições."
channel:
  - email

---

# Inscrições de e-mail

> Saiba mais sobre os estados de inscrição de usuários, como criar e gerenciar grupos de inscrições e como segmentar usuários com base em suas inscrições.

Este documento é apenas para fins informativos. Ele não se destina a fornecer, nem pode ser utilizado como, aconselhamento jurídico de qualquer natureza. O envio de e-mails de marketing e de transação pode estar sujeito a requisitos legais específicos. Para garantir que você esteja em conformidade com todas as leis, regras e regulamentos aplicáveis à sua empresa, consulte seu departamento jurídico e/ou equipe de conformidade regulatória.

## Estados de inscrição {#subscription-states}

A Braze possui três estados globais de inscrição para usuários de e-mail. Esses estados controlam o envio de mensagens aos usuários. Por exemplo, usuários no estado `unsubscribed` não recebem mensagens direcionadas a `subscribed` ou `opted-in`.

| Estado | Definição |
| ----- | ---------- |
| Opted-in | O usuário confirmou explicitamente que deseja receber e-mails. Recomendamos um processo de opt-in explícito para obter o consentimento dos usuários para o envio de e-mails. |
| Subscribed | O usuário não cancelou a inscrição nem optou explicitamente por receber e-mails. Este é o estado de inscrição padrão quando um perfil de usuário é criado. |
| Unsubscribed | O usuário cancelou explicitamente a inscrição dos seus e-mails. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
A Braze não contabiliza alterações no estado de inscrição como pontos de dados, tanto globalmente quanto em relação a grupos de inscrições.
{% endalert %}

### Endereços de e-mail com inscrição cancelada

A Braze cancela automaticamente a inscrição de qualquer usuário que cancele manualmente a inscrição por meio de um [rodapé personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/). Se o usuário atualizar seu endereço de e-mail e a opção **Reinscrever usuários quando atualizarem o e-mail** estiver ativada em **Configuração de envio**, o envio normal será retomado.

Se um usuário marcar um ou mais dos seus e-mails como spam, a Braze enviará apenas e-mails de transação para esse usuário. E-mails de transação referem-se à opção **Enviar para todos os usuários, incluindo os que cancelaram a inscrição** em **Público-alvo**.

{% alert tip %}
Consulte nossas práticas recomendadas de [aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/) para orientações sobre como reengajar seus usuários de forma eficaz.
{% endalert %}

### Bounces e e-mails inválidos

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}

Quando um endereço de e-mail sofre hard bounce, a Braze não altera automaticamente o estado de inscrição do usuário para "unsubscribed". Se um endereço sofrer hard bounce (inválido ou inexistente), a Braze o marca como inválido e não tenta novos envios. Se o usuário alterar seu endereço de e-mail, a Braze retoma o envio. A Braze faz novas tentativas de soft bounces por 72 horas.

### Atualizando estados de inscrição de e-mail

Existem quatro maneiras de atualizar o estado de inscrição de e-mail de um usuário:

#### Integração de SDK

Use o SDK da Braze para atualizar o estado de inscrição de um usuário.

#### REST API

Use o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para atualizar o [atributo `email_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) de um usuário. Por exemplo, para definir o estado de inscrição de e-mail de um usuário como cancelado quando ele usar um link de cancelamento de inscrição personalizado, inclua `email_subscribe: "unsubscribed"` nos atributos do usuário na sua requisição.

#### Perfil de usuário

1. Encontre o usuário em **Pesquisar usuários**.
2. Em **Engajamento**, selecione **Unsubscribed**, **Subscribed** ou **Opted In** para alterar o status de inscrição do usuário.

Se disponível, o perfil de usuário também exibe um registro de data e hora de quando a inscrição do usuário foi alterada pela última vez.

#### Central de Preferências

Inclua o Liquid da [Central de Preferências](#email-preference-center) na parte inferior dos seus e-mails para permitir que os usuários façam opt-in ou opt-out. A Braze gerencia as atualizações do estado de inscrição a partir da Central de Preferências.

### Verificando o estado de inscrição de e-mail

![Perfil de usuário de John Doe com o estado de inscrição de e-mail definido como Subscribed.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Você pode verificar o estado de inscrição de e-mail de um usuário das seguintes maneiras:

1. **Exportação via REST API:** Use os endpoints [Exportar usuários por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Exportar usuários por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para exportar perfis de usuários individuais em formato JSON.
2. **Perfil de usuário:** Encontre o perfil do usuário na página [Pesquisar usuários]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/), depois selecione a guia **Engajamento** para visualizar e atualizar manualmente o estado de inscrição de um usuário.

Quando um usuário atualiza seu endereço de e-mail, o estado de inscrição será definido como subscribed, a menos que o endereço de e-mail atualizado já exista em outro lugar em um espaço de trabalho da Braze.

## Grupos de inscrições

Grupos de inscrições são filtros de segmento que podem refinar ainda mais seu público a partir dos [estados globais de inscrição](#subscription-states). Esses grupos permitem que você apresente opções de inscrição mais detalhadas aos usuários finais.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

Por exemplo, suponha que você envie várias categorias de Campaigns de e-mail (promocionais, newsletter ou atualizações de produto). Nesse caso, você pode usar grupos de inscrições para permitir que seus clientes escolham de quais categorias de e-mail desejam se inscrever ou cancelar a inscrição em massa a partir de uma única página, usando uma [Central de Preferências de e-mail](#email-preference-center). Outra opção é usar grupos de inscrições para permitir que seus clientes escolham com que frequência desejam receber e-mails, criando grupos de inscrições para e-mails diários, semanais ou mensais.

Use os [endpoints de grupos de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups/) para gerenciar programaticamente os grupos de inscrições que você armazenou no dashboard da Braze na página **Grupos de inscrições**.

### Criando um grupo de inscrições

1. Acesse **Público** > **Gerenciamento de grupos de inscrições**.
2. Selecione **Criar grupo de inscrições de e-mail**.
3. Dê um nome e uma descrição ao seu grupo de inscrições.
4. Selecione **Salvar**.

Todos os grupos de inscrições são adicionados automaticamente à sua Central de Preferências.

![Campos para criar um grupo de inscrições.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentando com um grupo de inscrições

Ao criar seus segmentos, defina o nome do grupo de inscrições como filtro. Isso garantirá que os usuários que optaram pelo seu grupo receberão seus e-mails. Isso é ótimo para newsletters mensais, cupons, níveis de associação e muito mais.

![Exemplo de direcionamento de usuários no segmento "Lapsed Users" com o filtro para usuários no grupo de inscrições "Weekly Emails".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Arquivando grupos de inscrições

Grupos de inscrições arquivados não podem ser editados e não aparecerão mais nos filtros de segmento nem na sua Central de Preferências. Se você tentar arquivar um grupo que está sendo usado como filtro de segmento em qualquer e-mail, Campaign ou Canvas, receberá uma mensagem de erro que impedirá o arquivamento do grupo até que você remova todos os usos dele.

Para arquivar seu grupo na página **Grupos de inscrições**, faça o seguinte:

1. Encontre seu grupo na lista de grupos de inscrições.
2. Selecione **Arquivar** no menu suspenso <i class="fa-solid fa-ellipsis-vertical"></i>.

A Braze não processa alterações de estado para usuários em grupos arquivados. Por exemplo, se você arquivar o Grupo de inscrições 1 enquanto Alex está inscrito nele, Alex permanecerá como "inscrito" mesmo que clique em um link de cancelamento de inscrição. Isso não importa porque o Grupo de inscrições 1 está arquivado e você não pode enviar mensagens usando ele.

#### Visualizando tamanhos de grupos de inscrições

Você pode consultar o gráfico **Série temporal do grupo de inscrições** na página **Grupos de inscrições** para visualizar o tamanho do grupo de inscrições com base no número de usuários ao longo de um período de tempo. Esses tamanhos de grupos de inscrições também são consistentes com outras áreas da Braze, como o cálculo de tamanho de segmento.

![Um exemplo de gráfico "Série temporal do grupo de inscrições" datado de 2 a 11 de dezembro. O gráfico mostra um aumento de aproximadamente 10 milhões no número de usuários do dia 6 para o dia 7.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

Se a contagem da série temporal divergir significativamente de um segmento usando **Status de inscrição de e-mail é Unsubscribed**, lembre-se de que o gráfico conta a participação naquele **grupo de inscrições**, enquanto o filtro reflete o estado **global** de inscrição de e-mail — por exemplo, os usuários podem estar globalmente inscritos, mas com inscrição cancelada em um grupo específico.

#### Visualizando grupos de inscrições na análise de dados de Campaigns

Você pode ver a contagem de usuários que alteraram seu estado de inscrição (inscreveram-se ou cancelaram a inscrição) a partir de uma Campaign de e-mail específica na página de análise de dados dessa Campaign.

1. Na página **Análise de dados da Campaign** da sua Campaign, role para baixo até a seção **Desempenho da mensagem de e-mail**.
2. Selecione a seta em **Grupos de inscrições** para ver a contagem agregada de alterações de estado, conforme enviadas pelos seus clientes.

![A página "Desempenho da mensagem de e-mail" exibindo a contagem agregada de alterações de estado enviadas pelos clientes.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Verificando o grupo de inscrições de e-mail de um usuário

- **Perfil de usuário:** Perfis de usuários individuais podem ser acessados pelo dashboard da Braze na página [Pesquisar usuários]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#access-profiles). Lá, você pode pesquisar perfis de usuários por endereço de e-mail, número de telefone ou ID de usuário externo. Você também pode visualizar os grupos de inscrições de e-mail de um usuário na guia **Engajamento**.
- **REST API da Braze:** Use o [endpoint Listar grupos de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou o [endpoint Listar status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) para visualizar os grupos de inscrições de perfis de usuários individuais.

## Central de Preferências de e-mail {#email-preference-center}

A Central de Preferências de e-mail permite gerenciar quais usuários recebem newsletters de grupos de inscrições. Encontre-a no dashboard em **Grupos de inscrições**. Cada grupo de inscrições que você criar é adicionado à lista da Central de Preferências.

Para saber mais sobre como adicionar ou personalizar uma Central de Preferências, consulte [Central de Preferências]({{site.baseurl}}/user_guide/channels/email/subscriptions/).

## Alterando inscrições de e-mail {#changing-email-subscriptions}

Na maioria dos casos, os usuários gerenciam sua inscrição de e-mail por meio de links incluídos nos e-mails que recebem. Insira um rodapé legalmente compatível com um link de cancelamento de inscrição na parte inferior de cada e-mail. Quando os usuários selecionam a URL de cancelamento de inscrição, a Braze cancela a inscrição deles e exibe uma landing page confirmando a alteração. Inclua esta Liquid tag: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Quando um usuário seleciona "Cancelar inscrição de todos os tipos de e-mail acima" na Central de Preferências, a Braze define o status global de inscrição de e-mail como `unsubscribed` e cancela a inscrição de todos os grupos.

### Criando rodapés personalizados {#custom-footer}

Se você não quiser usar o rodapé padrão, crie um rodapé de e-mail personalizado para todo o espaço de trabalho e insira-o em cada e-mail usando {% raw %}`{{${email_footer}}}`{% endraw %}.

Isso evita a necessidade de criar um novo rodapé para cada modelo de e-mail ou Campaign de e-mail. Para ver os passos, consulte [Rodapé de e-mail personalizado]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer/).

#### Gerenciando estados de inscrição para endereços IP chineses

Se você prevê endereços IP chineses, não dependa exclusivamente de um link de cancelamento de inscrição para manter listas de `unsubscribed`. Forneça caminhos alternativos de cancelamento de inscrição, como um ticket de suporte ou e-mail de um representante de atendimento ao cliente.

### Criando uma página de cancelamento de inscrição personalizada

Quando os usuários selecionam uma URL de cancelamento de inscrição em um e-mail, eles abrem uma landing page padrão que confirma a alteração da inscrição.

Para usar uma landing page personalizada:

1. Acesse **Preferências de e-mail** > **Páginas e rodapés da inscrição**.
2. Adicione o HTML da sua página personalizada.

Inclua um link de reinscrição (por exemplo {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) para que os usuários possam desfazer um cancelamento de inscrição acidental.

Você também pode enviar os usuários para o seu site e atualizar o status com a REST API da Braze (por exemplo, link com {% raw %}`?user_id={{${user_id}}}`{% endraw %} e depois chamar [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/)).

{% alert note %}
Se você usar o rodapé do dashboard em vez de apenas um bloco de conteúdo HTML, o modelo ainda deve conter {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} para salvar. Para usar uma URL de cancelamento de inscrição diferente temporariamente, você pode comentar a tag padrão. Um exemplo é: {% raw %}`<!-- {{${set_user_to_unsubscribed_url}}} -->`{% endraw %}.
{% endalert %}

![Página de cancelamento de inscrição personalizada com uma pré-visualização "Sentimos muito em ver você partir!".]({% image_buster /assets/img/custom_unsubscribe.png %})

### Criando uma página de opt-in personalizada

Use uma página de opt-in personalizada para permitir que os usuários reconheçam e controlem as preferências de notificação antes da inscrição. Essa comunicação adicional pode ajudar as Campaigns de e-mail a não caírem em pastas de spam.

1. Acesse **Configurações** > **Preferências de e-mail**.
2. Selecione **Páginas e rodapés da inscrição**.
3. Personalize o estilo na seção **Página de opt-in personalizada** para ver como isso indica aos seus usuários que eles foram inscritos.

Os usuários chegam a esta página por meio da tag {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}.

{% alert tip %}
Use um processo de double opt-in para melhorar o alcance. A Braze envia um e-mail de confirmação adicional onde o usuário confirma as preferências de notificação por meio de um link. Após a confirmação, o usuário é marcado como opted-in.
{% endalert %}

![E-mail de opt-in personalizado com a mensagem "Que bom que você ainda quer receber nossas novidades".]({% image_buster /assets/img/custom_optin.png %})

## Inscrições e direcionamento de Campaigns {#subscriptions-and-campaign-targeting}

Por padrão, a Braze direciona Campaigns com mensagens push ou de e-mail para usuários que estão inscritos ou com opt-in. Altere isso em **Público-alvo** selecionando o menu suspenso ao lado de **Enviar para estes usuários:**.

A Braze suporta três estados de direcionamento:

- Usuários que estão inscritos ou com opt-in (padrão).
- Apenas usuários com opt-in.
- Todos os usuários, incluindo aqueles que cancelaram a inscrição.

{% alert important %}
É sua responsabilidade cumprir todas as [leis de spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) aplicáveis ao usar essas configurações de direcionamento.
{% endalert %}

## Segmentando por inscrições de usuários {#segmenting-by-user-subscriptions}

Use os filtros "Status de inscrição de e-mail" e "Status de inscrição de push" para segmentar usuários por status de inscrição.

Use isso para direcionar usuários que não fizeram opt-in nem opt-out e incentive um opt-in explícito. Crie um segmento com o filtro "Status de inscrição de e-mail/push é Subscribed" e envie Campaigns para usuários que estão inscritos, mas não fizeram opt-in.

![Status de inscrição de e-mail usado como filtro de segmento.]({% image_buster /assets/img_archive/not_optin.png %})