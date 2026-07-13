---
nav_title: Conectar fontes de dados
article_title: Conectar fontes de dados
page_order: 1
description: "Saiba como o BrazeAI Decisioning Studio Go se conecta aos seus dados de cliente através da sua plataforma de engajamento com clientes."
---

# Conectar fontes de dados {#connect-data-sources}

> O BrazeAI Decisioning Studio™ Go se conecta aos seus dados de cliente através da sua plataforma de engajamento com clientes (CEP). Este artigo explica quais dados são utilizados e como a conexão funciona.

## Como o Go acessa os dados de cliente {#how-go-accesses-customer-data}

Diferente do Decisioning Studio Pro, que suporta integrações diretas de dados com várias fontes, o Decisioning Studio Go acessa os dados de cliente através da sua CEP. Isso significa:

- **Os dados do público** são extraídos diretamente de segmentos ou listas definidos na sua CEP (Braze ou Salesforce Marketing Cloud) e podem incluir apenas certos atributos predefinidos (não dados 1P)
- **Os dados de engajamento** (aberturas, cliques, envios) são capturados através de consultas automatizadas ou integrações nativas com a sua CEP
- **Nenhuma configuração adicional de pipeline de dados** é necessária além do que você configura na sua CEP

## Padrões de integração suportados {#supported-integration-patterns}

O Decisioning Studio Go suporta as seguintes CEPs para acesso a dados:

| CEP | Fonte de público | Dados de engajamento |
|-----|-----------------|-----------------|
| **Braze** | Segments | Exportação do Braze Currents |
| **Salesforce Marketing Cloud** | Extensões de dados | Automação de consulta SQL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Padrões de integração suportados" }

## Requisitos de dados por CEP {#data-requirements-by-cep}

{% tabs %}
{% tab Braze %}

### Requisitos de dados da Braze {#braze-data-requirements}

Para integrações da Braze, o Decisioning Studio Go requer:

1. **Braze Currents:** você deve ter o Braze Currents ativado e configurado para exportar dados de engajamento para o Decisioning Studio Go. Isso permite que o agente aprenda com as respostas dos clientes.

2. **Acesso a Segments:** a chave de API que você criar deve ter permissões para acessar os Segments que definem seu público-alvo.

3. **Dados do perfil de usuário:** quaisquer atributos de perfil de usuário ou atributos personalizados que você deseja que o agente considere devem ser acessíveis através da API da Braze.

{% alert important %}
Certifique-se de que sua exportação do Braze Currents inclua dados de quaisquer Campaigns que você deseja comparar (incluindo Campaigns BAU).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### Requisitos de dados do SFMC {#sfmc-data-requirements}

Para integrações do Salesforce Marketing Cloud, o Decisioning Studio Go requer:

1. **Data Extensions:** seu público deve ser definido em uma Data Extension que o Decisioning Studio Go possa acessar. Use o SubscriberKey como o identificador principal do usuário.
2. **Acesso a eventos de rastreamento:** desde que o pacote de aplicativo instalado suporte configuração automatizada de ponta a ponta, nenhuma configuração adicional é necessária.

As extensões de dados e consultas de SQL são configuradas como parte da [configuração de orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration).

{% endtab %}
{% endtabs %}

## Melhores práticas {#best-practices}

- **Mantenha os dados atualizados:** certifique-se de que seus segmentos de público e dados de cliente sejam atualizados regularmente (no mínimo, diariamente) para que o agente trabalhe com informações atuais.
- **Inclua atributos relevantes:** pense em quais características do cliente podem influenciar quais mensagens têm mais impacto: dados demográficos, histórico de engajamento, comportamento de compra e estágio do ciclo de vida são todos sinais valiosos.

## Próximos passos {#next-steps}

Agora que você entende como o Go se conecta aos dados, prossiga para configurar sua integração com a CEP:

- [Configurar orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration)