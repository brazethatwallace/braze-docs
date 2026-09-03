---
nav_title: SSL na Braze
article_title: SSL na Braze
page_order: 5
page_type: reference
description: "Este artigo de referência aborda o SSL, para que ele é usado e como é usado na Braze."
channel: email
---

# SSL na Braze {#ssl-at-braze}

> Uma camada de soquete seguro (SSL) criptografa uma URL com HTTPS em vez de HTTP. HTTPS indica que um certificado SSL ou TLS válido e confiável existe e que o website é seguro para visitar.

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## Por que o SSL é importante? {#why-is-ssl-important}

A maioria dos domínios não exige SSL, mas a Braze recomenda fortemente o uso de SSL pelos seguintes motivos.

Proteger seu website e links com SSL é uma prática comum, mesmo para empresas que não lidam diretamente com informações sensíveis de clientes. Os usuários confiam mais em links protegidos com SSL, e a camada adicional de autenticação ajuda a proteger seus dados.

### Necessário para rastreamento de cliques e aberturas {#necessary-for-click-and-open-tracking}

A Braze transforma seus links usando seu subdomínio de rastreamento de link de marca para rastrear cliques e aberturas. Por padrão, esses links começam com HTTP. Usuários com navegadores ou extensões que restringem tráfego não seguro podem ter dificuldade em passar pelo redirecionamento antes da URL de destino, mesmo que a URL seja segura. Isso pode causar imagens quebradas e rastreamento impreciso. Aplique SSL ao subdomínio de rastreamento de link para garantir redirecionamentos seguros.

## Requisitos {#requirements}

### Navegador {#browser}

Os principais navegadores, como o Google Chrome, restringem o tráfego por meio de URLs não seguras para proteger os usuários. O uso de SSL ajuda a confirmar que o conteúdo é confiável e minimiza problemas como links e imagens quebrados em e-mails.

### Domínios HSTS {#hsts-domains}

Se você tem um domínio com HTTP Strict Transport Security (HSTS), configure o SSL e uma rede de distribuição de conteúdo (CDN) para enviar os certificados de segurança necessários. Sem SSL, links de imagens e da web deixam de funcionar.

## Adquirir um certificado SSL {#acquire-an-ssl-certificate}

Adquira um certificado SSL por meio de terceiros, geralmente uma rede de distribuição de conteúdo (CDN). Uma CDN hospeda o certificado e o disponibiliza ao navegador quando um usuário clica em um link, redirecionando o tráfego pela CDN para aplicar os certificados antes de enviá-lo ao SendGrid ou SparkPost.

Para iniciar a configuração do SSL, entre em contato com seu gerente de sucesso do cliente da Braze para iniciar uma configuração completa de e-mail da Braze.

Depois que a Braze iniciar a configuração, siga estas etapas:

1. A Braze fornecerá registros DNS para adicionar ao registro do seu domínio.
2. A Braze verificará se os registros foram adicionados corretamente ao seu registro.
3. Em seguida, selecione uma CDN e obtenha certificados SSL de um provedor terceirizado.
4. Neste ponto, configure sua CDN. A Braze não pode ajudar a solucionar problemas de configuração da CDN. Entre em contato com seu provedor de CDN para obter assistência adicional.
5. Entre em contato com seu gerente de sucesso do cliente para ativar o SSL.

## O que é uma CDN e por que preciso de uma? {#what-is-a-cdn-and-why-do-i-need-it}

Uma rede de distribuição de conteúdo (CDN) é uma plataforma de servidores que ajuda a garantir tempos de carregamento rápidos de conteúdo em diversas mídias, além de lidar com certificados de segurança.

{% alert important %}
A configuração da CDN sempre vem depois da validação dos seus registros DNS pela Braze. Se você ainda não iniciou essa etapa, entre em contato com o seu gerente de sucesso do cliente para saber mais sobre como começar.
{% endalert %}

Para rastreamento de cliques e aberturas, os parceiros de entrega transformam os links usando um subdomínio de marca, e a CDN aplica o certificado SSL a esses links transformados. Os parceiros frequentemente precisam apresentar certificados válidos ao navegador do destinatário para que links e imagens sejam exibidos corretamente. Como a Braze não solicita nem gerencia certificados, você precisa configurar isso por meio de uma CDN.

{% alert note %}
Se você não puder ou não quiser usar as CDNs listadas para rastreamento SSL de cliques e aberturas, é possível configurar uma configuração SSL personalizada. CDNs alternativas ou proxies personalizados podem resultar em uma configuração mais complexa. Consulte a documentação do [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) e do [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

### Recursos adicionais {#additional-resources}

{% alert important %}
Para solucionar problemas na configuração da sua CDN, entre em contato com o seu provedor de CDN ou consulte [Solução de problemas]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting) para orientações gerais.
{% endalert %}

