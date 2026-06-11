---
nav_title: Importação de Coorte do Heap
article_title: Importação de Coorte do Heap
description: "Este artigo de referência detalha a integração entre a Braze e a Heap, uma plataforma de insights digitais, que permite a importação de dados da Heap para a Braze, a criação de coortes de usuários e a exportação de dados da Braze para a Heap para criar segmentos."
alias: /partners/heap_cohort_import/
page_type: partner
search_tag: Partner

---

# Importação de coorte do Heap {#heap-cohort-import}

> A [Heap](https://heap.io/), uma plataforma de insights digitais, concentra você nas oportunidades da sua experiência digital que mais impactam seus negócios, eliminando o atrito, encantando seus clientes e acelerando a receita.

A integração entre a Braze e a Heap permite [importar dados da Heap para a Braze](#data-import-integration), criar coortes de usuários e [exportar dados da Braze para a Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/) para criar segmentos.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Heap | É necessário ter uma conta [Heap](https://heap.io/about) para aproveitar essa parceria. |
| Chave de importação de dados da Braze | Isso pode ser obtido no dashboard da Braze em **Integrações de parceiros** > **Parceiros de tecnologia** e selecionando **Heap**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
| Braze Currents | Para exportar dados da Braze para a Heap, você precisa ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) ativado na sua conta. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}
- Reengaje usuários que abandonaram um funil: dispare mensagens de reengajamento quando os usuários abandonarem o funil de compra ou de inscrição.
- Personalize a experiência de teste: identifique os pontos de atrito na sua experiência de avaliação e envie lembretes no momento certo para reengajar os usuários durante uma avaliação e ajudá-los a obter valor.
- Aumente o engajamento em anúncios e ofertas: direcione promoções, atualizações e anúncios de novos serviços para os públicos relevantes.

## Integração de importação de dados {#data-import-integration}

Use a integração Heap to Braze para sincronizar automaticamente as coortes definidas na Heap com a Braze.

### Etapa 1: Obter a chave de importação de dados da Braze {#step-1-get-the-braze-data-import-key}

Na Braze, navegue até **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Heap**.

Nessa página, você pode encontrar sua chave de importação de dados e um endpoint REST. Anote esses dois valores e forneça-os ao seu gerente de conta da Heap para concluir a configuração da integração.

![]({% image_buster /assets/img/heap/heap2.png %}){: style="max-width:90%;"}

### Etapa 2: Segmentar usuários importados na Braze {#step-2-segment-imported-users-in-braze}

Na Braze, navegue até **Segments**, dê um nome ao seu segmento de coorte da Heap e selecione **Heap Cohorts** como filtro. Aqui você pode escolher qual coorte da Heap deseja incluir. Depois que seu segmento de coorte da Heap for criado, você poderá selecioná-lo como filtro de público ao criar uma Campaign ou Canvas.

![No criador de segmentos da Braze, o filtro de atributos do usuário "Heap cohort" está definido como "includes" e "Heap Test Cohort".]({% image_buster /assets/img/heap/heap1.png %}){: style="max-width:90%;"}

### Usando essa integração {#using-this-integration}

Para usar seu segmento da Heap, crie uma Campaign ou Canvas na Braze e selecione o segmento como seu público-alvo.

![No criador de Campaigns da Braze, na etapa de direcionamento, o filtro "Direcionar por segmento de usuários" está definido como "Heap cohort".]({% image_buster /assets/img/heap/heap3.png %}){: style="max-width:90%;"}

{% alert important %}
Somente os usuários que já existem na Braze serão adicionados ou removidos de uma coorte. A importação de coorte não criará novos usuários na Braze.
{% endalert %}

## Detalhes da integração {#integration-details}

A estrutura de carga útil para dados exportados é a mesma que a estrutura de carga útil para conectores HTTP personalizados, que pode ser visualizada no [repositório de exemplos para conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## Correspondência de usuários {#user-matching}

Os usuários identificados podem ser correspondidos pelo `external_id` ou `alias`. Os usuários anônimos podem ser correspondidos pelo `device_id`. Usuários identificados que foram originalmente criados como usuários anônimos não podem ser identificados pelo `device_id` e devem ser identificados pelo `external_id` ou `alias`.