---
nav_title: VideoSmart
article_title: VideoSmart
description: "Este artigo de referência descreve a parceria entre a Braze e a VideoSmart, uma tecnologia de vídeo personalizado e interativo que permite que as marcas entreguem conteúdo não linear e orientado por dados em escala."
alias: /partners/videosmart/
page_type: partner
search_tag: Partner
---

# VideoSmart

> A [VideoSmart](https://www.videosmart.com/) oferece tecnologia de vídeo personalizado e interativo que permite entregar conteúdo não linear e orientado por dados em escala. Cada vídeo é gerado dinamicamente usando dados no nível do cliente, permitindo mensagens personalizadas e jornadas do usuário dentro de uma única experiência de vídeo.
>
> A integração com a VideoSmart permite incorporar conteúdo de vídeo personalizado em Campaigns de e-mail usando Connected Content da Braze e modelos Liquid para solicitar ativos de vídeo da VideoSmart. Essa integração é normalmente implementada por meio de um modelo reutilizável de bloco de conteúdo da Braze, permitindo implantação consistente entre Campaigns e flexibilidade na seleção de Campaigns e na lógica de personalização.

_Esta integração é desenvolvida e mantida pela VideoSmart._

## Sobre esta integração {#about-this-integration}

A VideoSmart se integra com a Braze para gerar dinamicamente ativos de vídeo personalizados no momento do envio, que são então incorporados diretamente no conteúdo de e-mail das suas Campaigns e Canvas na Braze.

Na Braze, você seleciona a campanha VideoSmart relevante e passa atributos do cliente (por meio de modelos Liquid) para a VideoSmart no momento do envio. Esses atributos são usados para renderizar uma experiência de vídeo única e personalizada para cada destinatário. Você pode então usar o Connected Content da Braze para solicitar URLs de vídeo ou ativos da API da VideoSmart em tempo real, permitindo personalização em escala.

Esta integração foi projetada para mensagens de e-mail da Braze que suportam modelos Liquid e Connected Content, e pode ser configurada para funcionar com atributos padrão do perfil de usuário da Braze ou campos de dados personalizados.

## Casos de uso {#use-cases}


Os casos de uso mais comuns incluem:

- Integração e jornadas de boas-vindas de clientes
- Educação financeira (como previdência e apólices de seguro)
- Extratos anuais e comunicações regulatórias
- Campanhas de conscientização de produto e venda cruzada
- Campanhas de retenção e reengajamento de clientes
- Lembretes de carrinho abandonado: quando um cliente adiciona produtos ao carrinho mas não finaliza a compra, você envia um e-mail com um vídeo personalizado que destaca os itens que ele deixou para trás
- Acompanhamento pós-compra: após uma compra, envie um vídeo personalizado de agradecimento e recomende produtos relacionados

## Pré-requisitos {#prerequisites}

Antes de começar, confirme que você tem o seguinte:

| Requisito | Descrição |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Credenciais de Connected Content da Braze | Uma credencial de autenticação básica de Connected Content chamada **basic_credentials**, configurada com os valores fornecidos pela VideoSmart |
| Modelo de **VideoSmart Content Block** | O modelo de **VideoSmart Content Block** adicionado ao seu dashboard da Braze (fornecido pela VideoSmart) |
| Uma mensagem de e-mail da Braze | Um e-mail de Campaign da Braze ou uma etapa de e-mail do Canvas onde você inserirá o **VideoSmart Content Block** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Siga estas etapas para ativar o **VideoSmart Content Block** e usá-lo em um e-mail.

### Etapa 1: Configurar o modelo de VideoSmart Content Block na Braze {#step-1-set-up-the-videosmart-content-block-template-in-braze}

Solicite o modelo de **VideoSmart Content Block** ao seu representante da VideoSmart e adicione-o ao seu dashboard da Braze.

A VideoSmart fornecerá as credenciais para a autenticação de Connected Content usada pelo Content Block.

### Etapa 2: Configurar a autenticação de Connected Content {#step-2-set-up-connected-content-authentication}

Crie uma credencial de autenticação básica de Connected Content na Braze chamada "basic_credentials".

- Siga as instruções em [Usando autenticação básica]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-basic-authentication).
- Use o nome de usuário e a senha fornecidos pela VideoSmart.

### Etapa 3: Adicionar o Content Block ao seu e-mail {#step-3-add-the-content-block-to-your-email}

Insira o **VideoSmart Content Block** no seu e-mail onde você deseja que o conteúdo de vídeo apareça.

Na maioria das configurações da Braze, os Content Blocks são referenciados usando o seguinte padrão (substitua "VideoSmart_Campaign" pelo nome do Content Block na sua conta):

{% raw %}`{{content_blocks.${VideoSmart_Campaign}}}`{% endraw %}

