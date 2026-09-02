---
nav_title: Depreciações
article_title: Depreciações
page_order: 9
page_type: reference
description: "Esta página inclui referências a artigos obsoletos e fornece uma lista de recursos obsoletos e sem suporte."
---

# Depreciações {#deprecations}

A tecnologia está sempre em movimento — dentro e fora da Braze! E fazemos o possível para acompanhá-la. Aqui, você encontrará as origens da Braze e sua tecnologia — como apoiamos nossos clientes nos tempos anteriores — antes de agora, pelo menos...

Você pode ter chegado aqui pesquisando um termo para uma integração ou recurso que não existe mais. Esta é nossa tentativa de manter você informado sobre nosso progresso e movimento no setor de tecnologia. Você pode encontrar uma lista de recursos obsoletos e sem suporte e ler artigos obsoletos visitando os links a seguir.

## Artigos obsoletos {#deprecated-articles}

- [Receptor de push broadcast personalizado para Android]({{site.baseurl}}/releases/deprecations/custom_broadcast_receiver/)
- [Configuração do Eclipse SDK or kit de desenvolvimento de software]({{site.baseurl}}/releases/deprecations/eclipse_setup_deprecated/)
- [Depreciação do TLS 1.0 e 1.1]({{site.baseurl}}/releases/deprecations/tls_deprecation/)
- [Integração do webhook Twilio]({{site.baseurl}}/releases/deprecations/twilio/)
- [Parceria com a Apptimize]({{site.baseurl}}/releases/deprecations/apptimize/)
- [Parceria com o Grouparoo]({{site.baseurl}}/releases/deprecations/grouparoo/)
- [Depreciação do `checkout.liquid` da Shopify]({{site.baseurl}}/releases/deprecations/shopify_checkout/)

## Registro de depreciações {#deprecations-log}

### Shopify `checkout.liquid`

**Suporte retirado**: Agosto de 2024 (fase 1), agosto de 2025 (fase 2)

