---
nav_title: Nift
article_title: Nift
description: "Este artigo de referência descreve a parceria entre a Braze e a Nift, uma plataforma bilateral que ajuda as empresas a adquirir, engajar e reter clientes."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> A [Nift](https://gonift.com/) ajuda as empresas a adquirir, engajar e reter clientes. A plataforma bilateral ajuda os parceiros a agradecerem seus clientes com cartões-presente da Nift. Agradecer aos clientes aumenta o lifetime value e gera receita incremental.

_Esta integração é mantida pela Nift._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Nift permite disparar automaticamente "agradecimentos" com presentes da Nift em momentos-chave do ciclo de vida do cliente e identificar quais clientes usaram o presente. Os cartões-presente Nift podem ser usados para acessar produtos e serviços fornecidos por marcas que confiam na tecnologia de matchmaking da Nift para adquirir novos clientes de forma econômica em escala.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Nift | É necessário ter uma conta Nift para aproveitar esta parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com todas as permissões de dados de usuários. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | Sua URL de endpoint REST. Seu endpoint dependerá da URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração {#integration}

### Etapa 1: Conecte-se à Braze na Nift {#step-1-connect-to-braze-in-nift}

Visite seu [dashboard da Nift](https://www.gonift.com/users/sign_in), navegue até **Accounts** > **Integrations** > **Braze** e clique em **Connect**.

### Etapa 2: Adicionar credenciais da Braze {#step-2-add-braze-credentials}

Na página **Link your Braze Account**, forneça sua chave da API REST da Braze e selecione seu endpoint da Braze, que dependerá da URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints).

Você pode alterar o nome do parâmetro de ID do cliente no link de indicação enviado aos seus clientes. A Nift usará isso para marcar seus clientes como processados na Braze quando eles tiverem selecionado um presente de uma de nossas marcas.

Clique em **Link Account**.

!["Página de integração do serviço Nift solicitando a chave de API da Braze e a URL do dashboard da Braze."]({% image_buster /assets/img/nift/link_your_braze_account.png %})

## Usando a integração {#using-the-integration}

Para usar a integração, distribua o link de indicação no seu envio de mensagens. Quando seu cliente usar o link de indicação e selecionar um presente de uma de nossas marcas, a Nift o marcará como processado na Braze.

Após a integração com a Braze, a Nift enviará automaticamente eventos para o registro de cliente existente na Braze com os seguintes dados:

- Nome do evento: `nift_processed`
- Horário: o momento em que o cliente selecionou/usou o presente