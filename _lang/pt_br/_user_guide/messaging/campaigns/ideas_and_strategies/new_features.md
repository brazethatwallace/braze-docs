---
nav_title: Divulgação de recursos e nova versão do app
article_title: Divulgação de recursos e nova versão do app
page_order: 9
page_type: reference
description: "Este artigo de referência discute como manter seus usuários informados e entusiasmados quando você lança novos recursos ou versões."
tool: Campaigns

---

# Divulgação de recursos e nova versão do app {#feature-awareness-and-new-app-version}

> Este artigo de referência aborda como usar a plataforma da Braze para manter seus clientes atualizados sobre novos recursos e versões do seu app.

Você trabalha duro para atualizar e melhorar continuamente seu app, e quer que seus usuários aproveitem esses novos recursos empolgantes e novas versões. Aprenda como ensinar seus usuários sobre os novos recursos que eles ainda não usaram e incentive-os a explorar o app para aproveitar ao máximo o que você tem a oferecer.

Campanhas de divulgação de recursos são uma ótima maneira de incentivar os usuários a permanecerem engajados com seu app enquanto você continua aprimorando suas funcionalidades. Manter os usuários atualizados é uma ótima forma de mantê-los ativos, melhorar as avaliações e garantir o engajamento.

## Filtrando pelas versões mais recentes do app {#filtering-by-most-recent-app-versions}

Os SDKs da Braze rastreiam automaticamente a versão mais recente do app de um usuário. Essas versões podem ser usadas em filtros e Segments para determinar quais usuários devem receber uma mensagem ou Campaign.

![O painel de Opções de direcionamento na etapa Direcionar Usuários no fluxo de criação de Campaigns. A seção Filtros adicionais inclui o seguinte filtro "Most Recent App Version Number for Android Stopwatch (Android) is below 3.7.0 (134.0.0.0)".]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
Pode levar algum tempo para que as versões atuais do app sejam preenchidas. A versão do app no perfil de usuário é atualizada quando a informação é capturada pelo SDK, o que depende de quando os usuários abrem seus apps. Se o usuário não abrir o app, a versão atual não será atualizada. <br><br> Esses filtros também não se aplicam retroativamente. É recomendável usar "maior que" ou "igual a" para versões atuais e futuras, mas usar filtros de versões anteriores pode causar comportamentos inesperados.
{% endalert %}

### Número da versão do app {#app-version-number}

Use o filtro **App Version Number** para segmentar usuários pela versão e número de build do app.

Este filtro suporta comparações numéricas para direcionar uma faixa de versões do app. Por exemplo, você pode direcionar usuários cujo app está "abaixo de", "acima de" ou "igual a" a versão "1.2.3", o que pode ser útil para promover um novo recurso que requer uma atualização do app.

Este novo filtro pode substituir o filtro legado "App Version Name", que exigia listar explicitamente cada versão anterior ou usar uma expressão regular.

**Como funciona**

* Cada parte da versão `major.minor.patch` enviada na versão do seu app é comparada como números inteiros
* Se os números principais (major) forem iguais, os números secundários (minor) são comparados, e assim por diante.

**Importante**

* Apps Android possuem tanto um [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) legível por humanos quanto um [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) interno. O filtro App Version Number usa o `versionCode` porque ele é garantidamente incrementado a cada lançamento na loja de apps.
* Isso pode causar confusão quando o `versionName` e o `versionCode` do seu app ficam dessincronizados, especialmente porque ambos os campos podem ser visualizados no dashboard da Braze. Como boa prática, verifique se o `versionName` e o `versionCode` do seu app são incrementados juntos.
* Se você precisar filtrar pelo campo legível `versionName` (incomum), use o filtro App Version Name.

#### Requisitos do SDK {#sdk-requirements}

Os valores para este filtro são coletados a partir do SDK da Braze para Android v3.6.0+ e SDK para iOS v3.21.0+. Mesmo que este filtro tenha requisitos de SDK, você ainda poderá direcionar usuários que estão em versões mais antigas do seu app usando este recurso!

Para Android, este número de versão é baseado no [Package Long Version Code](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) do app.

Para iOS, este número de versão é baseado na [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) do app.

{% alert tip %}
Este filtro preencherá os valores após os usuários atualizarem seus apps para as versões do SDK da Braze compatíveis. Até lá, o filtro não mostrará nenhuma versão quando selecionado.
{% endalert %}

#### Caso de uso {#use-case}

No cenário a seguir, vamos supor que você fez o upgrade para os SDKs da Braze que suportam este filtro na versão `2.0.0` do seu app.

Assim que a Braze receber dados da versão 2.0.0 do seu app, você poderá direcionar usuários com versões anteriores ou posteriores.

| Filtro  | Versão do app do usuário  | Resultado |
| :------------- | :----------- | :--------- |
| Menor que 2.0.0 | 1.0.0 | O usuário está no Segment, mesmo que o SDK da Braze não suportasse o filtro "App Version Number". |
| Maior que 2.0.0 | 2.5.1 | O usuário e todas as futuras instalações estarão no Segment. |
| Maior que 2.0.0 | 1.9.9 | O usuário não está no Segment. |
| Menor ou igual a 2.0.0 | 3.0.1 | O usuário não está no Segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Caso de uso" }

### Nome da versão do app {#app-version-name}

Use o filtro "App Version Name" para segmentar usuários pelo nome de build do app visível ao usuário.

Este filtro suporta correspondência com "é", "não é" e expressões regulares. Por exemplo, você pode direcionar usuários que possuem um app que não é a versão "1.2.3-test-build".

Para Android, este nome de versão é baseado no [Package Version Name](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) do app. Para iOS, este nome de versão é baseado na [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) do app.

### Não usou o recurso {#have-not-used-feature}

Quando você lança uma nova versão do app e introduz novos recursos, os usuários podem não perceber o novo conteúdo. Executar uma campanha de divulgação de recursos é uma ótima maneira de ensinar os usuários sobre novos recursos ou recursos que eles nunca usaram. Para isso, você deve criar um [atributo personalizado]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#custom-data) que é atribuído a usuários que nunca concluíram uma determinada ação dentro do seu app, ou usar um [evento personalizado]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#custom-data) para rastrear uma ação específica. Você pode usar esse atributo (ou evento) para segmentar os usuários para os quais deseja enviar a Campaign.

{% alert tip %}
Quer redirecionar uma parte específica do seu público? Confira [Campanhas de redirecionamento]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns) para aprender como redirecionar Campaigns aproveitando as ações anteriores dos seus usuários.
{% endalert %}