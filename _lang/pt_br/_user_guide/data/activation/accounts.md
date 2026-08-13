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

Alguns casos de uso exigem contexto no nível da conta, mesmo quando suas Campaigns e Canvas enviam para usuários individuais.

Objetos de conta permitem armazenar dados de conta uma vez e reutilizá-los para segmentação e personalização na Braze.

Isso permite que você:

- Segmente por atributos de conta
- Personalize mensagens com contexto de conta compartilhado (como nome da empresa ou setor)
- Modele relacionamentos entre contas e conecte um perfil de usuário a várias contas

Essa abordagem substitui a duplicação dos mesmos atributos de conta em vários perfis de usuário.

## Pré-requisitos {#prerequisites}

Antes de começar:

- Seu espaço de trabalho deve estar habilitado para o acesso antecipado de Contas. Entre em contato com a equipe de conta da Braze.
- Você já deve ter usuários na Braze.
- Depois que Contas for ativado, ele aparecerá em **Configurações de dados** > **Contas**. Se esta for a primeira vez que você usa Contas, siga as instruções de inicialização na tela.

## Modelo de dados de conta {#account-data-model}

Cada conta requer um ID externo (`id`) e um nome (`name`).

Os campos de conta nesta seção definem o esquema do objeto de conta. Esses campos se aplicam a cada registro de conta individual que você armazena na Braze.

A Braze inclui objetos de conta com campos padrão por padrão. Você pode adicionar e remover campos personalizados com base no seu caso de uso.

| Nome do campo | Tipo do campo | Obrigatório | Descrição |
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
- Edição no navegador em **Configurações de dados** > **Contas** para registros individuais

## Primeiros passos {#get-started}

### Etapa 1: Ativar Contas {#step-1-enable-accounts}

Contas é ativado no nível da empresa. Durante o acesso antecipado, a equipe de conta da Braze realiza a ativação única.

Quando Contas estiver ativado, acesse **Configurações de dados** > **Contas** e conclua o fluxo de inicialização única, se solicitado.

### Etapa 2: Adicionar registros de conta {#step-2-add-account-records}

Adicione ou atualize registros de conta por meio da REST API ou da edição no navegador.

### Etapa 3: Criar um filtro calculado para critérios de conta {#step-3-create-a-calculated-filter-for-account-criteria}

Antes de segmentar com base em dados de conta, crie um filtro calculado que defina seus critérios de conta. Para mais detalhes, consulte [Como os filtros calculados funcionam]({{site.baseurl}}/user_guide/audience/segments/calculated_filters#how-it-works).

### Etapa 4: Usar o filtro calculado no criador de segmentos {#step-4-use-the-calculated-filter-in-segment-builder}

No criador de segmentos, selecione o filtro calculado que você criou e adicione quaisquer filtros de atributo de usuário adicionais que suportem o direcionamento da sua Campaign ou Canvas.

## Criar segmentos baseados em conta {#build-account-based-segments}

Depois que seus registros de conta e filtro calculado estiverem prontos:

1. Acesse o [criador de segmentos]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).
2. Adicione seu filtro calculado pré-configurado para critérios de conta.
3. Adicione quaisquer filtros de atributo de usuário adicionais.
4. Salve seu segmento.

Por exemplo:

- **Filtro calculado:** `industry` da conta é exatamente `healthcare`
- **Filtro de atributo de usuário:** `days_since_last_login` é menor que `30`

## Personalizar com Liquid {#personalize-with-liquid}

Use a Liquid tag `{% raw %}{% data_object account %}{% endraw %}` para carregar dados de conta do usuário no array `data_objects`.

{% alert note %}
Ao usar **Prévia e teste**, use um segmento que inclua dados de conta para que a personalização possa ser resolvida corretamente.
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

## Noções básicas da API {#api-basics}

Você pode usar a REST API para gerenciar registros de conta durante o acesso antecipado.

{% alert note %}
Os detalhes dos endpoints para Contas são fornecidos durante a integração do acesso antecipado. Se você precisar de acesso ou detalhes de integração, entre em contato com a equipe de conta da Braze.
{% endalert %}

Para autenticação e noções básicas de endpoints REST, consulte a [Visão geral da API da Braze]({{site.baseurl}}/api/basics).

## Perguntas frequentes {#frequently-asked-questions}

### Posso adicionar campos personalizados às contas? {#can-i-add-custom-fields-to-accounts}

Sim. Você pode definir e gerenciar campos de conta personalizados no seu espaço de trabalho. Para requisitos de campo, consulte [Modelo de dados de conta](#account-data-model).

### Contas é um complemento pago? {#is-accounts-a-paid-add-on}

Não. Contas não é um complemento pago e está disponível em todos os planos. Durante o acesso antecipado, a equipe de conta da Braze deve ativá-lo para o seu espaço de trabalho.