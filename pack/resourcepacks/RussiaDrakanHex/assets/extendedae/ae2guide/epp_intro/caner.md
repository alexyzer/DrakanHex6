---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: МЭ Наполнитель
    icon: extendedae:caner
categories:
- extended devices
item_ids:
- extendedae:caner
---

# МЭ Наполнитель

<BlockImage id="extendedae:caner" scale="8"></BlockImage>

МЭ Наполнитель это машина, которая "консервирует" различные вещества, включая жидкости, Mekanism газ, ману Ботании и даже энергию!

Первый слот предназначен для заполнения, а второй — для заполнения.

Для работы ему требуется энергия, и каждая операция стоит 80 AU.

![GUI](../pic/caner_gui.png)

По умолчанию он заполняет только жидкости, для заполнения других объектов необходимо установить соответствующее дополнение.

### Поддержка аддонов:
- Applied Flux
- Applied Mekanistics
- Applied Botanics Addon

## Автокрафт с МЭ Наполнитель

Только верхняя и нижняя стороны могут принимать энергию и подключаться к сети.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../structure/caner_example.snbt"></ImportStructure>
</GameScene>

Простая настройка для МЭ Наполнитель. Наполнитель автоматически извлекает наполненный предмет, когда принимает ингредиенты из <ItemLink id="ae2:pattern_provider" />.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../structure/caner_auto.snbt"></ImportStructure>
</GameScene>

Схема должна содержать только материал для заполнения и сам контейнер, который нужно заполнить. Вот несколько примеров:

Наполните ведро водой:

![P1](../pic/fill_water.png)

Заполнить Энергетическую таблетку (необходимо установить Applied Flux):

![P1](../pic/fill_energy.png)


## Распоковать

МЭ Наполнитель также может опорожнять контейнер в пустом режиме. Для этого необходимо поочередно переключать входы и выходы.
