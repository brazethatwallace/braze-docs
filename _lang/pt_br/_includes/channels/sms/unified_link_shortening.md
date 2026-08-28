O encurtamento de links permite encurtar automaticamente URLs contidas em mensagens SMS ou RCS e coletar análise de dados de taxa de cliques, fornecendo métricas de engajamento adicionais para ajudar a entender como os usuários estão interagindo com suas campanhas.

O encurtamento de links pode ser ativado no [nível da variante de mensagem]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-1-create-your-campaign) tanto em Campaigns quanto em Canvas. Quando o encurtamento de links está ativado, os cliques geram um [evento de clique de SMS]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) enviado pelo Currents.

{% multi_lang_include channels/sms/rcs_link_shortening_note.md %}

Os links são encurtados usando nosso domínio curto compartilhado (`brz.ai`) ou seu domínio personalizado de encurtamento de links, e são válidos por 9 semanas a partir da data em que foram criados. Um exemplo de URL pode ser algo como `https://brz.ai/8jshX2dj`.

## Usando o encurtamento de links {#using-link-shortening}

Para usar o encurtamento de links, certifique-se de que a caixa de seleção de encurtamento de links no criador de mensagem esteja marcada.

{% tabs %}
{% tab SMS composer %}

![Criador de mensagem SMS com a caixa de seleção de encurtamento de links marcada.]({% image_buster /assets/img/link_shortening/shortening1.png %})

{% endtab %}
{% tab RCS composer %}

![Criador de mensagem RCS com a caixa de seleção de encurtamento de links marcada.]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %})

{% endtab %}
{% endtabs %}

A Braze reconhece apenas URLs que começam com `http://` ou `https://`. Quando uma URL é reconhecida, a seção **Prévia** é atualizada com uma URL de espaço reservado. A Braze estima o comprimento da mensagem após o encurtamento, mas um alerta solicita que você selecione um usuário teste e salve a mensagem como rascunho para uma estimativa mais precisa.

![Criador de mensagem com uma URL longa na caixa "Message" e um link encurtado gerado na prévia.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### Adicionando parâmetros UTM {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personalização com Liquid em URLs {#liquid-personalization-in-urls}

Para saber como construir URLs dinamicamente diretamente no criador da Braze, permitindo adicionar parâmetros UTM dinâmicos às suas URLs ou enviar links exclusivos aos usuários, consulte [Usar personalização com Liquid em URLs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls).

## Testes {#testing}

Antes de lançar sua Campaign ou Canvas, a prática recomendada é visualizar e testar sua mensagem primeiro. Para isso, acesse a guia **Teste** para visualizar e enviar uma mensagem SMS ou RCS para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) ou para um usuário individual.

Essa prévia é atualizada com a personalização relevante e a URL encurtada. A contagem de caracteres e os [segmentos faturáveis]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) também são atualizados para refletir a personalização renderizada e a URL encurtada.

Salve a Campaign ou o Canvas antes de enviar uma mensagem de teste para receber uma representação da URL encurtada que é enviada na sua mensagem. Se a Campaign ou o Canvas não for salvo antes de um envio de teste, o envio de teste incluirá uma URL de espaço reservado.

{% alert important %}
Se um rascunho for criado dentro de um Canvas ativo, uma URL encurtada não será gerada. A URL encurtada real é gerada quando o rascunho do Canvas se torna ativo.
{% endalert %}

![Guia "Teste" de mensagem com campos para selecionar destinatários de teste.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
A personalização Liquid e as URLs encurtadas são processadas na guia **Teste** após um usuário ser selecionado. Certifique-se de que um usuário esteja selecionado para receber uma contagem de caracteres precisa.
{% endalert %}

## Rastreamento de cliques {#click-tracking}

Quando o encurtamento de links está ativado, a tabela **SMS/MMS/RCS Performance** inclui uma coluna chamada **Total Clicks** que mostra uma contagem de eventos de clique por variante e uma taxa de cliques associada. Para mais detalhes sobre métricas, consulte [Performance de mensagens]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting).

![Tabela de métricas de performance de SMS e MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %})

As tabelas **Historical Performance** e **SMS/MMS/RCS Performance** também incluem uma opção para **Total Clicks** e mostram uma série temporal diária de eventos de clique. Os cliques são incrementados no redirecionamento (como quando um usuário acessa um link) e podem ser incrementados mais de uma vez por usuário.

## Redirecionamento de usuários {#retargeting-users}

Para orientações sobre redirecionamento, visite [Redirecionamento]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Consigo saber quais usuários individuais estão clicando em uma URL? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Sim. Você pode redirecionar usuários que clicaram em URLs usando os [filtros de redirecionamento de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) ou os eventos de clique de SMS (`users.messages.sms.ShortLinkClick`) enviados pelo Currents.

### O encurtamento de links funciona com deep links ou links universais? {#does-link-shortening-work-with-deep-links-or-universal-links}

O encurtamento de links não funciona com deep links. Como alternativa, você pode encurtar links universais de provedores terceiros, como Branch ou Appsflyer, mas os usuários podem experimentar um breve redirecionamento ou efeito de "flickering". Isso ocorre porque o link encurtado passa primeiro pela web antes de resolver para o link universal que suporta a abertura do app. Além disso, a Braze não consegue solucionar problemas que possam surgir ao encurtar links universais, como quebra de atribuição ou redirecionamentos inesperados.

{% alert note %}
Teste a experiência do usuário antes de implementar o encurtamento de links com links universais para confirmar que atende às suas expectativas.
{% endalert %}

### Os `send_ids` são associados a eventos de clique de SMS? {#are-send_ids-associated-with-sms-click-events}

Não. No entanto, você geralmente pode atribuir `send_ids` a eventos de clique usando o [Query Builder]({{site.baseurl}}/query_builder) para consultar dados do Currents com esta consulta:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```