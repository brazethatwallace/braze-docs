---
nav_title: Inbox Monster
article_title: Inbox Monster
alias: /partners/inbox_monster/
description: "Este artigo de referência descreve a parceria entre a Braze e o Inbox Monster, uma ferramenta de marketing por e-mail online que permite aos clientes da Braze desbloquear insights poderosos de entregabilidade e análise criativa para potencializar o desempenho da caixa de entrada."
page_type: partner
search_tag: Partner

---

# Inbox Monster

> O [Inbox Monster](https://inboxmonster.com/) é uma plataforma de sinais de caixa de entrada que ajuda marcas empresariais a garantir cada envio. É um conjunto integrado de soluções para entregabilidade, renderização criativa e monitoramento de SMS, que capacita as equipes modernas de gestão de relacionamento com o cliente (CRM) e acaba com os medos de envio.

A integração entre a Braze e o Inbox Monster permite eliminar os testes manuais de lista de sementes, automatizar a criação de sinais de posicionamento na caixa de entrada poderosos e acionáveis, simplificar o processo de revisão e aprovação de ativos criativos de e-mail e obter insights valiosos sobre entregabilidade. Você também pode importar modelos de e-mail de forma integrada para diagnósticos criativos e pré-visualizações em dispositivos.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta na plataforma Inbox Monster | Uma conta na plataforma Inbox Monster é necessária para aproveitar esta parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com as seguintes permissões: <br> - `messages.send` <br> - `templates.email.create`<br> - `templates.email.update` <br> - `templates.email.info`<br> - `templates.email.list` <br><br> E com os seguintes IPs na lista de permissões: <br> - `3.136.16.19` <br> - `3.140.233.31`<br> - `18.220.127.138` <br><br> Isso pode ser criado no dashboard da Braze em **Settings** > **APIs and Identifiers** na guia **API or interface de programação do aplicativo (API) Keys**. |
| Identificador do app da Braze | Um identificador de app da Braze. <br><br>Isso pode ser encontrado no dashboard da Braze em **Settings** > **APIs and Identifiers** na guia **App Identifiers**. |
| Endpoint da Braze | [Seu endpoint da Braze]({{site.baseurl}}/api/basics/#endpoints) está alinhado com a URL do seu dashboard da Braze.<br><br> Por exemplo, se a URL do seu dashboard for `https://dashboard-03.braze.com`, seu endpoint será `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para integrar o Inbox Monster, siga as etapas em [Integrando com o Inbox Monster](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_80147afaf3).

## Uso {#usage}

Para saber como enviar testes de posicionamento na caixa de entrada programados pelo Inbox Monster, consulte [Testes de posicionamento na caixa de entrada programados](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_7e74bc474e).