---
nav_title: Integração com parceiros da API or interface de programação do aplicativo (API)
alias: /api_partner_integration/
hidden: true
---

# Integração com parceiros da API or interface de programação do aplicativo (API) {#api-partner-integration}

> Saiba mais sobre os requisitos para integrações com parceiros de API or interface de programação do aplicativo (API), como a sintaxe dos cabeçalhos `User-Agent`.

{% alert important %}
Anteriormente, os parceiros eram obrigados a adicionar seu nome ao campo de parceiro em suas solicitações de API or interface de programação do aplicativo (API). Essa formatação não é mais suportada, e agora é necessário um cabeçalho `User-Agent`.
{% endalert %}

## Agentes de usuário {#user-agents}

Você deve incluir um cabeçalho `User-Agent` que identifique claramente a origem do tráfego. Isso permite que nossos clientes compartilhados vejam o tráfego de parceiros nos relatórios de uso da API or interface de programação do aplicativo (API) da Braze, e permite que os engenheiros da Braze identifiquem integrações que não estão seguindo as práticas recomendadas. Em geral, você deve usar apenas um único agente de usuário para todo o seu tráfego.

### Sintaxe {#syntax}

Seu cabeçalho `User-Agent` deve obedecer ao seguinte formato (que é semelhante ao padrão [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231#page-46)):

```bash
User-Agent: partner-OrganizationName
```

Substitua o seguinte:

| Espaço reservado | Descrição |
|-------------|-------------|
| `OrganizationName` | O nome da sua organização formatado em Pascal case. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Syntax" }

### Exemplos {#examples}

Por exemplo, o seguinte seria um agente de usuário correto para a Ingestão de dados na nuvem do Snowflake:

```bash
User-Agent: partner-Snowflake
```

Já o exemplo abaixo seria incorreto porque não identifica claramente a origem do tráfego:

```bash
User-Agent: axios/1.4.0
```
