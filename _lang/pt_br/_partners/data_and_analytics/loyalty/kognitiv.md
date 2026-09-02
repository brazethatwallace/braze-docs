---
nav_title: Kognitiv Inspire
article_title: Kognitiv Inspire
description: "O Kognitiv Inspire é um sistema de tecnologia de fidelidade que permite implementar e avaliar sua estratégia de fidelidade, oferecendo recursos inovadores e comunicações personalizadas com os membros para aumentar a eficácia do programa."
alias: /partners/kognitiv/
page_type: partner
search_tag: Partner
---

# Kognitiv Inspire

> O [Kognitiv Inspire](http://kognitiv.com) é um sistema de tecnologia de fidelidade que ajuda a desbloquear experiências inigualáveis do cliente por meio de programas de fidelidade orientados por resultados que ampliam o engajamento do cliente, aumentam os gastos e celebram o comportamento leal.

_Essa integração é mantida pelo Kognitiv Inspire._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Kognitiv permite que você implemente e avalie sua estratégia de fidelidade, oferecendo recursos inovadores e comunicações personalizadas com os membros para aumentar a eficácia do programa.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Kognitiv | É necessário ter uma conta [Kognitiv](http://kognitiv.com) para aproveitar essa parceria. |
| Chave de API do Kognitiv | Uma chave da API REST do Kognitiv. Ela pode ser criada na página **API Security Tokens**. |
| Endpoint REST da Braze | Sua URL de endpoint REST. Seu endpoint dependerá da URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

- **Inscrição personalizada em programas de fidelidade**: Impulsione seus membros em sua jornada de fidelidade com uma inscrição perfeita no programa e uma notificação de boas-vindas personalizada entregue por meio do canal preferido deles.
- **Emissão de recompensas e notificação de engajamento**: Mantenha viva a centelha da fidelidade emitindo recompensas e notificações que comemorem os marcos de cada membro.
- **Classificação e segmentação estratégica de membros**: Ative um engajamento mais personalizado, classificando e segmentando os membros com base em gastos, engajamento e regras de negócios simples ou complexas, adaptadas às necessidades específicas da sua marca.
- **Notificação de elegibilidade para promoção em tempo real**: Faça com que cada membro se sinta especial com notificações instantâneas sobre sua elegibilidade para promoções exclusivas.

## Integração {#integration}

Use os webhooks do Kognitiv para enviar solicitações à Braze quando ocorrerem eventos de fidelidade. Os exemplos a seguir ilustram como usar o Kognitiv e a Braze para emitir uma recompensa, registrar um usuário do Kognitiv na Braze e enviar a ele um e-mail de boas-vindas.

{% raw %}
### Emissão de recompensa pela Braze {#braze-issue-reward}

O exemplo do Kognitiv a seguir emite uma recompensa para um membro. O Kognitiv Inspire comunicará esse evento de emissão de recompensa à Braze como um evento personalizado por meio de webhooks. Para enviar um e-mail de acompanhamento comunicando a recompensa, crie uma Campaign ou um Canvas que dispare com base nesse evento personalizado.

**URL do webhook**: `<braze-api-rest-endpoint>`
**Corpo da solicitação**: `Raw Text`

- **Método HTTP**: POST
- **Cabeçalhos da solicitação**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Corpo da solicitação {#request-body}

```json
{
  "events" : [
    {
    "external_id" : "{{memberId}}",
    "app_id" : "93ec5a59-3752-4a45-8559-55b61209ba38",
    "name" : "rewards_issued",
    "time" : "{{issuedDate}}",
    "issued_date" : "{{issuedDate}}",
    "issued_location_name" : "{{issuedLocationName}}",
    "reward_type" : "{{rewardType}}"
    }
  ]
}
```

### Criar um usuário e enviar um e-mail de boas-vindas {#create-a-user-and-send-a-welcome-email}

O exemplo do Kognitiv a seguir cria um novo usuário na Braze quando ele se inscreve no KLS. Para agendar um e-mail de boas-vindas para esse usuário, crie uma Campaign ou um Canvas na Braze que dispare com base em atributos personalizados específicos.

**URL do webhook**: `<braze-api-rest-endpoint>` <br>
**Corpo da solicitação**: `Raw Text`

- **Método HTTP**: POST
- **Cabeçalhos da solicitação**:
  - **Authorization**: Bearer `<Kognitiv-api-key>`
  - **Content-Type** application/json

#### Corpo da solicitação

```json
{
  "attributes": [
    {
      "app_id": "93ec5a59-3752-4a45-855b6109ba38",
      "bio": "Software Architect",
      "country": "{{memberAddressCO}}",
      "email": "{{memberEmail}}",
      "email_subscribe": "opted_in",
      "external_id": "{{memberId}}",
      "first_name": "{{memberFirstName}}",
      "home_city": "{{memberAddressCity}}",
      "time_zone": "America/Chicago",
      "total_points_balance": "{{memberPointsAvailable}}",
      "CreatedKLS": "{{issuedTimestamp}}",
      "email_contact_allowed" : "{{memberEmailContactAllowed}}",
      "sms_contact_allowed" : "{{memberSmsContactAllowed}}",
      "date_joined": "{{issuedDate}}"
    }
  ]
}
```
{% endraw %}

## Documentação e recursos de integração do Kognitiv Inspire {#kognitiv-inspire-documentation-and-integration-features}

Depois de integrar a Braze ao Kognitiv Inspire, o Kognitiv permite que você acesse seu amplo portfólio de APIs, recursos de webhook de ponta e funcionalidades robustas de importação e exportação de dados para uma transferência em massa perfeita. Para saber mais sobre os recursos do Kognitiv Inspire e as funcionalidades de integração, consulte o [guia de recursos](https://info.kognitivloyalty.com) do Kognitiv ou entre em contato com a empresa para obter uma demonstração guiada.

### Endpoints

**Autorização da REST API**
- Região dos EUA: `https://app.kognitivloyalty.com/Auth/connect/token`
- Região CA/EMEA: `https://ca.kognitivloyalty.com/Auth/connect/token`
- Região APAC: `https://aus.kognitivloyalty.com/Auth/connect/token`

**REST API (URL base)**
- Região dos EUA: `https://app.kognitivloyalty.com/api`
- Região CA/EMEA: `https://ca.kognitivloyalty.com/api`
- Região APAC: `https://aus.kognitivloyalty.com/api`

**Endpoints de serviços web (URL base)**
- Região dos EUA: `https://app.kognitivloyalty.com/WS`
- Região CA/EMEA: `https://ca.kognitivloyalty.com/WS`
- Região APAC: `https://aus.kognitivloyalty.com/WS`

Para saber mais sobre como configurar tokens de acesso e endpoints SFTP, entre em contato com o Kognitiv para obter uma demonstração.