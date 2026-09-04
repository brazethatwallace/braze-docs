---
nav_title: Entendendo os registros DNS
article_title: Entendendo os registros DNS
page_order: 2
page_type: reference
description: "Este artigo de referência explica como os registros DNS funcionam nos provedores de serviços de e-mail da Braze, incluindo SPF, DKIM, DMARC e estruturas de registros específicas de cada provedor."
channel: email
---

# Entendendo os registros DNS {#understanding-dns-records}

> Esta referência explica como os registros DNS funcionam na Braze com três provedores de serviços de e-mail (ESPs) principais: SparkPost, SendGrid e Amazon Simple Email Service (SES). A configuração adequada do DNS é essencial para a autenticação de e-mail (SPF, DKIM, DMARC) e o alinhamento de marca, e impacta diretamente a entregabilidade.

Para saber mais, consulte [Autenticação de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication).

## Fundamentos da autenticação de e-mail {#core-email-authentication-fundamentals}

Antes de revisar as estruturas específicas de cada provedor, entenda o que esses registros fazem e como a Braze os utiliza para alcançar o alinhamento adequado.

### Sender Policy Framework (SPF) {#spf}

O SPF é um registro DNS em um domínio que especifica quais endereços IP estão autorizados a enviar e-mail em nome desse domínio.

A Braze não solicita que você modifique ou adicione registros SPF no domínio raiz corporativo (como `example.com`). Em vez disso, a Braze isola a entrega usando um domínio Return-jornada dedicado e personalizado (também conhecido como domínio de bounce, domínio MAIL FROM ou domínio envelope From), como `bounce.mail.example.com`.

Como os provedores de caixa de entrada receptores validam o SPF com base nesse domínio Return-jornada, e não no domínio visível do cabeçalho `From:`, a configuração do SPF fica inteiramente no nível do subdomínio. Dependendo do provedor de serviços de e-mail subjacente, a Braze lida com essa validação de duas formas:

- Delegação CNAME (SendGrid e SparkPost): Crie um `CNAME` apontando seu subdomínio de volta para o provedor de serviços de e-mail. O provedor hospeda e atualiza as políticas SPF em sua infraestrutura, passando na verificação SPF automaticamente.
- Registro TXT explícito (Amazon SES): Publique um registro `TXT` fixo diretamente no subdomínio de bounce contendo uma string de autorização explícita (por exemplo, `v=spf1 include:amazonses.com ~all`), concedendo à AWS permissão para enviar e-mails a partir dessa zona.

### Domain Keys Identified Mail (DKIM) {#dkim}

O DKIM adiciona uma assinatura digital criptográfica ao cabeçalho do e-mail. O servidor receptor usa a chave pública do remetente (publicada no DNS) para verificar se o e-mail foi originado pelo proprietário do domínio e não foi alterado em trânsito.

A Braze exige que as chaves públicas DKIM sejam publicadas por meio de registros `TXT` ou `CNAME` para que os ISPs receptores possam validar as assinaturas criptográficas geradas pelo seu provedor de serviços de e-mail.

### Alinhamento DMARC {#dmarc}

Para que um e-mail passe na verificação DMARC, o domínio no cabeçalho `From:` visível ao usuário deve corresponder (alinhar-se) ao domínio validado pelo SPF (o Return-jornada) ou pelo DKIM. Como as configurações da Braze alcançam o alinhamento tanto pelo SPF quanto pelo DKIM, suas políticas DMARC são atendidas com segurança.

A Braze lida com a autenticação básica de SPF e DKIM por padrão, mas você ainda precisa adicionar um registro DMARC ao seu domínio de envio. O DMARC é uma ferramenta de autenticação essencial exigida por quase todos os principais provedores de caixa de entrada. Ele comprova que seus e-mails são legítimos, fortalece a reputação do seu domínio e mantém sua entregabilidade saudável ao longo do tempo.

