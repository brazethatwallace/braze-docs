---
nav_title: "Objeto alias de usuario"
article_title: Objeto de alias de usuario de API
page_order: 11
page_type: reference
description: "Este artículo de referencia explica los distintos componentes del objeto alias de usuario."

---

# Objeto alias de usuario {#user-alias-object}

> Un alias sirve como identificador único alternativo del usuario. Al utilizar un objeto alias de usuario, puedes establecer un identificador coherente para los análisis que seguirá a un usuario determinado tanto antes como después de que haya iniciado sesión en una aplicación móvil o sitio web. También puedes utilizar este objeto para añadir los identificadores utilizados por un proveedor externo a los usuarios de tu empresa, con el fin de conciliar más fácilmente tus datos externamente.

El objeto alias de usuario consta de dos partes: un `alias_name` para el propio identificador, y un `alias_label` que indica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.

Este objeto se utiliza con frecuencia en todos nuestros puntos de conexión, y a menudo dentro de otros objetos.

## Cuerpo del objeto {#object-body}

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

| Campo | Tipo de datos | Ejemplo | Descripción |
|---|---|---|---|
| `alias_name` | Cadena | `john_doe_123` | Un identificador único para el usuario, como un ID de un sistema de terceros. Este valor no debe estar vacío y debe tener 236 bytes o menos. |
| `alias_label` | Cadena | `crm_id` | Una cadena personalizada no vacía que define el tipo de alias. Este valor no está limitado a opciones específicas. Puedes utilizar cualquier etiqueta significativa, como `email_id`, `amplitude_id`, `salesforce_lead_id` u otro valor que se ajuste a tu caso de uso. Este valor debe tener 236 bytes o menos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }

### Ejemplo {#example}

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "crm_id"
  },
  "external_id": "user_456"
}
```

En este ejemplo, `crm_id` es una etiqueta personalizada que indica que el alias representa un identificador de un sistema CRM or administración de las relaciones con el cliente.

### Ejemplo adicional {#additional-example}

```json
{
  "user_alias": {
    "alias_name": "a9f3c102",
    "alias_label": "amplitude_id"
  }
}
```

En este ejemplo, `amplitude_id` es un posible valor de etiqueta. También puedes utilizar etiquetas como `email_id` o `salesforce_lead_id`, u otra etiqueta personalizada que se ajuste a tu esquema de identificadores.