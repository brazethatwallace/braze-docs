---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "Este artigo de referência descreve a parceria entre a Braze e a Sheetlabs, um serviço que permite personalizar suas campanhas de marketing com dados provenientes de planilhas."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner
---

# Sheetlabs

> A [Sheetlabs](https://sheetlabs.com/) é uma plataforma que permite transformar planilhas em APIs poderosas e bem documentadas. Você pode importar dados do Google Sheets ou do Excel, transformá-los em uma API e, em seguida, usar essa API em outros aplicativos, como a Braze.
_Essa integração é mantida pela Sheetlabs._

## Sobre a integração {#about-the-integration}

A integração da Sheetlabs com a Braze permite que você use o [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) para incluir APIs da Sheetlabs em suas campanhas de marketing da Braze. Isso é normalmente usado para fornecer uma ponte entre uma planilha do Google (que é atualizada diretamente pela equipe de marketing) e os modelos da Braze. Isso permite que você faça mais com os modelos da Braze, como traduções ou conjuntos maiores de atributos personalizados.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Sheetlabs | É necessário ter uma [conta Sheetlabs](https://sheetlabs.com/) para aproveitar essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

A integração entre a Braze e a Sheetlabs permite executar os seguintes casos de uso:

1. **Separar o acesso do profissional de marketing do acesso à Campaign da Braze**: Algumas equipes desejam evitar dar a todos os funcionários acesso para configurar diretamente os modelos e o conteúdo da Braze. Em vez disso, eles querem que a equipe atualize o conteúdo de marketing em uma planilha. A Sheetlabs faz a ponte entre as planilhas e a Braze e pode ser atualizada em tempo real.
2. **Traduções**: Os modelos da Braze não oferecem suporte nativo a traduções. Se quiser oferecer suporte a vários idiomas, você deverá criar vários modelos. Ao usar a Sheetlabs em conjunto com a Braze, você pode ter um único modelo da Braze traduzido para vários idiomas.
3. **Extensão de atributos personalizados**: A Braze fornece um certo número de atributos personalizados que podem ser configurados. Ao usar a Sheetlabs em conjunto com a Braze, você pode adicionar outros atributos personalizados além dessa alocação inicial.

Consulte a [Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/) para saber mais sobre esses casos de uso.

## Integração {#integration}

### Etapa 1: Importar sua planilha para a Sheetlabs {#step-1-import-your-spreadsheet-into-sheetlabs}

Na Sheetlabs, faça upload de uma planilha do Excel ou vincule sua conta do Google e importe uma planilha do Google.

- Para importar uma planilha do Excel, clique em **Data Tables** na barra de menus e, em seguida, em **Import from CSV/Excel**.
- Para importar do Google Sheets, clique em **Data Tables** na barra de menus e, em seguida, em **Import from Google**. Em seguida, você precisará fornecer suas credenciais de login do Google e importar a planilha.

Você também pode optar por manter sua planilha do Google sincronizada, o que significa que a Sheetlabs buscará automaticamente os dados mais recentes da sua planilha do Google quando eles forem alterados.

Certifique-se de incluir o ID do usuário da Braze em sua planilha ou outro dado que possa ser usado como pesquisa posteriormente.

### Etapa 2: Criar uma API na Sheetlabs {#step-2-create-an-api-in-sheetlabs}

Em seguida, na Sheetlabs, acesse **APIs > Create API** e dê um nome à sua API. É provável que você queira permitir consultas por meio de um campo de pesquisa da sua planilha, como o ID do usuário da Braze.

Nesse ponto, você deve conseguir acessar sua API com um link como:<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`](https://sheetlabs.com/ACME/email1_translations?country=en).

### Etapa 3: Usar a API no Conteúdo conectado da Braze {#step-3-use-the-api-in-braze-connected-content}

Agora que sua API está acessível, você pode usá-la em suas chamadas de Conteúdo conectado. Aqui está um exemplo de como um modelo de tradução pode ficar:

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}
{% alert tip %}
Para mais exemplos e orientações sobre a integração com a Sheetlabs, consulte a [documentação da Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/).
{% endalert %}