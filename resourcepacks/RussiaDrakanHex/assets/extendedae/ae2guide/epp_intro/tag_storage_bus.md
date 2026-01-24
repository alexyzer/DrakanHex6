---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: МЭ Шина хранения по тегам
    icon: extendedae:tag_storage_bus
categories:
- extended devices
item_ids:
- extendedae:tag_storage_bus
---

# МЭ Шина хранения по тегам

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../structure/cable_tag_storage_bus.snbt"></ImportStructure>
</GameScene>

МЭ Шина хранения по тегам это <ItemLink id="ae2:storage_bus" /> который можно фильтровать по тегам предметов или жидкостей и который поддерживает некоторые базовые логические операторы.

Вот несколько примеров:

- Принимает только необработанную руду

c:raw_materials

- Принимает все слитки и драгоценные камни

c:ingots/* | c:gems/*

