{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Desabilitando o rastreamento de dados {#disabling-data-tracking}

Para desabilitar a coleta de dados, use o método `disableSDK`. Após chamar esse método, o SDK or kit de desenvolvimento de software da Braze para de enviar dados para os servidores da Braze.

```javascript
Braze.disableSDK();
```

## Retomando o rastreamento de dados {#resuming-data-tracking}

Para retomar a coleta de dados após desabilitá-la, use o método `enableSDK`.

```javascript
Braze.enableSDK();
```

## Limpando dados {#wiping-data}

Para excluir todos os dados do SDK or kit de desenvolvimento de software da Braze armazenados localmente no dispositivo, use o método `wipeData`. Após chamar esse método, o SDK or kit de desenvolvimento de software será desabilitado e precisará ser reabilitado com `enableSDK`.

```javascript
Braze.wipeData();
```

## Liberação de dados {#flushing-data}

Para solicitar uma liberação imediata de quaisquer dados pendentes para os servidores da Braze, use `requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## Configurando o rastreamento de anúncios ativado {#setting-ad-tracking-enabled}

Para informar a Braze se o rastreamento de anúncios está ativado para este dispositivo, use o método `setAdTrackingEnabled`. O SDK or kit de desenvolvimento de software não coleta esses dados automaticamente.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

O segundo parâmetro é o Google Advertising ID e é usado apenas no Android.

## Atualizando a lista de permissões da propriedade de rastreamento (somente iOS) {#updating-the-tracking-property-allow-list-ios-only}

Para atualizar a lista de tipos de dados declarados para rastreamento, use `updateTrackingPropertyAllowList`. Essa função não tem efeito no Android.

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

Para saber mais, consulte [Manifesto de privacidade]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift#swift_privacy-manifest).

## Logout e cancelamento de registro de push {#logout-and-unregister-push}

Este recurso ainda não é compatível com o SDK or kit de desenvolvimento de software do React Native.