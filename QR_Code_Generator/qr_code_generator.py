#pip install qrcode
#pip install Pillow -> for images and colours


import qrcode
class MyQR:
    def __init__(self, size: int, padding:int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qr(self, file_name: str, fg: str, bg:str ):   #fq -> foreground colour , bg -> background
        user_input: str = input("Enter some text:  -->  ")
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f'Successfully creater {file_name}')
        except Exception as e:
            print(f'Error {e}')   #limited only to 7000 chars


def main():
    myqr =MyQR(size=50, padding=1)
    myqr.create_qr("sample.png", fg = "blue", bg="yellow")


if __name__ == "__main__":
    main()