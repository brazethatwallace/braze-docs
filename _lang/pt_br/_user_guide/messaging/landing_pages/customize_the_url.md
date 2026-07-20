---
nav_title: Personalizar a URL
article_title: Personalizar a URL
description: "Saiba como personalizar as URLs das suas landing pages com a marca da sua empresa, conectando seu domínio ao seu espaço de trabalho da Braze."
page_order: 1
---

# Personalizar URLs de landing pages {#customize-landing-page-urls}

> Saiba como personalizar as URLs das suas landing pages com a marca da sua empresa, conectando seu domínio ao seu espaço de trabalho da Braze.

## Como funciona {#how-it-works}

Quando você [conecta seu domínio à Braze](#connect-your-domain-to-braze), ele será usado como o domínio padrão para todas as landing pages. Por exemplo, se você conectar o subdomínio `forms.example.com`, as URLs das suas landing pages passarão a ser `forms.example.com/holiday-sale`.

O número de domínios personalizados que você pode conectar à sua conta da Braze depende do seu [plano contratado]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). Para aumentar seu limite, entre em contato com o gerente da sua conta na Braze.

## Conectar seu domínio à Braze {#connect-your-domain-to-braze}

Para conectar um domínio à sua conta da Braze, peça a um administrador que siga as etapas abaixo.

1. Acesse **Configurações** > **Configurações da landing page**.
2. Insira o domínio que deseja conectar e selecione **Enviar**. Por exemplo, `forms.example.com`.
3. Copie e cole os registros **TXT** e **CNAME** nas configurações de DNS do seu provedor de domínio.
4. Volte ao dashboard da Braze para verificar a conexão.

![Página de configurações da landing page com um registro TXT e dois registros CNAME listados com seus respectivos nomes e valores.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
Dependendo do seu provedor de domínio, a conexão pode levar até 48 horas. Quando o processo for concluído, começaremos a usar seu domínio personalizado para suas landing pages no dashboard da Braze.
{% endalert %}

### Configuração do certificado SSL {#ssl-certificate-setup}

A Braze usa o Cloudflare para provisionar automaticamente certificados SSL para o seu domínio personalizado por meio de um [desafio ACME DNS-01](https://letsencrypt.org/docs/challenge-types/#dns-01-challenge). Esse método de validação contínua é ativado por um dos registros CNAME que você forneceu durante a configuração e permite que a autoridade certificadora (LetsEncrypt) verifique a propriedade do seu domínio por meio de registros DNS sem que a Braze precise ser proprietária do seu domínio.

## Remover seu domínio {#remove-your-domain}

Se você é administrador na Braze, pode remover um domínio configurado anteriormente seguindo estas etapas:

1. Acesse **Configurações** > **Configurações da landing page**.
2. Selecione **Remover domínio personalizado**.
3. Confirme a remoção do domínio.
4. Remova os registros DNS listados das configurações do seu domínio.

{% alert important %}
Quando você remove um domínio personalizado, essa URL deixa de ser válida. Todas as landing pages que estavam usando esse domínio serão revertidas automaticamente para o domínio padrão definido pela Braze.
{% endalert %}

## Migrar seu domínio {#migrate-your-domain}

Para migrar um domínio personalizado para outro espaço de trabalho:

1. Remova o domínio personalizado.
2. Crie um novo domínio personalizado no espaço de trabalho desejado.
3. Reconfigure o domínio personalizado com os novos registros DNS. Observe que seu subdomínio ficará indisponível durante esse processo.

## Recursos de DNS {#dns-resources}

{% multi_lang_include channels/email/dns_records.md %}

## Solução de problemas {#troubleshooting}

### Minha conexão de domínio falhou {#my-domain-connection-failed}

Verifique se o domínio foi inserido corretamente e se corresponde ao que você enviou para a Braze a partir da conta do seu provedor de domínio. Se estiver correto e corresponder, verifique os registros TXT e CNAME fornecidos pela Braze. Eles devem corresponder aos registros que você inseriu na conta do seu provedor de domínio.

## Perguntas frequentes {#frequently-asked-questions}

### Posso usar subdomínios aninhados para meu domínio personalizado? {#can-i-use-nested-subdomains-for-my-custom-domain}

Sim, você pode usar subdomínios aninhados para suas landing pages. Por exemplo, `forms.braze.com`, `pages.forms.braze.com` ou níveis mais profundos são todos compatíveis. O único requisito é que você não pode usar um domínio apex (como `braze.com`), pois a Braze usa registros CNAME para a conexão.

### Posso conectar vários subdomínios ao meu espaço de trabalho ou conectar um subdomínio a vários espaços de trabalho? {#can-i-connect-multiple-subdomains-to-my-workspace-or-connect-one-subdomain-to-multiple-workspaces}

Não, atualmente você só pode conectar um subdomínio a um espaço de trabalho.

### Posso usar o mesmo subdomínio que já uso para meu site principal ou meu domínio de envio? {#can-i-use-the-same-subdomain-that-i-currently-use-for-my-main-website-or-my-sending-domain}

Não, você não pode usar subdomínios que já estejam em uso. Embora esses subdomínios sejam válidos, eles não podem ser usados para landing pages se já estiverem atribuídos a outros fins ou tiverem registros DNS que entrem em conflito com os registros CNAME necessários.

### Por que meu domínio personalizado está preso em "Connecting" apesar de os registros DNS serem válidos? {#why-is-my-custom-domain-stuck-on-connecting-despite-valid-dns-records}

Se o seu domínio personalizado mostra todos os registros DNS como "Connected", mas o status do domínio permanece em "Connecting" por mais de quatro horas, sua organização pode estar usando registros CAA (Certificate Authority Authorization) ou bloqueios de zona do Cloudflare que impedem a Braze de proteger sua página.

#### Registros CAA {#caa-records}

Os registros CAA restringem quais autoridades certificadoras podem emitir certificados SSL para o seu domínio. Se seus registros CAA não incluírem o LetsEncrypt, a Braze (por meio do Cloudflare) não poderá emitir o certificado SSL necessário.

Para resolver isso, peça à sua equipe de TI que adicione um registro CAA ao seu subdomínio com os seguintes valores:
- **Tipo de registro:** CAA
- **Valor:** `0 issue "letsencrypt.org"`

Para saber mais, consulte a [documentação CAA do LetsEncrypt](https://letsencrypt.org/docs/caa/).

#### Bloqueios de zona do Cloudflare {#cloudflare-zone-holds}

Se sua organização usa o Cloudflare, um recurso de segurança de bloqueio de zona pode estar impedindo a Braze de criar seu domínio personalizado.

Para resolver isso, peça à sua equipe de TI que libere temporariamente o bloqueio de zona. Para saber mais, consulte a [documentação de bloqueio de zona do Cloudflare](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/#release-zone-holds).

#### Reiniciar o processo de validação {#restarting-the-validation-process}

Após resolver qualquer um dos problemas, exclua e recrie seu domínio personalizado no dashboard da Braze para reiniciar o processo de validação.

### Posso usar um proxy reverso para servir landing pages no meu domínio principal ou em um subdiretório? {#can-i-use-a-reverse-proxy-to-serve-landing-pages-under-my-main-domain-or-a-subdirectory}

Não, as Liquid tags de URL de landing pages não funcionarão corretamente com proxies reversos.