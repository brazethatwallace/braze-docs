---
nav_title: Ponte JavaScript
article_title: Ponte JavaScript para landing pages
page_order: 5
page_type: reference
description: "Saiba como usar a ponte JavaScript brazeBridge para registrar eventos, definir atributos personalizados e disparar ações da Braze a partir de um bloco de código personalizado de uma landing page."
---

# Ponte JavaScript para landing pages {#javascript-bridge-for-landing-pages}

> As landing pages suportam uma "ponte" JavaScript para conectar seu código personalizado (HTML, CSS e JavaScript) ao SDK da Braze.

Acesse a ponte usando `brazeBridge` em um bloco de código personalizado para registrar eventos, definir atributos personalizados, identificar usuários e muito mais quando um visitante interage com sua landing page.

## Como funciona {#how-it-works}

As landing pages permitem que você adicione HTML, CSS e JavaScript personalizados a um bloco de **código personalizado** para ter maior controle sobre a aparência, o estilo e o comportamento da sua página. Os blocos de código personalizado podem usar a [ponte JavaScript](#supported-methods) para registrar eventos, definir atributos personalizados, identificar usuários e muito mais:
- Registrar eventos personalizados e compras
- Definir atributos de usuário padrão e personalizados
- Rastrear cliques e envios de formulário
- Identificar usuários

Se você reutilizar código `brazeBridge` de mensagens no app ou Banners, ele ainda será executado nas landing pages. Os métodos que não se aplicam a landing pages são ignorados e registram um aviso no console do navegador em vez de causar um erro. Para mais detalhes, consulte [Métodos não suportados em landing pages](#methods-not-supported-on-landing-pages).

{% alert important %}
A ponte de landing page é assíncrona; cada método retorna uma Promise. Isso difere da [ponte de mensagens no app em HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge), cujos métodos retornam imediatamente. Se a próxima etapa do seu script depende da conclusão de uma chamada da ponte — como redirecionar a página, enviar um formulário ou enviar dados para a Braze — use `await` ou `.then()` e não presuma que a chamada foi concluída de forma síncrona.
{% endalert %}

## Disponibilidade da ponte {#bridge-availability}

Quando um visitante abre sua landing page, `brazeBridge` já está disponível no JavaScript do seu **código personalizado**. Chame os métodos da ponte diretamente nas landing pages — você não precisa aguardar um evento de prontidão separado como as mensagens no app usam com `ab.BridgeReady`.

Ter o objeto da ponte disponível não significa que o SDK da Braze está inicializado para aquele visitante. O SDK é inicializado para uma visita à landing page em qualquer um destes casos:

- O visitante abre a página por meio de uma [Liquid tag de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) enviada por um canal da Braze (e-mail, SMS, push, etc.). O SDK é inicializado automaticamente quando a página carrega.
- O visitante envia o formulário da página — por exemplo, clicando em um botão **Enviar** que envia os dados do formulário. Isso inclui chamadas `brazeBridge` feitas dentro dos callbacks `registerFormInput` de um [bloco de formulário personalizado]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks), já que eles são executados como parte do envio do formulário.

Se um visitante abrir a landing page diretamente, sem uma Liquid tag de landing page, e nunca enviar o formulário, a página será anônima para a Braze, e as chamadas de métodos da ponte não terão efeito.

{% alert note %}
`window.lpBridge` e `window.appboyBridge` referenciam o mesmo objeto da ponte, mas ambos estão obsoletos. Use `window.brazeBridge`.
{% endalert %}

## Exemplo {#example}

Como os métodos são assíncronos, use um handler assíncrono e `await` nas chamadas quando a ordem ou a conclusão forem importantes:

```html
<button id="button">Set Favorite Color</button>
<script>
  document.querySelector("#button").onclick = async function () {
    // Track a click for analytics
    await brazeBridge.logClick("set-favorite-color");
    // Set the user's custom attribute
    await brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    await brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    await brazeBridge.requestImmediateDataFlush();
  };
</script>
```

## Métodos suportados {#supported-methods}

Os seguintes métodos `brazeBridge` retornam uma promise e são suportados nos blocos de **código personalizado** de landing pages. Use `await` ou `.then()` quando precisar sequenciar tarefas ou garantir a conclusão.

### Métodos de nível superior {#top-level-methods}

| Método | Descrição |
| --- | --- |
| `brazeBridge.changeUser(userId, signature?)` | Identifica o usuário com um ID exclusivo. |
| `brazeBridge.logCustomEvent(eventName, eventProperties?)` | Registra um evento personalizado. |
| `brazeBridge.logPurchase(productId, price, currencyCode?, quantity?, purchaseProperties?)` | Registra uma compra. |
| `brazeBridge.requestImmediateDataFlush(callback?)` | Envia os dados enfileirados para os servidores da Braze. |
| `brazeBridge.logClick(trackingId)` | Registra um clique na landing page (`lp_c`) para o ID de rastreamento fornecido. Consulte [Rastreamento de cliques](#click-tracking). |
| `brazeBridge.logSubmit()` | Registra um envio de formulário de landing page (`lp_fs`). Específico de landing pages. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos de nível superior" }

### Métodos de `getUser()` {#getuser-methods}

{% alert note %}
`brazeBridge.getUser()` retorna um objeto simples de forma síncrona, então você não precisa usar `await` em `getUser()`; os métodos no objeto retornado (como `getUser().setEmail(email)`) retornam Promises.
{% endalert %}

`getUser()` retorna um objeto que expõe os seguintes métodos de usuário. Cada método retorna uma Promise.

| Método | Descrição |
| --- | --- |
| `getUser().setFirstName(firstName)` | Define o nome do usuário. |
| `getUser().setLastName(lastName)` | Define o sobrenome do usuário. |
| `getUser().setEmail(email)` | Define o endereço de e-mail do usuário. |
| `getUser().setPhoneNumber(phoneNumber)` | Define o número de telefone do usuário. |
| `getUser().setGender(gender: "m" \| "f" \| "o" \| "u" \| "n" \| "p")` | Define o gênero do usuário: masculino, feminino, outro, desconhecido, não aplicável ou prefere não dizer, respectivamente. |
| `getUser().setDateOfBirth(year, month, day)` | Define a data de nascimento do usuário. |
| `getUser().setCountry(country)` | Define o país do usuário. |
| `getUser().setHomeCity(city)` | Define a cidade do usuário. |
| `getUser().setLanguage(language)` | Define o idioma do usuário. |
| `getUser().setCustomUserAttribute(key, value, merge?)` | Define um atributo personalizado do usuário. |
| `getUser().addToCustomAttributeArray(key, value)` | Adiciona um valor a um array de atributo personalizado. |
| `getUser().removeFromCustomAttributeArray(key, value)` | Remove um valor de um array de atributo personalizado. |
| `getUser().incrementCustomUserAttribute(key, incrementValue?)` | Incrementa um atributo personalizado numérico. |
| `getUser().setCustomLocationAttribute(key, latitude, longitude)` | Define um atributo de localização personalizado. |
| `getUser().addToSubscriptionGroup(subscriptionGroupId)` | Adiciona o usuário a um grupo de inscrições de e-mail ou SMS. |
| `getUser().removeFromSubscriptionGroup(subscriptionGroupId)` | Remove o usuário de um grupo de inscrições de e-mail ou SMS. |
| `getUser().setEmailNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | Define o status de inscrição de notificações por e-mail. |
| `getUser().setPushNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | Define o status de inscrição de notificações por push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos de getUser()" }

## Rastreamento de cliques {#click-tracking}

Use `brazeBridge.logClick(trackingId)` para rastrear cliques na sua landing page. Cada chamada registra um evento de clique na landing page (`lp_c`) marcado com o ID de rastreamento que você fornecer:

```html
<a href="#" onclick="brazeBridge.logClick('cta-hero')">Get started</a>
```

{% alert note %}
O rastreamento de cliques em landing pages difere das mensagens no app, que usam `logClick('0')` e `logClick('1')` como IDs convencionais para "Botão 1" e "Botão 2". As landing pages não possuem IDs de botão especiais equivalentes. Cada chamada `logClick(trackingId)` registra um evento `lp_c` identificado pelo ID de rastreamento que você fornecer.
{% endalert %}

## Métodos não suportados em landing pages {#methods-not-supported-on-landing-pages}

Os métodos a seguir funcionam em mensagens no app e Banners, mas não são suportados em landing pages. Se o seu código chamar um deles em uma landing page, a Braze ignora a chamada. Sua página continua funcionando, mas você pode ver um aviso no console de desenvolvedor do navegador.

| Método | Observações |
| --- | --- |
| `brazeBridge.closeMessage()` | Não há interface de mensagem para fechar em uma landing page. |
| `brazeBridge.requestPushPermission(successCallback?, deniedCallback?)` | A permissão de push não é solicitada a partir de uma landing page. |
| `brazeBridge.web.registerAppboyPushMessages(successCallback?, deniedCallback?)` | O registro de web push não está disponível em landing pages. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos não suportados em landing pages" }

## Conteúdo relacionado {#related-content}

- [Criar blocos de formulário personalizados]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks) aborda um uso mais avançado desta ponte: conectar uma interface totalmente personalizada a um formulário de landing page.
- [Criar landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)