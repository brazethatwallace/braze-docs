---
nav_title: Configurar IPs e domínios
article_title: Configurar IPs e domínios
page_order: 0
page_type: tutorial
channel: email
description: "Este artigo tutorial vai orientar você sobre como configurar seus IPs e domínios para enviar e-mails pela Braze."

---

# Configurar IPs e domínios

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

> Este artigo apresenta os requisitos e as etapas necessárias para configurar seus endereços IP e pools de IP, além dos domínios e subdomínios necessários antes de começar a enviar e-mails com a Braze. <br><br>Embora a maior parte do processo de configuração seja feita pela Braze, descrevemos os requisitos e materiais para essa configuração.

<br>

{% alert important %}
Você pode usar SendGrid, SparkPost ou Amazon Simple Email Service (SES) como seu parceiro de prestador de serviço de e-mail (ESP). A partir de 2026, a Braze usa o Amazon SES como ESP padrão para novas configurações de e-mail. Para mais detalhes, consulte [Configuração do Amazon SES]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/amazon_ses).
{% endalert %}

## Método 1: Coordenar com a Braze (recomendado)

### Etapa 1: Descrever as informações

Envie as seguintes informações ao seu representante da Braze:

* Seus domínios e subdomínios escolhidos
* O número aproximado de e-mails que você enviará por mês, o que ajudará a determinar quantos IPs serão necessários
* Como você prefere mapear seus domínios de envio para os IPs alocados

### Etapa 2: A Braze configura as informações

Após receber seu e-mail, começaremos a configurar seus IPs, domínios e subdomínios, e pools de IP.

### Etapa 3: Adicionar registros DNS

Após a configuração dos seus IPs, domínios, subdomínios e pools de IP, enviaremos uma lista de registros DNS. Peça aos seus engenheiros e desenvolvedores que adicionem esses registros DNS onde necessário e, depois que forem adicionados, avise a equipe de integração da Braze.

{% multi_lang_include dns_records.md %}

Após a Braze fornecer seus registros DNS, adicione-os assim que sua equipe de DNS ou de TI puder. A verificação de domínio tem prazo limitado, e se os registros forem adicionados tarde demais, a verificação pode falhar mesmo que os registros DNS sejam resolvidos corretamente depois. Se seus registros DNS parecerem corretos, mas a verificação falhar, entre em contato com a equipe de integração ou suporte da Braze para reiniciar a verificação.

### Próximas etapas

Verificaremos sua configuração e validaremos todas as informações em nossos sistemas internos. A equipe de integração da Braze avisará quando tudo estiver pronto ou se houver problemas com seus registros DNS que precisem ser resolvidos com sua equipe de engenharia.

## Método 2: Configuração de e-mail por autoatendimento

Este método configura um domínio de envio, um domínio de rastreamento e um IP no total para uma empresa. Se você planeja configurar mais, consulte a equipe de integração da Braze (método 1).

{% multi_lang_include early_access_beta_alert.md feature='This self-service email setup feature' type='beta' %}
<br>Se você estiver usando o recurso de configuração de e-mail por autoatendimento, consulte também a equipe de integração da Braze.

### Pré-requisitos

Para usar a configuração de e-mail por autoatendimento, você deve atender aos seguintes pré-requisitos:

1. Você é um novo cliente em integração.
2. Você tem a permissão de nível de empresa "Manage Company Settings".

### Etapa 1: Iniciar a configuração

1. Acesse **Settings** > **Admin Settings** em **Company Settings**.
2. Em seguida, selecione a guia **Sender Verification**. Para visualizar essa guia, você deve ter a permissão de nível de empresa "Manage Company Settings".
3. Selecione **Start setup**.

### Etapa 2: Adicionar e verificar um domínio de envio

Um domínio de envio é usado no endereço "de" ao enviar um e-mail. Insira um domínio de envio e clique em **Submit**.

Em seguida, adicione os registros TXT e CNAME da parte inferior da página ao seu provedor DNS. Depois, volte ao dashboard da Braze e clique em **Verify**.

![]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

Se a verificação falhar e você acreditar que seus registros DNS estão corretos, entre em contato com o suporte da Braze para obter assistência.

{% alert important %}
O domínio de envio deve ser um subdomínio de um domínio que você possui. Por exemplo, se você possui "example.com", um subdomínio poderia ser "mail.example.com", o que permite usar o endereço de envio "@mail.example.com".
{% endalert %}

### Etapa 3: Adicionar e verificar um domínio de rastreamento

Um domínio de rastreamento é usado para encapsular links nos seus e-mails para fins de rastreamento de cliques e branding. Ele ficará visível para os usuários quando passarem o mouse sobre os links do e-mail ou clicarem neles. Recomendamos que ele corresponda ao seu domínio de envio.

1. Insira um domínio de rastreamento e selecione **Submit**.
2. Em seguida, adicione os registros CNAME da parte inferior da página ao seu provedor DNS.
3. Depois, volte ao dashboard da Braze e selecione **Verify**.

### Etapa 4: Adicionar um endereço IP

A Braze gera um registro A para associar seu endereço IP ao seu subdomínio de envio em uma configuração chamada DNS reverso (rDNS). Adicione o registro A no seu provedor DNS e clique em **Set up rDNS** para dar suporte à entregabilidade.

Observe que domínios adicionais que foram incluídos não aparecem na seção **Sender Verification**. Para adicionar mais domínios, entre em contato com a equipe de suporte da Braze.

### Próximas etapas

Após a conclusão da verificação do remetente, recomendamos o aquecimento de IP para que suas mensagens cheguem às caixas de entrada de destino com uma taxa consistentemente alta. Depois de concluir essa configuração, consulte também a equipe de integração da Braze para confirmar se seus domínios e [endereço IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) estão funcionando.