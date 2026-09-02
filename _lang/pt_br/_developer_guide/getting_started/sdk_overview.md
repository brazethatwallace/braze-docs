---
nav_title: Visão geral do SDK or kit de desenvolvimento de software
article_title: Visão geral do SDK or kit de desenvolvimento de software para desenvolvedores
description: "Este artigo de referência sobre integração apresenta uma visão geral técnica para desenvolvedores do SDK or kit de desenvolvimento de software da Braze. Ele discute as análises de dados padrão rastreadas pelo SDK or kit de desenvolvimento de software."
page_order: 0
---

# [![curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}Visão geral do SDK para desenvolvedores {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdevelopersdk-integration-basics-stylefloatrightwidth120pxborder0-classnoimgbordersdk-overview-for-developers}

> Antes de começar a integrar os SDKs da Braze, você pode se perguntar o que exatamente está desenvolvendo e integrando. Talvez você esteja curioso para saber como pode personalizar o SDK or kit de desenvolvimento de software para atender ainda mais às suas necessidades. Este artigo pode ajudar a esclarecer todas as suas dúvidas sobre o SDK or kit de desenvolvimento de software.

Você é um profissional de marketing e está procurando um resumo básico do SDK or kit de desenvolvimento de software? Em vez disso, dê uma olhada em nossa [visão geral para profissionais de marketing]({{site.baseurl}}/user_guide/get_started/sdk_overview).

Em resumo, o SDK or kit de desenvolvimento de software da Braze:
* Coleta e sincroniza dados de usuários em um perfil de usuário consolidado
* Coleta automaticamente dados da sessão, informações do dispositivo e tokens por push
* Captura dados de engajamento de marketing e dados personalizados específicos do seu negócio
* Potencializa as notificações por push, as mensagens no app e os canais de envio de mensagens do cartão de conteúdo

Assista ao vídeo a seguir para uma breve introdução aos conceitos básicos de integração do SDK or kit de desenvolvimento de software da Braze e suas funcionalidades principais.

{% multi_lang_include video.html id="il152jayp0" source="wistia" %}

## Performance do app {#app-performance}

A Braze não deve ter nenhum impacto negativo na performance do seu app.

Os SDKs da Braze têm uma pegada muito pequena. Nós ajustamos automaticamente a taxa de envio dos dados de usuários dependendo da qualidade da rede, além de permitir o controle manual da rede. Agrupamos automaticamente as solicitações de API or interface de programação do aplicativo (API) do SDK or kit de desenvolvimento de software para garantir que os dados sejam registrados rapidamente, mantendo a máxima eficiência de rede. Por fim, a quantidade de dados enviados do cliente para a Braze em cada chamada de API or interface de programação do aplicativo (API) é extremamente pequena.

## Compatibilidade do SDK or kit de desenvolvimento de software {#sdk-compatibility}

O SDK or kit de desenvolvimento de software da Braze foi projetado para funcionar muito bem e não interferir com outros SDKs presentes no seu app. Se você estiver enfrentando problemas que possam ser causados por incompatibilidade com outro SDK or kit de desenvolvimento de software, entre em contato com o suporte da Braze.

## Tratamento padrão de análise de dados e sessões {#default-analytics-and-session-handling}

Alguns dados de usuário são coletados automaticamente pelo nosso SDK or kit de desenvolvimento de software — por exemplo, Primeiro Uso do App, Último Uso do App, Contagem Total de Sessões, SO do Dispositivo, etc. Se você seguir nossos guias de integração para implementar nossos SDKs, poderá aproveitar essa [coleta de dados padrão]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection). Verificar essa lista pode ajudar a evitar o armazenamento das mesmas informações sobre os usuários mais de uma vez. Com exceção do início e do fim da sessão, todos os outros dados rastreados automaticamente não contam para o seu uso de pontos de dados.

{% alert note %}
Todos os nossos recursos são configuráveis, mas é uma boa ideia implementar completamente o modelo de coleta de dados padrão.

