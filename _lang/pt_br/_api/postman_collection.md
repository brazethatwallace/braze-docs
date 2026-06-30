---
nav_title: Postman e solicitações de amostra
article_title: Postman e solicitações de amostra
page_order: 3
description: "Este artigo de referência aborda a Coleção Postman da Braze, o que ela é, como configurar e usar a coleção, além de como editar e enviar solicitações."
page_type: reference

---

# Postman e solicitações de amostra {#postman-and-sample-requests}

> A Braze permite que você gere solicitações de API de amostra para todos os nossos endpoints por meio da nossa Coleção Postman. Este artigo de referência aborda a Coleção Postman da Braze, o que ela é, como configurar e usar a coleção, além de como editar e enviar solicitações.

## O que é o Postman? {#what-is-postman}

O Postman é uma ferramenta de edição visual gratuita para criar e testar solicitações de API. Em comparação com outros métodos (por exemplo, usando cURL), o Postman permite que você edite solicitações de API, visualize informações de cabeçalho e muito mais. Você pode salvar coleções (bibliotecas de exemplos de solicitações de API pré-fabricadas). Para acelerar a configuração com nossa REST API, fornecemos uma coleção com exemplos pré-fabricados para todos os endpoints.

Visualize ou baixe nossa Coleção do Postman clicando em **Run in Postman** nos nossos [documentos do Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) para começar.

## Como usar a coleção Postman da Braze {#using-the-braze-postman-collection}

Se você tiver uma conta no Postman (você pode baixar as versões para macOS, Windows e Linux no [site do Postman](https://www.getpostman.com)), pode abrir nossa documentação do Postman no seu próprio app do Postman clicando no botão laranja **Run in Postman**. Você pode então [criar um ambiente](#setting-up-your-postman-environment), ou usar nosso ambiente da REST API da Braze como modelo, e editar as solicitações `POST` e `GET` disponíveis para atender às suas próprias necessidades.

### Configurando seu ambiente Postman {#setting-up-your-postman-environment}

{% raw %}
A Coleção Postman da Braze usa uma variável de modelo, `{{instance_url}}`, para substituir a URL da REST API da sua instância da Braze nas solicitações pré-construídas, e a variável `{{api_key}}` para sua chave de API. Em vez de ter que editar manualmente todas as solicitações na coleção, você pode configurar essa variável no seu ambiente do Postman. Você pode selecionar nosso ambiente modelado (Braze REST API Environment Template) no menu suspenso e substituir os valores das variáveis pelos seus próprios, ou pode configurar seu próprio ambiente.
{% endraw %}

Para configurar seu próprio ambiente, execute as seguintes etapas:

1. Na guia **Workspaces**, selecione **Environments**.
2. Clique no botão **+** para criar um novo ambiente.
3. Dê um nome a esse ambiente (por exemplo, "Braze API Requests") e adicione chaves para `instance_url` e `api_key` com valores correspondentes à sua [instância da Braze]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) e à [chave da REST API da Braze]({{site.baseurl}}/api/api_key).
4. Clique em **Save**.

{% alert note %}
Nos corpos de solicitação `POST`, o `api_key` deve ser encapsulado em aspas: `"MY-API-KEY-EXAMPLE"`. Em URLs `GET`, não deve ser. Já fornecemos essa formatação para você nos corpos de solicitação `POST` desta documentação, URLs `GET` e modelo de ambiente para `YOUR-API-KEY-HERE`.
{% endalert %}

![Adicionando variáveis para chave de API e URL da instância ao ambiente da REST API da Braze no Postman.]({% image_buster /assets/img_archive/postman_variable.png %})

### Usando as solicitações pré-construídas da coleção {#using-the-pre-built-requests-from-the-collection}

Depois de configurar seu ambiente, você pode usar qualquer uma das solicitações pré-construídas na coleção como modelo para criar novas solicitações de API. Para começar a usar uma das solicitações pré-construídas, clique nela no menu **Collections** do Postman. Isso abrirá a solicitação como uma nova guia na janela principal do app Postman.

Em geral, existem dois tipos de solicitações que os endpoints da API da Braze aceitam: `GET` e `POST`. Dependendo de qual método `HTTP` o endpoint usa, você precisará editar a solicitação pré-construída de forma diferente.

#### Editar uma solicitação POST {#edit-a-post-request}

Ao editar uma solicitação `POST`, abra a solicitação e navegue até a seção **Body** no editor de solicitações. Para melhor legibilidade, selecione o botão de opção **raw** para formatar o corpo da solicitação `JSON`.

![Guia Body ao editar uma solicitação POST User Track no Postman]({% image_buster /assets/img_archive/postman_post.png %})

#### Editar uma solicitação GET {#edit-a-get-request}

Ao editar uma solicitação `GET`, edite os parâmetros passados na URL da solicitação. Para fazer isso, selecione a guia **Params** e edite os pares chave-valor nos campos que aparecem.

![Guia Params ao editar uma solicitação GET de consulta de lista de endereços de e-mail cancelados no Postman.]({% image_buster /assets/img_archive/postman_get.png %})

### Envie sua solicitação {#send-your-request}

Depois que sua solicitação de API estiver pronta, clique em **Send**. A solicitação é enviada e os dados da resposta são preenchidos em uma seção abaixo do editor de solicitações. A partir daqui, você pode visualizar os dados brutos retornados da API da Braze, ver o código de resposta HTTP, ver quanto tempo a solicitação levou para processar e visualizar as informações do cabeçalho.

![Exemplo de dados de resposta do corpo de uma solicitação POST com status 201 Created e tempo de resposta de 269 milissegundos.]({% image_buster /assets/img_archive/postman_response.png %})