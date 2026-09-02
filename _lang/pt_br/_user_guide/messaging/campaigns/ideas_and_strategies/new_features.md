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

## Filtragem pelas versões mais recentes do app {#filtering-by-most-recent-app-versions}

Os SDKs da Braze rastreiam automaticamente a versão mais recente do app de um usuário. Essas versões podem ser usadas em filtros e Segments para determinar quais usuários devem receber uma mensagem ou Campaign.

![O painel de opções de direcionamento na etapa Direcionar Usuários no fluxo de criação de Campaign. A seção Filtros Adicionais inclui o seguinte filtro: "Número da versão mais recente do app para Android Stopwatch (Android) é inferior a 3.7.0 (134.0.0.0)".]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
Pode levar algum tempo para que as versões atuais do app sejam preenchidas. A versão do app no perfil de usuário é atualizada quando a informação é capturada pelo SDK or kit de desenvolvimento de software, o que depende de quando os usuários abrem seus apps. Se o usuário não abrir o app, a versão atual não será atualizada. <br><br> Esses filtros também não se aplicam retroativamente. É recomendável usar "maior que" ou "igual a" para versões atuais e futuras, mas usar filtros de versões anteriores pode causar comportamentos inesperados.
{% endalert %}

### Número da versão do app {#app-version-number}

Use o filtro **Número da Versão do App** para segmentar usuários pela versão e número de build do app.

Esse filtro suporta comparações numéricas para direcionar uma faixa de versões do app. Por exemplo, você pode direcionar usuários cujo app é "menor que", "maior que" e "igual a" a versão do app "1.2.3", o que pode ser útil para promover um novo recurso que exige um upgrade do app.

Esse filtro pode substituir o filtro legado "Nome da Versão do App", que exigia listar explicitamente cada versão anterior ou usar uma expressão regular.

#### Como funciona {#how-it-works}

- Cada parte da versão `major.minor.patch` enviada na versão do app é comparada como números inteiros
- Se os números principais forem iguais, a Braze compara os números secundários. Se os números secundários forem iguais, a Braze compara os números de patch.
- Ao usar filtros "menor que" ou "menor ou igual a", se a versão do app não existir no perfil de um usuário, o filtro retorna `true` e o usuário é tratado como tendo uma versão mais antiga que a versão testada. Para evitar incluir usuários sem dados de versão, use filtros "maior que" ou "igual a".

#### Considerações importantes {#important-considerations}

- Apps Android possuem tanto um [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) legível por humanos quanto um [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) interno. O filtro Número da Versão do App usa o `versionCode` porque ele é garantidamente incrementado a cada lançamento na loja de apps.
- Isso pode causar confusão quando o `versionName` e o `versionCode` do seu app ficam fora de sincronia, especialmente porque ambos os campos podem ser visualizados no dashboard da Braze. Como boa prática, verifique se o `versionName` e o `versionCode` do seu app são incrementados juntos.
- Se você precisar filtrar pelo campo legível `versionName` (incomum), use o filtro Nome da Versão do App.

#### Requisitos do SDK or kit de desenvolvimento de software {#sdk-requirements}

Os valores para esse filtro são coletados a partir do SDK or kit de desenvolvimento de software da Braze para Android v3.6.0+ e SDK or kit de desenvolvimento de software para iOS v3.21.0+. Embora esse filtro tenha requisitos de SDK or kit de desenvolvimento de software, você ainda pode direcionar usuários que estão em versões mais antigas do seu app usando esse recurso.

Para Android, esse número de versão é baseado no [Package Long Version Code](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) do app.

Para iOS, esse número de versão é baseado na [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) do app.

{% alert tip %}
Esse filtro preenche os valores depois que os usuários fazem upgrade dos seus apps para as versões compatíveis do SDK or kit de desenvolvimento de software da Braze. Até lá, o filtro não mostra nenhuma versão quando selecionado.
{% endalert %}

#### Caso de uso {#use-case}

No cenário a seguir, vamos supor que você fez o primeiro upgrade para os SDKs da Braze que suportam esse filtro na versão `2.0.0` do seu app.

Assim que a Braze receber dados da versão 2.0.0 do seu app, você pode direcionar usuários com versões anteriores ou posteriores.

| Filtro  | Versão do app do usuário  | Resultado |
| :------------- | :----------- | :--------- |
| Menor que 2.0.0 | 1.0.0 | O usuário está no Segment or segmento, mesmo que o SDK or kit de desenvolvimento de software da Braze não suportasse o filtro "Número da Versão do App". |
| Maior que 2.0.0 | 2.5.1 | O usuário e todas as futuras instalações estão no Segment or segmento. |
| Maior que 2.0.0 | 1.9.9 | O usuário não está no Segment or segmento. |
| Menor ou igual a 2.0.0 | 3.0.1 | O usuário não está no Segment or segmento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Caso de uso" }

### Nome da versão do app {#app-version-name}

Use o filtro "Nome da Versão do App" para segmentar usuários pelo "nome de build" voltado ao usuário do app.

Esse filtro suporta correspondência com "é", "não é" e expressões regulares. Por exemplo, você pode direcionar usuários que possuem um app que não é a versão "1.2.3-test-build".

Para Android, esse nome de versão é baseado no [Package Version Name](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) do app. Para iOS, esse nome de versão é baseado na [Short Version String](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) do app.

### Recurso não utilizado {#have-not-used-feature}

Quando você lança uma nova versão do app e introduz novos recursos, os usuários podem não perceber o novo conteúdo. Executar uma Campaign de conscientização de recursos é uma ótima maneira de ensinar os usuários sobre novos recursos ou recursos que eles nunca usaram. Para isso, você deve criar um [atributo personalizado]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) que é atribuído a usuários que nunca completaram uma determinada ação dentro do seu app ou usar um [evento personalizado]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) para rastrear uma ação específica. Você pode usar esse atributo (ou evento) para segmentar os usuários para os quais deseja enviar a Campaign.

{% alert tip %}
Quer redirecionar uma parte específica do seu público? Confira [Campaigns de redirecionamento]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns) para aprender como redirecionar Campaigns aproveitando as ações anteriores dos seus usuários.
{% endalert %}