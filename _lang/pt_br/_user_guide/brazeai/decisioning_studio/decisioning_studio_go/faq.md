---
nav_title: FAQ
article_title: FAQ do Decisioning Studio Go
page_order: 8
page_type: FAQ
description: "Esta página fornece respostas para perguntas frequentes sobre o Decisioning Studio Go."
---

# Perguntas frequentes {#frequently-asked-questions}

## Geral {#general}

### O que é o Decisioning Studio Go? {#what-is-decisioning-studio-go}

O Decisioning Studio Go é um agente de decisão com IA integrado ao dashboard da Braze. Você cura um menu de opções — variantes de criativo, horário de envio, dias da semana — e o agente escolhe a combinação certa para cada usuário individual, otimizando para cliques. Ele entrega personalização um-para-um sem exigir um cientista de dados ou uma integração personalizada. A primeira versão suporta e-mail; canais adicionais serão lançados em betas separados, com cada canal gerenciado por seu próprio agente.

### Qual é a diferença em relação a testes A/B? {#how-is-this-different-from-ab-testing}

Os testes A/B encontram a variante com melhor desempenho na média de todo o público ou dentro de um Segment, e distribuem essa única variante para todos naquele grupo. O Decisioning Studio Go escolhe a melhor variante para cada usuário individual, com base no que aquele usuário já engajou anteriormente. Usuários diferentes podem receber variantes diferentes no mesmo envio. Em vez de distribuir uma variante vencedora para um grupo, o Decisioning Studio Go personaliza o conteúdo no nível individual.

### Qual é a diferença em relação ao Decisioning Studio Pro? {#how-is-this-different-from-decisioning-studio-pro}

O Go é o nível self-service. É o ponto de partida ideal para profissionais de marketing que desejam personalização um-para-um de e-mail sem uma implementação complexa. Ele otimiza para cliques e funciona com opções que você configura diretamente na Braze.

O Pro é o nível full-service. Ele otimiza para qualquer métrica de negócio, conecta-se a qualquer fonte de dados primários, suporta múltiplos canais e conta com suporte dedicado da equipe de AI Decisioning Services da Braze.

### Que tipo de IA é essa? É generativa? {#what-kind-of-ai-is-this-is-it-generative}

Não. O agente que decide o que enviar para cada usuário é um agente de decisão, não generativo. Ele não cria conteúdo para você. Você fornece as opções, e o agente aprende qual opção funciona melhor para cada usuário individual.

O Decisioning Studio Go é construído com aprendizado por reforço. O agente trata cada envio como uma oportunidade de aprender: ele testa combinações das opções que você aprovou, observa se cada usuário engaja e atualiza sua compreensão do que funciona para quem. Com o tempo, ele se torna cada vez mais preciso em combinar cada usuário individual com a opção do seu menu com maior probabilidade de gerar um clique.

## Públicos e grupos de controle {#audiences-and-control-groups}

### Qual é a diferença entre o grupo do Decisioning Studio e o grupo de controle aleatório? {#whats-the-difference-between-the-decisioning-studio-group-and-the-random-control-group}

O grupo do Decisioning Studio recebe conteúdo de e-mail otimizado por IA; o agente escolhe a melhor variante para cada usuário. O grupo de controle aleatório recebe combinações aleatórias das mesmas opções, sem otimização. Ambos os grupos respeitam as restrições que você configurou (por exemplo, se você definiu que uma linha de assunto não deve se repetir em 15 dias, essa regra se aplica ao controle aleatório também). Comparar os dois grupos oferece uma medida limpa do aumento gerado pelo agente.

### O controle aleatório é um grupo de holdout de usuários que não recebem e-mail? {#is-the-random-control-a-holdout-group-of-users-who-receive-no-email}

Não. Os usuários do controle aleatório ainda recebem e-mails. Eles recebem combinações selecionadas aleatoriamente das opções que você configurou, enviadas em dias aleatórios dentro do seu cronograma. Isso permite comparar "personalizado por IA" com "o mesmo conteúdo, enviado aleatoriamente", em vez de comparar com "nenhum e-mail".

### Por que o controle aleatório é obrigatório? {#why-is-the-random-control-required}

Por dois motivos. Primeiro, ele fornece uma medição contínua e em tempo real de quanto o agente está superando uma linha de base aleatória. Segundo, o agente usa o comportamento do controle aleatório como parte do seu sinal de aprendizado. O tamanho mínimo do controle aleatório é 5% — esse é o piso necessário para que o agente aprenda de forma confiável e para que a medição de desempenho seja significativa.

### Posso usar um Segment que já está sendo usado em outro Canvas ou Campaign? {#can-i-use-a-segment-thats-already-used-in-another-canvas-or-campaign}

Pode, mas é fortemente desencorajado e um aviso será exibido. Quando os mesmos usuários recebem mensagens do Decisioning Studio Go e de outros Canvas ou Campaigns ao mesmo tempo, as outras mensagens afetam o engajamento de formas que o agente não consegue considerar. A configuração mais limpa é um Segment dedicado ao agente.

## Configuração {#configuration}

### O que posso personalizar? {#what-can-i-personalize}

Dentro de cada criativo base, você pode marcar a linha de assunto, o CTA e uma imagem como pontos de personalização usando tags Liquid. O agente então escolhe entre as variantes que você forneceu para cada componente, por usuário. Você também pode ter múltiplos criativos base; o agente escolhe qual criativo base usar também.

