{% if include.location == "dnd" %}

1. **콘텐츠** > **Content Block**으로 이동합니다. <i class="fas fa-plus"></i> **Create Content Block**을 선택한 다음 **Drag-and-drop Content Block**을 선택합니다.
2. [편집기 블록]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks)을 끌어다 놓아 드래그 앤 드롭 콘텐츠 블록을 구축합니다.
3. **Rows** 탭에서 서식 블록을 편집기로 끌어다 놓아 콘텐츠 블록의 레이아웃을 만듭니다. <br><br> ![드래그 앤 드롭 콘텐츠 블록 작성기.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. 필요에 따라 드래그 앤 드롭 Content Blocks를 추가하여 이메일 캠페인을 구축합니다.
5. 콘텐츠 블록을 만든 후 **Done**을 선택합니다.
6. 콘텐츠 블록에 이름을 지정합니다. 이 이름은 **Content Block Liquid Tag**의 일부로 자동 입력됩니다.
7. (선택 사항) 설명을 추가합니다.
8. **미리보기** 탭을 선택하여 콘텐츠 블록이 어떻게 표시되는지 확인합니다. 필요에 따라 **Copy preview link**를 선택하여 임의의 사용자에게 이메일이 어떻게 보이는지 확인할 수 있는 공유 가능한 미리보기 링크를 생성하고 복사할 수 있습니다. 이 링크는 7일 동안 유효하며, 이후 다시 생성해야 합니다.<br><br> ![드래그 앤 드롭 콘텐츠 블록 작성기의 미리보기 탭.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. **Launch Content Block**을 선택합니다.

{% elsif include.location == "html" %}

1. **콘텐츠** > **Content Block**으로 이동합니다. <i class="fas fa-plus"></i> **Create Content Block**을 선택한 다음 **HTML code editor**를 선택합니다.
2. **HTML** 탭에서 HTML을 입력하거나 **Classic** 탭에서 콘텐츠 블록을 작성합니다. <br><br> ![HTML 코드 편집기 작성기.]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
3. 콘텐츠 블록을 만든 후 **Done**을 선택합니다.
4. 콘텐츠 블록의 이름을 입력합니다. 이 이름은 **Content Block Liquid Tag**의 일부로 자동 입력됩니다.
5. (선택 사항) 설명을 추가합니다.
6. **미리보기** 탭을 선택하여 콘텐츠 블록이 어떻게 표시되는지 확인합니다. 필요에 따라 **Copy preview link**를 선택하여 임의의 사용자에게 이메일이 어떻게 보이는지 확인할 수 있는 공유 가능한 미리보기 링크를 생성하고 복사할 수 있습니다. 이 링크는 7일 동안 유효하며, 이후 다시 생성해야 합니다.<br><br> ![HTML 코드 편집기 작성기의 미리보기 탭.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
7. **Launch Content Block**을 선택합니다.

{% endif %}