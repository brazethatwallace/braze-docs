---
nav_title: Amazon Bedrock
article_title: Amazon Bedrock
description: "Este artigo de referência descreve a parceria entre a Braze e o Amazon Bedrock, que permite conectar modelos do Bedrock à Braze para uso com agentes de IA personalizados."
alias: /partners/amazon_bedrock/
page_type: partner
search_tag: Partner

---

# Amazon Bedrock

> O [Amazon Bedrock](https://aws.amazon.com/bedrock/) é um serviço totalmente gerenciado da AWS que fornece acesso a modelos de base de empresas líderes em IA por meio de uma API unificada, para que as marcas possam criar e escalar aplicações de IA generativa na AWS.

{% multi_lang_include alerts/early_access_beta_alert.md feature='The Amazon Bedrock integration' %}

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Amazon Bedrock permite conectar suas credenciais do Amazon Bedrock à Braze para que você possa usar modelos hospedados no Bedrock ao criar agentes de IA personalizados. Com essa integração, seus agentes podem gerar textos personalizados, tomar decisões em tempo real ou atualizar campos de catálogo usando modelos disponíveis no Amazon Bedrock.

Quando você conecta o Amazon Bedrock, a Braze exibe um conjunto curado de modelos do Bedrock para agentes personalizados. Os modelos disponíveis na Braze podem ser diferentes do catálogo completo da sua conta AWS.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Uma conta AWS com acesso ao Amazon Bedrock | Uma conta AWS com acesso ao Amazon Bedrock na região da AWS onde seus modelos estão hospedados. Para obter ajuda, entre em contato com seu administrador ou com o [Suporte da AWS](https://aws.amazon.com/support). |
| Acesso a modelos do Amazon Bedrock | Acesso na sua conta AWS aos modelos do Bedrock que você pretende usar. Alguns modelos, como os da Anthropic, exigem que o acesso seja concedido na sua conta AWS. Nem todos os modelos estão disponíveis em todas as regiões da AWS. |
| Credenciais de autenticação | Uma [chave de API do Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html) de longo prazo ou, quando a autenticação por função IAM estiver ativada para o seu espaço de trabalho, uma função IAM que a Braze possa assumir. |
| Instância da Braze | Você pode encontrar sua instância da Braze na [página de visão geral da API]({{site.baseurl}}/api/basics#endpoints) ou com seu gerente de integração da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para conectar o Amazon Bedrock à Braze:

1. Acesse **Integrações de Parceiros** > **Parceiros de Tecnologia** no dashboard da Braze, depois pesquise e selecione **Amazon Bedrock**.
2. Em **Método de autenticação**, escolha **Chave de API** ou **Função IAM da AWS** (quando disponível).
3. Conclua a configuração para o método escolhido:
   - **Chave de API:** insira sua **chave de API do Amazon Bedrock** de longo prazo. Selecione a **região da AWS** onde seus modelos do Bedrock estão hospedados. Selecione **Salvar**.
   - **Função IAM da AWS:** use os valores exibidos pela Braze para configurar a política de confiança da sua função IAM e, em seguida, insira os detalhes da função na Braze:
     1. Copie o **ID da conta AWS da Braze** e confie nessa conta na política de confiança da sua função IAM.
     2. Copie o **ID externo da Braze** e exija-o na política de confiança da sua função com uma condição `sts:ExternalId`. Selecione **Gerar novo ID externo** se precisar de um novo valor.
     3. Insira o **ARN da função AWS** para a função IAM que possui permissões do Amazon Bedrock. O ARN deve corresponder a `arn:aws:iam::<account-id>:role/<role-name>`.
     4. Selecione a **região da AWS** onde seus modelos do Bedrock estão hospedados.
     5. Selecione **Salvar**.

{% alert note %}
**Função IAM da AWS** aparece apenas para espaços de trabalho onde essa opção de autenticação está ativada. Com a autenticação por função IAM, a Braze assume sua função para gerar credenciais de curta duração do Amazon Bedrock e não armazena uma chave de API de longo prazo.
{% endalert %}

Após salvar, a Braze exibe um status de conexão com a data e hora da conexão. Você pode selecionar modelos do Amazon Bedrock ao [criar um agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) no Console de Agentes.

{% alert note %}
Nem todos os modelos do Amazon Bedrock estão disponíveis em todas as regiões da AWS. Escolha uma região que suporte os modelos que você pretende usar. Modelos que não estão disponíveis na sua região conectada retornam erros durante a invocação do agente.
{% endalert %}

Para confirmar que a integração está funcionando, acesse o Console de Agentes e crie um agente de teste usando um dos seus modelos do Bedrock. Insira uma instrução como "Me conte uma piada" e execute uma invocação de teste para verificar se o modelo responde conforme esperado.

Para remover a integração, selecione **Desconectar** na página de **integração do Amazon Bedrock**.

Para problemas com sua conta ou credenciais do Amazon Bedrock, entre em contato com o [Suporte da AWS](https://aws.amazon.com/support).