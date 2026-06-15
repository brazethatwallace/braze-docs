---
nav_title: Bloquear dados personalizados
article_title: Bloquear dados personalizados
page_order: 3
page_type: reference
description: "Este artigo de referência explica como bloquear e excluir eventos personalizados e atributos personalizados na Braze."
---

# Bloquear dados personalizados {#blocklist-custom-data}

> Use o bloqueio para parar de rastrear dados personalizados que não são mais úteis. Use a exclusão para remover permanentemente eventos personalizados e atributos personalizados dos perfis de usuário após o bloqueio. Para pré-preenchimento, gerenciamento de propriedades e configuração de tipos de dados, consulte [Gerenciar dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/).

## Bloqueando dados personalizados {#blocklisting-custom-data}

Ocasionalmente, você pode identificar atributos personalizados, eventos personalizados ou eventos de compra que registram muitos pontos de dados, não são mais úteis para sua estratégia de marketing ou foram registrados por engano.

Para impedir que esses dados sejam enviados à Braze, você pode bloquear um objeto de dados personalizados enquanto sua equipe de engenharia trabalha para removê-lo do backend do seu app ou site. O bloqueio impede que um determinado objeto de dados personalizados seja registrado pela Braze dali em diante, o que significa que ele não aparecerá ao pesquisar um usuário específico.

### Escolhendo entre bloqueio e exclusão {#choosing-blocklisting-or-deletion}

- **Bloqueio** mantém os atributos personalizados, eventos ou compras existentes nos perfis de usuário, mas a Braze não processa mais novos dados para esses objetos.
- **Exclusão** remove esses dados dos perfis de usuário. Atributos personalizados e eventos excluídos são movidos para **Trashed** por sete dias, durante os quais você pode restaurá-los. Após sete dias, a Braze os exclui permanentemente. A exclusão não impede a chegada de novos dados, então confirme que seu SDK, API ou importações de CSV não estão mais enviando esses dados antes de excluir.

O bloqueio envia informações de bloqueio para o dispositivo de cada usuário e pode ser intensivo em dados. Bloquear um número muito grande de atributos, eventos ou compras (por exemplo, mais de 100) pode afetar o desempenho do app. Se você não planeja mais enviar esses dados à Braze, a exclusão geralmente é a melhor abordagem depois que você parar a integração de enviá-los.

