---
nav_title: "Aliases para identificar o objeto"
article_title: Aliases da API or interface de programação do aplicativo (API) para identificar o objeto
page_order: 11
page_type: reference
description: "Este artigo explica os aliases para identificar a especificação de objetos."

---

# Aliases para identificar o objeto {#aliases-to-identify-object}

Uma solicitação de API or interface de programação do aplicativo (API) com qualquer campo no objeto de atributos cria ou atualiza um atributo desse nome com o valor fornecido no perfil de usuário especificado.

Use os nomes de campo do perfil de usuário da Braze (listados a seguir ou qualquer outro listado na seção de [campos de perfil de usuário da Braze]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)) para atualizar esses valores especiais no perfil de usuário no dashboard ou adicionar seus próprios dados de atributo personalizado ao usuário.

## Corpo do objeto {#object-body}

```json
{
  "aliases_to_identify" : (required, array of aliases to identify object)
  [
    {
      "external_id" : (required, string) see External user ID,
      // external_ids for users that do not exist return a non-fatal error.
      // See server responses for details.
      "user_alias" : {
        "alias_name" : (required, string) see User aliases,
        "alias_label" : (required, string) see User aliases
      }
    }
  ]
}
```

- [ID de usuário externo]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [Aliases de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)