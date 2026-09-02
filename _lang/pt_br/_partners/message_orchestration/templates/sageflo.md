---
nav_title: Sageflo
article_title: Sageflo Radiate
description: "Este artigo de referência descreve a parceria entre a Braze e a Sageflo, uma ferramenta de marketing distribuído que permite que as equipes enviem facilmente seus próprios e-mails usando modelos, imagens e segmentos de público aprovados pelo marketing por meio de integrações de API or interface de programação do aplicativo (API) com a Braze."
alias: /partners/sageflo/
page_type: partner
search_tag: Partner

---

# Sageflo Radiate

> [Sageflo Radiate](https://sageflo.com/radiate) é uma ferramenta de marketing distribuído que permite que as equipes locais enviem facilmente seus próprios e-mails usando modelos, imagens e segmentos de público aprovados pelo marketing por meio de integrações de API or interface de programação do aplicativo (API) com a Braze.

_Esta integração é mantida pela Sageflo._

## Sobre a integração {#about-the-integration}

Dê às equipes locais as ferramentas de que precisam para fazer marketing de forma mais inteligente, aproveitando recursos sofisticados da Braze que incluem segmentação de público, governança de frequência e conteúdo dinâmico, tudo isso com diretrizes de proteção para sua marca.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Sageflo Radiate | É necessário ter uma conta Sageflo Radiate para aproveitar esta parceria. |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões completas de `templates` e `campaigns`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**. |
| Endpoint REST or transferir estado representacional da Braze | [URL do seu endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint de API or interface de programação do aplicativo (API) corresponde à URL do dashboard da sua instância da Braze. <br><br> Por exemplo, se a URL do seu dashboard for `https://dashboard-03.braze.com`, seu endpoint será `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

O Radiate é ideal para franquias e empresas de varejo que buscam ampliar seus esforços de marketing, capacitando equipes distribuídas a enviar e-mails para seus públicos locais pela Braze.

* Capacite equipes distribuídas a enviar facilmente e-mails de marketing e SMS
* Crie conexões com os clientes voltadas para a comunidade
* Mantenha a consistência da marca com proteções integradas
* Diminua a carga de trabalho da sua equipe de marketing nacional

## Integração {#integration}

Sua equipe de contas da Sageflo conduzirá a configuração da integração. Você precisará fornecer suas credenciais de API or interface de programação do aplicativo (API) da Braze, e a Sageflo trabalhará com sua equipe de marketing para configurar segmentos de público para locais e filiais específicos.

Após a conexão, a Sageflo irá:

* Configurar o ambiente Radiate e a conexão com a Braze
* Configurar segmentos de público baseados em localização na Braze
* Definir as configurações de Campaign, localização e grupo de usuários
* Mapear modelos da Braze para uso com Campaigns do Radiate
* Programar e conduzir o treinamento de usuários