---
nav_title: Google Tag Manager
article_title: Google Tag Manager com o SDK da Braze
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Aprenda como inicializar o SDK da Braze usando métodos como inicialização em tempo de execução, inicialização atrasada ou Google Tag Manager."

---

# Google Tag Manager com o SDK da Braze {#google-tag-manager-with-the-braze-sdk}

> Aprenda como usar o [Google Tag Manager (GTM)](https://developers.google.com/tag-platform/tag-manager) com o SDK da Braze, para que você possa controlar remotamente o rastreamento de eventos da Braze e as atualizações de atributos de usuário sem precisar de alterações de código ou novas versões do app.

{% sdktabs %}
{% sdktab web %}
## Sobre o Google Tag Manager para Web {#google-tag-manager}

O Google Tag Manager (GTM) permite que você adicione, remova e edite tags remotamente em seu site sem precisar de uma liberação de código de produção ou recursos de engenharia. A Braze oferece os seguintes modelos para o Web SDK:

| Tipo de tag | Caso de uso |
|--------|--------|
| Tag de inicialização | Essa tag permite que você [integre o Web Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) sem precisar modificar o código do seu site. |
| Tag de ação | Essa tag permite que você [crie Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [defina atributos do usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) e [gerencie a coleta de dados]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sobre o Google Tag Manager para Web" }

## Sequenciamento de tags para tags de ação da Braze {#tag-sequencing-for-braze-action-tags}

Eventos personalizados e outras tags de ação da Braze podem falhar quando são disparados antes que a tag **Braze Initialization** termine de carregar o Web SDK. No Google Tag Manager, abra a tag de ação, acesse **Advanced Settings** > **Tag Sequencing**, selecione **A tag that fires before [this tag] is fired** e escolha sua tag Braze Initialization.

Para saber mais, consulte [Verificar o sequenciamento de tags para eventos personalizados]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing).

## Registrar compras com o GTM {#log-purchases-with-gtm}

Nas tags de ação da Braze e nas tags HTML personalizadas, chame `braze.logPurchase()` para registrar receita. O namespace legado `appboy.logPurchase()` não é compatível com as integrações atuais do Web SDK.

## Registrar eventos personalizados com o GTM {#logging-custom-events-with-gtm}

Você pode registrar eventos personalizados usando uma tag **Custom HTML** no GTM. Essa abordagem usa a [camada de dados](https://developers.google.com/tag-platform/tag-manager/datalayer) do GTM para passar dados de eventos do seu site para uma tag do GTM que chama o Web SDK da Braze.

### Etapa 1: Envie o evento para a camada de dados {#step-1-push-the-event-to-the-data-layer}

No código do seu site, envie um evento para a camada de dados sempre que quiser disparar o evento personalizado. Por exemplo, para registrar um evento personalizado quando um botão é clicado:

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### Etapa 2: Crie um disparador no GTM {#step-2-create-a-trigger-in-gtm}

1. No seu contêiner do GTM, acesse **Triggers** e crie um novo disparador.
2. Defina o **Trigger Type** como **Custom Event**.
3. Defina o **Event Name** com o mesmo valor que você enviou para a camada de dados (por exemplo, `my_custom_event`).
4. Escolha quando o disparador deve ser acionado (por exemplo, **All Custom Events**).

### Etapa 3: Crie uma tag HTML personalizada {#step-3-create-a-custom-html-tag}

1. No GTM, acesse **Tags** e crie uma nova tag.
2. Defina o **Tag Type** como **Custom HTML**.
3. No campo HTML, adicione o seguinte:

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. Em **Triggering**, selecione o disparador que você criou na etapa 2.
5. Salve e publique seu contêiner.

Para incluir propriedades do evento, passe-as como o segundo argumento:

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Política de consentimento de usuários da UE do Google {#googles-eu-user-consent-policy}

{% alert important %}
O Google está atualizando sua [Política de consentimento de usuários da UE](https://www.google.com/about/company/user-consent-policy/) em resposta a mudanças na [Lei dos Mercados Digitais (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que está em vigor desde 6 de março de 2024. Essa nova mudança exige que os anunciantes divulguem certas informações aos seus usuários finais do EEE e do Reino Unido, bem como obtenham os consentimentos necessários deles. Consulte a documentação a seguir para saber mais.
{% endalert %}

Como parte da Política de consentimento de usuários da UE do Google, os seguintes atributos personalizados booleanos precisam ser registrados nos perfis de usuário:

- `$google_ad_user_data`
- `$google_ad_personalization`

Se você estiver definindo esses atributos por meio da integração com o GTM, os atributos personalizados exigem a criação de uma tag HTML personalizada. A seguir, um exemplo de como registrar esses valores como tipos de dados booleanos (não como strings):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Para saber mais, consulte [Audience Sync para Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync).

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## Solução de problemas {#troubleshooting}

Se a Braze não inicializar ou os eventos não aparecerem como esperado, confirme se o contêiner do GTM está publicado, se os disparadores e a ordem de acionamento das tags estão alinhados com o [ciclo de vida e a estratégia de inicialização]({{site.baseurl}}/developer_guide/sdk_integration) do seu SDK, e se os dispositivos de teste não estão bloqueando os endpoints da Braze.

Para falhas de inicialização, verifique se a tag da Braze ou o provedor de tag personalizado está recebendo o `actionType` e os parâmetros esperados (consulte as guias Android, Swift e Web nesta página). Para obter um registro detalhado ao validar eventos disparados pelo GTM, ative o registro de depuração do SDK da sua plataforma conforme descrito nos guias de integração vinculados nessas guias.