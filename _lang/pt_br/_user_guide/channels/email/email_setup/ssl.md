---
nav_title: SSL na Braze
article_title: Visão geral do SSL
page_order: 5
page_type: reference
description: "Este artigo de referência aborda o SSL, para que ele é usado e como é usado na Braze."
channel: email

---

# SSL na Braze {#ssl-at-braze}

> Uma camada de soquete seguro (SSL) criptografa uma URL com HTTPS em vez de HTTP. HTTPS indica que um certificado SSL ou TLS válido e confiável existe e que o site é seguro para visitar.

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

## Por que o SSL é importante? {#why-is-ssl-important}

A maioria dos domínios não requer SSL, mas a Braze recomenda fortemente o uso de SSL por essas razões.

Proteger seu site e seus links com SSL é uma prática comum, mesmo para empresas que não lidam diretamente com informações confidenciais de clientes. Os usuários confiam mais em links protegidos com SSL, e a camada adicional de autenticação ajuda a proteger seus dados.

### Necessário para rastreamento de cliques e aberturas {#necessary-for-click-and-open-tracking}

A Braze transforma seus links usando seu subdomínio de rastreamento de links da marca para rastrear cliques e aberturas. Por padrão, esses links começam com HTTP. Usuários com navegadores ou extensões que restringem tráfego não seguro podem ter dificuldade em passar pelo redirecionamento antes da URL de destino, mesmo que a URL seja segura. Isso pode causar imagens quebradas e rastreamento impreciso. Aplique SSL ao subdomínio de rastreamento de links para confirmar redirecionamentos seguros.

## Requisitos {#requirements}

### Navegadores {#browser}

Os principais navegadores, como o Google Chrome, restringem o tráfego por URLs não seguras para proteger os usuários. Usar SSL ajuda a confirmar que o conteúdo é confiável e minimiza problemas como links e imagens quebrados em e-mails.

### Domínios HSTS {#hsts-domains}

Se você tem um domínio com HTTP Strict Transport Security (HSTS), configure o SSL e um CDN para enviar os certificados de segurança necessários. Sem SSL, links de imagens e da web ficam quebrados.

## Obter um certificado SSL {#acquire-an-ssl-certificate}

Obtenha um certificado SSL por meio de terceiros, geralmente uma rede de entrega de conteúdo (CDN). Um CDN hospeda o certificado e o apresenta ao navegador quando um usuário clica em um link, redirecionando o tráfego pelo CDN para aplicar os certificados antes de enviá-lo ao SendGrid ou SparkPost.

Para iniciar a configuração do SSL, entre em contato com seu gerente de sucesso do cliente da Braze para iniciar uma configuração completa de e-mail na Braze.

Após a Braze iniciar a configuração, siga estas etapas:

1. A Braze fornecerá registros DNS para adicionar ao seu registro de domínio.
2. A Braze verificará se os registros foram adicionados corretamente ao seu registro.
3. Depois disso, selecione um CDN e obtenha certificados SSL de um provedor terceirizado.
4. Nesse ponto, você configurará seu CDN. A Braze não pode ajudar a solucionar problemas de configuração do CDN. Entre em contato com seu provedor de CDN para obter assistência adicional.
5. Entre em contato com seu gerente de sucesso do cliente para ativar o SSL.

## O que é um CDN e por que eu preciso dele? {#what-is-a-cdn-and-why-do-i-need-it}

Uma rede de entrega de conteúdo (CDN) é uma plataforma de servidores que ajuda a garantir tempos de carregamento rápidos de conteúdo em vários meios, além de lidar com certificados de segurança.

{% alert important %}
A configuração do CDN sempre ocorre após a validação dos seus registros DNS pela Braze. Se você ainda não iniciou essa etapa, entre em contato com seu gerente de sucesso do cliente para saber mais sobre como começar.
{% endalert %}

Para rastreamento de cliques e aberturas, os parceiros de entrega transformam links usando um subdomínio com marca, e o CDN aplica o certificado SSL a esses links transformados. Os parceiros frequentemente precisam apresentar certificados válidos ao navegador do destinatário para que links e imagens sejam exibidos corretamente. Como a Braze não solicita nem gerencia certificados, você deve configurar isso por meio de um CDN.

{% alert note %}
Se você não puder ou não quiser usar os CDNs listados para rastreamento de cliques e aberturas com SSL, pode definir uma configuração SSL personalizada. CDNs alternativos ou proxies personalizados podem resultar em uma configuração mais complexa. Consulte a documentação do [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) e do [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

### Recursos adicionais {#additional-resources}

{% alert important %}
Para solucionar problemas de configuração do CDN, entre em contato com seu provedor de CDN ou consulte a [Solução de problemas]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting/) para orientações gerais.
{% endalert %}

Consulte os seguintes recursos dos parceiros ESP sobre como configurar determinados CDNs. Embora seu CDN específico possa não estar listado, você deve garantir que seu CDN tenha a capacidade de aplicar certificados SSL.

Ao configurar o domínio de rastreamento de cliques do seu CDN, ative o cabeçalho `X-Forwarded-Host` para evitar possíveis problemas de segurança, como ataques de cabeçalho de host. Consulte a documentação do CDN ou sua equipe de suporte para obter as etapas.

| Parceiro | CDN | Documentação |
| --- | --- | --- |
| Amazon SES | AWS CloudFront | [Usando HTTPS com CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) |
| Amazon SES | CloudFlare | [Comece com SSL/TLS](https://developers.cloudflare.com/ssl/get-started/) |
| Amazon SES | Fastly | [Configurando TLS com certificados gerenciados pelo Fastly](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/) |
| Amazon SES | KeyCDN | [Como configurar SSL personalizado](https://www.keycdn.com/support/how-to-setup-custom-ssl) |
| Amazon SES | Google Cloud | [Certificados SSL gerenciados pelo Google](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) |
| SendGrid | AWS CloudFront | [Como configurar SSL para rastreamento de cliques usando CloudFront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront) |
| SendGrid | CloudFlare | [Usando CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare) |
| SendGrid | Fastly | [Usando Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly) |
| SendGrid | KeyCDN | [Usando KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) |
| SparkPost | AWS CloudFront | [Guia passo a passo com AWS CloudFront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront) |
| SparkPost | CloudFlare | [Guia passo a passo com Cloudflare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare) |
| SparkPost | Fastly | [Guia passo a passo com Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly) |
| SparkPost | Google Cloud Platform | [Guia passo a passo com Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform) |
| SparkPost | Microsoft Azure | [Guia passo a passo com Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Recursos adicionais" }

### Amazon SES

Se você está usando o Amazon SES como seu ESP, consulte a **Opção 2: Configurando um domínio HTTPS** na [documentação do Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) e especifique o domínio de rastreamento da AWS por região com base no seu cluster da Braze:

- **Clusters da Braze nos EUA:** `r.us-east-1.awstrack.me`
- **Clusters da Braze na UE:** `r.eu-central-1.awstrack.me`

{% alert important %}
Ao configurar o domínio de rastreamento de cliques do seu CDN, ative o cabeçalho `X-Forwarded-Host` para evitar possíveis problemas de segurança, como ataques de cabeçalho de host. Consulte seu provedor de CDN para obter as etapas.
{% endalert %}

## Solução de problemas {#troubleshooting}

Embora você deva lidar com a configuração do CDN, certificados e problemas de proxy com seu CDN, use estas dicas para identificar problemas comuns de rastreamento de cliques com SSL. Para orientações de solução de problemas, consulte [Solução de problemas]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/troubleshooting/).