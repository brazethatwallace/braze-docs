---
nav_title: Configurar IPs e domínios
article_title: Configurar IPs e domínios
page_order: 0
page_type: tutorial
channel: email
description: "Este artigo explica como configurar seus IPs e domínios para o envio de e-mails pela Braze."

---

# Configurar IPs e domínios {#set-up-ips-and-domains}

> Este artigo apresenta os requisitos e as etapas necessárias para configurar seus endereços IP e pools de IP, além dos domínios e subdomínios necessários antes de começar a enviar e-mails com a Braze.

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

<br>

{% alert important %}
Você pode usar SendGrid, SparkPost ou Amazon Simple Email Service (SES) como seu parceiro de prestador de serviço de e-mail (ESP). A partir de 2026, a Braze usa o Amazon SES como ESP padrão para novas configurações de e-mail. Para mais detalhes, consulte [Configuração do Amazon SES]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses/).
{% endalert %}

## Método 1: Coordenar com a Braze (recomendado) {#method-1-coordinate-with-braze-recommended}

### Etapa 1: Informações gerais {#step-1-outline-information}

Envie as seguintes informações ao seu representante da Braze:

* Seus domínios e subdomínios escolhidos
* O número aproximado de e-mails que você enviará por mês, o que ajudará a determinar quantos IPs serão necessários
* Como você prefere mapear seus domínios de envio para os IPs alocados

### Etapa 2: A Braze configura as informações {#step-2-braze-configures-information}

Após receber seu e-mail, começaremos a configurar seus IPs, domínios e subdomínios, e pools de IP.

### Etapa 3: Adicionar registros DNS {#step-3-add-dns-records}

Após a configuração dos seus IPs, domínios, subdomínios e pools de IP, enviaremos uma lista de registros DNS. Peça aos seus engenheiros e desenvolvedores que adicionem esses registros DNS onde necessário e, depois que forem adicionados, avise a equipe de integração da Braze.

{% multi_lang_include dns_records.md %}

Após a Braze fornecer seus registros DNS, adicione-os assim que sua equipe de DNS ou de TI puder. A verificação de domínio tem prazo limitado, e se os registros forem adicionados tarde demais, a verificação pode falhar mesmo que os registros DNS sejam resolvidos corretamente depois. Se seus registros DNS parecerem corretos, mas a verificação falhar, entre em contato com a equipe de integração ou o suporte da Braze para reiniciar a verificação.

### Próximas etapas {#next-steps}

Verificaremos sua configuração e validaremos todas as informações em nossos sistemas internos. A equipe de integração da Braze avisará quando tudo estiver pronto ou se houver problemas com seus registros DNS que precisem ser resolvidos com sua equipe de engenharia.

## Método 2: Configuração de e-mail por autoatendimento {#method-2-self-service-email-setup}

Este método configura um domínio de envio, um domínio de rastreamento e um IP no total para uma empresa. Se você planeja configurar mais, consulte a equipe de integração da Braze (método 1).

{% multi_lang_include early_access_beta_alert.md feature='This self-service email setup feature' type='beta' %}
<br>Se você estiver usando o recurso de configuração de e-mail por autoatendimento, consulte também a equipe de integração da Braze.

### Pré-requisitos {#prerequisites}

Para usar a configuração de e-mail por autoatendimento, você deve atender aos seguintes pré-requisitos:

1. Você é um novo cliente em integração.
2. Você tem a permissão de nível de empresa "Manage Company Settings".

### Etapa 1: Iniciar a configuração {#step-1-begin-setup}

1. Acesse **Configurações** > **Configurações de administrador** em **Configurações da empresa**.
2. Em seguida, selecione a guia **Verificação do remetente**. Para visualizar essa guia, você deve ter a permissão de nível de empresa "Manage Company Settings".
3. Selecione **Iniciar configuração**.

### Etapa 2: Adicionar e verificar um domínio de envio {#step-2-add-and-verify-a-sending-domain}

Um domínio de envio é usado no endereço "de" ao enviar um e-mail. Insira um domínio de envio e clique em **Enviar**.

Em seguida, adicione os registros TXT e CNAME da parte inferior da página ao seu provedor DNS. Depois, volte ao dashboard da Braze e clique em **Verificar**.

![]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

Se a verificação falhar e você acreditar que seus registros DNS estão corretos, entre em contato com o suporte da Braze para obter assistência.

{% alert important %}
O domínio de envio deve ser um subdomínio de um domínio que você possui. Por exemplo, se você possui "example.com", um subdomínio poderia ser "mail.example.com", o que permite usar o endereço de envio "@mail.example.com".
{% endalert %}

### Etapa 3: Adicionar e verificar um domínio de rastreamento {#step-3-add-and-verify-a-tracking-domain}

Um domínio de rastreamento é usado para encapsular links nos seus e-mails para fins de rastreamento de cliques e branding. Ele ficará visível para os usuários quando passarem o mouse sobre os links do e-mail ou clicarem neles. Recomendamos que ele corresponda ao seu domínio de envio.

1. Insira um domínio de rastreamento e selecione **Enviar**.
2. Em seguida, adicione os registros CNAME da parte inferior da página ao seu provedor DNS.
3. Depois, volte ao dashboard da Braze e selecione **Verificar**.

### Etapa 4: Adicionar um endereço IP {#step-4-add-an-ip-address}

A Braze gera um registro A para associar seu endereço IP ao seu subdomínio de envio em uma configuração chamada DNS reverso (rDNS). Adicione o registro A no seu provedor DNS e clique em **Configurar rDNS** para dar suporte à entregabilidade.

Observe que domínios adicionais que foram incluídos não aparecem na seção **Verificação do remetente**. Para adicionar mais domínios, entre em contato com a equipe de suporte da Braze.

### Pools de IP com mais de um IP dedicado {#ip-pools-with-more-than-one-dedicated-ip}

Quando um pool de IP contém vários endereços IP dedicados, a Braze e seu prestador de serviço de e-mail distribuem envios grandes entre esses IPs para capacidade e entregabilidade. A distribuição é aproximada — nem toda mensagem em uma campanha usa todos os IPs, e envios menores podem parecer desiguais entre os endereços. O SendGrid geralmente processa e-mails em blocos (na ordem de aproximadamente 1.500 mensagens por bloco), então o volume nem sempre se divide em uma proporção estrita de um para um entre os IPs. Se você envia rotineiramente um volume diário muito alto, discuta o dimensionamento do pool com seu contato de integração ou de sucesso do cliente na Braze.

### Próximas etapas

Após a conclusão da verificação do remetente, recomendamos o aquecimento de IP para que suas mensagens cheguem às caixas de entrada de destino com uma taxa consistentemente alta. Depois de concluir essa configuração, consulte também a equipe de integração da Braze para confirmar se seus domínios e [endereço IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/) estão funcionando.