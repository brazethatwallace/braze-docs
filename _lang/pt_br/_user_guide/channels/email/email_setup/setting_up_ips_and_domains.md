---
nav_title: Configurar IPs e domínios
article_title: Configurar IPs e domínios
page_order: 0
page_type: tutorial
channel: email
description: "Este artigo explica como configurar endereços IP, pools de IP, domínios e subdomínios para o envio de e-mails pela Braze."
---

# Configurar IPs e domínios {#set-up-ips-and-domains}

> Este artigo apresenta os requisitos e as etapas necessárias para configurar seus endereços IP e pools de IP, além dos domínios e subdomínios necessários antes de começar a enviar e-mails com a Braze.

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
A partir de 2026, a Braze usa o Amazon Simple Email Service (SES) como provedor de serviços de e-mail (ESP) padrão para novas configurações de e-mail. Para mais detalhes, consulte [Configuração do Amazon SES]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses).
{% endalert %}

## Método 1: Configuração de e-mail por autoatendimento {#method-1-self-service-email-setup}

Este método configura seus domínios de envio e rastreamento para uma empresa. Você precisará consultar a equipe de integração da Braze primeiro e enviar as seguintes informações ao seu representante da Braze para que seus pools de IP e endereços IP sejam adicionados:

- Seus domínios e subdomínios escolhidos
- O número aproximado de e-mails que você envia por mês, o que ajuda a determinar quantos IPs você precisa
- Como você prefere mapear seus domínios de envio para os pools de IP alocados

### Pré-requisitos {#prerequisites}

Para usar a configuração de e-mail por autoatendimento, confirme que você atende aos seguintes pré-requisitos:

- Você é um novo cliente em integração.
- Você tem a permissão de nível de empresa "Edit Domain Settings".

### Etapa 1: Iniciar a configuração {#step-1-begin-setup}

1. Acesse **Configurações** > **Email Self Serve** em **Configurações da empresa**.
2. Selecione **Start setup**.

### Etapa 2: Adicionar e verificar um domínio de envio {#step-2-add-and-verify-a-sending-domain}

Um domínio de envio é usado no endereço de remetente ao enviar um e-mail.

1. Insira um domínio de envio e selecione **Submit**.
2. Adicione os registros TXT e CNAME da parte inferior da página ao seu provedor DNS.

![Seção de registros DNS mostrando registros TXT e CNAME para copiar no seu sistema de gerenciamento de domínio.]({% image_buster /assets/img/email_setup/dns_records.png %})

{: start="3"}
3. Retorne ao dashboard da Braze e selecione **Verify**.

Peça aos seus engenheiros e desenvolvedores para adicionar esses registros DNS onde necessário. Para explicações detalhadas sobre como os registros DNS funcionam nos provedores de serviços de e-mail da Braze, incluindo SPF, DKIM, DMARC e estruturas de registros específicas de cada provedor, consulte [Entendendo os registros DNS]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/understanding_dns_records).

{% multi_lang_include channels/email/dns_records.md %}

Se a verificação falhar e você acreditar que seus registros DNS estão corretos, entre em contato com o suporte da Braze para obter assistência.

{% alert important %}
O domínio de envio deve ser subordinado a um domínio que você possui. Por exemplo, se você possui "example.com", um subdomínio poderia ser "mail.example.com", o que permite usar o endereço de envio "@mail.example.com".
{% endalert %}

### Etapa 3: Adicionar e verificar um domínio de rastreamento {#step-3-add-and-verify-a-tracking-domain}

Um domínio de rastreamento é usado para encapsular links nos seus e-mails para fins de rastreamento de cliques e branding. Ele fica visível para os destinatários quando passam o cursor sobre os links do e-mail ou clicam neles. A Braze recomenda que ele corresponda ao seu domínio de envio.

1. Insira um domínio de rastreamento e selecione **Submit**.
2. Adicione os registros CNAME da parte inferior da página ao seu provedor DNS.
3. Retorne ao dashboard da Braze e selecione **Verify**.

### Etapa 4: Adicionar um endereço IP {#step-4-add-an-ip-address}

A Braze gera um registro A para associar seu endereço IP ao seu subdomínio de envio em uma configuração chamada DNS reverso (rDNS). Adicione o registro A no seu provedor DNS e selecione **Set up rDNS** para dar suporte à entregabilidade.

Para adicionar ou editar seus endereços IP de um pool de IP, entre em contato com o suporte da Braze.

#### Pools de IP com mais de um IP dedicado {#ip-pools-with-more-than-one-dedicated-ip}

Quando um pool de IP contém vários endereços IP dedicados, a Braze e seu provedor de serviços de e-mail distribuem envios grandes entre esses IPs para capacidade e entregabilidade. A distribuição é aproximada — nem toda mensagem em uma Campaign usa todos os IPs, e envios menores podem parecer desiguais entre os endereços. O SendGrid frequentemente processa e-mails em lotes (na ordem de aproximadamente 1.500 mensagens por lote), então o volume nem sempre se divide em uma proporção estritamente proporcional entre os IPs. Se você envia rotineiramente um volume diário muito alto, discuta o dimensionamento do pool com seu contato de integração ou sucesso do cliente da Braze.

### Próximas etapas {#next-steps}

Após a verificação do remetente ser concluída, a Braze recomenda o aquecimento de IP para que suas mensagens cheguem às caixas de entrada de destino com uma taxa consistentemente alta. Use o [aquecimento de IP automatizado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/automated_ip_warming) para ajudar a configurar e monitorar seu cronograma de aquecimento.

Após concluir essa configuração, consulte a equipe de integração da Braze para confirmar se seus domínios e o [aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) estão funcionando.

## Método 2: Domínios verificados {#method-2-verified-domains}

Os domínios verificados permitem que você conceda à Braze o controle de um subdomínio específico para que a Braze possa automatizar a configuração de e-mail e o rastreamento de cliques por HTTPS. Com a delegação de domínio DNS, a Braze gerencia os registros DNS necessários para o envio de e-mail e o rastreamento de cliques. Por exemplo, se o seu subdomínio for "mail.example.com", você pode delegá-lo à Braze para configurar seus domínios de envio e rastreamento.

{% alert important %}
Atualmente, os domínios verificados são compatíveis apenas com o Amazon SES. Se você estiver usando o SendGrid ou o SparkPost, esse recurso não está disponível.<br><br>Os domínios verificados são compatíveis apenas com e-mail. {% multi_lang_include product_feedback_cta.md context="gap" feature="verified domains for channels other than email" %}
{% endalert %}

### Configuração {#setup}

#### Etapa 1: Coordenar com a Braze {#step-1-coordinate-with-braze}

Envie as seguintes informações ao seu representante da Braze:

- Seus domínios e subdomínios escolhidos
- Como você prefere mapear seus domínios para seus pools de IP
- O número aproximado de e-mails que você planeja enviar por mês em cada subdomínio, o que ajuda a determinar quantos IPs são necessários para seus pools de IP
- Quaisquer preocupações anteriores com entregabilidade que devam ser sinalizadas

#### Etapa 2: A Braze configura as informações {#step-2-braze-configures-information}

Após receber seu e-mail, a Braze adiciona o número esperado de IPs e pools de IP. Depois que os pools de IP e os endereços IP forem adicionados, siga as etapas em [Domínios verificados]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/verified_domains).