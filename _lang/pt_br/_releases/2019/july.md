---
nav_title: Julho
page_order: 6
noindex: true
page_type: update
description: "Este artigo contém notas de versão para julho de 2019."
---

# Julho de 2019 {#july-2019}

{% alert update %}
A Braze teve dois (você leu certo - **dois**) ciclos de lançamento de produtos este mês! A versão mais recente está indicada no topo, e a anterior é abordada na seção [No início deste mês](#earlier-this-month)!
{% endalert %}

## SAML/SSO

O [login único]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on) (SSO) oferece às empresas uma maneira segura e centralizada de controlar o acesso ao dashboard da Braze. Em resumo, um único conjunto de credenciais pode ser usado para acessar diferentes aplicativos, inclusive a Braze.

Além do [Google Sign-In com suporte a OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2), as empresas gostariam de ter SSO com suporte a SAML (Security Assertion Markup Language). Isso permite que elas se integrem perfeitamente com grandes provedores de identidade (IdPs), incluindo o [Azure Active Directory]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso) e o [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta), que suportam os mais recentes padrões do setor (SAML 2.0).

A Braze oferece suporte a:
- [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso)
- [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta)

## Exibição da chave de API or interface de programação do aplicativo (API) de eventos do Adjust {#adjust-event-api-key-shows}

Atualizamos a página de parceiros do Adjust para tornar essa chave de API or interface de programação do aplicativo (API) acessível aos clientes.

## Novos parceiros {#new-partners}

Alguns novos parceiros se juntaram ao nosso programa Alloys e foram adicionados à nossa documentação! Diga olá para:
- [FiveTran]({{site.baseurl}}/partners/fivetran)
- [Talon.One]({{site.baseurl}}/partners/talonone)
- [Voucherify]({{site.baseurl}}/partners/voucherify)

## Aprimoramento dos detalhes da campanha {#campaign-details-improvement}

Os detalhes expandidos da campanha agora são exibidos na seção... adivinhe... **Campaign Details** da página **Campaign**!

## Mostrar apenas os meus em Segments e Canvas {#show-only-mine-in-segments-canvas}

O filtro "Mostrar só os meus" na página **Campaigns** provou ser extremamente popular. Como resultado, também estamos adicionando essa opção às listas de Canvas e Segments!

### Comportamento de avanço {#advancement-behavior}

Agora é possível escolher [quando um usuário avança]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases) de uma etapa do Canvas para a próxima. Essas opções incluem "Message Sent" e "Entire Audience After Delay".

### Mensagens no app no Canvas {#in-app-messages-in-canvas}

[As mensagens no app]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) agora estão disponíveis no Canvas! Adicione uma etapa do Canvas e navegue pelos canais disponíveis para adicionar uma mensagem no app.

# No início deste mês {#earlier-this-month}

## Remoção da imagem do perfil do usuário {#user-profile-image-removal}

Estamos removendo as fotos de perfil de usuário exibidas nos perfis e nas pesquisas de usuários da Braze.

## Conteúdo conectado em Content Cards {#connected-content-in-content-cards}

Agora você pode usar as strings e a funcionalidade do [Conteúdo conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content#about-connected-content) nos [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards).

As chamadas do Conteúdo conectado para servidores externos ocorrerão quando um cartão for realmente enviado, não quando o cartão for visualizado pelo usuário. Semelhante ao e-mail, o conteúdo dinâmico será calculado e determinado no momento do envio, e não quando um cartão for realmente visualizado.

## Endereço de resposta nulo {#null-reply-to-address}

Os clientes agora podem definir um valor `null` para o endereço de resposta de uma mensagem de e-mail na página **Configurações de e-mail** na Braze ou usando a [API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/objects_filters/messaging/email_object). Quando usado, as respostas serão enviadas para o endereço de remetente listado. Agora é possível personalizar o campo de endereço de remetente como `dan@emailaddress.com`, e seus clientes poderão responder diretamente ao Dan.

Para definir um valor `null` para o endereço de resposta de uma mensagem de e-mail na Braze, acesse **Gerenciar configurações** na navegação e, em seguida, a guia **Configurações de e-mail**. Role até a seção **Outbound Email Settings** e selecione **Exclude "Reply-To" and send replies to "From"** como endereço padrão.

## Comparações de campanhas {#campaign-comparisons}

Analise [várias campanhas ao mesmo tempo para comparar o desempenho relativo delas]({{site.baseurl}}/report_builder), lado a lado na Braze — em uma única janela!

## Modelo de dispatch ID em mensagens com Liquid {#template-dispatch-id-into-messages-with-liquid}

{% alert note %}
O comportamento do `dispatch_id` difere entre Canvas e Campaigns porque a Braze trata as etapas do Canvas (exceto as etapas de entrada, que podem ser agendadas) como eventos disparados, mesmo quando são "agendadas". Saiba mais sobre o [comportamento do `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) em Canvas e Campaigns.
{% endalert %}

Se você quiser rastrear o envio de uma mensagem de dentro da própria mensagem (em uma URL, por exemplo), pode usar o modelo com o `dispatch_id`. Você pode encontrar a formatação para isso em nossa lista de tags de personalização compatíveis, em [Atributos do Canvas]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

Isso se comporta exatamente como o `api_id`: como o `api_id` não está disponível na criação da campanha, ele é inserido como um espaço reservado e será pré-visualizado como `dispatch_id_for_unsent_campaign`. O ID é gerado antes que a mensagem seja enviada e será incluído no momento do envio.

{% alert warning %}
O modelo Liquid de `dispatch_id_for_unsent_campaign` não funciona com mensagens no app, pois as mensagens no app não têm um `dispatch_id`.
{% endalert %}

## A configuração "Mostrar só os meus" persiste {#show-only-mine-setting-persists}

O filtro "Mostrar só os meus" na grade de campanhas permanecerá ativado sempre que você visitar a página **Campaigns**.

## Atualizações dos testes A/B {#ab-testing-updates}

É possível enviar um [teste A/B]({{site.baseurl}}/user_guide/messaging/ab_testing) único com até oito variantes (e controle opcional) para uma porcentagem especificada pelo usuário do público de uma campanha e, em seguida, enviar a melhor variante para o público restante em um horário pré-agendado.