Como isso requer acesso ao registro de domínio da sua empresa, você ou o administrador de rede precisam adicionar esse registro no nível do domínio raiz. Se você está começando, uma política básica como `p=none` atende aos requisitos mínimos dos provedores de caixa de entrada. Para saber mais sobre DMARC, consulte [DMARC.org](https://dmarc.org/). Para orientações específicas da Braze sobre DMARC, consulte [Autenticação de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup/authentication#dmarc).

## Arquitetura DNS específica do provedor de serviços de e-mail {#esp-specific-dns-architecture}

Diferentes arquiteturas de provedores de serviços de e-mail lidam com a delegação de DNS de formas distintas. Ao provisionar seu ambiente, use os registros exatos mapeados para o cluster específico do seu provedor.

### Arquitetura SparkPost {#sparkpost-architecture}

O SparkPost usa uma configuração híbrida. Ele usa registros `CNAME` explícitos para direcionar a infraestrutura de rastreamento e Return-jornada de volta ao SparkPost, enquanto usa um registro `TXT` bruto para autenticação DKIM.

- Configuração de SPF e Return-jornada: o SparkPost solicita um subdomínio designado para bounces (por exemplo, `mail.example.com`). Um registro `CNAME` aponta esse subdomínio para os processadores de bounce de entrada do SparkPost. Isso roteia o tráfego de bounce corretamente e valida o SPF automaticamente, pois o servidor de destino do SparkPost gerencia o protocolo.
- Configuração de DKIM: o SparkPost requer um registro `TXT` contendo a string exata da chave pública mapeada para um seletor específico.
- Rastreamento de cliques e aberturas: configure um subdomínio de rastreamento com um `CNAME` apontando para os endpoints de rastreamento do SparkPost (ou um proxy CDN se o rastreamento SSL for solicitado).

#### Exemplo de tabela DNS do SparkPost {#example-sparkpost-dns-table}

A tabela a seguir mostra exemplos de registros DNS para uma configuração SparkPost.

| Tipo de registro | Host/Nome | Valor/Destino | Finalidade |
| --- | --- | --- | --- |
| CNAME | mail.example.com | smtp.sparkpostmail.com | Alinhamento de Return-jornada / SPF |
| TXT | scph1226._domainkey.mail.example.com | v=DKIM1; k=rsa; p=... | Autenticação criptográfica DKIM |
| CNAME | click.mail.example.com | spgo.io (ou endpoint CDN) | Rastreamento de cliques e aberturas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Exemplo de tabela DNS do SparkPost" }

### Arquitetura SendGrid {#sendgrid-architecture}

O SendGrid utiliza uma infraestrutura automatizada conhecida como Domain Authentication. Em vez de fornecer chaves `TXT` brutas, o SendGrid fornece uma série de registros `CNAME` que apontam diretamente para servidores gerenciados pelo SendGrid.

- Configuração de SPF e Return-jornada: o SendGrid usa um `CNAME` específico (geralmente prefixado com `em`) mapeando seu subdomínio de envio para `uXXXXXX.wl.sendgrid.net`. O SendGrid hospeda e atualiza dinamicamente o registro SPF nesse endpoint.
- Configuração de DKIM: o SendGrid gera dois registros `CNAME` separados para DKIM (geralmente usando seletores como `s1` e `s2`). Eles apontam de volta para as chaves do SendGrid.
- O SendGrid fornece dois registros `CNAME` de DKIM para que possa rotacionar as chaves criptográficas automaticamente sem exigir que você atualize seu DNS manualmente.

#### Exemplo de tabela DNS do SendGrid {#example-sendgrid-dns-table}

A tabela a seguir mostra exemplos de registros DNS para uma configuração SendGrid.

| Tipo de registro | Host/Nome | Valor/Destino | Finalidade |
| --- | --- | --- | --- |
| CNAME | em.mail.example.com | u123456.wl.sendgrid.net | Return-jornada / SPF dinâmico |
| CNAME | s1._domainkey.mail.example.com | s1.domainkey.u123456.wl.sendgrid.net | Chave DKIM primária (rotacional) |
| CNAME | s2._domainkey.mail.example.com | s2.domainkey.u123456.wl.sendgrid.net | Chave DKIM secundária (rotacional) |
| CNAME | email.mail.example.com | sendgrid.net (ou endpoint CDN) | Rastreamento de cliques e aberturas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Exemplo de tabela DNS do SendGrid" }

### Arquitetura Amazon SES {#amazon-ses-architecture}

O Amazon SES usa Easy DKIM com registros `CNAME` junto com roteamento explícito de `MX` e `TXT` para rastreamento personalizado de bounces.

- Configuração de DKIM: o Amazon SES usa Easy DKIM, fornecendo três registros `CNAME`. Eles apontam para subdomínios gerenciados pela AWS contendo as chaves públicas. O SES rotaciona essas chaves automaticamente de forma transparente para manter a conformidade de segurança.
- Configuração de SPF e MAIL FROM personalizado: o SendGrid e o SparkPost gerenciam o roteamento do domínio de bounce por meio de um `CNAME`. O Amazon SES requer um registro `MX` explícito e um registro `TXT` colocados diretamente no subdomínio MAIL FROM designado. O registro `MX` garante que os avisos de bounce retornem aos servidores da Amazon, e o registro `TXT` contém a string SPF autorizada codificada.

Para saber mais, consulte [Configuração do Amazon SES]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses).

