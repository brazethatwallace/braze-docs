---
nav_title: Como o Braze usa Currents
article_title: Como a Braze usa Currents
page_order: 6
page_type: tutorial
description: "Este artigo de instruções do Currents o guiará pelo processo básico de configuração de entradas adequadas para dados de eventos, bem como sua transferência para um banco de dados e uma ferramenta de BI."
tool: Currents

---

# Como a Braze usa Currents

> A Braze usa Currents internamente com [parceiros]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners/) selecionados.

Filtramos nossos dados de e-mail e campanhas push em uma ferramenta de insights de negócios, Looker, mas o caminho até lá é um pouco diferente. Usamos uma versão invertida da metodologia Extract, Transform, Load (ETL)—trocando a ordem para Extract, Load, Transform (ELT).

## Etapa 1: Dados de eventos agregados e de admissão

Após lançar campanhas usando qualquer uma de nossas ferramentas de engajamento (como Campaigns ou Canvas), rastreamos dados de eventos usando nosso próprio sistema, bem como alguns de nossos parceiros de e-mail. Alguns desses dados são agregados e mostrados no dashboard, mas estávamos interessados em nos aprofundar mais!

## Etapa 2: Enviar dados de eventos para um parceiro de armazenamento de dados

Configuramos o Currents para enviar dados de eventos da Braze para o Amazon S3 para armazenamento e extração. Agora, sabemos que você pode usar o [Athena](https://aws.amazon.com/athena/) sobre o S3 para executar consultas. É uma ótima solução de curto prazo. Mas queríamos (e recomendamos a você) uma solução de longo prazo usando um banco de dados relacional e uma ferramenta de business intelligence/análise de dados.

O S3 fornece opções flexíveis de armazenamento e roteamento para mover, transformar e analisar dados. Não transformamos dados no S3 porque mantemos uma estrutura específica para eles.

## Etapa 3: Transformar dados de eventos com um banco de dados relacional

A partir do S3, escolhemos um data warehouse ([Snowflake Data Sharing](https://www.snowflake.com/try-the-data-warehouse-built-for-the-cloud/?&utm_medium=search&utm_source=adwords&utm_campaign=NA%20-%20Branded&utm_adgroup=NA%20-%20Branded%20Snowflake%20-%20Data&utm_term=%2Bsnowflake%20%2Bdata&utm_region=NA&gclid=EAIaIQobChMI0vLv6uDA3gIVEFqGCh3aiwMzEAAYASAAEgI72fD_BwE) ou Snowflake Reader Accounts, no nosso caso). Transformamos os dados lá e depois os movemos para o Looker, onde temos blocos configurados que estruturam e organizam nossos dados.

O Snowflake não é a única opção de data warehouse. Outras opções incluem [Redshift](https://aws.amazon.com/redshift/), [Google BigQuery](https://cloud.google.com/bigquery/?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-p-dr-1003905&utm_content=text-ad-none-any-DEV_c-CRE_288551384566-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+%7C+US+%7C+en+%7C+PHR+~+Big+Data+~+BigQuery+~+google+bigquery-KWID_43700035823403663-kwd-300487425311&utm_term=KW_google%20bigquery-ST_google+bigquery&gclid=EAIaIQobChMIl9OK8uHA3gIVyVmGCh1lFgB-EAAYASAAEgIfWfD_BwE) e mais!

### Snowflake Reader Accounts

O Snowflake Reader Accounts oferece aos usuários acesso aos mesmos dados e funcionalidades do [Snowflake Data Sharing]({{site.baseurl}}/partners/snowflake/), tudo sem exigir uma conta Snowflake ou um relacionamento de cliente com o Snowflake. Com o Reader Accounts, a Braze criará e compartilhará seus dados em uma conta e fornecerá credenciais para você fazer login e acessar seus dados. Isso significa que toda a cobrança de compartilhamento de dados e uso será gerenciada inteiramente pela Braze.

Para saber mais, entre em contato com seu gerente de sucesso do cliente.

#### Recursos adicionais
Para recursos úteis de monitoramento de uso, confira os artigos do Snowflake sobre [Resource Monitors](https://docs.snowflake.com/en/user-guide/resource-monitors.html) e [Viewing Warehouse Credit Usage](https://docs.snowflake.com/en/user-guide/credits.html#viewing-warehouse-credit-usage-for-your-account).

## Etapa 4: Usar uma ferramenta de business intelligence (BI) para manipular seus dados

Por fim, usamos uma ferramenta de BI para analisar nossos dados, transformá-los em gráficos e outras ferramentas visuais, e mais, usando [Looker e blocos do Looker](https://www.marketplace.looker.com/) para que não precisemos fazer ETL ou ELT dos dados toda vez que eles são movidos do Currents.

Se inspirou para fazer o mesmo? Confira os documentos a seguir para obter mais informações sobre eles e como você pode usá-los para construir seu banco de dados!

- [Bloco de comportamento do usuário](https://marketplace.looker.com/marketplace/detail/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)
- [Bloco de engajamento com mensagem](https://marketplace.looker.com/marketplace/detail/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct)