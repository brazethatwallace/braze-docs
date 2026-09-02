---
nav_title: Postman e solicitações de amostra
article_title: Postman e solicitações de amostra
page_order: 3
description: "Este artigo de referência aborda a Coleção Postman da Braze, o que ela é, como configurar e usar a coleção, além de como editar e enviar solicitações."
page_type: reference
---

# Postman e solicitações de amostra {#postman-and-sample-requests}

> A Braze permite que você gere solicitações de API or interface de programação do aplicativo (API) de amostra para todos os nossos endpoints por meio da nossa Coleção Postman. Este artigo de referência aborda a Coleção Postman da Braze, o que ela é, como configurar e usar a coleção, além de como editar e enviar solicitações.

## O que é o Postman? {#what-is-postman}

O Postman é uma ferramenta gratuita de edição visual para criar e testar requisições de API or interface de programação do aplicativo (API). Comparado a outros métodos (por exemplo, usar cURL), o Postman permite editar requisições de API or interface de programação do aplicativo (API), visualizar informações de cabeçalho e muito mais. Você pode salvar coleções (bibliotecas de exemplos pré-configurados de requisições de API or interface de programação do aplicativo (API)). Para acelerar a configuração com nossa REST or transferir estado representacional API or interface de programação do aplicativo (API), oferecemos uma coleção com exemplos pré-configurados para todos os endpoints.

Visualize ou baixe nossa coleção do Postman clicando em **Run in Postman** em nossa [documentação do Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) para começar.

## Usando a coleção Postman da Braze {#using-the-braze-postman-collection}

Se você tem uma conta Postman (é possível baixar as versões para macOS, Windows e Linux no [site do Postman](https://www.getpostman.com)), pode abrir nossa documentação do Postman no seu próprio app Postman clicando no botão laranja **Run in Postman**. Em seguida, você pode [criar um ambiente](#setting-up-your-postman-environment) ou usar nosso ambiente da REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze como modelo e editar as requisições `POST` e `GET` disponíveis de acordo com suas necessidades.

### Configurando seu ambiente Postman {#setting-up-your-postman-environment}

{% raw %}
A coleção Postman da Braze usa uma variável de modelo, `{{instance_url}}`, para substituir a URL da REST or transferir estado representacional API or interface de programação do aplicativo (API) da sua instância da Braze nas requisições pré-configuradas, e a variável `{{api_key}}` para sua chave de API or interface de programação do aplicativo (API). Em vez de editar manualmente todas as requisições na coleção, você pode configurar essa variável no seu ambiente Postman. Você pode selecionar nosso ambiente de modelo (Braze REST or transferir estado representacional API or interface de programação do aplicativo (API) Environment Template) no menu suspenso e substituir os valores das variáveis pelos seus, ou pode configurar seu próprio ambiente.
{% endraw %}

Para configurar seu próprio ambiente, siga as etapas a seguir:

1. Na guia **Workspaces**, selecione **Environments**.
2. Clique no botão **+** (mais) para criar um novo ambiente.
3. Dê um nome a esse ambiente (por exemplo, "Braze API or interface de programação do aplicativo (API) Requests") e adicione chaves para `instance_url` e `api_key` com valores correspondentes à sua [instância da Braze]({{site.baseurl}}/api/basics) e [chave da REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze]({{site.baseurl}}/api/basics).
4. Clique em **Save**.

{% alert note %}
Nos corpos de requisições `POST`, a `api_key` deve estar entre aspas: `"MY-API-KEY-EXAMPLE"`. Em URLs de `GET`, não deve. Já fornecemos essa formatação para você nos corpos de requisições `POST`, URLs de `GET` e no modelo de ambiente para `YOUR-API-KEY-HERE` desta documentação.
{% endalert %}

![Adicionando variáveis para chave de API or interface de programação do aplicativo (API) e URL da instância ao ambiente da REST or transferir estado representacional API or interface de programação do aplicativo (API) da Braze no Postman.]({% image_buster /assets/img_archive/postman_variable.png %})

### Usando as requisições pré-configuradas da coleção {#using-the-pre-built-requests-from-the-collection}

Depois de configurar seu ambiente, você pode usar qualquer uma das requisições pré-configuradas na coleção como modelo para criar novas requisições de API or interface de programação do aplicativo (API). Para começar a usar uma das requisições pré-configuradas, clique nela no menu **Collections** do Postman. A requisição será aberta em uma nova guia na janela principal do app Postman.

De modo geral, existem dois tipos de requisições que os endpoints da API or interface de programação do aplicativo (API) da Braze aceitam: `GET` e `POST`. Dependendo de qual método `HTTP` o endpoint utiliza, você precisará editar a requisição pré-configurada de forma diferente.

#### Editar uma requisição POST {#edit-a-post-request}

Ao editar uma requisição `POST`, abra a requisição e navegue até a seção **Body** no editor de requisições. Para melhor legibilidade, selecione o botão de opção **raw** para formatar o corpo da requisição `JSON`.

![Guia Body ao editar uma requisição POST User Track no Postman]({% image_buster /assets/img_archive/postman_post.png %})

#### Editar uma requisição GET {#edit-a-get-request}

Ao editar uma requisição `GET`, edite os parâmetros passados na URL da requisição. Para isso, selecione a guia **Params** e edite os pares de chave-valor nos campos exibidos.

![Guia Params ao editar uma requisição GET de consulta de lista de endereços de e-mail com inscrição cancelada no Postman.]({% image_buster /assets/img_archive/postman_get.png %})

### Enviar sua requisição {#send-your-request}

Quando sua requisição de API or interface de programação do aplicativo (API) estiver pronta, clique em **Send**. A requisição é enviada e os dados de resposta são preenchidos em uma seção abaixo do editor de requisições. A partir daqui, você pode visualizar os dados brutos retornados pela API or interface de programação do aplicativo (API) da Braze, ver o código de resposta HTTP, verificar quanto tempo a requisição levou para ser processada e visualizar informações de cabeçalho.

![Exemplo de dados de resposta do corpo de uma requisição POST com status 201 Created e tempo de resposta de 269 milissegundos.]({% image_buster /assets/img_archive/postman_response.png %})