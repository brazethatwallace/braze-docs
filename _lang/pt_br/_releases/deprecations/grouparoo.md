---
nav_title: Grouparoo
page_order: 1
page_type: update
noindex: true
description: "Este artigo descreve a parceria entre a Braze e o Grouparoo, uma ferramenta de ETL reversa de código aberto usada para alimentar as ferramentas de marketing, vendas e suporte com dados do seu data warehouse."

---

# Grouparoo

{% alert update %}
O suporte ao Grouparoo foi descontinuado a partir de abril de 2022.
{% endalert %}

> O [Grouparoo](https://www.grouparoo.com/) é uma ferramenta de ETL reversa de código aberto que sincroniza os dados do seu warehouse com as ferramentas de marketing, vendas e suporte. Sua interface de usuário centrada em modelos permite que membros não técnicos da equipe configurem e programem sincronizações de dados.

A integração entre a Braze e o Grouparoo sincroniza os dados do warehouse com a Braze. As programações de sincronização automática mantêm as comunicações com os clientes atualizadas com informações recentes.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta e projeto do Grouparoo | É necessário ter uma conta e um projeto do Grouparoo para aproveitar essa parceria.<br><br>Essa integração pode ser usada com a edição comunitária gratuita e com as soluções empresariais fornecidas pelo Grouparoo. A configuração ocorrerá na interface de usuário de configuração do Grouparoo. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões de usuários e rastreamento. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | [A URL do seu endpoint REST or transferir estado representacional](https://www.grouparoo.com/). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Criar um app da Braze no Grouparoo {#step-1-create-a-braze-app-in-grouparoo}

No Grouparoo, navegue até **Apps** e selecione **Braze** para criar um novo app da Braze. Na janela modal exibida, informe sua chave de API or interface de programação do aplicativo (API) da Braze e o endpoint REST or transferir estado representacional.

![O modal Criar app da Braze no Grouparoo, com campos para a chave de API da Braze e o endpoint REST.]({% image_buster /assets/img/grouparoo/add-app.png %})

### Etapa 2: Configurar um modelo e uma fonte de dados {#step-2-set-up-a-model-and-data-source}

Essa integração requer que você tenha um modelo existente e uma fonte de dados configurada antes de prosseguir para a próxima etapa. Se você não tiver essa configuração, visite a documentação do Grouparoo para saber como configurar um [modelo](https://www.grouparoo.com/docs/config/models) e uma [fonte de dados](https://www.grouparoo.com/docs/config/sources).

### Etapa 3: Criar um destino da Braze no Grouparoo {#step-3-create-a-braze-destination-in-grouparoo}

#### Selecionar o modo de sincronização {#select-sync-mode}

No Grouparoo, selecione seu modelo na barra de navegação. Em seguida, vá até a seção **Destinations** e clique em **Add new Destination**.

Em seguida, selecione o app **Braze** que você criou, nomeie o destino e selecione o modo de sincronização desejado entre os seguintes:
- **Sync**: Adicione, atualize e remova usuários da empresa conforme necessário. Essa opção procura novos registros, alterações em registros existentes e exclusões.
- **Additive**: Adicione e atualize os usuários da empresa conforme necessário, mas não remova ninguém. Essa opção procura novos usuários para adicionar à Braze e alterações nos usuários existentes da empresa, mas não controla as exclusões.
- **Enrich**: Atualize apenas os usuários que já existem na Braze. Não adicione ou remova usuários. Essa opção atualizará apenas os usuários existentes na Braze.

#### Mapeamento do campo de propriedade {#property-field-mapping}

Em seguida, você deve mapear os campos de propriedade do Grouparoo para os campos de propriedade da Braze.

![Exemplo de campos de mapeamento de propriedades. O userID do Grouparoo é definido para mapear para external_id. email, firstName e lastName são definidos como campos equivalentes "email", "first_name" e "last_name" do Grouparoo.]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Certifique-se de que o campo `external_id` da Braze esteja mapeado para a chave primária na sua tabela de origem. Mapeie o restante dos campos conforme necessário para seu caso de uso.

Seção **Send Record Properties**: Uma lista de campos de perfil de usuário predefinidos disponíveis para mapear dados. Qualquer um deles pode ser sincronizado a partir das propriedades do Grouparoo.

Seção **Optional Braze User Profile Fields**: Crie campos de perfil de usuário da Braze personalizados opcionais. Se você clicar em **Add New Braze User Profile Field**, verá todas as propriedades disponíveis que podem ser mapeadas para a Braze. O nome de qualquer novo campo que você criar será o mesmo da propriedade do Grouparoo, mas poderá ser renomeado.

#### Grupos do Grouparoo {#grouparoo-groups}

Além do mapeamento, você também pode optar por adicionar grupos do Grouparoo a grupos de inscrições da Braze.

![Em "Braze Subscription Groups" na janela de configuração de destino do Grouparoo, o grupo do Grouparoo "High value with recent automotive purchase" será adicionado ao grupo de inscrições da Braze "High value with recent automotive purchase".]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
Mais detalhes e atualizações sobre essa integração podem ser encontrados na [documentação do Grouparoo](https://www.grouparoo.com/docs/integrations/grouparoo-braze).
{% endalert %}