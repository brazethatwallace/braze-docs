---
nav_title: Denada
article_title: Denada
alias: /partners/denada/
description: "Este artigo de referência descreve a parceria entre a Braze e a Denada, uma plataforma criativa de marketing com IA que permite criar modelos de e-mail alinhados à sua marca por meio de conversa natural e exportá-los diretamente para a Braze."
page_type: partner
search_tag: Partner
---

# Denada

> A [Denada](https://heydenada.com) é uma plataforma criativa de marketing com IA que permite que especialistas no assunto criem materiais de marketing alinhados à marca por meio de conversa natural. Com a Denada, equipes podem ir da ideação ao conteúdo de e-mail finalizado sem precisar de expertise em design.

_Essa integração é mantida pela Denada._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Denada permite exportar modelos de e-mail criados na Denada diretamente para a Braze, incluindo o upload automático de imagens para a Biblioteca de mídia da Braze. Isso simplifica o processo de transição da ideação criativa para a execução de campanhas.

## Pré-requisitos {#prerequisites}

Os itens a seguir são necessários para usar esta integração:

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Denada | Uma [conta Denada](https://app.heydenada.com) é necessária para usar esta integração. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões completas de **Templates**. <br><br>Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [A URL do seu endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint depende da URL da Braze para a sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso {#use-cases}

A Denada foi criada para profissionais de marketing e especialistas no assunto que desejam criar conteúdo de e-mail alinhado à marca sem habilidades de design ou programação. É ideal para quem:
- Quer usar IA conversacional para gerar rapidamente modelos de e-mail e enviá-los diretamente para a Braze
- Precisa iterar em modelos de e-mail existentes na Braze reexportando da Denada com detecção de conflitos e suporte a sobrescrita
- Quer fazer upload e gerenciamento automático de imagens na Biblioteca de mídia da Braze durante a exportação

## Integração {#integration}

### Etapa 1: Configure sua integração {#step-1-configure-your-integration}

Na Denada, selecione o nome da sua empresa no canto inferior esquerdo e, em seguida, selecione **Team settings** > **Add integration**.

Selecione **Braze** como a integração, insira sua **chave de API** da Braze e selecione seu **endpoint da API REST** na lista de regiões disponíveis.

{% alert note %}
Esta é uma configuração única. Quando suas credenciais forem validadas, sua configuração será salva para todas as exportações futuras.
{% endalert %}

### Etapa 2: Exporte um modelo para a Braze {#step-2-export-a-template-to-braze}

Na Denada, abra um modelo de e-mail no editor e selecione **Export** > **Braze**.

Insira um nome de modelo e uma linha de assunto para o e-mail. Escolha sua preferência de tratamento de imagens:
- **Upload new:** Faz upload de todas as imagens para a Biblioteca de mídia da Braze.
- **Use existing:** Reutiliza imagens previamente enviadas quando disponíveis.

Se um modelo com o mesmo nome já existir na Braze, a Denada detecta o conflito e solicita que você confirme se deseja sobrescrever o modelo existente ou criar um novo.

Selecione **Export**. A Denada renderiza o modelo em HTML, faz upload das imagens para a Braze e cria ou atualiza o modelo de e-mail na sua conta da Braze.

## Usando a integração {#using-the-integration}

Você pode encontrar seus e-mails da Denada enviados na Braze em **Modelos e mídia** > **Modelos de e-mail**. Eles estão prontos para uso em qualquer Campaign ou Canvas da Braze.

A Denada rastreia exportações anteriores, então exportações subsequentes do mesmo modelo podem atualizar o modelo existente na Braze em vez de criar duplicatas.