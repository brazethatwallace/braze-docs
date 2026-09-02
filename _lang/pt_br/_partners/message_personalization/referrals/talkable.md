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

O Talkable traz a aquisição liderada por defensores para a jornada do cliente que a Braze impulsiona. A integração transfere em tempo real cada aceitação de indicação capturada pelo Talkable para o perfil correspondente na Braze, para que fluxos de boas-vindas, jornadas de indicação, segmentação e envio de mensagens de ciclo de vida possam ser iniciados a partir de consentimento confiável e contexto de indicação — tudo sem exportações manuais de listas ou sincronizações em lote.

O Talkable captura aceitações de marketing em dois cenários:

* **Inscrição do defensor:** Um defensor se inscreve em uma Campaign de indicação do Talkable e consente em receber e-mails de marketing.
* **Coleta de e-mail do amigo:** Um amigo conclui a etapa de coleta de e-mail do Talkable e aceita receber e-mails de marketing.

Em ambos os casos, o Talkable cria ou atualiza o perfil de usuário correspondente na Braze em tempo real e define o status de inscrição de e-mail do usuário como **Opted In**.

### Comportamento padrão {#default-behavior}

O Talkable envia dados para a Braze apenas em um evento discreto de aceitação de alguém que consentiu explicitamente no Talkable — seja um defensor se inscrevendo em uma Campaign ou um amigo aceitando durante a coleta de e-mail. O Talkable não executa lotes noturnos, sincronizações completas ou atualizações implícitas de perfil. O Talkable nunca envia perfis que não tenham feito a aceitação para a Braze.

## Casos de uso {#use-cases}

- Disparar um Canvas de boas-vindas na Braze no momento em que um defensor se inscreve em uma campanha de indicação da Talkable.
- Ativar amigos indicados com um Canvas específico para amigos e uma oferta personalizada de primeira compra assim que um amigo aceitar participar.
- Segmentar por contexto de indicação usando sinalizadores de defensor e amigo e metadados de campanha enviados como atributos personalizados da Braze.
- Direcionar aceitações de indicação para um grupo de inscrições designado na Braze para envio de newsletters em conformidade.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa do seguinte:

| Pré-requisito | Descrição |
| --- | --- |
| Uma conta Talkable | É necessário um site Talkable com pelo menos uma campanha configurada para aproveitar esta parceria. |
| Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.track`. Crie essa chave no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. Para saber mais, consulte [Criando chaves da API or interface de programação do aplicativo (API) REST or transferir estado representacional]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| Um endpoint REST or transferir estado representacional da Braze | A URL do seu endpoint REST or transferir estado representacional da Braze (por exemplo, `https://rest.iad-01.braze.com`). Os clusters da Braze nos EUA (`.com`) e na UE (`.eu`) são compatíveis. Para saber mais, consulte [Endpoints da REST or transferir estado representacional API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Instalar o app da Braze no Talkable {#step-1-install-the-braze-app-in-talkable}

1. Faça login no painel de administração do Talkable e abra o menu, depois acesse **All Site Settings** > **App Store**.
2. Localize **Braze** e selecione **Install**.
3. Insira seu endpoint REST or transferir estado representacional da Braze e uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional com permissões `users.track`, e selecione **Save**.

### Etapa 2: Configurar a ação de aceitação de e-mail {#step-2-configure-the-email-opt-in-action}

