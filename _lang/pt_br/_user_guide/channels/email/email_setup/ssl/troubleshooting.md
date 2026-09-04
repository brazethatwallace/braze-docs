---
nav_title: Solução de problemas
article_title: Solução de problemas de rastreamento de cliques SSL
page_order: 5
page_type: reference
description: "Diagnostique problemas de rastreamento de cliques SSL e configuração de CDN usando um índice de sintomas e um caminho de investigação padrão."
channel: email
---

# Solução de problemas de rastreamento de cliques SSL {#troubleshoot-ssl-click-tracking}

> Use esta página para identificar problemas comuns de rastreamento de cliques SSL. As orientações a seguir são genéricas, pois cada CDN é única. Para problemas de configuração de CDN, certificados ou proxy, entre em contato com a equipe de suporte do seu CDN, já que essas configurações ocorrem fora da Braze.

## Comece aqui: identifique seu sintoma {#start-here-match-your-symptom}

| Sintoma | Acesse |
| --- | --- |
| As taxas de abertura de e-mail caíram repentinamente | [Taxas de abertura de e-mail baixas](#low-email-open-rates) |
| Links rastreados retornam HTTP 403 | [HTTP 403 em links de redirecionamento](#http-403-on-redirect-links) |
| DNS ou CNAME aponta para o provedor de serviços de e-mail em vez da rede de distribuição de conteúdo (CDN) | [Problemas no registro de domínio](#domain-registry-issues) |
| "A conexão não é privada" ou links quebram durante a configuração | [Problemas com CDN](#cdn-issues) |
| Configuração de SSL concluída, mas os links ainda mostram HTTP | [Status de ativação do SSL](#ssl-enablement-status) |
| URL rastreada falha, mas URL não rastreada funciona | [Problemas com rastreamento de cliques](#click-tracking-issues) |
| Erros de ativação de SSL específicos do Amazon SES | [Amazon SES](#amazon-ses) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintoma de SSL" }

## Caminho de investigação padrão {#standard-investigation-path}

1. Confirme se o subdomínio de rastreamento de cliques aponta para a sua [rede de distribuição de conteúdo (CDN)]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it) — e não diretamente para o seu provedor de serviços de e-mail (SendGrid, SparkPost ou Amazon SES). Peça à sua equipe de TI ou web para verificar se as configurações do domínio correspondem à configuração da Braze. Para os requisitos da Braze, consulte [Adquirir um certificado SSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate).
2. Confirme se o certificado SSL está ativo para o domínio de rastreamento. Peça à sua equipe de TI ou web para confirmar se o certificado está atualizado e cobre o subdomínio de rastreamento de cliques. Para etapas de configuração e guias específicos de CDN, consulte [Adquirir um certificado SSL]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#acquire-an-ssl-certificate) e [Recursos adicionais]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#additional-resources).
3. Envie um e-mail de teste usando o [modelo de solução de problemas de rastreamento de cliques](#click-tracking-issues). Compare as URLs rastreadas com as não rastreadas.
4. Se os links rastreados falharem com erro 403, revise as regras de CDN e WAF (user agents, query strings, padrões de redirecionamento).
5. Se a configuração estiver completa, mas os links continuarem em HTTP, entre em contato com o seu CSM da Braze para confirmar se a Braze ativou o SSL.
6. Para problemas persistentes, coordene com a sua equipe de CDN ou TI e entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) informando códigos de erro e quaisquer detalhes do seu CDN ou provedor de domínio.

## Conceitos-chave {#key-concepts}

- **Domínio de rastreamento de cliques (CTD):** O subdomínio personalizado que a Braze usa para encapsular links para rastreamento de cliques (por exemplo, `clicks.mail.yourbrand.com`).
- **URL rastreada:** Encapsula o link HTTPS original no seu domínio de rastreamento. Quando um usuário clica nela, o domínio de rastreamento resolve a solicitação e redireciona para o destino final. Uma CDN permite rastrear URLs seguras (HTTPS). Sem ela, os usuários podem encontrar um erro de privacidade informando que a "conexão não é segura".
- **URL não rastreada:** Mantém a URL original intacta, ignorando a CDN para servir como um ambiente de controle.
- **Roteamento Fase 1 e Fase 2:** A Fase 1 aponta o CNAME do seu domínio de rastreamento de cliques diretamente para o seu provedor de serviços de e-mail (ESP) para verificação HTTP inicial. A Fase 2 aponta o CNAME para a sua CDN ou firewall de aplicação web (WAF), que encerra o SSL e encaminha as solicitações por proxy para o ESP com os cabeçalhos necessários. Para destinos CNAME específicos de cada ESP, consulte [Roteamento de Fase 1 e Fase 2 do ESP](#esp-phase-1-and-phase-2-routing).

## Domínios de rastreamento de cliques e fases de DNS {#click-tracking-domains-and-dns-phases}

O rastreamento de cliques com SSL requer uma configuração de DNS em duas fases, pois a Braze não provisiona nem renova certificados de segurança externos em seu nome.

1. **Fase 1 (configuração inicial):** O CNAME do seu domínio de rastreamento de cliques aponta diretamente para o endpoint do seu provedor de serviços de e-mail para verificação HTTP não criptografada.
2. **Fase 2 (implantação do SSL):** Você atualiza o CNAME para apontar para o edge da sua rede de distribuição de conteúdo (CDN) ou WAF, que mantém seu certificado SSL personalizado e encaminha as solicitações ao provedor de serviços de e-mail com os cabeçalhos necessários. O provedor de serviços de e-mail registra o clique e redireciona o destinatário para o destino final.

{% alert important %}
A Braze ativa o rastreamento de cliques com SSL somente após a conclusão da verificação da Fase 1. Se o SSL estiver ativado, mas seu DNS ainda apontar para o provedor de serviços de e-mail (Fase 1), os destinatários poderão ver [erros de incompatibilidade de nome SSL](#ssl-name-mismatch-errors).
{% endalert %}

## Roteamento ESP Fase 1 e Fase 2 {#esp-phase-1-and-phase-2-routing}

Ao solucionar problemas de erros de rastreamento de links, verifique se o seu registro DNS aponta para a rede ESP não criptografada (Fase 1) ou para a sua CDN (Fase 2).

| ESP | Destino CNAME da Fase 1 (direto ao ESP) | Destino CNAME da Fase 2 | Configuração de CDN necessária |
| --- | --- | --- | --- |
| Amazon SES | `r.us-east-1.awstrack.me` (US)<br>`r.eu-central-1.awstrack.me` (EU) | Seu endpoint de CDN (por exemplo, `d123.cloudfront.net`, `ssl.fastly.net` ou Cloudflare) | Ative o cabeçalho `X-Forwarded-Host` com o nome do seu domínio de rastreamento de cliques |
| SendGrid | `sendgrid.net` | Seu endpoint de CDN | Encaminhe os cabeçalhos `Host` originais (ou IDs de rastreamento personalizados com marca) para a origem sem descartar parâmetros |
| SparkPost | `spgo.io` | Seu endpoint de CDN | Ative o `X-Forwarded-Host` e encaminhe o cabeçalho `User-Agent` original intacto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Roteamento ESP Fase 1 e Fase 2" }

Para etapas de configuração de CDN e documentação de parceiros, consulte [SSL na Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl).

## Erros de incompatibilidade de nome SSL {#ssl-name-mismatch-errors}

Uma incompatibilidade de nome SSL é uma falha de autenticação de identidade durante o handshake TLS. Ela ocorre quando um navegador estabelece uma conexão criptografada, mas o domínio na barra de endereços não corresponde a nenhuma entrada nos campos Common Name (CN) ou Subject Alternative Names (SAN) do certificado.

### O DNS ainda aponta para o provedor de serviços de e-mail (Fase 1) {#dns-still-points-to-the-esp-phase-1}

Se você instruir a Braze a ativar o rastreamento de cliques SSL, mas deixar seu CNAME de DNS apontando diretamente para o provedor de serviços de e-mail (por exemplo, `sendgrid.net` do SendGrid), o navegador do destinatário abre seu domínio de rastreamento de cliques e chega à infraestrutura do provedor. O provedor não tem registro do seu certificado personalizado e serve seu próprio certificado de fallback (por exemplo, `*.sendgrid.net`). A incompatibilidade de nome faz a conexão falhar e retorna um aviso de conexão privada.

### O certificado não cobre o subdomínio de rastreamento (Fase 2) {#certificate-does-not-cover-the-tracking-subdomain-phase-2}

Se o seu DNS aponta para a sua rede de distribuição de conteúdo (CDN) (Cloudflare, CloudFront, entre outros), mas sua equipe de segurança aplicou um certificado que cobre apenas os ativos web principais (por exemplo, `yourbrand.com` e `www.yourbrand.com`), o subdomínio específico de rastreamento de cliques (por exemplo, `clicks.mail.yourbrand.com`) não está incluído. A CDN serve um certificado que não corresponde ao domínio de rastreamento, e os navegadores exibem um erro de privacidade.

## Fluxo de trabalho de triagem {#triage-workflow}

### Etapa 1: Execute uma consulta CNAME autoritativa {#step-1-run-an-authoritative-cname-lookup}

Abra seu terminal e verifique o roteamento DNS bruto do seu domínio de rastreamento de cliques:

```bash
dig CNAME clicks.mail.yourbrand.com
```

Na `ANSWER SECTION`, verifique para onde o CNAME resolve:

| Resultado | O que significa | Próxima etapa |
| --- | --- | --- |
| Resolve para um endpoint de provedor de serviços de e-mail (`sendgrid.net`, `spgo.io` ou `awstrack.me`) | O DNS ainda está na Fase 1 | Atualize seu registro de domínio para rotear o tráfego pela sua CDN. Consulte [Roteamento de Fase 1 e Fase 2 do provedor de serviços de e-mail](#esp-phase-1-and-phase-2-routing). |
| Resolve para um endpoint de distribuição CDN | O roteamento DNS da Fase 2 está correto | Prossiga para a Etapa 2 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Resultados da consulta CNAME" }

### Etapa 2: Valide o certificado TLS {#step-2-validate-the-tls-certificate}

Force uma validação TLS ao vivo no seu domínio de rastreamento de cliques para ver exatamente qual certificado os navegadores recebem. Insira seu domínio de rastreamento de cliques em um verificador SSL externo, como o [SSL Checker do SSL Shopper](https://www.sslshopper.com/ssl-checker.html#hostname=clicks.mail.yourbrand.com) (substitua `clicks.mail.yourbrand.com` pelo seu domínio).

Confirme o seguinte:

- O certificado é válido e não está expirado
- Seu domínio de rastreamento de cliques aparece no Common Name ou nos Subject Alternative Names
- A cadeia de certificados está completa, sem alertas de certificado intermediário não confiável

{% alert tip %}
Para um relatório TLS mais detalhado, você também pode usar o [Qualys SSL Labs SSL Server Test](https://www.ssllabs.com/ssltest/).
{% endalert %}

### Etapa 3: Revise problemas de configuração da CDN {#step-3-review-cdn-configuration-issues}

Se os links de e-mails em tempo real quebrarem durante a configuração, confirme que o DNS não foi apontado para sua CDN antes de a configuração estar concluída. Isso pode aparecer como um link incorreto ou erro de conexão. Entre em contato com seu provedor de CDN e revise a documentação dele para solucionar problemas de proxy e configurações de origem. Coordene com a equipe que gerencia sua configuração de SSL e CDN para obter assistência adicional.

## Baixas taxas de abertura de e-mail {#low-email-open-rates}

**Sintoma:** As taxas de abertura de e-mail caíram repentinamente após alterações no SSL ou CDN.

Se você está enfrentando taxas de abertura de e-mail repentinamente baixas, confirme se o certificado SSL está atualizado. Se estiver expirado, você deve renovar o certificado SSL com seu CDN ou provedor de certificados.

## HTTP 403 em links de redirecionamento {#http-403-on-redirect-links}

**Sintoma:** Links de e-mail rastreados retornam "403 Forbidden".

Se links de redirecionamento rastreados retornam `403 Forbidden`, a falha geralmente ocorre na sua rede de distribuição de conteúdo (CDN) ou firewall de aplicação web (WAF) — por exemplo, regras no AWS WAF ou Amazon CloudFront que bloqueiam determinados user agents, query strings ou padrões de redirecionamento. Revise os registros e métricas de solicitações bloqueadas com seu CDN ou provedor de nuvem. Para AWS, consulte [Solução de problemas com o CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting.html).

Para verificar se o problema é específico do rastreamento de cliques, desative o rastreamento de cliques para um link de teste (consulte [Desativando o rastreamento de cliques link a link]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis)). Se a URL de destino carrega quando o rastreamento de cliques está desativado, mas retorna `403` quando o rastreamento está ativado, concentre-se na configuração do seu domínio de rastreamento de cliques, CDN e WAF. Se o seu CNAME ainda aponta para o provedor de serviços de e-mail enquanto o SSL está ativado, você pode ver um [erro de incompatibilidade de nome SSL](#ssl-name-mismatch-errors) — comece pelo [fluxo de triagem](#triage-workflow).

## Problemas no registro de domínio {#domain-registry-issues}

**Sintoma:** O DNS ou CNAME do seu subdomínio de rastreamento aponta para o seu provedor de serviços de e-mail em vez do seu CDN.

Execute um comando dig para confirmar que o rastreamento de links aponta para o CDN. No seu terminal, execute `dig CNAME link_tracking_subdomain`. Na seção `ANSWER SECTION`, é listado para onde seu CNAME aponta. Se ele aponta para o provedor de serviços de e-mail (SendGrid, SparkPost ou Amazon SES) e não para o seu CDN, reconfigure o registro do seu domínio para apontar para o CDN.

## Problemas com CDN {#cdn-issues}

**Sintoma:** Os usuários veem erros de "conexão não é privada", ou os links quebram durante a configuração do CDN.

Se os links de e-mail em produção quebram durante a configuração, provavelmente você apontou o DNS para o CDN antes da configuração adequada. Isso pode aparecer como um erro de "link incorreto". Entre em contato com o provedor do seu CDN e revise a documentação para solucionar a configuração.

Se você vir uma mensagem de erro informando que sua conexão não é privada, isso pode indicar que seu SSL ou CDN não está configurado corretamente. Execute um comando `dig` no seu terminal (por exemplo, `dig CNAME your_link_tracking_subdomain`). Na seção `ANSWER SECTION`, se o resultado aponta para o seu provedor de serviços de e-mail em vez do seu CDN, o problema é uma configuração incorreta. Para que o rastreamento de cliques SSL da Braze funcione, o CNAME deve apontar para o seu CDN. Coordene com a equipe que gerencia a configuração do seu SSL e CDN para obter mais assistência.

## Status de ativação do SSL {#ssl-enablement-status}

**Sintoma:** A configuração do SSL está concluída, mas os links rastreados ainda aparecem como HTTP.

Se você concluiu a configuração do SSL e os links ainda aparecem como HTTP, entre em contato com o seu CSM da Braze para confirmar que a Braze ativou o SSL. A Braze ativa o SSL somente após todas as etapas de configuração estarem concluídas.

### Amazon SES {#amazon-ses}

Se você está usando o Amazon SES como provedor de serviços de e-mail, os seguintes problemas de configuração podem impedir a Braze de ativar o SSL ou causar erros durante a configuração:

- **Incompatibilidade de região:** Confirme que a origem do seu CDN aponta para o domínio de rastreamento AWS do seu cluster da Braze. Clusters nos EUA usam `r.us-east-1.awstrack.me`. Clusters na UE usam `r.eu-central-1.awstrack.me`. Usar a região errada pode bloquear a ativação do SSL.
- **Cabeçalho de host:** O Amazon SES exige que seu CDN encaminhe o cabeçalho de host correto. Ative o cabeçalho `X-Forwarded-Host` no seu domínio de rastreamento de cliques. Para os requisitos de roteamento das Fases 1 e 2, consulte [Roteamento das Fases 1 e 2 do ESP](#esp-phase-1-and-phase-2-routing).
- **Configuração de proxy:** Uma configuração de proxy ou CDN que substitui ou conflita com o cabeçalho de host pode causar falha na ativação do SSL. Revise as configurações de proxy com o provedor do seu CDN para confirmar que elas não interferem no encaminhamento do cabeçalho de host.
- **Registro alias do Route 53:** Se você usa o Route 53 para gerenciar o DNS do seu domínio, crie um [registro alias no Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) que aponte para a distribuição do seu CDN (por exemplo, `d111111abcdef8.cloudfront.net`). Usar um CNAME padrão em vez de um registro alias pode retornar erros HTTP 400.
- **Encaminhamento de cabeçalho desativado:** Se a ativação do SSL ainda falhar após configurar o `X-Forwarded-Host`, tente desativar o encaminhamento de cabeçalho no seu CDN ou proxy. Algumas configurações resolvem o problema quando o encaminhamento é totalmente desativado. Trabalhe com sua equipe de TI ou provedor de CDN para testar essa configuração.

## Problemas de rastreamento de cliques {#click-tracking-issues}

**Sintoma:** Links de e-mail rastreados falham, mas links não rastreados funcionam, ou os usuários veem erros de certificado ou DNS após clicar.

Problemas comuns de redirecionamento geralmente resultam de uma configuração inadequada entre a rede de distribuição de conteúdo (CDN) que hospeda o domínio de rastreamento e seus certificados SSL associados ou registros DNS CNAME. Essas configurações incorretas frequentemente fazem com que os usuários recebam um erro de privacidade "a conexão não é segura" ou uma falha `404` após clicar em um link de e-mail rastreado.

### Requisitos de formatação de links HTML {#html-link-formatting-requirements}

Para que o rastreamento de cliques funcione, seu provedor de serviços de e-mail (SendGrid, SparkPost ou Amazon SES) precisa encontrar e substituir links no seu HTML. Em todos esses provedores, os links devem atender a estes requisitos de formatação:

- Os links devem estar em uma tag HTML `<a>` com um atributo `href`.
- A URL deve começar com `http://` ou `https://`.

Regras adicionais específicas de cada provedor:

- **SendGrid:** Coloque a URL entre aspas simples ou duplas e não inclua espaços ao redor do `=` no atributo `href`.
- **Amazon SES:** As URLs devem estar em conformidade com a [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986). Espaços não codificados em uma URL impedem que o Amazon SES rastreie o link.

Para saber mais sobre quais esquemas de URL o rastreamento de cliques da Braze suporta, consulte [Requisitos de links para rastreamento de cliques]({{site.baseurl}}/user_guide/channels/email/email_setup/open_pixel_and_click_tracking#click-tracking-link-requirements). Para detalhes sobre HTML de cada provedor, consulte [Melhores práticas de HTML para rastreamento de cliques do SendGrid](https://www.twilio.com/docs/sendgrid/ui/analytics-and-reporting/click-tracking-html-best-practices), [Linguagem de modelo do SparkPost](https://developers.sparkpost.com/api/template-language/) e [Perguntas frequentes sobre métricas de envio de e-mail do Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/faqs-metrics.html).

Exemplos válidos incluem:

```html
<a href="http://www.example.com">Link</a>
<a href='https://example.com'>Link</a>
<a target="_blank" href="https://example.com">Link</a>
```

Os exemplos a seguir omitem `http://` ou `https://` e não são rastreados:

```html
<a href="example.com">Link</a>
<a href="www.example.com">Link</a>
```

Se você usa SendGrid, os exemplos a seguir também não são rastreados:

```html
<a href= http://www.example.com>Link</a>
<a href = "https://example.com">Link</a>
```

{% alert note %}
Embora o subdomínio `www` seja opcional, `http://` ou `https://` é obrigatório para que o rastreamento de cliques funcione corretamente.
{% endalert %}

### Testando o rastreamento de cliques {#testing-click-tracking}

Após concluir o [fluxo de triagem](#triage-workflow), use o modelo a seguir para testar a configuração do CDN do seu domínio de rastreamento, que é o mecanismo que suporta a análise de dados dos links nos seus e-mails.

1. Copie e cole o modelo a seguir em uma Campaign de e-mail HTML na Braze.

{% details Modelo de solução de problemas de rastreamento de cliques %}
{% raw %}
```html
<!DOCTYPE html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="color-scheme" content="light dark">
    <meta name="supported-color-schemes" content="light dark">
    <title>Click Tracking Test</title>
    <style>
        /* Base Dark Mode (Default) */
        body {
            margin: 0;
            padding: 0;
            background-color: #2b0562;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            color: #ffd1e9;
        }

        .email-container {
            width: 100%;
            max-width: 600px;
            margin: 40px auto;
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid #F3697F;
            border-radius: 16px;
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #E83F21 0%, #F3697F 100%);
            padding: 40px 20px 50px 20px;
            text-align: center;
        }

        .logo {
            display: block;
            margin: 0 auto 25px auto;
            border: 0;
            outline: none;
            text-decoration: none;
        }

        .header h1 {
            color: #ffffff;
            margin: 0;
            font-size: 26px;
            font-weight: 800;
            letter-spacing: -0.5px;
        }

        .content {
            padding: 40px 40px 20px 40px;
            line-height: 1.8;
            font-size: 15px;
        }

        .troubleshoot {
            margin: 0 40px 40px 40px;
            padding: 25px;
            background-color: rgba(253, 167, 216, 0.1);
            border-radius: 12px;
            font-size: 14px;
            border: 1px dashed #F3697F;
        }

        .troubleshoot h2 {
            margin-top: 0;
            font-size: 18px;
            color: #ffffff;
        }

        .btn-section {
            padding: 0 40px 40px 40px;
            text-align: center;
        }

        .btn {
            display: inline-block;
            padding: 16px 32px;
            border-radius: 12px;
            font-weight: 700;
            text-decoration: none;
            margin: 10px;
            font-size: 14px;
        }

        .btn-tracked {
            background-color: #F3697F;
            color: #ffffff;
        }

        .btn-untracked {
            border: 2px solid #FDA7D8;
            color: #FDA7D8;
            background-color: transparent;
        }

        .footer {
            text-align: center;
            font-size: 12px;
            color: #FDA7D8;
            padding-bottom: 40px;
            opacity: 0.6;
        }

        /* Light Mode Overrides */
        @media (prefers-color-scheme: light) {
            body { background-color: #F7FCFF !important; color: #2b0562 !important; }
            .email-container { background-color: #ffffff !important; border: 1px solid #FDA7D8 !important; box-shadow: 0 4px 20px rgba(43, 5, 98, 0.1); }
            .content { color: #2b0562 !important; }
            .troubleshoot { background-color: #F7FCFF !important; border-color: #F3697F !important; color: #2b0562 !important; }
            .troubleshoot h2 { color: #E83F21 !important; }
            .btn-untracked { color: #F3697F !important; border-color: #F3697F !important; }
            .footer { color: #2b0562 !important; }
            strong { color: #E83F21 !important; }
        }

        /* Mobile Optimization */
        @media only screen and (max-width: 480px) {
            .btn { display: block !important; margin: 10px 0 !important; width: auto !important; }
            .content, .troubleshoot { padding: 25px !important; }
        }
    </style>
</head>
{%- capture url -%}https://example.com{%- endcapture -%}
<body>
    <center>
        <table class="email-container" role="presentation" width="600" border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td class="header">
                    <img src="https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137"
                         width="150"
                         alt="Logo"
                         class="logo">
                    <h1>Testing Click Tracking Functionality</h1>
                </td>
            </tr>
            <tr>
                <td class="content">
                    <p>
                        Use this template to test the <strong>CDN configuration</strong> of your tracking domain—the mechanism supporting analytics for links within your emails.
                    </p>
                    <p>
                        A <strong>Tracked URL</strong> wraps the original HTTPS link in your tracking domain. When a user clicks it, the tracking domain resolves the request and redirects to the final destination. A CDN allows you to track secure (HTTPS) URLs; without it, users may encounter a "connection is not secure" privacy error. An <strong>Untracked URL</strong> maintains the original URL intact, bypassing the CDN to serve as a control environment.
                    </p>
                    <p>
                        Common redirection issues typically result from an improper configuration between the CDN hosting the tracking domain and the <strong>associated SSL certificate or DNS CNAME records.</strong>
                    </p>
                    <p>
                        <i style="font-size: 13px;">This template uses "example.com" as the destination URL. To test your own domain, replace the URL in the <strong>capture</strong> tag located on line 125.</i>
                    </p>
                </td>
            </tr>
            <tr>
                <td class="btn-section">
                    <a href="{{url}}" class="btn btn-tracked">Tracked URL</a>

                    <a href="{{url}}"
                       class="btn btn-untracked"
                       clicktracking="off"
                       data-msys-clicktrack="0"
                       ses:no-track="true">
                       Untracked URL
                    </a>
                </td>
            </tr>
            <tr>
                <td>
                    <div class="troubleshoot">
                        <h2>Troubleshooting the Test</h2>
                        <ul>
                            <li><strong>Tracked URL Fails / Untracked Works:</strong> This indicates a CDN or SSL certificate issue. Verify that your SSL certificate is valid and correctly bound to your tracking domain.</li>
                            <li><strong>Privacy Error (HTTPS):</strong> Ensure your CDN is configured to handle port 443 traffic and that the certificate matches your tracking CNAME.</li>
                            <li><strong>Both URLs Fail:</strong> Check the destination URL or your internal network firewall settings.</li>
                            <li>For more information, visit: <a href="{{ site.homeurl }}{{ site.baseurl }}/user_guide/channels/email/email_setup/ssl">SSL at Braze</a></li>
                        </ul>
                    </div>
                </td>
            </tr>
        </table>
        <div class="footer">
            Braze :: 63 Madison Avenue, 13th Floor :: New York, NY 10016
        </div>
    </center>
</body>
</html>
```
{% endraw %}
{% enddetails %}

{: start="2"}
2. Configure sua URL. Substitua a URL na tag `capture` próxima ao topo do corpo do modelo (onde `https://example.com` está definido). Por exemplo, substitua `https://example.com` por `https://braze.com/docs`.
3. Envie um e-mail de teste para você mesmo e selecione ambos os botões.
4. Verifique se o comportamento esperado e os critérios de sucesso estão conforme descrito no modelo.

Se a URL não rastreada funciona, mas a URL rastreada falha, pode haver uma lacuna na configuração. Consulte a documentação do seu provedor de serviços de e-mail e provedor de CDN específicos. Para requisitos detalhados sobre provisionamento de certificados, consulte [SSL na Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl).

Use a tabela a seguir para diagnosticar erros comuns ao testar o rastreamento de cliques.

| Código de erro | Solução de problemas |
| --- | --- |
| `"Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID)` | Conclua o [fluxo de triagem](#triage-workflow) e consulte [Erros de incompatibilidade de nome SSL](#ssl-name-mismatch-errors). Verifique se o seu domínio de rastreamento de cliques está listado no Common Name ou nos Subject Alternative Names do certificado. |
| `"This site can't be reached" (DNS_PROBE_FINISHED_NXDOMAIN)` | Verifique suas configurações de DNS. Confirme que o subdomínio de rastreamento está configurado conforme a configuração recomendada pelo seu CDN e provedor de serviços de e-mail. |
| `525 / 526 SSL Error` | Verifique se a configuração de SSL no seu CDN (como Cloudflare) corresponde à capacidade da sua Origin. |
| `404 Not Found` | Verifique se o seu CDN está configurado para encaminhar o caminho completo da URL para o provedor de serviços de e-mail, em vez de apontar para um diretório raiz vazio. |
| `400 Bad Request: Request Header or Cookie Too Large` | Esse erro geralmente ocorre quando o domínio de rastreamento de cliques herda cookies grandes demais do domínio do seu website. A Braze não define nem bloqueia cookies no domínio de rastreamento. Configure seu CDN para não enviar esses cookies ao provedor de serviços de e-mail ao fazer proxy reverso da solicitação de rastreamento de cliques. Talvez também seja necessário aumentar a configuração `large_client_header_buffers` na sua configuração do nginx (por exemplo, `large_client_header_buffers 4 32k;` para permitir cabeçalhos de até 32&nbsp;KB). Para saber mais, consulte seu provedor de CDN ou equipe de engenharia do website. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Códigos de erro e solução de problemas" }