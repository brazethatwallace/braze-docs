---
nav_title: "Links universais e App Links"
article_title: "Links universais e App Links"
page_order: 6.4
page_type: reference
description: "Este artigo descreve como configurar links universais da Apple e Android App Links."
channel: email
---

# Links universais e App Links {#universal-links-and-app-links}

> Este artigo descreve como configurar links universais da Apple e Android App Links.

{% alert tip %}
Para uma comparação dos tipos de links em todos os canais de envio de mensagens e orientações sobre quando você precisa de um arquivo AASA, consulte o [Guia de deep linking para iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide).
{% endalert %}

Os links universais da Apple e os Android App Links são mecanismos criados para proporcionar uma transição fluida entre conteúdo web e apps móveis. Enquanto os links universais são específicos do iOS, os Android App Links servem ao mesmo propósito para aplicativos Android.

## Como os links universais e os App Links funcionam {#how-universal-links-and-app-links-work}

Links universais (iOS) e App Links (Android) são links da web padrão (`http://mydomain.com`) que apontam tanto para uma página da web quanto para um conteúdo dentro de um app.

Quando um link universal ou App Link é aberto, o sistema operacional verifica se algum app instalado está registrado para aquele domínio. Se um app for encontrado, ele é aberto imediatamente, sem nunca carregar a página da web. Se nenhum app for encontrado, a URL da web é carregada no navegador web padrão do usuário, que também pode estar configurado para redirecionar para a App Store ou Google Play Store, respectivamente.

Em termos simples, os links universais permitem que um website associe suas páginas da web a telas específicas do app. Então, quando um usuário clica em um link para uma página da web que corresponde a uma tela do app, o app pode ser aberto diretamente (se estiver instalado no momento).

