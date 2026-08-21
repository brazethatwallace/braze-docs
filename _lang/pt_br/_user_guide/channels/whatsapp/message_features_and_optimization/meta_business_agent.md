---
nav_title: Meta Business Agent
article_title: Meta Business Agent e Braze WhatsApp
page_order: 8
description: "Este guia explica como o Meta Business Agent interage com um número de telefone do WhatsApp Business conectado à Braze e o que esperar se você ativá-lo."
page_type: reference
channel:
  - WhatsApp
alias: /meta_business_agent/
hidden: true
noindex: true
---

# Meta Business Agent e Braze WhatsApp {#meta-business-agent-and-braze-whatsapp}

> O Meta Business Agent pode responder a mensagens de entrada do WhatsApp em um número que também está conectado à Braze. Este artigo aborda como esses dois sistemas compartilham a visibilidade das mensagens, como ativar o agente nas ferramentas da Meta e como a cobrança é dividida. Ele reflete a funcionalidade e a documentação do produto Meta Business Agent da Meta em agosto de 2026.

A Meta continua desenvolvendo ativamente o Meta Business Agent, então alguns detalhes podem mudar. Consulte a [documentação do Meta Business Agent da Meta](https://developers.facebook.com/documentation/meta-business-agent/overview) para as informações mais recentes.

## O que é o Meta Business Agent? {#what-is-meta-business-agent}

O Meta Business Agent é um respondedor com tecnologia de IA que a Meta opera diretamente em um número de telefone do WhatsApp Business. Quando ativado para um número elegível, ele pode responder a mensagens de entrada dos usuários em nome da empresa, usando conhecimento (informações da empresa, perguntas frequentes, arquivos, conteúdo do website) e conectores configurados nas ferramentas da Meta.

A ativação do Meta Business Agent é feita inteiramente no WhatsApp Manager e no Meta Business Suite, e é separada do seu espaço de trabalho da Braze. A Braze não é necessária para a configuração, e atualmente não há controle no dashboard da Braze para isso.

## Como ele interage com seu número conectado à Braze {#how-it-interacts-with-your-braze-connected-number}

O Meta Business Agent e a Braze podem coexistir no mesmo número de telefone do WhatsApp Business, mas atualmente não compartilham visibilidade de todas as mensagens.

- **Mensagens de saída iniciadas pela Braze não são afetadas.** A Braze continua enviando mensagens de modelo do WhatsApp e mensagens de resposta por meio de Campaigns e Canvas exatamente como faz hoje, independentemente de o Meta Business Agent estar ativado.
- **Mensagens de entrada são roteadas pelo Meta Business Agent.** Para cada mensagem de entrada de um usuário, o Meta Business Agent decide se a encaminha para a Braze ou se a trata ele mesmo.
  - **Se a Meta roteia a mensagem para a Braze:** ela é processada da mesma forma que qualquer mensagem de entrada do WhatsApp é processada hoje. Os disparadores baseados em ação de Campaigns e Canvas existentes e as jornadas de ação são acionados de acordo com a lógica que você já construiu.
  - **Se o Meta Business Agent trata a mensagem ele mesmo:** a Braze atualmente não processa o canal separado (mensagens em espera e ecos de mensagens) que carregaria essa atividade. As mensagens de entrada que o agente decide tratar, e suas próprias respostas a essas mensagens, atualmente não são visíveis em nenhuma superfície da Braze.

| Fluxo de mensagens | O que acontece hoje |
| --- | --- |
| Mensagens de modelo do WhatsApp e mensagens de resposta enviadas por meio de Campaigns ou etapas do Canvas | Não afetado; a Braze continua enviando conforme configurado |
| Mensagem de entrada que a Meta roteia para a Braze | Processada normalmente; os disparadores e jornadas de ação existentes se aplicam |
| Mensagem de entrada que o Meta Business Agent trata ele mesmo | Atualmente não visível para a Braze; os disparadores e jornadas de ação existentes para mensagens de entrada não serão acionados |
| Mensagem de saída enviada pelo Meta Business Agent | Atualmente não visível para a Braze |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fluxo de mensagens" }

## Ativar o Meta Business Agent {#enable-meta-business-agent}

O Meta Business Agent é ativado por número de telefone nas ferramentas da Meta, não na Braze:

1. Verifique a elegibilidade e ative-o para um número de telefone no [WhatsApp Manager](https://business.facebook.com/wa/manage/home/), aceitando os Termos de Serviço do Meta Business Agent.
2. Configure o conhecimento e as habilidades do agente (informações da empresa, perguntas frequentes, arquivos, conectores) por meio das [APIs de configuração de agente](https://developers.facebook.com/documentation/meta-business-agent/reference/configure/agent-skills) da Meta.
3. Ative o agente usando as [Configurações do agente](https://developers.facebook.com/documentation/meta-business-agent/reference/onboard/agent-settings).

## O que considerar antes de ativá-lo {#things-to-weigh-before-enabling-it}

- **Sem controle no lado da Braze:** a ativação, configuração e desativação do Meta Business Agent acontecem nas ferramentas da Meta; não há nada para ligar ou desligar na Braze.
- **Cobrança:** com a introdução do Meta Business Agent, mensagens não baseadas em modelo agora são classificadas em uma de duas categorias: Serviço (categoria existente) ou Meta Business Agent (nova categoria).
  - Respostas não baseadas em modelo tratadas pela Braze são cobradas como mensagens de serviço a partir de 1º de outubro de 2026.
    - Se você responder a uma mensagem de entrada com um modelo de marketing, utilidade ou autenticação, a cobrança será feita de acordo com essa categoria.
  - Mensagens do Meta Business Agent são cobradas diretamente pela Meta a partir de 1º de agosto de 2026. Consulte os preços da Meta para mais detalhes.
  - As mensagens são classificadas em apenas uma categoria, então você nunca será cobrado duas vezes pela mesma mensagem.