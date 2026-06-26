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
- Usar o Fivetran para importar dados da Braze para o Snowflake
- Criar transformações combinando dados da Braze com dados de outros aplicativos e analisar efetivamente o comportamento dos usuários
- Importar dados do Snowflake para a Braze para criar novas oportunidades de engajamento de clientes
- Combinar os dados da Braze com os dados de outros aplicativos para obter uma compreensão mais holística do comportamento dos usuários
- Integrar com uma ferramenta de business intelligence para explorar ainda mais os dados armazenados no Snowflake

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
| Conta Mozart Data | É necessário ter uma conta Mozart Data para aproveitar essa parceria. [Inscreva-se aqui.](https://app.mozartdata.com/signup)|
| Conta Snowflake<br>Opção 1: Nova conta | Selecione **Create a New Snowflake Account** durante o processo de criação da conta da Mozart Data para que a Mozart Data provisione uma nova conta do Snowflake para você. |
| Conta Snowflake<br>Opção 2: Conta existente | Se sua organização já tiver uma conta do Snowflake, você poderá usar a opção Mozart Data Connected.<br><br>Selecione a opção **Already Have a Snowflake Account** para conectar uma conta Snowflake existente. Para usar essa opção, um usuário com permissões no nível da conta deve [seguir estas etapas](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

A integração é compatível tanto para a sincronização de dados da [Braze para a Mozart Data](#syncing-data-from-braze-to-mozart-data) quanto da [Mozart Data para a Braze](#syncing-data-from-mozart-data-to-braze).

### Sincronização de dados da Braze para a Mozart Data {#syncing-data-from-braze-to-mozart-data}

#### Etapa 1: Configurar o conector da Braze {#step-1-set-up-braze-connector}

1. Na Mozart Data, acesse **Connectors** e selecione **Add Connector**.
2. Procure por "Braze" e selecione o cartão do conector.
3. Digite um nome de esquema de destino onde todos os dados sincronizados da Braze serão armazenados. Recomendamos usar o nome do esquema padrão `braze`.
4. Selecione **Add Connector**.

#### Etapa 2: Preencha o formulário do conector Fivetran {#step-2-fill-out-the-fivetran-connector-form}

Você será redirecionado para a página do conector Fivetran após concluir a etapa 1. Preencha os campos indicados e selecione **Continue** > **Save & Test** para concluir o conector Fivetran.

O Fivetran começará a sincronizar os dados da sua conta da Braze com o data warehouse do Snowflake. Você pode acessar os dados de consulta na Mozart Data depois que o conector tiver concluído a sincronização.

### Sincronização de dados da Mozart Data para a Braze {#syncing-data-from-mozart-data-to-braze}

#### Etapa 1: Configurar um data warehouse do Snowflake {#step-1-set-up-a-snowflake-data-warehouse}

Siga as instruções de [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) para configurar uma tabela, um usuário e uma permissão na interface do Snowflake. Note que essa etapa requer acesso de administrador ao Snowflake.

#### Etapa 2: Configure sua integração com o Snowflake na Braze {#step-2-set-up-your-snowflake-integration-in-braze}

Depois de configurar seu data warehouse do Snowflake, na Mozart Data, acesse a página **Integration** e selecione **Braze**. A visualização da integração com a **Braze** lista as credenciais que devem ser copiadas para a Braze.

![Página de integração da Mozart Data com a Braze selecionada e credenciais de conexão do Snowflake para uso na Braze.]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Em seguida, com login feito na Braze, acesse **Integrations > Technology Partners > Snowflake** para iniciar o processo de integração. Copie as credenciais da Mozart Data e adicione-as à página de importação de dados do Snowflake. Selecione **Set up sync details** e insira sua conta do Snowflake e as informações da tabela de origem.

![Formulário de integração do parceiro Snowflake na Braze com os campos de conta, warehouse, banco de dados e esquema preenchidos com as credenciais da Mozart Data.]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Em seguida, na tela de configuração de importação do Snowflake na Braze, escolha um nome para a sincronização, forneça os e-mails de contato e selecione um tipo de dados e uma frequência de sincronização.

#### Etapa 3: Adicione uma chave pública ao usuário da Braze {#step-3-add-a-public-key-to-the-braze-user}
Nesse ponto, você precisará voltar ao Snowflake para concluir a configuração. Adicione a chave pública exibida no dashboard da Braze ao usuário que você criou para que a Braze se conecte ao Snowflake.

Para obter mais informações sobre como fazer isso, consulte a [documentação do Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Se você quiser alternar as chaves a qualquer momento, a Mozart Data poderá gerar um novo par de chaves e fornecer a você a nova chave pública.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Etapa 4: Testar conexão {#step-4-test-connection}

Depois que o usuário for atualizado com a chave pública, retorne ao dashboard da Braze e selecione **Test connection**. Se o teste for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, a conexão não for bem-sucedida, será exibida uma mensagem de erro para ajudar a solucionar o problema.

![Resultado do teste de conexão da integração Snowflake na Braze mostrando uma prévia bem-sucedida após a aplicação da chave pública.]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Você deve testar com êxito uma integração antes que ela possa passar do estado Rascunho para o estado Ativo. Se você precisar sair da página de criação, sua integração será salva e você poderá acessar novamente a página de detalhes para fazer alterações e testes.
{% endalert %}

## Usando essa integração {#using-this-integration}

### Como acessar os dados da Braze como um usuário da Mozart Data {#how-to-access-braze-data-as-a-mozart-data-user}
Após a criação bem-sucedida de uma conta na Mozart Data, você poderá acessar seus dados da Braze sincronizados com seu data warehouse do Snowflake a partir da Mozart Data.

#### Transformações {#transforms}
A Mozart Data oferece uma camada de transformação SQL para permitir que os usuários criem uma visualização ou uma tabela. É possível criar uma tabela de dimensão no nível do usuário (por exemplo, `dim_users`) para resumir os dados de uso do produto de cada usuário, o histórico de transações e as atividades de engajamento com mensagens da Braze.

#### Análise {#analysis}
Usando os modelos de transformação ou os dados brutos sincronizados da Braze, é possível analisar o engajamento dos usuários com as mensagens da Braze. Além disso, é possível combinar os dados da Braze com outros dados de aplicativos e analisar como os insights obtidos com a interação dos usuários com as mensagens da Braze se relacionam com outros dados que você possa ter sobre os usuários. Por exemplo, informações demográficas, histórico de compras, uso de produtos e engajamento no atendimento ao cliente.

Isso pode ajudá-lo a tomar decisões mais informadas sobre estratégias de engajamento para melhorar a retenção de usuários. Tudo isso pode ser feito na interface da Mozart Data usando a ferramenta de consulta, onde você pode exportar os resultados para uma planilha do Google ou CSV para preparar uma apresentação.

#### Business intelligence (BI)
Pronto para visualizar e compartilhar seus insights com outros membros da equipe? A Mozart Data se integra a quase todas as ferramentas de BI. Se você ainda não tem uma ferramenta de BI, entre em contato com a Mozart Data para configurar uma conta gratuita do Metabase.