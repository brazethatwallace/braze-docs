---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "Este artigo de referência descreve a parceria entre a Braze e a NPAW, uma plataforma inteligente de análise de dados que fornece insights práticos para os principais profissionais de mídia online."
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> A [NPAW](https://nicepeopleatwork.com/), também conhecida como _Nice People at Work_, é uma plataforma inteligente de análise de dados que fornece insights práticos para os principais profissionais de mídia online. Com a suíte de ferramentas YOUBORA da NPAW, os clientes da Braze agora podem aproveitar uma IA preditiva e robusta para entender melhor o comportamento do cliente e impulsionar o engajamento em todas as plataformas.

# Pré-requisitos {#prerequisites}

| Requisito | Origem | Descrição |
| --------------|------|-------------|
| Chave de API YOUBORA | [Configurações do YOUBORA](https://youbora.nicepeopleatwork.com/users/login) | Uma chave de API gerada ao se inscrever e que pode ser localizada em **Configurações** |
| ID | [Configurações da Braze](https://dashboard.braze.com/sign_in) | O YOUBORA oferece as opções de vincular o software à Braze via um ***Braze ID***, um ***ID de usuário externo*** ou um ***ID do usuário*** |
| Endpoint | [Configurações da Braze](https://dashboard.braze.com/sign_in) | Um endpoint de URL totalmente personalizável configurável pelo seu dashboard da Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

# Integração de análise de dados {#analytics-integration}

## Acessando a página de integrações {#accessing-the-integrations-page}

Após fazer login na sua conta da suíte de ferramentas YOUBORA, navegue até a página de integrações selecionando a opção **Integrações** no menu suspenso da conta.

![Menu suspenso da NPAW]({% image_buster /assets/img/npaw_dropdown.png %})

## Configurando sua integração {#configuring-your-integration}

Na página de integração, role para baixo até ver a opção de integração **Braze**. Ao clicar nela, a seção será expandida e exibirá uma série de parâmetros obrigatórios para preencher:

![Integração NPAW]({% image_buster /assets/img/npaw_integration.png %})

Preencha os campos com as informações coletadas na seção de pré-requisitos, em que:
* **Connector Name** é uma string **alfanumérica** que será usada para se referir a esta integração no futuro. Esse valor pode ser definido como qualquer coisa que você quiser, desde que contenha **apenas** letras e números.
* **User ID** é o ID previamente escolhido para vincular seu software YOUBORA à sua conta da Braze. Por exemplo, se você optar por realizar o vínculo via seu **Braze ID**, selecione **Braze ID** no menu suspenso para atribuir o valor ao campo adequado.
* **API Key** é a sua chave de API da suíte de ferramentas YOUBORA encontrada anteriormente na seção **API** em **Settings**.
* **Endpoint** é o endpoint de URL personalizável configurado anteriormente no seu dashboard da Braze.

Depois que todos os campos forem preenchidos, basta clicar no botão **Connect** para estabelecer uma conexão e salvar as alterações feitas.

## Usando sua integração NPAW {#using-your-npaw-integration}

Depois de terminar de configurar sua integração com a Braze, navegue até o produto **Users** e selecione o **Sample Manager** dentro do **Sections Manager**.

Depois de criar uma amostra no **Sample Manager**, você poderá clicar no ícone de três pontos no lado direito para enviar todos os usuários da sua amostra para a Braze.

![Gerenciador de amostras da NPAW]({% image_buster /assets/img/npaw_sample_manager.png %})

Agora, depois de enviar seus usuários para a Braze, você pode agir e focar Campaigns em segmentos de usuários para reengajar usuários inativos, entrar em contato com seus usuários mais leais ou realizar qualquer ação em qualquer segmento de usuário!