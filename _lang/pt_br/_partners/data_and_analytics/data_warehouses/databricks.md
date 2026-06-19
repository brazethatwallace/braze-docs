---
nav_title: Databricks
article_title: Databricks
description: "Este artigo descreve o Databricks Delta Sharing com a Braze (beta fechado), que permite acessar dados de engajamento e de Campaign da Braze na sua conta do Databricks."
page_type: partner
search_tag: Partner
permalink: /databricks/
hidden: true
---

# Databricks

> O [Databricks](https://www.databricks.com/) é uma plataforma de análise de dados unificada e aberta para criar, implantar, compartilhar e manter soluções corporativas de dados, análise de dados e IA em escala. A Plataforma de Inteligência de Dados do Databricks se integra ao armazenamento em nuvem e à segurança da sua conta na nuvem, além de gerenciar e implantar a infraestrutura de nuvem para você.

{% alert important %}
O Databricks Delta Sharing com a Braze está em **beta fechado**. A disponibilidade, as regiões suportadas e o comportamento do produto podem mudar. Entre em contato com o seu gerente de sucesso do cliente da Braze para participar ou confirmar se esse recurso está ativado para o seu espaço de trabalho.
{% endalert %}

## Delta Sharing (da Braze para o Databricks) {#delta-sharing-braze-to-databricks}

O [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html) do Databricks permite compartilhar dados de forma segura com unidades de negócios e subsidiárias em diferentes nuvens ou regiões, sem copiar ou replicar os dados.

**Use o Delta Sharing quando quiser:**
- Consultar dados de eventos e de Campaign da Braze usando o Databricks SQL
- Criar relatórios complexos e realizar modelagem de atribuição
- Combinar dados da Braze com outros dados na sua conta do Databricks
- Comparar seus dados de engajamento entre canais, setores e plataformas de dispositivos

Para instruções de configuração, consulte [Databricks Delta Sharing]({{site.baseurl}}/delta_sharing/).

Para saber mais sobre o Delta Sharing no Databricks, consulte [O que é Delta Sharing?](https://www.databricks.com/product/delta-sharing).

## Pré-requisitos {#prerequisites}

Antes de usar esse recurso, conclua o seguinte:

| Requisito | Descrição |
| ----------- | ----------- |
| Acesso à Braze | Para acessar esse recurso na Braze, entre em contato com o gerente da sua conta ou gerente de sucesso do cliente da Braze. |
| Conta do Databricks | Uma conta do Databricks com permissões de `admin`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

Quando estiver pronto para configurar o compartilhamento e consultar dados compartilhados, prossiga para [Databricks Delta Sharing]({{site.baseurl}}/delta_sharing/).