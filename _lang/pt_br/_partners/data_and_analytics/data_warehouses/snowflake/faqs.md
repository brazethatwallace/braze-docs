---
nav_title: FAQ
article_title: Perguntas frequentes sobre o compartilhamento de dados do Snowflake
page_order: 50
page_type: FAQ
description: "Este artigo responde a perguntas frequentes sobre o compartilhamento de dados do Snowflake."

---

# Perguntas frequentes {#frequently-asked-questions}

## É possível ofuscar dados de IPI por meio do compartilhamento de dados do Snowflake? {#is-it-possible-to-obfuscate-pii-data-via-snowflake-data-sharing}
Não, no momento isso não é suportado.

## Preciso de compartilhamento de dados na mesma região ou entre regiões? {#do-i-need-data-share-for-the-same-region-or-cross-region}
Use o compartilhamento de dados na mesma região nos seguintes cenários:
- Sua conta Snowflake está em US-EAST-1 (AWS) e a região do seu dashboard da Braze está nos EUA.
- Sua região Snowflake está em EU-CENTRAL-1 (AWS) e a região do seu dashboard da Braze está na UE.
- Sua região Snowflake está em AP-Northeast-1 (AWS) e a região do seu dashboard da Braze está no Japão.
- Sua região Snowflake está em AP-Southeast-2 (AWS) e a região do seu dashboard da Braze está na Austrália.
- Sua região Snowflake está em AP-Southeast-3 (AWS) e a região do seu dashboard da Braze está na Indonésia.

Caso contrário, use o compartilhamento de dados entre regiões.

## O que devo fazer com meu compartilhamento de dados ao mudar para uma nova conta do Snowflake? {#what-should-i-do-with-my-data-share-when-i-switch-to-a-new-snowflake-account}
Você pode excluir o compartilhamento de dados antigo associado à sua conta anterior do Snowflake e, em seguida, criar um novo compartilhamento para a nova conta. Todos os dados históricos estarão disponíveis no novo compartilhamento.

## O que acontece se eu trocar meu compartilhamento de dados para um novo espaço de trabalho da Braze? {#what-happens-if-i-switch-my-data-share-to-a-new-braze-workspace}

Se você reconfigurar uma integração de compartilhamento de dados existente para usar um espaço de trabalho diferente da Braze, poderá ver este erro no Snowflake ao consultar tabelas:

> Shared database is no longer available for use. It will need to be re-created if and when the publisher makes it available again.

Para resolver isso, você precisa excluir e recriar o compartilhamento dentro do Snowflake:

1. Exclua o banco de dados que foi criado com o compartilhamento anterior.
2. Crie o banco de dados novamente de acordo com as [instruções de integração]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake#step-2-create-the-database-in-snowflake).
3. Conceda novamente os privilégios de acesso necessários ao novo banco de dados.
4. Recrie quaisquer views (se aplicável) que faziam referência ao banco de dados antigo.

{% alert note %}
Na nova interface do Snowflake, você pode encontrar o compartilhamento da Braze em **Data Products** > **Private Sharing** > **Shared with you**.
{% endalert %}

## Por que não vejo dados no meu compartilhamento de dados? {#why-dont-i-see-data-in-my-data-share}
Você pode ter usado o ID de conta do Snowflake incorreto ao criar seu compartilhamento de dados. O ID de conta no dashboard de compartilhamento de dados deve corresponder à saída de `CURRENT_ACCOUNT()` da sua conta do Snowflake.

Se o seu compartilhamento é entre regiões, os dados podem não estar disponíveis imediatamente. Dependendo do volume de dados, pode levar algumas horas para que os dados sejam sincronizados com a sua região.

## Por que estou recebendo um erro de conformidade com a HIPAA ao criar um compartilhamento de dados? {#why-am-i-receiving-a-hipaa-compliance-error-when-creating-a-data-share}

