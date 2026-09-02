---
nav_title: Amazon Bedrock
article_title: Amazon Bedrock
description: "Este artigo de referência descreve a parceria entre a Braze e o Amazon Bedrock, que permite conectar modelos do Bedrock à Braze para uso com agentes de IA personalizados."
alias: /partners/amazon_bedrock/
page_type: partner
search_tag: Partner

---

# Amazon Bedrock

> O [Amazon Bedrock](https://aws.amazon.com/bedrock/) é um serviço totalmente gerenciado da AWS que fornece acesso a modelos de base de empresas líderes em IA por meio de uma API or interface de programação do aplicativo (API) unificada, para que as marcas possam criar e escalar aplicações de IA generativa na AWS.

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Amazon Bedrock integration' %}

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Amazon Bedrock permite conectar suas credenciais do Amazon Bedrock à Braze para que você possa usar modelos hospedados no Bedrock ao criar agentes de IA personalizados. Com essa integração, seus agentes podem gerar textos personalizados, tomar decisões em tempo real ou atualizar campos de catálogo usando modelos disponíveis por meio do Amazon Bedrock.

Quando você conecta o Amazon Bedrock, a Braze exibe um conjunto curado de modelos do Bedrock para agentes personalizados. Os modelos disponíveis na Braze podem ser diferentes do catálogo completo da sua conta AWS.

A Braze usa o endpoint `bedrock-mantle` do Amazon Bedrock para essa integração. O Amazon Bedrock também documenta um endpoint `bedrock-runtime` separado, com suporte a modelos e recursos diferentes. Portanto, ao consultar a documentação da AWS sobre disponibilidade ou comportamento, siga as orientações para [`bedrock-mantle`](https://docs.aws.amazon.com/bedrock/latest/userguide/endpoints.html).

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Uma conta AWS com acesso ao Amazon Bedrock | Uma conta AWS com acesso ao Amazon Bedrock na região da AWS onde seus modelos estão hospedados. Para obter ajuda, entre em contato com seu administrador ou com o [AWS Support](https://aws.amazon.com/support). |
| Acesso ao modelo do Amazon Bedrock | Acesso na sua conta AWS aos modelos do Bedrock que você planeja usar. Alguns modelos, como os da Anthropic, exigem que o acesso seja concedido na sua conta AWS. Nem todos os modelos estão disponíveis em todas as regiões da AWS — verifique a disponibilidade regional de cada modelo no console do Amazon Bedrock ou em [Disponibilidade regional por modelos](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html) antes de conectar. |
| Credenciais de autenticação | Uma [chave de API or interface de programação do aplicativo (API) do Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html) de longo prazo ou, quando a autenticação por função IAM estiver ativada para o seu espaço de trabalho, uma função IAM que a Braze possa assumir. |
| Instância da Braze | Você pode encontrar sua instância da Braze na [página de visão geral da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#endpoints) ou com seu gestor de integração da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para conectar o Amazon Bedrock à Braze:

1. Acesse **Partner Integrations** > **Technology Partners** no dashboard da Braze, depois pesquise e selecione **Amazon Bedrock**.
2. Em **Authentication method**, escolha **API or interface de programação do aplicativo (API) key** ou **AWS IAM role** (quando disponível).
3. Conclua a configuração do método escolhido:
   - **API or interface de programação do aplicativo (API) key:** Insira sua **Amazon Bedrock API or interface de programação do aplicativo (API) key** de longo prazo. Selecione a **AWS region** onde seus modelos do Bedrock estão hospedados. Selecione **Save**.
   - **AWS IAM role:** Use os valores exibidos pela Braze para configurar a política de confiança da sua IAM role e, em seguida, insira os detalhes da role na Braze:
     1. Copie o **Braze AWS account ID** e confie nessa conta na política de confiança da sua IAM role.
     2. Copie o **Braze external ID** e exija-o na política de confiança da sua role com uma condição `sts:ExternalId`. Selecione **Generate new external ID** se precisar de um novo valor.
     3. Insira o **AWS role ARN** da IAM role que possui permissões do Amazon Bedrock. O ARN deve corresponder a `arn:aws:iam::<account-id>:role/<role-name>`.
     4. Selecione a **AWS region** onde seus modelos do Bedrock estão hospedados.
     5. Selecione **Save**.

{% alert note %}
**AWS IAM role** aparece apenas para espaços de trabalho em que essa opção de autenticação está ativada. Com a autenticação por IAM role, a Braze assume sua role para gerar credenciais temporárias do Amazon Bedrock e não armazena uma chave de API or interface de programação do aplicativo (API) de longo prazo.
{% endalert %}

Após salvar, a Braze exibe um status de conexão com a data e hora da conexão. Você pode selecionar modelos do Amazon Bedrock ao [criar um agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) no Agent Console.

{% alert important %}
Nem todos os modelos do Amazon Bedrock estão disponíveis em todas as regiões da AWS. Antes de selecionar uma **AWS region** na Braze, abra os detalhes do modelo no Amazon Bedrock e confirme que o modelo lista essa região. Modelos que não estão disponíveis na sua região conectada retornam erros durante a invocação do agente (por exemplo, que o modelo não existe ou não está mais disponível). Consulte [Models at a glance](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html) para mais detalhes.
{% endalert %}

Para confirmar que a integração está funcionando, acesse o Agent Console e crie um agente de teste usando um dos seus modelos do Bedrock. Insira uma instrução como "Conte uma piada" e execute uma invocação de teste para verificar se o modelo responde conforme esperado.

Para remover a integração, selecione **Disconnect** na página de **Amazon Bedrock integration**.

Para problemas com sua conta ou credenciais do Amazon Bedrock, entre em contato com o [AWS Support](https://aws.amazon.com/support).