{% alert important %}
O Firebase Dynamic Links foi descontinuado. A Braze não tem uma integração direta com o Firebase, e o deep linking é gerenciado fora da plataforma Braze. Migre para soluções nativas da plataforma (links universais da Apple e Android App Links, conforme descrito neste artigo) ou para provedores alternativos de serviços de deep linking. Para orientações sobre migração, consulte as [Perguntas frequentes sobre migração do Firebase](https://firebase.google.com/support/dynamic-links-faq).
{% endalert %}

Esta tabela descreve as principais diferenças entre links universais e deep links tradicionais:

|                        | Links universais e App Links                                   | Deep links                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Compatibilidade de plataforma | iOS (versão 9 e posterior) e Android (versão 6.0 e posterior)  | Usado em diversos sistemas operacionais móveis    |
| Finalidade             | Conectar conteúdo da web e do app de forma integrada em dispositivos iOS e Android | Direcionar para conteúdo específico do app |
| Função                 | Direciona para páginas da web ou conteúdo do app com base no contexto           | Abre telas específicas do app   |
| Instalação do app      | Abre o app se ele estiver instalado; caso contrário, abre o conteúdo da web | Requer que o app esteja instalado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como os links universais e os App Links funcionam" }

## Casos de uso {#use-cases}

Links universais e App Links são mais comumente usados em Campaigns de e-mail, já que os e-mails podem ser abertos e clicados tanto em dispositivos desktop quanto em dispositivos móveis.

Alguns canais não funcionam bem com esses links. Por exemplo, notificações por push, mensagens no app e Content Cards devem usar deep links baseados em esquema (`mydomain://`).

{% alert note %}
Os Android App Links exigem um `IBrazeDeeplinkHandler` personalizado com lógica para tratar links de seus domínios separadamente de outras URLs da web. Pode ser mais fácil usar deep links e manter práticas de vinculação uniformes para canais diferentes de e-mail.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar links universais e App Links:

- Seu website deve ser acessível via HTTPS
- Seu app deve estar disponível na App Store (iOS) ou Google Play Store (Android)

## Configuração de links universais e App Links {#setting-up-universal-links-and-app-links}

Para que os apps ofereçam suporte a links universais ou App Links, tanto iOS quanto Android exigem que um arquivo de permissões especial seja hospedado no domínio do link. Esse arquivo contém definições de quais apps podem abrir links daquele domínio e, no caso do iOS, quais caminhos esses apps têm permissão para abrir:

- **iOS:** Arquivo Apple App Site Association (AASA)
- **Android:** Arquivo Digital Asset Links

Além desse arquivo de permissões, existem definições codificadas de quais domínios de links o app tem permissão para abrir, configuradas dentro do próprio app:

- **iOS:** Definidos como "Associated Domains" no Xcode
- **Android:** Definidos no arquivo `AndroidManifest.xml` do app

Essa associação bidirecional entre domínio e app é necessária para que um link universal ou App Link funcione, impedindo que qualquer app se apodere de links de um domínio específico ou que qualquer domínio abra um app específico.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Essas etapas foram adaptadas da documentação do desenvolvedor Apple. Para saber mais, consulte [Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Etapa 1: Configure as permissões do seu app {#step-1-configure-your-app-entitlements}

{% alert note %}
[No Xcode 13 e versões posteriores](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/), o Xcode pode lidar com o provisionamento de permissões automaticamente. Você provavelmente pode pular para a [etapa&nbsp;1c](#step-1c) e consultar estas instruções se tiver problemas.
{% endalert %}

#### Etapa 1a: Registre seu app {#step-1a}

1. Acesse developer.apple.com e faça login.
2. Clique em **Certificates, Identifiers & Profiles**.
3. Clique em **Identifiers**.
4. Se você ainda não tiver um App Identifier registrado, clique em + para criar um.
   a. Insira um **Name**. Pode ser o que você quiser.
   b. Insira o **Bundle ID**. Você pode encontrar o Bundle ID na guia **General** do seu projeto no Xcode para o build target correto.

#### Etapa 1b: Ative os Associated Domains no identificador do seu app {#step-1b-turn-on-associated-domains-in-your-app-identifier}

1. No App Identifier existente ou recém-criado, localize a seção **App Services**.
2. Selecione **Associated Domains**.
3. Clique em **Save**.

![Seção App Services]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Etapa 1c: Ative os Associated Domains no seu projeto Xcode {#step-1c}

Antes de prosseguir, verifique se o seu projeto Xcode tem o mesmo time selecionado em que você acabou de registrar o App Identifier.

1. No Xcode, acesse a guia **Capabilities** do arquivo do seu projeto.
2. Ative **Associated Domains**.

##### Dica de solução de problemas {#troubleshooting-tip}

Se você vir o erro "An App ID with Identifier 'your-app-id' is not available. Please enter a different string", faça o seguinte:

1. Verifique se o time correto está selecionado.
2. Verifique se o Bundle ID ([etapa 1a](#step-1a)) do seu projeto Xcode corresponde ao usado para registrar o App Identifier.

#### Etapa 1d: Adicione a permissão do domínio {#step-1d-add-the-domain-entitlement}

Na seção de domínios, adicione a tag de domínio apropriada. Você deve prefixá-la com `applinks:`. Neste caso, você pode ver que adicionamos `applinks:yourdomain.com`.

![Seção Associated Domains]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Etapa 1e: Confirme que o arquivo de permissões está incluído na compilação {#step-1e-confirm-that-the-entitlements-file-is-included-at-build}

No navegador do projeto, verifique se o novo arquivo de permissões está selecionado em **Target Membership**.

O Xcode deve fazer isso automaticamente.

### Etapa 2: Configure seu website para hospedar o arquivo AASA {#step-2-configure-your-website-to-host-the-aasa-file}

Para associar o domínio do seu website ao seu app nativo no iOS, você precisa hospedar o arquivo Apple App Site Association (AASA) no seu website. Esse arquivo funciona como uma maneira segura de verificar a propriedade do domínio para o iOS. Antes do iOS 9, os desenvolvedores podiam registrar qualquer esquema de URI para abrir seus apps, sem nenhuma verificação. No entanto, com o AASA, esse processo se tornou muito mais seguro e confiável.

O arquivo AASA contém um objeto JSON com uma lista de apps e os caminhos de URL no domínio que devem ser incluídos ou excluídos como links universais. Veja um exemplo de arquivo AASA:

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": "JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID`: Construído combinando o **Team ID** do seu app (acesse `https://developer.apple.com/account/#/membership/` para obter o Team ID) e o **Bundle Identifier**. Neste exemplo, "JHGFJHHYX" é o Team ID e "com.facebook.ios" é o Bundle ID.
- `paths`: Array de strings que especificam quais caminhos são incluídos ou excluídos da associação. Você pode usar `NOT` antes do caminho para desativar caminhos. Neste exemplo, todos os links nesse caminho irão para a web em vez de abrir o app. Você pode usar `*` como caractere curinga para ativar todos os caminhos em um diretório e `?` para corresponder a um único caractere (como /archives/201?/ para corresponder a todos os números de 2010 a 2019).

{% alert note %}
Essas strings diferenciam maiúsculas de minúsculas, e query strings e identificadores de fragmento são ignorados.
{% endalert %}

### Etapa 3: Hospede o arquivo AASA no seu domínio {#step-3-host-the-aasa-file-on-your-domain}

Quando o arquivo AASA estiver pronto, você pode hospedá-lo no seu domínio em `https://<<yourdomain>>/apple-app-site-association` ou em `https://<<yourdomain>>/.well-known/apple-app-site-association`.

Faça o upload do arquivo `apple-app-site-association` para o seu servidor web HTTPS. Você pode colocar o arquivo na raiz do servidor ou no subdiretório `.well-known`. Não adicione `.json` ao nome do arquivo.

{% alert important %}
O iOS só tentará buscar o arquivo AASA por meio de uma conexão segura (HTTPS).
{% endalert %}

Ao hospedar o arquivo AASA, verifique se o arquivo segue estas diretrizes:

- É servido via HTTPS.
- Usa o tipo MIME `application/json`.
- Não excede 128 KB (requisito a partir do iOS 9.3.1)

### Etapa 4: Prepare seu app para lidar com links universais {#step-4-prepare-your-app-to-handle-universal-links}

Quando um usuário toca em um link universal em um dispositivo iOS, o dispositivo inicia o app e envia a ele um objeto [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity). O app pode então consultar o objeto NSUserActivity para determinar como foi iniciado.

Para oferecer suporte a links universais no seu app, siga estas etapas:

1. Adicione uma permissão que especifique os domínios com os quais seu app é compatível.
2. Atualize o app delegate para responder adequadamente quando receber o objeto NSUserActivity.

No Xcode, abra a seção **Associated Domains** na guia **Capabilities** e adicione uma entrada para cada domínio com o qual seu app é compatível, prefixado com `applinks:`. Por exemplo, `applinks:www.mywebsite.com`.

{% alert note %}
A Apple recomenda limitar essa lista a no máximo 20 a 30 domínios.
{% endalert %}

### Etapa 5: Teste seu link universal {#step-5-test-your-universal-link}

Adicione o link universal a um e-mail e envie-o para um dispositivo de teste. Colar um link universal diretamente no campo de URL do Safari não fará com que o app abra automaticamente. Se você fizer isso, terá que puxar manualmente o website para baixo para que um prompt apareça no topo perguntando se deseja abrir o app correspondente.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Essas etapas foram adaptadas da documentação do desenvolvedor Android. Para saber mais, consulte [Add Android App Links](https://developer.android.com/training/app-links#add-app-links) e [Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Os Android App Links exigem um `IBrazeDeeplinkHandler` personalizado com lógica para lidar com links de seus domínios separadamente de outras URLs da web. Pode ser mais fácil usar deep links e manter as práticas de vinculação uniformes para canais que não sejam e-mail.
{% endalert %}

### Etapa 1: Crie deep links {#step-1-create-deep-links}

Primeiro, você precisa criar deep links para o seu app Android. Isso pode ser feito adicionando [intent filters](https://developer.android.com/guide/components/intents-filters) no arquivo `AndroidManifest.xml`. O intent filter deve incluir a ação `VIEW` e a categoria `BROWSABLE`, junto com a URL do seu website no elemento de dados.

### Etapa 2: Associe seu app ao seu website {#step-2-associate-your-app-with-your-website}

Você precisa associar seu app ao seu website. Isso pode ser feito criando um arquivo Digital Asset Links. Esse arquivo deve estar no formato JSON e inclui detalhes sobre os apps Android que podem abrir links para o seu website. Ele deve ser colocado no diretório `.well-known` do seu website.

### Etapa 3: Atualize o arquivo de manifesto do seu app {#step-3-update-your-app-manifest-file}

No arquivo `AndroidManifest.xml`, adicione um elemento meta-data dentro do elemento application. O elemento meta-data deve ter um atributo `android:name` com valor "asset_statements" e um atributo `android:resource` que aponte para um arquivo de recurso com um array de strings que inclua a URL do seu website.

### Etapa 4: Prepare seu app para lidar com deep links {#step-4-prepare-your-app-to-handle-deep-links}

No seu app Android, você precisa lidar com os deep links recebidos. Isso pode ser feito obtendo o intent que iniciou sua activity e extraindo os dados dele.

### Etapa 5: Testando seus deep links {#step-5-testing-your-deep-links}

Por fim, você pode testar seus deep links. Envie um link para si mesmo por meio de um app de envio de mensagens ou e-mail e clique nele. Se tudo estiver configurado corretamente, o app deve ser aberto.

{% endtab %}
{% endtabs %}

## Links universais, App Links e rastreamento de cliques {#universal-links-app-links-and-click-tracking}

{% alert note %}
Os links de rastreamento de cliques geralmente são configurados como parte da sua integração para e-mail. Se isso não foi concluído durante a integração do cliente, entre em contato com o gerente da sua conta para obter ajuda.
{% endalert %}

Nossos parceiros de envio de e-mail usam domínios de rastreamento de cliques para envolver todos os links e incluir parâmetros de URL para rastreamento de cliques em e-mails da Braze.

Por exemplo, um link como `https://www.example.com` se torna algo como `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Para permitir que links de e-mail com rastreamento de cliques funcionem como links universais ou App Links, você precisará realizar algumas configurações adicionais. Certifique-se de adicionar o domínio de rastreamento de cliques (`links.email.example.com`) como um domínio que o app tem permissão para abrir. Além disso, o domínio de rastreamento de cliques deve servir os arquivos AASA (iOS) ou Digital Asset Links (Android). Isso ajudará a garantir que os links de e-mail com rastreamento de cliques funcionem perfeitamente.

Se você não quiser que todos os links de rastreamento de cliques sejam links universais ou App Links, é possível especificar quais links devem ser links universais com base no parceiro de envio de e-mail. Consulte as guias a seguir para mais detalhes.

{% tabs %}
{% tab SendGrid %}

Para tratar um link de rastreamento de cliques do SendGrid como um link universal:

1. Configure os valores de pathPrefix do AASA ou AndroidManifest para tratar apenas links com `/uni/` no caminho da URL como links universais.
2. Adicione o atributo `universal="true"` à tag âncora (`<a>`) do seu link. Isso altera o caminho da URL do link envolvido para incluir `/uni/`.

{% alert note %}
Para e-mails AMP, esse atributo deve ser data-universal="true".
{% endalert %}

Por exemplo:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3. Certifique-se de que o seu app está configurado para lidar corretamente com os links envolvidos. Consulte o artigo do SendGrid sobre [Resolving SendGrid Click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) e siga as etapas para o seu sistema operacional. Este artigo contém código de exemplo para [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) e [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Com essa configuração, links com `/uni/` no caminho da URL funcionarão como links universais, enquanto todos os outros links funcionarão como links da web.

{% endtab %}
{% tab SparkPost %}

Para tratar um link de rastreamento de cliques do SparkPost como um link universal, adicione o seguinte atributo na seção de Atributos do editor de arrastar e soltar para e-mail, ou edite manualmente o HTML do link para incluir o seguinte atributo na tag âncora do seu link: `data-msys-sublink="custom_path"`.

Esse caminho personalizado permite que você trate seletivamente URLs com esse valor como um link universal.

Por exemplo:

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Em seguida, certifique-se de que o seu app está configurado para lidar corretamente com o caminho personalizado. Consulte o artigo do SparkPost sobre [Using SparkPost click tracking on deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). Este artigo contém código de exemplo para [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) e [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

{% endtab %}
{% tab Amazon SES %}

Use caminhos personalizados para adicionar segmentos de caminho às URLs de rastreamento de cliques de e-mail. Isso cria padrões de URL previsíveis que os sistemas operacionais móveis podem reconhecer para links universais e App Links.

Quando os usuários tocam em links de e-mail em dispositivos móveis, os caminhos personalizados ajudam a controlar se os links abrem no app móvel principal, em um app especializado ou no navegador móvel (por exemplo, páginas de produtos, programas de fidelidade, links de cancelamento de inscrição ou páginas legais).

Para tratar um link de rastreamento de cliques do Amazon SES como um link universal ou App Link:

1. Adicione atributos `ses:custom-path` às suas tags âncora no HTML do e-mail, ou adicione o atributo na seção **Atributos** do editor de arrastar e soltar para e-mail. O caminho personalizado é inserido na URL de rastreamento de cliques envolvida.

Por exemplo:

```html
<!-- Opens main shopping app -->
<a href="https://yourstore.com/product" ses:custom-path="shop">Shop Now</a>
<!-- Opens loyalty app -->
<a href="https://yourstore.com/rewards" ses:custom-path="rewards">My Rewards</a>
<!-- Opens specialized app -->
<a href="https://yourstore.com/limited" ses:custom-path="limited">Limited Edition</a>
<!-- Stays in browser -->
<a href="https://yourstore.com/unsubscribe" ses:no-track>Unsubscribe</a>
```

Certifique-se de que os seus caminhos personalizados seguem estes requisitos:

- **Formato:** Apenas caracteres alfanuméricos, pontos, underscores e hifens
- **Comprimento:** 1 a 32 caracteres
- **Sensibilidade a maiúsculas e minúsculas:** Os caminhos diferenciam maiúsculas de minúsculas para atender aos requisitos do sistema operacional móvel

{:start="2"}
2. Confirme que as suas URLs de rastreamento envolvidas incluem o segmento de caminho personalizado. Sem o atributo, links rastreados usam `track.yourstore.com/CL0/{encodedUrl}/...`. Com o atributo, eles seguem este formato: `track.yourstore.com/CL1/{customPath}/{encodedUrl}/...`

Por exemplo:

- `track.yourstore.com/CL1/shop/...`
- `track.yourstore.com/CL1/rewards/...`

{:start="3"}
3. Configure seus arquivos de associação de site no domínio de rastreamento de cliques para que os caminhos correspondam a `/CL1/{customPath}/`.

**iOS (Apple App Site Association):**

```json
{
  "applinks": {
    "apps": [],
    "details": [{
      "appID": "TEAMID.com.yourcompany.mainapp",
      "paths": ["/CL1/shop/*", "/CL1/rewards/*"]
    }, {
      "appID": "TEAMID.com.yourcompany.limitedapp",
      "paths": ["/CL1/limited/*"]
    }]
  }
}
```

**Android (Digital Asset Links):**

```json
[{
  "relation": ["delegate_permission/common.handle_all_urls"],
  "target": {
    "namespace": "android_app",
    "package_name": "com.yourcompany.mainapp",
    "sha256_cert_fingerprints": ["..."]
  }
}]
```

O Android faz a correspondência de caminhos no seu app, e não no `assetlinks.json`. Defina `android:pathPrefix="/CL1/{customPath}/"` no intent filter do seu `AndroidManifest.xml` para cada caminho personalizado que o seu app manipula.

Certifique-se de que o seu app está configurado para lidar com esses links envolvidos. Adicione o domínio de rastreamento de cliques aos domínios associados do seu app (iOS) ou intent filters (Android), e hospede o arquivo AASA ou Digital Asset Links nesse domínio conforme descrito anteriormente neste artigo.

{% endtab %}
{% endtabs %}

### Desativando o rastreamento de cliques link por link {#turning-off-click-tracking-on-a-link-to-link-basis}

Você pode desativar o rastreamento de cliques para links específicos adicionando código HTML à sua mensagem de e-mail no editor de HTML ou a um bloco HTML no editor de arrastar e soltar.

#### SendGrid

Se o seu provedor de serviços de e-mail é o SendGrid, use o código HTML `clicktracking=off` assim:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost

Se o seu provedor de serviços de e-mail é o SparkPost, use o código HTML `data-msys-clicktrack="0"` assim:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

Se o seu provedor de serviços de e-mail é o Amazon SES, use o código HTML `ses:no-track` assim:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### Editor de arrastar e soltar {#drag-and-drop-editor}

Ao usar o editor de arrastar e soltar de e-mail, insira o código HTML como um atributo personalizado se o link estiver vinculado a um texto, botão ou imagem.

##### Atributo personalizado para um link de texto {#custom-attribute-for-a-text-link}

#### SendGrid

Selecione o seguinte para o atributo personalizado:

- **Nome:** `clicktracking`
- **Valor:** `off`

#### SparkPost

Selecione o seguinte para o atributo personalizado:

- **Nome:** `data-msys-clicktrack`
- **Valor:** `0`

![Um atributo personalizado para um link de texto.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### Atributo personalizado para um botão ou imagem {#custom-attribute-for-a-button-or-image}

#### SendGrid

Selecione o seguinte para o atributo personalizado:

- **Nome:** `clicktracking`
- **Valor:** `off`
- **Tipo:** Link

#### SparkPost

Selecione o seguinte para o atributo personalizado:

- **Nome:** `data-msys-clicktrack`
- **Valor:** `0`
- **Tipo:** Link

![Um atributo personalizado para um botão.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Solução de problemas de links universais com rastreamento de cliques {#troubleshooting-universal-links-with-click-tracking}

Se os seus links universais não estiverem funcionando conforme o esperado nos seus e-mails, como quando o destinatário é direcionado do app de e-mail para o navegador antes de ser redirecionado para o app, consulte estas dicas para solucionar problemas na configuração dos seus links universais.

#### O Outlook mostra `[?it=` ou texto de URL bruto em vez de um botão {#outlook-shows-it-or-raw-url-text-instead-of-a-button}

O Outlook pode exibir texto de chamada para ação como `[?it=` ou exibir parte do `href` quando um link não usa um esquema de URL válido **`http://` ou `https://`**. Esquemas personalizados, esquemas ausentes ou URLs malformadas não são tratados como hiperlinks, então o cliente mostra o texto do atributo. Confirme que cada botão, link de imagem e URL rastreada usa um destino completo `https://` (ou `http://`). Isso se aplica tanto a links universais quanto a links da web padrão.

#### Verifique a localização do arquivo de link {#verify-link-file-location}

Certifique-se de que o arquivo AASA (iOS) ou o arquivo Digital Asset Links (Android) está localizado no lugar correto:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

É importante garantir que esses arquivos estejam sempre acessíveis publicamente. Se você não conseguir acessá-los, pode ter pulado uma etapa na configuração de links universais para e-mail.

#### Verifique as definições de domínio {#verify-domain-definitions}

Certifique-se de que as definições corretas estão configuradas para os domínios que o seu app tem permissão para abrir.

- **iOS:** Revise os Associated Domains configurados no Xcode para o seu app ([Etapa 1c: Ative Associated Domains no seu projeto Xcode]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links?tab=ios#step-1c)). Verifique se o domínio de rastreamento de cliques está incluído nessa lista.
- **Android:** Abra a página de informações do app (pressione e segure o ícone do app e clique em ⓘ). No menu de informações do app, localize **Abrir por padrão** e toque nessa opção. Deve aparecer uma tela com todos os links verificados que o app tem permissão para abrir. Verifique se o domínio de rastreamento de cliques está incluído nessa lista.

#### Todos os links de e-mail abrem o app {#every-email-link-opens-the-app}

Se todos os links de um e-mail abrem o seu app, incluindo links que você espera que abram no navegador, os valores de `paths` do AASA (iOS) ou `pathPrefix` do Android no seu domínio de rastreamento de cliques correspondem ao domínio inteiro (por exemplo, `*` ou `/*`).

Limite esses padrões às URLs que devem abrir o app. Para o SendGrid, faça a correspondência com `/uni/` e adicione `universal="true"` apenas nesses links. Consulte [Links universais, App Links e rastreamento de cliques](#universal-links-app-links-and-click-tracking).

#### O domínio de rastreamento não consegue servir arquivos .well-known {#tracking-domain-cant-serve-well-known-files}

Em alguns casos, o seu domínio de rastreamento de cliques pode não conseguir hospedar os arquivos `.well-known` necessários devido a limitações do provedor de serviços de e-mail ou restrições de infraestrutura. Se você não conseguir hospedar o arquivo AASA ou Digital Asset Links no seu domínio de rastreamento, considere as seguintes opções:

- **Desativar seletivamente o rastreamento de cliques em URLs de deep link:** Você pode desativar o rastreamento de cliques para links universais específicos para que eles vão diretamente ao seu domínio principal (onde é possível hospedar o arquivo AASA ou Digital Asset Links). Observe que este método pode causar perda de análise de dados de cliques para esses links específicos. Consulte [Desativando o rastreamento de cliques link por link](#turning-off-click-tracking-on-a-link-to-link-basis) para instruções.
- **Colocar uma rede de distribuição de conteúdo (CDN) na frente do subdomínio de rastreamento:** Se você precisa de cobertura completa de rastreamento de cliques e deep linking, pode colocar uma CDN (como Cloudflare ou CloudFront) na frente do seu subdomínio de rastreamento. Configure a CDN para servir os arquivos `.well-known` localmente e fazer proxy de todo o restante do tráfego para o seu provedor de serviços de e-mail. Essa abordagem é mais complexa, mas oferece controle total sobre rastreamento de cliques e links universais.

#### Links funcionando em um espaço de trabalho, mas não em outro {#links-working-in-one-workspace-but-not-another}

Se links universais ou App Links funcionam corretamente no seu espaço de trabalho de Produção, mas falham no espaço de trabalho de Desenvolvimento ou Teste, verifique se o domínio do endereço de e-mail de envio corresponde ao domínio de rastreamento configurado nas configurações de e-mail de cada espaço de trabalho. Configurações inconsistentes entre espaços de trabalho podem fazer com que links se comportem de maneira diferente, mesmo usando os mesmos modelos de e-mail e arquivos AASA ou Digital Asset Links.

Para verificar a configuração de e-mail:

1. Acesse **Configurações** > **Preferências de e-mail** no dashboard da Braze.
2. Revise as **Configurações de e-mail de saída** em **Configuração de envio**.
3. Confirme que o domínio de envio e o domínio de rastreamento estão devidamente alinhados para o espaço de trabalho onde os links não estão funcionando.

Se o domínio de envio difere entre espaços de trabalho, certifique-se de que cada espaço de trabalho tenha os registros DNS apropriados configurados e que os arquivos AASA (iOS) ou Digital Asset Links (Android) estejam acessíveis a partir de cada domínio de rastreamento.