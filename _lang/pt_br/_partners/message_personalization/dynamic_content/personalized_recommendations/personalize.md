---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "Este artigo de referência descreve a parceria entre a Braze e a Personalize.AI, uma plataforma de negócios SaaS baseada em IA que impulsiona o crescimento da receita a partir de recomendações personalizadas."
alias: /partners/personalize_ai/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> A [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) faz parceria com a Braze para gerar receita incremental ao entregar mensagens e ofertas personalizadas enviadas através da Braze.

A integração entre a Braze e a Personalize.AI permite exportar dados da Personalize.AI para a plataforma Braze para personalização e direcionamento de mensagens.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Instância da Personalize.AI | Uma instância da Personalize.AI é necessária para aproveitar esta parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com todas as permissões. <br><br>Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | A URL do seu endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

* Implantar testes, incluindo estratificação flexível, para obter resultados a partir do feedback do cliente
* Fornecer recomendações personalizadas para itens e ofertas, incluindo tratamento, timing e conteúdo
* Identificar objetivos prioritários e direcionar seu público ideal através da Braze
* Identificar oportunidades para reengajar usuários inativos
* Usar dados de geolocalização para encontrar o público certo para locais recém-abertos
* Usar modelagem de semelhança para construir com base nos dados limitados disponíveis para novos usuários, combinando-os com as recomendações mais relevantes
* Identificar as maneiras corretas de engajar os clientes ao longo de seu ciclo de vida
* Avaliar proativamente os clientes quanto à probabilidade de churn e atribuir uma pontuação de risco para encontrar indicadores precoces de churn
* Direcionar clientes com intervenções personalizadas para evitar que se tornem inativos

## Integração {#integration}

### Configure uma conexão com a Braze na Personalize.AI {#configure-a-connection-with-braze-in-personalizeai}

1. Na Personalize.AI, navegue até a guia **Integrations**, localizada em **Operationalization**, na sua instância da Personalize.AI.
2. Clique em **Braze**.
3. Configure sua integração com a Braze.
    * **Connection Name:** dê um nome para sua conexão. É assim que sua integração será referida na Personalize.AI.
    * **Sync Frequency:** a frequência de sincronização controla com que frequência a Personalize.AI exporta dados para a Braze. Selecione **Daily**, **Weekly** ou **Monthly**.
    * **API Key:** adicione sua chave de API da Braze.
    * **API URL:** adicione a URL do seu endpoint REST da Braze.
4. Clique em **EXPORT** para exportar dados para a Braze.

Depois que seus dados forem exportados, a Personalize.AI continuará a enviar dados para a Braze nos intervalos determinados pela frequência de sincronização que você definiu durante a integração.

## Usando essa integração {#using-this-integration}

A Personalize.AI exporta identificadores usados para direcionamento personalizado na Braze. Esses atributos personalizados indicam timing, conteúdo, tratamento e ofertas para cada cliente. Dependendo da integração, os campos podem ser passados como um evento ou obtidos pelas [APIs de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/public_apis/) em vez de armazenados no perfil do cliente. A Personalize.AI suporta o uso de `external_id` como identificador.

Os atributos de dados importados para a Braze são intuitivamente nomeados para uso em Canvas, seguindo uma terminologia consistente. Por exemplo, o atributo `C402_Target_Variant` na Personalize.AI seria exportado para a Braze como `"P.AI_Model_Treatment"`. Os atributos exportados da Personalize.AI são projetados para não interferir com quaisquer atributos existentes ou rastreamento do seu uso. Esses atributos são validados continuamente para confirmar que você pode referenciá-los com confiança.

Por exemplo, aqui está um conjunto de atributos de clientes relacionados a um exemplo de Canvas focado em churn.

| Atributo Personalize.AI | Valor |
| ----------- | ------------- |
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "Churn_Mitigation" |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | Treatment |
| `C4_Treatment` | "P.AI_Model" |
| `C4_Offer_Value` | $3 |
| `C4_Item_Recom` | "Caesar Salad" |
| `C4_Subject_Line` | "We miss you" |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Usando essa integração" }