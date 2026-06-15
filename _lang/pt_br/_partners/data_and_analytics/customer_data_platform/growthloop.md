---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "Este artigo de referência descreve a parceria entre a Braze e a GrowthLoop, uma plataforma que permite segmentar dados de cliente diretamente de data warehouses e enviá-los para a Braze."
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> A [GrowthLoop](https://growthloop.com/) ajuda as equipes de marketing a ativar dados de cliente do data warehouse na nuvem para a Braze e outros canais. Automatize, escale e meça programas de marketing a partir do seu data warehouse na nuvem, mantendo os dados em um único local centralizado.

_Essa integração é mantida pela GrowthLoop._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a GrowthLoop permite segmentar dados de cliente diretamente do data warehouse e enviá-los para a Braze, garantindo que os usuários possam otimizar o conjunto de recursos avançados da Braze em conjunto com sua única fonte da verdade. Simplifique os esforços de marketing para segmentação e ativação de clientes, reduzindo o tempo necessário para segmentar, lançar, testar e medir os resultados de campanhas direcionadas enviadas para a Braze.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta GrowthLoop growth ou enterprise | Uma conta GrowthLoop é necessária para aproveitar esta parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com todas as permissões.<br><br>Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | Sua URL de endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso {#use-cases}

Envie listas de clientes do seu data warehouse para a Braze, direcionando campanhas de e-mail e notificação por push com um clique, e mantenha-as sempre sincronizadas.

- E-mails baseados na ativação de inscrição — envie e-mails para ajudar os usuários que abandonam seu fluxo de inscrição e converta-os em usuários ativos.
- E-mails baseados em qualquer comportamento do usuário — envie e-mails com base no comportamento do usuário, como "Adicionar ao Carrinho".
- E-mails para clientes perdidos — reengaje clientes perdidos via e-mail com uma oferta.

## Integração {#integration}

### Configurar conexão da Braze no GrowthLoop {#configure-braze-connection-in-growthloop}

Após fazer login na plataforma de segmentação do GrowthLoop, navegue até a guia **Destinations** na barra lateral esquerda e clique em **New Destination** no canto superior direito.

Role até encontrar a Braze e clique em **Add Braze**.

Um popup aparecerá para configurar a conexão com o destino.

- **Destination name**: é assim que o destino será nomeado e referido no app daqui para frente
- **Sync frequency**: selecione Daily ou Hourly; controla com que frequência a GrowthLoop exporta públicos para a Braze
- **API key**: chave de API criada nos requisitos, com as permissões necessárias
- **API URL**: URL conforme definido nos requisitos

Clique em **Create** e você poderá exportar seu primeiro público para a Braze! Para criar um público na GrowthLoop, visite [Criar um público](https://www.growthloop.com/help-center-articles/create-an-audience).

### Pós-exportação {#post-export}

Depois que seu público for exportado, a cada 15 minutos a GrowthLoop gerará uma versão atualizada das suas listas de clientes e a enviará para a Braze.

Ao mesmo tempo, a GrowthLoop removerá usuários do seu público que não se qualificam mais e adicionará novos usuários qualificados ao seu público.

A Braze corresponderá os usuários e criará uma flag, indicando que eles fazem parte de um público da GrowthLoop.

Ao criar uma Campaign na Braze, você pode selecionar clientes nesse público da GrowthLoop.

## Solução de problemas {#troubleshooting}

Entre em contato com a equipe da GrowthLoop pelo e-mail solutions@growthloop.com para obter informações adicionais ou suporte.