---
nav_title: Blings
article_title: Blings
description: "Este artigo de referência descreve a integração entre a Braze e a Blings."
alias: /partners/blings/
page_type: partner
search_tag: Partner
---

# Blings

> A [Blings](https://www.blings.io/) é uma plataforma de vídeo personalizado de última geração que permite oferecer experiências de vídeo em tempo real, interativas e orientadas por dados em todos os canais e em escala.

_Essa integração é mantida pela Blings._

## Pré-requisitos {#prerequisites}

| Requisito       | Descrição                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| Conta Blings    | É necessário ter uma conta Blings para aproveitar essa parceria.         |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Obtenha seu snippet HTML da Blings {#step-1-obtain-your-blings-html-snippet}

{% tabs %}
{% tab Blings business and free plans %}

#### Planos business e free da Blings {#blings-business-and-free-plans}

Localize e copie seu snippet HTML diretamente no app da Blings.

1. Acesse a guia **Connect** do projeto MP5 selecionado.
2. Adicione as Liquid tags da Braze às variáveis correspondentes na página **Connect** da Blings. As tags preencherão dinamicamente os valores no snippet HTML.

![Snippet HTML da Blings.]({% image_buster /assets/img/blings/blings_connect_audience.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Blings Enterprise plan %}

#### Plano Enterprise da Blings {#blings-enterprise-plan}

Solicite o snippet HTML ao seu representante da Blings.

{% endtab %}
{% endtabs %}

### Etapa 2: Criar uma campaign na Braze {#step-2-create-a-braze-campaign}

Na Braze, crie uma nova campaign de e-mail ou mensagem no app e insira o snippet HTML da Blings. Use a pré-visualização do editor para confirmar que os campos personalizados e o conteúdo dinâmico da Creative Suite são exibidos corretamente.

### Etapa 3: Teste e lançamento {#step-3-test-and-launch}

Pré-visualize a campaign na Braze para confirmar que os campos personalizados estão sendo preenchidos corretamente. Em seguida, implemente sua campaign MP5 em escala.

![Pré-visualização da Blings na Braze.]({% image_buster /assets/img/blings/blings_braze_preview.png %}){: style="max-width:70%;"}

## Obtendo suporte {#getting-support}

Em caso de dúvidas ou para solicitar seu snippet, entre em contato com a Blings em [support@blings.io](mailto:support@blings.io) ou consulte a [central de ajuda da Blings](https://blings.gitbook.io/blings-knowledge-base/documentation).