{% alert important %}
O nome do Content Block diferencia maiúsculas de minúsculas e deve corresponder exatamente ao que você configurou na Braze.
{% endalert %}

### Etapa 4: Substituir campanha e dados de registro (opcional) {#step-4-override-campaign-and-record-data-optional}

Se o seu Content Block suporta valores padrão, você pode usá-lo sem definir nenhuma variável.

Se você precisar escolher uma campanha VideoSmart específica, passar campos de personalização personalizados, ou ambos, defina as seguintes variáveis Liquid antes de renderizar o Content Block:

- `vs_campaign_id`: identificador da campanha VideoSmart
- `vs_record_data`: uma string JSON contendo os valores que você deseja passar para o modelo da VideoSmart

#### Exemplo {#example}

Este exemplo usa atributos de usuário da Braze para o nome e o sobrenome:

{% raw %}
```liquid
{% assign vs_campaign_id = "CAMPAIGN_ID" %}

{% capture vs_record_data %}
{
  "FirstName": "{{ ${first_name} | default: 'Alex' | json_escape }}",
  "LastName": "{{ ${last_name} | default: 'Doe' | json_escape }}"
}
{% endcapture %}
{% assign vs_record_data = vs_record_data | strip_newlines %}
```
{% endraw %}

{% alert note %}
- Sempre forneça valores padrão para os valores usados em `vs_record_data` para que a prévia do e-mail da Braze seja exibida corretamente.
- `vs_record_data` deve ser um JSON válido, codificado como uma única string (o exemplo usa `strip_newlines`).
{% endalert %}

### Etapa 5: Usar as variáveis geradas pelo modelo de VideoSmart Content Block {#step-5-use-the-variables-generated-by-videosmarts-content-block-template}

Após a execução do Content Block, ele gera variáveis que você pode referenciar em outras partes do seu e-mail.

As variáveis comuns incluem:

{% raw %}
| Variável | Descrição |
| --------------------------------- | ----------------------------------------------------- |
| `{{ video_url }}` | URL do vídeo personalizado |
| `{{ poster_url }}` | URL da imagem de pôster do vídeo |
| `{{ output_data.VARIABLE_NAME }}` | Campos de saída adicionais expostos pelo Content Block |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 5: Usar as variáveis geradas pelo modelo de VideoSmart Content Block" }
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 5: Usar as variáveis geradas pelo modelo de VideoSmart Content Block" }

## Limites de frequência {#rate-limits}

A API da VideoSmart tem um limite de frequência de 10.000 solicitações por minuto. Se você exceder esse limite, poderá receber erros ou enfrentar atrasos na geração de vídeos.

Para reduzir esse risco, configure o limite de frequência da Campaign da Braze para que a taxa de envio de mensagens fique abaixo da capacidade da API da VideoSmart.

Para orientações da Braze sobre velocidade de entrega e limite de frequência, consulte [Velocidade de entrega e limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#delivery-speed-rate-limiting).

## Considerações {#considerations}

- O Connected Content é executado quando a mensagem é renderizada, então os valores podem diferir entre a prévia e o envio se seus valores padrão ou atributos forem diferentes.
- Confirme que seu e-mail inclui o Content Block antes de referenciar variáveis como `video_url`.
- Se você usar campos personalizados em `vs_record_data`, confirme os nomes de campo esperados com a VideoSmart.

## Solução de problemas {#troubleshooting}

### A prévia não está funcionando {#preview-not-working}

Se a prévia da Braze falhar (por exemplo, tentativas repetidas ou erros de autenticação), verifique se:

- A credencial de Connected Content "basic_credentials" existe e está configurada corretamente.
- O modelo de **VideoSmart Content Block** está presente na sua conta da Braze.
- Quaisquer variáveis obrigatórias (por exemplo, `vs_campaign_id` ou campos obrigatórios em `vs_record_data`) têm valores padrão definidos para a prévia.

### As variáveis do modelo de VideoSmart Content Block não estão gerando a saída esperada {#videosmarts-content-block-template-variables-not-generating-expected-output}

Se as variáveis geradas pelo modelo de VideoSmart Content Block não estão gerando a saída esperada, verifique o seguinte:

- O modelo de **VideoSmart Content Block** está configurado corretamente na Braze.
- A autenticação de Connected Content está configurada corretamente com as credenciais apropriadas.
- Imprima as variáveis no seu e-mail para confirmar que estão sendo definidas. Por exemplo: `{% raw %}{{ video_url }}{% endraw %}`

Se você estiver usando uma campanha personalizada, verifique também:

- `vs_campaign_id` está definido com um identificador de campanha válido.
- `vs_record_data` é um JSON válido e contém os campos esperados.