---
nav_title: Celebrus
article_title: Integração do Celebrus
description: "Integração entre Braze e Celebrus."
---

# Celebrus

> A Celebrus se integra perfeitamente ao SDK da Braze nos canais de aplicativos móveis e da Web, facilitando o preenchimento da Braze com dados de atividade do canal. Isso inclui insights abrangentes sobre o tráfego de visitantes em ativos digitais durante períodos específicos. <br><br>Além disso, a Celebrus captura dados de perfil ricos para cada cliente individual, que podem ser sincronizados com a Braze. Isso permite criar estratégias eficazes de análise de dados e comunicação da Braze com base em dados primários abrangentes, precisos e detalhados. Esse recurso é ainda mais reforçado pelos sinais orientados por machine learning da Celebrus, que permitem a captura de dados sem complicações e sem a necessidade de tag extensa. Com um robusto gráfico de identidade primário implementado, todos os dados se tornam instantaneamente acessíveis para uso imediato.

_Esta integração é mantida pela Celebrus._

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Celebrus | É necessário ter uma conta Celebrus para aproveitar essa parceria. |
| Data warehouse (opcional) | Ao usar o conector da Celebrus para atributos personalizados da Braze, você deve ter um data warehouse compatível com a integração da Ingestão de dados na nuvem (CDI) da Braze e configurar a CDI no dashboard da Braze. |
| Definições de configuração do SDK da Braze (opcional) | Ao usar o conector da Celebrus para o SDK da Braze, você deve passar o endpoint de SDK e a Chave da API SDK. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Implementação {#implementation}
Depois de instalar sua implementação da Celebrus, use os conectores da Celebrus para a Braze para integrar os dados da Celebrus à Braze. Há dois elementos na integração da Celebrus para a Braze: o SDK da Braze e os atributos personalizados da Braze. Você pode implantar um ou ambos, dependendo de como você usa a Braze e dos casos de uso de que precisa.

Se ainda não tiver o SDK da Braze implementado no seu canal da Web, você poderá usar a Celebrus para implantar o SDK da Braze. A Celebrus adicionará o SDK da Braze às páginas da Web e configurará a identidade da Braze para o visitante da Web usando o gráfico de identidade da Celebrus. Os atributos do cliente podem ser sincronizados com a Braze por meio da Ingestão de dados na nuvem (CDI). Isso requer um data warehouse compatível com a CDI da Braze e a configuração da CDI na Braze.

### Conector Celebrus para SDK da Braze {#celebrus-connector-for-braze-sdk}

O conector da Celebrus para o SDK da Braze fornece dados de alto nível de canais de aplicativos móveis e da Web para a Braze. No SDK da Braze, o `System Identity` da Celebrus do gráfico de identidade da Celebrus será usado como o identificador para a integração da Braze. Outros identificadores são compatíveis para a sincronização de atributos personalizados por meio do conector Celebrus de atributos personalizados da Braze.

O conector implanta e configura o SDK da Braze no seu canal, então você precisará definir algumas configurações no fluxo de dados do SDK da Braze e fornecer os valores para estas três configurações:

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
O conector da Celebrus para o SDK da Braze inserirá e inicializará o SDK da Braze para identificar o usuário e adicionar o identificador ao gráfico de identidade da Celebrus. Esse conector não registrará dados no perfil de usuário nem disparará outros métodos do SDK da Braze. <br><br>Você pode chamar quaisquer métodos desejados diretamente na sua base de código para registrar dados por meio do [SDK da Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) ou aproveitar outros recursos compatíveis com o SDK da Braze.
{% endalert%}

### Conector Celebrus para atributos personalizados da Braze {#celebrus-connector-for-braze-custom-attributes}

#### Etapa 1: configure os detalhes de conexão na Celebrus {#step-1-configure-connected-details-in-celebrus}

O conector da Celebrus para atributos personalizados da Braze envia atributos personalizados para um banco de dados intermediário, pré-formatado da maneira que a Braze espera recebê-lo. Na Celebrus, você configura os detalhes da conexão para o banco de dados, o que dependerá do tipo de banco de dados que estiver usando (como Snowflake ou Redshift).

#### Etapa 2: configure a Ingestão de dados na nuvem no seu dashboard da Braze {#step-2-configure-cloud-data-ingestion-in-your-braze-dashboard}

Essa integração usa a Ingestão de dados na nuvem da Braze. Siga as instruções em [Integrações de data warehouse]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/) para definir e configurar as [configurações da Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) de acordo com o tipo de data warehouse usado.

#### Etapa 3: sincronize os dados da Celebrus para a Braze {#step-3-sync-data-from-celebrus-to-braze}

A Celebrus captura e atribui identificadores exclusivos a um indivíduo, como e-mail, telefone, `external_id` ou alias de usuário, e os envia à Braze via CDI. Isso permite que os dados sejam sincronizados com a Braze para o mesmo indivíduo.

A Celebrus usará os identificadores definidos para enviar os atributos do cliente que estão definidos no construtor de perfil da Celebrus, mas somente quando os valores dos atributos forem alterados. Observe que os nomes dos atributos definidos no construtor de perfil da Celebrus serão usados na Braze por padrão. Portanto, certifique-se de atualizar esses nomes para aderir às [convenções de nomenclatura da Braze]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens).

{% alert important %}
Por enquanto, esta versão não oferece suporte a eventos e compras.<br><br> Esta integração envia atributos como valores de string, então alguns atributos são listas (como sinais). Por enquanto, as listas não podem ser convertidas em arrays. Não há atributos aninhados.
{% endalert%}