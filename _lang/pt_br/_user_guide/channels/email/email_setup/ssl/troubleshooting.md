---
nav_title: Solução de problemas
article_title: Solução de problemas de SSL
page_order: 5
page_type: reference
description: "Este artigo de referência aborda dicas de solução de problemas para SSL."
channel: email
---

# Solução de problemas {#troubleshooting}

> Use estas dicas para identificar problemas comuns de rastreamento de cliques com SSL. As orientações de solução de problemas são genéricas, pois cada CDN é único. Para problemas de configuração de CDN, certificados ou proxy, entre em contato com a equipe de suporte do seu CDN, já que essas configurações ocorrem fora do ecossistema da Braze.

## Conceitos-chave {#key-concepts}

- **URL rastreada:** Envolve o link HTTPS original no seu domínio de rastreamento. Quando um usuário clica nele, o domínio de rastreamento resolve a solicitação e redireciona para o destino final. Um CDN permite rastrear URLs seguras (HTTPS). Sem ele, os usuários podem encontrar um erro de privacidade "a conexão não é segura".
- **URL não rastreada:** Mantém a URL original intacta, ignorando o CDN para servir como um ambiente de controle.

## Baixas taxas de abertura de e-mail {#low-email-open-rates}

Se você está enfrentando taxas de abertura de e-mail repentinamente baixas, confirme se o certificado SSL está atualizado. Se estiver expirado, você deve renovar o certificado SSL com seu CDN ou provedor de certificados.

## HTTP 403 em links de redirecionamento {#http-403-on-redirect-links}

Se links de redirecionamento rastreados retornam **403 Forbidden**, a falha geralmente ocorre na sua rede de distribuição de conteúdo (CDN) ou firewall de aplicação web (WAF) — por exemplo, regras no AWS WAF ou Amazon CloudFront que bloqueiam determinados user agents, query strings ou padrões de redirecionamento. Revise os registros e métricas de solicitações bloqueadas com seu CDN ou provedor de nuvem. Para AWS, consulte [Solução de problemas com o CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/troubleshooting.html).

