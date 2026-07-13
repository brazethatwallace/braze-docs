---
nav_title: Boas práticas de backfill
article_title: Boas práticas de backfill
page_order: 7
page_type: reference
description: "Saiba como fazer o backfill correto de dados históricos para o BrazeAI Decisioning Studio, incluindo requisitos, armadilhas comuns e como evitar problemas de qualidade de dados que afetam a performance do modelo de IA."
---

# Boas práticas de backfill {#backfill-best-practices}

> Por diversos motivos, pode ser necessário fazer o backfill de dados — seja por erros nos dados, novas informações (como novas features) ou reconciliação de dados entre dois sistemas. Quando o backfill ocorrer, siga os princípios deste artigo para manter a qualidade dos dados e a performance do modelo.

## Quando o backfill é necessário {#when-backfilling-is-needed}

Backfill é o processo de preencher retroativamente um conjunto de dados com dados históricos. Cenários comuns incluem:

| Cenário | Descrição | Exemplo |
|---------|-----------|---------|
| **Novas features** | Você identificou uma nova métrica importante para o seu modelo e tem os logs históricos brutos para calculá-la. | Você adiciona "taxa de cliques" como uma feature e precisa de três meses de histórico para que o modelo tenha dados suficientes para aprender. |
| **Recuperação de dados** | Seu pipeline de dados falhou em dias específicos, criando lacunas nos dados entregues ao Decisioning Studio. | Uma falha no pipeline na terça-feira deixou uma lacuna. Após a correção ser implantada, você faz o backfill desses registros ausentes a partir do sistema de origem. |
| **Mudanças de lógica** | Você atualizou a fórmula de cálculo de uma feature ou alterou a definição de um evento. | Você redefiniu "usuário ativo" e precisa reexportar os dados históricos para que o modelo treine com a definição atualizada. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="When backfilling is needed" }

## Requisitos {#requirements}

Para que o Decisioning Studio funcione corretamente, todos os dados recebidos devem suportar backfill para períodos históricos. A janela de lookback específica necessária (medida em meses) depende dos requisitos de treinamento do modelo de IA. Consulte sua equipe de AI Decisioning Services para confirmar o valor correto para o seu caso de uso.

Ao realizar um backfill histórico, os seguintes padrões são obrigatórios:

- **Consistência de processo:** os snapshots históricos de features devem ser gerados usando um processo totalmente consistente com a criação de snapshots em tempo real. Se o seu pipeline em produção aplica transformações, agregações ou filtros, essas mesmas etapas devem ser aplicadas aos dados de backfill.
- **Consistência de schema:** o schema dos dados de backfill deve corresponder exatamente ao pipeline diário normal, incluindo os mesmos campos, tipos de dados e convenções de nomenclatura de colunas.

## Armadilhas comuns {#common-pitfalls}

### Vazamento de dados (viés de antecipação) {#data-leakage-look-ahead-bias}

O vazamento de dados é o erro de backfill mais crítico. Ele ocorre quando o processo de backfill incorpora inadvertidamente informações que não estariam disponíveis no momento em que o registro histórico foi gerado.

#### Por que isso importa {#why-it-matters}

Se o modelo treinar com dados que "conhecem o futuro", ele parecerá ter boa performance durante o treinamento, mas produzirá resultados ruins em produção, porque decisões em tempo real não têm acesso a dados futuros.

Por exemplo, considere calcular uma feature histórica de "lifetime value" usando o gasto total de um cliente até a data atual (ou seja, até hoje) e depois usar esse valor para prever um comportamento que ocorreu meses atrás. No momento daquele evento histórico, o lifetime value completo ainda não era conhecido.

Isso pode ser evitado sempre reconstruindo features históricas usando apenas as informações que estariam disponíveis no timestamp histórico, e não informações que se acumularam depois.

### Drift de schema e lógica {#schema-and-logic-drift}

Estruturas de dados e definições de negócio evoluem ao longo do tempo. Inconsistências entre dados históricos e dados em tempo real podem degradar silenciosamente a qualidade do modelo.

- **Drift de schema:** se um campo (por exemplo, `zip_code`) foi adicionado ao seu banco de dados recentemente, registros de backfill anteriores a essa mudança conterão valores nulos para esse campo. Garanta que seu pipeline lide com campos ausentes de forma adequada e que o modelo não dependa excessivamente de campos com cobertura histórica esparsa.
- **Drift de lógica:** se a definição de uma métrica mudou em um ponto específico no tempo (por exemplo, "usuário ativo" foi redefinido em 2024), aplicar a nova definição uniformemente a dados mais antigos (por exemplo, registros de 2022) pode criar picos ou quedas artificiais que não ocorreram de fato. Quando possível, aplique a definição que estava em vigor no momento de cada registro histórico, ou documente claramente o ponto de ruptura para que o modelo possa considerá-lo.

### Registros duplicados de jobs de backfill com falha {#duplicate-records-from-failed-backfill-jobs}

Jobs de backfill que falham no meio da execução e são reiniciados podem produzir registros duplicados se o processo não for projetado para evitar isso. Registros duplicados inflam artificialmente as métricas e introduzem ruído no treinamento do modelo.

**A solução:** projete todos os scripts de backfill para serem idempotentes: executar o mesmo job duas vezes deve produzir o mesmo resultado que executá-lo uma vez. Use um dos seguintes padrões:

- **Upsert (update ou insert):** com chave em um ID de transação único ou timestamp, de modo que reinserir um registro existente o atualize em vez de criar uma duplicata.
- **Delete e depois insert:** exclua os registros existentes para o intervalo de tempo alvo antes de inserir, para que o conjunto de dados seja sempre substituído de forma limpa.