#### Exemplo de tabela DNS do Amazon SES {#example-amazon-ses-dns-table}

A tabela a seguir mostra exemplos de registros DNS para uma configuração Amazon SES.

| Tipo de registro | Host/Nome | Valor/Destino | Finalidade |
| --- | --- | --- | --- |
| CNAME | sel1._domainkey.mail.example.com | sel1.dkim.amazonses.com | Chave Easy DKIM 1 (rotacional) |
| CNAME | sel2._domainkey.mail.example.com | sel2.dkim.amazonses.com | Chave Easy DKIM 2 (rotacional) |
| CNAME | sel3._domainkey.mail.example.com | sel3.dkim.amazonses.com | Chave Easy DKIM 3 (rotacional) |
| MX | bounce.mail.example.com | 10 feedback-smtp.us-east-1.amazonses.com | Roteia o processamento de bounces para a AWS |
| TXT | bounce.mail.example.com | v=spf1 include:amazonses.com ~all | Autorização SPF explícita |
| CNAME | track.mail.example.com | r.us-east-1.awstrack.me (ou CDN) | Rastreamento de cliques e aberturas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Exemplo de tabela DNS do Amazon SES" }

## Considerações avançadas de DNS {#advanced-dns-considerations}

### Divisão de string de registro TXT DKIM {#txt-dkim-record-string-splitting}

Ao implantar o SparkPost ou configurações manuais de DKIM, você pode encontrar chaves criptográficas longas (chaves DKIM de 2048 bits).

A especificação principal de DNS (RFC 1035) limita qualquer string de caracteres individual dentro de um registro `TXT` a um máximo de 255 caracteres. Uma chave pública de 2048 bits rotineiramente excede 400 caracteres, fazendo com que registros de domínio rejeitem a string única ou a truncem, invalidando a assinatura.

A divisão de string resolve esse problema. Quebre a string de caracteres em blocos de menos de 255 caracteres. Coloque cada bloco entre aspas retas, separados por um espaço, dentro do mesmo registro `TXT`.

{% alert note %}
Quando você usa provedores DNS como Cloudflare ou AWS Route 53, essas interfaces lidam automaticamente com a divisão quando você cola uma string longa. Sistemas legados (como GoDaddy ou Network Solutions) exigem que você formate manualmente a divisão usando a técnica de aspas duplas.
{% endalert %}

