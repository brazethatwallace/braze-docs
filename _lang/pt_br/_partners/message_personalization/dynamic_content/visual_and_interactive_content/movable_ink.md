---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "Este artigo de referência descreve a parceria entre a Braze e a Movable Ink, uma plataforma de software baseada em nuvem que oferece aos profissionais de marketing digital uma maneira de criar experiências visuais atraentes, exclusivas e cativantes para os clientes."
page_type: partner
search_tag: Partner

---

# Movable Ink

> A [Movable Ink](https://www.movableink.com/) é uma plataforma de software baseada em nuvem que oferece aos profissionais de marketing digital uma maneira de criar experiências visuais atraentes, exclusivas e cativantes para os clientes. A plataforma da Movable Ink oferece opções de personalização valiosas que podem ser facilmente inseridas nas suas Campaigns.

_Esta integração é mantida pela Movable Ink._

## Sobre a integração {#about-the-integration}

Expanda seus recursos criativos aproveitando os recursos do Intelligent Creative da Movable Ink, como enquetes, contagem regressiva e raspadinha. A integração entre a Movable Ink e a Braze oferece uma abordagem mais completa para mensagens dinâmicas orientadas por dados, fornecendo aos usuários elementos em tempo real sobre as coisas que importam.

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
|---|---|
| Conta da Movable Ink | É necessário ter uma conta da Movable Ink para usar essa parceria. |
| Fonte de dados | Você precisará conectar uma fonte de dados à Movable Ink. Isso pode ser feito por CSV, importação do site ou API. Passe os dados com um identificador unificador entre a Braze e a Movable Ink (por exemplo, `external_id`).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Casos de uso {#use-cases}

- Retrospectivas mensais ou de fim de ano personalizadas.
- Personalize dinamicamente as imagens para e-mail, push ou notificações Rich com base no último comportamento conhecido.<br>
	Por exemplo:
	- Usar uma mensagem push Rich para criar dinamicamente um cronograma de eventos por extração de dados da API.
	- Usar a contagem regressiva para notificar os usuários quando um grande período de vendas estiver prestes a começar (por exemplo, Black Friday, Dia dos Namorados ou ofertas de feriados)
	- Usar a raspadinha como uma forma divertida e interativa de distribuir códigos de promoção.

## Funcionalidades suportadas da Movable Ink {#supported-movable-ink-capabilities}

O Intelligent Creative tem muitas ofertas das quais os usuários da empresa podem tirar proveito. A lista a seguir mostra quais funcionalidades são compatíveis.

| Funcionalidade da Movable Ink | Recurso | Notificação Rich por push | Mensagens no app / Content Cards / E-mail | Informações |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| Otimizador criativo | Exibir conteúdo A/B | ✗ | ✔ | |
| Otimizar | ✗ | ✔* | * Requer a solução de deep linking da Branch |
| Regras de direcionamento | Data | ✔* | ✔ | * Suportada, mas não recomendada porque as notificações por push são armazenadas em cache após o recebimento e não são atualizadas |
| Dia da semana | ✔* | ✔ | * Suportada, mas não recomendada porque as notificações por push são armazenadas em cache após o recebimento e não são atualizadas |
| Hora do dia | ✔* | ✔ | * Suportada, mas não recomendada porque as notificações por push são armazenadas em cache após o recebimento e não são atualizadas |
| Histórias/Atividade de comportamento | | ✔* | ✔* | * O identificador de usuário exclusivo usado para a Braze precisa estar vinculado ao identificador do seu ESP |
| Deep linking no app | | ✔* | ✔* | * Para proporcionar uma experiência simplificada aos seus clientes, use uma solução de deep linking estabelecida via Branch ou uma solução validada com a equipe de experiência do cliente da Movable Ink. |
| Apps | Contagem regressiva | ✔* | ✔ | * Suportada, mas não recomendada porque as notificações por push são armazenadas em cache após o recebimento e não são atualizadas |
| Enquete | ✗ | ✔* | * Após a votação, o usuário sai do app e acessa uma landing page móvel |
| Raspadinha | ✔* | ✔* | * Ao clicar, o usuário sai do app e acessa a experiência da raspadinha |
| Vídeo | ✔* | ✔* | * Apenas GIFs animados, <br>Para Android, a Braze requer [suporte a GIF]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) na implementação |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Supported Movable Ink capabilities" }

## Integração {#integration}

### Etapa 1: crie uma fonte de dados para a Movable Ink {#step-1-create-a-data-source-for-movable-ink}

Os clientes precisarão criar uma fonte de dados que pode ser um CSV, importação de site ou integração de API.

![Diferentes opções de fonte de dados que serão exibidas: Upload de CSV, Site ou Integração de API.]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab CSV Data Source %}
- **Fonte de dados CSV**: Cada linha deve ter pelo menos uma coluna de segmento e uma coluna de conteúdo. Depois que seu CSV for enviado, selecione quais colunas devem ser usadas para direcionar o conteúdo. [Exemplo de arquivo CSV]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![Os campos que aparecerão ao selecionar "CSV" como sua fonte de dados.]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Website Data Source %}
- **Fonte de dados do site**: Cada linha deve ter pelo menos uma coluna de segmento e uma coluna de conteúdo. Após o upload do seu CSV, selecione quais colunas devem ser usadas para direcionamento do conteúdo.
  - Nesse processo, você precisará mapear:
    - Quais campos serão usados como segmentos
    - Quais campos você deseja como campos de dados que podem ser personalizados dinamicamente na criação (por exemplo: atributos do usuário ou atributos personalizados como nome, sobrenome, cidade, etc.)

