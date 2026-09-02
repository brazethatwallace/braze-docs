---
nav_title: LiftIgniter
article_title: LiftIgniter
alias: /partners/liftigniter/
description: "Este artigo de referência descreve a parceria entre a Braze e a LiftIgniter, uma plataforma de personalização líder que ajuda as empresas a transformar suas experiências de cliente."
page_type: partner
search_tag: Partner

---

# Liftigniter

> A [LiftIgniter](https://www.liftigniter.com/) é uma plataforma de personalização líder que ajuda as empresas a transformar as experiências dos clientes por meio da personalização em tempo real em todos os pontos de contato.

_Essa integração é mantida pela Liftigniter._

## Sobre a integração {#about-the-integration}

A integração da LiftIgniter com a Braze usa Conteúdo conectado para permitir que você recomende tópicos interessantes, como artigos de notícias, roupas e outros itens de varejo e vídeos.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta LiftIgniter | É necessário ter uma [conta da LiftIgniter](https://console.liftigniter.com/login) para usar essa parceria. |
| Integração da API da LiftIgniter | Você deve [integrar](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview) a LiftIgniter ao seu site ou app para extrair recomendações. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Use a [REST API da LiftIgniter](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389) para inserir conteúdo personalizado nas suas mensagens. Depois de ter sua conta da LiftIgniter e de integrar a LiftIgniter ao seu app, adicione o seguinte modelo ao seu criador de mensagens para chamar o conteúdo das mensagens, substituindo as informações conforme necessário (`x-api-key`, `theapikey`, etc.).

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

Em seguida, escreva sua mensagem, definindo o conteúdo que gostaria de chamar com JSON. Por exemplo, `{{json.items[0].title}}`.

{% endraw %}

![Uma imagem mostrando uma campanha push que inclui chamadas de Conteúdo conectado específicas da LiftIgniter. Há também a lógica de Conteúdo conectado adicionada ao campo de imagem.]({% image_buster /assets/img/liftigniter.png %})

Depois de colocar essa mensagem no corpo do criador, você poderá pré-visualizar a mensagem. Você pode até mesmo extrair imagens, conforme mostrado no exemplo a seguir:

![Uma pré-visualização de como a mensagem ficará depois de ser enviada.]({% image_buster /assets/img/liftigniter2.png %})