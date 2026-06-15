---
nav_title: Databricks Mosaic
article_title: Databricks Mosaic
description: "Este artigo de referência descreve a parceria entre a Braze e o Databricks Mosaic, que permite conectar modelos do Databricks à Braze para uso com agentes de IA personalizados."
alias: /partners/databricks_mosaic/
page_type: partner
search_tag: Partner

---

# Databricks Mosaic

> O [Databricks Mosaic AI](https://www.databricks.com/product/artificial-intelligence) é a plataforma unificada do Databricks para criar, implantar e gerenciar modelos de IA e machine learning em escala na Databricks Data Intelligence Platform.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_Essa integração é mantida pelo Databricks._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Databricks Mosaic permite conectar seu token e espaço de trabalho do Databricks à Braze para que você possa usar modelos do Databricks ao criar agentes de IA personalizados. A Braze usa suas credenciais do Databricks Mosaic para gerar conteúdo para seus clientes. Com essa integração, seus agentes podem gerar textos personalizados, tomar decisões em tempo real ou atualizar campos de catálogo usando modelos do Databricks.

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Conta do Databricks com token de acesso pessoal | Uma conta do Databricks com um [token de acesso pessoal](https://docs.databricks.com/en/dev-tools/auth/pat.html). Para obter ajuda, entre em contato com seu administrador ou com o [suporte do Databricks](https://help.databricks.com/). |
| Nome do espaço de trabalho do Databricks | O nome do espaço de trabalho (ou instância) da sua conta do Databricks. Esse é o subdomínio antes de `.cloud.databricks.com` ou `.azuredatabricks.net` (por exemplo, `dbc-eb57d699-f22c`). |
| Instância da Braze | Você pode encontrar sua instância da Braze na [página de visão geral da API]({{site.baseurl}}/api/basics/#endpoints) ou com seu gerente de integração da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para conectar suas credenciais do Databricks Mosaic à Braze:

1. Acesse **Integrações de parceiros** > **Parceiros de tecnologia** no dashboard da Braze e encontre **Databricks Mosaic Integration**.
2. Insira seu **Databricks Token**.
3. Insira o **Databricks Workspace Name**. Esse é o subdomínio antes de `.cloud.databricks.com` ou `.azuredatabricks.net`.
4. Selecione **Save**.

Após salvar, a Braze exibe um status de conexão com a data e a hora da conexão. Você pode selecionar modelos do Databricks ao [criar um agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/) no Console do agente.

Para remover a integração, selecione **Disconnect** na página **Databricks Mosaic Integration**.

Entre em contato com o [suporte do Databricks](https://help.databricks.com/) caso tenha problemas ou dúvidas sobre sua integração.