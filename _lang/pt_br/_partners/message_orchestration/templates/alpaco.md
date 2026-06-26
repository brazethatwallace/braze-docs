---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/alpaco/
description: "A integração entre a Braze e a Alpaco permite exportar modelos de e-mail e blocos de conteúdo compatíveis com Liquid e alinhados à marca para a Braze, prontos para uso em e-mail e mensagens no app."
page_type: partner
search_tag: Partner
---

# Alpaco

> A [Alpaco](https://alpaco.email/) é uma ferramenta de gestão criativa on-line que oferece um editor de arrastar e soltar para criar conteúdo reutilizável e seguro para a marca na Braze. A integração da Alpaco com a Braze permite exportar Content Blocks, Modelos de e-mail e Modelos de mensagens no app.

_Essa integração é mantida pela Alpaco._

{% alert note %}
A Alpaco oferece suporte pleno a [variáveis Liquid](https://shopify.github.io/liquid/) e, portanto, tem compatibilidade plena com todas as variáveis Liquid usadas nas suas configurações da Braze.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ------------| ----------- |
| Conta Alpaco | É necessário ter uma conta na Alpaco para usar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões completas de **Modelos**. <br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Instância do cluster | Sua [instância de cluster]({{site.baseurl}}/api/basics/#endpoints) da Braze se alinha com o dashboard e o endpoint REST da Braze. <br><br> Por exemplo, se a URL do seu dashboard for `https://dashboard-03.braze.com`, seu endpoint será `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

- Exporte **modelos de e-mail** totalmente projetados para uso em Campaigns da Braze e envio de mensagens transacionais.
- Crie e gerencie **blocos de conteúdo modulares** (por exemplo, cabeçalhos, rodapés, promoções) que podem ser reutilizados em vários canais.
- Crie **mensagens no app** envolventes com a mesma flexibilidade criativa dos e-mails, facilitando a entrega de experiências consistentes e alinhadas à marca em todos os canais.
- Ative a **personalização** incluindo Liquid tags compatíveis com a Braze, como `{{first_name}}` ou `{{custom_attribute}}`.
- Mantenha a **consistência da marca** centralizando o design criativo na Alpaco e enviando as atualizações para a Braze com uma única exportação.

## Integração {#integration}

Forneça sua chave da API REST e a instância do cluster da Braze para a equipe de sucesso do cliente da Alpaco. Em seguida, a equipe configurará a integração inicial para você.

{% alert note %}
Essa é uma configuração única e todas as exportações futuras usarão automaticamente essa chave de API.
{% endalert %}

## Exportação de mensagens da Alpaco para a Braze {#exporting-alpaco-messages-to-braze}

### Etapa 1: Criar um modelo na Alpaco {#step-1-create-a-template-in-alpaco}

Na Alpaco, crie um modelo que expresse a identidade da sua marca. Quando estiver pronto, selecione **Save**.

![Criar modelo na Alpaco]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Etapa 2: Redigir uma mensagem usando o modelo {#step-2-draft-a-message-using-the-template}

Em seguida, acesse o lobby da Alpaco e use seu modelo para criar um e-mail, uma mensagem no app ou um bloco de conteúdo. Para verificar sua mensagem antes de exportar, selecione **Review**.

![Criar e-mail na Alpaco]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Etapa 3: Exportar sua mensagem para a Braze {#step-3-export-your-message-to-braze}

Selecione **Export** e, em seguida, escolha a integração da Braze e especifique se está exportando um modelo de e-mail ou um bloco de conteúdo.

Se você fizer alterações após a exportação, poderá reexportar o conteúdo da Alpaco para atualizá-lo na Braze.

![Exportar e-mail na Alpaco]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Uso de modelos e blocos da Alpaco na Braze {#using-alpaco-templates-and-blocks-in-braze}

Dependendo do tipo de conteúdo exportado, o modelo aparecerá em uma das seguintes seções:

- **Modelos e mídia > Modelos de e-mail**
- **Modelos e mídia > Content Blocks**

Os modelos da Alpaco são ideais para organizações que desejam gerenciar de forma centralizada a consistência da marca. Eles também são compatíveis com as tags integradas da Braze para facilitar a categorização e o gerenciamento de conteúdo.