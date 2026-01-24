---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: МЭ Точная шина экспорта
    icon: extendedae:precise_export_bus
categories:
- extended devices
item_ids:
- extendedae:precise_export_bus
---

# МЭ Точная шина экспорта

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../structure/cable_precise_export_bus.snbt"></ImportStructure>
</GameScene>

МЭ Точная шина экспорта экспортирует предметы/жидкости в указанных количествах. Экспорт происходит только в том случае, если контейнер может полностью принять весь экспортируемый объем.

## Пример

![GUI](../pic/pre_bus_gui1.png)

Это означает экспорт 3 булыжников за операцию. Экспорт прекращается, когда количество булыжников в сети становится меньше 3.

![GUI](../pic/pre_bus_gui2.png)

Экспорт также прекращается, когда целевой контейнер не может вместить весь экспортированный объем. Теперь сундук может вместить только 2 булыжника, поэтому экспортная шина останавливается.
