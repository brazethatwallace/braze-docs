---
nav_title: Diretrizes da marca
article_title: Diretrizes da marca
page_order: 1
page_type: reference
description: "Este artigo de referência descreve como criar, gerenciar e usar diretrizes da marca que o Operator aplica ao gerar textos, modelos e imagens."
---

# Diretrizes da marca {#brand-guidelines}

> Adapte o estilo do seu texto gerado por IA para que corresponda à voz, ao tom e à personalidade da sua marca com diretrizes personalizadas da marca.

Crie e gerencie as diretrizes da marca acessando **Conteúdo** > **Diretrizes da marca**.

## Criação de diretrizes da marca {#creating-brand-guidelines}

### Etapa 1: Crie uma diretriz da marca {#step-1-create-a-brand-guideline}

Na página **Diretrizes da marca**, selecione **Criar nova**. Se quiser que essa diretriz da marca seja a padrão para o espaço de trabalho, marque **Usar como diretriz padrão da marca**. Você pode ter uma padrão por espaço de trabalho.

### Etapa 2: Descreva a personalidade da sua marca {#step-2-describe-your-brand-personality}

Para **Personalidade da marca**, pense no que torna sua marca única. Inclua características, valores, voz e quaisquer arquétipos que definam sua marca. Aqui estão algumas características a serem consideradas:

| **Característica**       | **Definição**                                                                       | **Exemplo**                                                        |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputação               | Como você quer que sua marca seja percebida no mercado.                               | Somos conhecidos por ser a marca mais confiável e focada no cliente em nosso setor. |
| Traços de personalidade  | Características humanas que descrevem o caráter da sua marca.                        | Nossa marca é amigável, acessível e sempre otimista.             |
| Valores                  | Valores essenciais que orientam as ações e decisões da sua marca.                    | Valorizamos sustentabilidade, transparência e comunidade.        |
| Diferenciação            | Qualidades únicas que diferenciam sua marca dos concorrentes.                        | Nos destacamos por oferecer um atendimento ao cliente personalizado que vai além do esperado. |
| Voz da marca             | O tom e o estilo de comunicação que sua marca utiliza.                                | Nossa voz é casual, mas informativa, garantindo clareza sem ser formal demais. |
| Arquétipo da marca       | O arquétipo que representa a persona da sua marca (O Herói, O Criador, e assim por diante). | Incorporamos o arquétipo do "Explorador", sempre buscando novos desafios e aventuras. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 2: Descreva a personalidade da sua marca" }

### Etapa 3: Defina a linguagem que deve ser evitada (opcional) {#step-3-define-language-that-should-be-avoided-optional}

Para **Exclusões**, liste qualquer linguagem ou estilo que não esteja alinhado com sua marca. Por exemplo, você pode querer evitar "sarcasmo", "atitudes negativas" ou tons "condescendentes".

![A janela "Criar diretriz da marca" com campos para inserir o nome, a descrição, a personalidade, as exclusões e o tom.]({% image_buster /assets/img/guidelines_create.png %})

### Etapa 4: Teste suas diretrizes {#step-4-test-your-guidelines}

Teste suas diretrizes para ver como elas funcionam. Expanda **Teste suas diretrizes** para gerar um texto de exemplo e ajuste conforme necessário.

### Etapa 5: Salve suas diretrizes {#step-5-save-your-guidelines}

Quando estiver satisfeito com suas diretrizes, selecione **Salvar diretriz da marca**. Suas diretrizes serão salvas no seu espaço de trabalho para uso futuro.

{% alert important %}
Você pode alterar o idioma de saída independentemente do idioma do seu texto, mas nem a Braze nem a OpenAI garantem a qualidade da tradução. Sempre teste e verifique as traduções antes de usá-las.
{% endalert %}

## Gerenciamento de diretrizes da marca {#managing-brand-guidelines}

Você pode editar as diretrizes da marca selecionando-as na página **Diretrizes da marca**. Arquive uma diretriz da marca para torná-la inativa e indisponível nos criadores de mensagens. Para torná-la ativa e selecionável novamente, você pode filtrar por diretrizes da marca arquivadas e então desarquivá-la.

## Uso de diretrizes da marca {#using-brand-guidelines}

Ao redigir uma mensagem, abra o Operator para [gerar textos]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy) e selecione sua diretriz da marca no menu suspenso **Aplicar diretriz da marca**. Se você designar uma diretriz da marca específica como padrão, a Braze a seleciona automaticamente no menu suspenso, mas você pode escolher uma diretriz diferente.

![Operator com "Important Alerts!!" selecionado como diretriz da marca.]({% image_buster /assets/img/guidelines_ai_assistant.png %})

{% multi_lang_include brazeai/generative_ai/policy.md %}