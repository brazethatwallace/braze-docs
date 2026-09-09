---
nav_title: Seu público
article_title: Seu público na Braze
page_order: 0
page_type: reference
description: "Saiba como a Braze define e gerencia seus usuários, identifica usuários e utiliza dados de usuários para impulsionar segmentação, personalização e envio de mensagens em todos os canais."

---

# Seu público na Braze {#your-braze-audience}

> Saiba como a Braze define e gerencia seus usuários, identifica usuários e utiliza dados de usuários para impulsionar segmentação, personalização e envio de mensagens em todos os canais.

Na Braze, um usuário (e seu perfil de usuário) representa uma pessoa individual para quem você pode enviar mensagens e analisar.

## Perfis de usuário {#user-profiles}

Um [perfil de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) funciona como uma fonte única de verdade para tudo que a Braze sabe sobre essa pessoa, incluindo:

- Identificadores (como IDs de usuário ou IDs externos)
- Dispositivos e canais de envio de mensagens
- Dados comportamentais e eventos
- Atributos e preferências
- Histórico de engajamento com mensagem

Um único perfil de usuário pode ser associado a vários dispositivos e canais, permitindo que você entenda e envie mensagens para alguém de forma integrada em todas as plataformas.

## Usuários anônimos e usuários identificados {#anonymous-users-and-identified-users}

Os usuários na Braze geralmente se enquadram em um de dois estados.

### Usuários anônimos {#anonymous-users}

Um [usuário anônimo]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) é alguém que interagiu com o seu app ou website, mas ainda não recebeu um identificador do seu sistema (como um `external_id`).

- Usuários anônimos são criados automaticamente quando o SDK da Braze é inicializado
- Você ainda pode rastrear eventos, atributos e engajamento com mensagem
- Esses usuários podem receber mensagens, dependendo do canal e do status de aceitação

#### Usuários anônimos e consentimento {#anonymous-users-and-consent}

Se você precisar encapsular o SDK da Braze em um wrapper de consentimento para cumprir suas políticas de consentimento, é possível coletar dados anônimos antes que os usuários concedam o consentimento. Quando o SDK é inicializado, um perfil de usuário anônimo é criado, permitindo que você rastreie o comportamento enquanto respeita os requisitos de consentimento.

**Envio de mensagens para usuários anônimos:**
Usuários anônimos podem disparar e receber mensagens enquanto o SDK da Braze permanecer inicializado. Isso inclui:

- [In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [Notificações por push]({{site.baseurl}}/user_guide/channels/push) (se os tokens por push estiverem registrados)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)

No entanto, se você desativar ou impedir a inicialização do SDK quando um usuário não concede ou retira o consentimento, os canais disparados pelo SDK não funcionam para esse usuário.

**Direcionamento de usuários com base no status de consentimento:**
Para enviar mensagens a usuários com base no status de consentimento deles, defina um atributo de usuário personalizado (como `has_marketing_consent`) no perfil. Você pode então criar Segments com base nesse atributo e manter esse valor sincronizado caso os usuários alterem suas preferências de consentimento fora da Braze. Para saber mais sobre o direcionamento de usuários anônimos, consulte [Casos de uso]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#use-cases).

### Usuários identificados {#identified-users}

Um [usuário identificado]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#identified-user-profiles) é aquele que foi associado a um `external_id` fornecido por você (por exemplo, um ID de cliente ou ID de conta).

Identificar um usuário permite que você:

- Unifique a atividade entre dispositivos e sessões
- Envie mensagens de forma consistente entre canais
- Segmente e personalize usando dados de usuário de longo prazo
- Gerencie perfis por meio de APIs e integrações

Quando um usuário anônimo é identificado posteriormente, a Braze mescla os dados elegíveis no perfil identificado de acordo com [este comportamento de mesclagem]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior). Por exemplo, tokens por push e histórico de mensagens são transferidos, e muitos campos do perfil anônimo são mesclados apenas quando ainda não estão definidos no perfil identificado. Quando há conflito de valores, o perfil identificado é mantido.

## Envie mensagens aos usuários por meio de canais {#message-users-through-channels}

Um [canal]({{site.baseurl}}/user_guide/channels) é uma forma específica pela qual a Braze pode entregar uma mensagem a um usuário. Os canais mais comuns incluem:

