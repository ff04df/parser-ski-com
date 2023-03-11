## parser-ski-com

Idea from https://www.fl.ru/projects/5119283/parsing-opisaniy-i-harakteristik-s-sayta.html

The parser of https://www.ski-com.ru

## Basic Information

* Consumes 3.6 Mbps, 0.56 MBps

* First of all check ***config.py***

* Parses all products in "Крепеж" and stores in excel file:

<table>
  <thead>
    <tr>
      <th>Название</th>
      <th>Информация</th>
      <th>Описание</th>
      <th>Кол-во модификаций</th>
      <th>Минимальная цена</th>
      <th>Ссылка</th>
    </tr>
  </thead>
    <tbody>
      <tr>
        <td><div dir="auto">product__title</div></td>
        <td><div dir="auto">product__min-text</div></td>
        <td><div dir="auto">item__desc</div></td>
        <td><div dir="auto">product__list-item</div></td>
        <td><div dir="auto">product__list-item--price</div></td>
        <td><div dir="auto">href</div></td>
      </tr>
    </tbody>
</table>
