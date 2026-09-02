---
nav_title: Jebbit
article_title: Jebbit
description: "Este artigo de referência descreve a parceria entre a Braze e a Jebbit, uma PaaS que permite passar e-mails e atributos de usuários das suas campanhas da Jebbit como dados de usuários para a Braze em tempo real."
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> A [Jebbit](https://www.jebbit.com/) é uma PaaS que permite criar experiências de engajamento para que os usuários capturem dados primários.

_Esta integração é mantida pela Jebbit._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Jebbit permite passar e-mails e atributos de usuários das suas campanhas da Jebbit como dados de usuários para a Braze em tempo real. Esses dados podem então ser usados para impulsionar iniciativas de marketing, como campanhas de e-mail personalizadas e gatilhos.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta da Jebbit | É necessário ter uma conta da Jebbit para usar essa parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com todas as permissões de dados de usuários. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | Sua URL de endpoint REST or transferir estado representacional. Seu endpoint dependerá da URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Ao solicitar a integração com a Jebbit, avise caso seja necessário cumprir algum prazo rígido. Além disso, confirme se você tem os atributos mapeados nas experiências da Jebbit que gostaria de passar para a Braze.

### Etapa 1: Fornecer credenciais da API or interface de programação do aplicativo (API) {#step-1-provide-api-credentials}

Forneça suas credenciais de API or interface de programação do aplicativo (API) para a Jebbit em um arquivo de texto por meio de uma solicitação de arquivo do Dropbox.
Envie seu arquivo usando a seguinte [URL do Dropbox](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx).

### Etapa 2: Confirmar o envio de teste {#step-2-confirm-test-submission}

Um engenheiro da Jebbit atribuído à sua integração fará o push de um envio de teste da Jebbit para a Braze, para que você possa ver como os dados ficarão no seu ambiente da Braze. Essa é a etapa final da ativação da integração. Agora que seus dados da Jebbit estão configurados, use-os para impulsionar suas iniciativas de marketing.

{% alert note %}
O ID de atributo que você definiu na Jebbit é como o nome do campo de atributo será exibido na Braze.
{% endalert %}

## Personalização {#customization}

Atualmente, oferecemos suporte especificamente aos endpoints de [dados de usuários]({{site.baseurl}}/api/endpoints/user_data/), mas solicitações para diferentes endpoints também podem ser atendidas.

Os nomes dos campos de atributos também podem ser personalizados de acordo com sua preferência.

Se quiser adicionar outros atributos da Jebbit à Braze, mapeie o novo atributo na sua conta da Jebbit. O atributo será exibido automaticamente na Braze à medida que você coletar dados para ele.