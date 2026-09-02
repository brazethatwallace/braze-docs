---
nav_title: Google Gemini
article_title: Google Gemini
description: "Este artigo de referência descreve a parceria entre a Braze e o Google Gemini, que permite conectar modelos Gemini à Braze para uso com agentes de IA personalizados."
alias: /partners/gemini/
page_type: partner
search_tag: Partner

---

# Google Gemini

> O [Google Gemini](https://deepmind.google/technologies/gemini/) é a família de modelos de IA do Google que combina raciocínio avançado em texto, código e imagens para ajudar as marcas a oferecer experiências mais inteligentes e personalizadas.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_Essa integração é mantida pelo Google._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Google Gemini permite conectar o Gemini à Braze usando uma chave de API or interface de programação do aplicativo (API) ou fazendo login com sua conta do Google, para que você possa usar modelos Gemini ao criar agentes de IA personalizados. Com essa integração, seus agentes podem gerar textos personalizados, tomar decisões em tempo real ou atualizar campos do catálogo usando os modelos Gemini do Google.

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Conta do Google Cloud | Uma conta do Google Cloud com acesso à API or interface de programação do aplicativo (API) do Gemini. Você pode se autenticar com uma chave de API or interface de programação do aplicativo (API) ou conectando sua conta do Google e selecionando um projeto do GCP no dashboard da Braze. Para obter ajuda, entre em contato com seu administrador ou com o [suporte do Google Cloud](https://cloud.google.com/support). |
| Instância da Braze | Você pode encontrar sua instância da Braze na [página de visão geral da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#endpoints) ou com seu gerente de integração da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para conectar o Google Gemini à Braze:

1. Acesse **Partner Integrations** > **Technology Partners** no dashboard da Braze e encontre o Google Gemini.
2. Em **Authentication Method**, escolha **API or interface de programação do aplicativo (API) Key** ou **Connect Google Account**.
3. Conclua a configuração do método escolhido:
   - **API or interface de programação do aplicativo (API) Key:** Em **API or interface de programação do aplicativo (API) Type**, selecione **Gemini API or interface de programação do aplicativo (API)** ou **Gemini Enterprise Agent Platform (formerly Vertex AI)**. Insira sua chave de API or interface de programação do aplicativo (API). Se você selecionou Gemini Enterprise Agent Platform, insira também o **Project ID**. Selecione **Save**.
   - **Connect Google Account:** Selecione **Connect Google Account**, depois selecione **Connect Google** e faça login com sua conta do Google. Selecione seu **GCP Project** no menu suspenso. Se tanto a Gemini API or interface de programação do aplicativo (API) quanto a Gemini Enterprise Agent Platform estiverem ativadas nesse projeto, escolha o **API or interface de programação do aplicativo (API) Type** que a Braze deve usar. Selecione **Save**.

{% alert note %}
**Connect Google Account** aparece apenas para espaços de trabalho em que essa opção de autenticação está ativada.
{% endalert %}

Depois de salvar, você pode selecionar modelos Gemini ao [criar um agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) no Console do agente.

Entre em contato com o [suporte do Google Cloud](https://cloud.google.com/support) em caso de problemas ou dúvidas sobre sua integração.