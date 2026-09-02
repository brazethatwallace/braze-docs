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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Esta integração oferece suporte às seguintes funcionalidades da Braze:

- **Sincronização de dados de usuários (`/users/track`):** Sincronize atributos de membros, eventos e compras com a Braze para segmentação e personalização.
- **Acionamento de Campaigns (`/campaigns/trigger/send`):** Acione mensagens únicas ou transacionais usando Campaigns da Braze.
- **Acionamento de Canvas (`/canvas/trigger/send`):** Inicie jornadas de múltiplas etapas e envio de mensagens de ciclo de vida usando **Canvas** da Braze.
- **Segmentação e personalização:** Crie públicos segmentados e entregue comunicações personalizadas a partir dos dados sincronizados.

## Integração {#integration}

A integração entre a GRAVTY® e a Braze é baseada em API, permitindo sincronização de dados em tempo real e acionamento de comunicações entre a GRAVTY® e a Braze.

### Etapa 1: Conectar a Braze com a GRAVTY® {#step-1-connect-braze-with-gravty}

1. Acesse **Subscriber Setup** na GRAVTY® para gerenciar integrações externas.
2. Selecione **Add New Subscriber**.
3. Selecione **Braze** como o provedor de integração.
4. Insira o seguinte:
   * **API URL** (seu endpoint REST da Braze)
   * **API Key** (sua chave da API REST da Braze)
5. Salve a configuração e confirme que a conexão está ativa.

![Formulário Add Subscriber da GRAVTY® com Braze selecionado, campos de API URL e API key, e um botão de ativação do subscriber.]({% image_buster /assets/img/lji/braze-subscriber-setup.png %}){: style="max-width:70%;"}

### Etapa 2: Configurar o gatilho de evento {#step-2-configure-event-trigger}

Crie um evento na GRAVTY® que é executado quando a atividade de um membro atende às condições que você definir (por exemplo, uma transação, pontos acumulados, mudança de nível ou inscrição no programa).

1. Navegue até a seção **Events** na GRAVTY®.
2. Clique em **Create Event**.
3. Defina as condições do evento (por exemplo, transação criada, pontos acumulados ou upgrade de nível).
4. Configure as regras que determinam quando o evento deve ser acionado.
5. Vincule o subscriber da Braze ao evento para ativar os gatilhos de comunicação.
6. Salve a configuração do evento.

A seguir, um exemplo de evento configurado para ser acionado quando um membro é inscrito no programa:

![Configuração de evento na GRAVTY® para inscrição de membro no programa, com a Braze vinculada como subscriber.]({% image_buster /assets/img/lji/event-configuration.png %})

### Etapa 3: Configurar o mapeamento de atributos do modelo {#step-3-configure-template-attribute-mapping}

Após configurar o evento, conclua a configuração do subscriber para ativar a sincronização de dados e os gatilhos de comunicação:

1. Selecione o **subscriber da Braze** criado na Etapa 1 no menu suspenso de subscribers.
2. Escolha o **canal** apropriado (**Campaign** ou **Canvas**) com base no seu caso de uso. Para cenários apenas de sincronização de dados, o canal pode ser deixado sem seleção.
3. Insira o **Campaign ID** ou **Canvas ID** correspondente no campo **Template Name**, conforme aplicável.
4. Configure o tipo de comunicação para suportar sincronização e/ou envio de mensagens baseado em gatilhos.

Para configurar o mapeamento de campos na GRAVTY®:

1. Clique em **Add New Field**.
2. Selecione o **atributo da GRAVTY®** no menu suspenso.
3. Insira o **nome do atributo na Braze** correspondente onde os dados devem ser mapeados.

{% alert important %}
Você não precisa mapear o `external_id`. A GRAVTY® o gera internamente aplicando hash no ID do membro (o identificador único do membro na GRAVTY®), e a Braze recebe esse valor com hash como `external_id` no perfil de usuário.<br><br> Antes de ativar a integração, confirme que isso corresponde à forma como você define o `external_id` na Braze atualmente. Se a Braze já usa um `external_id` diferente para as mesmas pessoas, trabalhe com a LJI para alinhar os identificadores antes de sincronizar os dados.
{% endalert %}

{: start="4"}
4. Repita as etapas **1 a 3** para adicionar mapeamentos adicionais conforme necessário.
5. Clique em **Save** para aplicar a configuração.

![Configuração de mapeamento de atributos para sincronização de membros com a Braze.]({% image_buster /assets/img/lji/gravty-attribute-mapping.png %})

{% alert note %}
A integração oferece suporte a todos os tipos de dados de atributos personalizados da Braze, incluindo números (inteiro, float), strings, arrays, booleanos, objetos, arrays de objetos e datas.
{% endalert %}

### Etapa 4: Testar a integração {#step-4-test-the-integration}

Acione um evento de teste na GRAVTY® para verificar se a sincronização, os gatilhos de comunicação e a integração como um todo estão funcionando conforme esperado.

* Os dados do membro são sincronizados com a Braze e refletidos no perfil do membro.

![Os campos de dados são preenchidos com base no mapeamento de campos configurado.]({% image_buster /assets/img/lji/braze-member-profile.png %})

* A comunicação é acionada com base na Campaign ou no Canvas configurado.

![Exemplo de e-mail acionado a partir da Braze.]({% image_buster /assets/img/lji/braze-email-example.png %})

## Suporte {#support}

Para suporte com a integração ou solução de problemas, entre em contato com a LJI em [support@lji.io](mailto:support@lji.io).