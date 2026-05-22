---
nav_title: Merkury
article_title: Merkury
description: "Este artigo de referência descreve a parceria entre a Braze e a Merkury, uma plataforma de identidade corporativa para seus apps, que permite que você aproveite o `MerkuryID` para aumentar as taxas de reconhecimento de visitantes do site para os clientes da Braze."
page_type: partner
search_tag: Partner

---

# Merkury

> A [Merkury](https://merkury.merkleinc.com/) é a plataforma de identidade corporativa da Merkle que ajuda as marcas a maximizar o engajamento, a experiência e a receita do consumidor com recursos de identidade primários sem cookies. O `MerkuryID` unifica os registros de clientes e prospects conhecidos e desconhecidos de uma marca, as visitas ao site/app e os dados do consumidor em um único ID de pessoa persistente.

_Essa integração é mantida pela Merkury._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Merkury permite que você aproveite o `MerkuryID` para aumentar as taxas de reconhecimento de visitantes do site para os clientes da Braze. Ao reconhecer visitantes que são assinantes de e-mail da marca, a Merkury atualiza o perfil da Braze para incluir o endereço de e-mail dos assinantes. Os recursos de reconhecimento aprimorados do `MerkuryID` melhoram as oportunidades de engajamento e personalização e aumentam imediatamente as quantidades de envio de e-mail de abandono de site e a receita associada.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta da Merkle | É necessário ter uma conta da Merkle para usar essa parceria. |
| ID do cliente da Merkle | Obtenha seu ID de cliente com um representante da Merkle. |
| Tag da Merkury | Coloque a tag da Merkury da Merkle no seu site. |
| Endpoint da Braze REST e do SDK | Seu URL do endpoint REST ou SDK. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints). |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Isso pode ser criado em **Braze Dashboard > Console de desenvolvedor > Chave da API REST > Criar nova chave de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% alert important %}
As solicitações do conector de identidade da Merkury para a Braze operam dentro das especificações do limite de taxa da API da Braze. Entre em contato com a Braze ou com seu gerente de conta da Merkle se tiver alguma dúvida.<br><br>A Merkury envia pelo menos uma solicitação ao final de uma sessão qualificada.
{% endalert %}

## Integração lado a lado de SDK {#side-by-side-sdk-integration}

Usa a tag Merkury do lado do cliente da Merkle para capturar dispositivos Braze e os encaminha para o endpoint do conector de identidade Merkury para identificação.

### Etapa 1: configure a tag do SDK para Web da Braze {#step-1-setup-braze-web-sdk-tag}

Você deve ter o [Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) implantado em seu site para usar essa integração.

### Etapa 2: implante a tag da Merkury da Merkle {#step-2-deploy-merkles-merkury-tag}

Implemente a tag Merkury em seu site para tornar o conector de identidade Merkury disponível em seu site. Seu gerente de conta da Merkle fornecerá um guia detalhado com instruções.

### Etapa 3: crie atributos personalizados {#step-3-create-custom-attributes}

O conector de identidade Merkury preenche os seguintes campos, que você deve criar na Braze como [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes).

| Nome do atributo | Tipo de dados | Descrição |
| --- | --- | --- |
| `hmid` | String | ID da Merkury da Merkle |
| `confidence_score` | Número | Nível de confiança da identificação da Merkury (de 1 a 8; quanto menor, melhor) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 3: crie atributos personalizados" }

### Etapa 4: forneça à Merkle o universo de e-mail do usuário {#step-4-provide-merkle-with-user-email-universe}

A Merkle recomenda uma exportação de segmentação do seu universo de e-mails permitidos. Isso pode ser acompanhado por exportações diárias de usuários ativos permitidos.

Os campos a seguir são obrigatórios:

- `braze_id`
- `external_id`
- endereço de e-mail

Consulte seu representante da Braze para obter mais informações.