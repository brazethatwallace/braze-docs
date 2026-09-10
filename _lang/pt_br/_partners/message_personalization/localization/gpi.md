---
nav_title: GPI
article_title: Globalization Partners International
date_published: "2026-09-09"
description: "Este artigo de referência descreve a parceria entre a Braze e a Globalization Partners International (GPI), um provedor de serviços de tradução. O GPI Translation Services Connector extrai conteúdo da Braze para tradução e importa as traduções finalizadas de volta pela API de Tradução da Braze."
alias: /partners/gpi/
page_type: partner
search_tag: Partner
---

# Globalization Partners International

> A [Globalization Partners International](https://www.globalizationpartners.com/) (GPI) fornece o GPI Translation Services Connector para a Braze. O conector extrai conteúdo de Campaigns, Canvas, modelos de e-mail e Content Blocks para tradução e, em seguida, importa as traduções finalizadas de volta para a Braze pela API de Tradução. A GPI oferece suporte a tradução humana, tradução com IA e tradução com IA com pós-edição por especialistas em mais de 200 idiomas.

_Essa integração é mantida pela Globalization Partners International._

## Sobre a integração {#about-the-integration}

O GPI Translation Services Connector se integra ao modelo multilíngue nativo da Braze e à API de Tradução. Você extrai o conteúdo traduzível pelo GPI Translation Portal, envia para a GPI para tradução e importa as traduções finalizadas de volta para a Braze sem precisar copiar e colar manualmente. A GPI preserva as Liquid tags e a personalização durante todo o fluxo de trabalho.

## Casos de uso {#use-cases}

### Lançamento de Campaign global {#global-campaign-launch}

Selecione Campaigns, Canvas ou modelos de e-mail na Braze, defina os idiomas de origem e destino e envie o conteúdo para a GPI para tradução humana profissional. A GPI cuida da localização e da garantia de qualidade em prévias de rascunho antes do lançamento.

### Localização urgente ou de alto volume {#time-sensitive-or-high-volume-localization}

Encaminhe promoções relâmpago, mensagens urgentes de ciclo de vida ou grandes lotes de Content Blocks pelo conector para receber as traduções importadas de volta para a Braze automaticamente. O prazo de entrega depende do fluxo de trabalho escolhido e pode variar de semanas a minutos.

### Suporte à internacionalização {#internationalization-support}

A GPI oferece orientação sobre formatação e práticas recomendadas para localização na Braze, incluindo idiomas da direita para a esquerda (RTL), como árabe, hebraico e persa.

### Localização contínua em escala {#ongoing-localization-at-scale}

A GPI usa Memória de Tradução para reutilizar traduções anteriores, garantindo consistência de terminologia e estilo e reduzindo custos em correspondências exatas, repetidas e parciais. Atualize Campaigns no idioma de origem na Braze e envie o conteúdo revisado para a GPI para atualizar as traduções correspondentes.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa do seguinte:

| Pré-requisito | Descrição |
| --- | --- |
| Uma conta na Globalization Partners International | É necessário ter uma conta na GPI para usar essa integração. |
| Uma chave da API REST da Braze | Uma chave da API REST da Braze com as seguintes permissões:<br>- `campaigns.list`<br>- `campaigns.details`<br>- `campaigns.translations.get`<br>- `campaigns.translations.update`<br>- `canvas.list`<br>- `canvas.details`<br>- `canvas.translations.get`<br>- `canvas.translations.update`<br>- `content_blocks.list`<br>- `content_blocks.info`<br>- `content_blocks.translations.get`<br>- `content_blocks.translations.update`<br>- `templates.email.list`<br>- `templates.email.info`<br>- `templates.email.translations.get`<br>- `templates.email.translations.update`<br><br>Crie essa chave no dashboard da Braze em **Configurações** > **APIs e identificadores** > **Chaves de API**. Para saber mais, consulte [Criando chaves da API REST]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| Um endpoint REST da Braze | [A URL do seu endpoint REST]({{site.baseurl}}/api/basics#endpoints). O endpoint depende da URL da Braze para a sua instância. |
| Configurações multilíngues da Braze | Os locais de destino devem estar configurados na Braze em **Configurações** > **Configurações de localização**. Para saber mais, consulte [Configurações multilíngues]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Criar uma chave da API REST da Braze {#step-1-create-a-braze-rest-api-key}

1. Na Braze, acesse **Configurações** > **APIs e identificadores** > **Chaves de API**.
2. Crie uma chave da API REST com as permissões listadas em [Pré-requisitos](#prerequisites).
3. Copie a chave de API e anote o endpoint REST da sua instância.

### Etapa 2: Enviar as configurações para a GPI {#step-2-send-settings-to-gpi}

1. Envie a sua chave de API e o endpoint REST para o gerente de conta da GPI.
2. Envie a lista de usuários que precisam de acesso ao conector para que a GPI possa ativá-lo para eles.
3. A GPI configura o conector com as suas credenciais e valida a conexão.

### Etapa 3: Configurar as definições de localização na Braze {#step-3-configure-localization-settings-in-braze}

1. Na Braze, acesse **Configurações** > **Configurações de localização** e confirme que os locais de destino estão ativados.
2. Confirme que o conteúdo enviado para tradução tem os locais necessários ativados. Conteúdo sem locais ativados não pode receber traduções importadas.
3. Adicione [Liquid tags de tradução]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) ao redor do conteúdo que precisa de tradução.
4. Para idiomas RTL, adicione Liquid tags para controlar a direção do conteúdo com base no idioma. Evite diretivas de alinhamento por estilo, a menos que você confirme que elas não afetam a renderização RTL.

## Usando a GPI com a Braze {#use-gpi-with-braze}

Somente conteúdo em status de rascunho ou rascunho pós-lançamento pode ser traduzido na Braze.

### Etapa 1: Exportar conteúdo para tradução {#step-1-export-content-for-translation}

1. No [GPI Translation Portal](https://www.translationportal.com), abra o conector **Braze** e selecione **New Request**.
2. Preencha a guia **Information** e, em seguida, abra a guia **Content**. Em **Categories**, selecione **Campaign**, **Canvas**, **Email Template** ou **Content Block** e escolha os itens a serem exportados.
3. Selecione **Submit** para enviar uma solicitação de orçamento para a GPI. O gerente de conta da GPI entrará em contato quando o orçamento estiver pronto para revisão e aprovação.

### Etapa 2: Importar traduções para a Braze {#step-2-import-translations-into-braze}

1. No conector **Braze**, localize o projeto que você deseja importar.
2. Selecione o ícone **Import** na coluna **Actions**.
3. Aguarde a mensagem de confirmação da importação. Verifique o status do trabalho de importação na página **Jobs**.

### Etapa 3: Verificar o status da solicitação de tradução {#step-3-check-translation-request-status}

1. Acesse o [GPI Translation Portal](https://www.translationportal.com).
2. Selecione **Sign In** e insira suas credenciais.
3. Na navegação do GPI Translation Portal, selecione **Braze** para abrir o dashboard do conector. Analise as tabelas **Quotes** e **Projects** para ver o status das solicitações e dos projetos.

### Etapa 4: Pré-visualizar traduções na Braze {#step-4-preview-translations-in-braze}

Depois de importar as traduções, pré-visualize na Braze:

1. Abra a tela **Editar** da Campaign ou mensagem que você traduziu.
2. No **criador de mensagem**, acesse a guia **Preview and Test** ou **Test**.
3. Em **Preview message as user**, selecione **Multi-language user** e escolha o local que deseja visualizar.
4. Confirme a prévia no idioma de destino. Para compartilhar com revisores externos, gere um link de prévia.

## Considerações {#considerations}

- O GPI Translation Services Connector para a Braze é distribuído sem custo.

## Solução de problemas {#troubleshooting}

Para obter assistência com o GPI Translation Services Connector para a Braze ou qualquer projeto de tradução da GPI, entre em contato com o gerente de projetos da GPI, ligue para +1-866-272-5874 ou envie um e-mail para [support@globalizationpartners.com](mailto:support@globalizationpartners.com).