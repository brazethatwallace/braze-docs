---
nav_title: Página do parceiro

page_order: 4

#Required
description: "Esta é a descrição da Pesquisa Google. Caracteres com mais de 160 são truncados, portanto, seja breve."
page_type: partner
tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks


noindex: true
#ATTENTION: remove noindex and this alert from template

---

# [Nome do parceiro] {#partner-name}

> Bem-vindo ao modelo de página de parceiro! Aqui, você encontrará tudo o que precisa para criar sua própria página de parceiro. Nesta primeira seção, você deve descrever o parceiro no primeiro parágrafo em uma ou duas frases. Além disso, inclua um link para o site principal do parceiro.

No segundo parágrafo, você deve explorar e explicar o relacionamento entre a Braze e esse parceiro. Esse parágrafo deve explicar como a Braze e esse parceiro trabalham juntos para estreitar o vínculo entre o usuário da Braze e seu cliente. Explique a "elevação" que ocorre quando um usuário da Braze se integra ou utiliza esse parceiro e seus serviços.

## Requisitos ou pré-requisitos {#requirements-or-prerequisites}

Esta seção é sobre o que você precisa para integrar com o parceiro e começar a usar os serviços dele. A melhor forma de apresentar essas informações é com um parágrafo rápido e instrutivo que descreva detalhes importantes e não técnicos do tipo "precisa saber", como se a sua integração estará sujeita a verificações de segurança ou aprovações adicionais. Em seguida, você deve usar uma tabela para descrever os requisitos técnicos da integração.

{% alert important %}
Os requisitos a seguir são requisitos típicos que você pode precisar da Braze. Recomendamos usar os títulos atribuídos, a origem, os links e a redação conforme listados na tabela a seguir. Certifique-se de ajustar a descrição para que você saiba para que cada um desses requisitos é utilizado.
{% endalert %}

| Requisito | Origem | Acesso | Descrição |
|---|---|---|---|
| Chave da API REST do espaço de trabalho da Braze | Plataforma Braze | Página **Configurações** > **Chave de API** | Esta descrição deve indicar o que fazer com a chave da API REST do espaço de trabalho. |
| Endpoint da API da Braze | Plataforma Braze | Confira nossos [endpoints listados]({{site.baseurl}}/api/basics#endpoints) ou abra um [ticket de suporte]({{site.baseurl}}/braze_support). | Descrição pendente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Requisitos ou pré-requisitos" }

## Integração [tipo de integração] {#type-of-integration-integration}

Aqui é onde você detalha a integração em etapas. Não escreva parágrafos intermináveis — estes são documentos técnicos que serão usados tanto por profissionais de marketing quanto por desenvolvedores para colocar a integração em funcionamento. Seu único objetivo nesta seção é escrever uma documentação descritiva que ajude o usuário da Braze a realizar o trabalho. Por "tipo de integração" no título da seção, queremos indicar se é uma integração lado a lado, servidor para servidor ou padrão. Isso permite que você tenha múltiplas seções de integração caso haja mais de uma forma de integrar com esse parceiro.

Se for uma integração com Currents, esta página deve estar localizada na seção de Currents, e uma página de navegação correspondente deve ser criada para redirecionar para essa localização em Currents.

### Etapa 1: Esta é uma breve descrição da primeira etapa {#step-1-this-is-a-short-description-of-step-one}

Apenas detalhe o processo, incluindo qualquer código necessário. Lembre-se de que você pode oferecer vários conjuntos diferentes de código — não há necessidade de oferecer apenas uma forma de integração.

### Etapa 2: Esta etapa descreverá imagens {#step-2-this-step-will-describe-images}

Você tem a opção de incluir imagens na sua documentação, então recomendamos que faça isso de forma consciente.

### Etapa 3: Quantas etapas {#step-3-how-many-steps}

Descreva o uso da integração — especialmente se isso envolver a inserção de Liquid no nosso criador de mensagem.

## Personalização {#customization}

Esta é uma seção **opcional**. Aqui, você pode descrever quaisquer formas específicas de personalizar sua integração entre os dois parceiros.

## Usando esta integração {#using-this-integration}

Isso deve descrever como usar a integração — informe ao leitor se ele precisa apertar alguns botões ou se não precisa fazer nada após a integração.

### Etapa 1: Esta é uma breve descrição da etapa um

Apenas seu típico passo a passo.

## Casos de uso {#use-cases}

Esta pode ser uma parte essencial da sua documentação. Embora seja opcional, este é um bom lugar para descrever casos de uso típicos ou até mesmo inovadores para a integração. Isso pode ser usado como uma forma de vender ou aumentar o valor do relacionamento — fornece contexto, ideias e, o mais importante, uma maneira de visualizar as capacidades da integração.