Consulte os seguintes recursos dos parceiros de provedor de serviços de e-mail sobre como configurar determinadas CDNs. Embora a sua CDN específica possa não estar listada, você deve garantir que ela tenha a capacidade de aplicar certificados SSL.

Ao configurar o domínio de rastreamento de cliques da sua CDN, ative o cabeçalho `X-Forwarded-Host` para prevenir possíveis problemas de segurança, como ataques de cabeçalho de host. Consulte a documentação da CDN ou a sua equipe de suporte para obter as etapas.

| Parceiro | CDN | Documentação |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [Usando HTTPS com o CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [Introdução ao SSL/TLS](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Configurando TLS com certificados gerenciados pelo Fastly](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [Como configurar SSL personalizado](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Certificados SSL gerenciados pelo Google](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [Como configurar SSL para rastreamento de cliques usando o CloudFront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [Usando o CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Usando o Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [Usando o KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [Guia passo a passo com AWS CloudFront](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Guia passo a passo com Cloudflare](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Guia passo a passo com Fastly](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Guia passo a passo com Google Cloud Platform](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Guia passo a passo com Microsoft Azure](https://docs.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Recursos adicionais" }

### Amazon SES

Se você está usando o Amazon SES como seu provedor de serviços de e-mail, consulte a **Opção 2: Configurando um domínio HTTPS** na [documentação do Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) e especifique o domínio de rastreamento da AWS por região com base no seu cluster Braze:

- **Clusters Braze US:** `r.us-east-1.awstrack.me`
- **Clusters Braze EU:** `r.eu-central-1.awstrack.me`

{% alert important %}
Ao configurar o domínio de rastreamento de cliques da sua CDN, ative o cabeçalho `X-Forwarded-Host` para prevenir possíveis problemas de segurança, como ataques de cabeçalho de host. Consulte o seu provedor de CDN para obter as etapas.
{% endalert %}

## Padrões de URL para rastreamento de cliques e aberturas {#click-and-open-tracking-url-patterns}

Seu provedor de serviços de e-mail (ESP) reescreve cada link rastreado para apontar para o seu domínio de rastreamento de cliques e, em seguida, adiciona um prefixo de caminho que marca a requisição como um clique ou abertura rastreada. A Braze não constrói esses caminhos. Seu ESP os adiciona quando reescreve o link. Para regras de CDN ou proxy, listas de permissão de segurança ou tratamento de links em apps móveis, use a documentação do seu ESP como fonte de referência.

| ESP | Padrões de caminho | Documentação do ESP |
| --- | --- | --- |
| SendGrid | `/wf/click?upn=...` para cliques rastreados e `/uni/wf/click?upn=...` para links que você sinaliza como links universais. Dependendo da sua configuração, links de marca também podem usar `/ls/click` (assinatura longa) ou `/ss/` (encurtado). | [Links universais](https://www.twilio.com/docs/sendgrid/ui/sending-email/universal-links) e [links encurtados](https://support.sendgrid.com/hc/en-us/articles/44375837088795-How-to-Know-if-my-Links-Are-Shortened-by-SendGrid) |
| SparkPost | `/f/` para cliques rastreados e `/q/` para aberturas rastreadas. Links que definem um caminho personalizado `data-msys-sublink` seguem `/f/{custom_path}/`. | [Deep links](https://docs.sparkpost.com/docs/tech-resources/deep-links-self-serve) |
| Amazon SES | `/CL0/{encodedUrl}/{index}/{messageId}/{hmac}` para cliques rastreados. Links que definem o atributo `ses:custom-path` seguem `/CL1/{customPath}/{encodedUrl}/...`. | [Domínios personalizados de abertura e clique](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Padrões de URL de rastreamento de cliques e aberturas por ESP" }

Por exemplo, se o seu domínio de rastreamento de cliques for `clicks.example.com` e o seu ESP for SparkPost, um clique rastreado resolve para uma URL que começa com `https://clicks.example.com/f/`.

{% alert important %}
Seu ESP é o proprietário desses prefixos de caminho e pode alterá-los ou adicionar novos, por isso a Braze não pode garantir uma lista permanente ou exaustiva. Quando suas ferramentas de segurança permitirem, adicione o domínio completo de rastreamento de cliques à lista de permissão em vez de caminhos individuais e confirme os padrões atuais na documentação do seu ESP.
{% endalert %}

Para tratar esses caminhos no seu app móvel, consulte [Links universais e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

## Solução de problemas {#troubleshooting}

Embora a configuração de CDN, certificados e problemas de proxy devam ser tratados diretamente com sua CDN, use estas dicas para identificar problemas comuns de rastreamento de cliques por SSL. Para orientações sobre solução de problemas, consulte [Solução de problemas]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting).