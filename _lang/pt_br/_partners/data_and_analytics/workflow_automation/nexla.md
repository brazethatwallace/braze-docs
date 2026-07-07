---
nav_title: Nexla
article_title: Nexla
description: "Este artigo de referência descreve a parceria entre a Braze e a Nexla, uma plataforma unificada de operações de dados que permite que os usuários do Braze Currents extraiam, transformem e carreguem dados do data lake para outros locais em um formato personalizado."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> A [Nexla](https://www.nexla.com) é líder em operações de dados unificadas e foi reconhecida como Gartner Cool Vendor em 2021. A plataforma Nexla fornece ferramentas para criar fluxos de dados escaláveis, proporcionando operações de dados governadas, colaboração e agilidade para equipes de negócios e de dados. As equipes que trabalham com dados obtêm uma experiência unificada com pouco ou nenhum código para integrar, transformar, provisionar e monitorar dados para qualquer caso de uso.

A integração entre a Braze e a Nexla permite que os clientes que usam o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/) aproveitem a Nexla para extrair, transformar e carregar dados do data lake em outros locais em um formato personalizado, tornando os dados facilmente acessíveis em todo o seu ecossistema.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Nexla | É necessário ter uma [conta Nexla](https://www.nexla.com/get-demo) para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze  | Sua URL de endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

O data-as-a-product da Nexla, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), permite trabalhar com dados de qualquer formato sem gerenciar metadados. Quando você configura fluxos de dados de ou para a Braze com a Nexla, ferramentas sem código ficam disponíveis em minutos. Depois que o fluxo de dados é definido para um destino, a Nexla monitora o fluxo e o dimensiona para qualquer quantidade de dados.

## Integração {#integration}

### Etapa 1: Criar uma conta Nexla {#step-1-create-a-nexla-account}

Se você ainda não tem uma conta Nexla, acesse o [site](https://www.nexla.com) da Nexla para solicitar uma demonstração e um teste gratuitos. Em seguida, acesse [www.dataops.nexla.io](https://www.dataops.nexla.io) e faça login com suas novas credenciais.

### Etapa 2: Adicione sua fonte {#step-2-add-your-source}

#### Se a Braze for sua fonte de dados {#if-braze-is-your-data-source}
1. Na plataforma Nexla, navegue até **Flows > Create a New Flow** na barra de ferramentas à esquerda.
2. Clique em **Create New Source**, selecione o conector da Braze e clique em **Next**.
3. Selecione **Add a New Credential**, nomeie a credencial, adicione sua chave de API da Braze e o endpoint REST e clique em **Save**.
4. Por fim, selecione seus dados e clique em **Save**.

A Nexla pesquisará os dados disponíveis na fonte e gerará um [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) para transformação ou envio a um destino.

#### Se a Braze for seu destino {#if-braze-is-your-destination}

Visite a documentação da Nexla sobre como [conectar fontes à Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Etapa 3: Transformar (opcional) {#step-3-transform-optional}

Se quiser realizar [transformações](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) personalizadas em seus dados ou usar os conectores pré-construídos da Nexla, clique no botão **Transform** no conjunto de dados para acessar o Transform Builder. Orientações sobre como usar o Transform Builder podem ser encontradas na [documentação da Nexla](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data).

### Etapa 4: Enviar para o destino {#step-4-send-to-destination}

Para enviar dados para um destino, clique na seta **Send to Destination** no conjunto de dados e selecione qualquer um dos conectores de destino da Nexla ou da Braze, caso você tenha uma origem diferente. Insira suas credenciais, configure as opções de destino e clique em **Save**. Os dados começarão a fluir instantaneamente no formato que você especificou para o destino de sua escolha.

## Usando esta integração {#using-this-integration}

Depois que o fluxo é configurado, nada mais é necessário. A Nexla tratará de todas as alterações nos dados de origem, dimensionará para qualquer volume de novos dados e notificará você sobre quaisquer alterações de esquema ou erros para triagem. Se quiser fazer alterações nas transformações, na origem ou no destino, basta clicar nessas opções e fazer a alteração — a Nexla atualizará o fluxo instantaneamente.