- [Push (web ou mobile)]({{site.baseurl}}/user_guide/channels/push)
- [E-mail]({{site.baseurl}}/user_guide/channels/email)
- [SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
- [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp)
- [Mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages)
- [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
- [Banners]({{site.baseurl}}/user_guide/channels/banners)
- [LINE]({{site.baseurl}}/user_guide/channels/line)
- [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks)

Um único perfil de usuário pode ter vários canais vinculados, como um endereço de e-mail e um dispositivo móvel ao mesmo tempo. A Braze usa esse modelo para coordenar o envio de mensagens entre canais, mantendo uma visão unificada do usuário.

Cada canal tem suas próprias regras de entrega, requisitos de aceitação e metadados, mas todos estão associados ao mesmo perfil de usuário.

## Formas como os usuários entram na Braze {#ways-users-enter-braze}

Os usuários são criados na Braze sempre que alguém interage com a sua marca por meio de uma integração ou canal compatível. A forma como eles são adicionados depende de como você implementou a Braze.

{% tabs %}
{% tab Apps móveis %}
- Quando um usuário abre seu app pela primeira vez, o SDK da Braze cria um perfil de usuário.
- Dispositivos e tokens por push são registrados automaticamente.
- Eventos e atributos podem ser registrados imediatamente.
{% endtab %}

{% tab Web %}
- Os usuários são criados quando o SDK web é inicializado.
- As inscrições de web push registram um navegador como canal de envio de mensagens.
{% endtab %}

{% tab E-mail e SMS %}
- Os usuários podem ser criados quando você faz upload de dados, chama APIs ou coleta aceitações.
- Endereços de e-mail e números de telefone são armazenados como identificadores de canal.
- O status de aceitação é rastreado por canal e por região.
{% endtab %}

{% tab APIs e integrações %}
- Você pode criar ou atualizar usuários diretamente por meio de [REST APIs]({{site.baseurl}}/api/endpoints/user_data) ou [importando um CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import).
- Ferramentas externas (como CDPs, CRMs ou data warehouses) podem sincronizar usuários na Braze automaticamente.
{% endtab %}
{% endtabs %}

## Fontes de dados de público {#audience-data-sources}

Os dados de usuários na Braze geralmente vêm de uma combinação de fontes.

{% tabs %}
{% tab Coleta automática %}
Os SDKs da Braze coletam automaticamente dados contextuais, como:

- Tipo de dispositivo e sistema operacional
- Idioma e fuso horário
- Versão do app e atividade de sessão
{% endtab %}

{% tab Comportamento do usuário %}
Quando os usuários interagem com seu app ou mensagens, a Braze registra:

- [Eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) (por exemplo, compras ou uso de recursos)
- Aberturas, cliques e conversões de mensagens
- Atividade de sessão e tendências de engajamento
{% endtab %}

{% tab Seus sistemas %}
Você pode enviar dados das suas próprias ferramentas para a Braze usando:

- [REST APIs]({{site.baseurl}}/api/endpoints/user_data)
- [Uploads de CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)
- Sincronizações de dados agendadas

Isso geralmente inclui identificadores, dados de conta ou contexto histórico.
{% endtab %}
{% endtabs %}

### Dados fornecidos pelo usuário {#user-provided-input}

Os usuários podem fornecer dados diretamente por meio de:

- [Centrais de Preferências]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)
- Formulários ou pesquisas (SDKs ou integrações)
- Experiências no app

### Integrações {#integrations}

A Braze se integra com plataformas como [Segment]({{site.baseurl}}/partners/segment), data warehouses e parceiros de tecnologia de análise de dados por meio de integrações, permitindo que os dados de usuários fluam automaticamente para os perfis de usuário.

## Gerenciar dados de usuários {#manage-user-data}

Você pode adicionar, atualizar ou remover dados de usuários de várias maneiras:

- **Ferramentas do dashboard** para edições manuais ou uploads de CSV
- **APIs** para atualizações em tempo real ou programáticas
- **SDKs** para capturar comportamentos diretamente no seu app ou site
- **Integrações** para sincronização contínua

Os dados podem ser removidos ao:

- Limpar valores de atributos
- Remover tags
- Atualizar status de inscrição
- Redefinir usuários no logout (para casos de uso com usuários anônimos)

## Recursos de dados de público {#audience-data-features}

Assim que os dados de usuários estão na Braze, eles potencializam praticamente todos os recursos de engajamento. Quanto mais completos e precisos forem seus dados de usuários, mais efetivamente você poderá usar os seguintes recursos.

| Recurso | Descrição |
| ---- | ---- |
| [Segmentação]({{site.baseurl}}/user_guide/audience/segments) | Crie públicos com base em: {::nomarkdown}<ul><li>Atributos e campos personalizados</li> <li>Eventos e comportamentos</li> <li>Engajamento com mensagem</li> <li>Propriedades de dispositivo e canal</li></ul>{:/} <br>Os Segments podem ser reutilizados em Campaigns e Canvas. |
| [Personalização]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize) | Use dados de usuários para personalizar o conteúdo, como: {::nomarkdown}<ul><li>Nomes e preferências no corpo da mensagem</li> <li>Recomendações dinâmicas</li> <li>Conteúdo específico por local ou idioma</li></ul>{:/} |
| Automação e orquestração | Dispare mensagens e jornadas com base em: {::nomarkdown}<ul><li>Ações do usuário</li> <li>Alterações de atributos</li> <li>Condições baseadas em tempo</li></ul>{:/} |
| Coordenação entre canais | Alcance usuários no canal mais apropriado, respeitando: {::nomarkdown}<ul><li>Status de aceitação</li> <li>Limites de frequência</li> <li>Preferências de canal</li></ul>{:/} |
| [Análise de dados e insights]({{site.baseurl}}/user_guide/analytics) | Entenda como diferentes públicos se comportam analisando: {::nomarkdown}<ul><li>Taxas de engajamento</li> <li>Jornadas de conversão</li> <li>Desempenho de Segments ao longo do tempo</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recursos de dados de público" }