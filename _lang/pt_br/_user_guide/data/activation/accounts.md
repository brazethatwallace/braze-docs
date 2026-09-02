---
nav_title: Contas
article_title: Objetos de conta
page_order: 7
page_type: reference
description: "Use objetos de conta para segmentar usuários, personalizar mensagens com dados de conta e gerenciar registros de conta."
---

# Objetos de conta {#account-objects}

> Use objetos de conta para segmentar e personalizar o envio de mensagens com dados de conta.

{% alert important %}
Contas está em acesso antecipado. Estas instruções podem mudar conforme o recurso evolui.
{% endalert %}

Com objetos de conta, você pode:

- Criar segmentos com critérios de conta
- Personalizar mensagens com atributos de conta por meio de Liquid
- Gerenciar registros de conta em um só lugar

Objetos de conta são modelos de dados no nível do espaço de trabalho conectados a perfis de usuário. Um registro de conta é uma conta específica e seus dados de campo associados.
Use objetos de conta quando o contexto da conta, como atributos da empresa, ajuda você a direcionar e personalizar o envio de mensagens.
Você também pode modelar hierarquias de contas (como contas pai e filho) e vincular um perfil de usuário a várias contas.

## Por que usar objetos de conta? {#why-use-account-objects}

Alguns casos de uso exigem contexto no nível da conta, mesmo quando seus Campaigns e Canvas enviam mensagens para usuários individuais.

Os objetos de conta permitem armazenar dados de conta uma única vez e reutilizá-los para segmentação e personalização em toda a Braze.

Isso permite que você:

- Segmente por atributos de conta
- Personalize mensagens com contexto compartilhado da conta (como nome da empresa ou setor)
- Modele relacionamentos entre contas e conecte um perfil de usuário a várias contas

Essa abordagem substitui a necessidade de duplicar os mesmos atributos de conta em vários perfis de usuário.

## Pré-requisitos {#prerequisites}

Antes de começar:

- Seu espaço de trabalho deve estar habilitado para o acesso antecipado de Accounts. Entre em contato com a equipe de conta da Braze.
- Você já deve ter usuários na Braze.
- Após Accounts ser ativado, ele aparece em **Configurações de dados** > **Accounts**. Se esta for a primeira vez que você usa Accounts, siga as instruções de inicialização exibidas na tela.

## Modelo de dados de conta {#account-data-model}

Cada conta requer um ID externo (`id`) e um nome (`name`).

Os campos de conta nesta seção definem o esquema do objeto Account. Esses campos se aplicam a cada registro individual de conta que você armazena na Braze.

A Braze inclui objetos de conta com campos padrão por padrão. Você pode adicionar e remover campos personalizados com base no seu caso de uso.

| Nome do campo | Tipo de campo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| `id` | string | Sim | O ID do sistema para a conta (por exemplo, ID do CRM). Deve ser único no seu espaço de trabalho. |
| `name` | string | Sim | Nome da conta. |
| `type` | string | Não | Tipo de conta, como cliente, parceiro ou revendedor. |
| `annual_revenue` | number | Não | Receita anual da conta. |
| `industry` | string | Não | Setor da conta. |
| `number_of_employees` | number | Não | Número de colaboradores. |
| `address` | string | Não | Endereço. |
| `city` | string | Não | Cidade. |
| `state` | string | Não | Estado ou província. |
| `postal_code` | string | Não | Código postal. |
| `country` | string | Não | País. |
| `notes` | string | Não | Notas adicionais. |
| `website` | string | Não | URL do website. |
| `main_phone` | string | Não | Número de telefone principal. |
| `created_date` | time | Não | Data e hora de criação da conta. |
| `sic_code` | string | Não | Código de Classificação Industrial Padrão. |
| Campos personalizados | custom | Não | Campos que você define e gerencia. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Campos do modelo de dados de conta" }

## Opções de integração de dados {#data-integration-options}

