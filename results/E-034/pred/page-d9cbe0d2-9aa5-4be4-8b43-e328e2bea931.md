动力节点 POWER NODE

□□相传的IT黄埔军校

yield x+y;
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

case Line, Rectangle, Shape 在代码块执行多条语句，或者箭头->表达式。

1.2.3 Text Block

Text Block 处理多行文本十分方便，省时省力。无需连接 "+", 单引号，换行符等。Java 15, 参考 IEP 378.

1.2.3.1 认识文本块

语法：使用三个双引号字符括起来的字符串.

"""

内容

"""

例如：

String name = """lisi"""; //Error 不能将文本块放在单行上

String name="lisi

20""; //Error 文本块的内容不能在没有中间行结束符的情况下跟随三

个开头双引号

String myname=""

zhangsan

20

"""; //正确

www.bjpowermode.com

13 / 200

Copyright©动力节点
