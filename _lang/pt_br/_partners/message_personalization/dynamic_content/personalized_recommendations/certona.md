---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "Este artigo de referência descreve a parceria entre a Braze e a Certona, uma solução de personalização omnicanal em tempo real que oferece personalização em todo o ciclo de vida do cliente. Use a Certona com o parceiro Conteúdo conectado da Braze para inserir facilmente recomendações de conteúdo em campanhas multicanal."
page_type: partner
search_tag: Partner

---

# Certona

> A plataforma [Certona](https://www.certona.com/) impulsiona a personalização ao longo do ciclo de vida do cliente. De campanhas de e-mail altamente individualizadas a recomendações de produtos baseadas em machine learning, a Certona garante que você esteja aproveitando o poder da personalização.

_Esta integração é mantida pela Certona._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Certona utiliza as recomendações de produtos de machine learning da Certona em Campaigns e Canvas da Braze por meio do Conteúdo conectado.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| [Conta Certona](https://manage.certona.com/) | É necessário ter uma conta Certona para aproveitar essa parceria. |
| [Endpoint da REST API da Certona](https://manage.certona.com/) | Esse endpoint é usado diretamente na mensagem da campanha da Braze para extrair conteúdo recomendado com base no ID do usuário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

Use a REST API da Certona para inserir conteúdo personalizado em suas mensagens. Isso pode ser feito adicionando o seguinte modelo de Conteúdo conectado ao seu criador de mensagens da Braze, juntamente com seu endpoint da REST API da Certona.

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

Em seguida, defina o conteúdo que você gostaria de chamar, como texto ou imagens relevantes. Por exemplo, `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}`.

{% endraw %}

![Uma imagem de uma campanha push com Conteúdo conectado relacionado à Certona incluído no corpo da mensagem.]({% image_buster /assets/img/certona.png %})

Depois de colocar essa mensagem no corpo do criador, faça uma pré-visualização da chamada do Conteúdo conectado para ter certeza de que as informações corretas são exibidas.

![Uma imagem mostrando a guia "Test", incentivando os usuários a testar completamente a mensagem antes de enviá-la.]({% image_buster /assets/img/certona2.png %})