Você pode gerenciar registros de conta por meio de:

- Endpoints da REST API para registros de conta
- Edição no navegador em **Data Settings** > **Accounts** para registros individuais

## Primeiros passos {#get-started}

### Etapa 1: Ativar Accounts {#step-1-enable-accounts}

O Accounts é ativado no nível da empresa. Durante o Acesso Antecipado, sua equipe de conta da Braze cuida da ativação única.

Quando o Accounts estiver ativado, acesse **Configurações de Dados** > **Accounts** e conclua o fluxo de inicialização única, se solicitado.

### Etapa 2: Adicionar registros de conta {#step-2-add-account-records}

Adicione ou atualize registros de conta por meio da REST API ou pela edição no navegador.

### Etapa 3: Criar um filtro calculado para critérios de conta {#step-3-create-a-calculated-filter-for-account-criteria}

Antes de segmentar com base em dados de conta, crie um filtro calculado que defina seus critérios de conta:

1. Acesse **Público** > **Filtros Calculados**.
2. Selecione **Criar filtro** e, em seguida, selecione **Filtros de objeto de dados**.
3. Defina seus critérios de conta.

Para mais detalhes, consulte [Filtros calculados]({{site.baseurl}}/user_guide/audience/segments/calculated_filters#create-a-calculated-filter).

### Etapa 4: Usar o filtro calculado no criador de segmentos {#step-4-use-the-calculated-filter-in-segment-builder}

No criador de segmentos, selecione o filtro calculado que você criou e adicione quaisquer filtros de atributo de usuário adicionais que suportem o direcionamento da sua Campaign ou Canvas.

## Criar segmentos baseados em conta {#build-account-based-segments}

Depois que seus registros de conta e o filtro calculado estiverem prontos:

1. Acesse o [criador de segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Adicione seu filtro calculado pré-configurado para os critérios de conta.
3. Adicione quaisquer filtros de atributo de usuário adicionais.
4. Salve seu Segment.

Por exemplo:

- **Filtro calculado:** `industry` da conta é exatamente `healthcare`
- **Filtro de atributo de usuário:** `days_since_last_login` é menor que `30`

## Personalizar com Liquid {#personalize-with-liquid}

Use a Liquid tag `{% raw %}{% data_object account %}{% endraw %}` para carregar os dados da conta do usuário no array `data_objects`.

{% alert note %}
Ao usar **prévia and Test**, use um Segment que inclua dados de conta para que a personalização seja resolvida corretamente.
{% endalert %}

{% raw %}
```liquid
{% data_object account %}
Hi {{${first_name}}},
We'd love to invite you and your peers at {{ data_objects[0].name }}.
```
{% endraw %}

Para iterar sobre todas as contas correspondentes:

{% raw %}
```liquid
{% data_object account %}
{% for acct in data_objects %}
- {{ acct.name }}
{% endfor %}
```
{% endraw %}

## Conceitos básicos da API {#api-basics}

Você pode usar a REST API para gerenciar registros de conta durante o Acesso Antecipado.

Para detalhes sobre endpoints, consulte [Endpoints de objetos de dados]({{site.baseurl}}/api/endpoints/data_objects).

Para informações sobre autenticação e conceitos básicos de endpoints REST, consulte [Visão geral da API da Braze]({{site.baseurl}}/api/basics).

## Perguntas frequentes {#frequently-asked-questions}

### Posso adicionar campos personalizados a contas? {#can-i-add-custom-fields-to-accounts}

Sim. Você pode definir e gerenciar campos de conta personalizados no seu espaço de trabalho. Para ver os requisitos de campo, consulte [Modelo de dados de conta](#account-data-model).

### Accounts é um complemento pago? {#is-accounts-a-paid-add-on}

Não. Accounts não é um complemento pago e está disponível em todos os planos. Durante o Acesso Antecipado, a equipe de conta da Braze precisa ativá-lo no seu espaço de trabalho.