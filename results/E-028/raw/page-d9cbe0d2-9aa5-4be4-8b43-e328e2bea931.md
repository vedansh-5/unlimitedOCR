<|det|>header [190, 19, 305, 50]<|/det|>动力节点 POWER NODE
<|det|>header [673, 26, 863, 42]<|/det|>□□相传的IT黄埔军校
<|det|>text [85, 85, 789, 321]<|/det|>yield x+y;
}
case Rectangle(int w, int h) -> w * h;
case Shape(int w, int h) -> {
    System.out.println("这是图形，要计算周长");
    yield 2*(w + h);
}
default -> throw new IllegalArgumentException("无效的对象：" + obj);
};
System.out.println("result = " + result);
}
<|det|>text [85, 339, 625, 355]<|/det|>case Line, Rectangle, Shape 在代码块执行多条语句，或者箭头->表达式。
<|det|>title [87, 400, 287, 419]<|/det|>1.2.3 Text Block
<|det|>text [85, 440, 825, 457]<|/det|>Text Block 处理多行文本十分方便，省时省力。无需连接 "+", 单引号，换行符等。Java 15, 参考 IEP 378.
<|det|>title [87, 481, 315, 502]<|/det|>1.2.3.1 认识文本块
<|det|>text [86, 520, 415, 535]<|/det|>语法：使用三个双引号字符括起来的字符串.
<|det|>text [87, 537, 125, 546]<|/det|>"""
<|det|>text [88, 557, 133, 574]<|/det|>内容
<|det|>text [88, 576, 123, 585]<|/det|>"""
<|det|>text [87, 637, 131, 651]<|/det|>例如：
<|det|>text [85, 654, 659, 671]<|/det|>String name = """lisi"""; //Error 不能将文本块放在单行上
<|det|>text [87, 673, 294, 690]<|/det|>String name="lisi
<|det|>text [247, 692, 911, 710]<|/det|>20""; //Error 文本块的内容不能在没有中间行结束符的情况下跟随三
<|det|>text [88, 712, 212, 730]<|/det|>个开头双引号
<|det|>text [87, 751, 273, 768]<|/det|>String myname=""
<|det|>text [128, 772, 213, 787]<|/det|>zhangsan
<|det|>text [128, 791, 153, 805]<|/det|>20
<|det|>text [128, 808, 253, 826]<|/det|>"""; //正确
<|det|>footer [87, 898, 319, 916]<|/det|>www.bjpowermode.com
<|det|>page_number [477, 900, 536, 913]<|/det|>13 / 200
<|det|>footer [658, 899, 810, 915]<|/det|>Copyright©动力节点
