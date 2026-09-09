---
nav_title: Configuração do Amazon SES
article_title: Configuração do Amazon SES
page_order: 1
page_type: reference
description: "Este artigo de referência explica como configurar o Amazon SES como seu prestador de serviço de e-mail."
channel: email
---

# Configuração do Amazon SES {#amazon-ses-setup}

> A Braze usa o Amazon Simple Email Service (SES) como prestador de serviço de e-mail padrão durante a configuração de um novo e-mail. Se a configuração necessária não estiver alinhada com os recursos do Amazon SES, fale com o suporte da Braze para ter a opção de concluir a configuração no SparkPost ou SendGrid.

## Pré-requisitos {#prerequisites}

Antes de iniciar a configuração do Amazon SES, confirme que você tem o seguinte:

- Nomes de domínio de envio
- Nomes de pool de IP (como marketing, transacional, staging)
- O número de endereços IP para cada pool de IP
- Sufixo preferido para domínios de rastreamento de cliques (como "clicks" ou "click", "links" ou "link")

## Exemplo de configuração {#setup-example}

Uma configuração típica do Amazon SES é semelhante à seguinte:

- **Nome da subconta:** braze
- **Cluster:** eu-02

| Pool de IP | Número de IPs | Conjunto de configuração | Domínio de envio | Domínio de rastreamento de cliques |
| --- | --- | --- | --- | --- |
| `eu02_braze_marketing` | 1 IP | `eu02_braze_marketing_set1` | `demo.braze.com` | `clicks.demo.braze.com` |
| `eu02_braze_transactional` | 1 IP | `eu02_braze_transactional_set1` | `dev.braze.com` | `clicks.dev.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Exemplo de configuração" }

{% alert note %}
O cluster e o nome da subconta são automaticamente adicionados aos pools de IP e conjuntos de configuração.
{% endalert %}

## Exemplos de configuração de domínio de rastreamento de cliques {#click-tracking-domain-configuration-examples}

As tabelas a seguir são exemplos de possíveis configurações de domínio de rastreamento de cliques com base na sua preferência de branding.

### Um domínio de rastreamento de cliques para cada domínio de envio {#one-click-tracking-domain-for-each-sending-domain}

| Pool de IP de marketing | Conjunto de configuração | Subdomínios de envio | Domínios de rastreamento de cliques |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set1 | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set2 | `email2.example.com` | `clicks.email2.example.com` |
| braze_marketing - 1 IP | braze_marketing_set3 | `email3.example.com` | `clicks.email3.example.com` |
| braze_marketing - 1 IP | braze_marketing_set4 | `email4.example.com` | `clicks.email4.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Um domínio de rastreamento de cliques para cada domínio de envio" }

### Um domínio de rastreamento de cliques para todos os domínios de envio {#one-click-tracking-domain-for-all-sending-domains}

Isso se baseia na regra de que o domínio de rastreamento de cliques precisa corresponder a pelo menos um domínio de envio do conjunto de configuração.

| Pool de IP de marketing | Conjunto de configuração | Subdomínios de envio | Domínios de rastreamento de cliques |
| --- | --- | --- | --- |
| braze_marketing - 1 IP | braze_marketing_set | `email1.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email2.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email3.example.com` | `clicks.email1.example.com` |
| braze_marketing - 1 IP | braze_marketing_set | `email4.example.com` | `clicks.email1.example.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Um domínio de rastreamento de cliques para todos os domínios de envio" }

## Considerações {#considerations}

- Os pools de IP na Amazon SES hospedam apenas o endereço IP em si, enquanto os conjuntos de configuração hospedam os domínios de envio e o domínio de rastreamento de cliques.
- Cada conjunto de configuração pode ter apenas um pool de IP atribuído a ele por vez, mas é possível criar vários conjuntos de configuração que usam o mesmo pool de IP com domínios de envio diferentes.
- A Amazon SES gerencia os registros rDNS e A internamente, pois mantém relacionamentos próximos com provedores de caixa de entrada para ajudar a reconhecer endereços IP.
- Cada domínio de envio tem um identificador MAIL FROM associado a ele para ajudar nas validações de SPF.
    - O valor para cada domínio de envio é "e".
    - O valor MAIL FROM não altera o endereço de remetente que seus clientes visualizam.
- O início do período de mensagem trap e o fim do período de mensagem trap não estão disponíveis se você estiver usando a Amazon SES como seu provedor de serviços de e-mail.

## Próximas etapas {#next-steps}

{% article_tiles %}
- name: Configurar SSL
  link: /docs/user_guide/channels/email/email_setup/ssl
{% endarticle_tiles %}