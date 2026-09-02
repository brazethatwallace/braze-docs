---
nav_title: Enviar e-mails para o Apple Private Relay
article_title: Enviar e-mails para o Apple Private Relay
alias: /email_relay/
page_order: 0
description: "Este artigo aborda o processo de envio de e-mails para o Apple Private Relay."
channel:
  - email
toc_headers: h2
---

# Enviar e-mails para o Apple Private Relay {#send-emails-to-apple-private-relay}

> O recurso de login único (SSO) da Apple permite que seus usuários compartilhem seus endereços de e-mail (`example@icloud.com`) ou ocultem seus endereços de e-mail mascarando o que é fornecido às marcas (`tq1234snin@privaterelay.appleid.com`) em vez do endereço de e-mail pessoal. A Apple encaminhará as mensagens enviadas para os endereços de relay para o endereço de e-mail real do usuário.

Para enviar e-mails para o relay de e-mail privado da Apple, registre seus domínios de envio com a Apple. Se você não configurar seus domínios com a Apple, os e-mails enviados para endereços de relay resultarão em bounces.

Se um usuário decidir desativar o encaminhamento de e-mail para o e-mail de relay do seu app, a Braze receberá informações de bounce de e-mail normalmente. Esses usuários podem gerenciar os apps que usam o login com a Apple na página de configurações do Apple ID (consulte a [documentação da Apple](https://support.apple.com/en-us/HT210426)).

## Configure seu provedor de e-mail {#configure-your-email-provider}

{% tabs %}
{% tab SendGrid %}

Se você usa o SendGrid como provedor de e-mail, pode enviar e-mails para a Apple sem fazer alterações no DNS.

1. Faça login no [Apple Developer Portal](https://developer.apple.com/)
2. Acesse a página **Certificates, Identifiers & Profiles**.
3. Selecione **Services** > **Sign in with Apple for Email Communication**.
4. Na seção **Email Sources**, adicione os domínios e subdomínios.
- O endereço deve ser formatado como: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (um exemplo seria: `bounces+1234567@braze.online.docs.com`).

Se o endereço de remetente desejado for um endereço `abmail`, inclua isso no seu subdomínio. Por exemplo, use `abmail.docs.braze.com` em vez de `docs.braze.com`.

{% endtab %}
{% tab SparkPost %}

Para configurar o Apple Private Relay para SparkPost, siga estas etapas:

1. Faça login com a Apple.
2. Siga a [documentação da Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) para registrar os domínios de e-mail.
3. A Apple verificará automaticamente os domínios, mostrará quais foram verificados e fornecerá a opção de verificar novamente ou excluir os domínios.

### Quando o domínio de envio também é o domínio de bounce {#when-the-sending-domain-is-also-the-bounce-domain}

Se um domínio de envio também é usado como domínio de bounce, você não poderá armazenar nenhum registro e precisará seguir estas etapas adicionais:

1. Se o domínio já foi verificado no SparkPost, você **deve** criar registros MX e TXT:

| Instância | Registro MX                  | Registro TXT                                   |
|-----------|------------------------------|-------------------------------------------------|
| US        | `smtp.sparkpostmail.com`     | `"v=spf1 redirect=_spf.sparkpostmail.com"`      |
| EU        | `smtp.eu.sparkpostmail.com`  | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"`   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Quando o domínio de envio também é o domínio de bounce" }

{% alert important %}
Para evitar falhas de SPF, você deve criar os registros MX e TXT e garantir que eles estejam propagados no DNS **antes** de excluir o registro CNAME.
{% endalert %}

{:start="2"}
2. Exclua o registro CNAME.
3. Substitua-o pelos registros MX e TXT para o roteamento adequado.
4. Crie seu registro A para apontar para sua rede de distribuição de conteúdo (CDN) ou hospedagem de arquivos.

{% endtab %}
{% tab Amazon SES %}

Para configurar o Apple Private Relay, o ideal é ter um domínio MAIL FROM personalizado configurado.

1. Faça login com a Apple.
2. Siga a [documentação da Apple](https://developer.apple.com/help/account/capabilities/configure-private-email-relay-service) para registrar os domínios de e-mail.

{% alert important %}
Confirme que seu DKIM/SPF corresponde ao que você registrou conforme as instruções indicadas no link.
{% endalert %}

{:start="3"}
3. A Apple verificará automaticamente os domínios, mostrará quais foram verificados e fornecerá a opção de verificar novamente ou excluir os domínios.

{% endtab %}
{% endtabs %}

Se você tiver alguma dúvida adicional, abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).