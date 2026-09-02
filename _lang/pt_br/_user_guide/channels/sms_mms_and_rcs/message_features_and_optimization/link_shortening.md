---
nav_title: Encurtamento de links
article_title: Encurtamento de links
page_order: 1
description: "Este artigo de referência aborda como ativar o encurtamento de links nas suas mensagens SMS e algumas perguntas frequentes."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Encurtamento de links {#link-shortening}

> Esta página aborda como ativar o encurtamento de links nas suas mensagens SMS e RCS, testar links encurtados, usar seu domínio personalizado em links encurtados e mais.

{% alert important %}
A Braze está implementando gradualmente o [encurtamento de links unificado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening?sdktab=unified), que consolida todos os links encurtados de SMS e RCS em um único formato de link personalizado (por exemplo, `brz.ai/abcdefgh`).
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

O encurtamento de links e o rastreamento de cliques permitem encurtar automaticamente URLs contidas em mensagens SMS ou RCS e coletar análises de taxa de cliques, fornecendo métricas de engajamento adicionais para ajudar a entender como os usuários estão interagindo com suas Campaigns.

O encurtamento de links e o rastreamento de cliques podem ser ativados no [nível da variante de mensagem]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-1-create-your-campaign) tanto em Campaigns quanto em Canvas.

{% multi_lang_include channels/sms/rcs_link_shortening_note.md %}

O comprimento da URL é determinado pelo tipo de rastreamento ativado:
- **Rastreamento básico** ativa o rastreamento de cliques no nível da Campaign. URLs estáticas têm um comprimento de 20 caracteres, e URLs personalizadas têm um comprimento de 25 caracteres.
- **Rastreamento avançado** ativa o rastreamento de cliques no nível da Campaign e do usuário, além de permitir o uso de recursos de segmentação e redirecionamento que dependem de cliques. Os cliques também geram um [evento de clique de SMS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) enviado pelo Currents. URLs estáticas com rastreamento avançado têm um comprimento de 27-28 caracteres, permitindo criar segmentos de usuários que clicaram em URLs. URLs personalizadas têm um comprimento de 32-33 caracteres.

Os links são encurtados usando nosso domínio curto compartilhado (`brz.ai`) ou seu domínio personalizado de encurtamento de links. Um exemplo de URL pode ser algo como: `https://brz.ai/8jshX` (básico, estático) ou `https://brz.ai/p/8jshX/2dj8d` (avançado, personalizado). Consulte [Testes](#legacy_testing) para saber mais.

Quaisquer URLs estáticas que comecem com `http://` ou `https://` são encurtadas. URLs estáticas encurtadas são válidas por um ano a partir da data de criação. URLs encurtadas que contêm personalização Liquid são válidas por dois meses.

{% alert note %}
Os links encurtados da Braze sempre incluem o protocolo `https://` e não podem ser configurados para usar um protocolo diferente.
{% endalert %}

## Usando o encurtamento de links {#using-link-shortening}

Para usar o encurtamento de links, verifique se o botão de encurtamento de links no criador de mensagem está ativado. Em seguida, escolha usar rastreamento básico ou avançado.

![Criador de mensagem com um botão de alternância para encurtamento de links.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening1.png %}){: width="1614" height="994"}

A Braze reconhece apenas URLs que começam com `http://` ou `https://`. Quando uma URL é reconhecida, a seção **Prévia** é atualizada com uma URL de espaço reservado. A Braze estima o comprimento da URL após o encurtamento, mas um aviso solicita que você selecione um usuário teste e salve a mensagem como rascunho para uma estimativa mais precisa.

![Criador de mensagem com uma URL longa na caixa "Mensagem" e um link encurtado gerado na prévia.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening3.png %}){: width="1569" height="516"}

{% alert note %}
Se você planeja usar o [filtro de canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) do BrazeAI<sup>TM</sup> e deseja que os canais SMS e RCS sejam selecionáveis, ative o encurtamento de links com rastreamento avançado.
{% endalert %}

### Adicionando parâmetros UTM {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personalização Liquid em URLs {#liquid-personalization-in-urls}

Você pode construir dinamicamente sua URL diretamente no criador da Braze, permitindo adicionar parâmetros UTM dinâmicos às suas URLs ou enviar links exclusivos aos usuários (como direcionar usuários ao carrinho abandonado ou a um produto específico que voltou ao estoque).

### Criar uma URL com tags de personalização Liquid compatíveis {#create-a-url-with-supported-liquid-personalization-tags}

As URLs podem ser geradas dinamicamente por meio do uso de quaisquer [tags de personalização Liquid compatíveis]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

A Braze também oferece suporte ao encurtamento de variáveis Liquid definidas de forma personalizada, como nos exemplos a seguir:

### Criar uma URL usando variáveis Liquid {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Encurtar URLs renderizadas por variáveis Liquid {#shorten-urls-rendered-by-liquid-variables}

**Canais compatíveis:** KakaoTalk, LINE, SMS, RCS, WhatsApp

A Braze encurta URLs renderizadas por Liquid, incluindo aquelas incluídas em propriedades de disparo de API or interface de programação do aplicativo (API). Por exemplo, se {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} representa uma URL válida, a Braze encurta e rastreia essa URL antes de enviar a mensagem.

### Encurtar URLs no endpoint `/messages/send` {#shorten-urls-in-messagessend-endpoint}