### Posso usar Content Blocks para os componentes personalizados? {#can-i-use-content-blocks-for-the-personalized-components}

Não. Content Blocks não funcionam como pontos de substituição de componentes criativos neste momento. Coloque sua linha de assunto, CTA e imagem personalizados diretamente no corpo do e-mail, em vez de dentro de um bloco de conteúdo.

### Posso usar modelos baseados em imagem sem elementos clicáveis? {#can-i-use-image-based-templates-with-no-clickable-elements}

Modelos baseados em imagem são suportados, mas limitam o que o agente pode otimizar. Se o e-mail inteiro for uma única imagem, o agente ainda pode decidir qual imagem enviar, mas não consegue otimizar linha de assunto, CTA ou layout dentro do e-mail. Você obtém mais aumento com modelos baseados em HTML com múltiplos pontos de personalização.

### Posso alterar o evento de conversão? {#can-i-change-the-conversion-event}

Para o nível self-service, o evento de conversão suportado é cliques. No Decisioning Studio Pro, você pode otimizar para qualquer métrica de negócio personalizada.

### Como funciona a frequência de envio? {#how-does-send-frequency-work}

Você seleciona uma única frequência, como três envios por semana. O agente não decide entre frequências. Dentro dessa frequência, ele escolhe quais dias (entre os dias que você permitiu) e quais horários (dentro do seu horário de silêncio, no fuso local do usuário) para enviar.

### Como funcionam os limites de frequência? {#how-do-frequency-caps-work}

Durante a configuração, você pode aplicar as regras de limite de frequência do seu espaço de trabalho ao agente e escolher se os envios do agente contam para o limite de frequência global de cada usuário. Seu CSM ou consultor de soluções pode ajudar a decidir a abordagem certa para o seu programa com base em como os limites de frequência estão configurados no seu espaço de trabalho.

### O agente pode enviar por múltiplos canais? {#can-the-agent-send-across-multiple-channels}

Cada agente é de canal único, e o canal suportado atualmente é e-mail. Você pode executar múltiplos agentes em paralelo para programas diferentes, mas cada agente gerencia um canal.

## Testes e lançamento {#testing-and-launch}

### Como faço para testar antes de ir ao ar? {#how-do-i-test-before-going-live}

Use o recurso nativo de envio de teste no criador da Braze. Os envios de teste mostram combinações específicas de variantes que você seleciona — eles servem para revisar o e-mail em si, não para prever o que o agente realmente enviaria para um usuário real. A prévia dinâmica no criador também permite ver como diferentes combinações de variantes são renderizadas.

### O que acontece logo após o lançamento? {#what-happens-right-after-i-launch}

O agente entra em um período de treinamento. Os e-mails são enviados desde o primeiro dia, sem período de espera, mas o desempenho pode flutuar enquanto o agente explora combinações. Os relatórios indicam quando o agente ainda está em treinamento versus quando ele passou para a personalização ativa, para que você sempre saiba em qual estágio ele está.

### Posso editar o agente após o lançamento? {#can-i-edit-the-agent-after-launch}

Sim. Público, cronograma, criativos e restrições podem ser atualizados após o lançamento. Você precisa promover as alterações antes que elas entrem em vigor.

### E se eu atualizar as opções de conteúdo após o lançamento? {#what-if-i-update-content-options-after-launch}

Você pode adicionar, remover ou alterar variantes da mesma forma como as configurou originalmente. As alterações precisam ser promovidas antes de entrarem em vigor. Adicionar uma nova variante não reinicia o treinamento do agente nas variantes existentes.

## Relatórios e resultados {#reporting-and-results}

### Os relatórios do Decisioning Studio Go correspondem ao que vejo na análise de e-mail em outros lugares da Braze? {#does-decisioning-studio-go-reporting-match-what-i-see-in-my-email-analytics-elsewhere-in-braze}

Os números podem diferir. O Decisioning Studio aplica uma filtragem de cliques mais agressiva do que os relatórios padrão de e-mail, então os totais podem ser menores. A comparação relativa entre o grupo do Decisioning Studio e o controle aleatório é consistente dentro dos relatórios do Decisioning Studio, pois a filtragem de cliques é aplicada igualmente a cada grupo.

### Para quais métricas o agente otimiza? {#what-metrics-does-the-agent-optimize-for}

Cliques únicos diários por usuário. O objetivo do agente é maximizar o número de usuários distintos que clicam, não o volume bruto de cliques.

### Posso ver quais combinações estão tendo melhor desempenho? {#can-i-see-which-combinations-are-performing-best}

Sim. Os relatórios incluem a distribuição de elementos individuais — como linhas de assunto, CTAs e imagens — que o agente envia.

### Quem é responsável pelo conteúdo que o agente envia? {#whos-accountable-for-the-content-the-agent-sends}

Você. O agente só envia conteúdo que você adicionou como variante. O agente decide a combinação para cada usuário, mas cada elemento individual vem das variantes que você forneceu.

## Suporte {#support}

### Onde posso obter ajuda com meu agente? {#where-do-i-get-help-with-my-agent}

Entre em contato com seu CSM ou consultor de soluções da Braze para obter ajuda com configuração, análise de desempenho ou design de programa.