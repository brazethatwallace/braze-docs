---
nav_title: GRAVTY®
article_title: Plataforma de fidelidade GRAVTY®
description: "Este artigo descreve a parceria entre a Braze e a GRAVTY®, uma plataforma de fidelidade de nível empresarial que permite às marcas projetar, gerenciar e escalar programas de fidelidade orientados por dados para aumentar o engajamento e a retenção de clientes."
alias: /partners/lji/
page_type: partner
search_tag: Partner
---

# Plataforma de fidelidade GRAVTY® {#gravty-loyalty-platform}

> A [GRAVTY®](https://www.lji.io/) é uma plataforma de fidelidade de nível empresarial da Loyalty Juggernaut Inc. (LJI) que permite a marcas de varejo, viagens, restaurantes (incluindo redes de fast-food) e serviços financeiros projetar, gerenciar e escalar programas de próxima geração — impulsionando crescimento mensurável em engajamento, retenção e lifetime value do cliente por meio de experiências personalizadas e orientadas por dados.

Construída sobre uma arquitetura flexível e API-first, a GRAVTY® oferece suporte a acúmulo e resgate em tempo real, gerenciamento de ecossistema de parceiros e integração entre canais. As equipes podem lançar mais rápido, iterar nos programas e entregar experiências de fidelidade em escala.

_Esta integração é mantida pela LJI._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a GRAVTY® conecta dados de fidelidade e gatilhos de envio de mensagens entre as duas plataformas. A GRAVTY® envia dados de usuários para a Braze como atributos, eventos e compras. A Braze armazena esses dados e entrega mensagens em canais como SMS, e-mail e notificações por push. Você usa os dados sincronizados para segmentação, personalização e gatilhos.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa do seguinte:

| Requisito | Descrição |
| :--- | :--- |
| Conta GRAVTY® | Uma conta GRAVTY® com permissão para configurar integrações e gerenciar inscrições de eventos. |
| Conta Braze | Uma conta Braze ativa com acesso à API ativado. |
| Chave da API REST da Braze | Uma chave da API REST com as permissões `campaigns.trigger.send`, `canvas.trigger.send` e `users.track`.<br><br> Crie essa chave no dashboard da Braze em **Settings** > **API Keys**. |
| Endpoint da API da Braze | Seu endpoint REST da Braze (por exemplo, `https://rest.fra-01.braze.eu`). Para saber mais, consulte [Instâncias e endpoints da Braze]({{site.baseurl}}/api/basics/#endpoints). |
| IDs de Campaign ou Canvas | IDs dos fluxos de trabalho de **Campaigns** ou **Canvas** que você aciona a partir da GRAVTY®. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Casos de uso {#use-cases}

Esta integração oferece suporte às seguintes funcionalidades da Braze:

- **Sincronização de dados de usuários (`/users/track`):** Sincronize atributos de membros, eventos e compras com a Braze para segmentação e personalização.
- **Acionamento de Campaigns (`/campaigns/trigger/send`):** Acione mensagens únicas ou transacionais usando Campaigns da Braze.
- **Acionamento de Canvas (`/canvas/trigger/send`):** Inicie jornadas de múltiplas etapas e envio de mensagens de ciclo de vida usando **Canvas** da Braze.
- **Segmentação e personalização:** Crie públicos segmentados e entregue comunicações personalizadas a partir dos dados sincronizados.

## Integração {#integration}

A integração entre a GRAVTY® e a Braze é baseada em API. Ela oferece suporte à sincronização de dados em tempo real e ao acionamento de comunicações.

![Diagrama de fluxo mostrando a GRAVTY® enviando dados e gatilhos para as APIs da Braze, que então envia mensagens para SMS, e-mail, push e WhatsApp.]({% image_buster /assets/img/lji/braze-gravty-integration.png %})

### Etapa 1: Conectar a Braze com a GRAVTY® {#step-1-connect-braze-with-gravty}

1. Acesse **Subscriber Setup** na GRAVTY® para gerenciar integrações externas.
2. Selecione **Add New Subscriber**.
3. Selecione **Braze** como o provedor de integração.
4. Insira o seguinte:
   * **API URL** (seu endpoint REST da Braze)
   * **API Key** (sua chave da API REST da Braze)
5. Salve a configuração e confirme que a conexão está ativa.

![Formulário Add Subscriber da GRAVTY® com Braze selecionado, campos de API URL e API key, e um botão de ativação do subscriber.]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### Etapa 2: Configurar o mapeamento de atributos do modelo {#step-2-configure-template-attribute-mapping}

Depois de salvar o subscriber da Braze, a GRAVTY® abre a página **Template Attribute Mapping**. Use-a para mapear campos para a Braze.

1. Selecione **Add New Field**.
2. Selecione um **atributo da GRAVTY®** na lista.
3. Insira o **nome do atributo na Braze** (atributo personalizado) onde o valor deve aparecer na Braze.

{% alert important %}
Você não precisa mapear o `external_id`. A GRAVTY® o gera internamente aplicando hash no ID do membro, e a Braze recebe esse valor com hash como `external_id` no perfil de usuário.<br><br> Antes de ativar a integração, confirme que isso corresponde à forma como você define o `external_id` na Braze atualmente. Se a Braze já usa um `external_id` diferente para as mesmas pessoas, trabalhe com a LJI para alinhar os identificadores antes de sincronizar os dados.
{% endalert %}

{: start="4"}
4. Repita as etapas 1 a 3 para adicionar mais mapeamentos.
5. Selecione **Save**.

![Página Subscription Setup da GRAVTY® com configuração de modelo, configuração de sincronização e uma tabela mapeando entidade, atributo da GRAVTY® e campos de atributo do modelo para a Braze.]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
A integração oferece suporte aos tipos de dados de atributos personalizados da Braze, incluindo números (inteiro, float), strings, arrays, booleanos, objetos, arrays de objetos e datas.
{% endalert %}

### Etapa 3: Testar a integração {#step-3-test-the-integration}

Acione um evento de teste na GRAVTY® para confirmar a sincronização, os gatilhos de comunicação e o fluxo de ponta a ponta.

![Visão geral do perfil de usuário na Braze mostrando Perfil, Atributos personalizados (nível, datas, país, cidade) e Eventos personalizados preenchidos a partir do mapeamento da GRAVTY®.]({% image_buster /assets/img/lji/braze-member-profile.png %})

## Suporte {#support}

Para suporte com a integração ou solução de problemas, entre em contato com a LJI em [support@lji.io](mailto:support@lji.io).