O encurtamento de links também é ativado para mensagens somente via API or interface de programação do aplicativo (API) por meio do [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages). Para também ativar o rastreamento básico ou avançado, use os parâmetros de solicitação `link_shortening_enabled` ou `user_click_tracking_enabled`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | Opcional | Booleano | Defina `link_shortening_enabled` como `true` para ativar o encurtamento de links e o rastreamento de cliques no nível da Campaign. Para usar o rastreamento, um `campaign_id` e um `message_variation_id` devem estar presentes. |
| `user_click_tracking_enabled` | Opcional | Booleano | Defina `user_click_tracking_enabled` como `true` para ativar o encurtamento de links e o rastreamento de cliques no nível da Campaign e do usuário. Você pode usar os dados rastreados para criar segmentos de usuários que clicaram em URLs.<br><br> Para usar este parâmetro, `link_shortening_enabled` deve ser `true`, e um `campaign_id` e um `message_variation_id` devem estar presentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Encurtar URLs no endpoint /messages/send" }

Para uma lista completa de parâmetros de solicitação, acesse [parâmetros de solicitação]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters).

## Testes {#testing}

Antes de lançar sua Campaign ou Canvas, é uma prática recomendada pré-visualizar e testar sua mensagem primeiro. Para isso, acesse a guia **Teste** para pré-visualizar e enviar uma mensagem SMS ou RCS para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou para um usuário individual.

Essa prévia é atualizada com a personalização relevante e a URL encurtada. O número de caracteres e os [segmentos faturáveis]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) também são atualizados para refletir a personalização renderizada e a URL encurtada.

Certifique-se de salvar a Campaign ou o Canvas antes de enviar uma mensagem de teste para receber uma representação da URL encurtada que é enviada na sua mensagem. Se a Campaign ou o Canvas não for salvo antes de um envio de teste, o envio de teste incluirá uma URL de espaço reservado.

Para que os Canvas apareçam no filtro "Clicou no link encurtado de SMS", a etapa do Canvas que contém o link encurtado também deve estar ativada com rastreamento avançado, que permite o rastreamento de cliques no nível do usuário. Se o link encurtado estiver configurado com rastreamento básico, a opção de filtrar eventos de clique em links encurtados de SMS não estará disponível. O mesmo requisito de rastreamento avançado se aplica quando você configura a entrada do Canvas ou jornadas de ação que dependem de links encurtados de SMS clicados.

{% alert important %}
Se um rascunho for criado dentro de um Canvas ativo, uma URL encurtada não será gerada. A URL encurtada real é gerada quando o rascunho do Canvas é ativado.
{% endalert %}

![Guia "Teste" da mensagem com campos para selecionar destinatários de teste.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening2.png %}){: width="1569" height="947"}

{% alert note %}
A personalização Liquid e as URLs encurtadas são modeladas na guia **Teste** após a seleção de um usuário. Certifique-se de que um usuário esteja selecionado para receber uma contagem precisa de caracteres.
{% endalert %}

## Rastreamento de cliques {#click-tracking}

Quando o encurtamento de links está ativado, a tabela **Desempenho de SMS/MMS/RCS** inclui uma coluna intitulada **Total de cliques** que mostra uma contagem de eventos de clique por variante e uma taxa de cliques associada. **Total de cliques** exclui cliques suspeitos de bots das contagens do dashboard. Para saber mais sobre métricas, consulte [Desempenho da mensagem]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting) e [Filtragem de cliques de bots]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering).

![Tabela de métricas de desempenho de SMS e MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %}){: width="1586" height="191"}

As tabelas **Desempenho histórico** e **Desempenho de SMS/MMS/RCS** também incluem uma opção para **Total de cliques** e mostram uma série temporal diária de eventos de clique. Os cliques são incrementados no redirecionamento (como quando um usuário visita um link) e podem ser incrementados mais de uma vez por usuário.

## Redirecionamento de usuários {#retargeting-users}

Para orientações sobre redirecionamento, acesse [Redirecionamento]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Eu sei quais usuários individuais estão clicando em uma URL? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Sim. Quando o **Rastreamento avançado** está ativado, você pode redirecionar usuários que clicaram em URLs aproveitando os [filtros de redirecionamento de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) ou os eventos de clique de SMS (`users.messages.sms.ShortLinkClick`) enviados pelo Currents.

### O encurtamento de links funciona com deep links ou links universais? {#does-link-shortening-work-with-deep-links-or-universal-links}

O encurtamento de links não funciona com deep links. Como alternativa, você pode encurtar links universais de provedores terceiros como Branch or ramificação ou Appsflyer, mas os usuários podem experimentar um breve redirecionamento ou efeito de "cintilação". Isso ocorre porque o link encurtado passa pela web primeiro antes de resolver para o link universal que suporta a abertura do app. Além disso, a Braze não consegue solucionar problemas que possam surgir ao encurtar links universais, como quebra de atribuição ou redirecionamentos inesperados.

{% alert note %}
Teste a experiência do usuário antes de implementar o encurtamento de links com links universais para confirmar que atende às suas expectativas.
{% endalert %}

### Os `send_ids` estão associados a eventos de clique de SMS? {#are-send_ids-associated-with-sms-click-events}

Não. No entanto, se você tiver o rastreamento avançado ativado, geralmente é possível atribuir `send_ids` a eventos de clique usando o [Query Builder]({{site.baseurl}}/query_builder) para consultar dados do Currents com esta consulta:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```


{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include channels/sms/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}