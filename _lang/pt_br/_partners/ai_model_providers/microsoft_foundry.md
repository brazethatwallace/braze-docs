---
nav_title: Microsoft Foundry
article_title: Microsoft Foundry
description: "Este artigo de referência descreve a parceria entre a Braze e o Microsoft Foundry, que permite conectar modelos de IA gerenciados pelo Foundry à Braze para uso com agentes de IA personalizados."
alias: /partners/microsoft_foundry/
page_type: partner
search_tag: Partner

---

# Microsoft Foundry

> O [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) é uma plataforma unificada como serviço do Azure para operações de IA empresarial, criação de modelos e desenvolvimento de aplicações.

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Microsoft Foundry integration' %}

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Microsoft Foundry permite usar modelos de IA generativa gerenciados no Microsoft Foundry ao criar agentes de IA personalizados. Atualmente, a integração é compatível com dois modelos: gpt-5.4-mini e gpt-5.4-nano. Com essa integração, seus agentes podem gerar textos personalizados, tomar decisões em tempo real ou atualizar campos de catálogo usando modelos gerenciados pelo Foundry.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Uma conta do Azure com uma assinatura ativa | Para obter ajuda, entre em contato com seu administrador ou consulte as [opções de conta do Azure](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account). |
| Instância do Microsoft Foundry | Uma instância do Microsoft Foundry para criar um projeto. |
| Projeto do Microsoft Foundry | Um projeto dentro da sua instância do Foundry para abrigar os modelos implantados. |
| Modelos implantados | Pelo menos um dos modelos compatíveis implantado dentro do projeto do Foundry. |
| Instância da Braze | Você pode encontrar sua instância da Braze na [página de visão geral da API]({{site.baseurl}}/api/basics#endpoints) ou com seu gerente de integração da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Implantar modelos compatíveis no Foundry {#deploy-supported-models-in-foundry}

A integração da Braze com o Microsoft Foundry é compatível com dois modelos: gpt-5.4-mini e gpt-5.4-nano. Ambos devem ser implantados em um projeto do Foundry dentro da instância do Foundry que você está integrando.

Para criar o projeto do Foundry e implantar os modelos, siga a [documentação do Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/tutorials/quickstart-create-foundry-resources?tabs=portal):

1. Faça login no Microsoft Foundry pelo portal do Azure.
2. No Microsoft Foundry, crie um projeto para abrigar os modelos que você deseja integrar com a Braze.
3. Decida se deseja usar o gpt-5.4-mini, o gpt-5.4-nano ou ambos.
4. Para cada modelo que deseja usar, implante-o seguindo a documentação do Microsoft Foundry. Não altere o nome de implantação padrão, ou a integração desse modelo poderá falhar.

## Integração {#integration}

Para conectar sua instância do Foundry à Braze:

1. Acesse **Integrações de parceiros** > **Parceiros de tecnologia** no dashboard da Braze e encontre **Microsoft Foundry**.
2. Insira sua **chave de API do Microsoft Foundry**.
3. Insira o **nome da sua instância do Microsoft Foundry**. Esse é o subdomínio antes de `.services.ai.azure.com`.
4. Selecione **Salvar**.

Após salvar, a Braze exibe um status de conexão com a data e hora da conexão. Você pode selecionar modelos do Foundry ao [criar um agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) no Console do agente.

{% alert important %}
Para usar o gpt-5.4-mini ou o gpt-5.4-nano, você deve implantar cada modelo no seu projeto do Foundry sem alterar o nome de implantação padrão.
{% endalert %}

Para confirmar que a integração está funcionando, acesse o Console do agente e crie um agente de teste usando um dos seus modelos implantados. Insira uma instrução simples, como "Me conte uma piada", e execute uma invocação de teste para verificar se o modelo responde conforme esperado.

Para remover a integração, selecione **Desconectar** na página de **Integração com o Microsoft Foundry**.

Entre em contato com o [suporte do Azure](https://azure.microsoft.com/en-us/support/options/) para quaisquer problemas ou dúvidas sobre sua integração.