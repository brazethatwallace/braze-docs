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
Para uma comparação dos tipos de links em todos os canais de envio de mensagens e orientações sobre quando você precisa de um arquivo AASA, consulte o [Guia de deep linking para iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide/).
{% endalert %}

Os links universais da Apple e os Android App Links são mecanismos criados para proporcionar uma transição fluida entre conteúdo web e apps móveis. Enquanto os links universais são específicos do iOS, os Android App Links servem ao mesmo propósito para aplicativos Android.

## Como os links universais e App Links funcionam {#how-universal-links-and-app-links-work}

Os links universais (iOS) e App Links (Android) são links web padrão (`http://mydomain.com`) que apontam tanto para uma página web quanto para um conteúdo dentro de um app.

Quando um link universal ou App Link é aberto, o sistema operacional verifica se algum app instalado está registrado para aquele domínio. Se um app for encontrado, ele é aberto imediatamente sem carregar a página web. Se nenhum app for encontrado, a URL web é carregada no navegador padrão do usuário, que também pode ser configurado para redirecionar para a App Store ou Google Play Store, respectivamente.

Em termos simples, os links universais permitem que um site associe suas páginas web a telas específicas do app. Assim, quando um usuário clica em um link para uma página web que corresponde a uma tela do app, o app pode ser aberto diretamente (se estiver instalado).

Esta tabela descreve as principais diferenças entre links universais e deep links tradicionais:

|                        | Links universais e App Links                                   | Deep Links                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Compatibilidade de plataforma | iOS (versão 9 e posterior) e Android (versão 6.0 e posterior)  | Usado em vários sistemas operacionais móveis    |
| Finalidade                | Conectar conteúdo web e de app de forma fluida em dispositivos iOS e Android | Vincular a conteúdo específico do app |
| Função               | Direciona para páginas web ou conteúdo do app com base no contexto           | Abre telas específicas do app   |
| Instalação do app       | Abre o app se estiver instalado, caso contrário abre o conteúdo web | Requer que o app esteja instalado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Como os links universais e App Links funcionam" }

## Casos de uso {#use-cases}

Os links universais e App Links são mais comumente usados em campanhas de e-mail, já que os e-mails podem ser abertos e clicados tanto em dispositivos desktop quanto móveis.

Alguns canais não funcionam bem com esses links. Por exemplo, notificações por push, mensagens no app e Content Cards devem usar deep links baseados em esquema (`mydomain://`).

{% alert note %}
Os Android App Links requerem um `IBrazeDeeplinkHandler` personalizado com lógica para tratar links de seus domínios separadamente de outras URLs web. Pode ser mais fácil usar deep links e manter as práticas de vinculação uniformes para canais que não sejam e-mail.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar links universais e App Links:

- Seu site deve ser acessível via HTTPS
- Seu app deve estar disponível na App Store (iOS) ou Google Play Store (Android)

## Configurando links universais e App Links {#setting-up-universal-links-and-app-links}

Para que os apps suportem links universais ou App Links, tanto o iOS quanto o Android exigem que um arquivo especial de permissões seja hospedado no domínio do link. Esse arquivo contém definições de quais apps podem abrir links daquele domínio e, no caso do iOS, quais caminhos esses apps podem abrir:

- **iOS:** Arquivo Apple App Site Association (AASA)
- **Android:** Arquivo Digital Asset Links

Além desse arquivo de permissões, existem definições codificadas de quais domínios de link o app pode abrir, configuradas dentro do próprio app:

- **iOS:** Definido como "Associated Domains" no Xcode
- **Android:** Definido no arquivo `AndroidManifest.xml` do app