O suporte para o `checkout.liquid` da Shopify começará a ser descontinuado em agosto de 2024 e terminará em agosto de 2025. A Shopify fará a transição para o [Checkout Extensibility](https://www.shopify.com/enterprise/blog/checkout-extensibility-winter-editions), que é mais seguro, performático e personalizável.

### Receptor de push broadcast personalizado para Android {#custom-push-broadcast-receiver-for-android}

**Suporte retirado**: Outubro de 2022

O uso de um `BroadcastReceiver` personalizado para notificações por push foi descontinuado. Use [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) em vez disso.

### Parceria com o Grouparoo {#grouparoo-partnership}

**Suporte retirado**: Abril de 2022

O suporte ao Grouparoo foi descontinuado a partir de abril de 2022.

### SDK or kit de desenvolvimento de software da Braze para Windows {#braze-windows-sdk}

**24 de março de 2022**: O SDK or kit de desenvolvimento de software da Braze para Windows está obsoleto, e nenhum novo app para Windows pode ser criado no dashboard da Braze.<br>
**15 de setembro de 2022**: Nenhuma mensagem nova pode ser enviada para os apps do Windows. As mensagens existentes e a coleta de dados não são afetadas.<br>
**11 de janeiro de 2024**: A Braze não enviará mais mensagens nem coletará dados de apps do Windows.

### Integração com o Baidu push {#baidu-push-integration}

**24 de março de 2022**: A integração da Braze com o Baidu push está obsoleta, e nenhum novo app do Baidu pode ser criado no dashboard da Braze.<br>
**15 de setembro de 2022**: Não é possível criar novas mensagens push do Baidu. As mensagens existentes e a coleta de dados não são afetadas.<br>
**11 de janeiro de 2024**: A Braze não enviará mais mensagens nem coletará dados dos apps do Baidu.

### Variável global appboyBridge {#appboybridge-global-variable}

**Suporte retirado**: Maio de 2021<br>
**Substituído por**: `brazeBridge`

A variável global `appboyBridge` está obsoleta e foi substituída por `brazeBridge`. `appboyBridge` continuará a funcionar para os clientes existentes, mas recomendamos que você migre para `brazeBridge` se estiver usando `appboyBridge`.

### Parceria Amazon Moments {#amazon-moments-partnership}

**Suporte retirado**: Junho de 2020

O suporte para o Amazon Moments foi descontinuado a partir de junho de 2020. O Amazon Moments está sendo incorporado à Amazon Advertising e descontinuou suas APIs e nossa integração.

### Parceria Factual {#factual-partnership}

**Suporte retirado**: Junho de 2020

O suporte ao Factual foi descontinuado a partir de junho de 2020. A Factual foi recentemente adquirida pelo Foursquare e não se integra mais à plataforma da Braze.

### Integração do webhook Twilio {#twilio-webhook-integration}

**Suporte retirado**: Janeiro de 2020

O suporte para a [integração do webhook Twilio]({{site.baseurl}}/partners/twilio/) foi descontinuado a partir de 31 de janeiro de 2020. Se ainda quiser acessar os serviços de SMS com a Braze, consulte nossa [documentação sobre SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/).

### Parceria com a Apptimize {#apptimize-partnership}

**Suporte retirado**: Agosto de 2019

Se estiver usando atualmente o [Apptimize com a Braze]({{site.baseurl}}/releases/deprecations/apptimize/), não haverá interrupção do serviço. Você ainda pode definir atributos personalizados do Apptimize para perfis de usuário da Braze. No entanto, não será fornecido suporte formal para esse parceiro.

### Mensagens originais no app {#original-in-app-messages}

**Suporte retirado:** Fevereiro de 2019<br>
**Substituído por**: [Mensagens no app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/)

A Braze aprimorou a aparência das mensagens no app para aderir às práticas recomendadas de UX e UI mais recentes e não oferece mais suporte às mensagens originais no app.

A Braze passou a usar uma nova forma de mensagens no app com as seguintes versões do SDK or kit de desenvolvimento de software:
- iOS: `2.19.0`
- Android: `1.13.0`
- Web: `1.3.0`

Antes dessas versões, a Braze suportava "mensagens originais no app". Anteriormente, o suporte para mensagens no app originais era fornecido para qualquer cliente que executasse uma campanha no app antes da nova versão. Todas as estatísticas da campanha não foram afetadas pela alteração, e aqueles que enviaram mensagens originais no app tiveram a oportunidade de enviar outras por meio do botão **Criar campanha** na página **Campaign**.

### Widget de feedback {#feedback-widget}

**Suporte retirado**: 1º de julho de 2019.

O SDK or kit de desenvolvimento de software da Braze forneceu um widget de feedback que podia ser adicionado ao seu app para permitir que os usuários deixassem feedback usando o método `submitfeedback` e o transmitissem para Desk.com ou Zendesk, sendo gerenciado no dashboard.

### Google Cloud Messaging (GCM)

**Suporte retirado**: Remoção do suporte da Braze: julho de 2018, remoção do suporte do Google: 29 de maio de 2019<br>
**Substituído por**: [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)

O Google [removeu o suporte ao GCM](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html) a partir de 29 de maio de 2019. A Braze descontinuou o suporte ao GCM dos SDKs do Android em julho de 2018, o que foi registrado em nossos [changelogs do SDK or kit de desenvolvimento de software do Android](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md). Isso significa que os tokens GCM existentes continuarão a funcionar, e você poderá enviar mensagens aos usuários existentes. No entanto, não será possível enviar mensagens a novos usuários.

Os clientes que ainda não migraram para o [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) podem ser afetados por essa alteração.

Se você não tiver feito a transição para o FCM, todos os registros de tokens por push do GCM falharão. Se os seus apps são atualmente compatíveis com o GCM, você precisará trabalhar com suas equipes de desenvolvimento na [transição do GCM para o Firebase Cloud Messaging (FCM)](https://developers.google.com/cloud-messaging/android/android-migrate-fcm).

### Eclipse

**Suporte retirado**: 2014-2015<br>
**Substituído por**: [Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)

A Braze descontinuou o suporte ao Eclipse IDE devido ao fato de o Google [ter encerrado o suporte](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html) ao plug-in Android Developer Tools (ADT) do Eclipse.

Se precisar de ajuda com a integração do Eclipse antes da migração, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact/) para obter assistência.

### Raw Event Stream (RES) {#the-raw-event-stream-res}

**Suporte retirado**: Julho de 2018<br>
**Substituído por**: [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/)

O Raw Event Stream foi o predecessor do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) e foi descontinuado para dar lugar ao futuro dos dados da Braze.

### Postergação enquanto sem atividades — recurso GCM {#delay-while-idle-gcm-feature}

**Suporte retirado**: Novembro de 2016

O parâmetro Postergação enquanto sem atividades fazia parte anteriormente das [opções de push do GCM](https://developers.google.com/cloud-messaging/http-server-ref). O Google retirou o suporte a essa opção em 15 de novembro de 2016. Anteriormente, quando definido como **true**, indicava que a mensagem não deveria ser enviada até que o dispositivo se tornasse ativo.

### Endpoints personalizados {#custom-endpoints}

**Suporte retirado**: Dezembro de 2019

Remoção de endpoints personalizados. Se você tiver um endpoint personalizado, poderá continuar a usá-lo, mas a Braze não os fornecerá mais.