Para verificar se o problema é específico do rastreamento de cliques, desative o rastreamento de cliques para um link de teste (consulte [Desativando o rastreamento de cliques link a link]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/#turning-off-click-tracking-on-a-link-to-link-basis)). Se a URL de destino carrega quando o rastreamento de cliques está desativado, mas retorna 403 quando o rastreamento está ativado, concentre-se na configuração do seu domínio de rastreamento de cliques, CDN e WAF.

## Problemas no registro de domínio {#domain-registry-issues}

Execute um comando dig para confirmar que o rastreamento de links aponta para o CDN. No seu terminal, execute `dig CNAME link_tracking_subdomain`. Na seção `ANSWER SECTION`, é listado para onde seu CNAME aponta. Se ele aponta para o provedor de serviço de e-mail (SendGrid, SparkPost ou Amazon SES) e não para o seu CDN, reconfigure o registro do seu domínio para apontar para o CDN.

## Problemas com o CDN {#cdn-issues}

Se os links de e-mail em produção quebram durante a configuração, provavelmente você apontou o DNS para o CDN antes da configuração adequada. Isso pode aparecer como um erro de "link incorreto". Entre em contato com o provedor do seu CDN e revise a documentação para solucionar a configuração.

Se você vir uma mensagem de erro informando que sua conexão não é privada, isso pode indicar que seu SSL ou CDN não está configurado corretamente. Execute um comando `dig` no seu terminal (por exemplo, `dig CNAME your_link_tracking_subdomain`). Na seção `ANSWER SECTION`, se o resultado aponta para o seu ESP em vez do seu CDN, o problema é uma configuração incorreta. Para que o rastreamento de cliques SSL da Braze funcione, o CNAME deve apontar para o seu CDN. Coordene com a equipe que gerencia a configuração do seu SSL e CDN para obter mais assistência.

## Status de ativação do SSL {#ssl-enablement-status}

Se você concluiu a configuração do SSL e os links ainda aparecem como HTTP, entre em contato com o seu gerente de sucesso do cliente da Braze para confirmar que a Braze ativou o SSL. A Braze ativa o SSL somente após todas as etapas de configuração estarem concluídas.

### Amazon SES {#amazon-ses}

Se você está usando o Amazon SES como provedor de serviço de e-mail, os seguintes problemas de configuração podem impedir a Braze de ativar o SSL ou causar erros durante a configuração:

- **Incompatibilidade de região:** Confirme que a origem do seu CDN aponta para o domínio de rastreamento AWS do seu cluster da Braze. Clusters nos EUA usam `r.us-east-1.awstrack.me`. Clusters na UE usam `r.eu-central-1.awstrack.me`. Usar a região errada pode bloquear a ativação do SSL.
- **Cabeçalho de host:** O Amazon SES exige que seu CDN encaminhe o cabeçalho de host correto. Ative o cabeçalho `X-Forwarded-Host` no seu domínio de rastreamento de cliques. Para saber mais, consulte a seção [Amazon SES](#amazon-ses).
- **Configuração de proxy:** Uma configuração de proxy ou CDN que substitui ou conflita com o cabeçalho de host pode causar falha na ativação do SSL. Revise as configurações de proxy com o provedor do seu CDN para confirmar que elas não interferem no encaminhamento do cabeçalho de host.
- **Registro alias do Route 53:** Se você usa o Route 53 para gerenciar o DNS do seu domínio, crie um [registro alias no Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) que aponte para a distribuição do seu CDN (por exemplo, `d111111abcdef8.cloudfront.net`). Usar um CNAME padrão em vez de um registro alias pode retornar erros HTTP 400.
- **Encaminhamento de cabeçalho desativado:** Se a ativação do SSL ainda falhar após configurar o `X-Forwarded-Host`, tente desativar o encaminhamento de cabeçalho no seu CDN ou proxy. Algumas configurações resolvem o problema quando o encaminhamento é totalmente desativado. Trabalhe com sua equipe de TI ou provedor de CDN para testar essa configuração.

## Problemas de rastreamento de cliques {#click-tracking-issues}

Problemas comuns de redirecionamento geralmente resultam de uma configuração inadequada entre o CDN que hospeda o domínio de rastreamento e seus certificados SSL associados ou registros DNS CNAME. Essas configurações incorretas frequentemente fazem com que os usuários recebam um erro de privacidade "a conexão não é segura" ou uma falha `404` após clicar em um link de e-mail rastreado.

Use o modelo a seguir para testar a configuração do CDN do seu domínio de rastreamento, que é o mecanismo que suporta a análise de dados dos links nos seus e-mails.

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

Se a URL não rastreada funciona, mas a URL rastreada falha, pode haver uma lacuna na configuração. Para solucionar, consulte a documentação do seu ESP e provedor de CDN específicos. Você também pode revisar o artigo [SSL na Braze]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl/) para requisitos detalhados sobre provisionamento de certificados.

Use a tabela a seguir para diagnosticar erros comuns ao testar o rastreamento de cliques.

| Código de erro | Solução de problemas |
| --- | --- |
| `"Your connection is not private" (NET::ERR_CERT_COMMON_NAME_INVALID)` | Verifique se o seu domínio de rastreamento possui um certificado SSL válido. |
| `"This site can't be reached" (DNS_PROBE_FINISHED_NXDOMAIN)` | Verifique suas configurações de DNS. Confirme que o subdomínio de rastreamento está configurado conforme a configuração recomendada pelo seu CDN e ESP. |
| `525 / 526 SSL Error` | Verifique se a configuração de SSL no seu CDN (como Cloudflare) corresponde à capacidade da sua Origin. |
| `404 Not Found` | Verifique se o seu CDN está configurado para encaminhar o caminho completo da URL para o ESP, em vez de apontar para um diretório raiz vazio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Códigos de erro e solução de problemas" }