Essa associação bidirecional entre domínio e app é necessária para que um link universal ou App Link funcione e impede que qualquer app sequestre links de um domínio específico ou que qualquer domínio abra um app específico.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Estas etapas são adaptadas da documentação para desenvolvedores da Apple. Para saber mais, consulte [Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Etapa 1: Configure os entitlements do seu app {#step-1-configure-your-app-entitlements}

{% alert note %}
[No Xcode 13 e posterior](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/), o Xcode pode gerenciar o provisionamento de entitlements automaticamente. Você provavelmente pode pular para a [etapa&nbsp;1c](#step-1c) e voltar a estas instruções se tiver problemas.
{% endalert %}

#### Etapa 1a: Registre seu app {#step-1a}

1. Acesse developer.apple.com e faça login.
2. Clique em **Certificates, Identifiers & Profiles**.
3. Clique em **Identifiers**.
4. Se você ainda não tiver um App Identifier registrado, clique em + para criar um.
   a. Insira um **Name**. Pode ser qualquer nome que você quiser.
   b. Insira o **Bundle ID**. Você pode encontrar o bundle ID na guia **General** do seu projeto Xcode para o build target correto.

#### Etapa 1b: Ative Associated Domains no seu app identifier {#step-1b-turn-on-associated-domains-in-your-app-identifier}

1. No seu App Identifier existente ou recém-criado, localize a seção **App Services**.
2. Selecione **Associated Domains**.
3. Clique em **Save**.

![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Etapa 1c: Ative Associated Domains no seu projeto Xcode {#step-1c}

Antes de prosseguir, verifique se o seu projeto Xcode tem o mesmo time selecionado que o usado para registrar o App Identifier.

1. No Xcode, acesse a guia **Capabilities** do arquivo do seu projeto.
2. Ative **Associated Domains**.

##### Dica de solução de problemas {#troubleshooting-tip}

Se você vir o erro "An App ID with Identifier 'your-app-id' is not available. Please enter a different string", faça o seguinte:

1. Verifique se o time correto está selecionado.
2. Verifique se o Bundle ID ([etapa 1a](#step-1a)) do seu projeto Xcode corresponde ao usado para registrar o App Identifier.

#### Etapa 1d: Adicione o entitlement de domínio {#step-1d-add-the-domain-entitlement}

Na seção de domínios, adicione a tag de domínio apropriada. Você deve prefixá-la com `applinks:`. Neste caso, você pode ver que adicionamos `applinks:yourdomain.com`.

![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Etapa 1e: Confirme que o arquivo de entitlements está incluído no build {#step-1e-confirm-that-the-entitlements-file-is-included-at-build}

No navegador do projeto, verifique se o novo arquivo de entitlements está selecionado em **Target Membership**.

O Xcode deve gerenciar isso automaticamente.

### Etapa 2: Configure seu site para hospedar o arquivo AASA {#step-2-configure-your-website-to-host-the-aasa-file}

Para associar o domínio do seu site ao seu app nativo no iOS, você precisa hospedar o arquivo Apple App Site Association (AASA) no seu site. Esse arquivo serve como uma forma segura de verificar a propriedade do domínio para o iOS. Antes do iOS 9, os desenvolvedores podiam registrar qualquer esquema de URI para abrir seus apps, sem nenhuma verificação. No entanto, com o AASA, esse processo se tornou muito mais seguro e confiável.

O arquivo AASA contém um objeto JSON com uma lista de apps e os caminhos de URL no domínio que devem ser incluídos ou excluídos como links universais. Aqui está um exemplo de arquivo AASA:

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

- `appID`: Construído combinando o **Team ID** do seu app (acesse `https://developer.apple.com/account/#/membership/` para obter o team ID) e o **Bundle Identifier**. No exemplo acima, "JHGFJHHYX" é o team ID e "com.facebook.ios" é o bundle ID.
- `paths`: Array de strings que especificam quais caminhos são incluídos ou excluídos da associação. Você pode usar `NOT` antes do caminho para desativar caminhos. Neste exemplo, todos os links nesse caminho irão para a web em vez de abrir o app. Você pode usar `*` como curinga para habilitar todos os caminhos em um diretório e `?` para corresponder a um único caractere (como /archives/201?/ para corresponder a todos os números de 2010 a 2019).

{% alert note %}
Essas strings diferenciam maiúsculas de minúsculas, e query strings e identificadores de fragmento são ignorados.
{% endalert %}

### Etapa 3: Hospede o arquivo AASA no seu domínio {#step-3-host-the-aasa-file-on-your-domain}

Quando o arquivo AASA estiver pronto, você pode hospedá-lo no seu domínio em `https://<<yourdomain>>/apple-app-site-association` ou em `https://<<yourdomain>>/.well-known/apple-app-site-association`.

Faça upload do arquivo `apple-app-site-association` para o seu servidor web HTTPS. Você pode colocar o arquivo na raiz do servidor ou no subdiretório `.well-known`. Não adicione `.json` ao nome do arquivo.

{% alert important %}
O iOS só tentará buscar o arquivo AASA por meio de uma conexão segura (HTTPS).
{% endalert %}

Ao hospedar o arquivo AASA, verifique se o arquivo segue estas diretrizes:

- É servido via HTTPS.
- Usa o tipo MIME `application/json`.
- Não excede 128 KB (requisito a partir do iOS 9.3.1)

### Etapa 4: Prepare seu app para lidar com links universais {#step-4-prepare-your-app-to-handle-universal-links}

Quando um usuário toca em um link universal em um dispositivo iOS, o dispositivo abre o app e envia a ele um objeto [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity). O app pode então consultar o objeto NSUserActivity para determinar como foi iniciado.

Para suportar links universais no seu app, siga estas etapas:

1. Adicione um entitlement que especifique os domínios que seu app suporta.
2. Atualize o app delegate para responder adequadamente quando receber o objeto NSUserActivity.

No Xcode, abra a seção **Associated Domains** na guia **Capabilities** e adicione uma entrada para cada domínio que seu app suporta, prefixada com `applinks:`. Por exemplo, `applinks:www.mywebsite.com`.

{% alert note %}
A Apple recomenda limitar essa lista a no máximo 20 a 30 domínios.
{% endalert %}

### Etapa 5: Teste seu link universal {#step-5-test-your-universal-link}

Adicione o link universal a um e-mail e envie-o para um dispositivo de teste. Colar um link universal diretamente no campo de URL do Safari não fará com que o app abra automaticamente. Se você fizer isso, precisará puxar manualmente a página para baixo para que um prompt apareça no topo perguntando se deseja abrir o respectivo app.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Estas etapas são adaptadas da documentação para desenvolvedores Android. Para saber mais, consulte [Add Android App Links](https://developer.android.com/training/app-links#add-app-links) e [Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Os Android App Links requerem um `IBrazeDeeplinkHandler` personalizado com lógica para tratar links de seus domínios separadamente de outras URLs web. Pode ser mais fácil usar deep links e manter as práticas de vinculação uniformes para canais que não sejam e-mail.
{% endalert %}

### Etapa 1: Crie deep links {#step-1-create-deep-links}

Primeiro, você precisa criar deep links para o seu app Android. Isso pode ser feito adicionando [intent filters](https://developer.android.com/guide/components/intents-filters) no seu arquivo `AndroidManifest.xml`. O intent filter deve incluir a ação `VIEW` e a categoria `BROWSABLE`, junto com a URL do seu site no elemento de dados.

### Etapa 2: Associe seu app ao seu site {#step-2-associate-your-app-with-your-website}

Você precisa associar seu app ao seu site. Isso pode ser feito criando um arquivo Digital Asset Links. Esse arquivo deve estar no formato JSON e incluir detalhes sobre os apps Android que podem abrir links para o seu site. Ele deve ser colocado no diretório `.well-known` do seu site.

### Etapa 3: Atualize o arquivo de manifesto do seu app {#step-3-update-your-app-manifest-file}

No seu arquivo `AndroidManifest.xml`, adicione um elemento meta-data dentro do elemento application. O elemento meta-data deve ter um atributo `android:name` com o valor "asset_statements" e um atributo `android:resource` que aponte para um arquivo de recurso com um array de strings que inclua a URL do seu site.

### Etapa 4: Prepare seu app para lidar com deep links {#step-4-prepare-your-app-to-handle-deep-links}

No seu app Android, você precisa tratar os deep links recebidos. Você pode fazer isso obtendo o intent que iniciou sua activity e extraindo os dados dele.

### Etapa 5: Teste seus deep links {#step-5-testing-your-deep-links}

Por fim, você pode testar seus deep links. Envie um link para si mesmo por meio de um app de mensagens ou e-mail e clique nele. Se tudo estiver configurado corretamente, o app deverá ser aberto.

{% endtab %}
{% endtabs %}

## Links universais, App Links e rastreamento de cliques {#universal-links-app-links-and-click-tracking}

{% alert note %}
Os links de rastreamento de cliques geralmente são configurados como parte da sua integração de e-mail. Se isso não foi concluído durante a integração do cliente, entre em contato com o seu gerente de conta para obter ajuda.
{% endalert %}

Nossos parceiros de envio de e-mail usam domínios de rastreamento de cliques para encapsular todos os links e incluir parâmetros de URL para rastreamento de cliques nos e-mails da Braze.

Por exemplo, um link como `https://www.example.com` se torna algo como `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Para permitir que links de e-mail com rastreamento de cliques funcionem como links universais ou App Links, você precisará realizar algumas configurações adicionais. Certifique-se de adicionar o domínio de rastreamento de cliques (`links.email.example.com`) como um domínio que o app pode abrir. Além disso, o domínio de rastreamento de cliques deve servir os arquivos AASA (iOS) ou Digital Asset Links (Android). Isso ajudará a garantir que os links de e-mail com rastreamento de cliques funcionem perfeitamente.

Se você não quiser que todos os links de rastreamento de cliques sejam links universais ou App Links, pode especificar quais links devem ser links universais com base no parceiro de envio de e-mail. Consulte as guias a seguir para mais detalhes.

{% tabs %}
{% tab SendGrid %}

Para tratar um link de rastreamento de cliques do SendGrid como um link universal:

1. Configure os valores de pathPrefix do AASA ou AndroidManifest para tratar apenas links com `/uni/` no caminho da URL como links universais.
2. Adicione o atributo `universal="true"` à tag âncora (`<a>`) do seu link. Isso altera o caminho da URL do link encapsulado para incluir `/uni/`.

{% alert note %}
Para e-mails AMP, esse atributo deve ser data-universal="true".
{% endalert %}

Por exemplo:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3. Certifique-se de que seu app está configurado para tratar os links encapsulados corretamente. Consulte o artigo do SendGrid sobre [Resolving SendGrid Click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) e siga as etapas para o seu sistema operacional. Este artigo contém código de exemplo para [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) e [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Com essa configuração, links com `/uni/` no caminho da URL funcionarão como links universais, enquanto todos os outros links funcionarão como links web.

{% endtab %}
{% tab SparkPost %}

Para tratar um link de rastreamento de cliques do SparkPost como um link universal, adicione o seguinte atributo à seção de atributos do editor de arrastar e soltar para e-mail, ou edite manualmente o HTML do link para incluir o seguinte atributo na tag âncora do seu link: `data-msys-sublink="custom_path"`.

Esse caminho personalizado permite que você trate seletivamente URLs com esse valor como um link universal.

Por exemplo:

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Em seguida, certifique-se de que seu app está configurado para tratar o caminho personalizado corretamente. Consulte o artigo do SparkPost sobre [Using SparkPost click tracking on deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). Este artigo contém código de exemplo para [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) e [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

{% endtab %}
{% tab Amazon SES %}

Use caminhos personalizados para adicionar segmentos de caminho às URLs de rastreamento de cliques de e-mail. Isso cria padrões de URL previsíveis que os sistemas operacionais móveis podem reconhecer para links universais e App Links.

Quando os usuários tocam em links de e-mail em dispositivos móveis, os caminhos personalizados ajudam a controlar se os links abrem no app móvel principal, em um app especializado ou no navegador móvel (por exemplo, páginas de produtos, programas de fidelidade, links de cancelamento de inscrição ou páginas legais).

Para tratar um link de rastreamento de cliques do Amazon SES como um link universal ou App Link:

1. Adicione atributos `ses:custom-path` às suas tags âncora no HTML do e-mail, ou adicione o atributo na seção **Atributos** do editor de arrastar e soltar para e-mail. O caminho personalizado é inserido na URL de rastreamento de cliques encapsulada.

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

Certifique-se de que seus caminhos personalizados seguem estes requisitos:

- **Formato:** Apenas caracteres alfanuméricos, pontos, underscores e hifens
- **Comprimento:** 1 a 32 caracteres
- **Diferenciação de maiúsculas e minúsculas:** Os caminhos diferenciam maiúsculas de minúsculas para atender aos requisitos do sistema operacional móvel

{:start="2"}
2. Confirme que suas URLs de rastreamento encapsuladas incluem o segmento de caminho personalizado. Os links seguem este formato: `track.yourstore.com/L1/{customPath}/...`

Por exemplo:

- `track.yourstore.com/L1/shop/...`
- `track.yourstore.com/L1/rewards/...`

{:start="3"}
3. Configure seus arquivos de associação de site no domínio de rastreamento de cliques para que os caminhos correspondam a `/L1/{customPath}/`.

**iOS (Apple App Site Association):**

```json
{
  "applinks": {
    "apps": [],
    "details": [{
      "appID": "TEAMID.com.yourcompany.mainapp",
      "paths": ["/L1/shop/*", "/L1/rewards/*"]
    }, {
      "appID": "TEAMID.com.yourcompany.limitedapp",
      "paths": ["/L1/limited/*"]
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
  },
  "include": ["/L1/shop/*", "/L1/rewards/*"]
}]
```

Certifique-se de que seu app está configurado para tratar esses links encapsulados. Adicione o domínio de rastreamento de cliques aos domínios associados do seu app (iOS) ou intent filters (Android), e hospede o arquivo AASA ou Digital Asset Links nesse domínio conforme descrito anteriormente neste artigo.

{% endtab %}
{% endtabs %}

### Desativando o rastreamento de cliques link a link {#turning-off-click-tracking-on-a-link-to-link-basis}

Você pode desativar o rastreamento de cliques para links específicos adicionando código HTML à sua mensagem de e-mail no editor de HTML ou a um bloco HTML no editor de arrastar e soltar.

#### SendGrid

Se o seu prestador de serviço de e-mail for o SendGrid, use o código HTML `clicktracking=off` assim:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost

Se o seu prestador de serviço de e-mail for o SparkPost, use o código HTML `data-msys-clicktrack="0"` assim:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

Se o seu prestador de serviço de e-mail for o Amazon SES, use o código HTML `ses:no-track` assim:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### Editor de arrastar e soltar {#drag-and-drop-editor}

Ao usar o editor de arrastar e soltar para e-mail, insira seu código HTML como um atributo personalizado se o link estiver vinculado a um texto, botão ou imagem.

##### Atributo personalizado para um link de texto {#custom-attribute-for-a-text-link}

#### SendGrid

Selecione o seguinte para o atributo personalizado:

- **Name:** `clicktracking`
- **Value:** `off`

#### SparkPost

Selecione o seguinte para o atributo personalizado:

- **Name:** `data-msys-clicktrack`
- **Value:** `0`

![Um atributo personalizado para um link de texto.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### Atributo personalizado para um botão ou imagem {#custom-attribute-for-a-button-or-image}

#### SendGrid

Selecione o seguinte para o atributo personalizado:

- **Name:** `clicktracking`
- **Value:** `off`
- **Type:** Link

#### SparkPost

Selecione o seguinte para o atributo personalizado:

- **Name:** `data-msys-clicktrack`
- **Value:** `0`
- **Type:** Link

![Um atributo personalizado para um botão.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Solução de problemas de links universais com rastreamento de cliques {#troubleshooting-universal-links-with-click-tracking}

Se seus links universais não estiverem funcionando como esperado nos seus e-mails, como navegar o destinatário do app de e-mail para o navegador web antes de finalmente redirecionar para o app, consulte estas dicas para solucionar problemas na configuração do seu link universal.

#### O Outlook mostra `[?it=` ou texto de URL bruto em vez de um botão {#outlook-shows-it-or-raw-url-text-instead-of-a-button}

O Outlook pode exibir texto de call-to-action como `[?it=` ou imprimir parte do `href` quando um link não usa um esquema de URL **`http://` ou `https://`** válido. Esquemas personalizados, esquemas ausentes ou URLs malformadas não são tratados como hiperlinks, então o cliente exibe o texto do atributo. Confirme que cada botão, link de imagem e URL rastreada usa um destino completo `https://` (ou `http://`). Isso se aplica tanto a links universais quanto a links web padrão.

#### Verifique a localização do arquivo de link {#verify-link-file-location}

Certifique-se de que o arquivo AASA (iOS) ou Digital Asset Links (Android) está localizado no lugar correto:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

É importante garantir que esses arquivos estejam sempre acessíveis publicamente. Se você não conseguir acessá-los, pode ter pulado uma etapa na configuração dos links universais para e-mail.

#### Verifique as definições de domínio {#verify-domain-definitions}

Certifique-se de que você tem as definições corretas para os domínios que seu app pode abrir.

- **iOS:** Revise os Associated Domains configurados no Xcode para o seu app ([Etapa 1c: Ative Associated Domains no seu projeto Xcode]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/?tab=ios#step-1c)). Verifique se o domínio de rastreamento de cliques está incluído nessa lista.
- **Android:** Abra a página de informações do app (pressione e segure o ícone do app e clique em ⓘ). No menu de informações do app, localize **Abrir por padrão** e toque nessa opção. Isso deve mostrar uma tela com todos os links verificados que o app pode abrir. Verifique se o domínio de rastreamento de cliques está incluído nessa lista.

#### O domínio de rastreamento não consegue servir arquivos .well-known {#tracking-domain-cant-serve-well-known-files}

Em alguns casos, o seu domínio de rastreamento de cliques pode não conseguir hospedar os arquivos `.well-known` necessários devido a limitações do ESP ou restrições de infraestrutura. Se você não conseguir hospedar o arquivo AASA ou Digital Asset Links no seu domínio de rastreamento, considere as seguintes opções:

- **Entre em contato com o seu ESP para hospedar os arquivos no domínio de rastreamento:** Seu subdomínio de rastreamento de cliques normalmente é um CNAME apontando para o seu ESP (SendGrid, SparkPost ou Amazon SES). Como o ESP encerra o tráfego para esse domínio, ele pode hospedar os arquivos `.well-known` para você. Tanto o SendGrid quanto o SparkPost oferecem suporte a isso. Entre em contato diretamente com o seu ESP para solicitar.
- **Desative seletivamente o rastreamento de cliques em URLs de deep link:** Se o seu ESP não puder hospedar os arquivos, você pode desativar o rastreamento de cliques para links universais específicos para que eles apontem diretamente para o seu domínio principal (onde você pode hospedar o arquivo AASA ou Digital Asset Links). Observe que esse método pode causar perda de análise de dados de cliques para esses links específicos. Consulte [Desativando o rastreamento de cliques link a link](#turning-off-click-tracking-on-a-link-to-link-basis) para instruções.
- **Coloque um CDN na frente do subdomínio de rastreamento:** Se você precisar de cobertura completa de rastreamento de cliques e deep linking, pode colocar um CDN (como Cloudflare ou CloudFront) na frente do seu subdomínio de rastreamento. Configure o CDN para servir os arquivos `.well-known` localmente e encaminhar todo o restante do tráfego para o seu ESP. Essa abordagem é mais complexa, mas oferece controle total sobre o rastreamento de cliques e os links universais.