import ugfx
import time
import dialogs
import urequests

def post_post(pushed):
  if(pushed):
    nick = dialogs.prompt_text("Please enter name")
    if nick:
      print(nick)
      response = urequests.post("http://127.0.0.1:3000/posts", data = "some dummy content")
      print(response)

ugfx.init()
1
ugfx.clear(ugfx.BLACK)

ugfx.fill_circle(60, 60, 50, ugfx.WHITE);
ugfx.fill_circle(60, 60, 40, ugfx.BLACK);
ugfx.fill_circle(60, 60, 30, ugfx.WHITE);
ugfx.fill_circle(60, 60, 20, ugfx.BLACK);
ugfx.fill_circle(60, 60, 10, ugfx.WHITE);

ugfx.thickline(1,1,100,100,ugfx.WHITE,10,5)
ugfx.box(30,30,50,50,ugfx.WHITE)

ugfx.string(150,25,"🦋 🐌 🐚 🐞 🐜 🕷 🕸 🐢 🐍 🦎 🦂 🦀 🦑 🐙 🦐 🐠 🐟 🐡 ","Roboto_BlackItalic24",ugfx.WHITE)

ugfx.flush()

def render(text, pushed):
    if(pushed):
        ugfx.string(100,10,text,"PermanentMarker22",ugfx.WHITE)
    else:
        ugfx.string(100,10,text,"PermanentMarker22",ugfx.BLACK)
    ugfx.flush()

def start_app(pushed):
    if(pushed):
        import launcher

ugfx.input_init()
ugfx.input_attach(ugfx.BTN_A, post_post)
ugfx.input_attach(ugfx.JOY_DOWN, lambda pressed: render('DOWN', pressed))
ugfx.input_attach(ugfx.JOY_LEFT, lambda pressed: render('LEFT', pressed))
ugfx.input_attach(ugfx.JOY_RIGHT, lambda pressed: render('RIGHT', pressed))
ugfx.input_attach(ugfx.BTN_B, lambda pressed: render('B', pressed))
ugfx.input_attach(ugfx.BTN_START, start_app)
ugfx.input_attach(ugfx.BTN_SELECT, lambda pressed: render('Select', pressed))

while True:
    pass
