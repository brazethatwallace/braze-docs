---
nav_title: "Objeto de alias de usuário"
article_title: Objeto de alias de usuário da API
page_order: 11
page_type: reference
description: "Este artigo de referência explica os diferentes componentes do objeto de alias de usuário."

---

# Objeto de alias de usuário {#user-alias-object}

> Um alias serve como um identificador de usuário exclusivo alternativo. Usando um objeto de alias de usuário, é possível definir um identificador consistente para análise de dados que seguirá um determinado usuário antes e depois do registro em um app móvel ou site. Você também pode usar este objeto para adicionar os identificadores usados por um fornecedor terceirizado aos usuários da sua empresa para reconciliar seus dados externamente de forma mais fácil.

O objeto de alias de usuário consiste em duas partes: um `alias_name` para o próprio identificador e um `alias_label` indicando o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.

Esse objeto é usado com frequência em todos os nossos endpoints e, muitas vezes, em outros objetos.

## Corpo do objeto {#object-body}

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

| Campo | Tipo de dados | Exemplo | Descrição |
|---|---|---|---|
| `alias_name` | String | `john_doe_123` | Um identificador exclusivo para o usuário, como um ID de um sistema de terceiros. Esse valor não pode estar vazio e deve ter 236 bytes ou menos. |
| `alias_label` | String | `crm_id` | Uma string personalizada não vazia que define o tipo de alias. Esse valor não é limitado a opções específicas. Você pode usar qualquer rótulo significativo, como `email_id`, `amplitude_id`, `salesforce_lead_id` ou outro valor que corresponda ao seu caso de uso. Esse valor deve ter 236 bytes ou menos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }

### Exemplo {#example}

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "crm_id"
  },
  "external_id": "user_456"
}
```

Neste exemplo, `crm_id` é um rótulo personalizado indicando que o alias representa um identificador de sistema CRM.

### Exemplo adicional {#additional-example}

```json
{
  "user_alias": {
    "alias_name": "a9f3c102",
    "alias_label": "amplitude_id"
  }
}
```

Neste exemplo, `amplitude_id` é um valor de rótulo possível. Você também pode usar rótulos como `email_id` ou `salesforce_lead_id`, ou outro rótulo personalizado que se encaixe no seu esquema de identificadores.