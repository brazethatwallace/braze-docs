---
nav_title: Mozart Data
article_title: Mozart Data
description: "Este artigo de referência descreve a parceria entre a Braze e a Mozart Data, uma plataforma de dados moderna e completa, permitindo que você use o Fivetran para importar dados para o Snowflake, criar transformações, combinar dados e muito mais."
alias: /partners/mozart_data/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> A [Mozart Data](https://mozartdata.com/) é uma plataforma de dados moderna e completa, com tecnologia Fivetran, Portable e Snowflake.

A integração entre a Braze e a Mozart Data permite:
{% multi_lang_include partners/workflow_automation/mozart_data_integration_bullets.md %}

## Pré-requisitos {#prerequisites}

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Mozart Data | É necessário ter uma conta Mozart Data para aproveitar essa parceria. [Inscreva-se para uma conta Mozart Data](https://app.mozartdata.com/signup)|
| Conta Snowflake<br>Opção 1: Nova conta | Selecione **Create a New Snowflake Account** durante o processo de criação da conta Mozart Data para que a Mozart Data provisione uma nova conta Snowflake para você. |
| Conta Snowflake<br>Opção 2: Conta existente | Se a sua organização já possui uma conta Snowflake, você pode usar a opção Mozart Data Connected.<br><br>Selecione a opção **Already Have a Snowflake Account** para conectar uma conta Snowflake existente. Para seguir essa opção, um usuário com permissões de nível de conta deve [seguir estas etapas](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

A integração é compatível tanto para sincronizar dados da [Braze para o Mozart Data](#syncing-data-from-braze-to-mozart-data) quanto do [Mozart Data para a Braze](#syncing-data-from-mozart-data-to-braze).

### Sincronizando dados da Braze para o Mozart Data {#syncing-data-from-braze-to-mozart-data}

#### Etapa 1: Configurar o conector da Braze {#step-1-set-up-braze-connector}

1. No Mozart Data, acesse **Connectors** e selecione **Add Connector**.
2. Pesquise por "Braze" e selecione o cartão do conector.
3. Insira um nome de esquema de destino onde todos os dados sincronizados da Braze serão armazenados. Recomendamos usar o nome de esquema padrão `braze`.
4. Selecione **Add Connector**.

#### Etapa 2: Preencher o formulário do conector Fivetran {#step-2-fill-out-the-fivetran-connector-form}

A página do conector Fivetran é aberta após a conclusão da etapa 1. Preencha os campos fornecidos e selecione **Continue** > **Save & Test** para concluir o conector Fivetran.

O Fivetran começa a sincronizar dados da sua conta Braze para o seu data warehouse Snowflake. Você pode acessar os dados de consulta no Mozart Data após o conector concluir a sincronização.

### Sincronizando dados do Mozart Data para a Braze {#syncing-data-from-mozart-data-to-braze}

#### Etapa 1: Configurar um data warehouse Snowflake {#step-1-set-up-a-snowflake-data-warehouse}

Siga as instruções de [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) para configurar uma tabela, um usuário e uma permissão na interface do Snowflake. Essa etapa requer acesso de nível administrador ao Snowflake.

#### Etapa 2: Configurar sua integração com o Snowflake na Braze {#step-2-set-up-your-snowflake-integration-in-braze}

Após configurar seu data warehouse Snowflake, no Mozart Data, acesse a página **Integration** e selecione **Braze**. A visualização da integração **Braze** lista as credenciais para copiar na Braze.

![Página de integração do Mozart Data com a Braze selecionada e credenciais de conexão do Snowflake para uso na Braze.]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Em seguida, estando conectado na Braze, acesse **Integrations > Technology Partners > Snowflake** para iniciar o processo de integração. Copie as credenciais do Mozart Data e adicione-as à página de importação de dados do Snowflake. Selecione **Set up sync details** e insira as informações da sua conta Snowflake e da tabela de origem.

![Formulário de integração do parceiro Snowflake na Braze com os campos de conta, warehouse, banco de dados e esquema preenchidos com as credenciais do Mozart Data.]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Em seguida, escolha um nome para a sincronização, forneça e-mails de contato e selecione um tipo de dados e uma frequência de sincronização na tela de configuração de importação do Snowflake na Braze.

#### Etapa 3: Adicionar uma chave pública ao usuário da Braze {#step-3-add-a-public-key-to-the-braze-user}
Neste ponto, volte ao Snowflake para concluir a configuração. Adicione a chave pública exibida no dashboard da Braze ao usuário que você criou para a Braze se conectar ao Snowflake.

Para mais informações sobre como fazer isso, consulte a [documentação do Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Se você quiser rotacionar as chaves em algum momento, o Mozart Data pode gerar um novo par de chaves e fornecer a nova chave pública.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Etapa 4: Testar a conexão {#step-4-test-connection}

Depois que o usuário for atualizado com a chave pública, retorne ao dashboard da Braze e selecione **Test connection**. Se for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, a conexão não for bem-sucedida, uma mensagem de erro será exibida para ajudar a solucionar o problema.

![Resultado do teste de conexão da integração Snowflake na Braze mostrando uma prévia bem-sucedida após a aplicação da chave pública.]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Você precisa testar a integração com sucesso antes que ela possa passar do estado de rascunho para ativo. Se precisar sair da página de criação, sua integração será salva, e você poderá revisitar a página de detalhes para fazer alterações e testar.
{% endalert %}

## Usando esta integração {#using-this-integration}

### Como acessar os dados da Braze como usuário do Mozart Data {#how-to-access-braze-data-as-a-mozart-data-user}
Após criar uma conta no Mozart Data com sucesso, você pode acessar os dados da Braze sincronizados com o seu data warehouse Snowflake a partir do Mozart Data.

#### Transformações {#transforms}
O Mozart Data oferece uma camada de transformação SQL que permite aos usuários criar uma visualização ou tabela. Você pode criar uma tabela de dimensão no nível do usuário (por exemplo, `dim_users`) para resumir os dados de uso do produto, o histórico de transações e as atividades de engajamento de cada usuário com as mensagens da Braze.

#### Análise {#analysis}
Usando os modelos de transformação ou os dados brutos sincronizados da Braze, você pode analisar o engajamento dos usuários com as mensagens da Braze. Além disso, é possível combinar os dados da Braze com outros dados de aplicativos e analisar como os insights obtidos a partir da interação dos usuários com as mensagens da Braze se relacionam com outros dados que você possa ter sobre eles. Por exemplo, informações demográficas, histórico de compras, uso do produto e engajamento com o atendimento ao cliente.

Isso pode ajudar você a tomar decisões mais informadas sobre estratégias de engajamento para melhorar a retenção de usuários. Tudo isso pode ser feito dentro da interface do Mozart Data usando a ferramenta de consulta, onde você pode exportar os resultados para uma planilha do Google ou um CSV para preparar uma apresentação.

#### Business intelligence (BI)
Pronto para visualizar e compartilhar seus insights com outros membros da equipe? O Mozart Data se integra com praticamente todas as ferramentas de BI. Se você ainda não tem uma ferramenta de BI, entre em contato com o Mozart Data para configurar uma conta gratuita do Metabase.