---
nav_title: Bynder
article_title: Bynder
description: "Este artigo de referência descreve a parceria entre a Braze e a Bynder, uma plataforma de gerenciamento de ativos digitais (DAM) que permite pesquisar e inserir URLs de ativos aprovados em Campaigns e Canvas da Braze por meio da extensão Universal Compact View para Chrome."
alias: /partners/bynder/
page_type: partner
search_tag: Partner
---

# Bynder

> A [Bynder](https://www.bynder.com) é uma plataforma de gerenciamento de ativos digitais (DAM) que ajuda os clientes a criar, gerenciar, encontrar e distribuir ativos digitais aprovados (imagens, vídeos e outros criativos) a partir de uma única fonte de verdade. Quando integrada à Braze, a extensão Universal Compact View (UCV) para Google Chrome da Bynder permite que profissionais de marketing pesquisem e selecionem ativos da Bynder sem sair do dashboard da Braze. Insira links para esses ativos diretamente em Campaigns e Canvas.

_Esta integração é mantida pela Bynder._

## Sobre esta integração {#about-this-integration}

Conectar a Bynder à Braze por meio da extensão UCV para Chrome dá aos profissionais de marketing acesso à biblioteca de ativos da Bynder dentro do editor de conteúdo da Braze. Abra a Universal Compact View como uma sobreposição em qualquer guia do navegador, incluindo o dashboard da Braze. Pesquise ou filtre pelo criativo certo e cole a URL do ativo na sua Campaign.

Isso mantém as Campaigns da Braze alinhadas com a fonte única de verdade da Bynder: as permissões corretas, a versão mais atual do arquivo e os direitos de uso corretos.

## Casos de uso {#use-cases}

- Profissionais de marketing que estão criando um e-mail, uma mensagem no app ou um Content Block na Braze podem inserir imagens de destaque, banners ou links de vídeos promocionais obtidos diretamente da Bynder, garantindo que as Campaigns usem a versão aprovada mais recente de um ativo.
- Gerentes de Campaign podem usar a barra de pesquisa e filtro da Universal Compact View para localizar criativos regionais ou localizados aprovados para um Segment de público específico antes de adicioná-los a uma etapa do Canvas.
- Equipes criativas podem aplicar a Dynamic Asset Transformation da Bynder para redimensionar ou reformatar um ativo para um canal específico antes de copiar o link para a Braze. Por exemplo, usar um recorte compacto para uma notificação por push ou um banner em tamanho completo para e-mail.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisa do seguinte:

| Requisito | Descrição |
| --- | --- |
| Uma conta Bynder | Uma conta Bynder com acesso aos ativos do DAM que você deseja referenciar na Braze. |
| Extensão Universal Compact View (UCV) da Bynder para Chrome | Instalada a partir da Chrome Web Store e conectada ao seu portal Bynder. Disponível apenas para Google Chrome. |
| Ativos e derivados públicos | Qualquer ativo, e o derivado específico que você planeja vincular, deve estar marcado como público na Bynder para que sua URL seja resolvida corretamente para os destinatários da mensagem. |
| Uma conta Braze | Acesso ao canal de envio de mensagens (e-mail, Content Block, mensagem no app, Canvas etc.) onde o ativo será usado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: instalar e conectar a extensão UCV da Bynder para Chrome {#step-1-install-and-connect-the-bynder-ucv-chrome-extension}

1. Acesse a [extensão UCV da Bynder](https://chromewebstore.google.com/detail/bynders-universal-compact/ilghhphnbdblpbdhmbdfiaidganphema) na Chrome Web Store.
2. Clique em **Add to Chrome**, revise as permissões solicitadas e clique em **Add extension**.
3. Na barra de ferramentas do Chrome, selecione o ícone da UCV da Bynder (fixe-o na barra de ferramentas primeiro, caso ainda não esteja visível).
4. Insira o domínio do seu portal Bynder (sem `https://`) e clique em **Connect**.
5. Na janela que se abre, faça login no seu portal Bynder com suas credenciais habituais.

### Etapa 2: pesquisar e selecionar um ativo da Bynder {#step-2-search-for-and-select-a-bynder-asset}

1. Com a extensão conectada, abra a Universal Compact View em qualquer guia do navegador, incluindo o dashboard da Braze.
2. Use o filtro inteligente e a barra de pesquisa para localizar a imagem, o vídeo, o documento ou o ativo de áudio que você precisa.
3. Selecione o ativo e, em seguida, selecione o derivado (ou o arquivo original, se for público) que deseja usar.
4. Clique em **Add Asset** para copiar a URL do ativo selecionado para a área de transferência.

### Etapa 3: adicionar a URL do ativo à sua Campaign na Braze {#step-3-add-the-asset-url-to-your-braze-campaign}

1. Na Braze, abra o e-mail, o Content Block, a mensagem no app ou a etapa do Canvas onde você deseja adicionar o ativo.
2. Cole a URL do ativo da Bynder copiada no campo relevante. Por exemplo, use uma tag `<img src="">` ou o campo de URL de imagem de um Content Block.

   Exemplo de URL de imagem:

   ```html
   <img src="https://your-portal.bynder.com/m/abcdef123456/original/campaign-banner.jpg" alt="Summer Campaign">
   ```

{: start="3"}
3. Salve e visualize sua mensagem para confirmar que o ativo é renderizado conforme esperado.

## Dicas {#tips}

### Aplicar Dynamic Asset Transformations antes de copiar a URL {#apply-dynamic-asset-transformations-before-copying-the-url}

Dentro da Universal Compact View, use as opções de transformação disponíveis para redimensionar, recortar ou reformatar um ativo para o canal que você está direcionando. Isso evita o upload de versões recortadas separadas para a Bynder.

### Gerar URLs de derivados específicas por canal {#generate-channel-specific-derivative-urls}

Cada transformação ou derivado produz sua própria URL distinta. Gere uma versão dimensionada para e-mail, outra para push e outra para mensagens no app, e cole cada uma no canal ou etapa do Canvas correspondente na Braze.

### Reutilizar uma URL de ativo em vários canais {#reuse-one-asset-url-across-channels}

Como um link colado aponta de volta para um ativo e derivado específicos na Bynder, o mesmo formato de URL pode ser reutilizado em e-mails, Content Blocks, mensagens no app e etapas do Canvas. Isso mantém o criativo consistente em todos os lugares onde é usado em uma Campaign.

### Atualizar o ativo de origem sem editar suas Campaigns {#update-the-source-asset-without-editing-your-campaigns}

Se o arquivo subjacente na Bynder for substituído mantendo as mesmas configurações de ativo público e derivado, qualquer mensagem ativa da Braze que referencie essa URL refletirá automaticamente a atualização. Você não precisa editar a Campaign em si.

## Considerações {#considerations}

- A extensão UCV da Bynder para Chrome está disponível apenas para Google Chrome. Em outros navegadores, copie as URLs dos ativos diretamente do portal completo da Bynder.
- Apenas ativos (e os derivados específicos sendo vinculados) que estão marcados como públicos na Bynder são resolvidos quando colados na Braze. Ativos privados retornam um erro de acesso para os destinatários.
- Se janelas pop-up não forem permitidas ou o portal já estiver aberto em outra guia, a janela de login pode não abrir corretamente. Antes de conectar, confirme que janelas pop-up estão permitidas e feche qualquer outra guia onde o portal esteja aberto.
- O acesso dentro da extensão segue as permissões existentes do usuário da empresa no DAM da Bynder, então ele vê e pode selecionar apenas os ativos que já está autorizado a acessar.

## Solução de problemas {#troubleshooting}

| Problema | Resolução |
| --- | --- |
| O ícone da extensão não está visível | Fixe a extensão UCV da Bynder na barra de ferramentas do Chrome a partir do menu de Extensões. |
| **Connect** não abre uma janela de login | Confirme que os pop-ups do Chrome estão permitidos para o domínio do seu portal Bynder e feche qualquer outra guia onde o portal já esteja aberto. |
| A URL do ativo não é renderizada na Braze | Confirme que o ativo e o derivado específico usado estão marcados como públicos no portal da Bynder. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }

Para saber mais, consulte a [documentação da Universal Compact View](https://support.bynder.com/hc/en-us/sections/16936397091858-Universal-Compact-View-UCV) da Bynder ou entre em contato com o suporte da Bynder.