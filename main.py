
import flet as ft


def main(page: ft.Page):

    #page.window_full_screen = True
    page.window_height = 720
    page.window_width = 420
    page.padding= ft.padding.only(top=30)
    page.vertical_alignment = "top"
    page.horizontal_alignment = "center"
    page.theme = ft.Theme(ft.colors.LIGHT_BLUE_500)
    page.appbar= ft.AppBar(
        leading=ft.Icon(ft.icons.CALCULATE_ROUNDED),
        leading_width=30,
        title=ft.Text("Estimate Calculator"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
    )
    inputWidth=130

    def calculate(e):
        wb = float(WeightBox.value)
        rb = float(RateBox.value)
        
        if wb and rb  > 0:
            try:
                amt = wb * rb
                AmountBox.value = ((float(labourBox.value)/100)*amt + amt)//1
                GstAmountBox.value =( (103/100)*float(AmountBox.value))//1
                page.update()

            except:
                pass    
            
    
    def clear(e):
        WeightBox.value,RateBox.value,labourBox.value,AmountBox.value,GstAmountBox.value='','','15','',''
        page.update()

    WeightBox= ft.TextField(suffix_text="gram",width=inputWidth,hint_text="Enter Weight",keyboard_type=ft.KeyboardType.NUMBER )
    RateBox = ft.TextField(prefix_icon=ft.icons.CURRENCY_RUPEE,width=inputWidth,hint_text="Enter Rate",keyboard_type=ft.KeyboardType.NUMBER )
    labourBox = ft.TextField(label="Labour Charge",suffix_icon=ft.icons.PERCENT,width=inputWidth*2+10,value="15")

    resultbtn = ft.FilledButton(text="Result" ,on_click=lambda e:calculate(e))
    clearbtn = ft.FloatingActionButton(text="clear",bgcolor="red",on_click=lambda e:clear(e))

    AmountBox = ft.TextField(value='',prefix_icon=ft.icons.CURRENCY_RUPEE,read_only=True,width=inputWidth*2+10,keyboard_type=ft.KeyboardType.NUMBER) 
    GstAmountBox = ft.TextField(value='',prefix_icon=ft.icons.CURRENCY_RUPEE,read_only=True,width=inputWidth*2+10,keyboard_type=ft.KeyboardType.NUMBER) 

    page.add(
        
        ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text('Weight'),
                            WeightBox,
                            
                        ]
                    ),
                    ft.Column(
                        controls=[
                            ft.Text('Rate'),
                            RateBox,
                           

                        ],
                    ),
                    
                ],
                alignment="center",
            )
        ),
        ft.Column(
            controls=[
                labourBox,
                resultbtn,

            ],
            alignment="center"
        ),
                    
        
        ft.Divider(color='transparent',height=40),
        ft.Column(
            controls=[
                ft.Text("Total Amount"),
                AmountBox,
                ft.Text("Total Amount With 3% GST"),
                GstAmountBox
            ]
        ),
        clearbtn
    )
    page.update()
ft.app(main)