1. No app da Braze no Talkable, abra a ação **Email opt-in**.
2. (Opcional) Insira um identificador de grupo de inscrições da Braze, adicione atributos personalizados e/ou configure um alias de usuário. Para saber mais, consulte [Personalizando o Talkable](#customizing-talkable).
3. Selecione **Save**. Deixe a ação desativada para que você possa verificar a configuração com uma carga útil de teste antes que qualquer evento ativo de aceitação de e-mail comece a sincronizar.

### Etapa 3: Testar com uma carga útil de exemplo {#step-3-test-with-a-sample-payload}

1. No Talkable, selecione **Send sample payload** na ação **Email opt-in** para enviar uma requisição de teste para a Braze.
2. Na Braze, acesse **Audience** > **User Search** e pesquise pelo endereço de e-mail de teste.
3. Confirme que o perfil existe com **Email Subscribe** definido como **Opted In** e que quaisquer atributos personalizados, inscrição em grupo de inscrições ou alias de usuário que você configurou aparecem conforme esperado.

### Etapa 4: Ativar a ação para tráfego em tempo real {#step-4-enable-the-action-for-live-traffic}

Quando o perfil de teste estiver correto na Braze, volte ao Talkable e ative a ação **Email opt-in**.

A partir desse ponto, cada evento de aceitação do Talkable sincroniza o perfil correspondente com a Braze em tempo real.

## Atributos de usuário padrão enviados para a Braze {#default-user-attributes-sent-to-braze}

A cada evento de aceitação, o Talkable cria ou atualiza o perfil de usuário correspondente na Braze com os seguintes atributos de usuário padrão da Braze. Valores vazios são omitidos.

| Atributo da Braze | Tipo | Notas |
| --- | --- | --- |
| `email_subscribe` | String | Definido como **Opted In** a cada evento de aceitação do Talkable. |
| `email` | String | Identificador principal usado para corresponder ao perfil da Braze. |
| `phone` | String | Capturado apenas como atributo de usuário. A Braze espera o formato E.164; enviado conforme armazenado no Talkable. |
| `first_name` | String | O nome da pessoa. |
| `last_name` | String | O sobrenome da pessoa. |
| Inscrição em grupo de inscrições | Não aplicável | O Talkable inscreve o usuário como inscrito quando um grupo de inscrições está configurado. |
| Alias de usuário | Não aplicável | Adicionado apenas quando um alias de usuário está configurado. Para saber mais, consulte [Personalizando o Talkable](#customizing-talkable). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atributos de usuário padrão enviados para a Braze" }

## Personalizar o Talkable {#customize-talkable}

As seguintes personalizações opcionais estão disponíveis. Configure qualquer combinação; elas são independentes.

### Inscrever aceitações em um grupo de inscrições da Braze {#enroll-opt-ins-in-a-braze-subscription-group}

1. Na Braze, copie um ID de grupo de inscrições em **Audience** > **Subscription Group Management**. Para saber mais, consulte [Gerenciamento de inscrições de usuários]({{site.baseurl}}/user_guide/channels/email/subscriptions).
2. Na ação **Email opt-in** do Talkable, cole-o no campo **Subscription group identifier**.

O Talkable inscreve cada aceitação nesse grupo de inscrições como inscrito, limitando as aceitações de indicação a esse grupo em vez de uma inscrição global. O Talkable apenas adiciona inscrições; nunca as remove.

### Enviar atributos personalizados {#send-custom-attributes}

Adicione qualquer par chave-valor ao editor de carga útil da ação. A chave inserida se torna o nome do atributo no perfil de usuário da Braze.

Os valores utilizam templates Liquid. As seguintes variáveis estão disponíveis:

{% raw %}
| Variável | Conteúdo |
| --- | --- |
| `{{ person }}` | O promotor ou amigo que fez a aceitação (`email`, `first_name`, `last_name`, `phone_number`, `username`, `is_advocate`, `custom_properties` e mais). |
| `{{ ip }}` | O endereço IP de onde a aceitação ocorreu. |
| `{{ campaign }}` | A Campaign de origem do Talkable (`name`, `type`, `tag_names` e mais). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variáveis de template Liquid" }
{% endraw %}

{% raw %}
Exemplo: adicione `talkable_is_advocate` = `{{ person.is_advocate }}` e `talkable_campaign_name` = `{{ campaign.name }}` para segmentar por contexto de indicação na Braze.
{% endraw %}

### Identificar usuários com aliases de usuário da Braze {#identify-users-with-braze-user-aliases}

No editor de carga útil, adicione `user_alias.alias_name` (por exemplo, {% raw %}`{{ person.username }}`{% endraw %}) e `user_alias.alias_label` (por exemplo, `username`). Para saber mais, consulte [Objeto de alias de usuário]({{site.baseurl}}/api/objects_filters/user_alias_object).

Quando ambos os campos estão presentes, o sistema identifica o usuário pelo alias além do e-mail, e a Braze cria um novo perfil com alias caso nenhuma correspondência exista.

{% alert note %}
Ambos os campos de alias são obrigatórios. Se apenas um dos campos `alias_name` ou `alias_label` estiver definido, o Talkable não envia um alias de usuário e o perfil é correspondido apenas por e-mail.
{% endalert %}

## Encontrar e criar usuários na Braze {#find-and-create-users-in-braze}

* Por padrão, a Braze faz a correspondência do perfil pelo endereço de e-mail. Se não existir um perfil correspondente, a Braze cria um novo.
* Quando um alias de usuário é configurado, a Braze também faz a correspondência por esse alias e cria um novo perfil com alias caso não haja correspondência.
* IDs externos não são usados por essa integração. Para vincular as aceitações do Talkable a um perfil existente identificado externamente, configure um alias de usuário cujo rótulo corresponda ao alias conhecido desse perfil.

## Usar o Talkable com a Braze {#use-talkable-with-braze}

### Encontrar um usuário sincronizado {#find-a-synced-user}

Acesse **Audience** > **User Search** e pesquise por e-mail para visualizar um perfil que o Talkable criou ou atualizou.

Os campos padrão (e-mail, telefone, nome ou sobrenome) e quaisquer atributos personalizados que você configurou aparecem no perfil; **Email Subscribe** mostra **Opted In**.

### Criar um Segment or segmento de indicação {#build-a-referral-segment}

1. Crie um Segment or segmento filtrado em **Email Subscribe** como **Opted In**.
2. Refine com os atributos personalizados que o Talkable envia — por exemplo, `talkable_is_advocate` igual a `true` para segmentar defensores da marca, ou `talkable_campaign_name` igual à sua Campaign para segmentar um programa de indicação específico.

### Disparar envio de mensagens de ciclo de vida {#trigger-lifecycle-messaging}

1. Crie um Canvas ou uma Campaign com entrega baseada em ação. Os seguintes tipos de disparo da Braze funcionam com essa integração:
* **Update Subscription Status** (por exemplo, a inscrição de e-mail passa para **Opted In**)
* **Update Subscription Group Status** (quando um grupo de inscrições é configurado)
* **Change Custom Attribute Value** (para qualquer atributo personalizado do Talkable que você enviar).
2. Personalize as mensagens com os atributos personalizados do Talkable no perfil (nome da Campaign, valor da recompensa, pessoa que indicou, entre outros).

## Considerações {#considerations}

* **Aceitação apenas por e-mail:** os números de telefone são capturados como um atributo de usuário padrão, mas a integração não define um status de inscrição de SMS. O Talkable não sincroniza aceitações de SMS.
* **Formato de telefone:** a Braze espera números de telefone no formato internacional (E.164).
* **Sincronização em tempo real baseada em eventos:** o Talkable envia uma solicitação por evento de aceitação (um usuário por solicitação). Não há agrupamento em lote nem sincronização completa periódica; o volume acompanha o volume de aceitações de indicação.
* **Entrega confiável:** se a Braze retornar temporariamente um erro, o Talkable faz novas tentativas automaticamente. Falhas persistentes enviam um alerta por e-mail para o administrador do site.

## Solução de problemas {#troubleshooting}

| Erro | Causa provável | Correção |
| --- | --- | --- |
| 401 Unauthorized | A chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional não tem as permissões `users.track`, ou o endpoint aponta para o cluster errado. | Gere novamente a chave com as permissões `users.track` e confirme se o endpoint REST or transferir estado representacional corresponde ao seu cluster da Braze. |
| Endpoint REST or transferir estado representacional rejeitado na instalação | A URL não é um endpoint REST or transferir estado representacional da Braze. | Use o endpoint REST or transferir estado representacional do seu cluster, por exemplo `https://rest.iad-01.braze.com`. Uma URL do dashboard não funciona. |
| Perfil criado, mas não está em um grupo de inscrições | Nenhum ID do grupo de inscrições configurado. | Insira o ID do grupo de inscrições na ação **Email opt-in**. |
| Alias de usuário não aplicado | Apenas um dos dois campos de alias (nome ou rótulo) está preenchido. | Preencha ambos os campos na ação: nome do alias e rótulo do alias. |
| Perfil não aparece | A solicitação de amostra ainda não foi enviada ou a ação está desativada. | Selecione **Send sample payload** no Talkable e verifique se a ação **Email opt-in** está ativada. |
| As solicitações pararam de ser enviadas após uma rotação de chave | A chave de API or interface de programação do aplicativo (API) armazenada foi revogada ou substituída na Braze. | Na **App Store** do Talkable, abra o app da Braze, cole a nova chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional e selecione **Save**; teste novamente com **Send sample payload**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Solução de problemas" }

Para saber mais sobre a integração com o Talkable, consulte a [documentação de integração Talkable Braze](https://docs.talkable.com/email_marketing_and_automation/braze/). Para entrar em contato com o suporte do Talkable, envie um e-mail para [support@talkable.com](mailto:support@talkable.com).