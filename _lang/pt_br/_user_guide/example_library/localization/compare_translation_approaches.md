---
nav_title: Comparar abordagens de tradução
article_title: Comparar abordagens para gerenciar traduções multilíngues
page_order: 1
page_type: reference
description: "Compare Liquid manual, Content Blocks, catálogos, mensagens multilíngues, parceiros de tradução e Connected Content para escolher como a Kitchenerie gerencia textos localizados."
tool:
  - Campaigns
  - Canvas
---

# Comparar abordagens para gerenciar traduções multilíngues {#compare-approaches-for-managing-multi-language-translations}

> Avalie como os textos localizados são armazenados, atualizados, pré-visualizados e enviados para que você possa escolher uma abordagem de localização que se encaixe no seu fluxo de QA, mix de canais e frequência de atualização.

## Sobre este exemplo {#about-this-example}

A Kitchenerie, uma varejista fictícia de utensílios de cozinha, envia e-mails, push e mensagens no app em inglês, francês e alemão. As equipes de marketing e engenharia precisam de uma forma repetível e escalável de gerenciar traduções entre Campaigns.

A Braze oferece vários padrões de localização:

- **Liquid condicional manual:** Conteúdo inserido por idioma no corpo da mensagem
- **Content Blocks:** Blocos reutilizáveis (com ou sem tags de tradução multilíngue)
- **Catálogos:** Linhas de tradução estruturadas com chave por localidade
- **Mensagens multilíngues:** Tags de tradução, uploads de CSV e a API de tradução (acesso antecipado)
- **Parceiros de tradução:** Smartling, Phrase, Lokalise e outros
- **Connected Content:** Strings localizadas obtidas do seu CMS ou API no momento do envio

Este exemplo compara as vantagens e desvantagens de cada abordagem para que você possa escolher a mais adequada ao seu fluxo de QA, mix de canais, frequência de atualização e recursos da equipe. Ele não substitui a configuração passo a passo de nenhum método individual. Para guias detalhados de cada recurso, comece com [Localização]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) e [Locais em mensagens]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Considerações {#considerations}

- Decida se você precisa de prévia e QA no dashboard, fluxos de tradução profissional, atualizações de conteúdo de alta frequência ou copy orientado por CMS em tempo real antes de escolher um padrão.
- [Mensagens multi-idioma]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) oferecem suporte a e-mail, push, banners, mensagens no app e Content Blocks. Note que SMS e WhatsApp usam outros padrões de localização. Liquid manual, Content Blocks, catálogos, parceiros e Connected Content podem ser aplicados em canais onde esses recursos são suportados.
- A Braze não gera traduções. Você fornece o copy por meio do dashboard, CSV, API, importação de catálogo, fluxo de trabalho com parceiros ou CMS externo.
- Liquid manual e Content Blocks com condicionais incorporados precisam de convenções de nomenclatura e processos de revisão à medida que os idiomas crescem, e fluxos multi-idioma e de parceiros centralizam atualizações, mas podem exigir manutenção via CSV ou API.
- Connected Content e alguns fluxos de parceiros dependem de sistemas externos. Se uma API ou CMS estiver indisponível no momento do envio, o conteúdo localizado pode não ser carregado.
- Sobreposição é comum. Por exemplo, você pode usar tags multi-idioma para o corpo do e-mail, Content Blocks para rodapés compartilhados e catálogos para copy de produto no mesmo programa.

## Configuração {#setup}

### Etapa 1: Capture seus requisitos de localização {#step-1-capture-your-localization-requirements}

| Requisito | Perguntas a responder |
| --- | --- |
| Prévia e QA | Os profissionais de marketing precisam visualizar a prévia de cada localidade no criador da Braze antes do envio? |
| Escala | Quantos idiomas e com que frequência o texto muda? |
| Fluxo de trabalho | Você precisa de revisão, correções e aprovações de tradutores? |
| Formato dos dados | O texto é conteúdo de marketing livre ou campos de produto estruturados (nomes, preços, URLs)? |
| Automação | As traduções devem ser atualizadas automaticamente quando seu CMS muda? |
| Habilidades da equipe | Sua equipe consegue manter Liquid, uploads de CSV, APIs ou integrações com parceiros? |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Capture seus requisitos de localização" }

### Etapa 2: Compare as abordagens de forma geral {#step-2-compare-approaches-at-a-glance}