Independentemente de você bloquear ou excluir, esses atributos personalizados, eventos e compras não aparecem mais na página **Gerenciar espaço de trabalho** e são removidos como filtros de segmento. Se você excluir dados personalizados, a Braze remove esses dados em nível de usuário dos perfis de acordo com [Como a exclusão funciona](#how-deletion-works).

Para bloquear dados personalizados, você precisa das [permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) listadas no menu suspenso a seguir para o seu espaço de trabalho.

{% details Permissões de usuário para bloqueio de dados personalizados %}

- Visualizar Campaigns
- Editar Campaigns
- Arquivar Campaigns
- Visualizar Canvas
- Editar Canvas
- Arquivar Canvas
- Visualizar regras do limite de frequência
- Editar regras do limite de frequência
- Visualizar priorização de mensagens
- Editar priorização de mensagens
- Visualizar Content Blocks
- Visualizar Feature Flags
- Editar Feature Flags
- Arquivar Feature Flags
- Visualizar Segments
- Editar Segments
- Visualizar modelos de IAM
- Editar modelos de IAM
- Arquivar modelos de IAM
- Visualizar modelos de e-mail
- Editar modelos de e-mail
- Arquivar modelos de e-mail
- Visualizar modelos de webhook
- Editar modelos de webhook
- Visualizar modelos de link
- Editar modelos de link
- Visualizar ativos da biblioteca de mídia
- Editar ativos da biblioteca de mídia
- Excluir ativos da biblioteca de mídia
- Visualizar locais
- Editar locais
- Arquivar locais
- Visualizar códigos de promoção
- Editar códigos de promoção
- Exportar códigos de promoção
- Visualizar centrais de preferências
- Editar centrais de preferências
- Visualizar relatórios
- Editar relatórios

{% enddetails %}

Os dados bloqueados não são enviados pelo SDK, e o dashboard da Braze não processa dados bloqueados de outras fontes (por exemplo, a API). No entanto, o bloqueio não remove dados dos perfis de usuário nem diminui retroativamente a quantidade de pontos de dados gerados por esse objeto de dados personalizados. Os dados bloqueados ficam ocultos, mas ainda podem ser usados para templates em Liquid.

### Bloqueando atributos personalizados, eventos personalizados e produtos {#blocklisting-custom-attributes-custom-events-and-products}

{% alert important %}
Quando um evento ou atributo é bloqueado, qualquer Segment, Campaign ou Canvas que use esse evento ou atributo é arquivado.
{% endalert %}

Para parar de rastrear um atributo personalizado, evento ou produto específico, siga estas etapas:

1. Pesquise na página **Atributos personalizados**, **Eventos personalizados** ou **Produtos**.
2. Selecione o atributo personalizado, evento ou produto. Para atributos personalizados e eventos, você pode selecionar até 100 para bloquear de uma vez.
3. Selecione **Blocklist**.

![Vários atributos personalizados selecionados que estão bloqueados na página de Atributos personalizados.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Você pode bloquear até 300 atributos personalizados e 300 eventos personalizados. Para impedir a coleta de determinados atributos de dispositivo, consulte nosso [guia do SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection).

{% alert important %}
Atributos personalizados ou eventos personalizados com status **Trashed** contam para o limite de bloqueio até serem excluídos.
{% endalert %}

Quando um evento personalizado ou atributo é bloqueado, o seguinte se aplica:

- Nenhum dado enviado à Braze é processado, e eventos e atributos bloqueados não contam mais como pontos de dados
- Os dados existentes ficam indisponíveis, a menos que sejam reativados
- Eventos e atributos bloqueados não aparecem em filtros ou gráficos
- Referências a dados bloqueados em rascunhos de Canvas ativos são carregadas como valores inválidos, o que pode causar erros
- Qualquer coisa que use o evento ou atributo bloqueado é arquivada

Para isso, a Braze envia as informações de bloqueio para cada dispositivo. Isso é importante ao considerar o bloqueio de um grande número de eventos e atributos (centenas de milhares ou milhões), pois seria uma operação intensiva em dados.

### Considerações sobre o bloqueio {#considerations-for-blocklisting}

Bloquear um grande número de eventos e atributos é possível, mas não recomendável. Isso porque, cada vez que um evento é realizado ou um atributo é (potencialmente) enviado à Braze, esse evento ou atributo precisa ser verificado em toda a lista de bloqueio.

Até 300 itens são enviados ao SDK para bloqueio. Se você bloquear mais de 300 itens, esses dados são enviados pelo SDK. Se você não precisar usar o evento ou atributo no futuro, considere removê-lo do código do seu app na próxima versão. Alterações na lista de bloqueio podem levar alguns minutos para se propagar. Você pode reativar qualquer evento ou atributo bloqueado a qualquer momento.

## Excluindo dados personalizados {#deleting-custom-data}

Ao criar campanhas e segmentos direcionados, você pode descobrir que não precisa mais de um evento personalizado ou atributo personalizado. Por exemplo, se você usou um atributo personalizado específico como parte de uma campanha única, pode excluir esses dados após [bloqueá-los](#blocklisting-custom-attributes-custom-events-and-products) e remover suas referências do seu app. Você pode excluir qualquer tipo de dado (como strings, números e atributos personalizados aninhados).

{% alert important %}
Você precisa ser [administrador da Braze]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#admin) para excluir dados personalizados.
{% endalert %}

Para excluir um evento personalizado ou atributo personalizado, faça o seguinte:

1. Acesse **Configurações de dados** > **Atributos personalizados** ou **Eventos personalizados**, dependendo do tipo de dado que deseja excluir.
2. Vá até o dado personalizado e selecione <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Ações** > **Blocklist**.
3. Após o dado personalizado ter sido bloqueado por 7 dias, selecione <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Ações** > **Excluir**.

### Como a exclusão funciona {#how-deletion-works}

Quando você exclui dados personalizados, o seguinte ocorre:

- **Para atributos personalizados:** Remove permanentemente os dados do atributo do perfil de cada usuário.
- **Para eventos personalizados:** Remove permanentemente os metadados do evento do perfil de cada usuário.

Quando um atributo ou evento é selecionado para exclusão, seu status é alterado para **Trashed**. Nos próximos sete dias, é possível restaurar o atributo ou evento. Se você não restaurá-lo após sete dias, os dados são excluídos permanentemente. Se você restaurar o atributo ou evento, ele volta ao estado de bloqueado.

A exclusão não impede o registro adicional dos objetos de dados personalizados nos perfis de usuário. Portanto, certifique-se de que os dados personalizados não estão mais sendo registrados antes de excluir o evento ou atributo.

### Informações importantes {#things-to-know}

Ao excluir dados personalizados, tenha em mente os seguintes detalhes:

* **A exclusão é permanente.** Os dados não podem ser recuperados.
* Os dados são removidos da plataforma Braze e dos perfis de usuário.
* Você pode "reutilizar" o nome do atributo personalizado ou do evento personalizado após a exclusão. Isso significa que, se você notar que dados personalizados "reaparecem" na Braze após a exclusão, isso pode ser causado por uma integração que não foi interrompida e está enviando dados com o mesmo nome de dado personalizado.
* Pode ser necessário bloquear um item novamente se a exclusão resultar no reaparecimento de dados personalizados. O status de bloqueio não é preservado porque os dados personalizados foram excluídos.
* A exclusão de dados personalizados não registra nenhum [ponto de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points/) e também não gera novos pontos de dados para uso.