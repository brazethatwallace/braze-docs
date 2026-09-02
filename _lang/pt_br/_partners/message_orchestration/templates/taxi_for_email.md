---
nav_title: Taxi for Email
article_title: Taxi for Email
alias: /partners/taxi_for_email
description: "Este artigo de referência descreve a parceria entre a Braze e o Taxi for Email, uma ferramenta de marketing de e-mail on-line que permite que os clientes da Braze criem modelos de e-mail inteligentes usando sua interface de arrastar e soltar e uma sintaxe simples, porém poderosa."
page_type: partner
search_tag: Partner

---

# Taxi for Email

> O [Taxi for Email](http://taxiforemail.com/) é uma ferramenta de marketing por e-mail on-line que oferece um editor visual de e-mail intuitivo do tipo arrastar e soltar. O Taxi incentiva as equipes a colaborar facilmente em campanhas de e-mail, permitindo que redatores e editores tenham o acesso e os recursos necessários para criar e-mails, tudo sem código.

_Essa integração é mantida pelo Taxi for Email._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Taxi usa a sintaxe simples e poderosa do Taxi para criar e exportar modelos de e-mail inteligentes para a Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ------------| ----------- |
| Conta do Taxi for Email | É necessário ter uma conta do Taxi for Email para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões completas de **Templates**. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint da Braze | [Seu endpoint da Braze]({{site.baseurl}}/api/basics/#endpoints) está alinhado com a URL do dashboard da Braze.<br><br> Por exemplo, se a URL do dashboard for `https://dashboard-03.braze.com`, seu endpoint será `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Crie um modelo de e-mail no Taxi {#step-1-create-a-taxi-email-template}

Crie um modelo do Taxi na plataforma Taxi. Depois que o modelo for criado, navegue até as **Organization Settings** e selecione a guia **ESP Connectors**.

### Etapa 2: Criar o conector da Braze {#step-2-create-braze-connector}

1. Na caixa de diálogo exibida, selecione o botão **Add New** e, em seguida, selecione **Braze** na lista suspensa.
2. Selecione **Braze** para editar as configurações do conector da Braze.
3. Insira o endpoint da Braze e a chave de API da Braze.

O campo do conector mudará de cor depois que os detalhes com as permissões corretas forem fornecidos. Se esse campo não mudar, verifique se seus campos estão alinhados com os requisitos listados.

## Uso {#usage}

Localize o modelo do Taxi que você fez upload na seção **Modelos e mídia > Modelos de e-mail** da sua conta na Braze. Agora você pode usar esse modelo de e-mail para começar a enviar mensagens de e-mail envolventes para seus clientes!