![Os campos que aparecerão ao selecionar "Website" como sua fonte de dados.]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API Integrations %}
- **Integrações de API**: Use a API da sua empresa para alimentar o conteúdo diretamente de uma resposta de API.

![Os campos que aparecerão ao selecionar "Integração de API" como sua fonte de dados.]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### Etapa 2: crie uma campanha na plataforma da Movable Ink {#step-2-create-a-campaign-on-the-movable-ink-platform}

Na tela inicial da Movable Ink, crie uma campanha. Você pode selecionar entre e-mail a partir de HTML, e-mail a partir de imagem ou um bloco que pode ser usado em qualquer canal, incluindo push, mensagem no app e Content Cards (sugerido).

Sugerimos também que dê uma olhada nas várias opções de conteúdo disponíveis nos blocos.

![Uma imagem de como a plataforma Movable Ink se parece ao criar uma nova campanha Movable Ink.]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

A Movable Ink tem um editor fácil para você arrastar e soltar elementos como texto ou imagens. Se tiver preenchido sua fonte de dados, você poderá gerar dinamicamente uma imagem usando as propriedades de dados. Além disso, também é possível criar fallbacks dentro desse fluxo para os usuários caso a Campaign seja enviada a destinatários que não se enquadrem nos critérios de personalização.

![O editor de blocos da Movable Ink mostrando os diferentes elementos personalizáveis.]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

Antes de finalizar sua campanha, certifique-se de visualizar as imagens dinâmicas e testar os parâmetros de consulta para ver como as imagens aparecerão ao serem visualizadas. Quando concluído, uma URL dinâmica será gerada que pode ser inserida na Braze!

Para mais informações sobre como usar a plataforma Movable Ink, visite o [centro de suporte da Movable Ink](https://support.movableink.com/)

### Etapa 3: obtenha a URL do conteúdo da Movable Ink {#step-3-obtain-movable-ink-content-url}

Para incluir o conteúdo da Movable Ink nas mensagens da Braze, você precisa localizar a URL de origem que a Movable Ink forneceu a você.

Para obter a URL de origem, configure o conteúdo no dashboard da Movable Ink e, em seguida, finalize e exporte o conteúdo. Na página **Finish**, copie a URL de origem (`img src`) da tag de criativo.

![A página que aparece após você ter concluído sua campanha Movable Ink, aqui você encontra sua URL de conteúdo.]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

Em seguida, na plataforma da Braze, cole a URL no campo apropriado. Os campos apropriados para seu canal de envio de mensagens podem ser encontrados na etapa 4. Por fim, substitua todas as tags de mesclagem (como {% raw %}`&mi_u=%%email%%`{% endraw %}) pela variável Liquid correspondente (como {% raw %}`&mi_u={{${email_address}}}`{% endraw %}).

### Etapa 4: experiência da Braze {#step-4-braze-experience}

{% tabs local %}
{% tab Email %}
Na plataforma da Braze, cole sua tag criativa no corpo do seu e-mail.![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab Push notification %}

1. Na plataforma da Braze:
	- Push para Android: cole a URL nos campos **Push Icon Image** e **Expanded Notification Image**.<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- Push para iOS: cole a URL no campo de link **Media** e indique o formato de arquivo em uso.<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Push para a web: cole a URL nos campos **Push Icon Image** e **Large Notification Image**.<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. Para evitar que as imagens sejam armazenadas em cache, prefixe a URL na mensagem com tags Liquid vazias: <br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}

