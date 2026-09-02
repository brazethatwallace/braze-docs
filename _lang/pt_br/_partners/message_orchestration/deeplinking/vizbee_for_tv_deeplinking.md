---
nav_title: Vizbee
article_title: Vizbee para deep linking de TV
alias: /partners/vizbee/
page_type: partner
description: "Este artigo de referência descreve a parceria entre a Braze e a Vizbee e como usá-la para oferecer suporte ao deep linking de TV."
search_tag: Partner

---
# Vizbee {#vizbee}

> [A Vizbee](https://vizbee.tv/) permite que todos os smartphones e smart TVs da sua casa funcionem juntos como um único dispositivo integrado para proporcionar ótimas experiências ao usuário. A Vizbee ajuda você a usar canais de marketing de apps móveis existentes, como notificações, deep links e e-mails, para adquirir e engajar espectadores de forma integrada em todos os dispositivos de TV Conectada (CTV) (como Roku, FireTV, Samsung TV, LG TV, etc.).

_Esta integração é mantida pela Vizbee._

## Sobre a integração {#about-the-integration}

A integração da Braze e da Vizbee permite que você use um único console para programar suas campanhas de marketing para adquirir e reter espectadores em apps de streaming em dispositivos móveis e de CTV. Com essa integração, você pode:
- Programar uma notificação móvel para usuários segmentados que, ao ser tocada, pode resultar na visualização do app móvel ou acionar de forma integrada a reprodução em um dispositivo de streaming ou TV nas proximidades.
- Programar uma campanha de e-mail marketing para usuários segmentados que, ao ser ativada, pode resultar em instalações automáticas do app CTV e login do usuário em um dispositivo CTV, como Roku ou FireTV.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta Vizbee | É necessário ter uma conta [Vizbee](https://vizbee.tv/) para aproveitar essa parceria. Você deve registrar seu app na Vizbee e ter um ID da Vizbee atribuído. |
| App iOS ou Android | Essa integração é compatível com apps para iOS e Android. Dependendo da sua plataforma, trechos de código podem ser necessários no seu aplicativo. |
| SDK or kit de desenvolvimento de software da Vizbee | Além do SDK or kit de desenvolvimento de software da Braze obrigatório, você deve instalar o SDK or kit de desenvolvimento de software da Vizbee. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Siga o [guia de integração de SDK or kit de desenvolvimento de software](https://console.vizbee.tv/app/vzb1765003429/develop/guides/ios-continuity) da Vizbee para configurar sua integração com a Braze. Lá você encontra orientações sobre deep linking do celular para a TV, instalações de apps de TV e atribuição de visualizações.

### Visualização de relatórios de instalação e atribuição {#vizbee-tv-app-installs-viewership-attribution}

A Vizbee e a Braze também permitem que você visualize o desempenho holístico das suas campanhas em dispositivos móveis e de CTV. O SDK or kit de desenvolvimento de software da Vizbee envia eventos personalizados para o SDK or kit de desenvolvimento de software da Braze, que podem ser visualizados nos seus relatórios de campanha no dashboard da Braze.