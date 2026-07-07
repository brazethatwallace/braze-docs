---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "Este artigo de referência descreve a parceria entre a Braze e o Phrase, um software baseado em nuvem para localização. Essa integração permite traduzir modelos de e-mail e Content Blocks sem sair da interface da Braze."
page_type: partner
search_tag: Partner

---

# Phrase

> O [Phrase](https://phrase.com/) é um software baseado em nuvem para gerenciamento de localização. O Phrase ativa fluxos de trabalho de tradução automatizados e oferece suporte à localização contínua para equipes ágeis.

_Essa integração é mantida pelo Phrase._

## Sobre a integração {#about-the-integration}

A integração do Phrase e da Braze permite traduzir modelos de e-mail e Content Blocks sem sair da interface da Braze. Com a integração do Phrase TMS para a Braze, você pode aumentar o engajamento dos clientes e impulsionar o crescimento em novos mercados com uma localização perfeita.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta Phrase TMS | É necessário ter uma conta Phrase TMS Ultimate ou Enterprise para aproveitar essa parceria. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com todas as permissões. <br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST da Braze | [Sua URL de endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

## Etapa 1: Configurações do Phrase TMS {#step-1-phrase-tms-settings}

No Phrase, navegue até **Settings > Integrations > Connectors > New**.

1. Forneça um nome para a conexão e altere o tipo para **Braze**.<br><br>
2. Insira a chave da API REST e o endpoint REST da Braze. <br><br>
3. Selecione como o conector deve importar modelos de e-mail com Content Blocks vinculados.
- Somente o modelo de e-mail selecionado
- Incluir Content Blocks<br><br>
4. Selecione como o conector deve exportar as traduções de modelos de e-mail.
- Criar novo item
- Item original
  - O item original exporta traduções para o mesmo modelo/bloco. Os segmentos de idioma são definidos pelo atributo fornecido.<br><br>
    {% raw %}
    Forneça o atributo de idioma se o item original for selecionado. O atributo de idioma define o idioma do argumento if/elsif. Se estiver usando a opção de item original, ela deverá ser estruturada conforme mostrado abaixo:

    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
    danish content
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
    portuguese content
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
    swedish content
    {% else %}
    Original content
    {% endif %}
    ```
    Ou usando o mapeamento de atribuição de chaves/valores:
    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
      {% assign abc_key1 = "danish_value1" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
      {% assign abc_key = "portuguese value" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
      {% assign abc_key = "swedish value" %}
    {% else %}
      {% assign abc_key = "Source language value" %}
    {% endif %}
    ```
    O Liquid acima deve ser rigorosamente seguido, mas o atributo de idioma, as chaves e os valores são ajustáveis.<br><br>
    Cada código de idioma só pode ser usado uma vez. No entanto, vários idiomas podem ser usados para um segmento, por exemplo:
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. Clique em **Test connection**. Uma marca de seleção será exibida se a conexão for bem-sucedida. Passe o mouse sobre o ícone para ver detalhes adicionais.<br><br>
7. Por fim, clique em **Save**. Esse conector estará disponível na página **Connectors**.

## Etapa 3: Enviar conteúdo para o Phrase e exportar de volta para a Braze {#step-3-send-content-to-phrase-and-export-back-to-braze}

1. Primeiro, configure o [portal do remetente](https://support.phrase.com/hc/en-us/articles/5709602111132) para permitir que os remetentes adicionem arquivos às solicitações diretamente do repositório on-line.<br><br>
2. Use o [Automated Project Creation (APC)](https://support.phrase.com/hc/en-us/articles/5709647363356) para que o Phrase TMS crie automaticamente novos projetos quando for detectada uma alteração nos estados especificados do fluxo de trabalho.<br><br>
3. Os itens de conteúdo selecionados são importados na primeira vez em que o APC é executado.

A [API do conector](https://cloud.memsource.com/web/docs/api#) pode automatizar etapas que, de outra forma, seriam executadas manualmente por meio da interface do usuário. [Webhooks](https://support.phrase.com/hc/en-us/articles/5709693398812) podem ser usados para que o Phrase TMS notifique sistemas de terceiros sobre determinados eventos (por exemplo, uma alteração no status do trabalho).