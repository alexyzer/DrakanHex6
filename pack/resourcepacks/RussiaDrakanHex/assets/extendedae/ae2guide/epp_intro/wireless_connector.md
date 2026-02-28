---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: МЭ Беспроводной соединитель
    icon: extendedae:wireless_connect
categories:
- extended devices
item_ids:
- extendedae:wireless_connect
- extendedae:wireless_tool
---

# МЭ Беспроводной соединитель

<Row gap="20">
<BlockImage id="extendedae:wireless_connect" scale="6"></BlockImage>
<ItemImage id="extendedae:wireless_tool" scale="6"></ItemImage>
</Row>

МЭ Беспроводной соединитель может связать две сети, как  <ItemLink id="ae2:quantum_link" />, но с ограниченными расстояниями и нельзя пересекать измерения.

## Подключите беспроводные разъёмы

Нажмите на два беспроводных коннектора, которые вы хотите связать с помощью беспроводной инструмент настройки МЭ, после чего вы сможете их соединить.

Нажмите "Красться" + правую кнопку мыши чтобы очистить текущие настройки беспроводной инструмент настройки МЭ.

МЭ Беспроводной соединитель изменит текстуру после успешного установления связи.

Не привязанные Беспроводные соединители

<GameScene zoom="5" background="transparent">
  <ImportStructure src="../structure/wireless_connector_off.snbt"></ImportStructure>
</GameScene>

Связанные Беспроводные соединители

<GameScene zoom="5" background="transparent">
  <ImportStructure src="../structure/wireless_connector_on.snbt"></ImportStructure>
</GameScene>

## Цвет

Беспроводные разъемы могут быть окрашены так же, как и кабели, и соединять нужно только кабели/разъемы одного цвета.

Для окрашивания разъема вам потребуется <ItemLink id="ae2:color_applicator" />.

Таким образом, вы можете настроить свои беспроводные разъемы следующим образом:

<GameScene zoom="3" background="transparent" interactive={true}>
  <ImportStructure src="../structure/wireless_connector_setup.snbt"></ImportStructure>
</GameScene>


## Потребление энергии

МЭ Беспроводной соединитель потребляет больше энергии, когда они находятся дальше друг от друга. Кривая зависимости затрат от расстояния нелинейна, поэтому затраты энергии могут стать очень высокими, если они находятся слишком далеко друг от друга.

Вы можете использовать <ItemLink id="ae2:energy_card" /> для экономии энергии, каждая карта может снизить затраты энергии на 10%.