<br>Se necessário para o seu caso de uso, você pode [limitar a coleta de determinados dados](#blocking-data-collection) após a conclusão da integração.
{% endalert %}

## Upload e download de dados {#data-upload-and-download}

O SDK or kit de desenvolvimento de software da Braze armazena dados em cache (sessões, eventos personalizados, etc.) e faz upload periodicamente. Os valores só serão atualizados no dashboard após o upload dos dados. O intervalo de upload leva em consideração o estado do dispositivo e é determinado pela qualidade da conexão de rede:

|Qualidade da conexão de rede |    Intervalo de envio de dados|
|---|---|
|Ótima    |10 segundos|
|Boa    |30 segundos|
|Ruim    |60 segundos|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Upload e download de dados" }

Se não houver conexão de rede, os dados serão armazenados em cache localmente no dispositivo até que a conexão seja restabelecida. Quando a conexão for restabelecida, os dados serão enviados para a Braze.

A Braze envia dados para o SDK or kit de desenvolvimento de software no início de uma sessão com base nos Segments em que o usuário se encontra no momento da sessão. As novas mensagens no app não serão atualizadas durante a sessão. No entanto, os dados do usuário durante a sessão continuarão sendo processados conforme são enviados pelo cliente. Por exemplo, um usuário inativo (que não usou o app há mais de 7 dias) ainda receberá conteúdo direcionado a usuários inativos em sua primeira sessão de volta ao app.

## Bloqueio da coleta de dados {#blocking-data-collection}

É possível (embora não recomendado) bloquear a coleta automática de determinados dados da sua integração SDK or kit de desenvolvimento de software ou adicionar processos a uma lista de permissões.

Bloquear a coleta de dados não é recomendado, pois remover dados analíticos reduz a capacidade da sua plataforma de personalização e direcionamento. Por exemplo:

- Se você optar por não integrar totalmente a localização em um dos SDKs, não será possível personalizar suas mensagens com base no idioma ou local.
- Se você optar por não integrar o fuso horário, talvez não consiga enviar mensagens no fuso horário do usuário.
- Se você optar por não integrar informações visuais específicas do dispositivo, o conteúdo das mensagens pode não ser otimizado para aquele dispositivo.

Recomendamos fortemente a integração completa dos SDKs para aproveitar ao máximo os recursos do nosso produto.

{% tabs %}
{% tab Web SDK or kit de desenvolvimento de software %}

Você pode simplesmente não integrar determinadas partes do SDK or kit de desenvolvimento de software ou usar [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) para um usuário. Esse método sincronizará os dados registrados antes da chamada de `disableSDK()` e fará com que todas as chamadas subsequentes ao SDK or kit de desenvolvimento de software da Braze para Web nessa página e em carregamentos futuros sejam ignoradas. Se você quiser retomar a coleta de dados posteriormente, poderá usar o método [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) para retomar a coleta de dados. Saiba mais sobre isso no nosso artigo [Desativando o rastreamento web]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=web).

{% endtab %}
{% tab Android SDK or kit de desenvolvimento de software %}

Você pode usar [`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder) para configurar o SDK or kit de desenvolvimento de software de modo que envie apenas um subconjunto das chaves ou valores do objeto de dispositivo de acordo com uma lista de permissões definida. Isso deve ser ativado via [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder).

{% alert important %}
Uma lista de permissões vazia fará com que **nenhum** dado do dispositivo seja enviado à Braze.
{% endalert %}

{% endtab %}
{% tab Swift SDK or kit de desenvolvimento de software %}

Você pode atribuir um conjunto de campos elegíveis a [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) na sua `Braze.Configuration` para especificar uma lista de permissões para os campos de dispositivo coletados pelo SDK or kit de desenvolvimento de software. A lista completa de campos está definida em [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). Para desativar a coleta de todos os campos de dispositivo, defina o valor dessa propriedade como um conjunto vazio (`[]`).

{% alert important %}
Por padrão, todos os campos são coletados pelo SDK or kit de desenvolvimento de software Swift da Braze. A remoção de algumas propriedades do dispositivo pode desativar recursos do SDK or kit de desenvolvimento de software.
{% endalert %}

Para mais detalhes de uso, consulte [Armazenamento]({{site.baseurl}}/developer_guide/storage?tab=swift) na documentação do SDK or kit de desenvolvimento de software Swift.

{% endtab %}
{% endtabs %}

## Qual versão do SDK or kit de desenvolvimento de software estou usando? {#what-version-of-the-sdk-am-i-on}

Você pode usar o dashboard para ver a versão do SDK or kit de desenvolvimento de software de um app específico acessando **Configurações > Configurações do app**. A **Versão do SDK or kit de desenvolvimento de software ativo** lista a versão mais recente do SDK or kit de desenvolvimento de software da Braze utilizada pelo seu aplicativo ativo mais recente para pelo menos 5% dos seus usuários.

![Um app chamado Swifty em um espaço de trabalho. A versão do SDK ativo é 6.6.0.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"}

{% alert tip %}
Se você tem um app iOS, pode confirmar que está usando o [Swift SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift) em vez do legado [Objective-C iOS SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) se a sua **Versão do SDK or kit de desenvolvimento de software ativo** for igual ou superior a 5.0.0, que foi a primeira versão lançada do Swift SDK or kit de desenvolvimento de software.
{% endalert %}