---
nav_title: Copy Pastd
article_title: Copy Pastd
alias: /partners/copy_pastd/
description: "Este artigo de referência descreve a parceria entre a Braze e a Copy Pastd, um construtor de e-mail de arrastar e soltar que envia Content Blocks e modelos com Liquid diretamente para o seu espaço de trabalho da Braze."
page_type: partner
search_tag: Partner
---

# Copy Pastd

> O [Copy Pastd](https://copypastd.com/) Building Blocks é um construtor de e-mail de arrastar e soltar que envia Content Blocks com Liquid e modelos completos diretamente para o seu espaço de trabalho da Braze. Crie o design uma vez, sincronize com a Braze e reutilize os mesmos componentes em Campaigns, Canvas e fluxos disparados sem precisar reconstruir o HTML a cada vez.

_Essa integração é mantida pela Copy Pastd._

## Sobre a integração {#about-the-integration}

A integração entre a Braze e a Copy Pastd permite que você crie e-mails no Building Blocks — um construtor de e-mail hospedado que produz saídas nativas da Braze com Liquid limpo, referências a Content Blocks e modelos que se encaixam em qualquer Campaign ou Canvas sem necessidade de conversão.

Você pode montar um e-mail a partir de blocos reutilizáveis, enviá-lo para a Braze com um clique e ter a certeza de que os mesmos estilos de marca, componentes e conteúdo dinâmico são renderizados de forma consistente em todos os envios. O resultado são menos modelos codificados manualmente, menos tempo gasto criando e enviando e-mails e uma biblioteca centralizada que atualiza tudo quando algo muda.

## Pré-requisitos {#prerequisites}

Os itens a seguir são necessários para usar esta integração:

| Requisito | Descrição |
| ----------- | ----------- |
| Conta na Copy Pastd | Obrigatória para usar o Building Blocks. Inscreva-se em [copypastd.com](https://copypastd.com). Cada cliente recebe um espaço de trabalho, uma biblioteca de folhas de estilo, cinco licenças de construtor e uma biblioteca de blocos. |
| Chave da API REST da Braze para modelos de e-mail | Uma chave de API com as permissões `templates.email.create`, `templates.email.update` e `templates.email.list`.<br><br>Crie a chave no dashboard da Braze em **Settings** > **API Keys**. |
| Chave da API REST da Braze para Content Blocks | Uma chave de API com as permissões `content_blocks.create`, `content_blocks.update`, `content_blocks.info` e `content_blocks.list`.<br><br>Crie a chave no dashboard da Braze em **Settings** > **API Keys**. |
| Chave da API REST da Braze para Catálogos (opcional) | Uma chave de API com acesso de leitura a `catalogs.get`, `catalogs.get_item` e `catalogs.get_selections`. Obrigatória apenas se você planeja vincular blocos a Catálogos da Braze. |
| Endpoint REST da Braze | [A URL do seu endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint depende da URL da Braze para a sua instância. O Building Blocks seleciona o endpoint automaticamente com base no cluster que você escolher. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Casos de uso {#use-cases}

* **Criação consistente com a marca em escala.** Aplique uma folha de estilo do Building Blocks a cada modelo, e cores, fontes, estilos de botão e escala de espaçamento são renderizados de forma idêntica em centenas de e-mails. Quando a marca mudar, atualize a folha de estilo uma vez e sincronize para distribuir a atualização em todos os seus e-mails de uma só vez.
* **Conteúdo conectado e modelos de produto vinculados a Catálogos.** Vincule campos de blocos de e-mail diretamente aos seus endpoints de [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) e [Catálogos da Braze]({{site.baseurl}}/user_guide/data/activation/catalogs/) de dentro do construtor. Reutilize o mesmo modelo para lançamentos de novos produtos, coleções sazonais ou atualizações de conteúdo sem mexer no Liquid.
* **Produção de e-mail self-service para profissionais de marketing não técnicos.** Componha um e-mail completo a partir de blocos aprovados, incluindo personalização e lógica Liquid, e envie para a Braze para revisão sem precisar de suporte de desenvolvedores para escrever HTML ou Liquid ou realizar garantia de qualidade em nenhum dos dois.
* **Cabeçalhos e rodapés centralizados, atualizados com um clique.** Crie um cabeçalho ou rodapé uma vez no construtor Building Blocks e envie para a Braze. Cada modelo que o referencia permanece sincronizado, então uma troca de logo, uma alteração de texto legal ou um novo link social requer apenas uma atualização no Building Blocks para ser aplicada em todos os e-mails já na Braze.
* **Conteúdo centralizado em todos os e-mails.** Crie um hero, rodapé ou cartão promocional uma vez como um bloco inteligente do Building Blocks. Atualize-o, sincronize, e cada e-mail já na Braze que o referencia recebe a alteração no próximo envio. Fluxos de boas-vindas, newsletters semanais e jornadas disparadas permanecem atualizados sem editar cada Campaign.
* **Modelos bloqueados para contribuidores self-service.** Crie modelos, bloqueie campos selecionados e convide outras equipes para criar seus próprios e-mails a partir de uma interface de contribuidor sem conceder acesso a ferramentas voltadas ao usuário.

## Integração {#integration}

### Etapa 1: Conectar o Building Blocks à Braze {#step-1-connect-building-blocks-to-braze}

{% alert note %}
Conectar o Building Blocks à Braze é uma configuração única. Após a validação das suas credenciais, o Building Blocks salva as credenciais para todas as sincronizações e envios de modelos futuros.
{% endalert %}

1. Faça login no Building Blocks em [blocks.copypastd.com](https://blocks.copypastd.com), ou selecione **Login** em [copypastd.com](https://copypastd.com).
2. No dashboard, selecione **Set up your Braze connection**. (Esse botão aparece para administradores no primeiro login e até ser concluído. Você também pode acessar a página em **Team Settings** > **Connect** > **Braze API Keys**.)
3. Selecione o cluster da Braze no menu suspenso. O endpoint REST correspondente é preenchido automaticamente.
4. Cole sua chave de API de modelos, sua chave de API de Content Blocks e (opcionalmente) sua chave de API de Catálogos nos campos correspondentes.
5. Selecione **Validate and save**. O Building Blocks faz uma chamada à Braze para confirmar que as chaves funcionam e que os escopos de permissão estão corretos. Se algo estiver faltando, um erro inline mostra qual escopo está incorreto.

### Etapa 2: Sincronizar sua biblioteca com a Braze {#step-2-sync-your-library-to-braze}

1. Após a validação das chaves, selecione **Sync now** no modal de configuração. (Você também pode ressincronizar a qualquer momento em **Settings** > **Connect** > **Braze** > **Sync library**.) <br> O Building Blocks envia sua folha de estilo e blocos para o seu espaço de trabalho da Braze como Content Blocks da Braze. Eles aparecem na Braze com nomes prefixados com `CP_` (por exemplo, `CP_Hero_1`) ou `cp_` para folhas de estilo (por exemplo, `cp_default_style`).
2. Após a conclusão da sincronização, você pode enviar modelos individuais a partir do construtor usando **Push to Braze**.

## Personalizar o Building Blocks {#customize-building-blocks}

### Etapa 1: Configurar sua folha de estilo {#step-1-set-up-your-stylesheet}

1. No Building Blocks, navegue até **Settings** > **Build** > **Stylesheets**.
2. Edite a folha de estilo padrão ou crie uma nova. Defina sua paleta de cores (24 cores nomeadas), fontes (Google Fonts compatível), estilos de botão, estilos de link, raio e escala de espaçamento.
3. Selecione **Save**. O Building Blocks regenera o Liquid para cada bloco que usa essa folha de estilo.
4. Selecione **Sync now** para enviar os estilos atualizados para o seu espaço de trabalho da Braze.

### Etapa 2: Ativar endpoints de Conteúdo conectado (opcional) {#step-2-enable-connected-content-endpoints-optional}

1. No Building Blocks, navegue até **Settings** > **Connect** > **Connected Content endpoints**.
2. Adicione a URL do endpoint, dê um nome e salve. O Building Blocks suporta o formato de resposta do Google Sheets, além do formato JSON padrão.
3. No construtor, vincule qualquer campo de texto, imagem ou link a uma variável de Conteúdo conectado no painel **Personalize**. O Liquid {% raw %}`{% connected_content %}`{% endraw %} correto é gerado na exportação.

### Etapa 3: Vincular a Catálogos da Braze (opcional) {#step-3-bind-to-braze-catalogs-optional}

1. No Building Blocks, navegue até **Settings** > **Connect** > **Catalogs**. O Building Blocks lê a lista de catálogos usando a chave de API de Catálogos.
2. Abra um bloco compatível (por exemplo, uma grade de produtos).
3. Selecione um catálogo e uma seleção, depois mapeie os campos do bloco para os atributos dos itens do catálogo.
4. Envie o modelo. O Building Blocks emite o Liquid correto {% raw %}`{% catalog_items %}`{% endraw %} e {% raw %}`{% catalog_selection_items %}`{% endraw %} para a Braze resolver no momento do envio.

### Etapa 4: Adicionar seus atributos personalizados da Braze (opcional) {#step-4-add-your-braze-custom-attributes-optional}

O Building Blocks já vem com os atributos de usuário padrão da Braze (`first_name`, `email`, `country` e assim por diante). Para vincular blocos aos seus próprios atributos personalizados, importe-os para o Building Blocks uma vez e eles ficarão disponíveis em todos os menus suspensos de **Personalize**.

1. No Building Blocks, navegue até **Team Settings** > **Connect** > **Custom Attributes**.
2. Importe seus atributos personalizados usando um dos seguintes métodos:
* **Importação em massa (recomendado).** Na Braze, navegue até **Data Settings** > **Custom Attributes** e selecione **Export** (canto superior direito). Faça upload do CSV no Building Blocks.
* **Adicionar atributos um por vez.** Digite o nome do atributo (por exemplo, `loyalty_tier`) e selecione **Add**. Esse método é útil se você está adicionando apenas alguns atributos ou se deseja adicionar um novo atributo entre exportações da Braze.

Após salvar, seus atributos personalizados aparecem no menu suspenso **Personalize** do construtor junto com os padrões. Inserir um atributo renderiza o Liquid correto {% raw %}`{{custom_attribute.${name}}}`{% endraw %} na exportação, para que a Braze resolva o valor por destinatário no momento do envio.

## Usar a integração {#use-the-integration}

### Etapa 1: Enviar um modelo para a Braze {#step-1-push-a-template-to-braze}

1. Abra qualquer e-mail no construtor Building Blocks.
2. Selecione **Push to Braze** (canto superior direito).
3. Selecione o espaço de trabalho e confirme. O Building Blocks cria um modelo de e-mail na Braze com o Liquid renderizado.

O modelo aparece na Braze em **Modelos e mídia** > **Modelos de e-mail**, nomeado de acordo com o e-mail e a data selecionada nas configurações do e-mail.

### Etapa 2: Usar o modelo em uma Campaign ou Canvas {#step-2-use-the-template-in-a-campaign-or-canvas}

1. Na Braze, crie uma nova Campaign de e-mail ou etapa do Canvas.
2. Selecione **Templates** e escolha o modelo enviado pelo Building Blocks.

O modelo carrega todas as referências do Building Blocks (folha de estilo, Content Blocks) como Liquid ativo {% raw %}`{{content_blocks.${...}}}`{% endraw %}, então atualizações no Building Blocks se propagam sem precisar reimportar o modelo.

### Etapa 3: Atualizar conteúdo centralmente {#step-3-update-content-centrally}

1. No Building Blocks, edite o bloco ou folha de estilo relevante.
2. Selecione **Sync** para enviar o Content Block atualizado de volta para a Braze.

Cada e-mail na Braze que o referencia (evergreen, disparados, fluxos de boas-vindas) recebe a nova versão no próximo envio. Você não precisa editar cada Campaign.

### Etapa 4: Criar pools de conteúdo {#step-4-build-content-pools}

Pools de conteúdo são tabelas de linhas de conteúdo que os e-mails referenciam em vez de conter texto estático. Atualize o pool no Building Blocks, e cada e-mail na Braze que o utiliza serve o novo conteúdo no próximo envio. Use pools de conteúdo em qualquer lugar onde o mesmo conteúdo precisa se manter atualizado em muitos e-mails, como newsletters semanais, fluxos de boas-vindas, sequências de recuperação, campanhas sazonais ou jornadas pós-compra.

1. No Building Blocks, selecione **Content** na navegação principal.
2. Selecione **New Pool**. Forneça um nome que descreva o que ele contém (por exemplo, Ofertas Semanais, Catálogo de Produtos, Artigos de Notícias).
3. Escolha o tipo de bloco que o pool alimenta (por exemplo, Hero, Grid, Card). Isso define quais campos estão disponíveis em cada linha.
4. Adicione linhas. Cada linha é um conteúdo. Preencha os campos (título, imagem, texto do CTA, link do CTA e assim por diante).
5. Defina a ordem de prioridade arrastando as linhas para cima ou para baixo. Alterne cada linha entre ativa ou inativa e defina datas de início e término opcionais. No momento do envio, a linha ativa de maior prioridade cujas datas são válidas é a escolhida.
6. Clique em **Save**. Os blocos inteligentes agora podem referenciar esse pool.

### Etapa 5: Usar blocos inteligentes para renderizar conteúdo de pools nos seus e-mails {#step-5-use-smart-blocks-to-render-pool-content-in-your-emails}

Um bloco inteligente é um bloco no canvas do construtor que referencia um ou mais pools de conteúdo em vez de conter conteúdo estático. No momento do envio, a Braze renderiza a linha do pool que tem a maior prioridade, está ativa e tem datas válidas. O Liquid exportado faz o trabalho. Nenhuma configuração extra na Braze é necessária.

1. No Building Blocks, arraste um bloco inteligente para o canvas (qualquer tipo de bloco que tenha um pool correspondente).
2. No painel de propriedades, abra o editor de cascata.
3. Adicione um ou mais pools de conteúdo em ordem de prioridade. Essa é a cascata (Waterfall): o primeiro pool com uma linha ativa e com datas válidas é renderizado. Se não houver nada ativo, o bloco inteligente passa para o próximo pool, e depois para o seguinte. Um padrão comum é Promoção Relâmpago > Ofertas Semanais > Favoritos Evergreen, para que sempre haja algo disponível.
4. Envie o modelo para a Braze. O Liquid exportado carrega a cascata completa, para que a Braze avalie a prioridade do pool e as datas a cada envio.

A partir de agora, você atualiza o pool, não o e-mail. Fluxos disparados, newsletters evergreen e campanhas sazonais permanecem atualizados enquanto o pool estiver atualizado.

Encontre seus modelos do Building Blocks enviados na Braze em **Modelos e mídia** > **Modelos de e-mail**. Folhas de estilo e blocos sincronizados aparecem em **Modelos e mídia** > **Content Blocks**.

## Considerações {#considerations}

- **Uma instância da Braze por espaço de equipe do Building Blocks.** Cada equipe do Building Blocks se conecta a uma única instância da Braze. Clientes que operam múltiplos espaços de trabalho (marcas, regiões ou ambientes separados) podem adicioná-los à mesma equipe, o que permite o compartilhamento de blocos.
- **Permissões de chave de API são separadas por escopo.** As chaves de modelos e de Content Blocks são mantidas separadas. A validação falha rapidamente se uma chave estiver sem um escopo obrigatório, para que você saiba exatamente qual permissão adicionar na Braze.
- **Nomes de Content Blocks são prefixados.** O Building Blocks envia Content Blocks com os prefixos `CP_` (blocos) e `cp_` (folhas de estilo) para evitar conflitos com Content Blocks criados diretamente na Braze.
- **Edições na folha de estilo atualizam todos os e-mails.** As folhas de estilo são renderizadas como um único Content Block da Braze referenciado por cada modelo. Uma alteração no Building Blocks atualiza todos os e-mails na Braze que a utilizam, incluindo os já agendados. Teste alterações na folha de estilo em um modelo de rascunho antes de sincronizar.
- **A vinculação de Catálogos é somente leitura.** O Building Blocks lê os catálogos para popular a interface de vinculação. Ele não grava nos Catálogos da Braze. Todo o gerenciamento de catálogos continua sendo feito no dashboard da Braze.
- **Limites de taxa e novas tentativas.** Todas as requisições de saída respeitam os limites de taxa da Braze, com backoff exponencial, jitter e tratamento de Retry-After. Um cabeçalho `User-Agent: partner-CopyPastd` é enviado em cada chamada para atribuição de parceiro.
- **Nenhum dado de usuário é transmitido.** O Building Blocks é uma ferramenta de criação de conteúdo. Ele não envia atributos de usuário, eventos, compras ou dados de segmentos para a Braze, e não consome pontos de dados da Braze.

## Solução de problemas {#troubleshooting}

- **A validação da chave de API falha.** Verifique se cada chave possui as permissões exatas listadas nos Pré-requisitos. Os escopos de modelos e Content Blocks são verificados separadamente. Se você regenerar uma chave na Braze, cole o novo valor no Building Blocks e revalide.
- **Incompatibilidade de endpoint REST.** As chaves de modelos e Content Blocks devem vir do mesmo espaço de trabalho da Braze, e o endpoint REST deve corresponder ao cluster. O menu suspenso do Building Blocks define isso para você, então verifique a seleção do cluster se a validação falhar.
- **O envio para a Braze retorna um erro.** Abra **Settings** > **Build** > **Activity log** para ver a última tentativa de sincronização e a resposta que a Braze retornou. A maioria das falhas está relacionada a permissões (escopo ausente) ou cotas (limite de taxa, com nova tentativa automática).
- **O Content Block não está atualizando na Braze.** Acione uma ressincronização manual em **Settings** > **Connect** > **Braze** > **Sync library**. O Building Blocks realiza uma comparação e troca, então blocos inalterados são ignorados.
- **O modelo referencia um Content Block que ainda não existe na Braze.** Envie as dependências primeiro (folha de estilo, blocos inteligentes) usando **Sync library**, depois envie o modelo.
- **Para qualquer outra situação.** Entre em contato com a Copy Pastd em [help@copypastd.com](mailto:help@copypastd.com). Inclua o nome da sua equipe e o horário da ação que falhou para que a Copy Pastd possa consultar o registro de atividades correspondente.