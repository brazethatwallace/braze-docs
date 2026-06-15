---
title: "Movable Ink Da Vinci"
article_title: Movable Ink Da Vinci
alias: "/partners/movable_ink_da_vinci/"
description: "A integração entre a Braze e a Movable Ink Da Vinci permite que as marcas entreguem envios de mensagens altamente personalizados, aproveitando o mecanismo de decisão de conteúdo orientado por IA da Da Vinci. A Da Vinci faz a curadoria do conteúdo mais relevante para cada usuário e implementa as mensagens de forma integrada por meio da Braze."
page_type: partner
search_tag: Partner

---

# Movable Ink Da Vinci

> A integração entre a Braze e a Movable Ink [Da Vinci](https://movableink.com/da-vinci) permite que as marcas entreguem envios de mensagens altamente personalizados, aproveitando o mecanismo de decisão de conteúdo orientado por IA da Da Vinci. A Da Vinci faz a curadoria do conteúdo mais relevante para cada usuário e implementa as mensagens de forma integrada por meio da Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|------------|-------------|
| Movable Ink Da Vinci | É necessário ter uma conta Movable Ink Da Vinci para aproveitar essa parceria. |
| Braze Currents - Eventos de engajamento com mensagem | Uma exportação personalizada do Braze Currents é necessária para enviar dados de eventos de engajamento com mensagem para a Movable Ink. |
| Chave da API REST da Braze | É necessária uma chave da API REST da Braze com as permissões `messages.send`, `sends.id.create` e `campaigns.details`. Isso pode ser criado no dashboard da Braze em **Settings** > **API Keys**. <br><br>A equipe da sua conta Movable Ink fornecerá mais instruções de configuração diretamente. Consulte a seção [Integração](#integration). |
| Instância do app Da Vinci na Braze | Crie uma instância dedicada do app Da Vinci na Braze. Um novo app pode ser criado no dashboard da Braze acessando **Settings** > **App Settings** > **+ Add App**. Nomeie o app como "**Movable Ink - Da Vinci**" e selecione qualquer plataforma (é necessário selecionar uma plataforma, mas o tipo não afeta a funcionalidade). Saiba mais sobre [como adicionar um novo app]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/#step-3-add-your-app-instances). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para começar a usar a integração, entre em contato com a equipe da sua conta Movable Ink para obter assistência. A Movable Ink fornecerá acesso e instruções de configuração conforme necessário. Você precisará fornecer à Movable Ink um conjunto de credenciais da API da Braze para permitir que a Da Vinci envie e-mails por meio da API de envio de mensagens da Braze.

Quando conectada, a Movable Ink irá:

- Trabalhar com o cliente e com a Braze para configurar a conta Da Vinci da marca para que ela seja implantada com sucesso na Braze.
- Capturar configurações específicas da marca para alinhar-se aos seus casos de uso de envio de mensagens.
- Realizar testes abrangentes e garantia de qualidade para validar se os e-mails são entregues conforme o esperado e se atendem a todos os padrões operacionais e de desempenho.