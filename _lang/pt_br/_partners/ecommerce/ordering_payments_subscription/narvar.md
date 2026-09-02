---
nav_title: Narvar
article_title: Narvar
description: "Saiba como integrar o Narvar à Braze."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> O Narvar é uma plataforma pós-compra que aumenta a fidelidade do cliente por meio de rastreamento de pedidos, atualizações de entrega e gerenciamento de devoluções. A integração entre a Braze e o Narvar permite que as marcas aproveitem os eventos de notificação do Narvar para disparar mensagens diretamente da Braze, mantendo os clientes informados com atualizações oportunas.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Conta Narvar | É necessário ter uma conta Narvar para aproveitar essa parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissão `messages.send`. Isso pode ser criado no dashboard da Braze em **Settings** > **API or interface de programação do aplicativo (API) Keys**. |
| Endpoint REST or transferir estado representacional da Braze | [URL do seu endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), que depende da URL da sua instância da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Recursos compatíveis {#supported-features}

| Tipo | Recursos compatíveis |
|-------|----------|
| Notificações | - Antecipação de entrega<br>- Atraso da operadora<br>- Padrão entregue |
| Canais | Notificações por push |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recursos compatíveis" }

{% alert note %}
Se você tiver interesse em tipos de notificação ou canais adicionais, entre em contato com o CSM or gerente de sucesso do cliente or gestor de sucesso do cliente da Braze e do Narvar.
{% endalert %}

## Detalhes da integração {#integration-details}

Para cada evento de notificação, o Narvar inicia uma solicitação para o endpoint [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging/) da Braze para entregar uma mensagem push a cada consumidor que aceitou recebê-las.

O Narvar é responsável por configurar as cargas úteis de notificação por push para cada mensagem. Atualmente, o Narvar não possui uma interface de design integrada para notificações por push, então a equipe deles colaborará com a sua equipe para determinar e definir os requisitos de carga útil. Essas cargas úteis podem ser personalizadas da mesma forma que as enviadas pelo seu próprio sistema, incluindo suporte para placeholders de conteúdo variável, como dados de pedidos e informações do consumidor.

## Primeiros passos com a integração Braze-Narvar {#getting-started-with-the-braze-narvar-integration}

1. **Entre em contato com o CSM or gerente de sucesso do cliente or gestor de sucesso do cliente do Narvar** para manifestar interesse na integração.
2. **Defina os ambientes da Braze** para staging e produção.
3. **Gere uma chave de API or interface de programação do aplicativo (API)** na Braze para uso do Narvar.
4. **Gere chave(s) de Campaign** na Braze conforme necessário.
5. **Forneça as chaves de API or interface de programação do aplicativo (API) e de Campaign** ao Narvar por meio de um link seguro de uso único.
6. **Compartilhe os detalhes da carga útil da notificação por push** para finalizar a configuração.