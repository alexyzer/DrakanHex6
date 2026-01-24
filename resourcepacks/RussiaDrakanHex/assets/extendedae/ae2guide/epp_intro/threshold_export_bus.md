---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: МЭ Пороговая шина экспорта
    icon: extendedae:threshold_export_bus
categories:
- extended devices
item_ids:
- extendedae:threshold_export_bus
---

# МЭ Пороговая шина экспорта

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../structure/cable_threshold_export_bus.snbt"></ImportStructure>
</GameScene>

МЭ Пороговая шина экспорта работает когда количество предметов, хранящегося в сети МЭ, превышает/ниже порогового значения.

## Пример

![GUI](../pic/thr_bus_gui1.png)

Пороговое значение для меди установлено на уровне 128, поэтому экспорт меди начинается, когда количество меди, хранящейся в сети, превышает 128.

![GUI](../pic/thr_bus_gui2.png)

Пороговое значение такое же, как указано выше, но режим установлен на «НИЖЕ». Экспорт меди начинается, когда уровень запасов меди ниже 128.