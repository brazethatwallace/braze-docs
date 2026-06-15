---
nav_title: Talkable
article_title: Talkable
description: "Este artigo de referência descreve a parceria entre a Braze e a Talkable, uma plataforma de marketing de indicação que sincroniza opt-ins de e-mail de marketing de campanhas de indicação para a Braze em tempo real."
alias: /partners/talkable/
page_type: partner
search_tag: Partner
---

# Talkable

> A [Talkable](https://www.talkable.com/) ajuda marcas de consumo a transformar clientes satisfeitos em um canal de indicação escalável. Com a integração da Braze, os opt-ins de e-mail de marketing capturados nas campanhas de indicação da Talkable fluem para a Braze em tempo real, fornecendo à sua equipe o consentimento, o contexto e os dados de campanha necessários para dar boas-vindas, segmentar e engajar cada novo promotor e amigo indicado.

_Esta integração é mantida pela Talkable._

## Sobre a integração {#about-the-integration}

A Talkable traz a aquisição liderada por promotores para a jornada do cliente que a Braze potencializa. A integração move cada opt-in de indicação capturado pela Talkable para o perfil correspondente na Braze em tempo real, para que fluxos de boas-vindas, jornadas de indicação, segmentação e envio de mensagens de ciclo de vida possam ser lançados a partir de consentimento confiável e contexto de indicação — tudo sem exportações manuais de listas ou sincronizações em lote.

A Talkable captura opt-ins de marketing em dois cenários:

* **Cadastro do promotor:** Um promotor se cadastra em uma campanha de indicação da Talkable e consente em receber e-mails de marketing.
* **Gating de e-mail do amigo:** Um amigo indicado completa a etapa de gating de e-mail da Talkable e opta por receber e-mails de marketing.

Em ambos os casos, a Talkable cria ou atualiza o perfil de usuário correspondente na Braze em tempo real e define o estado de inscrição de e-mail do usuário como **Opted In**.

### Comportamento padrão {#default-behavior}

A Talkable envia dados para a Braze apenas em um evento discreto de opt-in de alguém que consentiu explicitamente na Talkable — seja um promotor se cadastrando em uma campanha ou um amigo optando por participar durante o gating de e-mail. A Talkable não executa lotes noturnos, sincronizações completas ou atualizações implícitas de perfil. A Talkable nunca envia perfis que não fizeram opt-in para a Braze.

## Casos de uso {#use-cases}

- Acionar um Canvas de boas-vindas na Braze no momento em que um promotor se cadastra em uma campanha de indicação da Talkable.
- Ativar amigos indicados com um Canvas específico para amigos e uma oferta personalizada de primeira compra assim que o amigo fizer opt-in.
- Segmentar por contexto de indicação usando flags de promotor e amigo e metadados de campanha enviados como atributos personalizados da Braze.
- Direcionar opt-ins de indicação para um grupo de inscrições designado na Braze para envio de newsletters em conformidade.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa do seguinte:

| Pré-requisito | Descrição |
| --- | --- |
| Uma conta Talkable | Um site Talkable com pelo menos uma campanha configurada é necessário para aproveitar esta parceria. |
| Uma chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. Crie essa chave no dashboard da Braze em **Configurações** > **Chaves de API**. Para saber mais, consulte [Criando chaves da API REST]({{site.baseurl}}/api/basics/#creating-rest-api-keys). |
| Um endpoint REST da Braze | A URL do seu endpoint REST da Braze (por exemplo, `https://rest.iad-01.braze.com`). Tanto clusters US (`.com`) quanto EU (`.eu`) da Braze são suportados. Para saber mais, consulte [Endpoints da REST API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Instalar o app da Braze na Talkable {#step-1-install-the-braze-app-in-talkable}

1. Faça login no painel de administração da Talkable e abra o menu, depois acesse **All Site Settings** > **App Store**.
2. Localize **Braze** e selecione **Install**.
3. Insira seu endpoint REST da Braze e uma chave da API REST com permissões `users.track`, depois selecione **Save**.

### Etapa 2: Configurar a ação de opt-in de e-mail {#step-2-configure-the-email-opt-in-action}

1. No app da Braze na Talkable, abra a ação **Email opt-in**.
2. (Opcional) Insira um identificador de grupo de inscrições da Braze, adicione atributos personalizados e/ou configure um alias de usuário. Para saber mais, consulte [Personalizar a Talkable](#customizing-talkable).
3. Selecione **Save**. Deixe a ação desativada para que você possa verificar a configuração com uma carga útil de teste antes que qualquer evento de opt-in ao vivo comece a sincronizar.

### Etapa 3: Testar com uma carga útil de exemplo {#step-3-test-with-a-sample-payload}

1. Na Talkable, selecione **Send sample payload** na ação **Email opt-in** para enviar uma solicitação de teste para a Braze.
2. Na Braze, acesse **Audience** > **User Search** e pesquise pelo endereço de e-mail de teste.
3. Confirme que o perfil existe com **Email Subscribe** definido como **Opted In** e que quaisquer atributos personalizados, inscrição em grupo de inscrições ou alias de usuário que você configurou aparecem conforme esperado.

### Etapa 4: Ativar a ação para tráfego ao vivo {#step-4-enable-the-action-for-live-traffic}

Quando o perfil de teste estiver correto na Braze, retorne à Talkable e ative a ação **Email opt-in**.

A partir desse ponto, cada evento de opt-in da Talkable sincroniza o perfil correspondente para a Braze em tempo real.

## Atributos de usuário padrão enviados para a Braze {#default-user-attributes-sent-to-braze}

Em cada evento de opt-in, a Talkable cria ou atualiza o perfil de usuário correspondente na Braze com os seguintes atributos de usuário padrão da Braze. Valores vazios são omitidos.

| Atributo da Braze | Tipo | Observações |
| --- | --- | --- |
| `email_subscribe` | String | Definido como **Opted In** em cada evento de opt-in da Talkable. |
| `email` | String | Identificador principal usado para corresponder ao perfil da Braze. |
| `phone` | String | Capturado apenas como atributo de usuário. A Braze espera o formato E.164; enviado conforme armazenado na Talkable. |
| `first_name` | String | O nome da pessoa. |
| `last_name` | String | O sobrenome da pessoa. |
| Inscrição em grupo de inscrições | Não aplicável | Adicionado apenas quando um grupo de inscrições está configurado. O usuário é inscrito como subscribed. |
| Alias de usuário | Não aplicável | Adicionado apenas quando um alias de usuário está configurado. Para saber mais, consulte [Personalizar a Talkable](#customizing-talkable). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atributos de usuário padrão enviados para a Braze" }

## Personalizar a Talkable {#customize-talkable}

As seguintes personalizações opcionais estão disponíveis. Configure qualquer combinação; elas são independentes.

### Inscrever opt-ins em um grupo de inscrições da Braze {#enroll-opt-ins-in-a-braze-subscription-group}

1. Na Braze, copie um ID de grupo de inscrições em **Audience** > **Subscription Group Management**. Para saber mais, consulte [Gerenciando inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/).
2. Na ação **Email opt-in** da Talkable, cole-o no campo **Subscription group identifier**.

A Talkable inscreve cada opt-in nesse grupo de inscrições como subscribed, direcionando os opt-ins de indicação para esse grupo em vez de uma inscrição global. A Talkable apenas adiciona inscrições; nunca as remove.

### Enviar atributos personalizados {#send-custom-attributes}

Adicione qualquer par chave-valor no editor de carga útil da ação. A chave que você inserir se torna o nome do atributo no perfil de usuário da Braze.

Os valores são modelados com Liquid. As seguintes variáveis estão disponíveis:

{% raw %}
| Variável | Conteúdo |
| --- | --- |
| `{{ person }}` | O promotor ou amigo que fez opt-in (`email`, `first_name`, `last_name`, `phone_number`, `username`, `is_advocate`, `custom_properties` e mais). |
| `{{ ip }}` | O endereço IP de onde o opt-in ocorreu. |
| `{{ campaign }}` | A campanha de indicação da Talkable de origem (`name`, `type`, `tag_names` e mais). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variáveis de template Liquid" }
{% endraw %}

{% raw %}
Exemplo: adicione `talkable_is_advocate` = `{{ person.is_advocate }}` e `talkable_campaign_name` = `{{ campaign.name }}` para segmentar por contexto de indicação na Braze.
{% endraw %}

### Identificar usuários com aliases de usuário da Braze {#identify-users-with-braze-user-aliases}

No editor de carga útil, adicione `user_alias.alias_name` (por exemplo, {% raw %}`{{ person.username }}`{% endraw %}) e `user_alias.alias_label` (por exemplo, `username`). Para saber mais, consulte [Objeto de alias de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/).

Quando ambos os campos estão presentes, o sistema identifica o usuário pelo alias além do e-mail, e a Braze cria um novo perfil com alias se nenhuma correspondência existir.

{% alert note %}
Ambos os campos de alias são obrigatórios. Se apenas um dos campos `alias_name` ou `alias_label` estiver preenchido, a Talkable não envia um alias de usuário e o perfil é correspondido apenas por e-mail.
{% endalert %}

## Encontrar e criar usuários na Braze {#find-and-create-users-in-braze}

* Por padrão, a Braze corresponde o perfil pelo endereço de e-mail. Se nenhum perfil correspondente existir, a Braze cria um novo.
* Quando um alias de usuário está configurado, a Braze também corresponde por esse alias e cria um novo perfil com alias se nenhuma correspondência existir.
* IDs externos não são usados por esta integração. Para vincular opt-ins da Talkable a um perfil existente identificado externamente, configure um alias de usuário cujo rótulo corresponda ao alias conhecido desse perfil.

## Usar a Talkable com a Braze {#use-talkable-with-braze}

### Encontrar um usuário sincronizado {#find-a-synced-user}

Acesse **Audience** > **User Search** e pesquise por e-mail para visualizar um perfil que a Talkable criou ou atualizou.

Campos padrão (e-mail, telefone, nome ou sobrenome) e quaisquer atributos personalizados que você configurou aparecem no perfil; **Email Subscribe** mostra **Opted In**.

### Criar um segmento de indicação {#build-a-referral-segment}

1. Crie um segmento filtrado por **Email Subscribe** igual a **Opted In**.
2. Refine com os atributos personalizados que a Talkable envia — por exemplo, `talkable_is_advocate` igual a `true` para segmentar promotores, ou `talkable_campaign_name` igual à sua campanha para segmentar um programa de indicação específico.

### Acionar envio de mensagens de ciclo de vida {#trigger-lifecycle-messaging}

1. Crie um Canvas ou uma Campaign com entrega baseada em ação. Os seguintes tipos de gatilho da Braze funcionam com esta integração:
* **Update Subscription Status** (por exemplo, a inscrição de e-mail se torna **Opted In**)
* **Update Subscription Group Status** (quando um grupo de inscrições está configurado)
* **Change Custom Attribute Value** (para qualquer atributo personalizado da Talkable que você enviar).
2. Personalize mensagens com os atributos personalizados da Talkable no perfil (nome da campanha, valor da recompensa, indicador e assim por diante).

## Considerações {#considerations}

* **Apenas opt-in de e-mail:** Números de telefone são capturados como atributo de usuário padrão, mas a integração não define um estado de inscrição de SMS. A Talkable não sincroniza opt-ins de SMS.
* **Formato de telefone:** A Braze espera números de telefone no formato internacional (E.164).
* **Sincronização em tempo real, orientada por eventos:** A Talkable envia uma solicitação por evento de opt-in (um usuário por solicitação). Não há agrupamento em lote nem sincronização periódica completa; o volume acompanha o volume de opt-ins de indicação.
* **Entrega confiável:** Se a Braze retornar temporariamente um erro, a Talkable faz novas tentativas automaticamente. Falhas persistentes enviam um alerta por e-mail ao administrador do site.

## Solução de problemas {#troubleshooting}

| Erro | Causa provável | Correção |
| --- | --- | --- |
| 401 Unauthorized | A chave da API REST não possui as permissões `users.track`, ou o endpoint aponta para o cluster errado. | Emita novamente a chave com as permissões `users.track` e confirme que o endpoint REST corresponde ao seu cluster da Braze. |
| Endpoint REST rejeitado na instalação | A URL não é um endpoint REST da Braze. | Use o endpoint REST do seu cluster, por exemplo `https://rest.iad-01.braze.com`. Uma URL do dashboard não funciona. |
| Perfil criado mas não está em um grupo de inscrições | Nenhum ID de grupo de inscrições configurado. | Insira o ID do grupo de inscrições na ação **Email opt-in**. |
| Alias de usuário não aplicado | Apenas um dos dois campos de alias (nome ou rótulo) está preenchido. | Insira ambos os campos na ação: nome do alias e rótulo do alias. |
| Perfil não aparece | Solicitação de exemplo ainda não enviada, ou a ação está desativada. | Selecione **Send sample payload** na Talkable e certifique-se de que a ação **Email opt-in** está ativada. |
| Solicitações pararam de ser enviadas após rotação de chave | A chave de API armazenada foi revogada ou substituída na Braze. | Na **App Store** da Talkable, abra o app da Braze, cole a nova chave da API REST e selecione **Save**; teste novamente com **Send sample payload**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Solução de problemas" }

Para saber mais sobre a integração da Talkable, consulte a [documentação de integração Talkable Braze](https://docs.talkable.com/email_marketing_and_automation/braze/). Para entrar em contato com o suporte da Talkable, envie um e-mail para [support@talkable.com](mailto:support@talkable.com).