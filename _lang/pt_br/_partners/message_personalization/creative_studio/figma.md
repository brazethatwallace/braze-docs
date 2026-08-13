---
nav_title: Figma
article_title: Figma
description: "Este artigo de referência descreve a parceria entre a Braze e o Figma, que permite enviar imagens e ativos visuais para a biblioteca de mídia da Braze."
alias: /partners/figma/
page_type: partner
search_tag: Partner
---

# Figma

> O [Figma](https://www.figma.com/) é uma plataforma de design colaborativo que permite criar, projetar e prototipar produtos.

## Sobre a integração {#about-the-integration}

A integração entre a Braze e o Figma permite enviar imagens e ativos visuais do Figma diretamente para a biblioteca de mídia da Braze.

Assista a este vídeo para ter uma visão geral de como a integração funciona.

{% multi_lang_include video.html id="ab5ywsi72n" source="wistia" %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta no Figma | É necessário ter uma conta no Figma para aproveitar essa parceria. |
| Acesso à biblioteca de mídia da Braze | Você precisa ter a permissão "Manage Media Library Assets" para adicionar, editar e excluir ativos da biblioteca de mídia na Braze. |
| Acesso ao espaço de trabalho da Braze | Você precisa ter acesso aos espaços de trabalho para os quais deseja fazer upload dessas imagens e ativos visuais do Figma na Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Instalar o plugin Figma to Braze Export {#step-1-install-the-figma-to-braze-export-plugin}

Acesse a comunidade do Figma para encontrar o [plugin Braze Export](https://www.figma.com/community/plugin/1606726267245196698/figma-to-braze-export). Selecione **Open In** para carregar o plugin no seu arquivo do Figma.

No Figma, você também pode encontrar o plugin Figma to Braze Export na seção **Plugins**.

### Etapa 2: Conectar à Braze {#step-2-connect-to-braze}

Após a instalação, selecione **Connect to Braze** para conectar sua conta da Braze e, em seguida, selecione **Continue**.

Depois, selecione seu espaço de trabalho da Braze no menu suspenso **Braze workspace** ou insira o nome do espaço de trabalho.

### Etapa 3: Selecionar seus ativos do Figma {#step-3-select-your-figma-assets}

Selecione as imagens e os ativos visuais para exportar para a Braze. Para selecionar múltiplos ativos, pressione <kbd>Shift</kbd> ou arraste e solte o cursor sobre os ativos.

O nome da imagem ou do ativo visual exportado usa o nome do frame selecionado no Figma.

### Etapa 4: Exportar para a Braze {#step-4-export-to-braze}

Selecione **Export to Braze**. Suas imagens e ativos visuais são enviados para a biblioteca de mídia da Braze. Todas as imagens importadas por meio dessa integração têm sua origem definida como **Figma**.