| Dimensão | Liquid manual | Content Blocks | Catálogos | Mensagens multilíngues | Parceiros de tradução | Connected Content |
| --- | --- | --- | --- | --- | --- | --- |
| Prévia no dashboard / QA | Sim | Sim | Sim | Sim | Varia por parceiro | Limitado — mais difícil visualizar conteúdo obtido |
| Padrão (sem integração) | Sim | Sim | Parcial — configuração de catálogo necessária | Sim | Não — configuração do fornecedor | Não — API ou CMS necessário |
| Cobertura de canais | Todos os canais suportados | Todos os canais suportados | Todos os canais suportados | E-mail, push, banners, mensagens no app, Content Blocks | Varia por parceiro | Todos os canais suportados |
| Esforço de implementação | Baixo | Baixo–médio | Médio | Baixo | Alto (depende do parceiro) | Médio |
| Esforço contínuo (BAU) | Alto — edições por mensagem | Médio — manutenção de blocos | Médio — atualizações via CSV ou API | Médio — uploads de CSV | Médio — gerenciado na plataforma | Baixo — obtido no momento do envio |
| Atualizações de alta frequência | Não | Parcial | Não | Parcial | Sim | Sim |
| Fluxo de tradução profissional | Não | Não | Não | Não | Sim | Não |
| Dados estruturados / de produto | Limitado | Limitado | Sim — ideal para textos com chave | Limitado | Varia | Sim — por meio de fonte externa |
| Risco de dependência externa | Nenhum | Nenhum | Nenhum | Nenhum | Médio | Médio — envio falha se a fonte estiver fora do ar |
| Mais indicado para | Poucos idiomas, atualizações infrequentes | Componentes compartilhados entre mensagens | Muitas localidades com strings estruturadas | Muitos idiomas com menor esforço de copiar e colar | Tradução empresarial com aprovações | Localização dinâmica orientada por CMS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Compare as abordagens de forma geral" }

### Etapa 3: Associe cenários no estilo Kitchenerie a uma abordagem {#step-3-match-kitchenerie-style-scenarios-to-an-approach}

| Cenário Kitchenerie | Ponto de partida recomendado |
| --- | --- |
| Três idiomas, poucas Campaigns por mês, equipe de marketing pequena | Liquid condicional manual ou Content Blocks com Liquid |
| Cabeçalho, rodapé e blocos legais compartilhados entre e-mail e mensagens no app | Content Blocks — com [traduções multilíngues salvas no bloco]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#save-translations-in-content-blocks) quando as localidades aumentam |
| Nomes de produtos, linhas promocionais e URLs de imagens organizados por localidade | [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) |
| E-mail e push em oito ou mais localidades com prévia no criador | [Mensagens multilíngues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) |
| TMS central com fluxo de trabalho de tradutores e aprovações | [Parceiros de localização]({{site.baseurl}}/partners/message_personalization/localization) (por exemplo, Smartling ou Phrase) |
| Texto gerenciado em um CMS que é atualizado diariamente | [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Associe cenários no estilo Kitchenerie a uma abordagem" }

### Etapa 4: Implemente a abordagem selecionada {#step-4-implement-the-approach-you-selected}

1. **Liquid condicional manual:** Use atributos de perfil `language` ou localidade com `if` / `elsif` / `else` em Liquid. Consulte [Abordagens alternativas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#alternative-approaches) e [Lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic).
2. **Content Blocks:** Crie blocos reutilizáveis; opcionalmente, oculte Liquid condicional dentro dos blocos. Consulte [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) e a guia Content Blocks em [Enviando mensagens traduzidas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
3. **Catálogos:** Importe linhas de tradução (por exemplo, `id`, `context`, `language`, `body`) e faça referência a elas com Liquid `catalog_items`. Consulte a guia Catálogos em [Enviando mensagens traduzidas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages).
4. **Mensagens multilíngues:** [Adicione localidades]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings), envolva o texto em tags de tradução e faça upload de um CSV. Se você tem acesso antecipado aos [endpoints de tradução]({{site.baseurl}}/api/endpoints/translations), pode atualizar traduções via API. Visualize a prévia com **Multi-language user** no criador.
5. **Parceiros de tradução:** Configure as localidades do espaço de trabalho e siga a integração com o parceiro (por exemplo, [Smartling]({{site.baseurl}}/partners/message_personalization/localization/smartling) ou [Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase)).
6. **Connected Content:** Chame seu CMS ou API de tradução no momento do envio. Teste com cuidado; a prévia pode não refletir as respostas da API em tempo real. Consulte [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).

Para orquestração de Canvas e Campaigns entre regiões (uma jornada versus uma jornada por país), consulte [Gerenciamento de traduções]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management) na página de Localização.

## Artigos relacionados {#related-articles}

- [Localização]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [Mensagens multilíngues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [Configurações de localização]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Parceiros de localização]({{site.baseurl}}/partners/message_personalization/localization)
- [Linguagem de acessibilidade para mensagens localizadas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility)