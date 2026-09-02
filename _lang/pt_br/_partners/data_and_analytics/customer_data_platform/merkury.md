---
nav_title: Merkury
article_title: Merkury
description: "Este artigo de referência descreve a parceria entre a Braze e a Merkury, uma plataforma de identidade corporativa para seus apps, que permite aproveitar o `MerkuryID` para aumentar as taxas de reconhecimento de visitantes do site para os clientes da Braze."
page_type: partner
search_tag: Partner
---

# Merkury

> A [Merkury](https://merkury.merkleinc.com/) é a plataforma de identidade corporativa da Merkle que ajuda as marcas a maximizar o engajamento, a experiência e a receita do consumidor com recursos de identidade primários sem cookies. O `MerkuryID` unifica os registros de clientes e prospects conhecidos e desconhecidos de uma marca, as visitas ao site/app e os dados do consumidor em um único ID de pessoa persistente.

_Essa integração é mantida pela Merkury._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Merkle permite aproveitar o `MerkuryID` para aumentar as taxas de reconhecimento de visitantes do site para clientes da Braze. Ao reconhecer visitantes que são assinantes de e-mail da marca, o Merkury atualiza o perfil da Braze para incluir o endereço de e-mail do assinante. Os recursos aprimorados de reconhecimento do `MerkuryID` melhoram as oportunidades de engajamento e personalização, além de aumentar imediatamente a quantidade de envios de e-mail de abandono de site e a receita associada.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta Merkle | Uma conta Merkle é necessária para aproveitar esta parceria. |
| ID de cliente Merkle | Obtenha seu ID de cliente com seu representante Merkle. |
| Tag Merkury | Insira a tag Merkury da Merkle no seu website. |
| Endpoint REST or transferir estado representacional e SDK or kit de desenvolvimento de software da Braze | A URL do seu endpoint REST or transferir estado representacional ou SDK or kit de desenvolvimento de software. Seu endpoint dependerá da [URL da Braze para a sua instância]({{site.baseurl}}/api/basics#endpoints). |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as permissões `users.track, users.export.ids, users.export.segment, and segments.list`. <br><br>Ela pode ser criada em **Dashboard da Braze > Console de desenvolvedor > Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional > Criar nova chave de API or interface de programação do aplicativo (API)**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

{% alert important %}
As solicitações do conector de identidade Merkury para a Braze operam dentro das especificações de limite de frequência da API or interface de programação do aplicativo (API) da Braze. Entre em contato com a Braze ou com seu gestor de conta Merkle se tiver alguma dúvida.<br><br>O Merkury envia pelo menos uma solicitação ao final de uma sessão qualificada.
{% endalert %}

## Integração SDK or kit de desenvolvimento de software lado a lado {#side-by-side-sdk-integration}

Utiliza a tag Merkury do lado do cliente da Merkle para capturar dispositivos da Braze e encaminhá-los ao endpoint do conector de identidade Merkury para identificação.

### Etapa 1: Configurar a tag do SDK or kit de desenvolvimento de software web da Braze {#step-1-setup-braze-web-sdk-tag}

Você precisa ter o [SDK or kit de desenvolvimento de software web da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-gtm) implantado no seu website para usar esta integração.

### Etapa 2: Implantar a tag Merkury da Merkle {#step-2-deploy-merkles-merkury-tag}

Implante a tag Merkury no seu website para disponibilizar o conector de identidade Merkury. Seu gerente de conta da Merkle fornecerá um guia detalhado com instruções.

### Etapa 3: Criar atributos personalizados {#step-3-create-custom-attributes}

O conector de identidade Merkury preenche os campos a seguir, que você deve criar na Braze como [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes).

| Nome do atributo | Tipo de dados | Descrição |
| --- | --- | --- |
| `hmid` | String | ID Merkury da Merkle |
| `confidence_score` | Número | Nível de confiança da identificação feita pelo Merkury (1-8, menor é melhor) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 3: Criar atributos personalizados" }

### Etapa 4: Fornecer à Merkle o universo de e-mails dos usuários {#step-4-provide-merkle-with-user-email-universe}

A Merkle recomenda uma exportação de segmentação do seu universo de e-mails permitidos. Isso pode ser complementado com exportações diárias de usuários ativos permitidos.

Os seguintes campos são obrigatórios:

- `braze_id`
- `external_id`
- endereço de e-mail

Consulte seu representante da Braze para mais informações.