### Use subdomínios dedicados {#dedicated-subdomains}

Um erro comum durante a integração é solicitar o uso de um domínio organizacional de nível superior (como `example.com`) diretamente na Braze como domínio de envio. A Braze exige o uso de um subdomínio dedicado (por exemplo, `mail.example.com` ou `engage.example.com`).

Usar o domínio principal pode prejudicar a infraestrutura corporativa das seguintes formas:

#### Conflitos de registro MX {#mx-record-conflicts}

Um domínio só pode suportar um conjunto de registros `MX` de roteamento primário. Se você mapear seu domínio principal (`example.com`) para a infraestrutura do provedor de serviços de e-mail da Braze, os registros `MX` personalizados necessários para bounces sobrescrevem seus registros de e-mail corporativo. Isso pode interromper plataformas de envio de mensagens internas corporativas como Google Workspace ou Microsoft 365.

#### Excesso de includes SPF e o limite de 10 consultas {#spf-include-bloat-and-the-10-lookup-limit}

A especificação SPF (RFC 7208) limita os servidores de e-mail receptores a um máximo de 10 consultas DNS ao validar um registro SPF.

- Se um domínio principal adicionar os mecanismos do provedor de serviços de e-mail da Braze (`include:sparkpostmail.com` ou `include:amazonses.com`), isso conta significativamente contra esse limite.
- Se o limite for excedido, isso dispara um SPF PermError permanente, fazendo com que todos os e-mails corporativos falhem na autenticação.

#### Isolamento de reputação de IP e domínio {#ip-and-domain-reputation-isolation}

Se campanhas de marketing, recibos transacionais e e-mails internos de colaboradores compartilham um espaço de domínio raiz idêntico, um pico repentino de reclamações de SPAM em marketing pode prejudicar a reputação do domínio principal. Isso coloca em risco o encaminhamento de comunicações corporativas críticas para pastas de SPAM. Usar um subdomínio distinto isola a reputação do seu alcance de marketing.

## Fluxo de trabalho de implementação {#implementation-workflow}

Para garantir uma transição e implementação tranquilas, siga esta sequência:

1. Forneça os registros estruturados ao seu administrador de TI ou de rede para adicioná-los à sua plataforma de hospedagem (Cloudflare, Route 53 e assim por diante).
2. Defina um valor baixo de Time-To-Live (TTL) (por exemplo, 300 segundos ou cinco minutos) para os testes iniciais. Isso permite uma recuperação rápida caso ocorra um erro de digitação durante a inserção.
3. Execute uma consulta DNS (por exemplo, `dig CNAME mail.example.com`) ou use uma ferramenta de validação para confirmar que os registros estão resolvendo corretamente antes de prosseguir para a fase de aquecimento.

## Documentação de provedores DNS {#dns-provider-documentation}

Cada provedor DNS possui uma interface única. Compartilhe essas especificações com o administrador de rede ou consulte a documentação do seu provedor específico para mapear as entradas corretamente no seu arquivo de zona.

A tabela a seguir lista a documentação oficial dos provedores DNS mais utilizados.

| Provedor DNS | Recursos |
| --- | --- |
| Cloudflare | [Gerenciar registros DNS](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Amazon Route 53 | [Criar conjuntos de registros de recursos](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html) |
| GoDaddy | [Gerenciar registros DNS](https://www.godaddy.com/help/manage-dns-records-680) |
| Google Cloud DNS | [Configurar registros DNS para um nome de domínio](https://cloud.google.com/dns/docs/set-up-dns-records-domain-name) |
| Microsoft Azure DNS | [Gerenciar registros DNS usando o portal do Azure](https://learn.microsoft.com/en-us/azure/dns/dns-operations-recordsets-portal) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Documentação de provedores DNS" }

Para recursos adicionais sobre provedores de domínio, consulte [Configurar IPs e domínios]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains#step-2-add-and-verify-a-sending-domain).