{% endtab %}
{% tab In-app message %}

1. Na plataforma da Braze, cole a URL no campo **Rich Notification Media**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Forneça uma URL exclusiva para evitar armazenamento em cache. Para garantir que as imagens em tempo real da Movable Ink funcionem e não sejam afetadas pelo armazenamento em cache, use o Liquid para acrescentar um registro de data e hora ao final da URL da imagem da Movable Ink.

Para fazer isso, use a sintaxe a seguir, substituindo a URL da imagem conforme necessário:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Esse modelo pega o horário atual (em segundos), anexa-o ao fim da guia da imagem da Movable Ink (como parâmetro de consulta) e depois calcula o resultado final. Você pode visualizá-lo com a guia **Test**&#8212;isso avaliará o código e mostrará uma prévia.

**3.** Por fim, reavalie a inscrição no segmento. Para fazer isso, ative a opção `Re-evaluate audience membership and liquid at send-time` localizada na etapa **Target Audiences** de uma Campaign. Se esta opção não estiver disponível, entre em contato com seu gerente de sucesso do cliente ou suporte da Braze. Esta opção instruirá os SDKs da Braze a solicitar novamente a Campaign, fornecendo uma URL única cada vez que uma mensagem no app for acionada.

{% endtab %}
{% tab Content Card %}

1. Na plataforma da Braze, cole a URL no campo **Rich Notification Media**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Para dispositivos móveis: as imagens dos Content Cards no iOS e no Android são armazenadas em cache após o recebimento e não são atualizadas.
  - Como solução alternativa, agende sua Campaign como mensagem recorrente diária, semanal ou mensal, com uma expiração correspondente, para que o Content Card seja recriado a partir do modelo. Por exemplo, um Content Card que deve ser atualizado uma vez por dia deve ser configurado como um envio programado diário com uma expiração de 1 dia.
3. Para garantir que as imagens em tempo real da Movable Ink funcionem e não sejam afetadas pelo armazenamento em cache quando o modelo do Content Card é atualizado, use o Liquid para acrescentar um registro de data e hora ao final da URL da imagem da Movable Ink.

Para fazer isso, use a sintaxe a seguir, substituindo a URL da imagem conforme necessário:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Esse modelo pega o horário atual (em segundos), anexa-o ao fim da guia da imagem da Movable Ink (como parâmetro de consulta) e depois calcula o resultado final. Você pode visualizá-lo com a guia **Test**, que avaliará o código e mostrará uma prévia.

{% endtab %}
{% endtabs %}

## Solução de problemas {#troubleshooting}

### As imagens dinâmicas não são exibidas corretamente? Você está tendo dificuldades com qual canal? {#dynamic-images-not-showing-correctly-what-channel-are-you-experiencing-difficulties-with}
- **Push**: confirme se você tem uma lógica vazia antes da URL da imagem da Movable Ink: <br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}
- **Mensagens no app e Content Cards**: confirme se a URL da imagem é exclusiva para cada impressão. Isso pode ser feito anexando o Liquid apropriado para que cada URL seja diferente. Veja [instruções de mensagens no app e Content Cards]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/#step-4-braze-experience).
- **A imagem não está carregando**: substitua quaisquer "tags de mesclagem" pelos campos Liquid correspondentes no dashboard da Braze. Por exemplo: {% raw %}`https://mi-msg.com/p/rp/image.png?mi_u=%%email%%`{% endraw %} por {% raw %}`https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}`{% endraw %}.

### Está tendo problemas para exibir GIFs no Android? {#having-trouble-showing-gifs-on-android}
- O Android requer suporte a GIFs na implementação. Siga o artigo de [personalização de mensagens no app para Android]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) se você não tiver essa configuração.


[1]: https://www.movableink.com/
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})