A conta especificada não é compatível com a HIPAA ou está em [edições do Snowflake](https://docs.snowflake.com/en/user-guide/intro-editions) inferiores à Business Critical. Sua conta do Snowflake precisa ser atualizada para a edição Business Critical para estar em conformidade com a HIPAA no compartilhamento de dados. Entre em contato com o suporte do Snowflake para obter mais assistência com o upgrade da sua conta.

## Por que não consigo recriar um compartilhamento de dados após excluir um? {#why-cant-i-recreate-a-data-share-after-deleting-one}

O sistema pode ainda estar processando a exclusão do seu compartilhamento de dados anterior. Aguarde alguns minutos para que o processo de desprovisionamento seja concluído e tente criar o novo compartilhamento de dados novamente.

## Quantas vezes preciso executar `CREATE DATABASE` quando tenho vários espaços de trabalho compartilhando dados para a mesma conta Snowflake? {#how-many-times-do-i-need-to-run-create-database-when-i-have-multiple-workspaces-sharing-data-to-the-same-snowflake-account}

Você precisa executar `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` apenas uma vez. Quando vários compartilhamentos de dados de diferentes espaços de trabalho da Braze são compartilhados para a mesma conta Snowflake, eles são automaticamente combinados no mesmo compartilhamento. Depois que você cria o banco de dados inicial, os dados de espaços de trabalho adicionais são automaticamente adicionados ao banco de dados existente sem a necessidade de solicitações de compartilhamento ou etapas de criação de banco de dados adicionais.

Por exemplo, se você criar um compartilhamento de dados para a conta Snowflake 123 a partir do espaço de trabalho A, você aceita a solicitação de compartilhamento e cria um banco de dados. Quando você criar posteriormente um compartilhamento de dados para a mesma conta Snowflake 123 a partir do espaço de trabalho B, nenhuma nova solicitação de compartilhamento é enviada — os dados são imediatamente adicionados ao compartilhamento existente e ficam disponíveis no banco de dados criado anteriormente.

## Se eu tiver vários espaços de trabalho, um único banco de dados contém dados de todos eles? {#if-i-have-multiple-workspaces-does-a-single-database-contain-data-from-all-of-them}

Sim. Quando você compartilha dados de vários espaços de trabalho da Braze para a mesma conta do Snowflake, todos os dados são combinados em um único compartilhamento e ficam disponíveis no mesmo banco de dados. Você pode filtrar os dados por `app_group_id` para distinguir entre os espaços de trabalho.

Como prática recomendada, sempre filtre por `app_group_id` nas suas consultas para garantir que elas continuem funcionando corretamente no futuro. Isso garante que seus dashboards e relatórios permaneçam precisos caso você adicione espaços de trabalho adicionais no futuro. Sem esse filtro, suas métricas podem incluir inesperadamente dados de espaços de trabalho recém-adicionados.

## Qual é a abordagem recomendada para gerenciar dados de vários espaços de trabalho no Snowflake? {#what-is-the-recommended-approach-for-managing-data-from-multiple-workspaces-in-snowflake}

Envie todos os dados da Braze para o mesmo banco de dados e filtre por `app_group_id` para distinguir entre espaços de trabalho. Essa abordagem simplifica o gerenciamento de dados e garante relatórios consistentes em toda a sua organização.

## Quantos conectores de compartilhamento de dados do Snowflake eu preciso para múltiplos espaços de trabalho? {#how-many-snowflake-data-share-connectors-do-i-need-for-multiple-workspaces}

O número de conectores que você precisa depende da sua configuração específica e dos seus direitos de uso. Entre em contato com a equipe da sua conta Braze para saber mais sobre quais direitos são adequados para o seu caso de uso.

## Quais opções existem para isolar dados de diferentes espaços de trabalho dentro da mesma conta Snowflake? {#what-options-exist-for-isolating-data-from-different-workspaces-within-the-same-snowflake-account}

Você pode isolar logicamente usando a coluna `app_group_id`, que identifica a qual espaço de trabalho cada linha de dados pertence. As abordagens mais comuns são:

- **Views (recomendado):** Crie uma view para cada espaço de trabalho filtrada por `app_group_id`. Isso evita duplicar dados e ainda oferece a cada equipe ou caso de uso uma visão limpa e delimitada dos dados do seu espaço de trabalho.
- **Cópias em tabelas locais:** Copie os dados em tabelas separadas filtradas por `app_group_id`. Isso duplica os dados, então a abordagem com views geralmente é preferível.
- **Políticas de acesso por linha e roles:** Use políticas de acesso por linha nativas do Snowflake combinadas com roles para restringir quais linhas cada role pode consultar. Isso mantém os dados em uma única tabela enquanto aplica o controle de acesso no momento da consulta.

Você configura essas opções dentro da sua conta Snowflake.

## Posso usar uma conta Snowflake diferente para isolar dados de espaços de trabalho distintos? {#can-i-use-a-different-snowflake-account-to-isolate-data-from-different-workspaces}

Sim. Se o espaço de trabalho A compartilha com a conta X e o espaço de trabalho B compartilha com a conta Y, cada conta recebe um compartilhamento independente com dados separados. No entanto, a maioria das organizações usa uma única conta Snowflake para todos os dados de negócios. Portanto, essa abordagem pode adicionar sobrecarga operacional. Considere essa compensação antes de escolhê-la em vez das abordagens de isolamento lógico descritas na seção anterior.

## O isolamento de dados do espaço de trabalho é um caso de uso compatível com o Snowflake Data Sharing? {#is-workspace-data-isolation-a-supported-use-case-for-snowflake-data-sharing}

Sim, por meio das abordagens de isolamento lógico descritas nas seções anteriores. A Braze não cria compartilhamentos separados para cada espaço de trabalho, então você gerencia o isolamento no nível do Snowflake usando views, políticas de acesso por linha ou contas separadas.