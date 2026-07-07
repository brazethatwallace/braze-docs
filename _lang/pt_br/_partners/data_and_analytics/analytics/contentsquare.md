---
nav_title: Contentsquare
article_title: Contentsquare
description: "Este artigo de referência descreve a parceria entre a Braze e a Contentsquare, uma plataforma de análise de dados de experiência digital que permite melhorar a relevância e as taxas de conversão de suas campanhas por meio do direcionamento de mensagens com base na experiência digital de seus clientes."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [A Contentsquare](https://contentsquare.com/) é uma plataforma de análise de dados de experiência digital que possibilita uma compreensão sem precedentes da experiência do cliente.

_Essa integração é mantida pela Contentsquare._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Contentsquare permite que você envie Live Signals (fraude, sinais de frustração, etc.) como eventos personalizados na Braze. Aproveite os insights de experiência da Contentsquare para melhorar a relevância e as taxas de conversão de suas campanhas, direcionando mensagens com base na experiência digital e na linguagem corporal de seus clientes.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta da Contentsquare | É necessário ter uma conta na Contentsquare para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. Para criar uma nova chave no dashboard da Braze, acesse **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [URL do seu endpoint REST]({% image_buster /assets/img/contentsquare_custom_events.png %}). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

Alguns casos de uso comuns da Braze e da Contentsquare incluem:
- Hiperpersonalizar mensagens com base na intenção do cliente, exibindo os dados de experiência do cliente na Braze.
- Redirecionar clientes com base em seu comportamento digital, hesitações, frustrações e intenções.
- Identificar experiências ruins na Contentsquare e recuperar clientes com mensagens direcionadas e ofertas de retenção.
- Recuperar clientes em risco enviando mensagens mais relevantes e empáticas no momento e local certos.

## Integração {#integration}

Para integrar a Contentsquare à Braze, você deve solicitar a instalação de uma integração "Live Signals" no catálogo de integração da Contentsquare:

1. Na Contentsquare, clique em **Console** no menu **Settings**. Isso redirecionará você para o projeto em que está trabalhando no momento.
2. Na página **Projects**, acesse a guia **Integrations** e clique no botão **+ Add integration**.
3. No catálogo de integrações, localize a integração **Live Signals** e clique em **Add**. A equipe da Contentsquare entrará em contato com você para configurar o trecho de código para enviar sinais ao vivo para a Braze.
4. A Contentsquare agora processará sua integração. O texto do indicador será atualizado após a conclusão da integração.

Para saber mais, consulte [Solicitar uma integração da Contentsquare](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186).

## Usando essa integração {#using-this-integration}

Quando a integração estiver concluída, os eventos personalizados da Contentsquare estarão disponíveis para uso em suas campanhas e Canvas. Você pode verificar quais eventos estão sendo enviados para a Braze em **Configurações de dados** > **Eventos personalizados**.

![Dados do Contentsquare Live Signals na guia de eventos personalizados da Braze]({% image_buster /assets/img/contentsquare_custom_events.png %})