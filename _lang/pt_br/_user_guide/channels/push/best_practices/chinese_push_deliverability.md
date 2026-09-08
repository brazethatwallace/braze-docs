---
nav_title: Entregabilidade para dispositivos Android chineses
article_title: Entregabilidade de push para dispositivos Android chineses
page_order: 10

page_type: reference
description: "Este artigo aborda nuances de entregabilidade de push que você deve conhecer ao direcionar usuários em dispositivos Android fabricados por OEMs chineses."
channel: push

---

# Entregabilidade de push para dispositivos Android chineses {#push-deliverability-for-chinese-android-devices}

> Alguns dispositivos Android fabricados por fabricantes de equipamentos originais (OEMs) chineses, como Xiaomi, OPPO, Vivo e Huawei, otimizam a duração da bateria por meio de um gerenciamento agressivo do ciclo de vida dos apps. Essa otimização pode ter a consequência indesejada de encerrar o processamento de apps em segundo plano, o que pode reduzir a entregabilidade das suas notificações por push.<br><br>Para garantir que o desempenho de envio de mensagens do seu app funcione como esperado nesses dispositivos, suas equipes de marketing e engenharia devem colaborar e seguir as etapas descritas neste artigo.

## Etapas para desenvolvedores {#steps-for-developers}
Esses OEMs realizam suas otimizações encerrando agressivamente aplicativos em segundo plano e impedindo que eles iniciem automaticamente para executar tarefas em segundo plano. Como desenvolvedor, você precisará configurar seu app para pedir ao usuário que alivie essas restrições sempre que possível.

Isso pode ser feito fazendo com que seu app inicie automaticamente no dispositivo do usuário final, o que dá ao app permissão para executar em segundo plano e escutar mensagens da Braze. Infelizmente, como esse é um problema específico de OEM e não do Android, não existem APIs documentadas para exibir o prompt de permissão de inicialização automática para cada OEM.

Para resolver isso, integre uma biblioteca como o [AutoStarter](https://github.com/judemanutd/AutoStarter) em sua aplicação. O AutoStarter oferece suporte a vários fabricantes, proporcionando uma maneira fácil de chamar o gerenciador de permissões de inicialização em uma ampla variedade de dispositivos. Depois de integrar o AutoStarter, chame `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` para abrir o gerenciador de permissões de inicialização no dispositivo do usuário final. Combine essa ação com um prompt incentivando o usuário final a ativar a "inicialização automática" para o seu app. Sua equipe de marketing vai criar essa mensagem — veja a próxima seção!

## Etapas para profissionais de marketing {#steps-for-marketers}
Depois que seus usuários optarem por receber notificações por push, há etapas adicionais que eles podem realizar para melhorar a entrega de mensagens nesses dispositivos. Recomendamos que você envie, após sua [mensagem de push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages), uma mensagem no app direcionada a usuários em dispositivos OEM chineses com estas etapas adicionais:

- Ativar o "início automático" para o app
- Desativar a otimização de bateria para o app

### Identificando usuários em dispositivos OEM chineses {#identifying-users-on-chinese-oem-devices}

Para direcionar sua mensagem no app a usuários em dispositivos OEM chineses específicos, use os [filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) **Device Model** ou **Device OS**:

- **Device Model:** Use esse filtro para direcionar usuários pelo modelo do celular. Por exemplo, para identificar dispositivos Huawei, use um padrão regex contendo `huawei` para corresponder aos nomes de modelo. Para instruções detalhadas de configuração, consulte [Criar uma regex de Device Model para dispositivos Huawei](#build-a-device-model-regex-for-huawei-devices).
- **Device OS:** Use esse filtro para direcionar usuários pelo sistema operacional. Alguns OEMs chineses, como a Huawei, podem especificar explicitamente sua versão personalizada do Android no campo de sistema operacional do dispositivo. Para etapas de verificação, consulte [Verificar valores de Device OS antes de direcionar](#verify-device-os-values-before-you-target).

#### Criar uma regex de Device Model para dispositivos Huawei {#build-a-device-model-regex-for-huawei-devices}

1. Acesse **Audience** > **Segments** e crie ou edite um Segment.
2. Adicione o filtro **Device Model**.
3. Defina o operador como **matches regex**.
4. Insira `huawei` para corresponder aos nomes de modelo Huawei.
5. (Opcional) Se você também quiser dispositivos da marca Honor, use `(huawei|honor)`.

Para saber mais sobre o comportamento de regex na Braze e sobre testes de padrão, consulte [Expressões regulares]({{site.baseurl}}/user_guide/audience/segments/regex).

#### Verificar valores de Device OS antes de direcionar {#verify-device-os-values-before-you-target}

Algumas variantes de OEM podem reportar nomes de sistema operacional personalizados nos metadados do dispositivo. Como esse valor pode variar por modelo de dispositivo e distribuição do Android, verifique o que seus usuários enviam na Braze antes de criar o Segment:

1. Acesse **Search Users** e abra o perfil de um usuário-alvo conhecido.
2. Na guia **Overview**, verifique **Recent devices** e revise o valor de sistema operacional exibido para aquele dispositivo.
3. Copie a string exata do sistema operacional no filtro do seu Segment:
   - Use **Device OS** quando precisar de uma correspondência exata ou baseada em regex da string do sistema operacional.
   - Use **Device OS Version Number** quando precisar de intervalos numéricos de versão.
4. No criador de Segments, use **User Lookup** para confirmar que os usuários teste correspondem conforme esperado.

Para saber mais sobre onde encontrar metadados de dispositivo nos perfis, consulte [Perfis de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Para saber mais sobre como testar a lógica de segmentação, consulte [Criar um Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).