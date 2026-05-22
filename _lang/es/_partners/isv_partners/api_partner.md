---
nav_title: Integración de socios de API
alias: /api_partner_integration/
hidden: true
---

# Integración de socios de API {#api-partner-integration}

> Conoce los requisitos para las integraciones de API de socios, como la sintaxis de los encabezados `User-Agent`.

{% alert important %}
Anteriormente, los socios debían añadir su nombre al campo de socio en sus solicitudes de API. Este formato ya no es compatible, y ahora se requiere un encabezado `User-Agent`.
{% endalert %}

## Agentes de usuario {#user-agents}

Debes incluir un encabezado `User-Agent` que identifique claramente la fuente del tráfico. Esto permite a nuestros clientes compartidos ver el tráfico de socios en los informes de uso de la API de Braze, y permite a los ingenieros de Braze identificar las integraciones que no siguen las mejores prácticas. En general, solo debes utilizar un único agente de usuario para todo tu tráfico.

### Sintaxis {#syntax}

Tu encabezado `User-Agent` debe ajustarse al siguiente formato (que es similar al estándar [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46)):

```bash
User-Agent: partner-OrganizationName
```

Sustituye lo siguiente:

| Marcador de posición | Descripción |
|-------------|-------------|
| `OrganizationName` | El nombre de tu organización formateado en Pascal case. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sintaxis" }

### Ejemplos {#examples}

Por ejemplo, el siguiente sería un agente de usuario correcto para la Ingesta de datos de Cloud de Snowflake:

```bash
User-Agent: partner-Snowflake
```

Mientras que este sería incorrecto porque no identifica claramente la fuente del tráfico:

```bash
User-Agent: axios/1.4.0
```
